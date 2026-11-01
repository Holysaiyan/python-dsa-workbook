"""Build workbook/lessons.js from the lesson sources.

Every code example is run in CPython and its output recorded. Every practice solution is checked
against its tests, every starter is checked to fail them, every buggy variant is checked to fail
at least one visible test, and every quiz output question is answered by running its code.
The build fails if any of that is wrong, so the published lesson data is always verified.
"""
import json, os, subprocess, sys, tempfile, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from extras import EXTRAS
from extras_more import EXTRAS_MORE
EXTRAS.update(EXTRAS_MORE)
OUT = os.path.join(HERE, "..", "workbook", "lessons.js")

HARNESS = r'''
import json as __json
def __norm(x):
    if isinstance(x, tuple):
        x = list(x)
    if isinstance(x, list):
        return [__norm(i) for i in x]
    if isinstance(x, dict):
        return {str(k): __norm(v) for k, v in x.items()}
    return x
def __arg(a):
    if isinstance(a, dict) and "__py__" in a:
        return eval(a["__py__"])
    return a
__CALL_LINE__
__out = []
for __t in __json.loads(__TESTS__):
    try:
        if __call is None:
            raise NameError("define a function called __FUNC__")
        __got = __norm(__call(*[__arg(a) for a in __t["args"]]))
        __exp = __t["expected"]
        __ok = (__got == __exp) and (isinstance(__got, bool) == isinstance(__exp, bool))
        if __t.get("unordered") and isinstance(__got, list) and isinstance(__exp, list):
            __ok = sorted(map(str, __got)) == sorted(map(str, __exp))
        try:
            __gs = __json.dumps(__got)
        except Exception:
            __gs = repr(__got)
        __out.append({"ok": __ok, "got": __gs})
    except Exception as __e:
        __out.append({"ok": False, "error": type(__e).__name__ + ": " + str(__e)})
print("@@RESULTS@@" + __json.dumps(__out))
'''


def harness_for(practice, tests_json):
    if practice.get("wrapper"):
        call_line = practice["wrapper"]
    else:
        call_line = "__call = globals().get(%r)" % practice["func"]
    h = HARNESS.replace("__CALL_LINE__", call_line).replace("__FUNC__", practice["func"])
    return h.replace("__TESTS__", json.dumps(json.dumps(tests_json)))


def run(code, timeout=30):
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(code)
        path = f.name
    env = dict(os.environ, PYTHONHASHSEED="0")
    try:
        p = subprocess.run([sys.executable, "-I", path], capture_output=True, text=True, timeout=timeout, env=env, stdin=subprocess.DEVNULL)
    finally:
        os.unlink(path)
    return p.returncode, p.stdout, p.stderr


