"""Generate the course home page (index.html) from workbook/lessons.js, so the syllabus never drifts from the lessons."""
import json, pathlib, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "workbook" / "lessons.js").read_text()[len("window.DSA = "):].rstrip().rstrip(";"))
modules = data["modules"]
lessons = [L for m in modules for L in m["lessons"]]
n_lessons = len(lessons)
n_practice = sum(1 for L in lessons if L["practice"])
n_quiz = sum(len(L["quiz"]) for L in lessons)
n_examples = sum(1 for L in lessons for b in L["blocks"] if b["t"] == "code")
minutes = sum(L["minutes"] for L in lessons)
hours = round(minutes / 60)

def e(s):
    return html.escape(str(s), quote=True)

syllabus = ""
for mi, m in enumerate(modules):
    rows = ""
    for L in m["lessons"]:
        rows += f'<li><a href="workbook/#{e(L["id"])}"><span class="ls-title">{e(L["title"])}</span><span class="ls-meta">{L["minutes"]} min</span></a></li>'
    syllabus += f'<section class="module"><div class="module-head"><span class="module-n">{e(m["n"])}</span><h3>{e(m["title"])}</h3></div><ol class="lesson-list">{rows}</ol></section>'

page = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Python DSA Workbook</title>
<meta name="description" content="A free, interactive Python data structures and algorithms course built for graduate coding assessments: {n_lessons} lessons, runnable examples, quizzes, bug-fixing drills and auto-tested practice problems.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=JetBrains+Mono:wght@400;600&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap">
<style>
:root {{
  --paper: #f4f6f9; --surface: #ffffff; --ink: #131b2a; --muted: #586277; --rule: #d9dfe8;
  --accent: #2148cc; --accent-ink: #ffffff; --accent-soft: #e5ebfb; --code-bg: #eef2f7; --code-ink: #1b2436;
  --ok: #1b7a4b; --ok-soft: #e2f3ea; --warn: #8d6100; --warn-soft: #fbf1db;
  --syn-kw: #8a2ca6; --syn-str: #0b7442; --syn-num: #b04f17; --syn-com: #7a8597; --syn-fn: #2148cc;
  --shadow: 0 1px 2px rgba(19, 27, 42, .06), 0 4px 14px rgba(19, 27, 42, .05);
  --f-display: "Bricolage Grotesque", "Segoe UI", system-ui, sans-serif;
  --f-body: "Source Sans 3", "Segoe UI", system-ui, -apple-system, sans-serif;
  --f-mono: "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
  color-scheme: light;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --paper: #0e131b; --surface: #151c27; --ink: #e5eaf2; --muted: #98a3b6; --rule: #273143;
    --accent: #86a6ff; --accent-ink: #0e131b; --accent-soft: #1b2847; --code-bg: #111823; --code-ink: #dce3ee;
    --ok: #52c58c; --ok-soft: #13291f; --warn: #e3b552; --warn-soft: #2e2512;
    --syn-kw: #d29cf3; --syn-str: #83d6a3; --syn-num: #f2a875; --syn-com: #7d899d; --syn-fn: #86a6ff;
    --shadow: 0 1px 2px rgba(0, 0, 0, .3), 0 4px 14px rgba(0, 0, 0, .25);
    color-scheme: dark;
  }}
}}
:root[data-theme="dark"] {{
  --paper: #0e131b; --surface: #151c27; --ink: #e5eaf2; --muted: #98a3b6; --rule: #273143;
  --accent: #86a6ff; --accent-ink: #0e131b; --accent-soft: #1b2847; --code-bg: #111823; --code-ink: #dce3ee;
  --ok: #52c58c; --ok-soft: #13291f; --warn: #e3b552; --warn-soft: #2e2512;
  --syn-kw: #d29cf3; --syn-str: #83d6a3; --syn-num: #f2a875; --syn-com: #7d899d; --syn-fn: #86a6ff;
  --shadow: 0 1px 2px rgba(0, 0, 0, .3), 0 4px 14px rgba(0, 0, 0, .25);
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
html {{ padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }}
body {{ margin: 0; background: var(--paper); color: var(--ink); font-family: var(--f-body); font-size: 17px; line-height: 1.6; }}
img {{ max-width: 100%; }}
a {{ color: var(--accent); text-underline-offset: 2px; }}
code {{ font-family: var(--f-mono); font-size: .86em; background: var(--code-bg); color: var(--code-ink); padding: .08em .35em; border-radius: 4px; }}
:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
.wrap {{ max-width: 980px; margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
.nav {{ display: flex; align-items: center; justify-content: space-between; gap: 12px; padding-block: 18px; }}
.brand {{ font-family: var(--f-display); font-weight: 700; font-size: 1.2rem; letter-spacing: -.01em; text-decoration: none; color: var(--ink); }}
.brand span {{ color: var(--accent); }}
.nav-links {{ display: flex; gap: 6px 18px; flex-wrap: wrap; font-size: .95rem; font-weight: 600; }}
.nav-links a {{ text-decoration: none; color: var(--muted); }}
.nav-links a:hover {{ color: var(--accent); }}
.btn {{ display: inline-block; border: 1px solid var(--rule); background: var(--surface); color: var(--ink); border-radius: 8px; padding: 9px 16px; font-weight: 700; text-decoration: none; font-size: 1rem; }}
.btn.primary {{ background: var(--accent); color: var(--accent-ink); border-color: var(--accent); }}
.btn:hover {{ filter: brightness(1.05); }}
.hero {{ display: grid; grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr); gap: 36px; align-items: center; padding-block: 36px 48px; }}
.eyebrow {{ font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); font-weight: 700; margin: 0 0 12px; }}
h1 {{ font-family: var(--f-display); font-weight: 700; font-size: clamp(2.2rem, 5vw, 3.4rem); line-height: 1.02; letter-spacing: -.025em; margin: 0 0 16px; text-wrap: balance; }}
.lede {{ font-size: 1.2rem; color: var(--muted); margin: 0 0 24px; max-width: 54ch; }}
.ctas {{ display: flex; gap: 10px; flex-wrap: wrap; }}
.stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(105px, 1fr)); gap: 10px; margin-top: 28px; }}
.stat {{ border: 1px solid var(--rule); border-radius: 10px; padding: 10px 12px; background: var(--surface); }}
.stat b {{ display: block; font-family: var(--f-display); font-size: 1.5rem; line-height: 1.1; font-variant-numeric: tabular-nums; }}
.stat span {{ font-size: .82rem; color: var(--muted); }}
.demo {{ border: 1px solid var(--rule); border-radius: 12px; background: var(--surface); box-shadow: var(--shadow); overflow: hidden; }}
.demo-head {{ display: flex; justify-content: space-between; align-items: center; padding: 8px 10px 8px 14px; border-bottom: 1px solid var(--rule); }}
.demo-label {{ font-size: .74rem; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); font-weight: 700; }}
.demo-btn {{ font-size: .82rem; font-weight: 700; padding: 3px 10px; border-radius: 6px; background: var(--accent); color: var(--accent-ink); }}
.demo pre {{ margin: 0; padding: 12px 14px; font-family: var(--f-mono); font-size: 13.5px; line-height: 1.6; background: var(--code-bg); color: var(--code-ink); white-space: pre; overflow-x: auto; }}
.demo-out {{ padding: 10px 14px; font-family: var(--f-mono); font-size: 13px; border-top: 1px solid var(--rule); }}
.demo-out b {{ display: block; font-family: var(--f-body); font-size: .7rem; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); font-weight: 700; margin-bottom: 4px; }}
.tk-kw {{ color: var(--syn-kw); font-weight: 600; }} .tk-str {{ color: var(--syn-str); }} .tk-num {{ color: var(--syn-num); }} .tk-com {{ color: var(--syn-com); font-style: italic; }} .tk-fn {{ color: var(--syn-fn); }}
.demo-tests {{ list-style: none; margin: 0; padding: 10px 14px; display: grid; gap: 4px; border-top: 1px solid var(--rule); font-size: .88rem; }}
.demo-tests li {{ display: flex; justify-content: space-between; gap: 8px; }}
.pill {{ font-size: .72rem; font-weight: 700; padding: 1px 8px; border-radius: 99px; }}
.pill.ok {{ background: var(--ok-soft); color: var(--ok); }}
.pill.dim {{ background: var(--code-bg); color: var(--muted); }}
h2 {{ font-family: var(--f-display); font-weight: 600; font-size: clamp(1.5rem, 3vw, 1.9rem); line-height: 1.15; letter-spacing: -.015em; margin: 0 0 8px; text-wrap: balance; }}
.section {{ padding-block: 40px; border-top: 1px solid var(--rule); }}
.section > p.intro {{ margin: 0 0 22px; color: var(--muted); max-width: 64ch; }}
.steps {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 12px; counter-reset: s; }}
.step {{ border: 1px solid var(--rule); border-radius: 12px; padding: 14px 16px; background: var(--surface); counter-increment: s; display: grid; gap: 4px; align-content: start; }}
.step::before {{ content: counter(s); font-family: var(--f-mono); font-size: .8rem; font-weight: 600; color: var(--accent); background: var(--accent-soft); border-radius: 6px; width: 26px; height: 26px; display: grid; place-items: center; margin-bottom: 4px; }}
.step b {{ font-family: var(--f-display); font-weight: 600; font-size: 1.05rem; }}
.step span {{ font-size: .93rem; color: var(--muted); }}
.modules {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; }}
.module {{ border: 1px solid var(--rule); border-radius: 12px; background: var(--surface); overflow: hidden; }}
.module-head {{ display: flex; align-items: center; gap: 10px; padding: 12px 14px; border-bottom: 1px solid var(--rule); }}
.module-n {{ font-family: var(--f-mono); font-size: .8rem; font-weight: 600; color: var(--accent); background: var(--accent-soft); border-radius: 6px; width: 26px; height: 26px; display: grid; place-items: center; flex: none; }}
.module h3 {{ font-family: var(--f-display); font-weight: 600; font-size: 1.1rem; margin: 0; }}
.lesson-list {{ list-style: none; margin: 0; padding: 6px; display: grid; gap: 1px; }}
.lesson-list a {{ display: flex; justify-content: space-between; gap: 10px; align-items: baseline; padding: 7px 10px; border-radius: 7px; text-decoration: none; color: var(--ink); font-size: .96rem; }}
.lesson-list a:hover {{ background: var(--accent-soft); }}
.ls-meta {{ font-size: .8rem; color: var(--muted); font-variant-numeric: tabular-nums; white-space: nowrap; }}
.facts {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; }}
.fact {{ border-left: 3px solid var(--accent); padding: 2px 0 2px 14px; }}
.fact b {{ display: block; font-family: var(--f-display); font-weight: 600; font-size: 1.05rem; margin-bottom: 2px; }}
.fact p {{ margin: 0; font-size: .95rem; color: var(--muted); }}
.cta-band {{ margin-block: 8px 40px; border: 1.5px solid var(--accent); border-radius: 14px; padding: 24px; display: flex; flex-wrap: wrap; gap: 16px; align-items: center; justify-content: space-between; background: var(--surface); }}
.cta-band p {{ margin: 0; max-width: 52ch; }}
.cta-band b {{ font-family: var(--f-display); font-size: 1.2rem; display: block; }}
footer {{ border-top: 1px solid var(--rule); padding-block: 22px 40px; font-size: .88rem; color: var(--muted); display: flex; flex-wrap: wrap; gap: 8px 24px; justify-content: space-between; }}
footer p {{ margin: 0; }}
@media (max-width: 760px) {{
  .hero {{ grid-template-columns: minmax(0, 1fr); padding-block: 20px 36px; }}
  .nav-links {{ display: none; }}
}}
@media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important; }} }}
</style>
</head>
<body>
<div class="wrap">
  <nav class="nav" aria-label="Site">
    <a class="brand" href="./">Python <span>DSA</span> Workbook</a>
    <div class="nav-links"><a href="#how">How it works</a><a href="#syllabus">Syllabus</a><a href="#inside">Under the hood</a><a href="workbook/#review">Mixed review</a><a href="trainer/">Target Trainer</a></div>
  </nav>

  <header class="hero">
    <div>
      <p class="eyebrow">Free, open, runs in your browser</p>
      <h1>Learn data structures and algorithms the way assessments test them</h1>
      <p class="lede">{n_lessons} Python lessons where you predict output before you run it, pass hidden tests, state the complexity, fix a planted bug, and then rebuild your solution from memory. Built for graduate coding assessments, not for reading.</p>
      <div class="ctas"><a class="btn primary" href="workbook/#how-to-solve">Start lesson 1</a><a class="btn" href="#syllabus">Browse the syllabus</a></div>
      <div class="stats">
        <div class="stat"><b>{n_lessons}</b><span>lessons, about {hours} hours</span></div>
        <div class="stat"><b>{n_examples}</b><span>runnable examples</span></div>
        <div class="stat"><b>{n_practice} + {n_practice}</b><span>practice problems and bug fixes</span></div>
        <div class="stat"><b>{n_quiz}</b><span>quiz questions</span></div>
      </div>
    </div>
    <div class="demo" aria-label="The practice problem from the Hash sets lesson, with its tests passing">
      <div class="demo-head"><span class="demo-label">Your solution</span><span class="demo-btn">Run tests</span></div>
