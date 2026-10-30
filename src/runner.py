from browser import window
import sys, io, traceback, builtins

import json as _json

class JSONDecodeError(ValueError):
    def __init__(self, msg, doc, pos):
        lineno = doc.count("\n", 0, pos) + 1
        colno = pos - doc.rfind("\n", 0, pos)
        ValueError.__init__(self, "%s: line %d column %d (char %d)" % (msg, lineno, colno, pos))
        self.msg = msg
        self.doc = doc
        self.pos = pos
        self.lineno = lineno
        self.colno = colno

_WS = " \t\n\r"
_ESC = {'"': '"', "\\": "\\", "/": "/", "b": "\b", "f": "\f", "n": "\n", "r": "\r", "t": "\t"}
_NUMCH = "0123456789+-.eE"

def _loads(s, *args, **kw):
    if isinstance(s, (bytes, bytearray)):
        s = s.decode("utf-8")
    if not isinstance(s, str):
        raise TypeError("the JSON object must be str, bytes or bytearray, not " + type(s).__name__)
    n = len(s)

    def ws(i):
        while i < n and s[i] in _WS:
            i += 1
        return i

    def value(i):
        i = ws(i)
        if i >= n:
            raise JSONDecodeError("Expecting value", s, i)
        c = s[i]
        if c == "{":
            return obj(i + 1)
        if c == "[":
            return arr(i + 1)
        if c == '"':
            return string(i + 1)
        if s.startswith("true", i):
            return True, i + 4
        if s.startswith("false", i):
            return False, i + 5
        if s.startswith("null", i):
            return None, i + 4
        if s.startswith("NaN", i):
            return float("nan"), i + 3
        if s.startswith("Infinity", i):
            return float("inf"), i + 8
        if s.startswith("-Infinity", i):
            return float("-inf"), i + 9
        if c == "-" or c.isdigit():
            return number(i)
        raise JSONDecodeError("Expecting value", s, i)

    def number(i):
        start = i
        if s[i] == "-":
            i += 1
        if i >= n or not s[i].isdigit():
            raise JSONDecodeError("Expecting value", s, start)
        if s[i] == "0":
            i += 1
        else:
            while i < n and s[i].isdigit():
                i += 1
        is_float = False
        if i < n and s[i] == ".":
            j = i + 1
            if j >= n or not s[j].isdigit():
                return int(s[start:i]), i
            i = j
            while i < n and s[i].isdigit():
                i += 1
            is_float = True
        if i < n and s[i] in "eE":
            j = i + 1
            if j < n and s[j] in "+-":
                j += 1
            if j < n and s[j].isdigit():
                i = j
                while i < n and s[i].isdigit():
                    i += 1
                is_float = True
        text = s[start:i]
        return (float(text) if is_float else int(text)), i

    def string(i):
        start = i - 1
        out = []
        while True:
            if i >= n:
                raise JSONDecodeError("Unterminated string starting at", s, start)
            c = s[i]
            if c == '"':
                return "".join(out), i + 1
            if c == "\\":
                i += 1
                if i >= n:
                    raise JSONDecodeError("Unterminated string starting at", s, start)
                e = s[i]
                if e in _ESC:
                    out.append(_ESC[e])
                    i += 1
                elif e == "u":
                    h = s[i + 1:i + 5]
                    if len(h) != 4 or any(ch not in "0123456789abcdefABCDEF" for ch in h):
                        raise JSONDecodeError("Invalid \\uXXXX escape", s, i - 1)
                    code = int(h, 16)
                    i += 5
                    if 0xD800 <= code <= 0xDBFF and s[i:i + 2] == "\\u":
                        h2 = s[i + 2:i + 6]
                        if len(h2) == 4 and all(ch in "0123456789abcdefABCDEF" for ch in h2):
                            low = int(h2, 16)
                            if 0xDC00 <= low <= 0xDFFF:
                                code = 0x10000 + ((code - 0xD800) << 10) + (low - 0xDC00)
                                i += 6
                    out.append(chr(code))
                else:
                    raise JSONDecodeError("Invalid \\escape", s, i - 1)
            elif ord(c) < 0x20:
                raise JSONDecodeError("Invalid control character at", s, i)
            else:
                out.append(c)
                i += 1

    def obj(i):
        result = {}
        i = ws(i)
        if i < n and s[i] == "}":
            return result, i + 1
        while True:
            i = ws(i)
            if i >= n or s[i] != '"':
                raise JSONDecodeError("Expecting property name enclosed in double quotes", s, i)
            key, i = string(i + 1)
            i = ws(i)
            if i >= n or s[i] != ":":
                raise JSONDecodeError("Expecting ':' delimiter", s, i)
            val, i = value(i + 1)
            result[key] = val
            i = ws(i)
            if i < n and s[i] == "}":
                return result, i + 1
            if i >= n or s[i] != ",":
                raise JSONDecodeError("Expecting ',' delimiter", s, i)
            i += 1

    def arr(i):
        result = []
        i = ws(i)
        if i < n and s[i] == "]":
            return result, i + 1
        while True:
            val, i = value(i)
            result.append(val)
            i = ws(i)
            if i < n and s[i] == "]":
                return result, i + 1
            if i >= n or s[i] != ",":
                raise JSONDecodeError("Expecting ',' delimiter", s, i)
            i += 1

    result, end = value(0)
    end = ws(end)
    if end != n:
        raise JSONDecodeError("Extra data", s, end)
    return result

def _load(fp, *args, **kw):
    return _loads(fp.read())

_json.loads = _loads
_json.load = _load
_json.JSONDecodeError = JSONDecodeError


def run_code(src):
    buf = io.StringIO()
    old = (sys.stdout, sys.stderr, sys.stdin)
    sys.stdout = buf
    sys.stderr = buf
    sys.stdin = io.StringIO("")
    def _input(prompt=""):
        line = sys.stdin.readline()
        if line == "":
            raise EOFError("no more input")
        return line.rstrip("\n")
    ns = {"__name__": "__main__", "input": _input}
    try:
        exec(src, ns)
    except BaseException:
        traceback.print_exc()
    finally:
        sys.stdout, sys.stderr, sys.stdin = old
    return buf.getvalue()

window.pyRun = run_code
window.pyReady = True
