"""대표 이미지(1600x900) 공용 템플릿
- 분류마다 배경색을 달리하고(어두운 2종·밝은 2종), 4가지 구도 중 하나를 고른다.
- 글자와 핵심 도형은 홈 카드(3:2)에 잘리지 않도록 가로 125~1475px 안에 둔다.
사용 예:
    from thumblib import keyword, stat, compare, steps, render
    svg = stat('hotel-resort', '+25.2%', '리조트 객실당 매출', '2026년 3분기 · 전년 대비', icon='resort')
    render({'slug': svg}, '출력폴더')
"""
from playwright.sync_api import sync_playwright
import os

FONT = "'Noto Sans CJK KR','Noto Sans KR',sans-serif"
NAVY, ORANGE, CREAM, GRAY = '#1E2A3A', '#C8792D', '#F7F5F0', '#8A96A8'

# 분류별 색 구성: bg 배경, fg 주 글자, sub 보조 글자, acc 강조, card 카드 바탕, line 선
THEMES = {
    'tourism-policy':  dict(bg='#1E2A3A', fg='#F7F5F0', sub='#AEB8C6', acc='#E0954A', card='#2A3A50', line='#3B4C64', label='관광정책·트렌드'),
    'hotel-resort':    dict(bg='#2F5F63', fg='#F7F5F0', sub='#B9D0CF', acc='#F0B36B', card='#3A6E72', line='#4E8286', label='호텔 & 리조트'),
    'service-quality': dict(bg='#F7F5F0', fg='#1E2A3A', sub='#6B7686', acc='#C8792D', card='#FFFFFF', line='#D5D9E0', label='서비스품질'),
    'hotel-it-qa':     dict(bg='#E6ECF2', fg='#1E2A3A', sub='#5E6B7D', acc='#C8792D', card='#FFFFFF', line='#C7D0DB', label='호텔 IT·QA'),
    'report':          dict(bg='#1E2A3A', fg='#F7F5F0', sub='#AEB8C6', acc='#E0954A', card='#2A3A50', line='#3B4C64', label='리포트'),
    'column':          dict(bg='#ECE7DD', fg='#1E2A3A', sub='#6B7686', acc='#C8792D', card='#FFFFFF', line='#D5CFC2', label='칼럼'),
}

# 선 아이콘(24x24 기준 경로). stroke로 그린다.
ICONS = {
    'hotel':    'M4 21V5l8-3 8 3v16M4 21h16M9 21v-4h6v4M8 8h2M14 8h2M8 12h2M14 12h2',
    'resort':   'M3 20h18M7 20c0-6 1-10 5-13M12 7c-2-2-5-2-7 0M12 7c2-2 5-2 7 0M12 7c-1-3 0-5 3-5M14 20a4 4 0 0 1 6 0',
    'bed':      'M3 18V7M3 13h18v5M21 18v-4a3 3 0 0 0-3-3h-8v2M6.5 11.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z',
    'key':      'M14 10a4 4 0 1 0-1.2 2.8L20 20M17 17l2-2M15 15l2-2',
    'plane':    'M17.8 19.2L16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z',
    'globe':    'M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18',
    'chartup':  'M3 21h18M6 17v-4M11 17V9M16 17v-7M4 11l6-5 4 3 6-6M17 3h3v3',
    'chartdown':'M3 21h18M6 17V9M11 17v-5M16 17v-3M4 6l6 5 4-3 6 6M17 14h3v-3',
    'kiosk':    'M7 2h10v13H7zM9 5h6M9 8h6M10 15v4M14 15v4M6 21h12',
    'shield':   'M12 22s8-3 8-10V5l-8-3-8 3v7c0 7 8 10 8 10zM8.5 12l2.5 2.5 4.5-5',
    'users':    'M9 11a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7zM2 20c0-3.5 3-6 7-6s7 2.5 7 6M16 4.5a3.5 3.5 0 0 1 0 6.5M18 14c2.5.8 4 3 4 6',
    'calendar': 'M4 5h16v16H4zM4 9h16M8 3v4M16 3v4M8 13h2M14 13h2M8 17h2',
    'won':      'M4 7l3 11 3-11 2 0 3 11 3-11M3 11h18M3 14h18',
    'doc':      'M6 2h9l4 4v16H6zM15 2v4h4M9 11h7M9 15h7M9 19h4',
    'server':   'M4 4h16v6H4zM4 14h16v6H4zM7.5 7h.01M7.5 17h.01M11 7h6M11 17h6',
    'pin':      'M12 22s7-7 7-12a7 7 0 1 0-14 0c0 5 7 12 7 12zM12 12.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z',
    'star':     'M12 2.5l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4 6.1 20.5l1.2-6.5L2.5 9.4l6.6-.9z',
    'check':    'M4 12.5l5 5L20 6.5',
    'alert':    'M12 3l10 18H2zM12 10v5M12 18h.01',
    'search':   'M10.5 18a7.5 7.5 0 1 0 0-15 7.5 7.5 0 0 0 0 15zM16 16l5.5 5.5',
}

def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def icon(name, x, y, size, color, width=1.6):
    """아이콘을 (x,y) 왼쪽 위 기준, size 크기로 그린다."""
    s = size / 24
    return f'<g transform="translate({x},{y}) scale({s})"><path d="{ICONS[name]}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/></g>'

