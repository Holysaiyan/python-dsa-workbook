"""Make the website copy of Target Trainer (trainer/index.html) from the standalone trainer.html."""
import sys
src = open(sys.argv[1]).read()
head = '''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Practice games for game-based assessments: number targets, shape rotation, odd one out, memory, flashback, disco numbers, pulse and personality.">
<style>
:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}
.site-nav{display:flex;justify-content:space-between;align-items:center;gap:12px;margin:0 0 18px;flex-wrap:wrap}
.site-nav a,.site-foot a{display:inline-flex;align-items:center;gap:8px;text-decoration:none;font-weight:600;font-size:.92rem;color:var(--ink);background:var(--surface);border:1px solid var(--rule);border-radius:999px;padding:7px 14px}
.site-nav a:hover,.site-foot a:hover{border-color:var(--accent);color:var(--accent)}
.site-nav .crumb{font-size:.85rem;color:var(--muted)}
.site-foot{margin:28px 0 8px;padding-top:18px;border-top:1px solid var(--rule);display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;color:var(--muted);font-size:.88rem}
</style>
'''
s = src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '', 1)
i = s.index('</style>\n') + len('</style>\n'); s = s[:i] + '</head>\n<body>\n' + s[i:]
a = '<div class="wrap">\n'
assert s.count(a) == 1
s = s.replace(a, a + '  <nav class="site-nav" aria-label="Site"><a href="../">&larr; Python DSA Workbook</a><span class="crumb">Target Trainer</span></nav>\n', 1)
a = 'the practice round is there for exactly that.</p></div>\n  </details>\n'
assert s.count(a) == 1
s = s.replace(a, a + '  <footer class="site-foot"><span>Part of the Python DSA Workbook: lessons, practice and these games.</span><a href="../">&larr; Back to the workbook</a></footer>\n')
open(sys.argv[2], 'w').write(head + s.rstrip('\n') + '\n\n</body>\n</html>\n')
