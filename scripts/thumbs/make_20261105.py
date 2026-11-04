"""관광정책·트렌드 기사 2편 대표 이미지(1600x900) 원본 생성
사용법: python3 scripts/thumbs/make_20261105.py
결과: scripts/thumbs/originals/<슬러그>.jpg (로고 없음) → watermark.py로 최종 이미지 생성
오른쪽 아래(가로 1080~1475, 세로 815 아래)는 로고 자리로 비워 둔다.
"""
from playwright.sync_api import sync_playwright
from PIL import Image
import os, io
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'scripts', 'thumbs', 'originals')
NAVY, ORANGE, CREAM, SAND, GRAY, LINE, WHITE = '#1E2A3A', '#C8792D', '#F7F5F0', '#ECE7DD', '#8A96A8', '#D5D9E0', '#FFFFFF'
FONT = "'Noto Sans CJK KR','Noto Sans KR',sans-serif"
DEFS = f'<defs><marker id="ag" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{GRAY}"/></marker><marker id="ao" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{ORANGE}"/></marker><marker id="an" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{NAVY}"/></marker></defs>'
def frame(inner): return f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" font-family="{FONT}"><rect width="1600" height="900" fill="{CREAM}"/>{DEFS}{inner}</svg>'
def t(x, y, s, size=26, fill=NAVY, w=700, a='middle'): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{s}</text>'
def box(x, y, w, h, fill=WHITE, stroke=LINE, sw=3, r=14): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def arrow(x1, y1, x2, y2, col=GRAY, m='ag', w=5): return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{col}" stroke-width="{w}" fill="none" marker-end="url(#{m})"/>'
imgs = {}

# 1) 5대 관광권 (허브형) + 숙박 신규 사업 (오른쪽 패널)
s = t(800, 105, '지방공항 5대 관광권과 2027년 숙박 사업', 36)
s += t(800, 148, '문화체육관광부 발표(2026년 9월) · 2027년 예산안 기준', 22, GRAY, 500)
cx, cy = 500, 470
zones = [('김해', '부산·울산·거제·통영', 470, 250), ('대구', '대구·경주·안동', 720, 390), ('청주', '청주·공주·부여·전주', 220, 390), ('양양', '양양·강릉·속초', 650, 640), ('무안', '무안·목포·광주·여수', 290, 640)]
for n, d, x, y in [(a, b, x + 30, y) for a, b, x, y in zones]:
    s += f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="{LINE}" stroke-width="4"/>'
s += f'<circle cx="{cx}" cy="{cy}" r="95" fill="{NAVY}"/>' + t(cx, cy - 8, '국비 659억', 28, WHITE) + t(cx, cy + 30, '지방비 276억', 20, '#C9CED6', 500)
for n, d, x, y in [(a, b, x + 30, y) for a, b, x, y in zones]:
    s += box(x - 110, y - 50, 220, 100, WHITE, ORANGE, 3) + t(x, y - 6, n + '공항권', 26, ORANGE) + t(x, y + 28, d, 18, NAVY, 600)
s += box(930, 230, 545, 450, SAND, SAND, 0)
s += t(1202, 285, '숙박 분야 예산안', 28)
items = [('40억', '숙박업 품질 평가·컨설팅'), ('16억', '숙박정보 통합플랫폼'), ('1,523억', '지역 대형 호텔 건립 융자')]
for i, (a, b) in enumerate(items):
    y = 330 + i * 110
    s += box(960, y, 485, 90, WHITE, LINE, 2, 12) + t(1080, y + 58, a, 34, ORANGE, 800) + t(1190, y + 55, b, 22, NAVY, 600, 'start')
s += t(800, 770, '관광객을 지방으로 데려오는 정책, 머물게 하는 것은 숙박의 품질', 26)
imgs['regional-tourism-zones-2027-budget'] = frame(s)

# 2) 방한객 vs 카드 소비 증가율 (막대 차트) + 결제 수단 변화
s = t(800, 105, '방한객보다 두 배 빨리 늘어난 외국인 카드 소비', 36)
s += t(800, 148, '2026년 1~9월 · 전년 같은 기간 대비 (문화체육관광부 발표 보도 기준)', 22, GRAY, 500)
base = 660
s += f'<line x1="170" y1="{base}" x2="760" y2="{base}" stroke="{NAVY}" stroke-width="3"/>'
for x, v, lab, sub, col in [(250, 21.5, '방한객', '1,711만 명', GRAY), (520, 47.7, '관광 카드 소비', '15조 9,416억 원', ORANGE)]:
    h = v * 8.5
    s += f'<rect x="{x}" y="{base - h}" width="170" height="{h}" rx="8" fill="{col}"/>'
    s += t(x + 85, base - h - 22, f'+{v}%', 44, col if col == ORANGE else NAVY, 800)
    s += t(x + 85, base + 42, lab, 24) + t(x + 85, base + 76, sub, 19, GRAY, 600)
s += box(850, 215, 625, 470, WHITE, LINE, 3)
s += t(1162, 268, '넓어지는 외국인 결제 수단', 28)
rows = [('선불카드', '국내 계좌 없이 환전·충전·결제'), ('한도 특례', '무기명 선불 50만 → 100만 원'), ('오픈루프', '해외카드로 버스 결제, 2027년 1월')]
for i, (a, b) in enumerate(rows):
    y = 305 + i * 120
    s += f'<circle cx="905" cy="{y + 40}" r="14" fill="{ORANGE if i == 0 else NAVY}"/>'
    s += t(940, y + 32, a, 26, NAVY, 700, 'start') + t(940, y + 70, b, 21, GRAY, 600, 'start')
s += t(800, 790, '호텔의 결제 단말과 보증금 안내도 함께 점검할 때', 26)
imgs['inbound-payment-convenience-2026'] = frame(s)

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
