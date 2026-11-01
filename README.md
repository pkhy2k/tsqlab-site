# 관광서비스품질연구소 웹사이트

외부 패키지 없이 Node.js만으로 동작하는 정적 사이트다. 게시물은 `content/posts/`의 마크다운 파일로 관리한다.

## 폴더 구성

| 경로 | 내용 |
|---|---|
| `site.config.json` | 연구소명, 도메인, 사업자 정보, 분류, 필자, 출판 목록 |
| `content/posts/` | 게시물 (파일 1개 = 글 1편) |
| `content/pages/` | 연구소 소개, 문의, 개인정보처리방침, 이용약관 |
| `static/` | 이미지, 파비콘 (그대로 복사됨) |
| `src/style.css` | 디자인 |
| `scripts/build.mjs` | 사이트 생성기 |
| `POSTING.md` | 게시물 작성 규칙 |
| `.pages.yml` | 웹 편집 화면(Pages CMS) 설정 |

## 로컬에서 확인

Node.js 20 이상이 필요하다.

```
npm run preview
```

브라우저에서 http://localhost:4321 을 연다.

## 배포 절차

1. **GitHub 저장소 생성**: 이 폴더 전체를 비공개(private) 저장소로 올린다.
2. **Cloudflare Pages 연결**: Cloudflare 대시보드 > Workers & Pages > 프로젝트 생성 > GitHub 저장소 선택
   - 빌드 명령: `npm run build`
   - 출력 디렉터리: `dist`
3. **도메인 연결**: Cloudflare Pages 프로젝트의 사용자 지정 도메인(Custom domains)에 구매한 도메인을 추가하고 안내에 따라 DNS를 설정한다. HTTPS는 자동 적용된다.
4. **설정 수정**: `site.config.json`의 `url`을 실제 도메인으로, 사업자 정보와 소장 이름을 실제 값으로 바꾼다.
5. **검색 등록**
   - 네이버 서치어드바이저에 사이트를 등록하고, 발급된 확인 코드를 `site.config.json`의 `verification.naver`에 넣는다. 사이트맵(`/sitemap.xml`)과 RSS(`/rss.xml`)를 제출한다.
   - Google Search Console도 같은 방식으로 등록한다(`verification.google`).

`main` 브랜치에 변경이 반영될 때마다 Cloudflare Pages가 자동으로 다시 빌드·배포한다.

## 게시 전 확인 목록

- [ ] `site.config.json`의 `[ ]` 자리표시를 모두 실제 값으로 교체
- [ ] `content/pages/privacy.md`, `terms.md` 작성
- [ ] 소장 사진, 책 표지 등 이미지를 `static/images/`에 추가
- [ ] 예시 게시물 검토 후 유지 또는 삭제
