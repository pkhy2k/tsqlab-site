"""호텔 & 리조트 기사 2편 대표 이미지(1600x900) 원본 생성 (2026-11-07)
사용법: python3 scripts/thumbs/make_20261107.py
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
def arrow(x1, y1, x2, y2, col=GRAY, m='ag', w=5): return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{col}" stroke-width="{w}" fill="none" marker-end="url(#{m})"/>'
imgs = {}
def box(x, y, w, h, fill=WHITE, stroke=LINE, sw=3, r=14): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

# 1) 서울 호텔 투자와 용도 전환 (수치 비교 + 전환 흐름)
s = t(800, 105, '오피스가 호텔이 된다, 2026년 서울 호텔 투자', 36)
s += t(800, 150, '부동산 자문사 보고서와 보도 기준', 22, GRAY, 500)
s += box(140, 215, 600, 420, WHITE, LINE, 3)
s += t(440, 268, '2026년 상반기 서울 호텔 거래액', 24)
s += t(440, 300, '두 기관의 집계가 다르다', 19, GRAY, 600)
# bars (scale: 1.5조 -> 380px)
for i, (lab, v, txt, col) in enumerate([('쿠시먼앤드웨이크필드', 1.1, '약 1.1조 원', NAVY), ('젠스타메이트', 1.5, '약 1.5조 원', ORANGE)]):
    y = 355 + i * 130
    w = int(v / 1.5 * 330)
    s += t(170, y, lab, 20, GRAY, 600, 'start')
    s += f'<rect x="170" y="{y + 15}" width="{w}" height="56" rx="8" fill="{col}"/>' + t(170 + w + 12, y + 53, txt, 24, col, 800, 'start')
s += t(440, 612, '쿠시먼: 전년 대비 +71%', 20, NAVY, 600)
s += arrow(760, 425, 830, 425, ORANGE, 'ao', 6)
s += box(845, 215, 630, 420, SAND, SAND, 0)
s += t(1160, 268, '3분기: 노후 오피스 → 호텔 전환', 26)
steps = [('오피스 매입', '두산타워 약 8,971억 원'), ('용도 전환', '일부 · 전체 호텔로'), ('호텔 운영', '객실 공급 부족 지역')]
for i, (a, b) in enumerate(steps):
    y = 310 + i * 105
    c = NAVY if i < 2 else ORANGE
    s += box(895, y, 530, 80, WHITE, c, 3) + t(1010, y + 50, a, 26, c, 800) + t(1270, y + 50, b, 20, NAVY, 600)
    if i < 2: s += arrow(1160, y + 82, 1160, y + 100, GRAY, 'ag', 4)
s += t(800, 725, '투자 수치는 기대 수익, 실현 여부는 개관 후 고객이 느끼는 품질에 달려 있다', 25)
imgs['seoul-hotel-investment-conversion-2026'] = frame(s)

# 2) 일본 호텔: 방문객과 객실 단가 (양방향 막대 차트)
s = t(800, 105, '중국인 관광객이 줄어든 일본 호텔', 36)
s += t(800, 150, '2026년 9월, 전년 같은 달 대비 (JNTO · STR 자료 보도 기준)', 22, GRAY, 500)
def panel(x0, title, rows, vmax):
    o = box(x0, 200, 640, 470, WHITE, LINE, 3) + t(x0 + 320, 250, title, 26)
    zero = x0 + 320
    o += f'<line x1="{zero}" y1="280" x2="{zero}" y2="640" stroke="{LINE}" stroke-width="3"/>'
    for i, (lab, v) in enumerate(rows):
        y = 300 + i * 115
        w = int(abs(v) / vmax * 170)
        col = ORANGE if v > 0 else NAVY
        x = zero if v > 0 else zero - w
        o += t(x0 + 320, y + 8, lab, 22, NAVY, 700)
        o += f'<rect x="{x}" y="{y + 25}" width="{w}" height="50" rx="6" fill="{col}"/>'
        sign = '+' if v > 0 else '−'
        lx, an = (zero + w + 12, 'start') if v > 0 else (zero - w - 12, 'end')
        o += t(lx, y + 62, f'{sign}{abs(v)}%', 26, col, 800, an)
    return o
s += panel(140, '방일 외국인 수', [('중국', -44.5), ('한국', 25.6), ('대만', 13.0)], 44.5)
s += panel(835, '평균 객실 단가(ADR)', [('전국', 8.8), ('도쿄', 8.4), ('오사카', -19.7)], 19.7)
s += t(800, 735, '방문객 구성이 바뀌자, 같은 나라 안에서도 객실 단가가 엇갈렸다', 26)
imgs['japan-hotels-china-demand-shift-2026'] = frame(s)

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
