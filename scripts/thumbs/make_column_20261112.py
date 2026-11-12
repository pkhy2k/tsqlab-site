"""칼럼 'AI 시대, 관광인은 무엇으로 살아남는가' 대표 이미지(1600x900) 원본 (2026-11-12)
사용법: python3 scripts/thumbs/make_column_20261112.py → scripts/thumbs/originals/<슬러그>.jpg, 이어서 watermark.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_20261109 import frame, t, box, NAVY, ORANGE, GRAY, LINE, WHITE, SAND, OUT
from playwright.sync_api import sync_playwright
from PIL import Image
import io

s = t(800, 100, 'AI 시대, 관광인의 역량은 어디로 옮겨 가는가', 36)
s += box(150, 300, 400, 300, SAND, LINE, 3, 18)
s += t(350, 400, '할 줄 아는가', 34, GRAY, 800)
s += t(350, 455, '글쓰기 · 번역 · 도식 · 코딩', 22, GRAY, 600)
s += t(350, 520, 'AI가 장벽을 낮춘 영역', 22, GRAY, 700)
s += f'<line x1="570" y1="450" x2="760" y2="450" stroke="{NAVY}" stroke-width="5" marker-end="url(#an)"/>'
rows = [('무엇을 만들지 아는가', '방향과 선택'), ('맞는지 판단하는가', '현장의 언어와 검증'), ('책임질 수 있는가', '고객 앞의 사람')]
for i, (a, b) in enumerate(rows):
    y = 215 + i * 165
    c = ORANGE if i == 1 else NAVY
    s += box(790, y, 660, 135, WHITE, c, 4, 16)
    s += t(830, y + 60, a, 32, c, 800, 'start') + t(830, y + 104, b, 23, GRAY, 600, 'start')
s += t(800, 760, '대체되는 것은 일의 일부이지, 그 일이 왜 필요한지 아는 사람이 아니다', 25)
svg = frame(s)
imgs = {'column-surviving-in-the-ai-era': svg}
if __name__ == '__main__':
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = b.new_page(viewport={'width': 1600, 'height': 900})
        pg.set_content(f'<html><body style="margin:0">{svg}</body></html>')
        png = pg.screenshot(clip={'x': 0, 'y': 0, 'width': 1600, 'height': 900})
        Image.open(io.BytesIO(png)).convert('RGB').save(os.path.join(OUT, 'column-surviving-in-the-ai-era.jpg'), quality=88)
        print('ok column-surviving-in-the-ai-era')
        b.close()
