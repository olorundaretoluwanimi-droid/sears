// Scene library for "What Happened to Sears?" — loaded after index.html's primitives. Every scene is draw(t, s), deterministic.
window.ALWAYS = ['carlin_elev', 'carlin_plan1', 'carlin_plan2', 'carlin_title', 'carl1921_street2', 'carl1921_street1', 'cut_watch_a', 'cut_watch_b',
  'c1897_n0', 'c1902_n0', 'c1912_n0', 'c1918_n0', 'c1928_n0', 'store1929_allentown', 'tower1974', 'closing_hialeah', 'carl_station', 'habs_tower', 'mh1918_n52'];
const dark = s => (s.dk || 0) > .5, inkC = s => dark(s) ? C.cream : C.ink, dimC = s => dark(s) ? C.dim : C.ink2;
const COL = { red: () => C.red, cream: () => C.cream, ink: () => C.ink, pen: () => C.pen };
const life = s => seg(0, 0, 1) && 0;
function DUR_(s, v, base) { return v == null ? base : v < 0 ? -v * (s.vd || (s.t1 - s.t0)) : v; }

// ── entrances ─────────────────────────────────────────────────────────────────────────────────────────────
function enter(t, s, it, fn) {
  const a = AT(s, it.at ?? 0), mode = it.in || 'drop';
  if (mode === 'none' || (it.at === 0 && mode !== 'slide' && s.curl)) { fn(1); return; }
  const k = seg(t, a, a + (mode === 'slide' ? .7 : .42)); if (k <= 0) return;
  let dx = 0, dy = 0, al = 1;
  if (mode === 'drop') { dy = -70 * (1 - eback(k)); al = clamp(k * 3); }
  else if (mode === 'slide') { const f = it.from || [0, 600]; dx = f[0] * (1 - eo(k)); dy = f[1] * (1 - eo(k)); }
  else if (mode === 'fade') al = k;
  x.save(); x.globalAlpha *= al; x.translate(dx, dy); fn(k); x.restore();
}
// ── spread items ──────────────────────────────────────────────────────────────────────────────────────────
function ring(X, Y, r, k, o = {}) {
  if (k <= 0) return; x.save(); x.strokeStyle = o.pen ? C.pen : C.red; x.lineWidth = o.pen ? 5 : 4.5; x.lineCap = 'round'; x.beginPath();
  const a0 = -Math.PI * .6, n = 60; for (let i = 0; i <= n * k; i++) { const u = i / n, a = a0 + u * Math.PI * 2.15, rr_ = r * (1 + .06 * Math.sin(u * 9) + (o.pen ? .05 * Math.sin(u * 23) : 0));
    const px = X + Math.cos(a) * rr_ * 1.15, py = Y + Math.sin(a) * rr_ * .92; i ? x.lineTo(px, py) : x.moveTo(px, py); } x.stroke(); x.restore();
}
function nameCard(name, sub, X, Y, al, a = 1, dk) {
  const w1 = measure(name, { s: 58, f: F.fell }), w2 = measure(sub, { s: 21, f: F.mono, ls: 1 }), w = Math.max(w1, w2) + 70, h = 132, L = al === 'r' ? X - w : X;
  x.save(); x.globalAlpha *= a; x.shadowColor = 'rgba(30,18,6,.35)'; x.shadowBlur = 18; x.shadowOffsetY = 6; x.fillStyle = dk ? '#241d16' : C.mount; rr(L, Y - h / 2, w, h, 16); x.fill(); x.restore();
  x.save(); x.globalAlpha *= a; x.strokeStyle = dk ? '#7a6650' : C.ink; x.lineWidth = 1.8; rr(L, Y - h / 2, w, h, 16); x.stroke(); x.lineWidth = .8; rr(L + 6, Y - h / 2 + 6, w - 12, h - 12, 11); x.stroke();
  txt(name, L + 35, Y + 2, { s: 58, f: F.fell, c: dk ? C.cream : C.ink, id: 'nm' }); txt(sub, L + 35, Y + 42, { s: 21, f: F.mono, c: dk ? C.dim : C.ink2, ls: 1, id: 'ns' }); x.restore();
}
function item(t, s, it) {
  const a = AT(s, it.at ?? 0), dk = dark(s);
  if (it.k === 'ph') return enter(t, s, it, () => {
    const z = it.z ? lerp(it.z[0], it.z[1], seg(t, s.t0, s.t1)) : 1;
    plate(IM[it.img], it.x, it.y, it.w, it.h, { rot: it.rot, cart: it.cart, cap: it.cap, capAt: it.capAt, grade: it.grade, z, fx: it.fx, fy: it.fy, dark: dk, t, m: it.grade === 'paper' ? 10 : 16 }); });
  if (it.k === 'cut') return enter(t, s, it, () => cut(IM[it.img], it.x, it.y, it.w, { rot: (it.rot || 0) + Math.sin((t - s.t0) * .6) * .6, grade: it.grade || 'paper' }));
  if (it.k === 'drop') return drop(it.text, it.x, it.y, t, a, { s: it.s, f: F[(it.f || 'fell').toLowerCase()] || it.f, c: it.c ? COL[it.c]() : inkC(s), al: it.al, ls: it.ls, w: it.w, id: 'd' + it.text.slice(0, 4) });
  if (it.k === 'stamp') return stamp(it.text, it.x, it.y, t, a, { s: it.s, rot: it.rot, dark: dk, seed: it.text.length, id: 'st' });
  if (it.k === 'txt') { const k = seg(t, a, a + .35); if (k > 0) txt(it.text, it.x, it.y, { s: it.s, f: F[(it.f || 'serif').toLowerCase()] || it.f, it: it.it, w: it.w, al: it.al, c: it.c ? COL[it.c]() : inkC(s), a: k, id: 'tx' }); return; }
  if (it.k === 'tag') { const k = seg(t, a, a + .3); if (k > 0) { x.save(); x.globalAlpha *= k; srcTag(it.text, it.x, it.y, dk); x.restore(); } return; }
  if (it.k === 'hl') { const k = eo(seg(t, a, a + DUR_(s, it.dur, .6))); if (k <= 0) return; x.save(); x.globalCompositeOperation = dk ? 'screen' : 'multiply'; x.fillStyle = dk ? 'rgba(184,50,42,.45)' : 'rgba(214,72,52,.42)'; x.fillRect(it.x, it.y, it.w * k, it.h); x.restore(); return; }
  if (it.k === 'ring') return ring(it.x, it.y, it.r, eo(seg(t, a, a + .55)), { pen: it.pen });
  if (it.k === 'count') { const k = seg(t, a, a + DUR_(s, it.dur, 1.2)); if (k <= 0) return; const v = Math.round(lerp(it.from || 0, it.to, eo(k)));
    txt((it.pre || '') + counter(v) + (it.suf || ''), it.x, it.y, { s: it.s || 120, f: F.ost, w: 700, c: C.red, al: it.al || 'center', id: k >= 1 ? 'cn' : null });
    if (it.note) txt(it.note, it.x, it.y + (it.s || 120) * .42, { s: 40, f: F.fell, it: 1, c: inkC(s), al: it.al || 'center', a: seg(t, a + .5, a + .8), id: 'cnn' }); return; }
  if (it.k === 'name') { const k = seg(t, a, a + .35); if (k > 0) nameCard(it.name, it.sub, it.x, it.y, it.al, k, dk); return; }
  if (it.k === 'note') { const k = seg(t, a, a + .4); if (k > 0) { txt('☞', it.x - 20, it.y, { s: it.s * 1.2, f: F.serif, al: 'right', c: C.red, a: k }); txt(it.text, it.x, it.y, { s: it.s, f: F.fell, it: 1, c: inkC(s), a: k, id: 'nt' }); } return; }
  if (it.k === 'hand') { const w = measure(it.text, { s: it.s, f: F.hand }), X = it.al === 'center' ? it.x - w / 2 : it.x;
    if (t >= a) { x.save(); x.globalAlpha = seg(t, a, a + .2) * .92; x.fillStyle = dk ? '#241d16' : C.mount; x.shadowColor = 'rgba(30,18,6,.35)'; x.shadowBlur = 20; rr(X - 50, it.y - it.s * 1.2, w + 100, it.s * 1.9, 14); x.fill(); x.restore(); }
    return hand(it.text, X, it.y, t, a + .15, DUR_(s, it.dur, 1.6), { s: it.s, id: 'hd' }); }
  if (it.k === 'cal90') return cal90(t, s, it, a);
  if (it.k === 'map') return miniMap(t, s, it);
}
function sSpread(t, s) {
  ground(s.dk || 0, { border: !dark(s) }); const c = camAt2(s, t);
  withCam(c, () => { for (const it of s.items || []) item(t, s, it); });
}
// camera keys may use negative fractions of the line for their time
function camAt2(s, t) { const K = (s.cam || [[0, W / 2, H / 2, 1, 0]]).map(k => [k[0] < 0 ? -k[0] * (s.vd || (s.t1 - s.t0)) : k[0], ...k.slice(1)]); return camAt(Object.assign({}, s, { cam: K }), t); }

