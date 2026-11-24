#!/usr/bin/env python3
"""raw/* → assets/ for the page. Photos and pages → <name>.jpg (longest side capped). CROPS → crops from catalog pages:
'rect' keeps the paper (a clipping), 'ink' turns the paper transparent (line art: floor plans, engravings, type) → .png.
Run with the library's Python (PIL): $LIB/.venv/Scripts/python.exe tools/prep.py"""
import os, glob
from PIL import Image, ImageOps, ImageFilter
Image.MAX_IMAGE_PIXELS = None
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); A = os.path.join(D, 'assets'); os.makedirs(A, exist_ok=True)
CAP = {'carl_ed1940': 3600, 'hb1921': 3400, 'c19': 3000, 'mh19': 3000, 'rfd_1914': 3400}
SKIP = ('c1897_n1',)
for f in sorted(glob.glob(os.path.join(D, 'raw', '*'))):
    name, ext = os.path.splitext(os.path.basename(f))
    if ext.lower() not in ('.jpg', '.jpeg', '.png', '.tif', '.tiff') or name in SKIP: continue
    out = os.path.join(A, name + '.jpg')
    if os.path.exists(out) and os.path.getmtime(out) > os.path.getmtime(f): continue
    im = Image.open(f).convert('RGB')
    if name.startswith('c1897_n'): im = im.crop((0, 0, im.width, int(im.height * .965)))   # drop the scanner's watermark line
    cap = next((v for k, v in CAP.items() if name.startswith(k)), 2600)
    if max(im.size) > cap: im.thumbnail((cap, cap), Image.LANCZOS)
    im.save(out, quality=90); print(name, im.size)
# name: (source in raw/, (x0, y0, x1, y1) as fractions of the page, mode)
CROPS = {
    'carlin_elev': ('mh1918_n52', (.056, .059, .925, .419), 'rect'),
    'carlin_plan1': ('mh1918_n52', (.078, .488, .365, .705), 'ink'),
    'carlin_plan2': ('mh1918_n52', (.628, .488, .915, .705), 'ink'),
    'carlin_title': ('mh1918_n52', (.175, .428, .80, .475), 'ink'),
    'carl1921_birdseye': ('hb1921_sell', (.07, .045, .995, .215), 'rect'),
    'carl1921_street1': ('hb1921_quantity', (.315, .385, .94, .53), 'rect'),
    'carl1921_street2': ('hb1921_quantity', (.315, .555, .935, .73), 'rect'),
    'carl1921_street3': ('hb1921_sell', (.08, .345, .67, .485), 'rect'),
    'woodriver1921': ('hb1921_sell', (.07, .755, .995, .94), 'rect'),
    'schopper1921': ('hb1921_quantity', (.02, .765, .945, .945), 'rect'),
    'sell_head': ('hb1921_sell', (.40, .02, .99, .05), 'ink'),
    'q192': ('hb1921_quantity', (.02, .225, .27, .262), 'ink'),
    'p1906_general_v': ('p1906_general', (.03, 0.035, .497, 0.47), 'rect'),
    'p1906_merch_v': ('p1906_merch', (.03, 0.035, .497, 0.47), 'rect'),
    'p1906_trainshed_v': ('p1906_trainshed', (.03, 0.035, .497, 0.47), 'rect'),
    'p1906_noon_v': ('p1906_noon', (.03, 0.035, .497, 0.47), 'rect'),
    'p1906_yards_v': ('p1906_yards', (.03, 0.04, .497, 0.47), 'rect'),
    'p1906_desk_v': ('p1906_desk', (.03, 0.085, .497, 0.475), 'rect'),
    'cut_watch_a': ('c1897_n372', (.06, .24, .30, .448), 'ink'),
    'cut_watch_b': ('c1897_n372', (.35, .226, .57, .432), 'ink'),
    'cut_watch_c': ('c1897_n372', (.785, .595, .99, .80), 'ink'),
    'cut_watch_d': ('c1897_n372', (.578, .595, .775, .80), 'ink'),
    'cut_watches_head': ('c1897_n372', (.16, .043, .84, .074), 'ink'),
    'cut_mast1897': ('c1897_n2', (.03, .025, .99, .285), 'ink'),
    'letters1897': ('c1897_n29', (.662, .648, 1.0, .952), 'rect'),
    'cut_dare1897': ('c1897_n29', (.0, .952, 1.0, .976), 'ink'),
}
def ink(im):
    g = ImageOps.grayscale(im); g = ImageOps.autocontrast(g, cutoff=(2, 2))
    a = g.point(lambda v: max(0, min(255, int((215 - v) * 255 / 150)))).filter(ImageFilter.GaussianBlur(.6))
    o = Image.new('RGBA', im.size, (42, 32, 24, 255)); o.putalpha(a); return o
for name, (src, (x0, y0, x1, y1), mode) in CROPS.items():
    s = os.path.join(D, 'raw', src + '.jpg'); ext = '.png' if mode == 'ink' else '.jpg'; out = os.path.join(A, name + ext)
    if os.path.exists(out) and os.path.getmtime(out) > max(os.path.getmtime(s), os.path.getmtime(__file__)): continue
    im = Image.open(s).convert('RGB'); W, H = im.size; c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
    (ink(c) if mode == 'ink' else c).save(out, **({} if mode == 'ink' else {'quality': 92})); print('crop', name, c.size)
