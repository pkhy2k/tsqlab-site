"""리포트·칼럼 대표 이미지(1600x900)와 리포트 표지(600x800) 생성
사용법: python3 scripts/thumbs/make2.py <출력 폴더>
"""
from playwright.sync_api import sync_playwright
import os, sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
NAVY, ORANGE, CREAM, SAND, GRAY, LINE, WHITE, RED = '#1E2A3A', '#C8792D', '#F7F5F0', '#ECE7DD', '#8A96A8', '#D5D9E0', '#FFFFFF', '#D9534F'
FONT = "'Noto Sans CJK KR','Noto Sans KR',sans-serif"
SERIF = "'Noto Serif CJK KR','Noto Serif KR',serif"
ARROW = f'<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{GRAY}"/></marker></defs>'

def frame(inner, bg=CREAM, w=1600, h=900):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}"><rect width="{w}" height="{h}" fill="{bg}"/>{ARROW}{inner}</svg>'

LOGO = lambda x, y, s, ink, org: f'<g transform="translate({x} {y}) scale({s})"><path d="M50 347 V160 A140 140 0 0 1 330 160 V347" fill="none" stroke="{ink}" stroke-width="16"/><rect x="7" y="348" width="366" height="16" fill="{ink}"/><rect x="103" y="262" width="47" height="86" fill="{ink}"/><rect x="167" y="215" width="47" height="133" fill="{ink}"/><rect x="230" y="159" width="47" height="189" fill="{org}"/></g>'

imgs = {}

# R1 예약 변경·취소 사례: 위약금 구간과 D=6 결함
bands = [(-1, -1, LINE, '노쇼'), (0, 2, '#E3B48A', '100%'), (3, 6, '#EED7C0', '50%'), (7, 9, SAND, '무료')]
X = lambda d: 300 + (9 - d) * 100  # 왼쪽이 먼 날짜(D 큼)
r1 = ''
for a, b, c, lab in bands:
    x0, x1 = X(b) - 50, X(a) + 50
    r1 += f'<rect x="{x0}" y="400" width="{x1 - x0}" height="70" fill="{c}"/><text x="{(x0 + x1) / 2}" y="447" font-size="28" font-weight="700" fill="{NAVY}" text-anchor="middle">{lab}</text>'
for d in [7, 6, 3, 2, 0, -1]:
    hi = d == 6
    r1 += f'<circle cx="{X(d)}" cy="520" r="{18 if hi else 11}" fill="{RED if hi else ORANGE}"/><text x="{X(d)}" y="580" font-size="28" font-weight="700" fill="{RED if hi else NAVY}" text-anchor="middle">{d}</text>'
r1 += f'<text x="{X(4)}" y="640" font-size="24" fill="{GRAY}" text-anchor="middle">D = 체크인 날짜 − 취소일 (일)</text>'
r1 += f'<g transform="translate({X(6)} 270)"><rect x="-190" y="-70" width="380" height="110" rx="16" fill="{WHITE}" stroke="{RED}" stroke-width="5"/><text x="0" y="-22" font-size="26" font-weight="700" fill="{RED}" text-anchor="middle">D=6 취소 → 위약금 0원</text><text x="0" y="16" font-size="22" fill="{NAVY}" text-anchor="middle">기대 결과: 50,000원 (50%)</text><path d="M0 40 L0 112" stroke="{RED}" stroke-width="4"/></g>'
r1 += f'<text x="800" y="790" font-size="26" font-weight="700" fill="{NAVY}" text-anchor="middle">경곗값 7 · 6 · 3 · 2 · 0 · −1</text>'
imgs['report-cancellation-qa-case'] = frame(r1)

# R2 리스크 기반 테스트: 3x3 히트맵
cell, gx, gy = 150, 600, 170
heat = {9: '#C8792D', 6: '#DDA472', 4: '#EBCBAA', 3: '#F1DDC8', 2: '#F4E7DA', 1: '#F7F0E8'}
r2 = ''
for li in range(1, 4):
    for im in range(1, 4):
        x = gx + (im - 1) * cell; y = gy + (3 - li) * cell
        r2 += f'<rect x="{x}" y="{y}" width="{cell - 6}" height="{cell - 6}" rx="8" fill="{heat[li * im]}"/>'
pts = [(3, 3, '금액 오계산'), (2, 3, '부분 환불'), (2, 3, '중복 결제'), (2, 2, '마감 합계'), (2, 1, '영수증')]
off = {}
for li, im, lab in pts:
    k = (li, im); n = off.get(k, 0); off[k] = n + 1
    cx = gx + (im - 1) * cell + 72 + (n * 34 - (17 if k == (2, 3) else 0))
    cy = gy + (3 - li) * cell + 72
    r2 += f'<circle cx="{cx}" cy="{cy}" r="15" fill="{NAVY}" stroke="{WHITE}" stroke-width="3"/>'
