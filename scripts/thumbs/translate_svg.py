"""한국어 대표 이미지 생성 스크립트의 SVG를 그대로 가져와 글자만 영어로 바꿔 영어판 원본을 만든다.
사용법:
  python3 scripts/thumbs/translate_svg.py list <스크립트.py> <슬러그> ...      # 바꿀 한국어 글자 목록 출력(JSON)
  python3 scripts/thumbs/translate_svg.py render <번역.json>                   # scripts/thumbs/originals/en/<슬러그>.jpg 생성
번역 JSON 형식: {"<슬러그>": {"script": "make_20261104.py", "map": {"한국어 글자": "English", ...}}}
렌더 뒤 python3 scripts/thumbs/watermark.py --en <슬러그> ... 로 로고를 넣는다. 영어가 길어 잘리거나 겹치면 map의 영어를 줄이거나 "@size" 규칙을 쓴다.
"""
import os, re, sys, json, io, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'originals', 'en')
HANGUL = re.compile(r'[가-힣]')

def load_imgs(script):
    src = open(os.path.join(HERE, script)).read()
    for cut in ('\nwith sync_playwright()', "\nif __name__ == '__main__':", '\nrender('):
        i = src.find(cut)
        if i > 0: src = src[:i]
    tmp = tempfile.mkdtemp()
    g = {'__name__': 'tsvg', '__file__': os.path.join(HERE, script)}
    old = sys.argv; sys.argv = [script, tmp]; sys.path.insert(0, HERE)
    try: exec(compile(src, script, 'exec'), g)
    finally: sys.argv = old
    return g['imgs']

def texts(svg):
    return [t for t in re.findall(r'>([^<>]+)<', svg) if HANGUL.search(t)]

def translate(svg, m):
    # "@16|English" 형식이면 그 글자의 font-size를 16으로 줄인다(영어가 길어 넘칠 때)
    for ko, en in list(m.items()):
        mo = re.match(r'@(\d+)\|(.*)$', en)
        if mo:
            svg = re.sub(r'(<text[^>]*font-size=")\d+("[^>]*>)' + re.escape(ko) + '<', lambda x: x.group(1) + mo.group(1) + x.group(2) + mo.group(2) + '<', svg)
            m = {**m, ko: mo.group(2)}
    def rep(mo):
        s = mo.group(1)
        return '>' + (m.get(s.strip(), s) if HANGUL.search(s) else s) + '<'
    out = re.sub(r'>([^<>]+)<', rep, svg)
    out = out.replace("'Noto Sans CJK KR','Noto Sans KR',sans-serif", "'Noto Sans','Noto Sans CJK KR',sans-serif").replace("'Noto Serif CJK KR','Noto Serif KR',serif", "'Noto Serif','Noto Serif CJK KR',serif")
    return out

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'list':
        imgs = load_imgs(sys.argv[2])
        print(json.dumps({s: sorted(set(x.strip() for x in texts(imgs[s]))) for s in sys.argv[3:]}, ensure_ascii=False, indent=1))
    else:
        cfg = json.load(open(sys.argv[2]))
        from playwright.sync_api import sync_playwright
        from PIL import Image
        os.makedirs(OUT, exist_ok=True)
        cache = {}
        with sync_playwright() as p:
            b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
            pg = b.new_page(viewport={'width': 1600, 'height': 900})
            for slug, c in cfg.items():
                imgs = cache.setdefault(c['script'], load_imgs(c['script']))
                svg = translate(imgs[slug], c['map'])
                left = [t for t in texts(svg)]
                if left: print('번역 누락', slug, left)
                pg.set_content(f'<html><body style="margin:0">{svg}</body></html>'); pg.wait_for_timeout(200)
                png = pg.screenshot(clip={'x': 0, 'y': 0, 'width': 1600, 'height': 900})
                Image.open(io.BytesIO(png)).convert('RGB').save(os.path.join(OUT, f'{slug}.jpg'), 'JPEG', quality=88)
                print('ok', slug)
            b.close()
