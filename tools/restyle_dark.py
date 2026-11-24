# One-off: turn the catalog-page engine (index.html) into the series' warm dark look — same scenes and motion graphics,
# IBM Plex type, flat dark ground, hard-edged pictures with mono tags, paper cards only for quotes and order blanks.
import os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(D, 'index.html'); s = open(p, encoding='utf-8').read()
head = open(os.path.join(D, 'tools', 'dark_head.html'), encoding='utf-8').read()
s = head + s[s.index("// ── grounds and camera"):]
a = s[s.index("// paper ground with the catalog's"):s.index("// camera keys")]
s = s.replace(a, "// the series' flat warm-dark ground\nfunction ground() { x.fillStyle = C.bg; x.fillRect(0, 0, W, H); }\n")
s = s.replace("if (!MAP) return; const s = w / MAP.W, dark = o.dark, P", "if (!MAP) return; const s = w / MAP.W, dark = o.dark !== false, P")
s = s.replace("x.strokeStyle = o.dark ? C.cream : C.ink; x.lineWidth = 1.5; x.stroke(); txt(name, p[0] + (o.dx ?? 16), p[1] + (o.dy ?? 9), { s: o.s || 30, f: F.fell, c: o.dark ? C.cream : C.ink,",
              "x.strokeStyle = C.cream; x.lineWidth = 1.5; x.stroke(); txt(name, p[0] + (o.dx ?? 16), p[1] + (o.dy ?? 9), { s: o.s || 30, w: 500, c: C.cream,")
a = s[s.index("function subs(t) {"):s.index("// ── page curl")]
s = s.replace(a, open(os.path.join(D, 'tools', 'dark_subs.js'), encoding='utf-8').read())
s = s.replace("path(flap); x.fillStyle = C.paper2; x.fill(); x.restore();", "path(flap); x.fillStyle = '#2a231b'; x.fill(); x.restore();")
s = s.replace("x.save(); path(flap); x.clip(); x.drawImage(PAPER, 300, 200, 900, 500, 0, 0, W, H); const g", "x.save(); path(flap); x.clip(); const g")
s = s.replace("g.addColorStop(0, 'rgba(60,40,15,.45)'); g.addColorStop(.35, 'rgba(255,245,220,.18)'); g.addColorStop(1, 'rgba(60,40,15,.1)');",
              "g.addColorStop(0, 'rgba(0,0,0,.5)'); g.addColorStop(.35, 'rgba(241,231,211,.10)'); g.addColorStop(1, 'rgba(0,0,0,.15)');")
a = s[s.index("function sBlank(t, s) {"):s.index("const SCN = ")]
s = s.replace(a, open(os.path.join(D, 'tools', 'dark_blank.js'), encoding='utf-8').read())
s = s.replace("x.setTransform(1, 0, 0, 1, 0, 0); x.globalAlpha = 1; x.filter = 'none'; x.fillStyle = C.desk; x.fillRect(0, 0, W, H);",
              "x.setTransform(1, 0, 0, 1, 0, 0); x.globalAlpha = 1; x.filter = 'none'; ground();")
a = s[s.index("  await document.fonts.load('40px Fell');"):s.index("  try { FILM = await")]
s = s.replace(a, "  await Promise.all(['400 40px Sans', '500 40px Sans', '700 40px Sans', '400 40px Mono', '600 40px Mono', 'italic 400 40px SerifI'].map(f => document.fonts.load(f)));\n")
s = s.replace("PAPER = makePaper(); DESK = makeDesk(); SPECK = makeSpeck(); makeGrain();", "SPECK = makeSpeck(); makeGrain();")
s = s.replace("L.push(load(`assets/${n}.${png ? 'png' : 'jpg'}`).then(im => { if (im) IM[n] = im; }));",
              "L.push(load(`assets/${n}.${png ? 'png' : 'jpg'}`).then(im => { if (im) { im._n = n; IM[n] = im; } }));")
open(p, 'w', encoding='utf-8').write(s)
print('PAPER' in s, 'Fell' in s, 'DESK' in s)