r2 += f'<text x="{gx + 2*cell + 72}" y="{gy + 115}" font-size="22" font-weight="700" fill="{WHITE}" text-anchor="middle">9</text>'
r2 += f'<text x="{gx + 222}" y="{gy + 3*cell + 50}" font-size="24" font-weight="700" fill="{NAVY}" text-anchor="middle">영향 →</text><text x="{gx - 40}" y="{gy + 222}" font-size="24" font-weight="700" fill="{NAVY}" text-anchor="middle" transform="rotate(-90 {gx - 40} {gy + 222})">가능성 →</text>'
r2 += f'<g font-size="24" fill="{NAVY}"><text x="1130" y="300" font-weight="700">리스크 수준</text><text x="1130" y="345">= 가능성 × 영향</text><text x="1130" y="420" fill="{ORANGE}" font-weight="700">9  금액 오계산</text><text x="1130" y="460">6  부분 환불 · 중복 결제</text><text x="1130" y="500">4  마감 합계</text><text x="1130" y="540">2  영수증 레이아웃</text></g>'
r2 += f'<g font-size="22" fill="{GRAY}"><text x="330" y="330">무엇부터,</text><text x="330" y="365">얼마나 깊게?</text></g>'
imgs['report-risk-based-testing-hotel'] = frame(r2)

# R3 AI 에이전트 업무 흐름: 단계별 AI/사람 역할
steps = ['요구사항', '계획', '설계', '실행·결함', '완료']
r3 = f'<text x="190" y="388" font-size="30" font-weight="700" fill="{ORANGE}" text-anchor="middle">AI</text><text x="190" y="418" font-size="20" fill="{GRAY}" text-anchor="middle">작성·정리</text><text x="190" y="588" font-size="30" font-weight="700" fill="{NAVY}" text-anchor="middle">사람</text><text x="190" y="618" font-size="20" fill="{GRAY}" text-anchor="middle">선택·판단·책임</text>'
for i, s in enumerate(steps):
    x = 290 + i * 250
    r3 += f'<rect x="{x}" y="210" width="210" height="80" rx="40" fill="{NAVY}"/><text x="{x + 105}" y="260" font-size="28" font-weight="700" fill="{WHITE}" text-anchor="middle">{s}</text>'
    r3 += f'<rect x="{x + 20}" y="340" width="170" height="100" rx="14" fill="{WHITE}" stroke="{ORANGE}" stroke-width="5"/><g fill="#F1DDC8"><rect x="{x + 45}" y="370" width="120" height="12" rx="6"/><rect x="{x + 45}" y="398" width="90" height="12" rx="6"/></g>'
    r3 += f'<rect x="{x + 20}" y="540" width="170" height="100" rx="14" fill="{NAVY}"/><path d="M{x + 80} 592 l18 20 l36 -42" fill="none" stroke="{ORANGE}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
    r3 += f'<path d="M{x + 105} 445 L{x + 105} 530" stroke="{GRAY}" stroke-width="5" stroke-dasharray="6 8" marker-end="url(#ar)"/>'
    if i < 4: r3 += f'<path d="M{x + 215} 250 L{x + 240} 250" stroke="{GRAY}" stroke-width="5" marker-end="url(#ar)"/>'
r3 += f'<text x="800" y="740" font-size="28" font-weight="700" fill="{NAVY}" text-anchor="middle">AI가 만든 것은 초안, 판단은 사람이</text>'
imgs['report-ai-agent-qa-workflow'] = frame(r3)

# C1 키오스크와 프런트 매니저
c1 = f'''<g transform="translate(560 160)"><rect x="0" y="0" width="240" height="420" rx="24" fill="{NAVY}"/><rect x="26" y="34" width="188" height="230" rx="10" fill="#2E405A"/>
<rect x="50" y="64" width="140" height="18" rx="9" fill="{CREAM}"/><rect x="50" y="98" width="100" height="14" rx="7" fill="{GRAY}"/><rect x="50" y="180" width="140" height="50" rx="10" fill="{ORANGE}"/>
<text x="120" y="214" font-size="22" font-weight="700" fill="{WHITE}" text-anchor="middle">체크인</text><rect x="70" y="300" width="100" height="14" rx="7" fill="#2E405A"/><rect x="40" y="420" width="160" height="150" fill="{NAVY}"/><rect x="0" y="570" width="240" height="20" rx="6" fill="{NAVY}"/></g>
<g transform="translate(990 300)"><circle cx="0" cy="0" r="70" fill="{SAND}"/><circle cx="0" cy="-12" r="30" fill="{GRAY}"/><path d="M-50 50 Q0 6 50 50" fill="{GRAY}"/>
<rect x="-110" y="110" width="220" height="150" rx="16" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/>{''.join(f'<rect x="-80" y="{140 + i*36}" width="26" height="26" rx="4" fill="none" stroke="{NAVY}" stroke-width="4"/><path d="M-75 {153 + i*36} l7 8 l14 -16" fill="none" stroke="{ORANGE}" stroke-width="5" stroke-linecap="round"/><rect x="-40" y="{146 + i*36}" width="{110 - i*20}" height="12" rx="6" fill="{LINE}"/>' for i in range(3))}</g>
<path d="M830 360 C 880 300, 900 300, 920 300" fill="none" stroke="{GRAY}" stroke-width="6" stroke-dasharray="4 14" stroke-linecap="round"/>
<circle cx="880" cy="230" r="34" fill="{ORANGE}"/><text x="880" y="243" font-size="34" font-weight="700" fill="{WHITE}" text-anchor="middle">?</text>
<text x="800" y="830" font-size="26" font-weight="700" fill="{NAVY}" text-anchor="middle">대체될 것인가, 품질을 지킬 것인가</text>'''
imgs['column-kiosk-and-front-manager'] = frame(c1)

