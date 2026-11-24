#!/usr/bin/env python3
"""lines.json + cleaned narration durations + the shot list below → film.json (scenes, voice starts, subtitles) and audio/cues.json.
Each chapter opens on an order blank (BLANK s, page curl in). A 'spread' is a laid-out page with items and its own moving camera:
items appear at `at` (seconds after the line starts, or a negative fraction of the line). Every scene lasts until the next starts."""
import json, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L = json.load(open(os.path.join(D, 'audio/lines.json'), encoding='utf-8'))
DUR = json.load(open(os.environ.get('DURFILE') or os.path.join(D, 'audio/vo/dur.json')))
SZ = json.load(open(os.path.join(D, 'assets/sizes.json')))
GAP, BLANK, LEAD, END, TITLE = 0.65, 5.4, 0.6, 18.0, 5.6
COLOUR = ('closed_', 'closing_', 'craftsman_', 'kenmore', 'tower_river', 'tower1974', 'carl_station', 'carl_courthouse', 'lumber_stamp')
def gr(img): return 'colour' if img.startswith(COLOUR) else 'paper' if img.startswith(('c18', 'c19', 'mh19', 'hb19', 'letters', 'carl_ed', 'ad1888', 'carl_1873')) else 'sepia'
def asp(img): w, h = SZ[img]; return w / h

# ── chapter cards (order blanks): no, article, year, price-stamp, side picture, sub line, darkness ──
CH = {'open': None,
      'c1': dict(no='No. 1', art='Gold Watch', year='1886', price='$14.00', side='sears_portrait', sub='a station agent, a refused shipment, and fourteen-dollar watches', of='1 OF 7'),
      'c2': dict(no='No. 104', art='Consumers Guide', year='1897', price='15¢', side='c1897_n0', sideGrade='paper', sub='the book that brought the city store to every farm', of='2 OF 7'),
      'c3': dict(no='No. 3031', art='The Carlin', year='1918', price='$1,172', side='carlin_elev', sub='a house, by mail, by rail, in pieces', of='3 OF 7'),
      'c4': dict(no='—', art='Sears Store', year='1925', price='2 FEB', side='store1929_allentown', sub='a store at the end of the road', of='4 OF 7'),
      'c5': dict(no='—', art='Sears Tower', year='1973', price='1,451 FT', side='tower1974', sideGrade='colour', sub='the tallest building in the world', of='5 OF 7', dk=.35),
      'c6': dict(no='—', art='The Big Book', year='1993', price='25 JAN', side='c1902_n0', sideGrade='paper', sub='the last catalog', of='6 OF 7', dk=.7),
      'c7': dict(no='—', art='Closing Sale', year='2018', price='15 OCT', side='closing_hialeah', sideGrade='colour', sub='what happened to Sears', of='7 OF 7', dk=1),
      'end': dict(no='—', art='Your House', year='Today', price='STILL HERE', side='carl_station', sideGrade='colour', sub='what of Sears is still around you', of='', dk=.1)}
DK = {'open': 0, 'c1': 0, 'c2': 0, 'c3': 0, 'c4': 0, 'c5': .35, 'c6': .7, 'c7': 1, 'end': .1}

# ── helpers ──
def ph(img, x, y, w=None, h=None, **k):
    if h is None: h = round(w / asp(img))
    if w is None: w = round(h * asp(img))
    return dict(k='ph', img=img, x=x, y=y, w=w, h=h, grade=k.pop('grade', gr(img)), **k)
def cut(img, x, y, w, **k): return dict(k='cut', img=img, x=x, y=y, w=w, **k)
def T(kind, **k): return dict(k=kind, **k)
def tag(text, x, y, at=0, **k): return dict(k='tag', text=text, x=x, y=y, at=at, **k)
def cam(*keys): return [list(k) for k in keys]
PUSH = cam((0, 960, 540, 1.0, 0), (-1.1, 980, 530, 1.07, .4))
PULL = cam((0, 960, 530, 1.1, -.3), (-1.1, 960, 540, 1.0, 0))
def hero(img, tagtext, cap=None, cam_=None, fy=.5, fx=.5, z=(1.0, 1.04), extra=(), w=None, y=None, cart=0, rot=0, **k):
    a = asp(img); W_ = w or (1560 if a >= 1.5 else 1400 if a >= 1.2 else 1150 if a >= .9 else 640); H_ = round(W_ / a)
    if H_ > 820: H_ = 820; W_ = round(H_ * a)
    X = (1920 - W_) // 2; Y = y if y is not None else max(70, (930 - H_) // 2 + 10)
    items = [ph(img, X, Y, W_, H_, cap=cap, fy=fy, fx=fx, z=list(z), cart=cart, rot=rot, at=0, **{'in': 'none'}), tag(tagtext, X - 14, Y - 28)] + list(extra)
    return dict(type='spread', items=items, cam=cam_ or PUSH, **k)
