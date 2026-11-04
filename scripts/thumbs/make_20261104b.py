"""호텔 IT 솔루션 기사 3편 대표 이미지(1600x900) 원본 생성
사용법: python3 scripts/thumbs/make_20261104b.py
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

# 1) 에이전트 예약 흐름 (가로 흐름도)
s = t(800, 110, 'AI 에이전트는 호텔을 어떻게 예약하는가', 36)
s += t(800, 155, '메타 Muse의 연결 규칙과 클라우드베즈 연동 발표 기준', 22, GRAY, 500)
s += box(140, 360, 230, 150, SAND, SAND) + t(255, 425, '여행자', 30) + t(255, 465, '"바닷가 호텔 2박"', 21, GRAY, 600)
s += arrow(380, 435, 455, 435)
s += box(465, 340, 250, 190, NAVY, NAVY) + t(590, 420, 'AI 에이전트', 30, WHITE) + t(590, 462, '구매 전 사용자 승인', 20, '#C9CED6', 500)
opts = [('① 연결 도구', '있으면 우선 사용', ORANGE), ('② 공개 API', '직접 연결', NAVY), ('③ 브라우저', '화면을 직접 조작', GRAY)]
for i, (a, b, c) in enumerate(opts):
    y = 230 + i * 150
    s += arrow(720, 435, 800, y + 55, c, 'ao' if c == ORANGE else ('an' if c == NAVY else 'ag'), 4)
    s += box(810, y, 260, 110, WHITE, c, 3) + t(940, y + 48, a, 26, c) + t(940, y + 84, b, 20, GRAY, 600)
s += arrow(1080, 285, 1175, 400, ORANGE, 'ao', 5)
s += box(1185, 330, 290, 90, WHITE, ORANGE, 3) + t(1330, 385, '호텔 예약 엔진', 26)
s += arrow(1330, 425, 1330, 480, NAVY, 'an', 5)
s += box(1185, 490, 290, 110, NAVY, NAVY) + t(1330, 540, 'PMS', 30, WHITE) + t(1330, 578, '직접 예약으로 기록', 20, '#C9CED6', 500)
s += t(800, 735, '요금·재고(ARI)와 정책 데이터가 정확해야 에이전트가 고를 수 있다', 26, NAVY, 700)
imgs['ai-agent-booking-direct-channel-2026'] = frame(s)

# 2) PMS-MCP 허브와 관리 장치 (중앙 허브형 + 수치 강조)
s = t(800, 110, 'PMS와 AI 비서를 잇는 MCP, 그 사이에 필요한 것', 36)
s += box(140, 330, 280, 220, NAVY, NAVY) + t(280, 420, 'PMS', 40, WHITE) + t(280, 465, '예약 · 요금 · 고객', 22, '#C9CED6', 500)
s += arrow(430, 440, 520, 440, ORANGE, 'ao', 6) + t(475, 415, 'MCP', 22, ORANGE)
gate = [('권한', '사람 계정 범위'), ('기록', '누가 무엇을'), ('책임자', '업무별 지정')]
s += box(535, 260, 330, 360, WHITE, ORANGE, 3) + t(700, 305, '관리 장치', 26, ORANGE)
for i, (a, b) in enumerate(gate):
    y = 335 + i * 92
    s += box(565, y, 270, 76, SAND, SAND, 0, 10) + t(640, y + 47, a, 26, NAVY, 700) + t(760, y + 47, b, 19, GRAY, 600)
s += arrow(875, 440, 960, 440, GRAY, 'ag', 5)
for i, n in enumerate(['ChatGPT', 'Claude', 'Copilot', 'Gemini']):
    y = 260 + i * 92
    s += box(975, y, 230, 72, WHITE, LINE, 3, 36) + t(1090, y + 46, n, 24, NAVY, 600)
s += box(1238, 300, 230, 250, WHITE, LINE, 3) + t(1353, 360, 'MCP 사용량', 22, GRAY, 600) + t(1353, 440, '+70%', 64, ORANGE, 800) + t(1353, 490, '2026년 7~9월', 20, GRAY, 600) + t(1353, 520, '아팔레오 발표', 18, GRAY, 500)
s += t(800, 720, '조회부터 시작하고, 쓰기 권한과 대량 변경은 단계적으로', 26)
imgs['pms-mcp-ai-assistant-governance-2026'] = frame(s)

# 3) 키오스크 기능 확장 (두 갈래 분기)
s = t(800, 110, '숙박 키오스크, 체크인 기계에서 무인 프런트로', 36)
s += t(800, 155, '2026년 10월 국내 신제품 발표 기준', 22, GRAY, 500)
s += box(150, 360, 300, 170, NAVY, NAVY) + t(300, 440, '키오스크', 34, WHITE) + t(300, 482, '체크인 · 체크아웃', 22, '#C9CED6', 500)
s += f'<path d="M460 420 C560 420 560 290 650 290" stroke="{ORANGE}" stroke-width="5" fill="none" marker-end="url(#ao)"/>'
s += f'<path d="M460 470 C560 470 560 600 650 600" stroke="{NAVY}" stroke-width="5" fill="none" marker-end="url(#an)"/>'
s += box(665, 210, 360, 160, WHITE, ORANGE, 3) + t(845, 262, '판매 · 재고', 30, ORANGE) + t(845, 302, '24시간 편의용품 판매', 21, NAVY, 600) + t(845, 336, '자동 발주 · AI 가격 조정', 21, NAVY, 600)
s += box(665, 520, 360, 160, WHITE, NAVY, 3) + t(845, 572, '무인 프런트', 30) + t(845, 612, '간이 PMS · 채널 연동', 21, NAVY, 600) + t(845, 646, '객실키 · AI 응대', 21, NAVY, 600)
checks = ['장애 시 대체 경로', '가격 변동 고지', '접근성 실사용 점검', '개인정보 처리 범위']
s += box(1105, 250, 370, 400, SAND, SAND, 0) + t(1290, 305, '서비스품질 점검', 26)
for i, c in enumerate(checks):
    y = 360 + i * 70
    s += f'<circle cx="1150" cy="{y - 8}" r="12" fill="{ORANGE}"/>' + t(1180, y, c, 23, NAVY, 600, 'start')
s += t(800, 770, '기능이 늘수록 멈췄을 때의 준비가 품질이 된다', 26)
imgs['kiosk-to-unmanned-front-2026'] = frame(s)

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
