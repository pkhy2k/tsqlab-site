# 게시물 작성 규칙 (Claude·편집부용)

이 문서는 Claude가 연구소 게시물을 작성할 때 따르는 규칙이다. 소장의 콘텐츠 가이드는 아래 "편집 가이드" 절에 추가한다.

## 1. 작업 흐름

1. 소장이 주제나 콘텐츠 가이드를 전달한다.
2. Claude가 `content/posts/<영문-슬러그>.md` 파일로 초안을 작성한다.
3. Claude는 `main` 브랜치에 직접 올리지 않고, `post/<슬러그>` 브랜치에 커밋한 뒤 PR(Pull Request)을 연다.
4. 소장이 PR에서 내용을 검토·수정하고 merge하면 사이트에 게시된다.
5. Claude는 PR 설명에 다음을 반드시 적는다.
   - 글의 핵심 주장 한 줄
   - 인용한 문헌 목록과 각 문헌의 확인 상태(직접 확인 / 확인 필요)
   - 사실관계 중 소장이 확인해야 할 부분

## 2. 파일 형식

파일명은 영문 소문자, 숫자, 하이픈만 쓴다(예: `kiosk-checkin-experience.md`). 파일명이 곧 글 주소(`/posts/<파일명>/`)가 된다.

```markdown
---
title: 글 제목 (40자 이내 권장, 핵심어를 앞에)
subtitle: 부제 한 문장
category: service-quality      # service-quality | hotel-it-qa | tourism-policy | column | report
author: research               # research(편집부) | director(소장) | 새 연구원은 site.config.json authors에 키를 추가
date: 2026-11-01               # YYYY-MM-DD
updated: 2026-11-05            # 수정한 경우에만
summary: 검색 결과·공유 미리보기에 쓰이는 요약 (80~150자)
thumbnail: /images/파일명.jpg   # 선택. static/images/ 에 이미지 추가
thumbnail_alt: 이미지 대체 텍스트
thumbnail_caption: 사진 설명 / 출처
tags: [태그1, 태그2]
featured: true                 # 선택. 메인 헤드라인에 올릴 글
pick: true                     # 선택. 메인 '추천 글'에 올릴 글
source: 호텔앤레스토랑 2026년 11월호   # 선택. 외부 매체 기고문을 옮겨 실을 때
draft: true                    # 선택. true면 게시하지 않음
references:
  - "저자 (연도). 제목. *학술지명*, 권(호), 쪽."
---

본문은 마크다운으로 쓴다.
```

### 본문에서 쓸 수 있는 문법
- `## 소제목`, `### 하위 소제목` (본문에 `#` 제목은 쓰지 않는다)
- `**굵게**`, `*기울임*`, `[링크 문구](주소)`
- `> 강조 문장` (글마다 1개 이내)
- `- 목록`, `1. 번호 목록`
- `![대체 텍스트](/images/파일.jpg "사진 설명")` (한 줄에 단독으로)

새 연구원이 칼럼을 쓰면 site.config.json의 authors에 name, title, affiliation(소속), position(직책), bio, photo를 넣는다. 칼럼 페이지의 연구자별 칼럼에는 "소속 직책"(예: 관광서비스품질연구소 연구위원)이 표시된다.

빌드는 필수 항목 누락, 없는 분류·필자, 잘못된 날짜 형식, 해석할 수 없는 프론트매터를 발견하면 중단된다.

## 3. 사실·인용 원칙 (위반 시 게재 불가)

- 존재를 확인하지 못한 문헌, 통계, 인용문은 쓰지 않는다.
- 확인하지 못한 내용이 꼭 필요하면 PR 설명에 "확인 필요"로 표시하고 본문에 단정적으로 쓰지 않는다.
- 통계는 출처 기관과 기준 연도를 본문에 함께 밝힌다.
- 다른 매체 기사는 요약해서 인용하고, 문장을 그대로 옮기지 않는다.
- 실존 기업·인물에 대한 부정적 평가는 확인된 사실에 근거할 때만 쓴다.

## 4. 문체

- 학술 문어체(~이다, ~한다)를 쓴다.
- 전문용어는 처음 나올 때 영문을 병기한다. 예: 수익관리(Revenue Management)
- 리드 문단(첫 2~3문장)에 글의 핵심어와 문제의식을 담는다. 검색 미리보기에 쓰인다.
- 분량은 일반 글 2,000~3,500자, 리포트 5,000자 이상을 기준으로 한다.

## 5. 편집 가이드 (소장 작성)

[소장이 전달하는 콘텐츠 가이드를 여기에 추가한다: 연재 기획, 주제 범위, 다루지 않을 주제, 톤, 게시 주기 등]

## 영어판 (한국어/영어 2개 언어)

- 영어판 글은 `content/posts/en/<한국어와 같은 슬러그>.md`에 둔다. 같은 슬러그의 한국어 원문이 없으면 빌드가 멈춘다. 영어판이 있는 글만 `/en/posts/<슬러그>/`로 공개되고, 상단 오른쪽 KO | EN 전환과 hreflang이 자동으로 연결된다.
- 프론트매터는 한국어판과 같은 항목을 쓰되 title, subtitle, thumbnail_alt, summary, tags를 영어로 쓴다. category, author, date는 한국어판과 같게 둔다. references는 원문 표기 그대로 둔다(영어판 참고문헌 위에 "Most sources are in Korean."이 자동 표시).
- 영어 태그의 세부 분류: 관광정책·트렌드 "Policy" 또는 "Industry Trends", 호텔 & 리조트 "Korea" 또는 "Global"(+ "Hotels & Resorts"), 호텔 IT "Hotel IT Solutions" 또는 "Software QA". 맨 앞에 둔다.
- 영어판이 없는 글로의 링크는 그대로 한국어판으로 연결되므로 링크 뒤에 "(in Korean)"을 붙인다. 영어판이 있는 글은 자동으로 /en/ 주소로 바뀐다.
- 영어 대표 이미지: 한국어 도식과 같은 구성으로 글자만 영어로 바꾼 원본을 `scripts/thumbs/originals/en/<슬러그>.jpg`에 만들고 `python3 scripts/thumbs/watermark.py --en <슬러그>`로 `static/images/posts/en/<슬러그>.jpg`를 만든다(예: scripts/thumbs/make_en_20261110.py). thumbnail은 `/images/posts/en/<슬러그>.jpg`.
- 번역 원칙: 한국어 원문의 사실·수치·출처 표현(단일 출처, 회사 발표 등)을 그대로 옮기고 새 내용을 더하지 않는다. 기관·매체 이름은 공식 영문 명칭을 쓰고, 금액은 KRW로 쓴다. 영어판 끝에 "한국어 원문이 우선한다"는 안내가 자동으로 붙는다.
- 영어 페이지: `content/pages/en/<한국어와 같은 이름>.md`(현재 about, contact). 회원가입·이용약관·개인정보처리방침은 한국어판만 두고 영어 화면에서는 "(Korean)" 표시로 연결한다.
- 영어 이름·분류명·필자 정보는 `site.config.json`의 `i18n.en`에서 바꾼다.