def portrait(img, name, sub, tagtext, extra=(), side='l', **k):
    a = asp(img); H_ = 780; W_ = round(H_ * a); X = 170 if side == 'l' else 1750 - W_
    nx = X + W_ + 110 if side == 'l' else X - 110
    items = [ph(img, X, 110, W_, H_, cart=1, rot=-1.5 if side == 'l' else 1.5, at=0, **{'in': 'none'}), tag(tagtext, X - 10, 84),
             T('name', name=name, sub=sub, x=nx, y=470, al='l' if side == 'l' else 'r', at=.5)] + list(extra)
    return dict(type='spread', items=items, cam=k.pop('cam', cam((0, 960, 540, 1.04, 0), (-1.1, 940, 530, 1.0, -.3))), **k)

S = {
 # ── cold open: your house ──
 'n01': dict(type='spread', cam=cam((0, 960, 540, 1.25, 0), (-1.1, 960, 540, 1.0, 0)), items=[
     cut('cut_watch_a', 760, 470, 360, rot=-8, at=.0), cut('cut_watch_b', 1180, 520, 330, rot=6, at=.35),
     T('drop', text='Take a look around your house.', x=960, y=860, s=64, al='center', at=.6)]),
 'n02': dict(type='spread', cam=cam((0, 760, 540, 1.0, 0), (-1.1, 1160, 540, 1.0, 0)), items=[
     ph('craftsman_westland', 120, 130, 900, at=0, rot=-2, cap='Craftsman · 2019'), tag('PHOTO · PHILLIP PESSAR · WESTLAND MALL, HIALEAH · 2019 (CC BY 2.0)', 110, 100),
     ph('kenmore', 1200, 120, 560, at=-.55, rot=2.5, cap='Kenmore'), tag('PHOTO · STILFEHLER · 2007 (PUBLIC DOMAIN)', 1190, 92, at=-.55)]),
 'n03': dict(type='spread', cam=cam((0, 980, 520, 1.12, 0), (-1.1, 960, 540, 1.0, 0)), items=[
     ph('lumber_stamp', 250, 120, 820, at=0, rot=-1.5, cap='Stamped lumber in a Sears house'), tag('PHOTO · ROSEMARY THORNTON · 2013 (PUBLIC DOMAIN)', 240, 92),
     ph('carlin_elev', 1000, 470, 760, at=-.4, rot=2, cap='The Carlin · 1918'), T('drop', text='by train, in pieces', x=1380, y=410, s=52, al='center', at=-.6)]),
 'n04': dict(type='spread', cam=cam((0, 960, 470, 1.0, 0), (-1.1, 960, 520, 1.06, 0)), items=[
     cut('cut_mast1897', 960, 360, 1500, at=0, grade='paper'), T('stamp', text='CHICAGO', x=1500, y=690, s=70, rot=-7, at=-.5)]),
 'n05': dict(type='spread', cam=cam((0, 900, 540, 1.0, 0), (-1.1, 1000, 520, 1.08, .5)), items=[
     ph('ad1888', 260, 160, 760, at=0, rot=-2), tag('ADVERTISEMENT · WINCHESTER (IND.) JOURNAL · 5 JAN 1888', 250, 132),
     cut('cut_watch_a', 1400, 470, 420, rot=8, at=-.3), T('stamp', text='$14', x=1450, y=800, s=110, rot=-6, at=-.65)]),
 'n06': dict(type='spread', cam=cam((0, 700, 540, 1.0, 0), (-1.1, 1250, 540, 1.0, 0)), items=[
     ph('c1897_n0', 140, 110, None, 800, at=0, rot=-2), ph('c1928_n460', 760, 130, None, 780, at=-.3, rot=1.5), ph('mh1918_n52', 1330, 110, None, 800, at=-.65, rot=-1),
     tag('SEARS CATALOGS · 1897 · 1928 · 1918 (INTERNET ARCHIVE)', 140, 84)]),
 'n07': hero('rfd_1914a', 'PHOTO · HARRIS & EWING · RURAL FREE DELIVERY · 1914 (LIBRARY OF CONGRESS)', z=(1.0, 1.06)),
 'n08': dict(type='spread', cam=PUSH, items=[ph('p1906_general_v', 517, 90, None, 820, at=0, rot=-1, cap='Sears, Roebuck & Co., Chicago · 1906'),
     tag('STEREOGRAPH · SEARS, ROEBUCK & CO. · 1906 (SCAN: RICHARD, CC BY 2.0)', 507, 64)]),
 'n09': dict(type='calendar', a=['1993', 'the Big Book ends'], b=['1994', 'Amazon is founded'], flip=-.55),
 'n10': dict(type='title'),
 'n11': dict(type='seven', at=[-.1, -.2, -.3, -.4, -.5, -.62, -.78]),
 'n12': hero('c1928_n460', 'SEARS CATALOG · CHRISTMAS STOCKINGS · FALL 1928 (INTERNET ARCHIVE)', cam_=cam((0, 960, 300, 1.5, 0), (-1.1, 960, 520, 1.0, 0)),
             extra=[T('ring', x=1040, y=300, r=110, at=-.55)]),
 # ── 1. a gold watch ──
 'n13': dict(type='map', focus='North Redwood', zoom=(1.0, 3.2), towns=[['North Redwood', .3], ['Minneapolis', .9]], routes=[],
             note=['NORTH REDWOOD, MINN.', 'a railroad station · 1886']),
 'n14': dict(type='spread', cam=PUSH, items=[cut('cut_watch_a', 700, 500, 520, rot=-10, at=0), cut('cut_watch_b', 1150, 470, 470, rot=7, at=.3),
     T('stamp', text='REFUSED', x=960, y=520, s=120, rot=-12, at=-.7)]),
 'n15': dict(type='map', focus='North Redwood', zoom=(3.0, 2.0), towns=[['North Redwood', 0]], swarm=dict(src='North Redwood', n=14, at=.15, dur=-.8, r=220),
             note=['$14 EACH', 'to station agents up and down the line']),
 'n16': dict(type='spread', cam=PUSH, items=[T('count', x=960, y=560, s=200, pre='$', to=5000, at=.2, dur=-.5, al='center'),
     T('txt', text='in six months', x=960, y=650, s=46, f='Fell', it=1, al='center', at=-.35), cut('cut_watch_b', 1600, 360, 300, rot=12, at=0), cut('cut_watch_a', 330, 700, 300, rot=-9, at=0)]),
 'n17': portrait('roebuck', 'Alvah Curtis Roebuck', '1864–1948 · WATCH REPAIRMAN FROM INDIANA', 'A. C. ROEBUCK · c. 1890–1910', at=0,
             extra=[T('map', x=1180, y=660, w=600, towns=[['Chicago', -.15], ['Minneapolis', 0]], routes=[['Minneapolis', 'Chicago', 0, -.3, .2]])]),
 'n18': dict(type='spread', cam=cam((0, 960, 520, 1.0, 0), (-.55, 960, 760, 1.7, 0), (-1.1, 960, 800, 1.7, 0)), items=[
     ph('ad1888', 410, 90, 1100, at=0, **{'in': 'none'}), tag('ADVERTISEMENT · WINCHESTER (IND.) JOURNAL · 5 JAN 1888', 400, 64),
     T('hl', x=440, y=890, w=1040, h=60, at=-.45)]),
 'n19': dict(type='spread', cam=PUSH, items=[T('drop', text='SEARS, ROEBUCK & CO.', x=960, y=470, s=120, f='FellSC', al='center', at=.2, ls=4),
     T('stamp', text='1893', x=960, y=640, s=96, rot=-4, at=-.5)]),
 'n20': portrait('sears_portrait', 'Richard Warren Sears', '1863–1914 · FOUNDER', 'R. W. SEARS · c. 1890–1910', at=0,
             extra=[cut('cut_watches_head', 1350, 760, 760, at=-.5, grade='paper')]),
 'n21': portrait('rosenwald1919', 'Julius Rosenwald', '1862–1932 · PARTNER FROM 1895 · PRESIDENT 1908–1924', 'J. ROSENWALD · NATIONAL PHOTO CO. · 1919 (LIBRARY OF CONGRESS)', at=0),
 'n22': hero('trio1895', 'SEARS · NUSBAUM · ROSENWALD · 1895 (LIBRARY OF CONGRESS)', cam_=cam((0, 960, 520, 1.0, 0), (-1.1, 960, 470, 1.15, 0))),
 'n23': dict(type='bars', title='SEARS, ROEBUCK & CO. · ANNUAL SALES', data=[['1895', .75, '$750,000'], ['1907', 50, '$50 million +']], max=55, at=[-.15, -.55],
             img='p1906_merch'),
 'n24': dict(type='map', focus='Chicago', zoom=(1.0, 1.0), towns=[['Chicago', 0]], swarm=dict(src='Chicago', n=60, at=.1, dur=-.9, r=900), note=['WHAT ELSE?', '']),
 # ── 2. the catalog ──
 'n25': hero('c1897_n0', 'CONSUMERS GUIDE · CATALOGUE NO. 104 · SPRING 1897 (INTERNET ARCHIVE)', cam_=cam((0, 960, 300, 1.35, 0), (-1.1, 960, 520, 1.0, 0)), w=640),
 'n26': dict(type='stack', img='c1897_n2', keys=[[.1, 32, '1888'], [-.45, 322, '1894'], [-.8, 532, '1895']]),
 'n27': dict(type='flip', pages=['c1897_n171', 'c1897_n372', 'c1897_n29', 'c1928_n993', 'c1897_n55', 'c1928_n460'], words=['Groceries.', 'Stoves.', 'Dolls.', 'Medicines.', 'Bicycles.', 'Clothing.', 'Plows.']),
 'n28': hero('rfd_wagon', 'PHOTO · RURAL FREE DELIVERY CARRIER (SMITHSONIAN NATIONAL POSTAL MUSEUM)', extra=[T('stamp', text='R.F.D. 1896', x=1580, y=200, s=64, rot=-8, at=-.4)]),
 'n29': dict(type='spread', cam=cam((0, 760, 540, 1.0, 0), (-1.1, 1180, 540, 1.0, 0)), items=[
     ph('parcel1913', 130, 110, None, 800, at=0, rot=-1.5, cap='Opening up Parcel Post · 1913'), tag('PHOTO · NATIONAL PHOTO CO. · 1913 (LIBRARY OF CONGRESS)', 120, 84),
     ph('rfd_auto', 860, 300, 960, at=-.45, rot=2, cap='A rural carrier · c. 1910'), tag('SMITHSONIAN NATIONAL POSTAL MUSEUM', 850, 272, at=-.45)]),
 'n30': dict(type='map', focus='Chicago', zoom=(1.0, 1.0), towns=[['Chicago', 0]], swarm=dict(src='Chicago', n=160, at=.1, dur=-.85, r=1400),
             count=dict(text='1 in 5', label='Americans got the catalog by 1908', at=.4), count2=dict(text='100,000 items · 1,400 pages', at=-.6)),
 'n31': dict(type='spread', cam=cam((0, 900, 560, 1.12, 0), (-1.1, 960, 520, 1.0, 0)), items=[
     ph('p1906_merch_v', 520, 80, None, 820, at=0, **{'in': 'none'}), tag('STEREOGRAPH · MERCHANDISE BUILDING · 1906 (CC BY 2.0)', 510, 54),
     T('note', text='world’s largest', x=1480, y=480, s=44, at=-.6), T('txt', text='commercial building', x=1480, y=540, s=44, f='Fell', it=1, at=-.6)]),
 'n32': dict(type='conveyor', img='habs_conveyors', img2='p1906_trainshed_v', tag='HABS · SHIPPING COURT CONVEYORS (LIBRARY OF CONGRESS)', tag2='STEREOGRAPH · TRAIN SHED · 1906 (CC BY 2.0)'),
 'n33': dict(type='spread', cam=cam((0, 960, 540, 1.0, 0), (-.7, 1040, 700, 1.55, 0), (-1.1, 1040, 700, 1.55, 0)), items=[
     ph('c1897_n29', 520, 70, None, 840, at=0, **{'in': 'none'}), tag('SEARS CATALOGUE · SPRING 1897 · p. 28', 510, 44),
     T('ring', x=1047, y=742, r=125, at=-.5)]),
 'q01': dict(type='letter', img='letters1897', who='A. J. Barwick', place='Chapel Hill, N.C.', date='Jan. 13, 1897', head='Much Pleased with Watch.',
             q=['I am much pleased. So far', 'it is all you claim for it.', 'It keeps splendid time.'], hl=[.08, .16, .5]),
 'n34': dict(type='spread', cam=cam((0, 960, 540, 1.0, 0), (-1.1, 960, 520, 1.04, 0)), items=[
     cut('cut_dare1897', 960, 360, 1760, at=0, grade='paper'), T('hl', x=80, y=330, w=1760, h=60, at=.3, dur=-.6),
     T('drop', text='“Give us one trial.”', x=960, y=640, s=96, al='center', at=-.6)]),
 'n35': hero('c1928_n460', 'SEARS CATALOG · FALL 1928 · p. 459 (INTERNET ARCHIVE)', cam_=cam((0, 960, 640, 1.6, 0), (-1.1, 960, 470, 1.25, 0)), w=600,
             extra=[ph('c1912_n0', 1380, 140, None, 700, at=-.4, rot=4), ph('c1928_n0', 150, 160, None, 680, at=-.2, rot=-4)]),
 'n36': dict(type='spread', cam=PUSH, items=[ph('c1928_n0', 210, 110, None, 790, at=0, rot=-2, cap='Fall & Winter 1928–29'), tag('SEARS CATALOG COVER · 1928 (INTERNET ARCHIVE)', 200, 84),
     T('drop', text='1933', x=1350, y=380, s=150, f='OST', w=700, c='red', al='center', at=.4), T('txt', text='the Christmas Book', x=1350, y=450, s=44, f='Fell', it=1, al='center', at=-.25),
     T('drop', text='The Wish Book', x=1350, y=640, s=96, al='center', at=-.75), T('stamp', text='1968', x=1350, y=760, s=72, rot=-6, at=-.85)]),
 'n37': hero('c1928_n460', 'SEARS CATALOG · CHRISTMAS · FALL 1928 (INTERNET ARCHIVE)', cam_=cam((0, 960, 340, 1.45, 0), (-1.1, 960, 560, 1.3, 0)), w=600,
             extra=[T('ring', x=790, y=420, r=90, at=-.55, pen=1), T('ring', x=1150, y=330, r=80, at=-.8, pen=1)]),
 'n38': dict(type='spread', cam=PULL, items=[ph('mh1918_n0', 650, 90, None, 820, at=0, rot=-1.5), tag('HONOR BILT MODERN HOMES · 1918 (INTERNET ARCHIVE)', 640, 64)]),
 # ── 3. a house in a box ──
 'n39': hero('mh1911_n0', 'MODERN HOMES · SEARS, ROEBUCK & CO. · 1911 (INTERNET ARCHIVE)', z=(1.0, 1.08)),
 'n40': dict(type='house', phase='parts'),
 'n41': dict(type='spread', cam=PUSH, items=[T('cal90', x=960, y=480, at=.1, dur=-.8), T('txt', text='“a man of average abilities”', x=960, y=860, s=44, f='Fell', it=1, al='center', at=.4)]),
 'n42': dict(type='dots', light=1, from_=75000, per=50, img='mh1918_n12', label='Sears houses, 1908–1940', keys=[[0, 0], [-.6, 75000]], note='≈ 70,000–75,000'),
 'n43': dict(type='map', focus='Carlinville', zoom=(1.0, 2.6), towns=[['Chicago', 0], ['Carlinville', .4]], routes=[['Chicago', 'Carlinville', .2, -.8, -.25]]),
 'n44': dict(type='spread', cam=cam((0, 960, 540, 1.0, 0), (-1.1, 1100, 520, 1.12, 0)), items=[
     ph('carl_ed1940', 140, 80, None, 840, at=0, rot=-1.5, cap='Carlinville · 1940'), tag('1940 CENSUS DISTRICT MAP (NATIONAL ARCHIVES)', 130, 54),
     ph('carl_courthouse', 1130, 140, None, 740, at=-.35, rot=2, cap='Macoupin County Courthouse'), tag('PHOTO · JOHN MARGOLIES · 1991 (LIBRARY OF CONGRESS)', 1120, 112, at=-.35)]),
 'n45': hero('carl1921_street3', 'HONOR BILT MODERN HOMES · 1921 · p. 4 (INTERNET ARCHIVE)', extra=[T('stamp', text='STANDARD OIL · 1918', x=1460, y=180, s=58, rot=-6, at=-.55)]),
 'n46': dict(type='spread', cam=PUSH, items=[ph('hb1921_quantity', 160, 70, None, 850, at=0, rot=-1), tag('HONOR BILT MODERN HOMES · 1921 · p. 5', 150, 44),
     T('hl', x=176, y=262, w=470, h=50, at=.3), T('count', x=1350, y=520, s=220, to=192, at=.2, dur=-.4, al='center'),
     T('txt', text='houses · about $1,000,000', x=1350, y=610, s=46, f='Fell', it=1, al='center', at=-.45)]),
 'n47': dict(type='spread', cam=cam((0, 960, 540, 1.25, 0), (-1.1, 960, 520, 1.0, 0)), items=[
     ph('carl1921_birdseye', 90, 200, 1740, at=0, **{'in': 'none'}, cap='Birdseye view of Sears houses at Carlinville, Ill.'), tag('HONOR BILT MODERN HOMES · 1921 · p. 4', 80, 172),
     T('drop', text='The Standard Addition', x=960, y=860, s=72, al='center', at=-.55)]),
 'n48': dict(type='house', phase='carlin'),
 'n49': dict(type='spread', cam=cam((0, 960, 300, 1.55, 0), (-1.1, 960, 520, 1.0, 0)), items=[
     ph('hb1921_sell', 330, 60, None, 860, at=0, **{'in': 'none'}), ph('hb1921_quantity', 970, 60, None, 860, at=0, **{'in': 'none'}),
     tag('HONOR BILT MODERN HOMES · 1921 · pp. 4–5 (INTERNET ARCHIVE)', 320, 36)]),
 'n50': dict(type='house', phase='wipe'),
 'n51': hero('schopper1921', 'HONOR BILT MODERN HOMES · 1921 · p. 5', cap='Schopper, Ill. · sold to the Standard Oil Company',
             extra=[T('stamp', text='CLOSED · 1925', x=1420, y=210, s=70, rot=-7, at=-.5)]),
 'n52': dict(type='schoper'),
 'n53': dict(type='spread', cam=cam((0, 1100, 520, 1.1, 0), (-1.1, 900, 540, 1.0, 0)), items=[
     ph('carl1921_street1', 120, 150, 1680, at=0, **{'in': 'none'}), tag('HONOR BILT MODERN HOMES · 1921 · p. 5', 110, 122),
     T('count', x=960, y=860, s=130, pre='≈ ', to=150, at=.3, dur=-.4, al='center', note='still standing')]),
 'n54': hero('lumber_stamp', 'PHOTO · ROSEMARY THORNTON · STAMPED LUMBER IN A SEARS HOUSE · 2013 (PUBLIC DOMAIN)', cam_=cam((0, 960, 540, 1.0, 0), (-1.1, 1020, 470, 1.25, 0)),
             extra=[T('ring', x=700, y=360, r=120, at=-.75)]),
 'n55': dict(type='ledger', rows=[['c.1912', 'Sears lends buyers the money', ''], ['1929–33', 'the Depression: loans go bad', '$11,000,000'], ['1933', 'Sears stops lending', '']]),
 'n56': hero('mh1918_cover', 'HONOR BILT MODERN HOMES · 1918', w=560, cam_=PULL, extra=[T('stamp', text='1908–1940', x=1450, y=520, s=80, rot=-5, at=.5)]),
 # ── 4. a store ──
 'n57': hero('truck1909', 'SEARS, ROEBUCK ELECTRIC TRUCK · c. 1908 (PUBLIC DOMAIN)', w=900),
 'n58': dict(type='spread', cam=PUSH, items=[T('drop', text='“The future is stores.”', x=960, y=440, s=96, al='center', at=.4),
     T('txt', text='Robert E. Wood · joined Sears 1924', x=960, y=540, s=38, f='Mono', al='center', at=-.4)]),
 'n59': dict(type='spread', cam=cam((0, 960, 540, 1.0, 0), (-1.1, 960, 520, 1.08, 0)), items=[
     ph('p1906_noon_v', 200, 110, None, 800, at=0, **{'in': 'none'}, cap='The West Side plant'), tag('STEREOGRAPH · ON THE STREET AT NOON · 1906 (CC BY 2.0)', 190, 84),
     T('stamp', text='2 FEB 1925', x=1580, y=420, s=66, rot=-6, at=-.4), T('txt', text='the first store', x=1580, y=510, s=40, f='Fell', it=1, al='center', at=-.5)]),
 'n60': dict(type='dots', light=1, from_=324, per=1, img='store1929_allentown', label='Sears stores', keys=[[0, 1], [-.4, 27], [-.85, 324]], years=[[0, '1925'], [-.4, '1927'], [-.85, '1932']]),
 'n61': dict(type='bars', title='SEARS SALES · 1931', data=[['Stores', 53.4, '53%'], ['Catalog', 46.6, '47%']], max=60, at=[-.25, -.45], img='store1926_seattle'),
 'n62': hero('store1929_allentown', 'SEARS, ROEBUCK BUILDING · ALLENTOWN, PA. · 1929 (PUBLIC DOMAIN)', cap='Allentown, Pa. · 1929', z=(1.0, 1.08)),
 'n63': hero('store1926_seattle', 'SEARS, ROEBUCK WESTERN BRANCH · SEATTLE · c. 1926 (MOHAI)', w=1150, cap='Seattle · c. 1926'),
 'n64': dict(type='spread', cam=cam((0, 760, 540, 1.0, 0), (-1.1, 1200, 520, 1.0, 0)), items=[
     ph('c1928_n995', 160, 90, None, 820, at=0, rot=-1.5, cap='Craftsman · 1928'), tag('SEARS CATALOG · FALL 1928 · p. 994', 150, 64),
     ph('kenmore', 1260, 140, None, 720, at=-.35, rot=2, cap='Kenmore'), tag('PHOTO · STILFEHLER · 2007 (PUBLIC DOMAIN)', 1250, 112, at=-.35),
     T('stamp', text='1927', x=960, y=480, s=96, rot=-5, at=-.55)]),
 'n65': hero('craftsman_westland', 'PHOTO · PHILLIP PESSAR · 2019 (CC BY 2.0)', z=(1.0, 1.1)),
 'n66': dict(type='spread', cam=PULL, items=[ph('p1906_yards_v', 517, 100, None, 800, at=0, **{'in': 'none'}, cap='Railroad yards · 1906'), tag('STEREOGRAPH · SEARS, ROEBUCK & CO. · 1906 (CC BY 2.0)', 507, 74)]),
 # ── 5. the tower ──
 'n67': hero('tower_river', 'PHOTO · W. LEMAY · SEARS TOWER FROM THE CHICAGO RIVER · 2015 (CC0)', w=720, cam_=cam((0, 960, 760, 1.3, 0), (-1.1, 960, 380, 1.3, 0))),
 'n68': dict(type='tower'),
 'n69': dict(type='spread', cam=cam((0, 760, 540, 1.0, 0), (-1.1, 1180, 540, 1.0, 0)), items=[
     ph('habs_tower', 170, 90, None, 820, at=0, rot=-1.5, cap='The West Side plant tower'), tag('HABS · MERCHANDISE BUILDING TOWER (LIBRARY OF CONGRESS)', 160, 64),
     ph('tower1974', 1170, 90, None, 820, at=-.4, rot=2, cap='Sears Tower · 1974'), tag('DOCUMERICA · U.S. EPA · 1974 (NATIONAL ARCHIVES)', 1160, 64, at=-.4)]),
 'n70': hero('tower1974', 'DOCUMERICA · U.S. EPA · CHICAGO · 1974 (NATIONAL ARCHIVES)', cam_=cam((0, 960, 300, 1.25, 0), (-1.1, 960, 760, 1.25, 0)), w=560),
 'n71': dict(type='rivals'),
 'n72': dict(type='spread', cam=PUSH, items=[T('drop', text='Allstate', x=520, y=420, s=90, al='center', at=.2), T('drop', text='Dean Witter', x=960, y=560, s=90, al='center', at=-.3),
     T('drop', text='Discover', x=1400, y=420, s=90, al='center', at=-.55), T('stamp', text='SOCKS & STOCKS', x=960, y=760, s=60, rot=-4, at=-.85)]),
 'n73': dict(type='bars', title='THE BIGGEST RETAILER IN AMERICA', data=[['Sears', 50, 'until c. 1990'], ['Walmart', 58, 'from c. 1990']], max=60, at=[-.15, -.5], img='tower_river', dk=1),
 'n74': hero('tower1974', 'DOCUMERICA · U.S. EPA · 1974 (NATIONAL ARCHIVES)', w=520, cam_=PULL),
 # ── 6. the last catalog ──
 'n75': dict(type='ledger', dark=1, big='−$3,900,000,000', rows=[['1992', 'net loss', '−$3.9 billion']], note='the biggest loss a North American retailer had ever reported'),
 'n76': dict(type='fan', pages=['c1897_n0', 'c1902_n0', 'c1912_n0', 'c1918_n0', 'c1928_n0'], count=dict(pre='−$', per_day=1000000, label='a day, by one account')),
 'n77': dict(type='spread', cam=PUSH, items=[T('stamp', text='25 JAN 1993', x=960, y=300, s=90, rot=-4, at=.1), T('drop', text='No more Big Book.', x=960, y=480, s=92, al='center', at=-.25),
     T('count', x=640, y=720, s=110, to=113, at=-.55, dur=1.0, al='center', note='stores close'), T('count', x=1280, y=720, s=110, to=50000, at=-.7, dur=1.2, al='center', note='jobs')]),
 'n78': hero('tower_river', 'PHOTO · W. LEMAY · 2015 (CC0)', w=700, cam_=PULL),
 'n79': dict(type='calendar', a=['25 JAN 1993', 'the Big Book ends'], b=['5 JUL 1994', 'a company that will become Amazon'], flip=-.2, dark=1),
 'n80': dict(type='spread', cam=PUSH, items=[T('txt', text='1993', x=960, y=260, s=110, f='OST', w=700, c='red', al='center', at=.1),
     T('drop', text='Walmart · Home Depot', x=960, y=520, s=92, al='center', at=-.45), T('txt', text='not the internet', x=960, y=640, s=56, f='Fell', it=1, al='center', at=-.62)]),
 'n81': hero('closed_brooklyn', 'PHOTO · TONY WEBSTER · BROOKLYN CENTER, MINN. · 2019 (CC BY 2.0)', cam_=PULL),
 # ── 7. the closing-sale sign ──
 'n82': dict(type='dots', from_=3500, per=1, img='closed_vero', tag='PHOTO · POKEMONPRIME · VERO BEACH, FLA. · 2024 (CC BY 4.0)', label='Sears and Kmart stores', keys=[[0, 0], [-.85, 3500]], years=[[0, '2005']]),
 'n83': hero('closed_vero', 'PHOTO · POKEMONPRIME · VERO BEACH, FLA. · 2024 (CC BY 4.0)', z=(1.0, 1.08)),
 'n84': dict(type='spread', cam=PUSH, items=[ph('craftsman_westland', 200, 140, 900, at=0, rot=-2, cap='Craftsman → Stanley Black & Decker'),
     T('stamp', text='SOLD · 2017', x=1450, y=360, s=76, rot=-6, at=-.4), T('stamp', text='DIEHARD · 2019', x=1450, y=600, s=66, rot=-3, at=-.75)]),
 'n85': dict(type='dots', from_=3500, per=1, img='closing_hialeah', tag='PHOTO · PHILLIP PESSAR · HIALEAH, FLA. · 2020 (CC BY 2.0)', label='Sears and Kmart stores', keys=[[0, 3500], [-.7, 687]], years=[[0, '2005'], [-.6, '2018']]),
 'n86': hero('closing_hialeah', 'PHOTO · PHILLIP PESSAR · HIALEAH, FLA. · 12 FEB 2020 (CC BY 2.0)', cam_=cam((0, 960, 540, 1.0, 0), (-1.1, 940, 600, 1.25, 0))),
 'n87': hero('closing_hialeah', 'PHOTO · PHILLIP PESSAR · HIALEAH, FLA. · 12 FEB 2020 (CC BY 2.0)', cam_=cam((0, 940, 600, 1.25, 0), (-1.1, 900, 640, 1.9, 0))),
 'n88': dict(type='dots', from_=3500, per=1, img='closing_hialeah', tag='PHOTO · PHILLIP PESSAR · HIALEAH, FLA. · 2020 (CC BY 2.0)', label='Sears stores', keys=[[0, 687], [-.75, 5]], years=[[0, '2018'], [-.6, '2025']]),
 'n89': dict(type='spread', dk=1, cam=PULL, items=[T('drop', text='So what’s left?', x=960, y=520, s=110, al='center', at=.2, c='cream')]),
 # ── epilogue ──
 'n90': dict(type='map', focus='Carlinville', zoom=(1.0, 3.0), towns=[['Carlinville', .2]], routes=[]),
 'n91': dict(type='spread', cam=cam((0, 760, 540, 1.0, 0), (-1.1, 1180, 540, 1.0, 0)), items=[
     ph('carl_station', 120, 170, 960, at=0, rot=-1.5, cap='Carlinville station · 2020'), tag('PHOTO · THECATALYST31 · 2020 (CC0)', 110, 142),
     ph('carl_courthouse', 1250, 110, None, 780, at=-.5, rot=2), tag('PHOTO · JOHN MARGOLIES · 1991 (LIBRARY OF CONGRESS)', 1240, 82, at=-.5)]),
 'n92': dict(type='house', phase='today'),
 'n93': dict(type='spread', cam=cam((0, 700, 540, 1.0, 0), (-1.1, 1250, 540, 1.0, 0)), items=[
     ph('craftsman_westland', 90, 160, 640, at=0, rot=-2, cap='Craftsman'), ph('kenmore', 800, 150, None, 640, at=-.25, rot=1.5, cap='Kenmore'),
     ph('tower_river', 1330, 110, None, 700, at=-.6, rot=-1, cap='Willis Tower · since 2009')]),
 'n94': dict(type='map', focus='Chicago', zoom=(1.0, 1.0), towns=[['Chicago', 0]], swarm=dict(src='Chicago', n=120, at=.1, dur=-.9, r=1400), warm=1),
 'n95': dict(type='spread', cam=PUSH, items=[cut('cut_watch_b', 960, 470, 520, rot=0, at=0, grade='paper'), T('drop', text='The third time, it let go.', x=960, y=880, s=70, al='center', at=.4)]),
 'n96': dict(type='spread', cam=PULL, items=[ph('carl1921_street2', 140, 140, 1640, at=0, **{'in': 'none'}, cap='Carlinville, Ill.'),
     cut('cut_mast1897', 960, 860, 900, at=-.6, grade='paper')]),
 'n97': dict(type='spread', cam=PUSH, items=[ph('hb1921_quantity', 190, 70, None, 850, at=0, rot=-1.5), ph('c1928_n460', 1130, 90, None, 830, at=.3, rot=2),
     T('hand', text='Did your family order from the catalog?', x=960, y=560, s=62, at=-.1, dur=2.2, al='center')]),
}
missing = [l['id'] for l in L if l['id'] not in S]
if missing: raise SystemExit('no shot for ' + ', '.join(missing))
scenes, vo, subs, t, prev = [], {}, [], LEAD, None
for l in L:
    ch = l['chapter']
    if ch != prev and CH.get(ch):
        b = dict(type='blank', t0=round(t, 2), curl=1, **CH[ch]); b['dk'] = CH[ch].get('dk', DK[ch])
        b['cam'] = [[0, 960, 540, 1.0, 0], [BLANK, 930, 530, 1.05, -.5]]; scenes.append(b); t += BLANK
    if ch != prev and ch == 'c1': pass
    prev = ch; d = DUR[l['id']]
    sh = json.loads(json.dumps(S[l['id']])); sh['t0'] = round(t, 2); sh['line'] = l['id']; sh['vd'] = round(d, 2); sh.setdefault('dk', DK[ch]); sh['ch'] = ch
    if 'from_' in sh: sh['from'] = sh.pop('from_')
    if sh['type'] == 'title': d = max(d, TITLE)
    if ch != prev and l is L[0]: pass
    scenes.append(sh); vo[l['id']] = round(t, 3)
    parts = l['subs']; n = sum(len(p) for p in parts); tt = t; dv = DUR[l['id']]
    for i, p in enumerate(parts):
        dd = dv * len(p) / n; subs.append([round(tt - .08, 2), round(tt + dd + (.3 if i == len(parts) - 1 else .02), 2), p]); tt += dd
    t += d + GAP
# the first scene after a blank, and the first of the film, curl in from the previous page
for i, s in enumerate(scenes):
    if i and scenes[i - 1]['type'] == 'blank': s['curl'] = 1
for i in range(len(subs) - 1): subs[i][1] = round(min(subs[i][1], subs[i + 1][0] - .02), 2)
scenes.append(dict(type='end', t0=round(t + .6, 2), curl=1, dk=.1))
dur = round(t + .6 + END, 1)
for i, s in enumerate(scenes): s['t1'] = scenes[i + 1]['t0'] if i + 1 < len(scenes) else dur
F = dict(dur=dur, scenes=scenes, vo=vo, subs=[{'t0': a, 't1': b, 'text': s} for a, b, s in subs])
json.dump(F, open(os.path.join(D, 'film.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
json.dump(F['subs'], open(os.path.join(D, 'audio/cues.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('scenes', len(scenes), 'subs', len(subs), 'duration', dur, 's =', round(dur / 60, 1), 'min')
