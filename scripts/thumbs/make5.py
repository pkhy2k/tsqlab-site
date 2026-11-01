"""신규 주제 3편 대표 이미지(1600x900) 생성
사용법: python3 scripts/thumbs/make5.py <출력 폴더>
"""
from playwright.sync_api import sync_playwright
import os, sys
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
NAVY, ORANGE, CREAM, SAND, GRAY, LINE, WHITE, RED = '#1E2A3A', '#C8792D', '#F7F5F0', '#ECE7DD', '#8A96A8', '#D5D9E0', '#FFFFFF', '#C0504D'
FONT = "'Noto Sans CJK KR','Noto Sans KR',sans-serif"
DEFS = f'<defs><marker id="ag" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="{GRAY}"/></marker></defs>'
def frame(inner, bg=CREAM): return f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" font-family="{FONT}"><rect width="1600" height="900" fill="{bg}"/>{DEFS}{inner}</svg>'
def t(x, y, s, size=26, fill=NAVY, w=700, a='middle'): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{s}</text>'
imgs = {}

# 1) 서비스 회복: 키오스크 오류 → 사람 → 공정성 3차원
s = f'<rect x="150" y="220" width="300" height="440" rx="22" fill="{NAVY}"/><rect x="178" y="252" width="244" height="190" rx="10" fill="{CREAM}"/>'
s += f'<circle cx="300" cy="320" r="34" fill="none" stroke="{RED}" stroke-width="7"/><path d="M300 300 L300 326 M300 338 L300 342" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>' + t(300, 405, '예약을 찾을 수 없습니다', 20, NAVY, 600)
s += f'<rect x="205" y="480" width="190" height="110" rx="8" fill="#2E3D52"/>' + t(300, 720, '셀프서비스 실패', 28)
s += f'<path d="M470 440 L640 440" stroke="{GRAY}" stroke-width="5" marker-end="url(#ag)"/>' + t(555, 415, '사람에게 넘김', 22, GRAY, 600)
s += f'<circle cx="760" cy="370" r="60" fill="{ORANGE}"/><rect x="680" y="440" width="160" height="150" rx="70" fill="{ORANGE}"/>' + t(760, 720, '서비스 회복', 28, ORANGE)
s += f'<path d="M880 440 L1010 440" stroke="{GRAY}" stroke-width="5" marker-end="url(#ag)"/>'
for i, (a, b) in enumerate([('분배 공정성', '해결과 보상'), ('절차 공정성', '속도와 노력'), ('상호작용 공정성', '설명·사과·공감')]):
    y = 250 + i * 150
    s += f'<rect x="1030" y="{y}" width="420" height="110" rx="14" fill="{WHITE}" stroke="{LINE}" stroke-width="3"/>' + t(1240, y + 50, a, 30) + t(1240, y + 88, b, 22, GRAY, 500)
imgs['kiosk-failure-service-recovery'] = frame(s)

# 2) 날짜: 달력 vs 영업일자 타임라인
x0, x1 = 160, 1440
X = lambda h: x0 + (h - 20) / 10 * (x1 - x0)   # 20시~익일 6시
s = t(800, 130, '자정과 나이트 오디트 사이', 34)
s += f'<line x1="{x0}" y1="330" x2="{x1}" y2="330" stroke="{NAVY}" stroke-width="5"/><line x1="{x0}" y1="560" x2="{x1}" y2="560" stroke="{NAVY}" stroke-width="5"/>'
s += t(x0, 270, '달력 날짜', 26, GRAY, 600, 'start') + t(x0, 500, '영업일자', 26, GRAY, 600, 'start')
mid, aud = X(24), X(27)
s += f'<rect x="{x0}" y="300" width="{mid - x0}" height="60" fill="{SAND}"/><rect x="{mid}" y="300" width="{x1 - mid}" height="60" fill="#E4E7EC"/>'
s += t(X(22), 340, '11월 1일', 28) + t(X(28.5), 340, '11월 2일', 28)
s += f'<rect x="{x0}" y="530" width="{aud - x0}" height="60" fill="{SAND}"/><rect x="{aud}" y="530" width="{x1 - aud}" height="60" fill="#E4E7EC"/>'
s += t(X(22), 570, '11월 1일', 28) + t(X(28.5), 570, '11월 2일', 28)
s += f'<rect x="{mid}" y="380" width="{aud - mid}" height="130" fill="{ORANGE}" opacity="0.25"/>' + t((mid + aud) / 2, 455, '날짜가 어긋나는 시간', 26, ORANGE)
for h, lab in [(24, '00:00 자정'), (27, '03:00 나이트 오디트')]:
    s += f'<line x1="{X(h)}" y1="280" x2="{X(h)}" y2="640" stroke="{ORANGE}" stroke-width="4" stroke-dasharray="10 8"/>' + t(X(h), 680, lab, 24, NAVY, 700)
s += t(800, 790, '마감 시각은 호텔마다 다르다 · 예시', 22, GRAY, 500)
imgs['hotel-dates-test-design'] = frame(s)

# 3) 등급평가: 1000점 막대 + 성급 기준
s = t(800, 130, '호텔 등급평가 1,000점', 36)
s += f'<rect x="200" y="200" width="840" height="90" fill="{NAVY}"/><rect x="1040" y="200" width="360" height="90" fill="{ORANGE}"/>'
s += t(620, 257, '현장평가 700점', 30, WHITE) + t(1220, 257, '암행·불시평가 300점', 28, WHITE)
for i, (st, pct) in enumerate([(5, 90), (4, 80), (3, 65), (2, 50), (1, 40)]):
    y = 360 + i * 70; w = 1200 * pct / 100
    s += f'<rect x="200" y="{y}" width="{w}" height="46" rx="6" fill="{SAND}"/>' + t(215, y + 33, '★' * st, 26, ORANGE, 700, 'start') + t(200 + w - 15, y + 33, f'{pct}% 이상', 24, NAVY, 700, 'end')
s += f'<rect x="1080" y="700" width="320" height="120" rx="14" fill="{WHITE}" stroke="{ORANGE}" stroke-width="3"/>' + t(1240, 748, '개인정보 보호', 28) + t(1240, 790, '가점 최대 10 · 감점 10', 22, ORANGE, 700)
imgs['hotel-grading-reform-2026'] = frame(s)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': 1600, 'height': 900})
    for name, svg in imgs.items():
        pg.set_content(f'<html><body style="margin:0">{svg}</body></html>'); pg.wait_for_timeout(150)
        pg.screenshot(path=f'{OUT}/{name}.png', clip={'x': 0, 'y': 0, 'width': 1600, 'height': 900})
    b.close()
print('done')
