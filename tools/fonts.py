#!/usr/bin/env python3
"""Subset woff2 files from Google Fonts (all SIL OFL 1.1) into fonts/, covering printable ASCII plus the characters used in the
film (index.html, film.json). Delete fonts/ and rerun after adding unusual characters."""
import re, sys, urllib.parse, urllib.request, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = ''.join(open(os.path.join(D, f), encoding='utf-8').read() for f in ['index.html', 'film.json'] if os.path.exists(os.path.join(D, f)))
chars = ''.join(sorted(set(src + ''.join(chr(c) for c in range(32, 127)) + '’‘“”–—·×…≈→☞½¼¾é°') - set('\n\r\t')))
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'
JOBS = [('fell', 'IM Fell English:ital@0'), ('fell_i', 'IM Fell English:ital@1'), ('fellsc', 'IM Fell English SC'),
        ('ost400', 'Old Standard TT:wght@400'), ('ost700', 'Old Standard TT:wght@700'),
        ('serif400', 'Source Serif 4:wght@400'), ('serif600', 'Source Serif 4:wght@600'), ('serifi', 'Source Serif 4:ital,wght@1,400'),
        ('sans600', 'Source Sans 3:wght@600'), ('sans400', 'Source Sans 3:wght@400'), ('mono500', 'IBM Plex Mono:wght@500'),
        ('hand', 'Pinyon Script')]
os.makedirs(os.path.join(D, 'fonts'), exist_ok=True)
for name, fam in JOBS:
    url = 'https://fonts.googleapis.com/css2?' + urllib.parse.urlencode({'family': fam, 'text': chars, 'display': 'block'})
    css = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=60).read().decode()
    urls = re.findall(r'url\((https://[^)]+)\)', css)
    if not urls: sys.exit(f'no font url for {fam}')
    data = urllib.request.urlopen(urllib.request.Request(urls[0], headers={'User-Agent': UA}), timeout=60).read()
    open(os.path.join(D, f'fonts/{name}.woff2'), 'wb').write(data); print(name, len(data), 'bytes', len(urls), 'part(s)')