// a tear-off day counter: 1 → 90 days
function cal90(t, s, it, a) {
  const k = seg(t, a, a + DUR_(s, it.dur, 3)), d = Math.max(1, Math.round(lerp(1, 90, eio(k)))), X = it.x, Y = it.y;
  x.save(); x.shadowColor = 'rgba(30,18,6,.4)'; x.shadowBlur = 24; x.shadowOffsetY = 10; x.fillStyle = '#efe4c8'; x.fillRect(X - 220, Y - 230, 440, 420); x.restore();
  x.fillStyle = C.red; x.fillRect(X - 220, Y - 230, 440, 90); txt('DAY', X, Y - 168, { s: 44, f: F.sc, c: C.cream, al: 'center', ls: 6 });
  txt(String(d), X, Y + 120, { s: 230, f: F.ost, w: 700, c: C.ink, al: 'center', id: d === 90 ? 'c90' : null });
  for (let i = 0; i < 6; i++) { x.fillStyle = C.ink; x.beginPath(); x.arc(X - 160 + i * 64, Y - 230, 7, 0, 7); x.fill(); }
  const f = ((t - a) * 12) % 1; if (k > 0 && k < 1) { x.save(); x.globalAlpha = 1 - f; x.translate(X, Y - 140); x.rotate(-f * .6); x.fillStyle = '#efe4c8'; x.fillRect(-220 + f * 200, f * 120, 440, 330); x.restore(); }
}
// ── map scenes ────────────────────────────────────────────────────────────────────────────────────────────
const MX = 280, MY = 60, MW = 1360;
function mapGeom() { const s = MW / MAP.W; return { s, P: n => [MX + MAP.towns[n][0] * s, MY + MAP.towns[n][1] * s] }; }
function railPts(seed, n, src, r) {   // destination points on rail lines near src (world px), deterministic
  const g = mapGeom(), S = g.P(src), R = rnd(seed), out = [], all = [];
  for (const l of MAP.rail) for (const p of l) all.push(p);
  let guard = 0; while (out.length < n && guard++ < 20000) { const p = all[Math.floor(R() * all.length)], q = [MX + p[0] * g.s, MY + p[1] * g.s], d = Math.hypot(q[0] - S[0], q[1] - S[1]);
    if (d > 40 && d < r) out.push(q); } return out;
}
function sMap(t, s) {
  const dk = dark(s); ground(s.dk || 0, { border: !dk }); const l = t - s.t0, g = mapGeom(), F_ = g.P(s.focus || 'Chicago');
  const z = lerp(s.zoom[0], s.zoom[1], eio(seg(t, s.t0, s.t1))), zmax = Math.max(s.zoom[0], s.zoom[1]), u = zmax > 1 ? (z - 1) / (zmax - 1) : 0;
  const c = { x: lerp(960, F_[0], u), y: lerp(540, F_[1], u), z, r: 0 };
  withCam(c, () => {
    mapDraw(MX, MY, MW, { dark: dk }); x.strokeStyle = dk ? '#7a6650' : C.ink; x.lineWidth = 2 / z; x.strokeRect(MX, MY, MW, MAP.H * g.s);
    for (const r of s.routes || []) route(g.P(r[0]), g.P(r[1]), seg(t, AT(s, r[2]), AT(s, r[2]) + DUR_(s, r[3], 2)), { bend: r[4] ?? .2, lw: 4 / z, ps: 14 / z, dash: [10 / z, 7 / z] });
    if (s.swarm) { const w = s.swarm, pts = railPts(7 + w.n, w.n, w.src, w.r), S = g.P(w.src), a0 = AT(s, w.at), span = DUR_(s, w.dur, 3);
      pts.forEach((q, i) => { const st = a0 + span * i / w.n, k = seg(t, st, st + .9);
        if (k >= 1) { x.fillStyle = C.red; x.beginPath(); x.arc(q[0], q[1], 4.5 / z, 0, 7); x.fill(); }
        else if (k > 0) { const e = eio(k), px = lerp(S[0], q[0], e), py = lerp(S[1], q[1], e) - Math.sin(e * Math.PI) * 30 / z; x.save(); x.globalAlpha = .9; parcel(px, py, 7 / z); x.restore(); } }); }
    for (const [n, at, o] of s.towns || []) { const k = seg(t, AT(s, at), AT(s, at) + .35); if (k > 0) town(g.P(n), n, Object.assign({ r: 9 / z, s: 34 / z, a: k, dark: dk, c: n === (s.focus || '') ? C.red : (dk ? C.cream : C.ink), id: 'tw' + n }, o || {})); }
  });
  if (s.note) { const k = seg(t, s.t0 + .5, s.t0 + .8); if (k > 0) { x.save(); x.globalAlpha = k; x.fillStyle = dk ? 'rgba(36,29,22,.92)' : 'rgba(241,230,204,.94)'; rr(90, 90, 620, s.note[1] ? 150 : 110, 16); x.fill();
    x.strokeStyle = dk ? '#7a6650' : C.ink; x.lineWidth = 1.6; x.stroke(); txt(s.note[0], 125, 160, { s: 46, f: F.ost, w: 700, c: C.red, id: 'mn0' }); if (s.note[1]) txt(s.note[1], 125, 210, { s: 32, f: F.fell, it: 1, c: dk ? C.cream : C.ink, id: 'mn1' }); x.restore(); } }
  if (s.count) { const k = seg(t, AT(s, s.count.at), AT(s, s.count.at) + .4); if (k > 0) { x.save(); x.globalAlpha = k; x.fillStyle = 'rgba(241,230,204,.94)'; rr(1290, 640, 560, 230, 18); x.fill(); x.strokeStyle = C.ink; x.lineWidth = 1.6; x.stroke();
    txt(s.count.text, 1570, 760, { s: 120, f: F.ost, w: 700, c: C.red, al: 'center', id: 'mc' }); txt(s.count.label, 1570, 830, { s: 30, f: F.fell, it: 1, al: 'center', id: 'mcl' }); x.restore(); } }
  if (s.count2) { const k = seg(t, AT(s, s.count2.at), AT(s, s.count2.at) + .4); if (k > 0) { x.save(); x.globalAlpha = k; x.fillStyle = 'rgba(241,230,204,.94)'; rr(90, 90, 760, 100, 16); x.fill(); x.strokeStyle = C.ink; x.lineWidth = 1.6; x.stroke();
    txt(s.count2.text, 470, 158, { s: 44, f: F.ost, w: 700, c: C.red, al: 'center', id: 'mc2' }); x.restore(); } }
  srcTag('MAP · SCHEMATIC · NATURAL EARTH (PUBLIC DOMAIN)', 1640, 1050 - 0, dk);
}
function miniMap(t, s, it) {
  const sc = it.w / MAP.W, P = n => [it.x + MAP.towns[n][0] * sc, it.y + MAP.towns[n][1] * sc];
  x.save(); x.shadowColor = 'rgba(30,18,6,.35)'; x.shadowBlur = 18; x.fillStyle = C.mount; x.fillRect(it.x - 10, it.y - 10, it.w + 20, MAP.H * sc + 20); x.restore();
  mapDraw(it.x, it.y, it.w, {}); x.strokeStyle = C.ink; x.lineWidth = 1.5; x.strokeRect(it.x, it.y, it.w, MAP.H * sc);
  for (const r of it.routes || []) route(P(r[0]), P(r[1]), seg(t, AT(s, r[2]), AT(s, r[2]) + DUR_(s, r[3], 2)), { bend: r[4] ?? .2, lw: 3, ps: 10 });
  for (const [n, at] of it.towns || []) { const k = seg(t, AT(s, at), AT(s, at) + .3); if (k > 0) town(P(n), n, { r: 6, s: 24, a: k, c: n === 'Chicago' ? C.red : C.ink }); }
}
// ── calendar flip (1993 → 1994) ───────────────────────────────────────────────────────────────────────────
function sCalendar(t, s) {
  const dk = !!s.dark || dark(s); ground(dk ? 1 : s.dk || 0, { border: !dk }); const f = AT(s, s.flip), k = eio(seg(t, f, f + .8)), c = camAt2(s, t);
  const page = (lab, X, Y, rot, al) => { x.save(); x.translate(X, Y); x.rotate(rot); x.globalAlpha *= al; x.shadowColor = 'rgba(0,0,0,.45)'; x.shadowBlur = 30; x.shadowOffsetY = 12;
    x.fillStyle = '#efe4c8'; x.fillRect(-380, -300, 760, 560); x.shadowColor = 'transparent'; x.fillStyle = C.red; x.fillRect(-380, -300, 760, 110);
    for (let i = 0; i < 8; i++) { x.fillStyle = C.ink; x.beginPath(); x.arc(-320 + i * 91, -300, 8, 0, 7); x.fill(); }
    const big = lab[0].length > 6; txt(big ? lab[0] : lab[0], 0, big ? 70 : 110, { s: big ? 130 : 230, f: F.ost, w: 700, al: 'center', c: C.ink, id: 'cal' + lab[0] });
    txt(lab[1], 0, 200, { s: 44, f: F.fell, it: 1, al: 'center', c: C.ink2, id: 'cl' + lab[0] }); x.restore(); };
  withCam(c, () => { page(s.b, 960, 470, .02, seg(t, f - .2, f)); page(s.a, 960 - k * 200, 470 - k * 900, -k * .5, 1 - seg(k, .7, 1)); });
}
// ── title, the seven things, end card ────────────────────────────────────────────────────────────────────
function sTitle(t, s) {
  ground(0); const l = t - s.t0, c = { x: 960, y: 540, z: lerp(1.04, 1, eo(seg(l, 0, 4))), r: 0 };
  withCam(c, () => {
    plate(IM.c1902_n0, 1320, 120, 470, 634, { rot: 4, grade: 'paper', t, m: 10 });
    drop('What Happened', 140, 380, t, s.t0 + .3, { s: 128, f: F.fell, id: 'ti1' }); drop('to Sears?', 140, 520, t, s.t0 + .75, { s: 128, f: F.fell, id: 'ti2' });
    const k = seg(l, 1.6, 2.0); hair(146, 575, 146 + 1000 * eo(k), 575, C.ink, 2);
    txt('THE CATALOG THAT BUILT SMALL-TOWN AMERICA', 146, 640, { s: 38, f: F.sc, ls: 3, a: seg(l, 1.8, 2.2), id: 'ti3' });
    stamp('1886–2026', 400, 780, t, s.t0 + 2.6, { s: 64, rot: -5, id: 'ti4' });
    txt('SEARS, ROEBUCK AND CO. · CHICAGO', 146, 880, { s: 22, f: F.mono, c: C.ink2, ls: 2, a: seg(l, 2.9, 3.2) });
  });
}
const SEVEN = [['cut_watch_a', 'A watch', '1886'], ['c1897_n0', 'The catalog', '1897'], ['carlin_elev', 'A house', '1918'], ['store1929_allentown', 'A store', '1925'],
  ['tower1974', 'A tower', '1973'], ['c1902_n0', 'The last catalog', '1993'], ['closing_hialeah', 'A closing-sale sign', '2018']];
