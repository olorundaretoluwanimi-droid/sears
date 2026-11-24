# One-off: adapt scenes.js to the series' dark look (see restyle_dark.py). Every replacement must match once.
import os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(D, 'scenes.js'); s = open(p, encoding='utf-8').read()
R = [
 ("const dark = s => (s.dk || 0) > .5,", "const dark = s => true,"),
 # rings: the series' clean red arc, drawn clockwise
 ("""  if (k <= 0) return; x.save(); x.strokeStyle = o.pen ? C.pen : C.red; x.lineWidth = o.pen ? 5 : 4.5; x.lineCap = 'round'; x.beginPath();
  const a0 = -Math.PI * .6, n = 60; for (let i = 0; i <= n * k; i++) { const u = i / n, a = a0 + u * Math.PI * 2.15, rr_ = r * (1 + .06 * Math.sin(u * 9) + (o.pen ? .05 * Math.sin(u * 23) : 0));
    const px = X + Math.cos(a) * rr_ * 1.15, py = Y + Math.sin(a) * rr_ * .92; i ? x.lineTo(px, py) : x.moveTo(px, py); } x.stroke(); x.restore();""",
  """  if (k <= 0) return; x.save(); x.strokeStyle = C.red; x.lineWidth = 3.5; x.beginPath(); x.arc(X, Y, r, -Math.PI / 2, -Math.PI / 2 + Math.PI * 2 * k); x.stroke(); x.restore();"""),
 # name card: the series' name box (dark shade, red bar, Plex Sans name, mono role)
 ("""  const w1 = measure(name, { s: 58, f: F.fell }), w2 = measure(sub, { s: 21, f: F.mono, ls: 1 }), w = Math.max(w1, w2) + 70, h = 132, L = al === 'r' ? X - w : X;
  x.save(); x.globalAlpha *= a; x.shadowColor = 'rgba(30,18,6,.35)'; x.shadowBlur = 18; x.shadowOffsetY = 6; x.fillStyle = dk ? '#241d16' : C.mount; rr(L, Y - h / 2, w, h, 16); x.fill(); x.restore();
  x.save(); x.globalAlpha *= a; x.strokeStyle = dk ? '#7a6650' : C.ink; x.lineWidth = 1.8; rr(L, Y - h / 2, w, h, 16); x.stroke(); x.lineWidth = .8; rr(L + 6, Y - h / 2 + 6, w - 12, h - 12, 11); x.stroke();
  txt(name, L + 35, Y + 2, { s: 58, f: F.fell, c: dk ? C.cream : C.ink, id: 'nm' }); txt(sub, L + 35, Y + 42, { s: 21, f: F.mono, c: dk ? C.dim : C.ink2, ls: 1, id: 'ns' }); x.restore();""",
  """  const w = Math.max(measure(name, { s: 46, w: 700 }), measure(sub, { s: 19, f: 'Mono' })) + 64, h = 116, L = al === 'r' ? X - w : X, Yt = Y - h / 2;
  x.save(); x.globalAlpha *= a; shade(L, Yt, w, h, .88); x.fillStyle = C.red; x.fillRect(L + 18, Yt + 16, 6, 84);
  txt(name, L + 40, Yt + 62, { s: 46, w: 700, c: C.cream, id: 'nm' }); txt(sub, L + 42, Yt + 96, { s: 19, f: 'Mono', c: C.dim, id: 'ns' }); x.restore();"""),
 # photos flash white as they cut in (the series' cut grammar)
 ("""    const z = it.z ? lerp(it.z[0], it.z[1], seg(t, s.t0, s.t1)) : 1;
    plate(IM[it.img], it.x, it.y, it.w, it.h, { rot: it.rot, cart: it.cart, cap: it.cap, capAt: it.capAt, grade: it.grade, z, fx: it.fx, fy: it.fy, dark: dk, t, m: it.grade === 'paper' ? 10 : 16 }); });""",
  """    const z = it.z ? lerp(it.z[0], it.z[1], seg(t, s.t0, s.t1)) : 1, fl = (it.in === 'none' || (it.at === 0 && s.curl)) ? 0 : 1 - seg(t, a, a + .14);
    plate(IM[it.img], it.x, it.y, it.w, it.h, { cap: it.cap, grade: it.grade, z, fx: it.fx, fy: it.fy, t, flash: fl }); });"""),
 ("  if (it.k === 'cut') return enter(t, s, it, () => cut(IM[it.img], it.x, it.y, it.w, { rot: (it.rot || 0) + Math.sin((t - s.t0) * .6) * .6, grade: it.grade || 'paper' }));",
  "  if (it.k === 'cut') return enter(t, s, it, () => cut(IM[it.img], it.x, it.y, it.w, { rot: (it.rot || 0) + Math.sin((t - s.t0) * .6) * .6 }));"),
 ("if (it.k === 'tag') { const k = seg(t, a, a + .3); if (k > 0) { x.save(); x.globalAlpha *= k; srcTag(it.text, it.x, it.y, dk); x.restore(); } return; }",
  "if (it.k === 'tag') { const k = seg(t, a, a + .3); if (k > 0) { x.save(); x.globalAlpha *= k; srcTag(it.text, it.x, it.y); x.restore(); } return; }"),
 ("x.fillStyle = dk ? 'rgba(184,50,42,.45)' : 'rgba(214,72,52,.42)';", "x.fillStyle = 'rgba(229,81,47,.6)';"),
 ("x.globalCompositeOperation = dk ? 'screen' : 'multiply';", "x.globalCompositeOperation = 'multiply';"),
 ("txt((it.pre || '') + counter(v) + (it.suf || ''), it.x, it.y, { s: it.s || 120, f: F.ost, w: 700, c: C.red,", "txt((it.pre || '') + counter(v) + (it.suf || ''), it.x, it.y, { s: it.s || 120, f: 'Mono', w: 600, c: C.red,"),
 ("if (it.k === 'note') { const k = seg(t, a, a + .4); if (k > 0) { txt('☞', it.x - 20, it.y, { s: it.s * 1.2, f: F.serif, al: 'right', c: C.red, a: k });",
  "if (it.k === 'note') { const k = seg(t, a, a + .4); if (k > 0) { x.save(); x.globalAlpha *= k; x.fillStyle = C.red; x.fillRect(it.x - 26, it.y - it.s * .8, 6, it.s); x.restore();"),
 ("x.fillStyle = dk ? '#241d16' : C.mount; x.shadowColor = 'rgba(30,18,6,.35)'; x.shadowBlur = 20; rr(X - 50, it.y - it.s * 1.2, w + 100, it.s * 1.9, 14); x.fill(); x.restore(); }\n    return hand(it.text, X, it.y, t, a + .15, DUR_(s, it.dur, 1.6), { s: it.s, id: 'hd' }); }",
  "x.fillStyle = C.bg; rr(X - 50, it.y - it.s * 1.2, w + 100, it.s * 1.9, 4); x.fill(); x.restore(); }\n    return hand(it.text, X, it.y, t, a + .15, DUR_(s, it.dur, 1.6), { s: it.s, c: C.cream, w: 400, id: 'hd' }); }"),
 # cal90: numbers in mono
 ("txt('DAY', X, Y - 168, { s: 44, f: F.sc, c: C.cream, al: 'center', ls: 6 });", "txt('DAY', X, Y - 168, { s: 40, w: 700, c: C.cream, al: 'center', ls: 8 });"),
 ("txt(String(d), X, Y + 120, { s: 230, f: F.ost, w: 700, c: C.ink, al: 'center',", "txt(String(d), X, Y + 110, { s: 210, f: 'Mono', w: 600, c: C.ink, al: 'center',"),
 # map boxes on the dark ground
 ("if (s.note) { const k = seg(t, s.t0 + .5, s.t0 + .8); if (k > 0) { x.save(); x.globalAlpha = k; x.fillStyle = dk ? 'rgba(36,29,22,.92)' : 'rgba(241,230,204,.94)'; rr(90, 90, 620, s.note[1] ? 150 : 110, 16); x.fill();\n    x.strokeStyle = dk ? '#7a6650' : C.ink; x.lineWidth = 1.6; x.stroke(); txt(s.note[0], 125, 160, { s: 46, f: F.ost, w: 700, c: C.red, id: 'mn0' }); if (s.note[1]) txt(s.note[1], 125, 210, { s: 32, f: F.fell, it: 1, c: dk ? C.cream : C.ink, id: 'mn1' }); x.restore(); } }",
  "if (s.note) { const k = seg(t, s.t0 + .5, s.t0 + .8); if (k > 0) { x.save(); x.globalAlpha = k; shade(90, 90, 660, s.note[1] ? 150 : 110, .9); x.fillStyle = C.red; x.fillRect(108, 106, 6, s.note[1] ? 118 : 78);\n    txt(s.note[0], 135, 160, { s: 44, f: 'Mono', w: 600, c: C.red, id: 'mn0' }); if (s.note[1]) txt(s.note[1], 137, 205, { s: 30, it: 1, c: C.cream, id: 'mn1' }); x.restore(); } }"),
 ("if (s.count) { const k = seg(t, AT(s, s.count.at), AT(s, s.count.at) + .4); if (k > 0) { x.save(); x.globalAlpha = k; x.fillStyle = 'rgba(241,230,204,.94)'; rr(1290, 640, 560, 230, 18); x.fill(); x.strokeStyle = C.ink; x.lineWidth = 1.6; x.stroke();\n    txt(s.count.text, 1570, 760, { s: 120, f: F.ost, w: 700, c: C.red, al: 'center', id: 'mc' }); txt(s.count.label, 1570, 830, { s: 30, f: F.fell, it: 1, al: 'center', id: 'mcl' }); x.restore(); } }",
  "if (s.count) { const k = seg(t, AT(s, s.count.at), AT(s, s.count.at) + .4); if (k > 0) { x.save(); x.globalAlpha = k; shade(1270, 640, 600, 230, .9);\n    txt(s.count.text, 1570, 760, { s: 120, f: 'Mono', w: 600, c: C.red, al: 'center', id: 'mc' }); txt(s.count.label, 1570, 830, { s: 28, c: C.cream, al: 'center', id: 'mcl' }); x.restore(); } }"),
 ("if (s.count2) { const k = seg(t, AT(s, s.count2.at), AT(s, s.count2.at) + .4); if (k > 0) { x.save(); x.globalAlpha = k; x.fillStyle = 'rgba(241,230,204,.94)'; rr(90, 90, 760, 100, 16); x.fill(); x.strokeStyle = C.ink; x.lineWidth = 1.6; x.stroke();\n    txt(s.count2.text, 470, 158, { s: 44, f: F.ost, w: 700, c: C.red, al: 'center', id: 'mc2' }); x.restore(); } }",
  "if (s.count2) { const k = seg(t, AT(s, s.count2.at), AT(s, s.count2.at) + .4); if (k > 0) { x.save(); x.globalAlpha = k; shade(90, 90, 760, 100, .9);\n    txt(s.count2.text, 470, 156, { s: 42, f: 'Mono', w: 600, c: C.red, al: 'center', id: 'mc2' }); x.restore(); } }"),
 ("  srcTag('MAP · SCHEMATIC · NATURAL EARTH (PUBLIC DOMAIN)', 1640, 1050 - 0, dk);", "  srcTag('MAP · SCHEMATIC · NATURAL EARTH (PUBLIC DOMAIN)', 280, 46);"),
 ("mapDraw(MX, MY, MW, { dark: dk }); x.strokeStyle = dk ? '#7a6650' : C.ink;", "mapDraw(MX, MY, MW, {}); x.strokeStyle = C.line;"),
 ("x.fillStyle = C.mount; x.fillRect(it.x - 10, it.y - 10, it.w + 20, MAP.H * sc + 20); x.restore();\n  mapDraw(it.x, it.y, it.w, {}); x.strokeStyle = C.ink;",
  "x.fillStyle = C.bg; x.fillRect(it.x - 10, it.y - 10, it.w + 20, MAP.H * sc + 20); x.restore();\n  mapDraw(it.x, it.y, it.w, {}); x.strokeStyle = C.line;"),
 ("if (k > 0) town(P(n), n, { r: 6, s: 24, a: k, c: n === 'Chicago' ? C.red : C.ink }); }", "if (k > 0) town(P(n), n, { r: 6, s: 24, a: k, c: n === 'Chicago' ? C.red : C.cream }); }"),
 # calendar: mono numbers on paper pages
 ("txt(big ? lab[0] : lab[0], 0, big ? 70 : 110, { s: big ? 130 : 230, f: F.ost, w: 700, al: 'center', c: C.ink,", "txt(lab[0], 0, big ? 70 : 110, { s: big ? 120 : 210, f: 'Mono', w: 600, al: 'center', c: C.ink,"),
 ("txt(lab[1], 0, 200, { s: 44, f: F.fell, it: 1, al: 'center', c: C.ink2,", "txt(lab[1], 0, 200, { s: 42, it: 1, al: 'center', c: C.ink2,"),
 ("x.fillStyle = '#efe4c8'; x.fillRect(-380, -300, 760, 560);", "x.fillStyle = C.paper; x.fillRect(-380, -300, 760, 560);"),
 # title
 ("    plate(IM.c1902_n0, 1320, 120, 470, 634, { rot: 4, grade: 'paper', t, m: 10 });", "    plate(IM.c1902_n0, 1300, 110, 520, 702, { t, flash: 1 - seg(l, 0, .14) });\n    srcTag('SEARS CATALOGUE NO. 111 · 1902 (INTERNET ARCHIVE)', 1300, 96);"),
 ("drop('What Happened', 140, 380, t, s.t0 + .3, { s: 128, f: F.fell, id: 'ti1' }); drop('to Sears?', 140, 520, t, s.t0 + .75, { s: 128, f: F.fell, id: 'ti2' });",
  "drop('What Happened', 140, 380, t, s.t0 + .3, { s: 120, id: 'ti1' }); drop('to Sears?', 140, 515, t, s.t0 + .75, { s: 120, id: 'ti2' });"),
 ("const k = seg(l, 1.6, 2.0); hair(146, 575, 146 + 1000 * eo(k), 575, C.ink, 2);", "const k = seg(l, 1.6, 2.0); x.fillStyle = C.red; x.fillRect(146, 568, 1000 * eo(k), 4);"),
 ("txt('THE CATALOG THAT BUILT SMALL-TOWN AMERICA', 146, 640, { s: 38, f: F.sc, ls: 3, a: seg(l, 1.8, 2.2), id: 'ti3' });", "txt('THE CATALOG THAT BUILT SMALL-TOWN AMERICA', 146, 636, { s: 32, f: 'Mono', w: 600, ls: 2, c: C.dim, a: seg(l, 1.8, 2.2), id: 'ti3' });"),
 ("txt('SEARS, ROEBUCK AND CO. · CHICAGO', 146, 880, { s: 22, f: F.mono, c: C.ink2, ls: 2, a: seg(l, 2.9, 3.2) });", "txt('Sears, Roebuck and Co. · Chicago', 146, 880, { s: 34, w: 700, a: seg(l, 2.9, 3.2) });"),
 # seven
 ("x.shadowColor = 'rgba(30,18,6,.4)'; x.shadowBlur = 20; x.shadowOffsetY = 8; x.fillStyle = C.mount; x.fillRect(-w / 2, -h / 2, w, h); x.shadowColor = 'transparent';\n    x.strokeStyle = C.ink; x.lineWidth = 1.5; x.strokeRect(-w / 2 + 10, -h / 2 + 10, w - 20, h - 20);",
  "x.fillStyle = C.panel; x.fillRect(-w / 2, -h / 2, w, h); x.strokeStyle = C.line; x.lineWidth = 1; x.strokeRect(-w / 2 + .5, -h / 2 + .5, w - 1, h - 1);"),
 ("txt(`No. ${i + 1}`, -w / 2 + 28, h / 2 - 72, { s: 22, f: F.mono, c: C.ink2 }); txt(lab, -w / 2 + 28, h / 2 - 34, { s: 38, f: F.fell, id: 'sv' + i });",
  "txt(`NO. ${i + 1}`, -w / 2 + 28, h / 2 - 72, { s: 19, f: 'Mono', w: 600, c: C.dim, ls: 1 }); txt(lab, -w / 2 + 28, h / 2 - 32, { s: 32, w: 700, id: 'sv' + i });"),
 ("x.translate(X + w / 2, Y + h / 2 - 60 * (1 - eback(k))); x.rotate(rot * Math.PI / 180);", "x.translate(X + w / 2, Y + h / 2 - 60 * (1 - eback(k)));"),
 # end card
 ("drop('What Happened to Sears?', 150, 230, t, s.t0 + .2, { s: 84, f: F.fell }); txt('THE CATALOG THAT BUILT SMALL-TOWN AMERICA', 154, 290, { s: 28, f: F.sc, ls: 3, a: k });\n  hair(154, 320, 154 + 1100 * eo(k), 320, C.ink, 1.5);",
  "drop('What Happened to Sears?', 150, 230, t, s.t0 + .2, { s: 72 }); txt('THE CATALOG THAT BUILT SMALL-TOWN AMERICA', 154, 288, { s: 24, f: 'Mono', w: 600, ls: 1, c: C.dim, a: k });\n  hair(154, 326, 154 + 1100 * eo(k), 326, C.dim, 1);"),
 ("cr.forEach((c, i) => txt(c, 154, 430 + i * 52, { s: 23, f: F.serif, c: C.ink2,", "cr.forEach((c, i) => txt(c, 154, 430 + i * 52, { s: 22, c: '#CDBFA6',"),
 ("  cut(IM.cut_watch_a, 1640, 250, 260, { rot: 8, a: k, grade: 'paper' });", "  cut(IM.cut_watch_a, 1640, 250, 240, { rot: 8, a: k });"),
 # bars, dots, stack
 ("plate(IM[s.img], 110, 140, 560, Math.min(740, 560 / (IM[s.img] ? IM[s.img].width / IM[s.img].height : 1)), { rot: -2, grade: gr_(s.img), dark: dk, t });",
  "plate(IM[s.img], 60, 120, 640, Math.min(780, 640 / (IM[s.img] ? IM[s.img].width / IM[s.img].height : 1)), { grade: gr_(s.img), t, flash: s.curl ? 0 : 1 - seg(t, s.t0, s.t0 + .14) });"),
 ("txt(s.title, 780, 150, { s: 24, f: F.mono, c: dimC(s), ls: 2, id: 'bt' });", "txt(s.title, 780, 150, { s: 24, f: 'Mono', w: 600, c: C.dim, ls: 2, id: 'bt' });"),
 ("txt(lab, X + BW / 2, Yb + 50, { s: 38, f: F.fell, c: inkC(s), al: 'center', id: 'bl' + i });", "txt(lab, X + BW / 2, Yb + 50, { s: 34, w: 700, c: C.cream, al: 'center', id: 'bl' + i });"),
 ("txt(vl, X + BW / 2, Yb - h - 22, { s: 46, f: F.ost, w: 700, c: inkC(s),", "txt(vl, X + BW / 2, Yb - h - 22, { s: 44, f: 'Mono', w: 600, c: i === n - 1 ? C.red : C.cream,"),
 ("  const dk = !s.light, l = t - s.t0; ground(dk ? Math.max(s.dk || 0, .85) : 0, { border: !dk });", "  const dk = true, l = t - s.t0; ground();"),
 ("{ grade: gr_(s.img), dark: dk, t, rot: -1.2 }); if (s.tag) srcTag(s.tag, 90, 104, dk); }", "{ grade: gr_(s.img), t, flash: s.curl ? 0 : 1 - seg(t, s.t0, s.t0 + .14) }); if (s.tag) srcTag(s.tag, 100, 112); }"),
 ("txt(counter(val), cx, Math.min(900, Y0 + gh + 150), { s: 130, f: F.ost, w: 700,", "txt(counter(val), cx, Math.min(900, Y0 + gh + 150), { s: 130, f: 'Mono', w: 600,"),
 ("txt(s.label, cx, Math.min(900, Y0 + gh + 150) + 46, { s: 34, f: F.fell, it: 1,", "txt(s.label, cx, Math.min(900, Y0 + gh + 150) + 46, { s: 30,"),
 ("txt(Y[j][1], X0, 140, { s: 40, f: F.ost, w: 700, c: C.red, id: 'dy' }); }", "txt(Y[j][1], X0, 140, { s: 40, f: 'Mono', w: 600, c: C.red, id: 'dy' }); }"),
 ("if (s.note) txt(s.note, X0 + gw, 140, { s: 30, f: F.fell, it: 1,", "if (s.note) txt(s.note, X0 + gw, 140, { s: 28, f: 'Mono',"),
 ("plate(IM[s.img], 140, 110, 600, 780, { rot: -2, grade: 'paper', t, m: 10 }); srcTag('CONSUMERS GUIDE · SPRING 1897', 130, 84);",
  "plate(IM[s.img], 120, 110, 600, 780, { grade: 'paper', t }); srcTag('CONSUMERS GUIDE · SPRING 1897', 120, 96);"),
 ("txt(counter(pages) + ' pages', X + 200, Yb - hpx - 175, { s: 64, f: F.ost, w: 700, c: C.red,", "txt(counter(pages) + ' pages', X + 200, Yb - hpx - 175, { s: 60, f: 'Mono', w: 600, c: C.red,"),
 ("{ s: 48, f: F.ost, w: 700, c: C.ink, al: 'left', id: 'sty' });", "{ s: 46, f: 'Mono', w: 600, c: C.cream, al: 'left', id: 'sty' });"),
 # flip
 ("plate(im, 650 + j * 14, 70 + j * 10, 620, 830, { rot: j * 1.5 - 1, grade: 'paper', t, m: 8, a: j ? .9 : 1 }); }", "plate(im, 650 + j * 14, 70 + j * 10, 620, 830, { grade: 'paper', t, a: j ? .9 : 1 }); }"),
 ("plate(IM[pg], 0, 0, 620, 830, { grade: 'paper', t, m: 8 }); x.restore(); }", "plate(IM[pg], 0, 0, 620, 830, { grade: 'paper', t }); x.restore(); }"),
 ("drop(s.words[j], j % 2 ? 1620 : 330, 230 + j * 92, t, a, { s: 70, f: F.fell, al: 'center', id: 'fw' + j }); } });", "drop(s.words[j], j % 2 ? 1620 : 330, 230 + j * 92, t, a, { s: 62, al: 'center', id: 'fw' + j }); } });"),
 # conveyor
 ("plate(IM[s.img], 170, 100, 1020, 824, { grade: 'sepia', t, rot: -1 }); srcTag(s.tag, 160, 74);", "plate(IM[s.img], 60, 76, 1060, 856, { grade: 'sepia', t, flash: s.curl ? 0 : 1 - seg(t, s.t0, s.t0 + .14) }); srcTag(s.tag, 60, 62);"),
 ("plate(IM[s.img2], 1240, 200, 560, 576, { rot: 2.5, grade: 'sepia', t, m: 12, cap: 'Train shed · 1906' })", "plate(IM[s.img2], 1180, 180, 680, 650, { grade: 'sepia', t, cap: 'Train shed · 1906', flash: 1 - seg(t, AT(s, -.45), AT(s, -.45) + .14) })"),
 # letter (the series' quote card on paper)
 ("const im = IM[s.img], h = 820, w = h * (im ? im.width / im.height : .84); plate(im, 120, 100, w, h, { grade: 'paper', t, m: 10, rot: -1.5 }); srcTag('SEARS CATALOGUE · SPRING 1897 · p. 28', 110, 74);",
  "const im = IM[s.img], h = 860, w = h * (im ? im.width / im.height : .84); plate(im, 60, 60, w, h, { grade: 'paper', t }); srcTag('SEARS CATALOGUE · SPRING 1897 · p. 28', 60, 46);"),
 ("x.fillRect(120, 100 + h * s.hl[0], w * k, h * (s.hl[1] - s.hl[0])); x.restore();", "x.fillRect(60, 60 + h * s.hl[0], w * k, h * (s.hl[1] - s.hl[0])); x.restore();"),
 ("const X = 900, Y = 150, W_ = 900, H_ = 650; x.save(); x.translate(X + W_ / 2, Y + H_ / 2); x.rotate(1 * Math.PI / 180); x.translate(-W_ / 2, -H_ / 2);\n    x.shadowColor = 'rgba(30,18,6,.4)'; x.shadowBlur = 28; x.shadowOffsetY = 10; x.fillStyle = '#f1e7cf'; x.fillRect(0, 0, W_, H_); x.shadowColor = 'transparent';\n    for (let i = 0; i < 12; i++) hair(60, 170 + i * 42, W_ - 60, 170 + i * 42, 'rgba(60,80,120,.12)', 1);",
  "const X = 860, Y = 60, W_ = 1000, H_ = 760; x.save(); x.translate(X, Y); paperCard(0, 0, W_, H_, t);"),
 ("txt(s.head, W_ / 2, 76, { s: 40, f: F.sc, al: 'center', ls: 2, id: 'lh' }); txt(`${s.place}, ${s.date}`, W_ - 60, 128, { s: 30, f: F.fell, it: 1, al: 'right', c: C.ink2, id: 'lp' });\n    txt('Gentlemen:', 60, 200, { s: 34, f: F.fell, it: 1, a: seg(l, .5, .8) });",
  "txt(s.head.toUpperCase(), 60, 96, { s: 22, f: 'Mono', w: 600, ls: 2, c: C.ink2, id: 'lh' }); txt(`${s.place} · ${s.date}`, 60, 132, { s: 22, f: 'Mono', c: C.ink2, id: 'lp' });\n    txt('Gentlemen:', 60, 230, { s: 44, it: 1, c: C.ink, a: seg(l, .5, .8) });"),
 ("if (n > 0) txt(q.slice(0, n), 60, 290 + i * 84, { s: 54, f: F.fell, it: 1, id: n === q.length ? 'lq' + i : null }); });\n    hand(s.who, 480, 590, t, s.t0 + s.vd * .85, .9, { s: 62, id: 'lw' }); x.restore();",
  "if (n > 0) txt(q.slice(0, n), 60, 340 + i * 104, { s: 66, it: 1, c: C.ink, id: n === q.length ? 'lq' + i : null }); });\n    x.restore();"),
 ("nameCard(s.who, 'A CUSTOMER · CHAPEL HILL, N.C. · 1897', 1060, 905, 'l', seg(l, 1.0, 1.4));", "nameCard(s.who, 'A CUSTOMER · CHAPEL HILL, N.C. · 1897', 860, 900, 'l', seg(l, 1.0, 1.4));"),
 # ledger: typed in mono on the paper ledger, a dark-room light around it
 ("const X = 260, Y = 110, W_ = 1400, H_ = 760; x.save(); x.shadowColor = 'rgba(0,0,0,.45)'; x.shadowBlur = 30; x.shadowOffsetY = 12; x.fillStyle = '#e8e2c8'; x.fillRect(X, Y, W_, H_); x.restore();",
  "const X = 260, Y = 110, W_ = 1400, H_ = 760; paperCard(X, Y, W_, H_, t);"),
 ("txt('LEDGER · SEARS, ROEBUCK AND CO.', X + 40, Y + 70, { s: 30, f: F.sc, ls: 3, c: C.ink2 });", "txt('LEDGER · SEARS, ROEBUCK AND CO.', X + 40, Y + 70, { s: 24, f: 'Mono', w: 600, ls: 2, c: C.ink2 });"),
 ("hand(d, X + 30, Yr, t, a, .5, { s: 48, id: 'ld' + i }); hand(what, X + 250, Yr, t, a + .5, 1.2, { s: 48, id: 'lw' + i });\n      if (amt) hand(amt, X + 1080, Yr, t, a + 1.6, .8, { s: 52, c: C.red, id: 'la' + i }); });",
  "hand(d, X + 30, Yr, t, a, .5, { s: 36, id: 'ld' + i }); hand(what, X + 250, Yr, t, a + .5, 1.2, { s: 36, w: 400, id: 'lw' + i });\n      if (amt) hand(amt, X + 1080, Yr, t, a + 1.6, .8, { s: 38, c: C.red, id: 'la' + i }); });"),
 ("if (s.big) stamp(s.big, 960, Y + 560, t, s.t0 + s.vd * .3, { s: 96, rot: -4, id: 'lbig' });", "if (s.big) stamp(s.big, 960, Y + 560, t, s.t0 + s.vd * .3, { s: 80, rot: -3, paper: 1, id: 'lbig' });"),
 ("if (s.note) txt(s.note, 960, Y + 700, { s: 34, f: F.fell, it: 1, al: 'center', c: C.ink2,", "if (s.note) txt(s.note, 960, Y + 700, { s: 32, it: 1, al: 'center', c: C.ink2,"),
 # tower
 ("plate(IM.tower1974, 110, 90, 500, 828, { rot: -1.5, grade: 'colour', t }); srcTag('DOCUMERICA · U.S. EPA · 1974', 100, 64);", "plate(IM.tower1974, 60, 76, 520, 860, { grade: 'colour', t }); srcTag('DOCUMERICA · U.S. EPA · 1974', 60, 62);"),
 ("x.fillStyle = col; x.fillRect(X, Yb - h, 150, h); x.strokeStyle = C.ink; x.lineWidth = 1.5; x.strokeRect(X, Yb - h, 150, h);", "x.fillStyle = col; x.fillRect(X, Yb - h, 150, h);"),
 ("txt(counter(Math.round(hft * k2)) + ' ft', X + 75, Yb - h - 22, { s: 44, f: F.ost, w: 700, c: col === C.red ? C.red : C.ink,", "txt(counter(Math.round(hft * k2)) + ' ft', X + 75, Yb - h - 22, { s: 42, f: 'Mono', w: 600, c: col === C.red ? C.red : C.cream,"),
 ("txt(lab, X + 75, Yb + 46, { s: 30, f: F.fell, it: 1, al: 'center', id: 'tl' + lab }); };", "txt(lab, X + 75, Yb + 46, { s: 24, f: 'Mono', c: C.dim, al: 'center', id: 'tl' + lab }); };"),
 ("hair(760, Yb, 1700, Yb, C.ink, 2);", "hair(760, Yb, 1700, Yb, C.dim, 2);"),
 ("txt('tallest in the world · 1973–1998', 1340, 140, { s: 38, f: F.fell, it: 1,", "txt('tallest in the world · 1973–1998', 1340, 140, { s: 34, w: 500,"),
 # rivals
 ("if (i < n) { x.fillStyle = 'rgba(42,32,24,.55)';", "if (i < n) { x.fillStyle = 'rgba(241,231,211,.55)';"),
 ("drop('Walmart', 300, 300, t, s.t0 + .3, { s: 90, f: F.fell, al: 'center' }); txt('from Arkansas · 1962', 300, 350, { s: 30, f: F.fell, it: 1,", "drop('Walmart', 300, 300, t, s.t0 + .3, { s: 84, al: 'center' }); txt('from Arkansas · 1962', 300, 350, { s: 26, f: 'Mono', c: C.dim,"),
 ("drop('Home Depot', 1620, 300, t, AT(s, -.55), { s: 90, f: F.fell, al: 'center' }); txt('one thing, for less · 1978', 1620, 350, { s: 30, f: F.fell, it: 1,", "drop('Home Depot', 1620, 300, t, AT(s, -.55), { s: 84, al: 'center' }); txt('one thing, for less · 1978', 1620, 350, { s: 26, f: 'Mono', c: C.dim,"),
 ("srcTag('MAP · SCHEMATIC · DOTS ILLUSTRATIVE, NOT STORE LOCATIONS', 560, 110);", "srcTag('MAP · SCHEMATIC · DOTS ILLUSTRATIVE, NOT STORE LOCATIONS', 560, 104);"),
 # fan
 ("plate(IM[p], -230, -880, 460, 620, { grade: 'paper', t, m: 8, dark: true }); x.restore(); });", "plate(IM[p], -230, -880, 460, 620, { grade: 'paper', t }); x.restore(); });"),
 ("txt('−$' + counter(v), 1450, 470, { s: 104, f: F.ost, w: 700, c: C.red, al: 'center', id: 'fanv' }); txt(s.count.label, 1450, 540, { s: 38, f: F.fell, it: 1,", "txt('−$' + counter(v), 1450, 470, { s: 96, f: 'Mono', w: 600, c: C.red, al: 'center', id: 'fanv' }); txt(s.count.label, 1450, 540, { s: 32,"),
 ("srcTag('SEARS CATALOGS · 1897–1928 (INTERNET ARCHIVE)', 540, 64, true);", "srcTag('SEARS CATALOGS · 1897–1928 (INTERNET ARCHIVE)', 540, 64);"),
 # house
 ("txt('SEARS, ROEBUCK & CO.', 120, 88, { s: 22, f: F.sc, c: C.cream, al: 'center' }); txt('READY-CUT', 480, 88, { s: 22, f: F.sc, c: C.cream, al: 'center' });", "txt('SEARS, ROEBUCK & CO.', 120, 88, { s: 20, w: 700, c: C.cream, al: 'center' }); txt('READY-CUT', 480, 88, { s: 20, w: 700, c: C.cream, al: 'center' });"),
 ("txt(counter(v), 1520, 560, { s: 120, f: F.ost, w: 700, c: C.red, al: 'center', id: 'hp' }); txt('parts, as many as', 1520, 440, { s: 36, f: F.fell, it: 1, al: 'center', id: 'hp2' });", "txt(counter(v), 1520, 560, { s: 116, f: 'Mono', w: 600, c: C.red, al: 'center', id: 'hp' }); txt('as many as', 1520, 440, { s: 30, f: 'Mono', c: C.dim, al: 'center', id: 'hp2' }); txt('parts', 1520, 620, { s: 30, f: 'Mono', c: C.dim, al: 'center' });"),
 ("txt('INSTRUCTIONS', 0, -10, { s: 26, f: F.sc, c: '#e9d6a8', al: 'center' }); txt('Honor Bilt', 0, 34, { s: 30, f: F.fell, it: 1, c: '#e9d6a8', al: 'center' });", "txt('INSTRUCTIONS', 0, -10, { s: 24, w: 700, c: '#e9d6a8', al: 'center', ls: 2 }); txt('Honor Bilt', 0, 34, { s: 28, it: 1, c: '#e9d6a8', al: 'center' });"),
 ("const frame = () => { x.save(); x.shadowColor = 'rgba(30,18,6,.4)'; x.shadowBlur = 26; x.shadowOffsetY = 10; x.fillStyle = C.mount; x.fillRect(EX - 16, EY - 16, EW + 32, EH + 32); x.restore(); };", "const frame = () => { x.fillStyle = C.panel; x.fillRect(EX, EY, EW, EH); };"),
 ("x.strokeStyle = C.ink; x.lineWidth = 2; x.strokeRect(EX, EY, EW, EH);\n      const pk", "x.strokeStyle = C.line; x.lineWidth = 1; x.strokeRect(EX, EY, EW, EH);\n      const pk"),
 ("if (IM.carlin_plan1 && pk > 0) { x.save(); x.beginPath(); x.rect(1330, 120, 470 * pk, 1000); x.clip(); x.drawImage(IM.carlin_plan1, 1330, 120, 470, 507); x.restore(); }", "if (IM.carlin_plan1 && pk > 0) { x.save(); x.beginPath(); x.rect(1330, 120, 470 * pk, 1000); x.clip(); x.drawImage(tinted(IM.carlin_plan1, '#E6D7B8'), 1330, 120, 470, 507); x.restore(); }"),
 ("if (IM.carlin_title) cut(IM.carlin_title, EX + EW / 2, EY + EH + 70, 900, { sh: false, a: seg(l, s.vd * .3, s.vd * .3 + .4) });", "if (IM.carlin_title) cut(IM.carlin_title, EX + EW / 2, EY + EH + 70, 900, { a: seg(l, s.vd * .3, s.vd * .3 + .4) });"),
 ("x.strokeStyle = C.ink; x.lineWidth = 2; x.strokeRect(EX, EY, EW, EH);\n      if (wk >= 1) capPill('Street view of Sears, Roebuck and Co.\\nhouses at Carlinville, Ill.', EX + EW - 30, EY + EH - 6, 'r', false, seg(l, w0 + 1.8, w0 + 2.2));",
  "x.strokeStyle = C.line; x.lineWidth = 1; x.strokeRect(EX, EY, EW, EH);\n      if (wk >= 1) capPill('Sears houses at Carlinville, Ill.\\n1921 catalog', EX + 18, EY + EH - 18, seg(l, w0 + 1.8, w0 + 2.2));"),
 ("enter(t, s, { at: -.5, in: 'slide', from: [500, 0] }, () => plate(IM.carl1921_street1, 1300, 520, 520, 520 / 3.05, { rot: 3, grade: 'sepia', t, m: 10 }));\n      srcTag('HONOR BILT MODERN HOMES · 1921 · pp. 4–5 (INTERNET ARCHIVE)', EX - 10, EY - 26); });",
  "enter(t, s, { at: -.5, in: 'slide', from: [500, 0] }, () => plate(IM.carl1921_street1, 1300, 560, 560, 560 / 3.05, { grade: 'sepia', t }));\n      srcTag('HONOR BILT MODERN HOMES · 1921 · pp. 4–5 (INTERNET ARCHIVE)', EX, EY - 14); });"),
 ("withCam(c, () => { plate(IM.carl1921_street1, 160, 90, 1600, 525, { grade: 'sepia', t, z: lerp(1, 1.05, seg(t, s.t0, s.t1)) }); srcTag('HONOR BILT MODERN HOMES · 1921 · p. 5', 150, 64);",
  "withCam(c, () => { plate(IM.carl1921_street1, 160, 90, 1600, 525, { grade: 'sepia', t, z: lerp(1, 1.05, seg(t, s.t0, s.t1)) }); srcTag('HONOR BILT MODERN HOMES · 1921 · p. 5', 160, 76);"),
 ("x.fillStyle = on ? C.red : 'rgba(42,32,24,.18)';", "x.fillStyle = on ? C.red : 'rgba(241,231,211,.14)';"),
 ("txt('≈ 150 of 156 · still standing', 1760, 660, { s: 34, f: F.fell, it: 1, al: 'right',", "txt('≈ 150 of 156 · still standing', 1760, 664, { s: 28, f: 'Mono', w: 600, c: C.cream, al: 'right',"),
 ("x.save(); x.shadowColor = 'rgba(30,18,6,.4)'; x.shadowBlur = 26; x.fillStyle = C.mount; x.fillRect(X - 16, Y - 16, w + 32, h + 32); x.restore();\n    cover(img, X, Y, w, h, { grade: 'sepia', t }); x.save(); x.globalAlpha = gone * .7; x.fillStyle = '#cdb98f';",
  "cover(img, X, Y, w, h, { grade: 'sepia', t }); x.save(); x.globalAlpha = gone * .75; x.fillStyle = C.bg;"),
 ("x.strokeStyle = C.ink; x.lineWidth = 2; x.strokeRect(X, Y, w, h); srcTag('SCHOPPER, ILL. · HONOR BILT MODERN HOMES · 1921', X - 10, Y - 26);", "x.strokeStyle = C.line; x.lineWidth = 1; x.strokeRect(X, Y, w, h); srcTag('SCHOPPER, ILL. · HONOR BILT MODERN HOMES · 1921', X, Y - 14);"),
]
bad = []
for a, b in R:
    n = s.count(a)
    if n != 1: bad.append((n, a[:90]))
    else: s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s)
print('applied', len(R) - len(bad), 'of', len(R)); [print(' miss', n, a) for n, a in bad]
