"""호텔 & 리조트 게시판 첫 기사 3편 대표 이미지(1600x900) 생성
사용법: python3 scripts/thumbs/make_20261104.py <출력 폴더>
"""
from playwright.sync_api import sync_playwright
import os, sys
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
NAVY, ORANGE, CREAM, SAND, GRAY, LINE, WHITE = '#1E2A3A', '#C8792D', '#F7F5F0', '#ECE7DD', '#8A96A8', '#D5D9E0', '#FFFFFF'
FONT = "'Noto Sans CJK KR','Noto Sans KR',sans-serif"
DEFS = f'<defs><marker id="ag" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{GRAY}"/></marker><marker id="ao" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{ORANGE}"/></marker></defs>'
def frame(inner, bg=CREAM): return f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" font-family="{FONT}"><rect width="1600" height="900" fill="{bg}"/>{DEFS}{inner}</svg>'
def t(x, y, s, size=26, fill=NAVY, w=700, a='middle'): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{s}</text>'
imgs = {}

# 1) 3분기 숙박시장: 단가 vs 점유율 막대 (전년 동기 대비, 야놀자리서치 보도)
s = t(800, 120, '2026년 3분기 숙박시장, 무엇이 성장을 이끌었나', 34)
s += t(800, 165, '전년 동기 대비 증감률 · 야놀자리서치 보도 기준', 22, GRAY, 500)
base = 700; scale = 16   # 1% = 16px
groups = [('호텔·리조트', [('객실 단가', 9.0), ('점유율', 1.0), ('RevPAR', 10.1)]),
          ('리조트', [('객실 단가', 17.1), ('점유율', 6.9), ('RevPAR', 25.2)])]
gx = [260, 900]
for (gname, bars), x0 in zip(groups, gx):
    s += f'<line x1="{x0 - 30}" y1="{base}" x2="{x0 + 470}" y2="{base}" stroke="{LINE}" stroke-width="3"/>'
    for i, (lab, v) in enumerate(bars):
        x = x0 + i * 150; h = v * scale
        col = ORANGE if lab == '객실 단가' else (NAVY if lab == 'RevPAR' else GRAY)
        s += f'<rect x="{x}" y="{base - h}" width="110" height="{h}" rx="6" fill="{col}"/>'
        s += t(x + 55, base - h - 14, f'+{v}%', 28, col)
        s += t(x + 55, base + 38, lab, 22, NAVY, 600)
    s += t(x0 + 205, base + 95, gname, 30)
s += f'<rect x="270" y="300" width="340" height="64" rx="12" fill="{WHITE}" stroke="{ORANGE}" stroke-width="3"/>' + t(440, 341, '성장은 가격에서 나왔다', 24, ORANGE)
imgs['lodging-q3-2026-price-led-growth'] = frame(s)

# 2) 브랜드 재편: 위로(하이엔드) / 옆으로(전환·지방)
s = t(800, 120, '호텔 브랜드 재편의 두 방향', 36)
# 왼쪽: 롯데 - 위로
s += f'<rect x="200" y="560" width="440" height="110" rx="12" fill="{SAND}"/>' + t(420, 605, '롯데호텔 서울', 28) + t(420, 645, '1979년 개관 · 1,015실', 22, GRAY, 500)
s += f'<path d="M420 545 L420 395" stroke="{ORANGE}" stroke-width="6" marker-end="url(#ao)"/>' + t(470, 480, '하이엔드로', 24, ORANGE, 700, 'start')
s += f'<rect x="200" y="250" width="440" height="120" rx="12" fill="{NAVY}"/>' + t(420, 300, '더그랜드롯데 서울', 30, WHITE) + t(420, 342, '2026년 8월 · 868실', 22, '#C9CED6', 500)
s += t(420, 740, '위로: 객실은 줄이고 가치는 높인다', 26)
# 오른쪽: 조선 - 옆으로
s += f'<line x1="800" y1="200" x2="800" y2="760" stroke="{LINE}" stroke-width="3" stroke-dasharray="10 10"/>'
for i, (a, b) in enumerate([('종로', '232실 · 2027년 상반기'), ('여수', '427실 · 첫 호남권')]):
    y = 270 + i * 190
    s += f'<rect x="900" y="{y}" width="200" height="110" rx="12" fill="{SAND}"/>' + t(1000, y + 50, '기존 호텔', 24) + t(1000, y + 85, a, 22, GRAY, 600)
    s += f'<path d="M1110 {y + 55} L1210 {y + 55}" stroke="{GRAY}" stroke-width="5" marker-end="url(#ag)"/>'
    s += f'<rect x="1225" y="{y}" width="250" height="110" rx="12" fill="{WHITE}" stroke="{ORANGE}" stroke-width="3"/>' + t(1350, y + 50, '조선 브랜드', 26) + t(1350, y + 85, b, 20, ORANGE, 700)
s += t(1180, 690, '2030년 국내 14곳 목표', 24, GRAY, 600)
s += t(1180, 740, '옆으로: 인수·전환으로 지방 확장', 26)
imgs['hotel-brand-portfolio-2026'] = frame(s)

# 3) 미국 호텔 전망: RevPAR 전망 상향 + 수요 구성
s = t(800, 120, '2026년 미국 호텔시장 전망', 36)
s += t(420, 210, 'RevPAR 증가율 전망 (CoStar·Tourism Economics)', 22, GRAY, 600)
for i, (lab, v, col) in enumerate([('이전 전망', 2.8, GRAY), ('8월 상향', 4.4, ORANGE)]):
    x = 230 + i * 220; h = v * 90
    s += f'<rect x="{x}" y="{680 - h}" width="150" height="{h}" rx="8" fill="{col}"/>' + t(x + 75, 680 - h - 16, f'+{v}%', 34, col) + t(x + 75, 722, lab, 24, NAVY, 600)
s += f'<line x1="200" y1="680" x2="640" y2="680" stroke="{LINE}" stroke-width="3"/>'
s += f'<line x1="800" y1="200" x2="800" y2="760" stroke="{LINE}" stroke-width="3" stroke-dasharray="10 10"/>'
s += t(1150, 210, '수요 구성 (Marcus &amp; Millichap)', 22, GRAY, 600)
rows = [('해외 방문객', '−4.3%', GRAY, '6월까지 누적'), ('단체 숙박', '+2.4%', NAVY, '6월까지 누적'), ('출장 예약', '+5.6~8.6%', ORANGE, '8~10월 예약')]
for i, (a, v, col, note) in enumerate(rows):
    y = 260 + i * 140
    s += f'<rect x="900" y="{y}" width="500" height="110" rx="12" fill="{WHITE}" stroke="{LINE}" stroke-width="3"/>'
    s += t(930, y + 50, a, 28, NAVY, 700, 'start') + t(930, y + 88, note, 20, GRAY, 500, 'start') + t(1375, y + 70, v, 34, col, 800, 'end')
s += t(800, 820, '해외 수요의 빈자리를 국내 단체·출장 수요가 채웠다', 26)
imgs['us-hotel-outlook-2026'] = frame(s)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': 1600, 'height': 900})
    for name, svg in imgs.items():
        pg.set_content(f'<html><body style="margin:0">{svg}</body></html>'); pg.wait_for_timeout(150)
        pg.screenshot(path=f'{OUT}/{name}.png', clip={'x': 0, 'y': 0, 'width': 1600, 'height': 900})
    b.close()
print('done')