def text(x, y, s, size, fill, weight=700, anchor='start', ls=0):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}">{esc(s)}</text>'

def lines(x, y, rows, size, fill, weight=800, gap=1.22, anchor='start'):
    return ''.join(text(x, y + i * size * gap, r, size, fill, weight, anchor) for i, r in enumerate(rows))

def frame(cat, inner):
    t = THEMES[cat]
    tag = f'<rect x="125" y="96" width="{len(t["label"]) * 26 + 44}" height="50" rx="25" fill="none" stroke="{t["acc"]}" stroke-width="2.5"/>' + text(147, 130, t['label'], 24, t['acc'], 700)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" font-family="{FONT}">'
            f'<rect width="1600" height="900" fill="{t["bg"]}"/>{tag}{inner}</svg>')

# ---- 구도 1: 핵심어(큰 제목 + 큰 아이콘)
def keyword(cat, rows, sub='', icon_name='hotel'):
    """rows: 큰 글자 1~3줄(한 줄 10자 안팎). sub: 아래 한 줄 설명."""
    t = THEMES[cat]
    size = 92 if max(len(r) for r in rows) <= 9 else 78
    y0 = 450 - (len(rows) - 1) * size * 0.61
    s = lines(125, y0, rows, size, t['fg'])
    if sub: s += text(125, y0 + len(rows) * size * 1.22 + 20, sub, 30, t['sub'], 500)
    s += f'<circle cx="1210" cy="470" r="250" fill="{t["card"]}"/>' + icon(icon_name, 1060, 320, 300, t['acc'], 1.4)
    return frame(cat, s)

# ---- 구도 2: 숫자 강조(큰 수치 + 설명)
def stat(cat, value, label, note='', icon_name='chartup'):
    t = THEMES[cat]
    # 글자 폭을 어림해(한글 1em, 숫자·영문 0.6em, 기호 0.35em) 980px 안에 들도록 크기를 정한다
    em = sum(1.0 if ord(ch) > 0x3000 else (0.35 if ch in ',.·' else 0.6) for ch in value)
    vs = min(250, int(980 / max(em, 1)))
    s = text(125, 560, value, vs, t['acc'], 800, ls=-6)
    s += text(130, 650, label, 46, t['fg'], 800) + (text(130, 710, note, 28, t['sub'], 500) if note else '')
    s += f'<rect x="1150" y="250" width="320" height="320" rx="40" fill="{t["card"]}"/>' + icon(icon_name, 1200, 300, 220, t['fg'], 1.5)
    return frame(cat, s)

# ---- 구도 3: 비교(왼쪽 대 오른쪽)
def compare(cat, title, left, right, mid='→'):
    """left/right: (큰 글자, 작은 설명, 아이콘)"""
    t = THEMES[cat]
    s = text(125, 250, title, 54, t['fg'], 800)
    for i, (big, small, ic) in enumerate([left, right]):
        x = 125 + i * 720
        fill = t['card'] if i == 0 else t['acc']
        fg = t['fg'] if i == 0 else ('#1E2A3A' if cat in ('tourism-policy', 'hotel-resort', 'report') else '#FFFFFF')
        s += f'<rect x="{x}" y="320" width="630" height="440" rx="28" fill="{fill}"/>' + icon(ic, x + 50, 370, 120, fg, 1.6)
        s += text(x + 50, 610, big, 64, fg, 800) + text(x + 50, 680, small, 30, fg, 500)
    s += text(800, 570, mid, 64, t['sub'], 700, 'middle')
    return frame(cat, s)

# ---- 구도 4: 단계·요소 3개
def steps(cat, title, items, joiner='arrow'):
    """items: [(아이콘, 짧은 글자, 설명)] 3개. joiner: 'arrow'(흐름) 또는 'plus'(요소)"""
    t = THEMES[cat]
    s = text(125, 260, title, 58, t['fg'], 800)
    for i, (ic, big, small) in enumerate(items[:3]):
        x = 125 + i * 470
        s += f'<rect x="{x}" y="340" width="400" height="420" rx="26" fill="{t["card"]}"/>'
        s += f'<circle cx="{x + 200}" cy="470" r="80" fill="{t["bg"]}"/>' + icon(ic, x + 145, 415, 110, t['acc'], 1.7)
        s += text(x + 200, 625, big, 44, t['fg'], 800, 'middle') + text(x + 200, 680, small, 26, t['sub'], 500, 'middle')
        if i < 2:
            sym = '→' if joiner == 'arrow' else '+'
            s += text(x + 435, 565, sym, 48, t['acc'], 800, 'middle')
    return frame(cat, s)

def render(svgs, out_dir):
    """svgs: {파일이름(확장자 없이): svg문자열}. PNG로 저장한다."""
    os.makedirs(out_dir, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = b.new_page(viewport={'width': 1600, 'height': 900})
        for name, svg in svgs.items():
            pg.set_content(f'<html><body style="margin:0">{svg}</body></html>'); pg.wait_for_timeout(150)
            pg.screenshot(path=f'{out_dir}/{name}.png', clip={'x': 0, 'y': 0, 'width': 1600, 'height': 900})
        b.close()
