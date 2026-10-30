"""Assemble the workbook page from template.html, runner.py and lessons.js.

  python3 src/assemble.py            -> workbook/index.html (standalone site: full HTML skeleton, Brython from workbook/vendor/)
  python3 src/assemble.py --artifact -> build/artifact.html (fragment for a claude.ai artifact, Brython from jsDelivr)
"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
template = (HERE / "template.html").read_text()
runner = (HERE / "runner.py").read_text()
assert "</script" not in runner

artifact = "--artifact" in sys.argv
page = template.replace("/*RUNNER*/", runner)

if artifact:
    page = page.replace("/*BRYTHON_BASE*/", "https://cdn.jsdelivr.net/npm/brython@3.13.2/")
    out = ROOT / "build" / "artifact.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(page)
else:
    page = page.replace("/*BRYTHON_BASE*/", "vendor/")
    page = page.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
    page = page.replace('<a class="home-link" href="../" id="home-link" hidden>', '<a class="home-link" href="../" id="home-link">')
    head = (
        '<!doctype html>\n<html lang="en-GB">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="description" content="An interactive Python data structures and algorithms workbook: 21 lessons, runnable examples, quizzes, bug-fixing drills and auto-tested practice problems.">\n'
        '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}</style>\n'
    )
    page = head + page.replace("<title>", "<title>", 1)
    # the template starts with <title> and <link>s followed by <style>: move the head part into <head>
    i = page.index('<div class="app"')
    page = page[:i] + "</head>\n<body>\n" + page[i:] + "\n</body>\n</html>\n"
    out = ROOT / "workbook" / "index.html"
    out.write_text(page)

print("wrote", out.relative_to(ROOT), out.stat().st_size // 1024, "KB")
