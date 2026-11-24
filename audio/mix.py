#!/usr/bin/env python3
"""Score, foley and narration for "What Happened to Sears?" → out/mix.wav (48 kHz stereo). All timing from ../film.json.
Score (core/audio/sampler: VSCO 2 CE CC0, Salamander piano CC BY 3.0): a parlour upright with a light ragtime lilt (pizzicato bass on 1
and 3, soft chords on 2 and 4), clarinet tune, string pad; glockenspiel for the Christmas pages; a horn for Carlinville; it thins to solo
piano in minor for the decline and brings the opening tune back, slower, at the end. Music dips ≈ 8 dB under the voice.
Foley from the scenes: paper for every page curl and photo laid down, pen on the order blanks, a rubber stamp for prices and dates,
one cash-register bell (the first $14), a train and wood for the house, the plant's conveyor, a calendar page torn off."""
import json, os, sys
import numpy as np, soundfile as sf, soxr
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.environ.get('LIB') or os.path.expanduser('~/lemo-opuscar'); sys.path.insert(0, LIB)
from core.audio import sampler as S
from core.audio.sfx import SR, add, bp, hp, lp, noise, env_exp, t_, thump, norm, limit, brown, ding, click
F = json.load(open(os.path.join(D, 'film.json'), encoding='utf-8')); DUR = F['dur']; SC = F['scenes']
N = int(DUR * SR); S.seed(9); np.random.seed(9)
BPM = 84; BEAT = 60 / BPM; BAR = 4 * BEAT
CH = {'F': ('F2', ['A3', 'C4', 'F4']), 'Bb': ('A#1', ['A#3', 'D4', 'F4']), 'C7': ('C2', ['A#3', 'C4', 'E4']), 'Dm': ('D2', ['A3', 'D4', 'F4']),
      'Gm': ('G1', ['A#3', 'D4', 'G4']), 'A7': ('A1', ['C#4', 'E4', 'G4']), 'C': ('C2', ['G3', 'C4', 'E4']), 'Am': ('A1', ['A3', 'C4', 'E4'])}
TUNE = {'F': ['A4', 'C5', 'D5', 'C5'], 'Bb': ['D5', 'C5', 'A#4', 'A4'], 'C7': ['G4', 'A#4', 'C5', 'A#4'], 'Dm': ['F4', 'A4', 'D5', 'A4'],
        'Gm': ['G4', 'A#4', 'D5', 'A#4'], 'A7': ['E4', 'G4', 'C#5', 'A4'], 'C': ['G4', 'C5', 'E5', 'C5'], 'Am': ['E4', 'A4', 'C5', 'A4']}
ev = []
def E(*a): ev.append(a)
def oct_(n, k): return n[:-1] + str(int(n[-1]) + k)
def bar(t0, name, st):
    b, ch = CH[name]; g = st['g']
    if st['rag']:   # bass on 1 and 3, chord on 2 and 4 (light stride), swung eighths
        E(t0, 'contrabass_pizz', b, .9, .34, -.1, .5 * g); E(t0 + 2 * BEAT, 'contrabass_pizz', oct_(b, 1) if b[-1] == '1' else b, .9, .3, -.1, .42 * g)
        for k in (1, 3):
            for i, n in enumerate(ch): E(t0 + k * BEAT, 'upright', n, .5, .22, -.2 + .2 * i, .34 * g)
    else:            # gentle broken chord
        for i, n in enumerate([oct_(b, 1) if b[-1] in '12' else b] + ch + ch[1:2]): E(t0 + i * BAR / 5, st['arp'], n, 1.8, .2 + .04 * (i == 0), -.25 + .1 * i, .34 * g)
    if st['pad']:
        for i, n in enumerate(ch): E(t0, 'violas' if i < 2 else 'violins', oct_(n, -1) if i == 0 else n, BAR + .3, .2, (-.3, .1, .35)[i], .16 * g * st['pad'])
    if st['lo']: E(t0, 'cellos', b if b[-1] != '1' else oct_(b, 1), BAR + .3, .22, -.2, .22 * g)
