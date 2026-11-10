"""영어판 대표 이미지(1600x900) 원본 생성 — 다국어 예시 3편
사용법: python3 scripts/thumbs/make_en_20261110.py
결과: scripts/thumbs/originals/en/<슬러그>.jpg (로고 없음) → python3 scripts/thumbs/watermark.py --en <슬러그> ...
한국어 원본 스크립트(make_20261105.py, make_20261104.py, make_20261104b.py)의 도식을 그대로 두고 글자만 영어로 바꿨다.
오른쪽 아래(가로 1080~1475, 세로 815 아래)는 로고 자리로 비워 둔다. 수치는 본문에 나온 숫자만 쓴다.
"""
from playwright.sync_api import sync_playwright
from PIL import Image
import os, io
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'scripts', 'thumbs', 'originals', 'en')
NAVY, ORANGE, CREAM, SAND, GRAY, LINE, WHITE = '#1E2A3A', '#C8792D', '#F7F5F0', '#ECE7DD', '#8A96A8', '#D5D9E0', '#FFFFFF'
FONT = "'Noto Sans','Noto Sans CJK KR',sans-serif"
DEFS = f'<defs><marker id="ag" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{GRAY}"/></marker><marker id="ao" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{ORANGE}"/></marker><marker id="an" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{NAVY}"/></marker></defs>'
def frame(inner): return f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" font-family="{FONT}"><rect width="1600" height="900" fill="{CREAM}"/>{DEFS}{inner}</svg>'
def t(x, y, s, size=26, fill=NAVY, w=700, a='middle'): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{s}</text>'
def box(x, y, w, h, fill=WHITE, stroke=LINE, sw=3, r=14): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def arrow(x1, y1, x2, y2, col=GRAY, m='ag', w=5): return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{col}" stroke-width="{w}" fill="none" marker-end="url(#{m})"/>'
imgs = {}

# 1) 방한객 vs 카드 소비 증가율 (make_20261105.py 2번)
s = t(800, 105, "Foreign card spending grew twice as fast as visitor numbers", 34)
s += t(800, 148, 'January–September 2026, year on year (as reported from Ministry of Culture, Sports and Tourism data)', 21, GRAY, 500)
base = 660
s += f'<line x1="170" y1="{base}" x2="760" y2="{base}" stroke="{NAVY}" stroke-width="3"/>'
for x, v, lab, sub, col in [(250, 21.5, 'Foreign visitors', '17.11 million', GRAY), (520, 47.7, 'Tourism card spending', 'KRW 15.94 trillion', ORANGE)]:
    h = v * 8.5
    s += f'<rect x="{x}" y="{base - h}" width="170" height="{h}" rx="8" fill="{col}"/>'
    s += t(x + 85, base - h - 22, f'+{v}%', 44, col if col == ORANGE else NAVY, 800)
    s += t(x + 85, base + 42, lab, 22) + t(x + 85, base + 76, sub, 19, GRAY, 600)
s += box(850, 215, 625, 470, WHITE, LINE, 3)
s += t(1162, 268, 'More ways for visitors to pay', 28)
rows = [('Prepaid cards', 'Exchange, top up and pay without a Korean account'), ('Higher limit', 'Anonymous prepaid: KRW 0.5M → 1M'), ('Open loop', 'Foreign cards on Seoul buses, Jan 2027')]
for i, (a, b) in enumerate(rows):
    y = 305 + i * 120
    s += f'<circle cx="905" cy="{y + 40}" r="14" fill="{ORANGE if i == 0 else NAVY}"/>'
    s += t(940, y + 32, a, 26, NAVY, 700, 'start') + t(940, y + 70, b, 20, GRAY, 600, 'start')
s += t(800, 790, "Time to check hotels' payment terminals and deposit guidance too", 26)
imgs['inbound-payment-convenience-2026'] = frame(s)

# 2) 3분기 숙박시장 단가 vs 점유율 (make_20261104.py 1번)
s = t(800, 120, 'What drove growth in Korea’s lodging market in Q3 2026?', 34)
s += t(800, 165, 'Change year on year · as reported from Yanolja Research', 22, GRAY, 500)
base = 700; scale = 16
groups = [('Hotels & resorts', [('ADR', 9.0), ('Occupancy', 1.0), ('RevPAR', 10.1)]),
          ('Resorts', [('ADR', 17.1), ('Occupancy', 6.9), ('RevPAR', 25.2)])]
gx = [260, 900]
for (gname, bars), x0 in zip(groups, gx):
    s += f'<line x1="{x0 - 30}" y1="{base}" x2="{x0 + 470}" y2="{base}" stroke="{LINE}" stroke-width="3"/>'
    for i, (lab, v) in enumerate(bars):
        x = x0 + i * 150; h = v * scale
        col = ORANGE if lab == 'ADR' else (NAVY if lab == 'RevPAR' else GRAY)
        s += f'<rect x="{x}" y="{base - h}" width="110" height="{h}" rx="6" fill="{col}"/>'
        s += t(x + 55, base - h - 14, f'+{v}%', 28, col)
        s += t(x + 55, base + 38, lab, 22, NAVY, 600)
    s += t(x0 + 205, base + 95, gname, 30)
s += f'<rect x="240" y="300" width="400" height="64" rx="12" fill="{WHITE}" stroke="{ORANGE}" stroke-width="3"/>' + t(440, 341, 'Growth came from price', 24, ORANGE)
imgs['lodging-q3-2026-price-led-growth'] = frame(s)

# 3) 에이전트 예약 흐름 (make_20261104b.py 1번)
s = t(800, 110, 'How does an AI agent book a hotel?', 36)
s += t(800, 155, "Based on Meta Muse's connection rules and the Cloudbeds integration announcement", 22, GRAY, 500)
s += box(140, 360, 230, 150, SAND, SAND) + t(255, 425, 'Traveller', 30) + t(255, 465, '"2 nights by the sea"', 20, GRAY, 600)
s += arrow(380, 435, 455, 435)
s += box(465, 340, 250, 190, NAVY, NAVY) + t(590, 420, 'AI agent', 30, WHITE) + t(590, 462, 'User approves purchase', 19, '#C9CED6', 500)
opts = [('① Connector', 'Used first if available', ORANGE), ('② Public API', 'Direct connection', NAVY), ('③ Browser', 'Operates the screen', GRAY)]
for i, (a, b, c) in enumerate(opts):
    y = 230 + i * 150
    s += arrow(720, 435, 800, y + 55, c, 'ao' if c == ORANGE else ('an' if c == NAVY else 'ag'), 4)
    s += box(810, y, 260, 110, WHITE, c, 3) + t(940, y + 48, a, 25, c) + t(940, y + 84, b, 19, GRAY, 600)
s += arrow(1080, 285, 1175, 400, ORANGE, 'ao', 5)
s += box(1185, 330, 290, 90, WHITE, ORANGE, 3) + t(1330, 385, 'Hotel booking engine', 24)
s += arrow(1330, 425, 1330, 480, NAVY, 'an', 5)
s += box(1185, 490, 290, 110, NAVY, NAVY) + t(1330, 540, 'PMS', 30, WHITE) + t(1330, 578, 'Recorded as direct booking', 19, '#C9CED6', 500)
s += t(800, 735, 'Agents can only choose hotels whose rates, inventory (ARI) and policies are accurate', 25, NAVY, 700)
imgs['ai-agent-booking-direct-channel-2026'] = frame(s)

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = b.new_page(viewport={'width': 1600, 'height': 900})
        for name, svg in imgs.items():
            pg.set_content(f'<html><body style="margin:0">{svg}</body></html>'); pg.wait_for_timeout(200)
            png = pg.screenshot(clip={'x': 0, 'y': 0, 'width': 1600, 'height': 900})
            Image.open(io.BytesIO(png)).convert('RGB').save(os.path.join(OUT, f'{name}.jpg'), 'JPEG', quality=88)
            print('ok', name)
        b.close()
