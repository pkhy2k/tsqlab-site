"""2026-11-02 주간 기사 3편 대표 이미지(1600x900) 생성
사용법: python3 scripts/thumbs/make_20261102.py <출력 폴더>
PNG 렌더 후 static/images/posts/<슬러그>.jpg 로 JPEG(quality 88) 변환
"""
from playwright.sync_api import sync_playwright
from PIL import Image
import os, sys
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
JPG = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'images', 'posts')
NAVY, ORANGE, CREAM, SAND, GRAY, LINE, WHITE, RED = '#1E2A3A', '#C8792D', '#F7F5F0', '#ECE7DD', '#8A96A8', '#D5D9E0', '#FFFFFF', '#C0504D'
FONT = "'Noto Sans CJK KR','Noto Sans KR',sans-serif"
DEFS = f'<defs><marker id="ag" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{GRAY}"/></marker><marker id="ao" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{ORANGE}"/></marker></defs>'
def frame(inner, bg=CREAM): return f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" font-family="{FONT}"><rect width="1600" height="900" fill="{bg}"/>{DEFS}{inner}</svg>'
def t(x, y, s, size=26, fill=NAVY, w=700, a='middle'): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{s}</text>'
imgs = {}

# 1) 서비스 청사진: 4층 + 3선, 실패 지점
s = t(800, 100, '호텔 체크인 서비스 청사진', 36)
rows = [('고객 행동', ['도착', '예약 확인 요청', '결제', '키 수령']),
        ('현장 직원', ['인사', '예약 조회', '결제 처리', '객실 안내']),
        ('후방 직원', ['', '객실 배정 조정', '', '하우스키핑 확인']),
        ('지원 시스템', ['', 'PMS · 채널 예약', '결제 승인', '키 발급 · 객실 상태'])]
lines = [('상호작용선', 290), ('가시선', 450), ('내부 상호작용선', 610)]
for i, (lab, cells) in enumerate(rows):
    y = 150 + i * 160
    s += f'<rect x="80" y="{y + 20}" width="230" height="100" rx="12" fill="{NAVY if i < 2 else "#3B4A60"}"/>' + t(195, y + 80, lab, 28, WHITE)
    for j, c in enumerate(cells):
        if not c: continue
        x = 360 + j * 300
        s += f'<rect x="{x}" y="{y + 25}" width="260" height="90" rx="10" fill="{WHITE}" stroke="{LINE}" stroke-width="3"/>' + t(x + 130, y + 80, c, 24 if len(c) < 9 else 21)
for lab, y in lines:
    dash = '' if lab == '가시선' else 'stroke-dasharray="12 9"'
    col = ORANGE if lab == '가시선' else GRAY
    s += f'<line x1="80" y1="{y + 10}" x2="1540" y2="{y + 10}" stroke="{col}" stroke-width="{5 if lab == "가시선" else 3}" {dash}/>'
    s += f'<rect x="1350" y="{y - 8}" width="190" height="36" rx="18" fill="{CREAM}"/>' + t(1530, y + 20, lab, 20, col, 700, 'end')
for cx, cy in [(905, 675), (1505, 675), (905, 515)]:
    s += f'<circle cx="{cx}" cy="{cy}" r="22" fill="{RED}"/>' + t(cx, cy + 9, 'F', 24, WHITE)
s += f'<circle cx="1180" cy="850" r="16" fill="{RED}"/>' + t(1206, 858, '실패 지점(Fail Point)', 22, NAVY, 600, 'start')
imgs['service-blueprint-hotel-checkin'] = frame(s)