STY = {   # progression, rag?, arpeggio instrument, pad level, low strings, gain, melody instrument
 'open': (['F', 'Dm', 'Bb', 'C7'], 0, 'upright', 1, 0, .8, None),
 'c1': (['F', 'Bb', 'F', 'C7'], 1, 'upright', .6, 0, .9, 'clarinet'), 'c2': (['F', 'Dm', 'Gm', 'C7'], 1, 'upright', .7, 0, .9, 'clarinet'),
 'c3': (['Bb', 'F', 'Gm', 'C7'], 0, 'upright', 1, 1, .95, 'horn'), 'c4': (['F', 'A7', 'Dm', 'C7'], 1, 'upright', .6, 0, .9, 'clarinet'),
 'c5': (['Dm', 'Bb', 'F', 'C'], 0, 'piano', 1, 1, .8, None), 'c6': (['Dm', 'Bb', 'Gm', 'A7'], 0, 'piano', 0, 0, .6, None),
 'c7': (['Dm', 'Bb', 'Am', 'Dm'], 0, 'piano', 0, 1, .5, None), 'end': (['F', 'Dm', 'Bb', 'C7'], 0, 'upright', 1, 1, .9, 'horn')}
LCH = {l['id']: l['chapter'] for l in json.load(open(os.path.join(D, 'audio/lines.json'), encoding='utf-8'))}
# chapter spans: an order blank starts a chapter; the music of a chapter starts on its blank
spans, cur, start = [], 'open', 0.0
for i, s in enumerate(SC):
    if s['type'] == 'blank' or s['type'] == 'end':
        nxt = 'end' if s['type'] == 'end' else next((LCH[x['line']] for x in SC[i + 1:] if x.get('line')), 'end')
        if nxt == cur: continue
        spans.append((cur, start, s['t0'])); start, cur = s['t0'], nxt
spans.append((cur, start, DUR))
XMAS = [(s['t0'], s['t1']) for s in SC if s.get('line') in ('n35', 'n36', 'n37', 'n12')]
for ch, a, b in spans:
    prog, rag, arp, pad, lo, g, mel = STY[ch]; st = dict(rag=rag, arp=arp, pad=pad, lo=lo, g=g); t, i = a, 0
    if ch != 'open': E(a, 'timpani', 'F2', 2.0, .3, 0, .28 * g)
    end_slow = ch == 'end'
    while t < b - 1.0:
        name = prog[i % len(prog)]; bar(t, name, st)
        if mel and i % 4 in (1, 2):
            for j, n in enumerate(TUNE[name]): E(t + j * BEAT, mel, n, BEAT * (1.6 if j == 3 else .95), .24, .05, .26 * g)
        if any(x0 <= t < x1 for x0, x1 in XMAS):
            for j, n in enumerate(TUNE[name]): E(t + j * BEAT + BEAT / 2, 'glockenspiel', oct_(n, 1), 1.0, .2, .3, .2)
        t += BAR * (1.25 if end_slow else 1); i += 1
mus = S.render(ev, dur=DUR, master=False)[:N]; mus = S.room(mus, size=.55, mix=.22)
if len(mus) < N: mus = np.pad(mus, ((0, N - len(mus)), (0, 0)))
# ── foley ──
fx = np.zeros((N, 2), np.float32)
def paper(v=1.0, d=.28): return bp(noise(d), 900, 6500) * env_exp(d, .07) * (1 - np.exp(-t_(d) / .012)) * v
def curl(v=1.0): d = .7; x = bp(noise(d), 700, 7000) * np.sin(np.pi * t_(d) / d) ** 1.5; return norm(x) * .5 * v
def pen(d, v=1.0):
    x = bp(noise(d), 2500, 8000) * (0.6 + 0.4 * np.sin(2 * np.pi * 9 * t_(d)) ** 2); return norm(x) * .18 * v
def stampfx(v=1.0): return norm(thump(.8, 110)[:int(.25 * SR)] + np.pad(paper(.6, .12), (0, int(.13 * SR)))[:int(.25 * SR)]) * v
def wood(v=1.0): d = .12; return norm(bp(noise(d), 300, 2400) * env_exp(d, .018)) * v
def tear(v=1.0): d = .45; x = bp(noise(d), 1500, 9000) * (np.abs(np.sin(2 * np.pi * 31 * t_(d))) ** 3) * np.linspace(1, .3, len(t_(d))); return norm(x) * .5 * v
def train(d=4.0, v=1.0):
    x = lp(brown(d), 300)[:int(d * SR)] * 2; tt = t_(d); cl = np.zeros_like(tt)
    for k in np.arange(.15, d, .42): i0 = int(k * SR); seg = wood(.6); cl[i0:i0 + len(seg)] += seg[:len(cl) - i0]
    return norm(x * np.sin(np.pi * tt / d) + cl * .5) * v