def main():
    modules = []
    problems = []
    for name in ["m0", "m1", "m2", "m3", "m4", "m5", "m6", "m7"]:
        m = importlib.import_module(name)
        mod = {"id": m.MODULE["id"], "title": m.MODULE["title"], "lessons": [], "n": m.MODULE.get("n") or str(len([x for x in modules if not x["n"].isalpha()]) + 1)}
        for L in m.LESSONS:
            blocks = []
            for b in L["blocks"]:
                kind = b[0]
                if kind == "code":
                    rc, out, err = run(b[1])
                    if rc != 0:
                        problems.append(f"{L['id']}: example failed\n{b[1]}\n{err}")
                    blocks.append({"t": "code", "code": b[1], "out": out})
                elif kind == "table":
                    blocks.append({"t": "table", "head": b[1], "rows": b[2]})
                elif kind in ("steps",):
                    blocks.append({"t": "steps", "items": b[1]})
                else:
                    blocks.append({"t": kind, "html": b[1]})
            lesson = {k: L[k] for k in ("id", "title", "minutes", "tags", "summary", "mistakes")}
            if mod["n"].isalpha():
                lesson["n"] = mod["n"] + str(len(mod["lessons"]) + 1)
            else:
                lesson["n"] = str(1 + sum(len(x["lessons"]) for x in modules if not x["n"].isalpha()) + len(mod["lessons"]))
            lesson["blocks"] = blocks
            lesson["related"] = [{"title": t, "url": u} for t, u in L.get("related", [])]
            X = EXTRAS.get(L["id"], {})
            # quiz: run any code question, fill "@run", check distractors differ
            quiz = []
            for qi, q in enumerate(X.get("quiz", [])):
                item = {"q": q["q"], "options": list(q["options"]), "why": q["why"], "code": q.get("code")}
                if q.get("code"):
                    rc, out, err = run(q["code"])
                    if rc != 0:
                        problems.append(f"{L['id']} quiz {qi}: code failed\n{err}")
                        continue
                    actual = out.strip()
                    if "@run" in item["options"]:
                        item["out"] = out
                        item["answer"] = item["options"].index("@run")
                        item["options"][item["answer"]] = actual
                        for oi, o in enumerate(item["options"]):
                            if oi != item["answer"] and o.strip() == actual:
                                problems.append(f"{L['id']} quiz {qi}: distractor equals the real output {actual!r}")
                    else:
                        item["answer"] = q["answer"]   # a conceptual question about the code; it must still run cleanly
                else:
                    item["answer"] = q["answer"]
                if not (0 <= item["answer"] < len(item["options"])) or len(item["options"]) < 2:
                    problems.append(f"{L['id']} quiz {qi}: bad options/answer")
                quiz.append(item)
            lesson["quiz"] = quiz
            lesson["limit"] = X.get("limit")
            lesson["complexity"] = X.get("complexity")
            if lesson["complexity"]:
                c = lesson["complexity"]
                for key in ("time", "space"):
                    opts = [o.split(" ")[0] if o.startswith("O(") and ") " in o else o for o in c[key + "_options"]]
                    # accepted answers must appear among the options (options may carry a label after the notation)
                    for acc in c[key]:
                        if not any(o == acc or o.startswith(acc + " ") for o in c[key + "_options"]):
                            problems.append(f"{L['id']} complexity {key}: accepted {acc!r} not in options {c[key + '_options']}")
            lesson["debug"] = None
            P = L.get("practice")
            if P:
                # expected values from the reference solution
                tests = [{"label": lab, "args": args, "hidden": hid} for lab, args, hid in P["tests"]]
                probe = [{"args": t["args"], "expected": None} for t in tests]
                getter = P["solution"] + "\n" + (P.get("wrapper") or f"__call = {P['func']}") + "\nimport json\ndef _arg(a):\n    return eval(a['__py__']) if isinstance(a, dict) and '__py__' in a else a\nprint(json.dumps([__call(*[_arg(a) for a in t['args']]) for t in json.loads(%r)]))\n" % json.dumps(probe)
                rc, out, err = run(getter)
                if rc != 0:
                    problems.append(f"{L['id']}: solution crashed\n{err}")
                    continue
                expected = json.loads(out.strip().splitlines()[-1])
                for t, e in zip(tests, expected):
                    t["expected"] = e
                # verify through the real harness
                rc, out, err = run(P["solution"] + "\n" + harness_for(P, tests))
                res = json.loads(out.split("@@RESULTS@@")[-1])
                if not all(r["ok"] for r in res):
                    problems.append(f"{L['id']}: solution fails harness {res}")
                # the starter must not pass everything
                rc, out, err = run(P["starter"] + "\n" + harness_for(P, tests))
                res = json.loads(out.split("@@RESULTS@@")[-1])
                if all(r["ok"] for r in res):
                    problems.append(f"{L['id']}: starter passes all tests")
                lesson["practice"] = {
                    "title": P["title"], "prompt": P["prompt"], "func": P["func"],
                    "starter": P["starter"], "wrapper": P.get("wrapper"),
                    "tests": tests, "hints": P["hints"], "solution": P["solution"],
                    "explain": P["explain"],
                }
                DB = X.get("debug")
                if DB:
                    dtests = [dict(t) for t in tests]
                    if DB.get("extra_tests"):
                        extra = [{"label": lab, "args": args, "hidden": hid} for lab, args, hid in DB["extra_tests"]]
                        probe = [{"args": t["args"], "expected": None} for t in extra]
                        rc, out, err = run(P["solution"] + "\n" + (P.get("wrapper") or f"__call = {P['func']}") + "\nimport json\ndef _arg(a):\n    return eval(a['__py__']) if isinstance(a, dict) and '__py__' in a else a\nprint(json.dumps([__call(*[_arg(a) for a in t['args']]) for t in json.loads(%r)]))\n" % json.dumps(probe))
                        if rc != 0:
                            problems.append(f"{L['id']}: solution crashed on debug extra tests\n{err}")
                        else:
                            for t, e in zip(extra, json.loads(out.strip().splitlines()[-1])):
                                t["expected"] = e
                            dtests += extra
                    # the buggy starter must fail at least one test and must not hang
                    try:
                        rc, out, err = run(DB["starter"] + "\n" + harness_for(P, dtests), timeout=20)
                        parts = out.split("@@RESULTS@@")
                        if len(parts) < 2:
                            problems.append(f"{L['id']}: buggy starter crashed before tests ran\n{err[-400:]}")
                        else:
                            res = json.loads(parts[-1])
                            if all(r["ok"] for r in res):
                                problems.append(f"{L['id']}: buggy starter passes every test")
                            if not any(r["ok"] for r in res):
                                print(f"note: {L['id']} buggy starter fails every test")
                            if not any((not r["ok"]) and not t["hidden"] for r, t in zip(res, dtests)):
                                # a debug exercise must show at least one failing case: unhide the first
                                for r, t in zip(res, dtests):
                                    if not r["ok"]:
                                        t["hidden"] = False
                                        break
                    except subprocess.TimeoutExpired:
                        problems.append(f"{L['id']}: buggy starter hangs")
                    # the reference solution must pass the debug tests too
                    rc, out, err = run(P["solution"] + "\n" + harness_for(P, dtests))
                    if not all(r["ok"] for r in json.loads(out.split("@@RESULTS@@")[-1])):
                        problems.append(f"{L['id']}: solution fails debug tests")
                    lesson["debug"] = {"intro": DB["intro"], "starter": DB["starter"], "hint": DB["hint"], "tests": dtests}
            else:
                lesson["practice"] = None
            mod["lessons"].append(lesson)
        modules.append(mod)

    # house style: no em dashes anywhere
    blob = json.dumps(modules, ensure_ascii=False)
    if "—" in blob or "&mdash;" in blob:
        problems.append("em dash found")
    known = {L["id"] for m in modules for L in m["lessons"]}
    for k in EXTRAS:
        if k not in known:
            problems.append(f"extras for unknown lesson {k}")
    for m in modules:
        for L in m["lessons"]:
            if L["practice"] and not L["debug"]:
                problems.append(f"{L['id']}: practice without a debug exercise")
            if L["practice"] and not L["complexity"]:
                problems.append(f"{L['id']}: practice without a complexity gate")
            if not L["quiz"]:
                problems.append(f"{L['id']}: no quiz")

    if problems:
        print("\n\n".join(problems))
        sys.exit(1)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        f.write("window.DSA = " + json.dumps({"modules": modules, "harness": HARNESS}, ensure_ascii=False) + ";\n")
    n = sum(len(m["lessons"]) for m in modules)
    print(f"ok: {n} lessons, {os.path.getsize(OUT)//1024} KB")


if __name__ == "__main__":
    main()
