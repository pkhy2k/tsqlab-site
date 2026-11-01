"""학위논문 기반 시리즈 대표 이미지(1600x900) 4종 생성
사용법: python3 scripts/thumbs/make4.py <출력 폴더>
"""
from playwright.sync_api import sync_playwright
import os, sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
NAVY, ORANGE, CREAM, SAND, GRAY, LINE, WHITE = '#1E2A3A', '#C8792D', '#F7F5F0', '#ECE7DD', '#8A96A8', '#D5D9E0', '#FFFFFF'
FONT = "'Noto Sans CJK KR','Noto Sans KR',sans-serif"
DEFS = (f'<defs><marker id="ag" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{GRAY}"/></marker>'
        f'<marker id="an2" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#1E2A3A"/></marker><marker id="ao" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{ORANGE}"/></marker></defs>')
def frame(inner, bg=CREAM, w=1600, h=900):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}"><rect width="{w}" height="{h}" fill="{bg}"/>{DEFS}{inner}</svg>'
def t(x, y, s, size=26, fill=NAVY, w=700, anchor='middle'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{s}</text>'
imgs = {}

# 1) 측정 도구의 흐름: SERVQUAL → SERVPERF → E-S-QUAL → SSTQUAL
steps = [('SERVQUAL', '1988', '사람 ↔ 사람'), ('SERVPERF', '1992', '성과 중심'), ('E-S-QUAL', '2005', '웹 ↔ 사람'), ('SSTQUAL', '2011', '기기 ↔ 사람')]
s = ''
for i, (n, y, d) in enumerate(steps):
    x = 140 + i * 350; last = i == 3; x += 0
    s += f'<rect x="{x}" y="230" width="280" height="170" rx="16" fill="{ORANGE if last else WHITE}" stroke="{ORANGE if last else LINE}" stroke-width="3"/>'
    s += t(x + 140, 300, n, 38, WHITE if last else NAVY) + t(x + 140, 350, y, 26, WHITE if last else GRAY, 500)
    s += t(x + 140, 460, d, 26, NAVY, 500)
    if i < 3: s += f'<path d="M{x + 288} 315 L{x + 340} 315" stroke="{GRAY}" stroke-width="4" marker-end="url(#ag)"/>'
dims = ['편리성', '기능성', '디자인성', '보안성/개인정보', '즐거움', '확신성', '고객화']
for i, d in enumerate(dims):
    x = 160 + i * 186
    s += f'<rect x="{x}" y="600" width="170" height="64" rx="32" fill="{NAVY}"/>' + t(x + 85, 641, d, 22 if len(d) > 4 else 25, WHITE)
s += f'<path d="M1190 500 L1190 545 M245 545 L1361 545 M245 545 L245 590 M1361 545 L1361 590" stroke="{ORANGE}" stroke-width="3" fill="none"/>'
s += t(800, 740, 'SSTQUAL 7가지 구성요인', 28, GRAY, 500)
imgs['sstqual-seven-dimensions'] = frame(s)

# 2) 4채널 플로우 모델
ox, oy, L = 240, 770, 580
s = f'<rect x="{ox}" y="{oy - L}" width="{L}" height="{L}" fill="{WHITE}" stroke="{LINE}" stroke-width="3"/>'
s += f'<rect x="{ox + L/2}" y="{oy - L}" width="{L/2}" height="{L/2}" fill="{ORANGE}"/>'
s += f'<rect x="{ox}" y="{oy - L}" width="{L/2}" height="{L/2}" fill="#EED7C0"/><rect x="{ox + L/2}" y="{oy - L/2}" width="{L/2}" height="{L/2}" fill="{SAND}"/><rect x="{ox}" y="{oy - L/2}" width="{L/2}" height="{L/2}" fill="#E4E7EC"/>'
s += t(ox + 3*L/4, oy - 3*L/4 + 12, '플로우', 40, WHITE) + t(ox + L/4, oy - 3*L/4 + 12, '불안', 34) + t(ox + 3*L/4, oy - L/4 + 12, '지루함', 34) + t(ox + L/4, oy - L/4 + 12, '무관심', 34, GRAY)
s += f'<path d="M{ox} {oy} L{ox + L + 40} {oy}" stroke="{NAVY}" stroke-width="4" marker-end="url(#ag)"/><path d="M{ox} {oy} L{ox} {oy - L - 40}" stroke="{NAVY}" stroke-width="4" marker-end="url(#ag)"/>'
s += t(ox + L/2, oy + 60, '기술 (디지털 리터러시)', 28) + f'<text x="{ox - 50}" y="{oy - L/2}" font-size="28" font-weight="700" fill="{NAVY}" text-anchor="middle" transform="rotate(-90 {ox - 50} {oy - L/2})">도전 (과제의 난이도)</text>'
s += f'<circle cx="{ox + L/4}" cy="{oy - L/2 - 55}" r="16" fill="{NAVY}"/><path d="M{ox + L/4 + 22} {oy - L/2 - 55} L{ox + 3*L/4 - 30} {oy - L/2 - 55}" stroke="{NAVY}" stroke-width="5" stroke-dasharray="12 8" marker-end="url(#an2)"/>'
s += t(900, 270, '호텔 체크인은', 34, NAVY, 700, 'start') + t(900, 320, '도전 수준이 높은 과제', 34, NAVY, 700, 'start') + t(900, 375, '예약 조회 · 본인 확인 · 결제 · 객실 키', 24, GRAY, 500, 'start') + t(900, 480, '직관적 화면 · 안내 영상 · 전담 직원', 26, ORANGE, 700, 'start') + t(900, 525, '→ 고객의 기술 수준을 보완해 균형으로', 26, ORANGE, 700, 'start')
imgs['flow-at-the-kiosk'] = frame(s)

# 3) 점검표: 재이용의 조건 / 몰입의 조건
s = t(420, 140, '재이용의 조건', 34) + t(1180, 140, '몰입의 조건', 34, ORANGE)
left = ['기능성', '보안성/개인정보', '디자인성', '확신성']
for i, n in enumerate(left):
    y = 200 + i * 120
    s += f'<rect x="200" y="{y}" width="440" height="90" rx="12" fill="{WHITE}" stroke="{LINE}" stroke-width="3"/><rect x="230" y="{y + 27}" width="36" height="36" rx="6" fill="none" stroke="{NAVY}" stroke-width="4"/><path d="M238 {y + 45} L246 {y + 54} L260 {y + 34}" stroke="{NAVY}" stroke-width="5" fill="none"/>' + t(300, y + 57, n, 30, NAVY, 700, 'start')
right = ['즐거움', '고객화']
for i, n in enumerate(right):
    y = 200 + i * 120
    s += f'<rect x="960" y="{y}" width="440" height="90" rx="12" fill="{ORANGE}"/><rect x="990" y="{y + 27}" width="36" height="36" rx="6" fill="none" stroke="{WHITE}" stroke-width="4"/><path d="M998 {y + 45} L1006 {y + 54} L1020 {y + 34}" stroke="{WHITE}" stroke-width="5" fill="none"/>' + t(1060, y + 57, n, 30, WHITE, 700, 'start')
s += f'<rect x="960" y="460" width="440" height="90" rx="12" fill="{WHITE}" stroke="{ORANGE}" stroke-width="3" stroke-dasharray="10 8"/>' + t(1180, 515, '두 요인 모두 재이용에도 유의', 24, ORANGE, 600)
s += f'<path d="M680 380 L920 380" stroke="{GRAY}" stroke-width="4" marker-end="url(#ag)"/>' + t(800, 360, '결함 없음 다음', 22, GRAY, 500)
s += t(800, 760, '편리성은 두 결과 모두에서 고유 효과가 유의하지 않았다', 24, GRAY, 500)
imgs['hotel-kiosk-quality-checklist'] = frame(s)

# 4) 키오스크 접근성
kx = 640
s = f'<rect x="{kx}" y="180" width="320" height="520" rx="24" fill="{NAVY}"/><rect x="{kx + 30}" y="215" width="260" height="190" rx="10" fill="{CREAM}"/><rect x="{kx + 60}" y="250" width="200" height="20" rx="4" fill="{LINE}"/><rect x="{kx + 60}" y="290" width="140" height="20" rx="4" fill="{LINE}"/><rect x="{kx + 60}" y="340" width="200" height="44" rx="8" fill="{ORANGE}"/>'
s += f'<rect x="{kx + 60}" y="440" width="200" height="120" rx="8" fill="#2E3D52"/><rect x="{kx + 40}" y="700" width="240" height="30" rx="4" fill="{NAVY}"/>'
calls = [(kx - 40, 280, '음성 안내', 'end'), (kx - 40, 500, '화면 높이·휠체어 접근', 'end'), (kx + 360, 280, '안내 영상 모니터', 'start'), (kx + 360, 500, '보조 인력·호출벨', 'start')]
for x, y, lab, a in calls:
    sx = kx if a == 'end' else kx + 320
    s += f'<path d="M{sx} {y - 10} L{x + (10 if a == "end" else -10)} {y - 10}" stroke="{GRAY}" stroke-width="3"/><circle cx="{x}" cy="{y - 10}" r="8" fill="{ORANGE}"/>'
    s += t(x + (-20 if a == 'end' else 20), y, lab, 30, NAVY, 700, a)
s += f'<rect x="590" y="770" width="420" height="64" rx="32" fill="{ORANGE}"/>' + t(800, 812, '2026.1.28 접근성 의무 적용', 26, WHITE)
imgs['kiosk-service-gap-barrier-free'] = frame(s)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg = b.new_page(viewport={'width': 1600, 'height': 900})
    for name, svg in imgs.items():
        pg.set_content(f'<html><body style="margin:0">{svg}</body></html>'); pg.wait_for_timeout(150)
        pg.screenshot(path=f'{OUT}/{name}.png', clip={'x': 0, 'y': 0, 'width': 1600, 'height': 900})
    b.close()
print('done')