def rattle(d, v=1.0): tt = t_(d); return norm(bp(noise(d), 400, 3000) * (.5 + .5 * np.sin(2 * np.pi * 7 * tt) ** 2)) * .25 * v
def AT(s, v): return s['t0'] + .4 if v is None else s['t0'] + (-v) * s.get('vd', s['t1'] - s['t0']) if v < 0 else s['t0'] + v
first_cash = True
for s in SC:
    if s.get('curl'): add(fx, curl(), s['t0'], .55, .1)
    ty = s['type']
    if ty == 'blank':
        a = s['t0'] + .5; add(fx, pen(.5), a, .5, -.2); add(fx, pen(.9), a + .55, .5, 0); add(fx, pen(.45), a + 1.55, .5, .1); add(fx, stampfx(), a + 2.15, .55, .2)
    for it in s.get('items', []):
        a = AT(s, it.get('at', 0))
        if it['k'] in ('ph', 'cut') and it.get('in') != 'none' and not (it.get('at') == 0 and s.get('curl')): add(fx, paper(.7), a, .32, -.1)
        elif it['k'] == 'stamp':
            add(fx, stampfx(), a, .5, .15)
            if first_cash and it.get('text') == '$14': add(fx, ding(.7), a + .12, .35, .2); first_cash = False
        elif it['k'] == 'hand': add(fx, pen(1.8), a + .15, .45, 0)
        elif it['k'] == 'drop': add(fx, click(.6, .5), a + .2, .12, 0)
    if ty == 'house' and s.get('phase') in ('parts', 'carlin'):
        if s['phase'] == 'parts': add(fx, train(4.0), s['t0'], .35, -.3)
        for k in range(14): add(fx, wood(), s['t0'] + 1.7 + k * min(.35, s['vd'] * .5 / 14), .22, (k % 3 - 1) * .3)
    if ty == 'schoper': add(fx, train(3.5), s['t0'] + s['vd'] * .7, .3, .3)
    if ty == 'conveyor': add(fx, rattle(min(s['t1'] - s['t0'], 8)), s['t0'], .35, 0)
    if ty == 'calendar': add(fx, tear(), AT(s, s.get('flip')), .5, 0)
    if ty in ('ledger', 'letter'): add(fx, pen(1.5), s['t0'] + .4, .35, 0)
fx += np.repeat(lp(brown(DUR), 400)[:N, None] * .006, 2, axis=1).astype(np.float32)
# ── narration (cleaned: breaths out, long pauses shortened) ──
voc = np.zeros((N, 2), np.float32); VO = {}
for k, at in F['vo'].items():
    y, sr = sf.read(os.path.join(D, f'audio/vo/{k}.wav')); y = y if y.ndim == 1 else y.mean(1)
    y = soxr.resample(y, sr, SR); y = y / (np.sqrt(np.mean(y[np.abs(y) > .01] ** 2)) + 1e-9) * .11
    add(voc, y, at, 1.0, 0); VO[k] = (at, at + len(y) / SR)
g = np.ones(N)
for a, b in VO.values(): g[int(a * SR):int(b * SR)] = np.minimum(g[int(a * SR):int(b * SR)], .4)
from scipy.ndimage import uniform_filter1d
g = uniform_filter1d(g, int(.5 * SR)); mus *= g[:, None]; fx *= (.65 + .35 * g)[:, None]
out = mus * 3.0 + fx * .75 + voc
tail = int(3.0 * SR); out[-tail:] *= np.linspace(1, 0, tail)[:, None]
def tp_limit(x, ceil):
    from scipy.signal import resample_poly
    from scipy.ndimage import maximum_filter1d, minimum_filter1d, uniform_filter1d
    up = resample_poly(x, 4, 1); n = int(.004 * SR * 4)
    g = np.minimum(1, ceil / np.maximum(maximum_filter1d(np.abs(up), 2 * n + 1), 1e-9)); g = uniform_filter1d(minimum_filter1d(g, 2 * n + 1), n)
    return resample_poly(up * g, 1, 4)[:len(x)]
out = np.stack([tp_limit(limit(out[:, c], .5), .45) for c in range(2)], 1)
os.makedirs(os.path.join(D, 'out'), exist_ok=True); sf.write(os.path.join(D, 'out/mix.wav'), out.astype(np.float32), SR)
def db(a): return 20 * np.log10(np.sqrt(np.mean(a ** 2)) + 1e-12)
vm = np.zeros(N, bool)
for a, b in VO.values(): vm[int(a * SR):int(b * SR)] = True
print('mix', round(DUR, 1), 's | voice', round(db(voc[vm]), 1), 'bed under voice', round(db((mus * 3 + fx * .75)[vm]), 1), 'music alone', round(db((mus * 3)[~vm]), 1))
