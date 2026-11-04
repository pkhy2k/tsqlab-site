"""호텔 IT 솔루션 기사 2편(AI 컨시어지, AI 수익관리) 대표 이미지 원본 생성
사용법: python3 scripts/thumbs/make_20261104c.py → scripts/thumbs/originals/ → watermark.py
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

# 1) AI 컨시어지: 메시지 → 에이전트 격자 → 직원 넘김
s = t(800, 110, 'AI 컨시어지, 업무별 에이전트와 사람에게 넘기는 길', 36)
s += t(800, 155, '야놀자클라우드솔루션 Pulse AI 발표 기준 · 에이전트 8개', 22, GRAY, 500)
s += box(140, 360, 230, 170, SAND, SAND) + t(255, 430, '투숙객 메시지', 26) + t(255, 470, '메신저 · 웹 포털', 20, GRAY, 600)
s += arrow(380, 445, 450, 445)
agents = ['고객 응대', '예약', '체크인·아웃', '룸서비스', '하우스키핑', '결제', '업셀링', '…']
for i, a in enumerate(agents):
    r, c = divmod(i, 4)
    x = 465 + c * 150; y = 330 + r * 120
    s += box(x, y, 135, 95, NAVY if a != '…' else WHITE, NAVY, 3, 12) + t(x + 67, y + 56, a, 20, WHITE if a != '…' else NAVY, 700)
s += t(765, 600, 'PMS와 직접 연결 · 실시간 예약·객실 상태', 20, GRAY, 600)
s += arrow(1080, 445, 1170, 445, ORANGE, 'ao', 6) + t(1125, 420, '넘김', 20, ORANGE)
s += box(1185, 330, 290, 230, WHITE, ORANGE, 3) + t(1330, 390, '직원', 32, ORANGE) + t(1330, 440, '불만 · 환불', 21, NAVY, 600) + t(1330, 475, '안전 · 건강', 21, NAVY, 600) + t(1330, 510, 'AI가 답 못한 요청', 21, NAVY, 600)
s += t(800, 720, '응대 자동화의 품질은 정답률보다 넘김의 설계로 결정된다', 26)
imgs['ai-concierge-pulse-ai-2026'] = frame(s)

# 2) AI 수익관리: 가드레일 밴드 안의 요금 선 (밴드 차트)
s = t(800, 110, 'AI가 요금을 정하고, 사람은 경계를 정한다', 36)
s += t(800, 155, 'AI 수익관리시스템의 역할 분담 (개념도)', 22, GRAY, 500)
x0, x1, ytop, ybot = 200, 1100, 300, 620
s += f'<rect x="{x0}" y="{ytop}" width="{x1 - x0}" height="{ybot - ytop}" fill="{SAND}" rx="10"/>'
s += f'<line x1="{x0}" y1="{ytop}" x2="{x1}" y2="{ytop}" stroke="{ORANGE}" stroke-width="4" stroke-dasharray="14 10"/>' + t(x0 + 10, ytop - 14, '상한 (수익관리자)', 21, ORANGE, 700, 'start')
s += f'<line x1="{x0}" y1="{ybot}" x2="{x1}" y2="{ybot}" stroke="{ORANGE}" stroke-width="4" stroke-dasharray="14 10"/>' + t(x0 + 10, ybot + 36, '하한 (수익관리자)', 21, ORANGE, 700, 'start')
pts = [(200, 520), (290, 480), (380, 500), (470, 430), (560, 450), (650, 380), (740, 400), (830, 350), (920, 420), (1010, 390), (1100, 440)]
s += f'<polyline points="{" ".join(f"{x},{y}" for x, y in pts)}" fill="none" stroke="{NAVY}" stroke-width="6" stroke-linejoin="round"/>'
for x, y in pts: s += f'<circle cx="{x}" cy="{y}" r="7" fill="{NAVY}"/>'
s += t(650, 560, 'AI: 매일의 요금 결정', 24, NAVY, 700)
s += box(1170, 290, 305, 340, WHITE, NAVY, 3) + t(1322, 340, '사람이 맡는 예외', 25)
for i, c in enumerate(['신규 호텔 초기 운영', '시장의 급격한 변화', '협상 요금(기업·단체)', '추천 거부와 그 이유']):
    y = 400 + i * 58
    s += f'<circle cx="1205" cy="{y - 8}" r="10" fill="{ORANGE}"/>' + t(1228, y, c, 20, NAVY, 600, 'start')
s += t(800, 735, '자동화가 깊어질수록 가드레일을 정하는 판단이 중요해진다', 26)
imgs['ai-rms-guardrails-2026'] = frame(s)

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