# C2 테스트는 질문이다
qs = [('이 값들은 같은 대접을 받을까?', 360, 250), ('이 조건들이 겹치면?', 360, 470), ('무엇이 가장 아플까?', 360, 690),
      ('딱 경계에서는?', 1240, 250), ('지금 이 상태에서 이걸 하면?', 1240, 470), ('정말?', 1240, 690)]
c2 = f'<text x="800" y="600" font-family="{SERIF}" font-size="440" font-weight="700" fill="{NAVY}" text-anchor="middle">?</text>'
for t, x, y in qs:
    w = 44 + len(t) * 25; hi = t == '정말?'
    c2 += f'<rect x="{x - w/2}" y="{y - 40}" width="{w}" height="64" rx="32" fill="{ORANGE if hi else WHITE}" stroke="{ORANGE if hi else NAVY}" stroke-width="4"/><text x="{x}" y="{y + 2}" font-size="25" font-weight="700" fill="{WHITE if hi else NAVY}" text-anchor="middle">{t}</text>'
imgs['column-testing-is-asking'] = frame(c2)

# C3 하우스키핑 점검표와 7원칙
c3 = f'''<g transform="translate(330 330)"><rect x="0" y="120" width="420" height="120" rx="14" fill="{NAVY}"/><rect x="0" y="40" width="130" height="100" rx="14" fill="{NAVY}"/><rect x="20" y="70" width="90" height="50" rx="12" fill="{WHITE}"/>
<rect x="130" y="95" width="290" height="60" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/><rect x="230" y="95" width="190" height="60" fill="{SAND}"/><rect x="10" y="240" width="20" height="50" fill="{NAVY}"/><rect x="390" y="240" width="20" height="50" fill="{NAVY}"/></g>
<g transform="translate(900 150)"><rect x="0" y="0" width="380" height="580" rx="18" fill="{WHITE}" stroke="{NAVY}" stroke-width="6"/><rect x="120" y="-24" width="140" height="48" rx="10" fill="{NAVY}"/>
{''.join(f'<circle cx="54" cy="{80 + i*72}" r="22" fill="{ORANGE if i == 6 else NAVY}"/><text x="54" y="{89 + i*72}" font-size="24" font-weight="700" fill="{WHITE}" text-anchor="middle">{i+1}</text><rect x="96" y="{72 + i*72}" width="{230 - (i % 3) * 30}" height="16" rx="8" fill="{LINE}"/>' for i in range(7))}</g>
<text x="540" y="740" font-size="28" font-weight="700" fill="{NAVY}" text-anchor="middle">객실 점검과 소프트웨어 테스트</text>'''
imgs['column-housekeeping-seven-principles'] = frame(c3)

# 리포트 표지 (600x800)
covers = {
    'report-cancellation-qa-case': ('01', ['호텔 예약 변경·취소', '기능 QA 사례 분석']),
    'report-risk-based-testing-hotel': ('02', ['호텔 시스템의', '리스크 기반 테스트']),
    'report-ai-agent-qa-workflow': ('03', ['AI 에이전트와 함께하는', 'QA 업무 가이드']),
}
cov = {}
for k, (no, lines) in covers.items():
    t = ''.join(f'<text x="56" y="{330 + i*62}" font-family="{SERIF}" font-size="44" font-weight="700" fill="{WHITE}">{l}</text>' for i, l in enumerate(lines))
    cov[k] = frame(f'''<rect x="0" y="0" width="600" height="800" fill="{NAVY}"/><rect x="56" y="120" width="60" height="8" fill="{ORANGE}"/>
<text x="56" y="180" font-size="24" font-weight="700" fill="#C9D1DC" letter-spacing="6">REPORT {no}</text>{t}
<line x1="56" y1="620" x2="544" y2="620" stroke="#3A4A62" stroke-width="2"/>{LOGO(56, 650, 0.2, WHITE, ORANGE)}
<text x="140" y="702" font-family="{SERIF}" font-size="24" font-weight="700" fill="{WHITE}">관광서비스품질연구소</text>''', bg=NAVY, w=600, h=800)

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
print('done', len(imgs), len(cov))