function sSeven(t, s) {
  ground(0); const c = camAt2(Object.assign({ cam: [[0, 960, 540, 1.03, 0], [-1.1, 960, 540, 1.0, 0]] }, s), t);
  withCam(c, () => SEVEN.forEach(([img, lab, yr], i) => {
    const a = AT(s, s.at[i]), k = seg(t, a, a + .45); if (k <= 0) return; const row = i < 4 ? 0 : 1, col = row ? i - 4 : i, n = row ? 3 : 4, w = 380, h = 390;
    const X = 960 - (n * w + (n - 1) * 40) / 2 + col * (w + 40), Y = 70 + row * 440, rot = ((i * 37) % 7 - 3) * .6;
    x.save(); x.globalAlpha = clamp(k * 3); x.translate(X + w / 2, Y + h / 2 - 60 * (1 - eback(k))); x.rotate(rot * Math.PI / 180);
    x.shadowColor = 'rgba(30,18,6,.4)'; x.shadowBlur = 20; x.shadowOffsetY = 8; x.fillStyle = C.mount; x.fillRect(-w / 2, -h / 2, w, h); x.shadowColor = 'transparent';
    x.strokeStyle = C.ink; x.lineWidth = 1.5; x.strokeRect(-w / 2 + 10, -h / 2 + 10, w - 20, h - 20);
    if (img.startsWith('cut_')) cut(IM[img], 0, -40, 200, { sh: false }); else { x.save(); x.beginPath(); x.rect(-w / 2 + 24, -h / 2 + 24, w - 48, 240); x.clip(); cover(IM[img], -w / 2 + 24, -h / 2 + 24, w - 48, 240, { grade: gr_(img), t }); x.restore(); }
    txt(`No. ${i + 1}`, -w / 2 + 28, h / 2 - 72, { s: 22, f: F.mono, c: C.ink2 }); txt(lab, -w / 2 + 28, h / 2 - 34, { s: 38, f: F.fell, id: 'sv' + i });
    stamp(yr, w / 2 - 75, h / 2 - 60, t, a + .3, { s: 40, rot: -6, seed: i }); x.restore(); }));
}
function gr_(img) { return /^(closed_|closing_|craftsman_|kenmore|tower_river|tower1974|carl_station|carl_courthouse|lumber_stamp)/.test(img) ? 'colour' : /^(c18|c19|mh19|hb19|letters|carl_ed|ad1888)/.test(img) ? 'paper' : 'sepia'; }
function sEnd(t, s) {
  ground(.1); const l = t - s.t0, k = seg(l, .2, .8);
  drop('What Happened to Sears?', 150, 230, t, s.t0 + .2, { s: 84, f: F.fell }); txt('THE CATALOG THAT BUILT SMALL-TOWN AMERICA', 154, 290, { s: 28, f: F.sc, ls: 3, a: k });
  hair(154, 320, 154 + 1100 * eo(k), 320, C.ink, 1.5);
  const cr = ['Catalogs  Sears, Roebuck and Co.: Consumers Guide 1897; catalogs 1902, 1912, 1918, 1928; Modern Homes 1911, 1918, 1921 (Internet Archive, public domain)',
    'Photographs  Library of Congress (Harris & Ewing; National Photo Co.; John Margolies; HABS); National Archives (Documerica, U.S. EPA; 1940 Census); Smithsonian National Postal Museum',
    'Sears stereographs 1906 (scans: Richard from USA, CC BY 2.0) · Phillip Pessar (CC BY 2.0) · Tony Webster (CC BY 2.0) · Pokemonprime (CC BY 4.0) · w_lemay (CC0) · TheCatalyst31 (CC0)',
    'Rosemary Thornton; Stilfehler; MOHAI, Webster & Stevens; Winchester Journal 1888 (public domain) · Map data: Natural Earth (public domain), schematic',
    'Words  Richmond Fed; History.com; Wikipedia; Fortune; NPR; Britannica; Madison Historical (SIUE); SEC filings; the catalogs themselves',
    'Music  original score; VSCO 2 CE (CC0), Salamander Grand Piano (CC BY 3.0, Alexander Holm) · Fonts: IM Fell, Old Standard TT, Source Serif 4, Source Sans 3, IBM Plex Mono, Pinyon Script (OFL)'];
  cr.forEach((c, i) => txt(c, 154, 430 + i * 52, { s: 23, f: F.serif, c: C.ink2, a: seg(l, .6 + i * .12, .9 + i * .12), pass: 1 }));
  cut(IM.cut_watch_a, 1640, 250, 260, { rot: 8, a: k, grade: 'paper' });
  const f = seg(l, 15, 17.6); if (f > 0) { x.fillStyle = `rgba(21,17,13,${f})`; x.fillRect(0, 0, W, H); }
}
// ── numbers ───────────────────────────────────────────────────────────────────────────────────────────────
function sBars(t, s) {
  const dk = dark(s); ground(s.dk || 0, { border: !dk }); const c = camAt2(Object.assign({ cam: [[0, 960, 540, 1.0, 0], [-1.1, 970, 530, 1.04, 0]] }, s), t);
  withCam(c, () => {
    plate(IM[s.img], 110, 140, 560, Math.min(740, 560 / (IM[s.img] ? IM[s.img].width / IM[s.img].height : 1)), { rot: -2, grade: gr_(s.img), dark: dk, t });
    txt(s.title, 780, 150, { s: 24, f: F.mono, c: dimC(s), ls: 2, id: 'bt' });
    const n = s.data.length, gap = 80, BW = Math.min(300, (1000 - gap * (n - 1)) / n), X0 = 820, Yb = 830, Hm = 560;
    s.data.forEach(([lab, v, vl], i) => { const a0 = AT(s, s.at[i]), k = eo(seg(t, a0, a0 + .8)); if (k <= 0) return; const h = Hm * v / s.max * k, X = X0 + i * (BW + gap);
      x.fillStyle = i === n - 1 ? C.red : (dk ? '#8c7a62' : '#7d6a52'); x.fillRect(X, Yb - h, BW, h);
      txt(lab, X + BW / 2, Yb + 50, { s: 38, f: F.fell, c: inkC(s), al: 'center', id: 'bl' + i });
      txt(vl, X + BW / 2, Yb - h - 22, { s: 46, f: F.ost, w: 700, c: inkC(s), al: 'center', a: seg(k, .8, 1), id: 'bv' + i }); });
    hair(780, Yb, 1840, Yb, dimC(s), 2);
  });
}
function sDots(t, s) {
  const dk = !s.light, l = t - s.t0; ground(dk ? Math.max(s.dk || 0, .85) : 0, { border: !dk });
  if (s.img) { plate(IM[s.img], 100, 130, 860, 860 / (IM[s.img] ? IM[s.img].width / IM[s.img].height : 1.33) > 700 ? 700 : 860 / (IM[s.img] ? IM[s.img].width / IM[s.img].height : 1.33), { grade: gr_(s.img), dark: dk, t, rot: -1.2 }); if (s.tag) srcTag(s.tag, 90, 104, dk); }
  const per = s.per || 1, N = Math.ceil(s.from / per), cols = N > 2000 ? 70 : N > 600 ? 50 : 20, sz = Math.min(18, 700 / cols), X0 = 1100, Y0 = 170;
  const K = s.keys.map(k => [k[0] < 0 ? -k[0] * s.vd : k[0], k[1]]); let i = 0; while (i < K.length - 1 && K[i + 1][0] <= l) i++;
  const a = K[i], b = K[Math.min(i + 1, K.length - 1)], val = Math.round(lerp(a[1], b[1], b === a ? 0 : eio(seg(l, a[0], b[0])))), lit = Math.ceil(val / per);
  for (let j = 0; j < N; j++) { const X = X0 + (j % cols) * sz, Y = Y0 + Math.floor(j / cols) * sz; x.fillStyle = j < lit ? (dk ? '#E8C27A' : C.red) : (dk ? '#2c241c' : 'rgba(42,32,24,.12)'); x.fillRect(X, Y, sz - 3, sz - 3); }
  const gw = cols * sz, cx = X0 + gw / 2, gh = Math.ceil(N / cols) * sz;
  txt(counter(val), cx, Math.min(900, Y0 + gh + 150), { s: 130, f: F.ost, w: 700, c: dk ? (val <= 9 ? C.red : C.cream) : C.red, al: 'center', id: 'dn' });
  txt(s.label, cx, Math.min(900, Y0 + gh + 150) + 46, { s: 34, f: F.fell, it: 1, c: dk ? C.dim : C.ink2, al: 'center', id: 'dl' });
  if (s.years) { const Y = s.years.map(k => [k[0] < 0 ? -k[0] * s.vd : k[0], k[1]]); let j = 0; while (j < Y.length - 1 && Y[j + 1][0] <= l) j++; txt(Y[j][1], X0, 140, { s: 40, f: F.ost, w: 700, c: C.red, id: 'dy' }); }
  if (s.note) txt(s.note, X0 + gw, 140, { s: 30, f: F.fell, it: 1, c: dk ? C.dim : C.ink2, al: 'right', a: seg(l, 1, 1.4), id: 'dno' });
  if (per > 1) txt(`each square = ${per} houses`, X0, Y0 + gh + 30, { s: 20, f: F.mono, c: dk ? C.dim : C.ink2 });
}
function sStack(t, s) {
  ground(0); const l = t - s.t0, c = camAt2(Object.assign({ cam: [[0, 960, 540, 1.0, 0], [-1.1, 980, 520, 1.05, 0]] }, s), t);
  withCam(c, () => {
    plate(IM[s.img], 140, 110, 600, 780, { rot: -2, grade: 'paper', t, m: 10 }); srcTag('CONSUMERS GUIDE · SPRING 1897', 130, 84);
    const K = s.keys.map(k => [AT(s, k[0]) - s.t0, k[1], k[2]]); let i = 0; while (i < K.length - 1 && K[i + 1][0] <= l) i++;
    const a = K[i], b = K[Math.min(i + 1, K.length - 1)], pages = Math.round(lerp(a[1], b[1], b === a ? 0 : eio(seg(l, b[0] - .9, b[0])))), hpx = pages * .8, X = 1100, Yb = 830;
    x.save(); x.shadowColor = 'rgba(30,18,6,.45)'; x.shadowBlur = 24; x.shadowOffsetY = 10; x.fillStyle = '#d8c69c'; x.fillRect(X, Yb - hpx, 520, hpx); x.restore();
    for (let p = 0; p < hpx; p += 3) { const yy = Yb - p, off = Math.sin(p * 1.7) * 3; x.fillStyle = (p / 3) % 2 ? '#f1e6c8' : '#8f7a55'; x.fillRect(X + off, yy - 1.5, 520, 1.5); }
    if (IM.c1897_n0 && hpx > 4) { x.save(); x.translate(X, Yb - hpx); x.transform(1, 0, -.35, .22, 0, 0); x.drawImage(IM.c1897_n0, 0, -IM.c1897_n0.height * 520 / IM.c1897_n0.width, 520, IM.c1897_n0.height * 520 / IM.c1897_n0.width); x.restore(); } x.strokeStyle = C.ink2; x.lineWidth = 1.2; x.strokeRect(X, Yb - hpx, 520, hpx);
    txt(counter(pages) + ' pages', X + 200, Yb - hpx - 175, { s: 64, f: F.ost, w: 700, c: C.red, al: 'center', id: 'stk' });
    txt(b[0] <= l ? b[2] : a[2], X + 560, Yb - 20, { s: 48, f: F.ost, w: 700, c: C.ink, al: 'left', id: 'sty' });
  });
}
function sFlip(t, s) {
  ground(0); const l = t - s.t0, n = s.words.length, per = s.vd * .92 / n, i = Math.min(n - 1, Math.floor(l / per)), P = s.pages, pg = P[Math.floor(l / per) % P.length];
  const c = { x: 960, y: 540, z: 1 + .02 * Math.sin(l), r: 0 };
  withCam(c, () => { for (let j = 3; j >= 0; j--) { const im = IM[P[(Math.floor(l / per) + j) % P.length]]; plate(im, 650 + j * 14, 70 + j * 10, 620, 830, { rot: j * 1.5 - 1, grade: 'paper', t, m: 8, a: j ? .9 : 1 }); }
    const f = (l / per) % 1; if (f < .25) { const k = f / .25; x.save(); x.globalAlpha = 1 - k; x.translate(960, 485); x.rotate(-k * 1.3); x.translate(-310 - k * 400, -415); plate(IM[pg], 0, 0, 620, 830, { grade: 'paper', t, m: 8 }); x.restore(); }
    for (let j = 0; j <= i; j++) { const a = s.t0 + j * per; drop(s.words[j], j % 2 ? 1620 : 330, 230 + j * 92, t, a, { s: 70, f: F.fell, al: 'center', id: 'fw' + j }); } });
}
function sConveyor(t, s) {
  ground(0); const l = t - s.t0, c = camAt2(Object.assign({ cam: [[0, 900, 540, 1.08, 0], [-1.1, 960, 520, 1.0, 0]] }, s), t);
  withCam(c, () => {
    plate(IM[s.img], 170, 100, 1020, 824, { grade: 'sepia', t, rot: -1 }); srcTag(s.tag, 160, 74);
    const paths = [[[220, 360], [1160, 300]], [[220, 520], [1160, 470]], [[260, 700], [1160, 660]]];
    paths.forEach((p, pi) => { for (let j = 0; j < 7; j++) { const u = ((l * .22 + j / 7 + pi * .13) % 1), X = lerp(p[0][0], p[1][0], u), Y = lerp(p[0][1], p[1][1], u);
      x.save(); x.translate(X, Y); x.rotate(-.06); x.fillStyle = '#f2e8d0'; x.strokeStyle = C.ink; x.lineWidth = 1.2; x.fillRect(-34, -22, 68, 44); x.strokeRect(-34, -22, 68, 44);
      for (let q = 0; q < 3; q++) hair(-26, -10 + q * 10, 20 - q * 8, -10 + q * 10, C.pen, 1.5); x.restore(); } });
    enter(t, s, { at: -.45, in: 'slide', from: [700, 0] }, () => plate(IM[s.img2], 1240, 200, 560, 576, { rot: 2.5, grade: 'sepia', t, m: 12, cap: 'Train shed · 1906' }));
  });
}
function sLetter(t, s) {
  ground(0); const l = t - s.t0, c = camAt2(Object.assign({ cam: [[0, 960, 540, 1.0, 0], [-1.1, 980, 540, 1.03, 0]] }, s), t);
  withCam(c, () => {
    const im = IM[s.img], h = 820, w = h * (im ? im.width / im.height : .84); plate(im, 120, 100, w, h, { grade: 'paper', t, m: 10, rot: -1.5 }); srcTag('SEARS CATALOGUE · SPRING 1897 · p. 28', 110, 74);
    const k = eo(seg(t, s.t0 + .3, s.t0 + .9)); x.save(); x.globalCompositeOperation = 'multiply'; x.fillStyle = 'rgba(214,72,52,.38)'; x.fillRect(120, 100 + h * s.hl[0], w * k, h * (s.hl[1] - s.hl[0])); x.restore();
    const X = 900, Y = 150, W_ = 900, H_ = 650; x.save(); x.translate(X + W_ / 2, Y + H_ / 2); x.rotate(1 * Math.PI / 180); x.translate(-W_ / 2, -H_ / 2);
    x.shadowColor = 'rgba(30,18,6,.4)'; x.shadowBlur = 28; x.shadowOffsetY = 10; x.fillStyle = '#f1e7cf'; x.fillRect(0, 0, W_, H_); x.shadowColor = 'transparent';
    for (let i = 0; i < 12; i++) hair(60, 170 + i * 42, W_ - 60, 170 + i * 42, 'rgba(60,80,120,.12)', 1);
    txt(s.head, W_ / 2, 76, { s: 40, f: F.sc, al: 'center', ls: 2, id: 'lh' }); txt(`${s.place}, ${s.date}`, W_ - 60, 128, { s: 30, f: F.fell, it: 1, al: 'right', c: C.ink2, id: 'lp' });
    txt('Gentlemen:', 60, 200, { s: 34, f: F.fell, it: 1, a: seg(l, .5, .8) });
    s.q.forEach((q, i) => { const a = s.t0 + .6 + i * s.vd * .27, n = Math.floor(q.length * seg(t, a, a + Math.max(.8, s.vd * .25))); if (n > 0) txt(q.slice(0, n), 60, 290 + i * 84, { s: 54, f: F.fell, it: 1, id: n === q.length ? 'lq' + i : null }); });
    hand(s.who, 480, 590, t, s.t0 + s.vd * .85, .9, { s: 62, id: 'lw' }); x.restore();
    nameCard(s.who, 'A CUSTOMER · CHAPEL HILL, N.C. · 1897', 1060, 905, 'l', seg(l, 1.0, 1.4));
  });
}
function sLedger(t, s) {
  const dk = !!s.dark; ground(dk ? .85 : s.dk || 0, { border: !dk }); const l = t - s.t0, c = camAt2(Object.assign({ cam: [[0, 960, 540, 1.0, 0], [-1.1, 960, 520, 1.05, 0]] }, s), t);
  withCam(c, () => {
    const X = 260, Y = 110, W_ = 1400, H_ = 760; x.save(); x.shadowColor = 'rgba(0,0,0,.45)'; x.shadowBlur = 30; x.shadowOffsetY = 12; x.fillStyle = '#e8e2c8'; x.fillRect(X, Y, W_, H_); x.restore();
    for (let i = 0; i < 16; i++) hair(X, Y + 120 + i * 40, X + W_, Y + 120 + i * 40, 'rgba(70,110,140,.35)', 1);
    [X + 220, X + 1050].forEach(cx => { hair(cx, Y, cx, Y + H_, 'rgba(180,50,40,.55)', 1.5); hair(cx + 6, Y, cx + 6, Y + H_, 'rgba(180,50,40,.55)', 1.5); });
    txt('LEDGER · SEARS, ROEBUCK AND CO.', X + 40, Y + 70, { s: 30, f: F.sc, ls: 3, c: C.ink2 });
    s.rows.forEach(([d, what, amt], i) => { const a = s.t0 + .3 + i * s.vd * .3, Yr = Y + 200 + i * 120; hand(d, X + 30, Yr, t, a, .5, { s: 48, id: 'ld' + i }); hand(what, X + 250, Yr, t, a + .5, 1.2, { s: 48, id: 'lw' + i });
      if (amt) hand(amt, X + 1080, Yr, t, a + 1.6, .8, { s: 52, c: C.red, id: 'la' + i }); });
    if (s.big) stamp(s.big, 960, Y + 560, t, s.t0 + s.vd * .3, { s: 96, rot: -4, id: 'lbig' });
    if (s.note) txt(s.note, 960, Y + 700, { s: 34, f: F.fell, it: 1, al: 'center', c: C.ink2, a: seg(l, s.vd * .5, s.vd * .5 + .4), id: 'lno' });
  });
}
function sTower(t, s) {
  ground(.35, { border: true }); const l = t - s.t0, c = camAt2(Object.assign({ cam: [[0, 960, 600, 1.05, 0], [-1.1, 960, 520, 1.0, 0]] }, s), t);
  withCam(c, () => {
    plate(IM.tower1974, 110, 90, 500, 828, { rot: -1.5, grade: 'colour', t }); srcTag('DOCUMERICA · U.S. EPA · 1974', 100, 64);
    const Yb = 880, S = 620 / 1451, k = eio(seg(l, .6, s.vd * .55));
    const bar = (X, hft, lab, k2, col) => { const h = hft * S * k2; x.fillStyle = col; x.fillRect(X, Yb - h, 150, h); x.strokeStyle = C.ink; x.lineWidth = 1.5; x.strokeRect(X, Yb - h, 150, h);
      for (let y = Yb - 12; y > Yb - h + 6; y -= 12) hair(X + 10, y, X + 140, y, 'rgba(0,0,0,.18)', 1);
      txt(counter(Math.round(hft * k2)) + ' ft', X + 75, Yb - h - 22, { s: 44, f: F.ost, w: 700, c: col === C.red ? C.red : C.ink, al: 'center', id: 'tw' + lab });
      txt(lab, X + 75, Yb + 46, { s: 30, f: F.fell, it: 1, al: 'center', id: 'tl' + lab }); };
    bar(900, 249, 'West Side plant, 1906', seg(l, .2, .8), '#9c8a70'); bar(1260, 1451, 'Sears Tower, 1973', k, C.red);
    hair(760, Yb, 1700, Yb, C.ink, 2);
    if (seg(l, s.vd * .6, s.vd * .6 + .4) > 0) txt('tallest in the world · 1973–1998', 1340, 140, { s: 38, f: F.fell, it: 1, al: 'center', a: seg(l, s.vd * .6, s.vd * .6 + .4), id: 'tt' });
  });
}
function sRivals(t, s) {
  ground(.35); const l = t - s.t0, c = camAt2(Object.assign({ cam: [[0, 960, 540, 1.0, 0], [-1.1, 960, 540, 1.04, 0]] }, s), t);
  withCam(c, () => {
    mapDraw(560, 120, 800, { rails: false }); const R = rnd(3), sc = 800 / MAP.W; const n = Math.round(160 * eio(seg(l, .8, s.vd * .6)));
    for (let i = 0; i < 160; i++) { const p = MAP.towns.Carlinville, xx = 560 + (200 + R() * 750) * sc, yy = 120 + (220 + R() * 400) * sc; if (i < n) { x.fillStyle = 'rgba(42,32,24,.55)'; x.beginPath(); x.arc(xx, yy, 4, 0, 7); x.fill(); } }
    drop('Walmart', 300, 300, t, s.t0 + .3, { s: 90, f: F.fell, al: 'center' }); txt('from Arkansas · 1962', 300, 350, { s: 30, f: F.fell, it: 1, al: 'center', a: seg(l, .8, 1.1), id: 'r1' });
    drop('Home Depot', 1620, 300, t, AT(s, -.55), { s: 90, f: F.fell, al: 'center' }); txt('one thing, for less · 1978', 1620, 350, { s: 30, f: F.fell, it: 1, al: 'center', a: seg(t, AT(s, -.55) + .4, AT(s, -.55) + .7), id: 'r2' });
    srcTag('MAP · SCHEMATIC · DOTS ILLUSTRATIVE, NOT STORE LOCATIONS', 560, 110);
  });
}
function sFan(t, s) {
  ground(.75); const l = t - s.t0, P = s.pages, n = P.length;
  P.forEach((p, i) => { const k = eo(seg(l, .1 + i * .12, .6 + i * .12)), fall = eio(seg(l, s.vd * .55 + i * .18, s.vd * .55 + i * .18 + 1.0));
    const an = (i - (n - 1) / 2) * .16 * k; x.save(); x.translate(760, 980 + fall * 700); x.rotate(an + fall * (i - 2) * .4); x.globalAlpha = 1 - fall * .8;
    plate(IM[p], -230, -880, 460, 620, { grade: 'paper', t, m: 8, dark: true }); x.restore(); });
  const k = seg(l, .8, s.vd * .8); if (k > 0) { const v = Math.round(lerp(0, s.count.per_day, eo(k)));
    txt('−$' + counter(v), 1450, 470, { s: 104, f: F.ost, w: 700, c: C.red, al: 'center', id: 'fanv' }); txt(s.count.label, 1450, 540, { s: 38, f: F.fell, it: 1, c: C.cream, al: 'center', id: 'fanl' }); }
  srcTag('SEARS CATALOGS · 1897–1928 (INTERNET ARCHIVE)', 540, 64, true);
}
// ── the house in a box (phases: parts, carlin, wipe, today) ─────────────────────────────────────────────────
function lumber(X, Y, w, rot, label) { x.save(); x.translate(X, Y); x.rotate(rot); x.fillStyle = C.wood; x.strokeStyle = C.wood2; x.lineWidth = 1.5; x.fillRect(-w / 2, -10, w, 20); x.strokeRect(-w / 2, -10, w, 20);
  txt(label, 0, 7, { s: 15, f: F.mono, al: 'center', c: '#5b3a1a' }); x.restore(); }