# 2) 채널 매니저 연동
s = t(800, 100, '객실 재고는 시스템 사이에서 틀어진다', 36)
s += f'<rect x="110" y="330" width="280" height="240" rx="20" fill="{NAVY}"/>' + t(250, 440, 'PMS', 44, WHITE) + t(250, 490, '재고 · 요금', 24, '#C9D1DC', 500)
s += f'<rect x="620" y="330" width="320" height="240" rx="20" fill="{ORANGE}"/>' + t(780, 440, '채널 매니저', 38, WHITE) + t(780, 490, '분배 · 수신', 24, WHITE, 500)
s += f'<path d="M400 420 L605 420" stroke="{GRAY}" stroke-width="5" marker-end="url(#ag)"/><path d="M610 480 L405 480" stroke="{GRAY}" stroke-width="5" marker-end="url(#ag)"/>'
s += t(505, 400, '재고·요금', 20, GRAY, 600) + t(505, 520, '예약', 20, GRAY, 600)
chans = ['OTA A', 'OTA B', 'OTA C', '자사 예약 엔진']
for i, c in enumerate(chans):
    y = 170 + i * 135
    s += f'<rect x="1180" y="{y}" width="300" height="95" rx="14" fill="{WHITE}" stroke="{LINE}" stroke-width="3"/>' + t(1330, y + 58, c, 28)
    s += f'<path d="M950 450 L1165 {y + 48}" stroke="{GRAY}" stroke-width="3" marker-end="url(#ag)"/>'
s += f'<line x1="1110" y1="{170 + 3 * 135 + 48 - 30}" x2="1150" y2="{170 + 3 * 135 + 48}" stroke="{RED}" stroke-width="6"/><line x1="1150" y1="{170 + 3 * 135 + 48 - 30}" x2="1110" y2="{170 + 3 * 135 + 48}" stroke="{RED}" stroke-width="6"/>'
for i, lab in enumerate(['지연', '중복', '순서 뒤바뀜', '부분 실패']):
    x = 190 + i * 330
    s += f'<rect x="{x}" y="730" width="270" height="76" rx="38" fill="{SAND}" stroke="{ORANGE}" stroke-width="3"/>' + t(x + 135, 778, lab, 28, ORANGE)
imgs['channel-manager-integration-testing'] = frame(s)

# 3) 방한객 vs 체류일수
s = t(800, 100, '방한객은 늘고, 머무는 날은 줄었다', 36)
s += t(430, 190, '방한 외래객', 30) + t(1170, 190, '평균 체류일수', 30)
base = 700
for i, (yr, v) in enumerate([('2023', 1103), ('2025', 1894)]):
    h = v / 1894 * 420; x = 250 + i * 220
    s += f'<rect x="{x}" y="{base - h}" width="150" height="{h}" rx="8" fill="{NAVY if i else GRAY}"/>' + t(x + 75, base - h - 18, f'{v:,}만 명', 26) + t(x + 75, base + 45, yr, 26, GRAY, 600)
for i, (yr, v) in enumerate([('2023', 7.8), ('2025', 6.5)]):
    h = v / 7.8 * 420; x = 990 + i * 220
    s += f'<rect x="{x}" y="{base - h}" width="150" height="{h}" rx="8" fill="{ORANGE if i else GRAY}"/>' + t(x + 75, base - h - 18, f'{v}일', 26) + t(x + 75, base + 45, yr, 26, GRAY, 600)
s += f'<line x1="800" y1="200" x2="800" y2="760" stroke="{LINE}" stroke-width="3"/>'
s += t(430, 820, '+71.7%', 32, NAVY) + t(1170, 820, '−1.3일', 32, ORANGE)
s += t(800, 870, '국정감사 제출 자료(한국관광공사) 보도 기준', 20, GRAY, 500)
imgs['inbound-tourists-stay-quality-2026'] = frame(s)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': 1600, 'height': 900})
    for name, svg in imgs.items():
        pg.set_content(f'<html><body style="margin:0">{svg}</body></html>'); pg.wait_for_timeout(200)
        png = f'{OUT}/{name}.png'
        pg.screenshot(path=png, clip={'x': 0, 'y': 0, 'width': 1600, 'height': 900})
        Image.open(png).convert('RGB').save(os.path.join(JPG, f'{name}.jpg'), 'JPEG', quality=88)
    b.close()
print('done')
