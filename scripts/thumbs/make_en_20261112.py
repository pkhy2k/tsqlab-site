"""영어판 대표 이미지(1600x900) 원본 생성 — 목요일 기사 3편 (2026-11-12)
사용법: python3 scripts/thumbs/make_en_20261112.py
결과: scripts/thumbs/originals/en/<슬러그>.jpg (로고 없음) → python3 scripts/thumbs/watermark.py --en <슬러그> ...
make_20261112.py의 도식을 그대로 쓰고 글자만 영어로 바꾼다(TXT['en']).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_20261112 import build, render, ROOT

if __name__ == '__main__':
    render(build('en'), os.path.join(ROOT, 'scripts', 'thumbs', 'originals', 'en'))
