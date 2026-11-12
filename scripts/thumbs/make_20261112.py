"""목요일 기사 3편 대표 이미지(1600x900) 원본 생성 (2026-11-12)
사용법: python3 scripts/thumbs/make_20261112.py
결과: scripts/thumbs/originals/<슬러그>.jpg (로고 없음) → watermark.py로 최종 이미지 생성
영어판은 make_en_20261112.py가 이 파일의 build('en')을 호출해 같은 도식에 영어 글자만 바꿔 만든다.
오른쪽 아래(가로 1080~1475, 세로 815 아래)는 로고 자리로 비워 둔다. 수치는 본문에 나온 숫자만 쓴다.
"""
from playwright.sync_api import sync_playwright
from PIL import Image
import os, io
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NAVY, ORANGE, CREAM, SAND, GRAY, LINE, WHITE = '#1E2A3A', '#C8792D', '#F7F5F0', '#ECE7DD', '#8A96A8', '#D5D9E0', '#FFFFFF'
FONTS = {'ko': "'Noto Sans CJK KR','Noto Sans KR',sans-serif", 'en': "'Noto Sans','Noto Sans CJK KR',sans-serif"}
DEFS = f'<defs><marker id="ag" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{GRAY}"/></marker><marker id="ao" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{ORANGE}"/></marker></defs>'
def t(x, y, s, size=26, fill=NAVY, w=700, a='middle'): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{s}</text>'
def box(x, y, w, h, fill=WHITE, stroke=LINE, sw=3, r=14): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

TXT = {
 'ko': dict(
  a_title='방한 외국인 관광객, 14년 만에 두 배', a_sub='연간 방한객 · 문화체육관광부 발표 보도 기준 (2026년은 11월 12일 추정 돌파, 연말은 전망)',
  a_bars=[('2012', 1000, '1,000만'), ('2019', 1750, '1,750만'), ('2024', 1637, '1,637만'), ('2025', 1894, '1,894만'), ('2026.11.12', 2000, '2,000만 돌파'), ('2026 연말', 2300, '2,300만 전망')],
  a_note1='비수도권 공항 입국 324만 명 · 전체의 19.0% · +37.4% (1~9월)', a_foot='다음 목표 3,000만 명, 숫자 다음은 수용 품질',
  b_title='방한 소비, 피부과와 약국으로', b_sub='2026년 1~9월 방한 외국인 카드 소비 · 전년 같은 기간 대비 (보도 기준)',
  b_bars=[('의료 소비액', 57.9, '1조 8,398억 원'), ('의료 결제 건수', 69.0, '442만 건'), ('약국 결제액', 196.1, '')],
  b_card='의료 소비 중 비중', b_rows=[('피부과', '53.72%', '55.72%'), ('약국', '6.66%', '12.49%')], b_yr=('2025', '2026'),
  b_foot='시술과 회복에 맞춰 짜는 일정, 호텔의 체류 서비스도 바뀐다',
  c_title='객실 밖으로 나간 호텔 브랜드', c_sub='국내 특급호텔 자체 브랜드(PB) 상품 · 2026년 보도 사례',
  c_hub=('호텔', '브랜드'),
  c_nodes=[('김치', '조선호텔 김치', '2025년 매출 540억 원'), ('침구', '워커힐 홈쇼핑 방송', '약 40분, 약 1,000세트'), ('판매 채널', '온라인몰에서', 'TV홈쇼핑·백화점·편의점'), ('해외', '워커힐 김치 수출', '누적 82t (9월 기준)')],
  c_foot='호텔 밖에서 팔리는 상품도 고객에게는 호텔의 약속이다'),
 'en': dict(
  a_title='Foreign visitors to Korea doubled in 14 years', a_sub='Annual arrivals, as reported from the Ministry of Culture, Sports and Tourism (2026: estimated on 12 Nov; year-end is a forecast)',
  a_bars=[('2012', 1000, '10M'), ('2019', 1750, '17.5M'), ('2024', 1637, '16.37M'), ('2025', 1894, '18.94M'), ('12 Nov 2026', 2000, '20M passed'), ('End of 2026', 2300, '23M forecast')],
  a_note1='Arrivals via non-capital airports: 3.24M · 19.0% of total · +37.4% (Jan–Sep)', a_foot='Next target 30 million: after the numbers comes quality',
  b_title='Visitor spending moves to dermatology and pharmacies', b_sub='Foreign visitors’ card spending, Jan–Sep 2026 vs same period 2025 (as reported)',
  b_bars=[('Medical spending', 57.9, 'KRW 1.84 trillion'), ('Medical transactions', 69.0, '4.43 million'), ('Pharmacy spending', 196.1, '')],
  b_card='Share of medical spending', b_rows=[('Dermatology', '53.72%', '55.72%'), ('Pharmacy', '6.66%', '12.49%')], b_yr=('2025', '2026'),
  b_foot='Itineraries built around treatment and recovery change hotel stays too',
  c_title='Hotel brands beyond the guest room', c_sub='Private-brand (PB) products of Korean luxury hotels, cases reported in 2026',
  c_hub=('Hotel', 'brand'),
  c_nodes=[('Kimchi', 'Josun Hotel kimchi', '2025 sales KRW 54 billion'), ('Bedding', 'Walkerhill home shopping', '~1,000 sets in ~40 min'), ('Channels', 'From own online malls to', 'TV shopping, stores, shops'), ('Overseas', 'Walkerhill kimchi exports', '82 t cumulative (Sep)')],
  c_foot='Products sold outside the hotel are still the hotel’s promise'),
}