<pre><span class="tk-kw">def</span> <span class="tk-fn">still_in</span>(check_ins, check_outs):
    left = <span class="tk-fn">set</span>(check_outs)
    added = <span class="tk-fn">set</span>()
    result = []
    <span class="tk-kw">for</span> rid <span class="tk-kw">in</span> check_ins:
        <span class="tk-kw">if</span> rid <span class="tk-kw">not in</span> left <span class="tk-kw">and</span> rid <span class="tk-kw">not in</span> added:
            result.append(rid)
            added.add(rid)
    <span class="tk-kw">return</span> result</pre>
      <ul class="demo-tests">
        <li><span>given example</span><span class="pill ok">pass</span></li>
        <li><span>nobody left</span><span class="pill ok">pass</span></li>
        <li><span>repeated check-ins</span><span><span class="pill dim">hidden</span> <span class="pill ok">pass</span></span></li>
        <li><span>order kept</span><span><span class="pill dim">hidden</span> <span class="pill ok">pass</span></span></li>
      </ul>
      <div class="demo-out"><b>Next</b>State the complexity, then rebuild it from memory.</div>
    </div>
  </header>

  <section class="section" id="how">
    <h2>Five steps before a lesson counts as mastered</h2>
    <p class="intro">Reading a solution feels like understanding. These steps are the difference between recognising an answer and producing one under time pressure.</p>
    <div class="steps">
      <div class="step"><b>Predict, then run</b><span>Write what each example prints before you press Run. The page checks your prediction.</span></div>
      <div class="step"><b>Pass hidden tests</b><span>Each practice problem has visible and hidden tests, with partial credit, like a real assessment.</span></div>
      <div class="step"><b>State the complexity</b><span>No tick until you name the time and space complexity. Interviewers ask; so does the page.</span></div>
      <div class="step"><b>Fix the bug</b><span>A second version with a realistic bug planted in it. Read the failing case, change one thing, re-run.</span></div>
      <div class="step"><b>Rebuild from memory</b><span>Your passing code is saved and the editor cleared. Write it again without looking.</span></div>
    </div>
  </section>

  <section class="section" id="syllabus">
    <h2>Syllabus</h2>
    <p class="intro">Python basics for anyone new or rusty, six DSA modules from how to start a problem to dynamic programming, and a final project you can talk about in interviews. Each lesson is about 15 to 35 minutes of reading and coding, plus the practice.</p>
    <div class="modules">{syllabus}</div>
  </section>

  <section class="section" id="inside">
    <h2>Under the hood</h2>
    <div class="facts">
      <div class="fact"><b>Python runs in your browser</b><p>Examples and tests run on Brython, a Python 3 implementation in JavaScript. Nothing is sent to a server and there is no account to create.</p></div>
      <div class="fact"><b>Every example is verified</b><p>A build script runs each example in CPython and records its output, checks every model solution against its tests, and answers every output quiz question by running the code.</p></div>
      <div class="fact"><b>Progress stays with you</b><p>Mastery, quiz answers, timings and drafts are saved in your browser's storage. Clearing site data resets them.</p></div>
      <div class="fact"><b>Open source</b><p>Lessons are plain Python data files. The source, the build pipeline and this site are in the repository, so you can add a lesson or fix a mistake.</p></div>
    </div>
  </section>

  <div class="cta-band">
    <p><b>New or rusty at Python? Start with P1.</b>The Python basics module gets you from variables to classes. Already comfortable? Jump to lesson 1, the six-step routine every DSA lesson builds on.</p>
    <a class="btn primary" href="workbook/#py-values">Start Python basics</a> <a class="btn" href="workbook/#how-to-solve">Go to lesson 1</a>
  </div>

  <footer>
    <p>Original course content. Brython is BSD-licensed (see workbook/vendor/LICENSE). Not affiliated with any employer or assessment provider.</p>
    <p><a href="workbook/#review">Mixed review</a></p>
  </footer>
</div>
</body>
</html>
"""

(ROOT / "index.html").write_text(page)
print("wrote index.html", len(page) // 1024, "KB;", n_lessons, "lessons,", n_examples, "examples,", n_quiz, "quiz questions,", minutes, "minutes")
