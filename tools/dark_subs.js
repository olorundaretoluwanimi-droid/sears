function subs(t) {   // the series' captions: Plex Sans 500, 47 px, centred, black shadow, no band
  const s = FILM.subs.find(q => t >= q.t0 && t < q.t1); if (!s) return;
  x.save(); x.shadowColor = 'rgba(0,0,0,1)'; x.shadowBlur = 14; txt(s.text, W / 2, 1022, { s: 47, w: 500, al: 'center' }); txt(s.text, W / 2, 1022, { s: 47, w: 500, al: 'center' }); x.restore();
}
function srcTag(s, X, Y) { txt(s, X + 14, Y, { s: 17, f: 'Mono', w: 600, ls: 1, c: C.cream }); x.fillStyle = C.cream; x.fillRect(X, Y - 12, 6, 13); }

