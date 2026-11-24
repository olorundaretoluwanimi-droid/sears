// order blank: the chapter card — a paper card typed in Plex Mono, the price or date stamped in red; the chapter's picture beside it
function sBlank(t, s) {
  const c = camAt(s, t); ground();
  withCam(c, () => {
    if (s.side) { const im = IM[s.side], h = 700, w = Math.min(560, im ? h * im.width / im.height : 520), X = 1800 - w;
      plate(im, X, 150, w, h, { grade: s.sideGrade, t }); }
    const bx = 120, by = 220, w = 1100, h = 560; paperCard(bx, by, w, h, t);
    x.save(); x.translate(bx, by);
    x.strokeStyle = C.ink; x.lineWidth = 1; x.strokeRect(20.5, 20.5, w - 41, h - 41);
    txt('SEARS, ROEBUCK & CO.', w / 2, 96, { s: 50, w: 700, al: 'center', ls: 6, c: C.ink });
    txt('ORDER BLANK  ·  CHICAGO, ILL.', w / 2, 136, { s: 21, f: 'Mono', w: 600, al: 'center', c: C.ink2, ls: 3 });
    const cols = [[60, 'CATALOGUE NO.'], [290, 'NAME OF ARTICLE'], [650, 'YEAR'], [800, 'PRICE']];
    hair(50, 170, w - 50, 170, C.ink, 1.5); hair(50, 214, w - 50, 214, C.ink, 1); cols.forEach(([cx, l]) => txt(l, cx, 200, { s: 18, f: 'Mono', w: 600, ls: 1, c: C.ink2 }));
    [270, 630, 780].forEach(cx => hair(cx, 170, cx, 400, C.ink, 1)); for (let i = 0; i < 3; i++) hair(50, 300 + i * 50, w - 50, 300 + i * 50, 'rgba(42,33,24,.3)', 1);
    const a = s.t0 + .5; hand(s.no, 66, 282, t, a, .45, { s: 38 }); hand(s.art, 296, 282, t, a + .5, .9, { s: 38, id: 'oa' }); hand(s.year, 656, 282, t, a + 1.5, .4, { s: 38, id: 'oy' });
    stamp(s.price, 925, 268, t, a + 2.05, { s: Math.min(54, 54 * 200 / measure(s.price, { s: 54, f: 'Mono', w: 600 })), rot: -5, seed: 3, paper: 1, id: 'op' });
    if (s.sub) txt(s.sub, w / 2, 470, { s: 36, it: 1, al: 'center', c: C.ink, a: seg(t, a + 2.4, a + 2.7), id: 'os' });
    txt(`${s.of || ''}`, w - 60, h - 46, { s: 20, f: 'Mono', w: 600, al: 'right', c: C.ink2, a: seg(t, a + 2.4, a + 2.7) });
    x.restore();
  });
}
