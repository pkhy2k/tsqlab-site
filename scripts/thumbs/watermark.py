"""대표 이미지 오른쪽 아래에 연구소 로고(아이콘+연구소명)를 넣는다.
- 원본은 scripts/thumbs/originals/<슬러그>.jpg에 보관하고, 결과를 static/images/posts/<슬러그>.jpg로 쓴다.
- 원본에서 매번 다시 만들므로 여러 번 실행해도 로고가 겹치지 않는다.
- 1600x900 이미지만 처리한다(리포트 표지 600x800 등은 건너뜀).
사용:
  python3 scripts/thumbs/watermark.py              # 원본 폴더의 모든 이미지
  python3 scripts/thumbs/watermark.py <슬러그> ...  # 지정한 글만
새 이미지: make 스크립트의 결과 JPEG를 originals에 저장한 뒤 이 스크립트를 실행한다.
"""
import os, sys, io, glob
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, 'scripts', 'thumbs', 'originals')
OUT = os.path.join(ROOT, 'static', 'images', 'posts')
NAVY, ORANGE = '#1E2A3A', '#C8792D'
RIGHT, BOTTOM = 1462, 878   # 홈 카드(좌우 125px 잘림)에서도 보이도록 오른쪽 끝을 1475px 안에 둔다
LEFT = 138                  # 오른쪽 아래가 도식과 겹치면 왼쪽 아래에 둔다

MARK = f'''<html><body style="margin:0;background:transparent">
<div id="m" style="display:inline-flex;flex-direction:column;align-items:ALIGN;gap:7px;padding:2px">
<div style="display:inline-flex;align-items:flex-end;gap:9px;color:{NAVY};font-family:'Noto Serif CJK KR',serif;font-weight:700;font-size:23px;letter-spacing:-0.4px;line-height:1">
<svg width="28" height="27" viewBox="130 50 380 372"><path d="M180 397 V210 A140 140 0 0 1 460 210 V397" fill="none" stroke="{NAVY}" stroke-width="20"/><rect x="137" y="396" width="366" height="20" fill="{NAVY}"/><rect x="233" y="312" width="47" height="86" fill="{NAVY}"/><rect x="297" y="265" width="47" height="133" fill="{NAVY}"/><rect x="360" y="209" width="47" height="189" fill="{ORANGE}"/></svg>
<span style="padding-bottom:1px">관광서비스품질연구소</span></div>
<div style="color:#A9B1BE;font-family:'Noto Sans CJK KR',sans-serif;font-weight:400;font-size:14px;letter-spacing:0.2px;line-height:1">© Tourism Service Quality Lab. All rights reserved.</div>
</div></body></html>'''

def render_mark(align):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = b.new_page(viewport={'width': 800, 'height': 200})
        pg.set_content(MARK.replace('ALIGN', align)); pg.wait_for_timeout(200)
        png = pg.locator('#m').screenshot(omit_background=True)
        b.close()
    return Image.open(io.BytesIO(png)).convert('RGBA')

def busy(im, box, bg=245):
    reg = im.crop(box).convert('L'); px = reg.load(); w, h = reg.size
    return sum(1 for i in range(w) for j in range(h) if abs(px[i, j] - bg) > 20) / (w * h) > 0.001

def main(slugs):
    mark_r, mark_l = render_mark('flex-end'), render_mark('flex-start')
    files = [os.path.join(SRC, s + '.jpg') for s in slugs] if slugs else sorted(glob.glob(os.path.join(SRC, '*.jpg')))
    for f in files:
        im = Image.open(f).convert('RGB')
        if im.size != (1600, 900):
            continue
        mark = mark_r
        y = BOTTOM - mark.height
        x = RIGHT - mark.width
        if busy(im, (x - 12, y - 4, RIGHT + 8, BOTTOM + 6)):
            x = LEFT; mark = mark_l
            if busy(im, (x - 8, y - 4, x + mark.width + 12, BOTTOM + 6)):
                print('확인 필요(양쪽 모두 겹침, 오른쪽에 둠)', os.path.basename(f)); mark = mark_r; x = RIGHT - mark.width
        im.paste(mark, (x, y), mark)
        im.save(os.path.join(OUT, os.path.basename(f)), 'JPEG', quality=88, optimize=True)
        print('ok', os.path.basename(f))

if __name__ == '__main__':
    main(sys.argv[1:])