function boxcar(X, Y, open) { x.save(); x.translate(X, Y); x.fillStyle = '#6b3a24'; x.fillRect(0, 0, 600, 150); x.strokeStyle = C.ink; x.lineWidth = 2; x.strokeRect(0, 0, 600, 150);
  for (let i = 1; i < 12; i++) hair(i * 50, 4, i * 50, 146, 'rgba(0,0,0,.25)', 1);
  x.fillStyle = '#2b1a10'; x.fillRect(240, 16, 120 * open + 4, 134); txt('SEARS, ROEBUCK & CO.', 120, 88, { s: 22, f: F.sc, c: C.cream, al: 'center' }); txt('READY-CUT', 480, 88, { s: 22, f: F.sc, c: C.cream, al: 'center' });
  x.fillStyle = C.ink; [80, 520].forEach(w => { x.beginPath(); x.arc(w, 156, 20, 0, 7); x.fill(); }); x.restore(); }
function sHouse2(t, s) {
  const l = t - s.t0, ph = s.phase, dk = dark(s); ground(s.dk || 0);
  const EX = 160, EY = 90, EW = 1100, EH = Math.round(EW * 1284 / 2172);
  if (ph === 'parts') {
    const c = camAt2(Object.assign({ cam: [[0, 960, 540, 1.0, 0], [-1.1, 900, 520, 1.06, 0]] }, s), t);
    withCam(c, () => {
      miniMap(t, s, { x: 1280, y: 90, w: 520, towns: [['Chicago', 0]], routes: [['Chicago', 'Carlinville', .2, 1.6, -.25]] });
      boxcar(lerp(-700, 160, eio(seg(l, 0, 1.2))), 720, seg(l, 1.2, 1.6)); const R = rnd(13), N = 60, k0 = 1.6, span = Math.max(2, s.vd * .55);
      for (let i = 0; i < N; i++) { const st = k0 + span * i / N, k = seg(l, st, st + .7), row = Math.floor(i / 6), col = i % 6, tx = 840 + col * 150 + (row % 2) * 40, ty = 640 - row * 26;
        const w = 120 + R() * 30; if (k <= 0) continue; const e = eio(k), px = lerp(460, tx, e), py = lerp(780, ty, e) - Math.sin(e * Math.PI) * 200; lumber(px, py, w, (1 - e) * (R() * 4 - 2), String(1000 + i * 37)); }
      const v = Math.round(30000 * eo(seg(l, k0, k0 + span + .6)));
      txt(counter(v), 1520, 560, { s: 120, f: F.ost, w: 700, c: C.red, al: 'center', id: 'hp' }); txt('parts, as many as', 1520, 440, { s: 36, f: F.fell, it: 1, al: 'center', id: 'hp2' });
      enter(t, s, { at: -.75, in: 'drop' }, () => { x.save(); x.translate(1500, 760); x.rotate(-.05); x.fillStyle = '#4a2f22'; x.fillRect(-150, -90, 300, 180); x.strokeStyle = '#d9c08a'; x.lineWidth = 2; x.strokeRect(-140, -80, 280, 160);
        txt('INSTRUCTIONS', 0, -10, { s: 26, f: F.sc, c: '#e9d6a8', al: 'center' }); txt('Honor Bilt', 0, 34, { s: 30, f: F.fell, it: 1, c: '#e9d6a8', al: 'center' }); x.restore(); });
    }); return;
  }
  const img = IM.carlin_elev;
  const frame = () => { x.save(); x.shadowColor = 'rgba(30,18,6,.4)'; x.shadowBlur = 26; x.shadowOffsetY = 10; x.fillStyle = C.mount; x.fillRect(EX - 16, EY - 16, EW + 32, EH + 32); x.restore(); };
  if (ph === 'carlin') {
    const c = camAt2(Object.assign({ cam: [[0, 960, 520, 1.0, 0], [-1.1, 880, 560, 1.05, 0]] }, s), t);
    withCam(c, () => { frame(); const R = rnd(5), cols = 8, rows = 6, cw = EW / cols, ch = EH / rows, span = Math.max(2.2, s.vd * .5);
      for (let i = 0; i < cols * rows; i++) { const cx = i % cols, cy = rows - 1 - Math.floor(i / cols), land = .2 + span * i / (cols * rows) + R() * .2, k = seg(l, land, land + .55), tx = EX + cx * cw, ty = EY + cy * ch;
        if (k >= 1) { x.save(); x.beginPath(); x.rect(tx - .5, ty - .5, cw + 1, ch + 1); x.clip(); cover(img, EX, EY, EW, EH, { grade: 'sepia', t }); x.restore(); }
        else if (k > 0) { const e = eio(k); lumber(lerp(1500 + R() * 200, tx + cw / 2, e), lerp(980, ty + ch / 2, e) - Math.sin(e * Math.PI) * 240, cw * .9, (1 - e) * 2, String(3031 + i)); } else R(); }
      x.strokeStyle = C.ink; x.lineWidth = 2; x.strokeRect(EX, EY, EW, EH);
      const pk = seg(l, s.vd * .45, s.vd * .8); if (IM.carlin_plan1 && pk > 0) { x.save(); x.beginPath(); x.rect(1330, 120, 470 * pk, 1000); x.clip(); x.drawImage(IM.carlin_plan1, 1330, 120, 470, 507); x.restore(); }
      if (IM.carlin_title) cut(IM.carlin_title, EX + EW / 2, EY + EH + 70, 900, { sh: false, a: seg(l, s.vd * .3, s.vd * .3 + .4) });
      stamp('$1,172', 1560, 760, t, AT(s, -.82), { s: 96, rot: -6, id: 'hc' }); });
    return;
  }
  if (ph === 'wipe') {
    const c = camAt2(Object.assign({ cam: [[0, 900, 520, 1.0, 0], [-1.1, 760, 480, 1.08, 0]] }, s), t);
    withCam(c, () => { frame(); cover(img, EX, EY, EW, EH, { grade: 'sepia', t }); const w0 = AT(s, .3) - s.t0, wk = eio(seg(l, w0, w0 + 1.8)), XW = EX + EW * wk;
      x.save(); x.beginPath(); x.rect(EX, EY, EW * wk, EH); x.clip(); cover(IM.carl1921_street2, EX, EY, EW, EH, { grade: 'sepia', t, fy: .55 }); x.restore();
      if (wk > 0 && wk < 1) { x.save(); x.fillStyle = '#d9c08a'; x.fillRect(XW - 9, EY - 30, 18, EH + 60); x.strokeStyle = C.ink; x.lineWidth = 1.5; x.strokeRect(XW - 9, EY - 30, 18, EH + 60);
        for (let i = 0; i < 24; i++) hair(XW - 9, EY - 20 + i * (EH + 40) / 24, XW - (i % 4 ? 2 : -3), EY - 20 + i * (EH + 40) / 24, C.ink, 1); x.restore(); }
      x.strokeStyle = C.ink; x.lineWidth = 2; x.strokeRect(EX, EY, EW, EH);
      if (wk >= 1) capPill('Street view of Sears, Roebuck and Co.\nhouses at Carlinville, Ill.', EX + EW - 30, EY + EH - 6, 'r', false, seg(l, w0 + 1.8, w0 + 2.2));
      enter(t, s, { at: -.5, in: 'slide', from: [500, 0] }, () => plate(IM.carl1921_street1, 1300, 520, 520, 520 / 3.05, { rot: 3, grade: 'sepia', t, m: 10 }));
      srcTag('HONOR BILT MODERN HOMES · 1921 · pp. 4–5 (INTERNET ARCHIVE)', EX - 10, EY - 26); });
    return;
  }
  if (ph === 'today') {   // 156 houses, about 150 still standing
    const c = camAt2(Object.assign({ cam: [[0, 960, 540, 1.0, 0], [-1.1, 960, 520, 1.04, 0]] }, s), t);
    withCam(c, () => { plate(IM.carl1921_street1, 160, 90, 1600, 525, { grade: 'sepia', t, z: lerp(1, 1.05, seg(t, s.t0, s.t1)) }); srcTag('HONOR BILT MODERN HOMES · 1921 · p. 5', 150, 64);
      const n = 156, cols = 39, X0 = 200, Y0 = 690, k = seg(l, .4, s.vd * .6);
      for (let i = 0; i < n; i++) { const X = X0 + (i % cols) * 39, Y = Y0 + Math.floor(i / cols) * 46, on = i < Math.round(150 * eo(k));
        x.fillStyle = on ? C.red : 'rgba(42,32,24,.18)'; x.beginPath(); x.moveTo(X, Y + 14); x.lineTo(X + 14, Y); x.lineTo(X + 28, Y + 14); x.lineTo(X + 28, Y + 36); x.lineTo(X, Y + 36); x.closePath(); x.fill(); }
      txt('≈ 150 of 156 · still standing', 1760, 660, { s: 34, f: F.fell, it: 1, al: 'right', a: seg(l, s.vd * .5, s.vd * .5 + .4), id: 'htd' }); });
  }
}
function sSchoper(t, s) {
  ground(0); const l = t - s.t0, img = IM.schopper1921, X = 140, Y = 150, w = 1640, h = Math.round(1640 / 3.63), gone = eio(seg(l, s.vd * .25, s.vd * .7));
  const c = camAt2(Object.assign({ cam: [[0, 960, 520, 1.0, 0], [-1.1, 960, 560, 1.04, 0]] }, s), t);
  withCam(c, () => {
    x.save(); x.shadowColor = 'rgba(30,18,6,.4)'; x.shadowBlur = 26; x.fillStyle = C.mount; x.fillRect(X - 16, Y - 16, w + 32, h + 32); x.restore();
    cover(img, X, Y, w, h, { grade: 'sepia', t }); x.save(); x.globalAlpha = gone * .7; x.fillStyle = '#cdb98f'; x.fillRect(X, Y + h * .35, w, h * .65); x.restore();
    x.strokeStyle = C.ink; x.lineWidth = 2; x.strokeRect(X, Y, w, h); srcTag('SCHOPPER, ILL. · HONOR BILT MODERN HOMES · 1921', X - 10, Y - 26);
    const R = rnd(4); for (let i = 0; i < 40; i++) { const st = s.vd * .2 + i * .06, k = seg(l, st, st + .9); if (k <= 0 || k >= 1) continue; const e = eio(k);
      lumber(lerp(X + 200 + R() * 1200, 1600, e), lerp(Y + h * .5 + R() * 60, 860, e) - Math.sin(e * Math.PI) * 160, 110, e * 2, String(200 + i)); }
    boxcar(lerp(900, 2100, eio(seg(l, s.vd * .72, s.vd * .95))), 760, 0);
    stamp('GHOST TOWN', 960, Y + h + 120, t, AT(s, -.85), { s: 84, rot: -5, id: 'sg' });
  });
}
Object.assign(SCN, { spread: sSpread, map: sMap, calendar: sCalendar, title: sTitle, seven: sSeven, end: sEnd, bars: sBars, dots: sDots, stack: sStack, flip: sFlip,
  conveyor: sConveyor, letter: sLetter, ledger: sLedger, tower: sTower, rivals: sRivals, fan: sFan, house: sHouse2, schoper: sSchoper });