def build(lang='ko'):
    L = TXT[lang]
    def frame(inner): return f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" font-family="{FONTS[lang]}"><rect width="1600" height="900" fill="{CREAM}"/>{DEFS}{inner}</svg>'
    imgs = {}
    # 1) 연도별 방한객 세로 막대 (2026 돌파는 주황, 연말 전망은 점선)
    s = t(800, 100, L['a_title'], 38) + t(800, 145, L['a_sub'], 20 if lang == 'en' else 21, GRAY, 500)
    base, sc = 640, 0.17
    s += f'<line x1="170" y1="{base}" x2="1430" y2="{base}" stroke="{NAVY}" stroke-width="3"/>'
    for i, (yr, v, lab) in enumerate(L['a_bars']):
        cx = 265 + i * 214
        h = v * sc
        if i == 5:
            s += f'<rect x="{cx - 65}" y="{base - h:.0f}" width="130" height="{h:.0f}" rx="8" fill="none" stroke="{ORANGE}" stroke-width="4" stroke-dasharray="10 8"/>'
            col = ORANGE
        else:
            col = ORANGE if i == 4 else (NAVY if i == 0 else GRAY)
            s += f'<rect x="{cx - 65}" y="{base - h:.0f}" width="130" height="{h:.0f}" rx="8" fill="{col}"/>'
        s += t(cx, f'{base - h - 18:.0f}', lab, 26 if lang == 'ko' else 23, ORANGE if i >= 4 else NAVY, 800)
        s += t(cx, base + 38, yr, 22, NAVY, 700)
    s += box(250, 702, 1100, 56, WHITE, LINE, 2, 12) + t(800, 739, L['a_note1'], 23, NAVY, 700)
    s += t(800, 800, L['a_foot'], 25, ORANGE, 800)
    imgs['inbound-20-million-policy-2026'] = frame(s)

    # 2) 증가율 가로 막대 + 비중 변화 카드
    s = t(800, 100, L['b_title'], 38 if lang == 'ko' else 34) + t(800, 145, L['b_sub'], 21, GRAY, 500)
    x0 = 150
    for i, (lab, v, sub) in enumerate(L['b_bars']):
        y = 225 + i * 170
        w = v * 3.0
        col = ORANGE if i == 2 else NAVY
        s += t(x0, y + 4, lab, 26, NAVY, 700, 'start')
        s += f'<rect x="{x0}" y="{y + 22}" width="{w:.0f}" height="58" rx="8" fill="{col}"/>'
        s += t(f'{x0 + w + 16:.0f}', y + 64, f'+{v}%', 32, col, 800, 'start')
        if sub:  # 보조 수치는 막대 아래 작은 글씨로
            s += t(x0, y + 112, sub, 20, GRAY, 600, 'start')
    s += box(950, 205, 500, 470, WHITE, LINE, 3)
    s += t(1200, 260, L['b_card'], 27)
    s += t(1222, 310, L['b_yr'][0], 21, GRAY, 700) + t(1385, 310, L['b_yr'][1], 21, ORANGE, 800)
    for i, (lab, a, b) in enumerate(L['b_rows']):
        y = 335 + i * 160
        s += t(980, y + 50, lab, 26, NAVY, 800, 'start')
        s += t(1222, y + 50, a, 26, GRAY, 700) + t(1385, y + 50, b, 28, ORANGE, 800)
        s += f'<path d="M1284 {y + 41} L1296 {y + 41}" stroke="{GRAY}" stroke-width="3" marker-end="url(#ag)"/>'
        s += f'<line x1="980" y1="{y + 100}" x2="1420" y2="{y + 100}" stroke="{LINE}" stroke-width="2"/>' if i == 0 else ''
    s += t(800, 790, L['b_foot'], 25)
    imgs['inbound-medical-beauty-spending-2026'] = frame(s)

    # 3) 허브형: 호텔 브랜드에서 네 갈래
    s = t(800, 100, L['c_title'], 38) + t(800, 145, L['c_sub'], 21, GRAY, 500)
    hx, hy = 800, 450
    pos = [(400, 300), (1200, 300), (400, 610), (1200, 610)]
    for (nx, ny) in pos:
        ex = nx + (190 if nx < hx else -190)
        s += f'<line x1="{hx}" y1="{hy}" x2="{ex}" y2="{ny}" stroke="{LINE}" stroke-width="5"/>'
    s += f'<circle cx="{hx}" cy="{hy}" r="118" fill="{NAVY}"/>'
    s += t(hx, hy - 6, L['c_hub'][0], 34, WHITE, 800) + t(hx, hy + 38, L['c_hub'][1], 30, WHITE, 700)
    for i, ((nx, ny), (head, a, b)) in enumerate(zip(pos, L['c_nodes'])):
        col = ORANGE if i in (0, 3) else NAVY
        s += box(nx - 205, ny - 85, 410, 170, WHITE, col, 4)
        s += t(nx, ny - 30, head, 30, col, 800) + t(nx, ny + 15, a, 22, NAVY, 700) + t(nx, ny + 52, b, 22, GRAY, 700)
    s += t(800, 790, L['c_foot'], 25)
    imgs['hotel-pb-beyond-rooms-2026'] = frame(s)
    return imgs

def render(imgs, out):
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = b.new_page(viewport={'width': 1600, 'height': 900})
        for slug, svg in imgs.items():
            pg.set_content(f'<html><body style="margin:0">{svg}</body></html>')
            pg.wait_for_timeout(150)
            png = pg.screenshot(clip={'x': 0, 'y': 0, 'width': 1600, 'height': 900})
            Image.open(io.BytesIO(png)).convert('RGB').save(os.path.join(out, slug + '.jpg'), quality=88)
            print('ok', slug)
        b.close()

if __name__ == '__main__':
    render(build('ko'), os.path.join(ROOT, 'scripts', 'thumbs', 'originals'))
