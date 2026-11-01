"""기사 대표 이미지 생성 (1600x900, 3:2로 잘려도 핵심이 보이도록 가운데 1350px 안에 배치)"""
from playwright.sync_api import sync_playwright
import os, sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
NAVY, ORANGE, CREAM, SAND, GRAY, LINE, WHITE = '#1E2A3A', '#C8792D', '#F7F5F0', '#ECE7DD', '#8A96A8', '#D5D9E0', '#FFFFFF'
FONT = "'Noto Sans CJK KR','Noto Sans KR',sans-serif"
SERIF = "'Noto Serif CJK KR','Noto Serif KR',serif"

def frame(inner, bg=CREAM):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" font-family="{FONT}">
<rect width="1600" height="900" fill="{bg}"/>{inner}</svg>'''

def tag(x, y, text, fill=NAVY, color=WHITE):
    w = 26 + len(text) * 15
    return f'<rect x="{x}" y="{y}" width="{w}" height="40" rx="20" fill="{fill}"/><text x="{x + w/2}" y="{y + 27}" font-size="19" font-weight="700" fill="{color}" text-anchor="middle" letter-spacing="1">{text}</text>'

imgs = {}

# 1. SERVQUAL × 시스템 품질 — 두 원의 교집합
imgs['servqual-and-system-quality'] = frame(f'''
<circle cx="680" cy="450" r="250" fill="none" stroke="{NAVY}" stroke-width="10"/>
<circle cx="920" cy="450" r="250" fill="none" stroke="{ORANGE}" stroke-width="10"/>
<clipPath id="c1"><circle cx="680" cy="450" r="250"/></clipPath>
<circle cx="920" cy="450" r="250" fill="{NAVY}" clip-path="url(#c1)"/>
<text x="560" y="440" font-size="42" font-weight="700" fill="{NAVY}" text-anchor="middle">서비스</text>
<text x="560" y="492" font-size="42" font-weight="700" fill="{NAVY}" text-anchor="middle">품질</text>
<text x="1040" y="440" font-size="42" font-weight="700" fill="{ORANGE}" text-anchor="middle">시스템</text>
<text x="1040" y="492" font-size="42" font-weight="700" fill="{ORANGE}" text-anchor="middle">품질</text>
<g fill="{WHITE}"><rect x="770" y="395" width="60" height="42" rx="4"/><rect x="792" y="437" width="16" height="14"/><rect x="778" y="451" width="44" height="6" rx="3"/></g>
<circle cx="800" cy="500" r="16" fill="{ORANGE}"/>
<g font-size="20" fill="{GRAY}" font-weight="500">
<text x="330" y="200">유형성</text><text x="290" y="300">신뢰성</text><text x="270" y="560">응답성</text><text x="300" y="680">확신성</text><text x="390" y="770">공감성</text>
<text x="1180" y="200">기능 적합성</text><text x="1240" y="300">성능 효율성</text><text x="1260" y="560">신뢰성</text><text x="1230" y="680">사용성</text></g>
''')

# 2. 숙박일 경곗값 — 수직선과 경계 표시
def tick(x, label, hi=False):
    c = ORANGE if hi else NAVY
    return f'<line x1="{x}" y1="470" x2="{x}" y2="510" stroke="{c}" stroke-width="5"/><circle cx="{x}" cy="490" r="{16 if hi else 9}" fill="{c}"/><text x="{x}" y="565" font-size="30" font-weight="700" fill="{c}" text-anchor="middle">{label}</text>'
xs = {0: 300, 1: 380, 2: 460, 3: 540, 14: 1180, 15: 1260}
seg = f'''
<rect x="230" y="470" width="110" height="40" fill="{LINE}"/>
<rect x="340" y="470" width="160" height="40" fill="{SAND}"/>
<rect x="500" y="470" width="720" height="40" fill="#E9D3BC"/>
<rect x="1220" y="470" width="150" height="40" fill="{LINE}"/>
<text x="285" y="440" font-size="22" fill="{GRAY}" text-anchor="middle">무효</text>
<text x="420" y="440" font-size="22" fill="{NAVY}" text-anchor="middle">할인 없음</text>
<text x="860" y="440" font-size="22" fill="{ORANGE}" font-weight="700" text-anchor="middle">연박 할인 5%</text>
<text x="1295" y="440" font-size="22" fill="{GRAY}" text-anchor="middle">무효</text>
<text x="860" y="615" font-size="24" fill="{GRAY}" text-anchor="middle">숙박일 (박)</text>'''
bubble = f'''<rect x="610" y="170" width="380" height="130" rx="65" fill="{NAVY}"/><path d="M780 298 L800 345 L830 298 Z" fill="{NAVY}"/>
<text x="800" y="257" font-size="56" font-weight="700" fill="{WHITE}" text-anchor="middle">혹시 14박이면?</text>'''
imgs['service-sense-to-test-design'] = frame(seg + ''.join(tick(x, k, True) for k, x in xs.items()) + bubble + f'<circle cx="620" cy="700" r="14" fill="{ORANGE}"/><text x="648" y="709" font-size="24" fill="{NAVY}">2값 경곗값 분석으로 테스트할 값 6개</text>')

# 3. 703호 — 문 하나, 키 카드 둘
imgs['room-703-error-defect-failure'] = frame(f'''
<rect x="620" y="140" width="360" height="620" rx="8" fill="{NAVY}"/>
<rect x="650" y="170" width="300" height="590" rx="4" fill="#2B3A4F"/>
<rect x="720" y="230" width="160" height="80" rx="8" fill="{CREAM}"/>
<text x="800" y="290" font-family="{SERIF}" font-size="58" font-weight="700" fill="{NAVY}" text-anchor="middle">703</text>
<rect x="895" y="460" width="22" height="90" rx="11" fill="{ORANGE}"/>
<line x1="560" y1="760" x2="1040" y2="760" stroke="{NAVY}" stroke-width="10"/>
<g transform="rotate(-14 420 470)"><rect x="300" y="390" width="230" height="146" rx="14" fill="{WHITE}" stroke="{NAVY}" stroke-width="6"/><rect x="300" y="420" width="230" height="26" fill="{NAVY}"/><text x="330" y="505" font-size="30" font-weight="700" fill="{NAVY}">703</text></g>
<g transform="rotate(12 1180 470)"><rect x="1070" y="390" width="230" height="146" rx="14" fill="{WHITE}" stroke="{ORANGE}" stroke-width="6"/><rect x="1070" y="420" width="230" height="26" fill="{ORANGE}"/><text x="1100" y="505" font-size="30" font-weight="700" fill="{ORANGE}">703</text></g>
<circle cx="800" cy="105" r="0"/>
<g font-size="24" font-weight="700" text-anchor="middle">
<text x="420" y="680" fill="{GRAY}">오류</text><text x="420" y="715" fill="{GRAY}" font-size="18" font-weight="500">Error</text>
<text x="1180" y="680" fill="{ORANGE}">장애</text><text x="1180" y="715" fill="{ORANGE}" font-size="18" font-weight="500">Failure</text></g>
<path d="M480 690 L560 690" stroke="{GRAY}" stroke-width="4" marker-end="url(#a)"/><path d="M1040 690 L1120 690" stroke="{ORANGE}" stroke-width="4" marker-end="url(#b)"/>
<defs><marker id="a" markerWidth="10" markerHeight="10" refX="6" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="{GRAY}"/></marker><marker id="b" markerWidth="10" markerHeight="10" refX="6" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="{ORANGE}"/></marker></defs>
<text x="800" y="830" font-size="22" font-weight="700" fill="{NAVY}" text-anchor="middle">결함 Defect</text>
''')

# 4. 결함 보고서 — 메모 대 보고서
imgs['defect-report-severity-priority'] = frame(f'''
<g transform="rotate(-6 470 470)"><rect x="300" y="300" width="340" height="300" fill="#F3E39B"/>
<text x="330" y="380" font-size="34" fill="{NAVY}" font-weight="500">할인 이상함</text><text x="330" y="440" font-size="34" fill="{NAVY}" font-weight="500">15% 나옴</text><text x="330" y="500" font-size="34" fill="{NAVY}" font-weight="500">확인 바람</text></g>
<path d="M680 460 L790 460" stroke="{GRAY}" stroke-width="8" marker-end="url(#m)"/>
<defs><marker id="m" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{GRAY}"/></marker></defs>
<rect x="830" y="150" width="480" height="610" rx="14" fill="{WHITE}" stroke="{LINE}" stroke-width="3"/>
<text x="870" y="225" font-size="34" font-weight="700" fill="{NAVY}">결함 보고서</text>
<line x1="870" y1="250" x2="1270" y2="250" stroke="{NAVY}" stroke-width="4"/>
<g font-size="22" fill="{GRAY}"><text x="870" y="310">재현 절차</text><text x="870" y="420">기대 결과</text><text x="870" y="510">실제 결과</text><text x="870" y="600">심각도</text><text x="870" y="690">우선순위</text></g>
<g fill="{LINE}"><rect x="1020" y="294" width="250" height="14" rx="7"/><rect x="1020" y="324" width="210" height="14" rx="7"/><rect x="1020" y="354" width="230" height="14" rx="7"/></g>
<text x="1020" y="420" font-size="26" font-weight="700" fill="{NAVY}">270,000원</text>
<text x="1020" y="510" font-size="26" font-weight="700" fill="{ORANGE}">255,000원</text>
<rect x="1020" y="574" width="96" height="40" rx="20" fill="#D9534F"/><text x="1068" y="602" font-size="22" font-weight="700" fill="{WHITE}" text-anchor="middle">높음</text>
<rect x="1020" y="664" width="130" height="40" rx="20" fill="none" stroke="{NAVY}" stroke-width="3"/><text x="1085" y="692" font-size="22" font-weight="700" fill="{NAVY}" text-anchor="middle">별도 판단</text>
''')

# 5. VOC — 말풍선이 막대그래프로 (원고 예시 수치: 16, 13, 12, 7, 2)
bars = [('변경·취소', 16), ('체크인', 13), ('예약', 12), ('정산', 7), ('기타', 2)]
bx = ''
for i, (n, v) in enumerate(bars):
    x = 760 + i * 130; h = v * 26
    c = ORANGE if n in ('변경·취소', '정산') else NAVY
    bx += f'<rect x="{x}" y="{720 - h}" width="84" height="{h}" fill="{c}"/><text x="{x + 42}" y="{705 - h}" font-size="24" font-weight="700" fill="{c}" text-anchor="middle">{v}</text><text x="{x + 42}" y="760" font-size="21" fill="{NAVY}" text-anchor="middle">{n}</text>'
bub = ''
for (x, y, w) in [(260, 220, 220), (330, 380, 260), (230, 540, 200), (410, 640, 180)]:
    bub += f'<rect x="{x}" y="{y}" width="{w}" height="90" rx="45" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/><g fill="{LINE}"><rect x="{x + 34}" y="{y + 30}" width="{w - 68}" height="10" rx="5"/><rect x="{x + 34}" y="{y + 52}" width="{(w - 68) * 0.6}" height="10" rx="5"/></g>'
imgs['voc-to-test-priority'] = frame(bub + f'<path d="M560 450 L680 450" stroke="{GRAY}" stroke-width="8" marker-end="url(#v)"/><defs><marker id="v" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{GRAY}"/></marker></defs><line x1="740" y1="720" x2="1400" y2="720" stroke="{NAVY}" stroke-width="5"/>' + bx + f'<text x="1080" y="180" font-size="30" font-weight="700" fill="{NAVY}" text-anchor="middle">VOC 50건 기능별 분포</text>')

# 6. 고객 데이터와 AI — 가린 정보 카드, 자물쇠, AI 칩
imgs['hotel-data-ai-agent'] = frame(f'''
<rect x="250" y="230" width="430" height="440" rx="18" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/>
<circle cx="340" cy="320" r="44" fill="{SAND}"/><circle cx="340" cy="306" r="16" fill="{GRAY}"/><path d="M312 346 Q340 322 368 346" fill="{GRAY}"/>
<text x="410" y="312" font-size="32" font-weight="700" fill="{NAVY}">고객A</text><text x="410" y="348" font-size="22" fill="{GRAY}">객실X 예약 취소</text>
<g font-size="24" fill="{NAVY}"><text x="290" y="440">연락처</text><text x="290" y="510">카드</text><text x="290" y="580">이메일</text></g>
<g fill="{NAVY}"><rect x="420" y="418" width="210" height="30" rx="4"/><rect x="420" y="488" width="210" height="30" rx="4"/><rect x="420" y="558" width="210" height="30" rx="4"/></g>
<rect x="745" y="420" width="110" height="94" rx="14" fill="{ORANGE}"/><path d="M770 420 V385 A30 30 0 0 1 830 385 V420" fill="none" stroke="{ORANGE}" stroke-width="14"/><circle cx="800" cy="460" r="12" fill="{WHITE}"/><rect x="795" y="462" width="10" height="26" fill="{WHITE}"/>
<path d="M720 600 L880 600" stroke="{GRAY}" stroke-width="8" marker-end="url(#d)"/><defs><marker id="d" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{GRAY}"/></marker></defs>
<rect x="960" y="300" width="300" height="300" rx="28" fill="{NAVY}"/>
<g stroke="{NAVY}" stroke-width="10">{''.join(f'<line x1="{1000 + i*55}" y1="270" x2="{1000 + i*55}" y2="300"/><line x1="{1000 + i*55}" y1="600" x2="{1000 + i*55}" y2="630"/><line x1="930" y1="{340 + i*55}" x2="960" y2="{340 + i*55}"/><line x1="1260" y1="{340 + i*55}" x2="1290" y2="{340 + i*55}"/>' for i in range(5))}</g>
<text x="1110" y="475" font-size="96" font-weight="700" fill="{WHITE}" text-anchor="middle">AI</text>
<rect x="1035" y="505" width="150" height="40" rx="20" fill="{ORANGE}"/><text x="1110" y="533" font-size="22" font-weight="700" fill="{WHITE}" text-anchor="middle">초안 → 검증</text>
''')

# 7. 호텔리어에서 도메인 QA로 — 벨에서 체크리스트로 이어지는 길
imgs['hotelier-to-domain-qa'] = frame(f'''
<path d="M420 600 C 620 600, 620 330, 820 330 S 1040 560, 1180 560" fill="none" stroke="{GRAY}" stroke-width="8" stroke-dasharray="4 22" stroke-linecap="round"/>
<g transform="translate(420 600)"><ellipse cx="0" cy="40" rx="150" ry="22" fill="{NAVY}"/><path d="M-110 30 A110 110 0 0 1 110 30 Z" fill="{ORANGE}"/><rect x="-14" y="-102" width="28" height="22" rx="6" fill="{NAVY}"/></g>
<text x="420" y="740" font-size="30" font-weight="700" fill="{NAVY}" text-anchor="middle">프런트 데스크</text>
<g transform="translate(1180 560)"><rect x="-150" y="-260" width="300" height="380" rx="16" fill="{WHITE}" stroke="{NAVY}" stroke-width="6"/><rect x="-60" y="-284" width="120" height="44" rx="10" fill="{NAVY}"/>
{''.join(f'<rect x="-110" y="{-190 + i*80}" width="40" height="40" rx="6" fill="none" stroke="{NAVY}" stroke-width="5"/><path d="M-102 {-170 + i*80} l10 12 l20 -24" fill="none" stroke="{ORANGE}" stroke-width="7" stroke-linecap="round"/><rect x="-50" y="{-178 + i*80}" width="{150 - i*25}" height="16" rx="8" fill="{LINE}"/>' for i in range(4))}</g>
<text x="1180" y="740" font-size="30" font-weight="700" fill="{NAVY}" text-anchor="middle">도메인 QA</text>
<circle cx="820" cy="330" r="34" fill="{NAVY}"/><text x="820" y="342" font-size="30" font-weight="700" fill="{WHITE}" text-anchor="middle">?</text>
''')

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg = b.new_page(viewport={'width': 1600, 'height': 900})
    for name, svg in imgs.items():
        pg.set_content(f'<html><body style="margin:0">{svg}</body></html>')
        pg.wait_for_timeout(150)
        pg.screenshot(path=f'{OUT}/{name}.png', clip={'x': 0, 'y': 0, 'width': 1600, 'height': 900})
    b.close()
print('done', len(imgs))
