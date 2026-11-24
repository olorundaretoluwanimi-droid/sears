import os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def patch(fn, R):
    p = os.path.join(D, fn); s = open(p, encoding='utf-8').read()
    for a, b in R:
        assert s.count(a) == 1, (fn, a[:70]); s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s)
patch('index.html', [("  const fam = o.f || 'Sans', s = size || o.s || 30;",
                      "  const fam = ({ Sans: 'Sans', Mono: 'Mono' })[o.f] || F[String(o.f || '').toLowerCase()] || 'Sans', s = size || o.s || 30;")])
patch('scenes.js', [
 ("      miniMap(t, s, { x: 1280, y: 90, w: 520, towns: [['Chicago', 0]], routes: [['Chicago', 'Carlinville', .2, 1.6, -.25]] });",
  "      miniMap(t, s, { x: 120, y: 90, w: 520, towns: [['Chicago', 0]], routes: [['Chicago', 'Carlinville', .2, 1.6, -.25]] });"),
 ("txt(counter(v), 1520, 560, { s: 116, f: 'Mono', w: 600, c: C.red, al: 'center', id: 'hp' }); txt('as many as', 1520, 440, { s: 30, f: 'Mono', c: C.dim, al: 'center', id: 'hp2' }); txt('parts', 1520, 620, { s: 30, f: 'Mono', c: C.dim, al: 'center' });",
  "txt(counter(v), 1480, 250, { s: 116, f: 'Mono', w: 600, c: C.red, al: 'center', id: 'hp' }); txt('as many as', 1480, 140, { s: 30, f: 'Mono', c: C.dim, al: 'center', id: 'hp2' }); txt('parts', 1480, 310, { s: 30, f: 'Mono', c: C.dim, al: 'center' });"),
 ("'Music  original score; VSCO 2 CE (CC0), Salamander Grand Piano (CC BY 3.0, Alexander Holm) · Fonts: IM Fell, Old Standard TT, Source Serif 4, Source Sans 3, IBM Plex Mono, Pinyon Script (OFL)'];",
  "'Music  original score; VSCO 2 CE (CC0), Salamander Grand Piano (CC BY 3.0, Alexander Holm) · Fonts: IBM Plex Sans, IBM Plex Mono, Source Serif 4 (OFL)'];"),
])
patch('tools/build_film.py', [
 ("'n96': dict(type='spread', cam=PULL, items=[ph('carl1921_street2', 140, 140, 1640, at=0, **{'in': 'none'}, cap='Carlinville, Ill.'),\n     cut('cut_mast1897', 960, 860, 900, at=-.6, grade='paper')]),",
  "'n96': dict(type='spread', cam=PULL, items=[ph('carl1921_street2', 140, 140, 1640, at=0, **{'in': 'none'}, cap='Carlinville, Ill.'), tag('HONOR BILT MODERN HOMES · 1921 · p. 5', 140, 126)]),"),
])
p = os.path.join(D, 'CREDITS'); s = open(p, encoding='utf-8').read()
a = s[s.index('FONTS (SIL Open Font License 1.1)'):s.index('The user is responsible')]
s = s.replace(a, 'FONTS (SIL Open Font License 1.1)\n  IBM Plex Sans, IBM Plex Mono (IBM) · Source Serif 4 (Adobe).\n\n'); open(p, 'w', encoding='utf-8').write(s)
print('ok')
