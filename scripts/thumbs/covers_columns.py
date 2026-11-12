"""칼럼 표지(600x800) 생성 — 홈 칼럼 목록에 쓰는 세로형 표지
사용법: python3 scripts/thumbs/covers_columns.py        # 한국어 표지
       python3 scripts/thumbs/covers_columns.py --en   # 영어판 표지(COVERS_EN → static/images/posts/en/)
새 칼럼을 쓰면 COVERS에 (슬러그: (제목 줄 목록, 필자명))을 추가하고 다시 실행한 뒤,
글 프론트매터에 cover: /images/posts/<슬러그>-cover.jpg 를 넣는다.
제목은 한 줄 12자 안팎, 2~3줄로 나눈다.
"""
import os, io
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'static', 'images', 'posts')
NAVY, ORANGE, WHITE = '#1E2A3A', '#C8792D', '#FFFFFF'
FONT = "'Noto Sans CJK KR','Noto Sans KR',sans-serif"
SERIF = "'Noto Serif CJK KR','Noto Serif KR',serif"
LOGO = lambda x, y, s: f'<g transform="translate({x} {y}) scale({s})"><path d="M50 347 V160 A140 140 0 0 1 330 160 V347" fill="none" stroke="{WHITE}" stroke-width="16"/><rect x="7" y="348" width="366" height="16" fill="{WHITE}"/><rect x="103" y="262" width="47" height="86" fill="{WHITE}"/><rect x="167" y="215" width="47" height="133" fill="{WHITE}"/><rect x="230" y="159" width="47" height="189" fill="{ORANGE}"/></g>'

COVERS = {
    'column-surviving-in-the-ai-era': (['AI 대전환시대,', '관광업계 종사자의', '위기와 생존'], '박건희'),
    'column-testing-is-asking': (['테스트는', '질문이다'], '박건희'),
    'column-kiosk-and-front-manager': (['키오스크가 두려웠던', '프런트 매니저가', '품질을 묻게 되기까지'], '박건희'),
    'column-housekeeping-seven-principles': (['하우스키핑 점검표로', '읽는 소프트웨어', '테스트 7원칙'], '박건희'),
    'report-ai-agent-qa-workflow': (['AI 에이전트와', '함께하는', 'QA 업무 가이드'], '박건희'),
    'report-cancellation-qa-case': (['호텔 예약', '변경·취소 기능', 'QA 사례 분석'], '박건희'),
    'report-risk-based-testing-hotel': (['호텔 시스템의', '리스크 기반 테스트'], '박건희'),
    'report-hotel-kiosk-sstqual-flow': (['호텔 키오스크는', '무엇으로 고객을', '몰입하게 하는가'], '박건희'),
}

COVERS_EN = {
    'column-surviving-in-the-ai-era': (['Crisis and', 'Survival in the', 'AI Transition'], 'Winston Park'),
    'column-testing-is-asking': (['Testing Is', 'Asking', 'Questions'], 'Winston Park'),
    'column-kiosk-and-front-manager': (['The Front Office', 'Manager Who', 'Feared Kiosks'], 'Winston Park'),
    'column-housekeeping-seven-principles': (['Seven Testing', 'Principles in a', 'Housekeeping List'], 'Winston Park'),
    'report-ai-agent-qa-workflow': (['QA Work with', 'AI Agents:', 'A Guide'], 'Winston Park'),
    'report-cancellation-qa-case': (['Booking Changes', 'and Cancellations:', 'A QA Case Study'], 'Winston Park'),
    'report-risk-based-testing-hotel': (['Risk-Based', 'Testing for', 'Hotel Systems'], 'Winston Park'),
    'report-hotel-kiosk-sstqual-flow': (['What Makes', 'Guests Absorbed', 'at a Kiosk?'], 'Winston Park'),
}
EN = False

def svg(lines, author):
    t = ''.join(f'<text x="56" y="{300 + i*70}" style="font-family:{SERIF}" font-size="{44 if EN else 50}" font-weight="700" fill="{WHITE}" letter-spacing="-1">{l}</text>' for i, l in enumerate(lines))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="800" viewBox="0 0 600 800" font-family="{FONT}"><rect width="600" height="800" fill="{NAVY}"/>
<rect x="56" y="110" width="60" height="8" fill="{ORANGE}"/>
<text x="56" y="172" font-size="28" font-weight="700" fill="#C9D1DC" letter-spacing="7">COLUMN</text>{t}
<text x="56" y="{300 + len(lines)*70 + 30}" font-size="26" font-weight="500" fill="#E0954A">{author}</text>
<line x1="56" y1="620" x2="544" y2="620" stroke="#3A4A62" stroke-width="2"/>{LOGO(56, 650, 0.2)}
<text x="140" y="702" style="font-family:{SERIF}" font-size="26" font-weight="700" fill="{WHITE}">{'Tourism Service Quality Lab' if EN else '관광서비스품질연구소'}</text></svg>'''

if __name__ == '__main__':
    import sys
    if '--en' in sys.argv:
        EN = True; COVERS = COVERS_EN; OUT = os.path.join(OUT, 'en'); SERIF = "'Noto Serif','Noto Serif CJK KR',serif"
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = b.new_page(viewport={'width': 600, 'height': 800})
        for slug, (lines, author) in COVERS.items():
            pg.set_content(f'<html><body style="margin:0">{svg(lines, author)}</body></html>'); pg.wait_for_timeout(150)
            png = pg.screenshot(clip={'x': 0, 'y': 0, 'width': 600, 'height': 800})
            Image.open(io.BytesIO(png)).convert('RGB').save(os.path.join(OUT, f'{slug}-cover.jpg'), 'JPEG', quality=90, optimize=True)
            print('ok', slug)
        b.close()
