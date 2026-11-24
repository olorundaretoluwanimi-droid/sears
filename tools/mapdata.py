# Natural Earth (public domain) → assets/map.json: land, lakes and rail lines of the lower 48 window, Albers-projected and simplified,
# in a 0..1000 × 0..~620 space. No borders are drawn (DIRECTOR.md §13); rails are today's network, shown as a schematic.
import json, math, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); NE = os.path.join(D, 'research', 'ne')
P1, P2, L0, F0 = map(math.radians, (29.5, 45.5, -96, 37.5))
n = (math.sin(P1) + math.sin(P2)) / 2; Cc = math.cos(P1) ** 2 + 2 * n * math.sin(P1); r0 = math.sqrt(Cc - 2 * n * math.sin(F0)) / n
def alb(lon, lat):
    l, f = math.radians(lon), math.radians(lat); r = math.sqrt(Cc - 2 * n * math.sin(f)) / n; th = n * (l - L0)
    return r * math.sin(th), r0 - r * math.cos(th)
X0, Y0 = alb(-125, 49.5)[0], alb(-96, 50.5)[1]; X1 = alb(-66, 49.5)[0]; Y1 = alb(-98, 23.5)[1]
S = 1000 / (X1 - X0)
def pr(lon, lat): x, y = alb(lon, lat); return round((x - X0) * S, 1), round((Y0 - y) * S, 1)
H = round((Y0 - Y1) * S, 1)
def inwin(lon, lat): return -130 <= lon <= -60 and 20 <= lat <= 54
def simp(pts, tol):
    out = [pts[0]]
    for p in pts[1:]:
        if abs(p[0] - out[-1][0]) + abs(p[1] - out[-1][1]) >= tol: out.append(p)
    return out
def rings(geom):
    t, c = geom['type'], geom['coordinates']
    if t == 'Polygon': return c
    if t == 'MultiPolygon': return [r for poly in c for r in poly]
    if t == 'LineString': return [c]
    if t == 'MultiLineString': return c
    return []
def layer(fn, tol, keep=lambda p: True):
    out = []
    for f in json.load(open(os.path.join(NE, fn), encoding='utf-8'))['features']:
        if not keep(f['properties']): continue
        for r in rings(f['geometry']):
            if not any(inwin(*q[:2]) for q in r): continue
            pts = simp([pr(*q[:2]) for q in r], tol)
            if len(pts) >= 2: out.append(pts)
    return out
land = layer('ne_50m_land.geojson', 1.2); lakes = layer('ne_50m_lakes.geojson', 1.0)
rail = layer('ne_10m_railroads_north_america.geojson', 1.5)
towns = {'Chicago': (-87.63, 41.88), 'Carlinville': (-89.88, 39.28), 'North Redwood': (-95.10, 44.57), 'Minneapolis': (-93.27, 44.98),
         'Wood River': (-90.10, 38.86), 'Springfield': (-89.65, 39.80), 'St. Louis': (-90.20, 38.63), 'Hoffman Estates': (-88.08, 42.04),
         'Waukesha': (-88.23, 43.01), 'Cairo': (-89.18, 37.00), 'Norwood': (-84.46, 39.16)}
json.dump({'W': 1000, 'H': H, 'land': land, 'lakes': lakes, 'rail': rail, 'towns': {k: pr(*v) for k, v in towns.items()}},
          open(os.path.join(D, 'assets', 'map.json'), 'w'), separators=(',', ':'))
print('H', H, 'land', len(land), 'lakes', len(lakes), 'rail', len(rail), sum(len(r) for r in rail), 'pts')
