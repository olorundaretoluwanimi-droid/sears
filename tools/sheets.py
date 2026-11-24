# sheets.py <prefix> [per_sheet]: contact sheets of stills/t_*.jpg in time order → research/<prefix>N.jpg (6 per row, labelled with time)
import glob, re, sys, subprocess, os
f = sorted(glob.glob('stills/t_*.jpg'), key=lambda p: float(re.findall(r't_([\d.]+)\.jpg', p)[0])); n = int(sys.argv[2]) if len(sys.argv) > 2 else 36
for i in range(0, len(f), n): subprocess.run([sys.executable, 'tools/sheet.py', f'research/{sys.argv[1]}{i // n + 1}.jpg', '6', '330'] + f[i:i + n], check=True)
