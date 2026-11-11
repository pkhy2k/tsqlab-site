"""월요일 기사 4편 대표 이미지(1600x900) 원본 생성 (2026-11-09)
사용법: python3 scripts/thumbs/make_20261109.py
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
DEFS = f'<defs><marker id="ag" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{GRAY}"/></marker><marker id="an" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{NAVY}"/></marker></defs>'
def frame(inner): return f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" font-family="{FONT}"><rect width="1600" height="900" fill="{CREAM}"/>{DEFS}{inner}</svg>'
def t(x, y, s, size=26, fill=NAVY, w=700, a='middle'): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{s}</text>'
def box(x, y, w, h, fill=WHITE, stroke=LINE, sw=3, r=14): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
imgs = {}

# 1) 관광발전지수: 상위 지표와 하위 지표 순위 (점 그래프, 1위가 왼쪽)
s = t(800, 100, '관광발전지수 12위, 지표별 순위는 엇갈렸다', 36)
s += t(800, 145, '세계경제포럼 관광발전지수 · 110개국 중 순위 (2026년 10월 문화체육관광부 발표 보도 기준)', 21, GRAY, 500)
x0, x1 = 560, 1440
def xr(r): return x0 + (r - 1) / 109 * (x1 - x0)
s += f'<line x1="{x0}" y1="215" x2="{x1}" y2="215" stroke="{LINE}" stroke-width="3"/>'
for r in (1, 25, 50, 75, 110):
    s += f'<line x1="{xr(r):.0f}" y1="207" x2="{xr(r):.0f}" y2="223" stroke="{GRAY}" stroke-width="2"/>' + t(f'{xr(r):.0f}', 197, f'{r}위', 18, GRAY, 600)
rows = [('ICT 준비도', 1, NAVY), ('계절 편중 완화', 4, NAVY), ('종합 순위', 12, NAVY), ('환대 평판 지수', 65, ORANGE), ('호텔 객실 수(인구 대비)', 69, ORANGE), ('숙박·음식업 노동생산성', 69, ORANGE), ('정부 예산 중 관광 비중', 76, ORANGE)]
for i, (lab, r, c) in enumerate(rows):
    y = 270 + i * 72
    s += t(530, y + 9, lab, 24, NAVY, 700, 'end')
    s += f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{LINE}" stroke-width="2" stroke-dasharray="4 6"/>'
    s += f'<line x1="{x0}" y1="{y}" x2="{xr(r):.0f}" y2="{y}" stroke="{c}" stroke-width="6"/>'
    s += f'<circle cx="{xr(r):.0f}" cy="{y}" r="14" fill="{c}"/>' + t(f'{xr(r) + 26:.0f}', y + 9, f'{r}위', 24, c, 800, 'start')
s += t(800, 790, '기반 시설은 상위권, 현장에서 체감하는 환대와 숙박은 하위권', 25)
imgs['ttdi-hospitality-reputation-2026'] = frame(s)

# 2) 호텔 체인 AI: 91% → 28% → 13% 깔때기
s = t(800, 100, '호텔 체인의 AI, 도입과 성과 사이', 36)
s += t(800, 145, 'h2c AI Opportunity Study 2026 · 호텔 체인 113곳 조사', 21, GRAY, 500)
fun = [('AI를 이미 사용', '91%', 1000, NAVY), ('전사 AI 전략 보유', '28%', 720, NAVY), ('측정 가능한 투자 수익 보고', '13%', 460, ORANGE)]
for i, (lab, v, w, c) in enumerate(fun):
    y = 205 + i * 165
    x = 800 - w / 2
    s += f'<rect x="{x:.0f}" y="{y}" width="{w}" height="130" rx="16" fill="{c}"/>'
    s += t(800, y + 62, v, 54, WHITE, 800) + t(800, y + 105, lab, 24, WHITE, 600)
s += t(800, 735, '주요 장애: 기술·교육 부족 56% · 시스템 연동 38% · 전략 부재 32% · 데이터 거버넌스 28%', 24, NAVY, 700)
s += t(800, 780, '사용의 60%는 외부 범용 도구, 핵심 시스템과 연결된 AI는 아직 적다', 22, GRAY, 600)
imgs['hotel-chain-ai-readiness-2026'] = frame(s)

# 3) 메리어트와 힐튼 지역별 RevPAR 증감 (묶음 막대, 0 기준선)
s = t(800, 100, '같은 분기, 다른 아시아', 36)
s += t(800, 145, '2026년 3분기 객실당 매출(RevPAR) 전년 대비 증감률 · 회사 발표 기준', 21, GRAY, 500)
zero, sc = 560, 26  # 1%p = 26px
s += f'<line x1="200" y1="{zero}" x2="1400" y2="{zero}" stroke="{GRAY}" stroke-width="3"/>' + t(185, zero + 8, '0%', 20, GRAY, 600, 'end')
groups = [('전 세계', 6.5, 5.8), ('미국(·캐나다)', 7.4, 7.0), ('아시아태평양', 9.0, -0.5)]
for i, (lab, m, h) in enumerate(groups):
    cx = 360 + i * 400
    for j, (v, c) in enumerate([(m, ORANGE), (h, NAVY)]):
        x = cx - 90 + j * 100
        hgt = abs(v) * sc
        y = zero - hgt if v >= 0 else zero
        s += f'<rect x="{x}" y="{y:.0f}" width="80" height="{hgt:.0f}" rx="6" fill="{c}"/>'
        txt = '+9% 이상' if (i == 2 and j == 0) else ('+' if v > 0 else '−') + f'{abs(v):.1f}%'
        ty = y - 14 if v >= 0 else y + hgt + 34
        s += t(x + 40, f'{ty:.0f}', txt, 24, c, 800)
    s += t(cx, zero + 95, lab, 26, NAVY, 700)
s += box(470, 690, 26, 26, ORANGE, ORANGE, 0, 4) + t(508, 712, '메리어트', 22, NAVY, 700, 'start')
s += box(680, 690, 26, 26, NAVY, NAVY, 0, 4) + t(718, 712, '힐튼', 22, NAVY, 700, 'start')
s += t(840, 712, '메리어트 아시아태평양은 중국 제외 · 9% 이상', 20, GRAY, 600, 'start')
s += t(800, 790, '메리어트는 1~9월 개관의 40% 이상이 브랜드 전환', 24)
imgs['global-hotel-chains-q3-2026'] = frame(s)

# 4) 카노 모형 곡선
s = t(800, 95, '카노 모형, 속성마다 만족을 만드는 방식이 다르다', 36)
ox, oy, W, H = 520, 470, 660, 330  # 원점(가운데)
s += f'<line x1="{ox - W/2:.0f}" y1="{oy}" x2="{ox + W/2 + 20:.0f}" y2="{oy}" stroke="{GRAY}" stroke-width="3" marker-end="url(#ag)"/>'
s += f'<line x1="{ox}" y1="{oy + H/2 + 10:.0f}" x2="{ox}" y2="{oy - H/2 - 20:.0f}" stroke="{GRAY}" stroke-width="3" marker-end="url(#ag)"/>'
s += t(ox, oy - H / 2 - 35, '만족', 22, GRAY, 700) + t(ox, oy + H / 2 + 45, '불만', 22, GRAY, 700)
s += t(ox - W / 2, oy + 40, '충족 안 됨', 20, GRAY, 600, 'start') + t(ox + W / 2 + 20, oy + 40, '충족됨', 20, GRAY, 600, 'end')
L, R = ox - W / 2 + 10, ox + W / 2
s += f'<path d="M{L} {oy + 110} L{R} {oy - 110}" stroke="{NAVY}" stroke-width="7" fill="none"/>'
s += f'<path d="M{L} {oy + 160} Q{ox - 60} {oy - 10} {R} {oy - 15}" stroke="{GRAY}" stroke-width="7" fill="none"/>'
s += f'<path d="M{L} {oy + 15} Q{ox + 60} {oy + 10} {R} {oy - 160}" stroke="{ORANGE}" stroke-width="7" fill="none"/>'
# 범례 카드 (오른쪽)
cards = [('매력적 품질', '없어도 불만 없음, 있으면 기쁨', ORANGE, '예: 이름을 기억한 맞이'), ('일원적 품질', '충족할수록 만족이 비례', NAVY, '예: 체크인 대기 시간'), ('당연적 품질', '있어도 칭찬 없음, 없으면 불만', GRAY, '예: 욕실 청결')]
for i, (a, b, c, ex) in enumerate(cards):
    y = 190 + i * 175
    s += box(920, y, 540, 145, WHITE, c, 4)
    s += t(948, y + 48, a, 28, c if c != GRAY else NAVY, 800, 'start') + t(948, y + 88, b, 21, NAVY, 600, 'start') + t(948, y + 122, ex, 19, GRAY, 600, 'start')
s += t(800, 790, '시간이 지나면 매력적 품질은 당연적 품질로 옮겨 간다', 25)
imgs['kano-model-hotel-attributes'] = frame(s)

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = b.new_page(viewport={'width': 1600, 'height': 900})
        for slug, svg in imgs.items():
            pg.set_content(f'<html><body style="margin:0">{svg}</body></html>')
            png = pg.screenshot(clip={'x': 0, 'y': 0, 'width': 1600, 'height': 900})
            Image.open(io.BytesIO(png)).convert('RGB').save(os.path.join(OUT, slug + '.jpg'), quality=88)
            print('ok', slug)
        b.close()
