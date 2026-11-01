"""리포트 04(소장 박사학위논문 리뷰) 대표 이미지(1600x900)와 표지(600x800) 생성
사용법: python3 scripts/thumbs/make3.py <출력 폴더>
"""
from playwright.sync_api import sync_playwright
import os, sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
NAVY, ORANGE, CREAM, SAND, GRAY, LINE, WHITE = '#1E2A3A', '#C8792D', '#F7F5F0', '#ECE7DD', '#8A96A8', '#D5D9E0', '#FFFFFF'
FONT = "'Noto Sans CJK KR','Noto Sans KR',sans-serif"
SERIF = "'Noto Serif CJK KR','Noto Serif KR',serif"
DEFS = (f'<defs><marker id="ag" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{LINE}"/></marker>'
        f'<marker id="ao" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{ORANGE}"/></marker>'
        f'<marker id="an" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{NAVY}"/></marker></defs>')

def frame(inner, bg=CREAM, w=1600, h=900):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}"><rect width="{w}" height="{h}" fill="{bg}"/>{DEFS}{inner}</svg>'

LOGO = lambda x, y, s, ink, org: f'<g transform="translate({x} {y}) scale({s})"><path d="M50 348 V160 A140 140 0 0 1 330 160 V348" fill="none" stroke="{ink}" stroke-width="16"/><rect x="7" y="348" width="366" height="16" fill="{ink}"/><rect x="103" y="262" width="47" height="86" fill="{ink}"/><rect x="167" y="215" width="47" height="133" fill="{ink}"/><rect x="230" y="159" width="47" height="189" fill="{org}"/></g>'

# 연구모형: SSTQUAL 7요인 → 플로우 → 지속이용의도, 디지털 리터러시 조절
factors = [('편리성', None), ('기능성', None), ('디자인성', None), ('보안성/개인정보', None), ('즐거움', '.307'), ('확신성', None), ('고객화', '.298')]
s = ''
y0, gap = 150, 92
fx, fy = 860, 470      # 플로우 상자 중심
for i, (name, beta) in enumerate(factors):
    y = y0 + i * gap
    hi = beta is not None
    s += f'<rect x="150" y="{y - 32}" width="330" height="64" rx="12" fill="{ORANGE if hi else WHITE}" stroke="{ORANGE if hi else LINE}" stroke-width="3"/>'
    s += f'<text x="315" y="{y + 10}" font-size="28" font-weight="700" fill="{WHITE if hi else NAVY}" text-anchor="middle">{name}</text>'
    s += f'<path d="M484 {y} L{fx - 150} {fy}" stroke="{ORANGE if hi else LINE}" stroke-width="{6 if hi else 3}" fill="none" marker-end="url(#{"ao" if hi else "ag"})"/>'
    if hi:
        mx, my = 484 + (fx - 150 - 484) * 0.45, y + (fy - y) * 0.45
        s += f'<rect x="{mx - 46}" y="{my - 24}" width="92" height="40" rx="8" fill="{CREAM}"/><text x="{mx}" y="{my + 6}" font-size="26" font-weight="700" fill="{ORANGE}" text-anchor="middle">β {beta}</text>'
s += f'<text x="315" y="105" font-size="26" font-weight="700" fill="{GRAY}" text-anchor="middle">SSTQUAL 7요인</text>'
s += f'<rect x="{fx - 140}" y="{fy - 60}" width="280" height="120" rx="60" fill="{NAVY}"/><text x="{fx}" y="{fy + 4}" font-size="38" font-weight="700" fill="{WHITE}" text-anchor="middle">플로우</text><text x="{fx}" y="{fy + 40}" font-size="20" fill="#C9D1DC" text-anchor="middle">몰입 경험</text>'
s += f'<path d="M{fx + 144} {fy} L1180 {fy}" stroke="{NAVY}" stroke-width="6" fill="none" marker-end="url(#an)"/><text x="{(fx + 144 + 1180) / 2}" y="{fy - 20}" font-size="26" font-weight="700" fill="{NAVY}" text-anchor="middle">β .610</text>'
s += f'<rect x="1190" y="{fy - 60}" width="260" height="120" rx="14" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/><text x="1320" y="{fy + 12}" font-size="32" font-weight="700" fill="{NAVY}" text-anchor="middle">지속이용의도</text>'
s += f'<rect x="{fx - 130}" y="150" width="260" height="70" rx="12" fill="{SAND}"/><text x="{fx}" y="194" font-size="26" font-weight="700" fill="{NAVY}" text-anchor="middle">디지털 리터러시</text>'
s += f'<path d="M{fx} 224 L{fx} 350" stroke="{GRAY}" stroke-width="4" stroke-dasharray="10 8" fill="none"/><text x="{fx + 16}" y="300" font-size="22" fill="{GRAY}">조절</text>'
s += f'<text x="800" y="830" font-size="26" fill="{NAVY}" text-anchor="middle">n = 461 · 호텔 셀프 체크인/아웃 키오스크 이용객</text>'
imgs = {'report-hotel-kiosk-sstqual-flow': frame(s)}

no, lines = '04', ['호텔 키오스크 품질과', '고객의 몰입']
t = ''.join(f'<text x="56" y="{330 + i*62}" font-family="{SERIF}" font-size="44" font-weight="700" fill="{WHITE}">{l}</text>' for i, l in enumerate(lines))
cov = {'report-hotel-kiosk-sstqual-flow': frame(f'''<rect x="0" y="0" width="600" height="800" fill="{NAVY}"/><rect x="56" y="120" width="60" height="8" fill="{ORANGE}"/>
<text x="56" y="180" font-size="24" font-weight="700" fill="#C9D1DC" letter-spacing="6">REPORT {no}</text>{t}
<text x="56" y="470" font-size="22" fill="#C9D1DC">소장 박사학위논문 리뷰</text>
<line x1="56" y1="620" x2="544" y2="620" stroke="#3A4A62" stroke-width="2"/>{LOGO(56, 650, 0.2, WHITE, ORANGE)}
<text x="140" y="702" font-family="{SERIF}" font-size="24" font-weight="700" fill="{WHITE}">관광서비스품질연구소</text>''', bg=NAVY, w=600, h=800)}

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg = b.new_page(viewport={'width': 1600, 'height': 900})
    for name, svg in imgs.items():
        pg.set_content(f'<html><body style="margin:0">{svg}</body></html>'); pg.wait_for_timeout(150)
        pg.screenshot(path=f'{OUT}/{name}.png', clip={'x': 0, 'y': 0, 'width': 1600, 'height': 900})
    for name, svg in cov.items():
        pg.set_content(f'<html><body style="margin:0">{svg}</body></html>'); pg.wait_for_timeout(150)
        pg.screenshot(path=f'{OUT}/{name}-cover.png', clip={'x': 0, 'y': 0, 'width': 600, 'height': 800})
    b.close()
print('done')
