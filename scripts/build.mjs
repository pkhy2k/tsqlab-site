// 관광서비스품질연구소 정적 사이트 생성기 (외부 패키지 없음)
// 사용법: node scripts/build.mjs   → dist/ 에 사이트 생성
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const DIST = path.join(ROOT, 'dist');
const cfg = JSON.parse(fs.readFileSync(path.join(ROOT, 'site.config.json'), 'utf8'));
const SITE_URL = cfg.url.replace(/\/$/, '');
const errors = [];

// ---------- 유틸 ----------
const esc = (s = '') => String(s)
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const fmtDate = (d) => (d ? d.replaceAll('-', '.') : '');
// 신규 글 표시: 글 링크에 게시일(data-d)을 달고, 브라우저에서 최근 N일 이내 글에 NEW 표시
const DATE_BY_SLUG = {};
const markNew = (html) => html.replace(/<a ([^>]*?)href="\/posts\/([a-z0-9-]+)\/"/g,
  (m, pre, slug) => (DATE_BY_SLUG[slug] && !/aria-hidden|tabindex="-1"/.test(pre) ? `<a ${pre}href="/posts/${slug}/" data-d="${DATE_BY_SLUG[slug]}"` : m));
const write = (rel, content) => {
  if (rel.endsWith('.html')) content = markNew(content);
  const file = path.join(DIST, rel);
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, content);
};
const copyDir = (src, dest) => {
  if (!fs.existsSync(src)) return;
  fs.mkdirSync(dest, { recursive: true });
  for (const e of fs.readdirSync(src, { withFileTypes: true })) {
    const s = path.join(src, e.name), d = path.join(dest, e.name);
    e.isDirectory() ? copyDir(s, d) : fs.copyFileSync(s, d);
  }
};
const catBySlug = Object.fromEntries(cfg.categories.map((c) => [c.slug, c]));

// ---------- 프론트매터 ----------
function parseValue(v) {
  v = v.trim();
  if (v === 'true') return true;
  if (v === 'false') return false;
  if (v.startsWith('[') && v.endsWith(']')) {
    return v.slice(1, -1).split(',').map((x) => parseValue(x)).filter((x) => x !== '');
  }
  if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) return v.slice(1, -1);
  return v;
}
function parseFrontmatter(src, file) {
  const m = src.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
  if (!m) { errors.push(`${file}: 프론트매터(--- 블록)가 없다`); return { data: {}, body: src }; }
  const data = {};
  let listKey = null;
  for (const line of m[1].split(/\r?\n/)) {
    if (!line.trim() || line.trim().startsWith('#')) continue;
    const item = line.match(/^\s+-\s+(.*)$/);
    if (item && listKey) { data[listKey].push(parseValue(item[1])); continue; }
    const kv = line.match(/^([A-Za-z_][\w-]*):\s*(.*)$/);
    if (!kv) { errors.push(`${file}: 해석할 수 없는 프론트매터 줄 → ${line}`); continue; }
    if (kv[2] === '') { data[kv[1]] = []; listKey = kv[1]; } else { data[kv[1]] = parseValue(kv[2]); listKey = null; }
  }
  return { data, body: m[2] };
}

// ---------- 마크다운(본문용 부분 집합) ----------
function inline(t) {
  t = esc(t);
  const codes = [];
  t = t.replace(/`([^`]+)`/g, (_, c) => `\u0000${codes.push(c) - 1}\u0000`);
  t = t.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, (_, txt, url) => {
    const ext = /^https?:\/\//.test(url) && !url.startsWith(SITE_URL);
    return `<a href="${url}"${ext ? ' target="_blank" rel="noopener"' : ''}>${txt}</a>`;
  });
  t = t.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  t = t.replace(/(^|[^*])\*([^*\s][^*]*)\*/g, '$1<em>$2</em>');
  t = t.replace(/\u0000(\d+)\u0000/g, (_, i) => `<code>${codes[i]}</code>`);
  return t;
}
function markdown(src) {
  const lines = src.replace(/\r/g, '').split('\n');
  const out = [];
  let para = [];
  const flush = () => { if (para.length) { out.push(`<p>${inline(para.join(' '))}</p>`); para = []; } };
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    let m;
    if (!line.trim()) { flush(); continue; }
    if ((m = line.match(/^(#{1,4})\s+(.*)$/))) {
      flush();
      const lv = Math.max(2, m[1].length);
      out.push(`<h${lv}>${inline(m[2])}</h${lv}>`);
    } else if (/^---+\s*$/.test(line)) {
      flush(); out.push('<hr>');
    } else if ((m = line.match(/^!\[([^\]]*)\]\((\S+?)(?:\s+"([^"]*)")?\)\s*$/))) {
      flush();
      out.push(`<figure><img src="${esc(m[2])}" alt="${esc(m[1])}" loading="lazy">${m[3] ? `<figcaption>${inline(m[3])}</figcaption>` : ''}</figure>`);
    } else if (/^>\s?/.test(line)) {
      flush();
      const q = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) q.push(lines[i++].replace(/^>\s?/, ''));
      i--;
      out.push(`<blockquote>${q.map(inline).join('<br>')}</blockquote>`);
    } else if (/^\s*[-*]\s+/.test(line) || /^\s*\d+\.\s+/.test(line)) {
      flush();
      const ordered = /^\s*\d+\./.test(line);
      const re = ordered ? /^\s*\d+\.\s+/ : /^\s*[-*]\s+/;
      const items = [];
      while (i < lines.length && re.test(lines[i])) items.push(lines[i++].replace(re, ''));
      i--;
      const tag = ordered ? 'ol' : 'ul';
      out.push(`<${tag}>${items.map((x) => `<li>${inline(x)}</li>`).join('')}</${tag}>`);
    } else {
      para.push(line.trim());
    }
  }
  flush();
  return out.join('\n');
}
const plain = (md) => md.replace(/!\[[^\]]*\]\([^)]*\)/g, '').replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
  .replace(/[#>*`_-]/g, '').replace(/\s+/g, ' ').trim();

// ---------- 콘텐츠 읽기 ----------
const REQUIRED = ['title', 'category', 'author', 'date'];
function loadPosts() {
  const dir = path.join(ROOT, 'content', 'posts');
  const posts = [];
  for (const f of fs.readdirSync(dir).filter((x) => x.endsWith('.md'))) {
    const { data, body } = parseFrontmatter(fs.readFileSync(path.join(dir, f), 'utf8'), f);
    if (data.draft === true) continue;
    for (const k of REQUIRED) if (!data[k]) errors.push(`${f}: 필수 항목 '${k}'가 없다`);
    if (data.category && !catBySlug[data.category]) errors.push(`${f}: 없는 분류 '${data.category}'`);
    if (data.author && !cfg.authors[data.author]) errors.push(`${f}: 없는 필자 '${data.author}'`);
    if (data.date && !/^\d{4}-\d{2}-\d{2}$/.test(data.date)) errors.push(`${f}: date는 YYYY-MM-DD 형식이어야 한다`);
    const slug = f.replace(/\.md$/, '');
    if (!/^[a-z0-9-]+$/.test(slug)) errors.push(`${f}: 파일명은 영문 소문자·숫자·하이픈만 쓴다`);
    posts.push({
      ...data,
      slug,
      url: `/posts/${slug}/`,
      tags: Array.isArray(data.tags) ? data.tags : [],
      references: Array.isArray(data.references) ? data.references : [],
      html: markdown(body),
      excerpt: data.summary || plain(body).slice(0, 120),
    });
  }
  return posts.sort((a, b) => (b.date || '').localeCompare(a.date || '') || a.slug.localeCompare(b.slug));
}
function loadPages() {
  const dir = path.join(ROOT, 'content', 'pages');
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter((x) => x.endsWith('.md')).map((f) => {
    const { data, body } = parseFrontmatter(fs.readFileSync(path.join(dir, f), 'utf8'), f);
    return { ...data, slug: f.replace(/\.md$/, ''), html: markdown(body) };
  });
}

// ---------- 공통 조각 ----------
// 로고: 아치 + 상승하는 막대 3개 (마지막 막대 주황)
const logo = (size) => `<svg class="logo" width="${size}" height="${Math.round(size * 372 / 380)}" viewBox="130 50 380 372" aria-hidden="true"><path d="M180 397 V210 A140 140 0 0 1 460 210 V397" fill="none" stroke="currentColor" stroke-width="16"/><rect x="137" y="398" width="366" height="16" fill="currentColor"/><rect x="233" y="312" width="47" height="86" fill="currentColor"/><rect x="297" y="265" width="47" height="133" fill="currentColor"/><rect x="360" y="209" width="47" height="189" fill="var(--logo-orange)"/></svg>`;
const searchBtn = `<a class="icon-btn" href="/search/" aria-label="글 검색"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg></a>`;
const navLinks = (active) => cfg.categories.map((c) =>
  `<a href="/category/${c.slug}/"${c.slug === active ? ' class="active" aria-current="page"' : ''}>${esc(c.name)}</a>`).join('') + '<a href="/books/">출판</a>';

function headerHome() {
  const today = new Intl.DateTimeFormat('ko-KR', { dateStyle: 'full', timeZone: 'Asia/Seoul' }).format(new Date());
  return `<header class="topbar"><div class="wrap topbar-in"><span>${today}</span>
<nav aria-label="보조 메뉴"><a href="/about/">연구소 소개</a><a href="/contact/">문의하기</a>${cfg.social.instagram ? `<a href="${esc(cfg.social.instagram)}" target="_blank" rel="noopener">인스타그램</a>` : ''}</nav></div></header>
<div class="wrap masthead"><a href="/" class="brand-lg" aria-label="${esc(cfg.name)} 홈">${logo(52)}<span>${esc(cfg.name)}</span></a><span class="brand-en">${esc(cfg.nameEn)}</span></div>
<nav class="mainnav" aria-label="주 메뉴"><div class="wrap mainnav-in"><div class="nav-left"><a href="/" class="nav-brand" aria-label="${esc(cfg.name)} 홈">${logo(24)}<span>${esc(cfg.name)}</span></a><div class="navlinks">${navLinks()}</div></div>${searchBtn}</div></nav>`;
}
function headerCompact(active) {
  return `<header class="compact"><div class="wrap compact-in"><a href="/" class="brand-sm" aria-label="${esc(cfg.name)} 홈">${logo(34)}<span>${esc(cfg.name)}</span></a>
<nav class="navlinks" aria-label="주 메뉴">${navLinks(active)}${searchBtn}</nav></div></header>`;
}
function footer() {
  const b = cfg.business;
  return `<footer class="site-footer"><div class="wrap footer-in"><div class="footer-info">
<strong>${esc(cfg.name)}</strong>
<span>소장 ${esc(b.director)}${b.email ? ` · 이메일 <a href="mailto:${esc(b.email)}">${esc(b.email)}</a>` : ''}</span>
<span>© ${esc(cfg.name)}. 무단 전재 및 재배포 금지.</span></div>
<nav aria-label="하단 메뉴"><a href="/about/">연구소 소개</a><a href="/terms/">이용약관</a><a href="/privacy/" class="strong">개인정보처리방침</a><a href="/contact/">문의하기</a></nav></div></footer>`;
}
function thumb(p, ratio = 'wide', linked = true) {
  const inner = p.thumbnail
    ? `<img src="${esc(p.thumbnail)}" alt="${esc(p.thumbnail_alt || p.title)}" loading="lazy">`
    : `<span class="ph-label">${esc(catBySlug[p.category]?.name || '')}</span>`;
  const cls = `thumb ${ratio}${p.thumbnail ? '' : ' ph'}`;
  return linked ? `<a href="${p.url}" class="${cls}" tabindex="-1" aria-hidden="true">${inner}</a>` : `<div class="${cls}">${inner}</div>`;
}
const byline = (p) => `${esc(cfg.authors[p.author]?.name || '')} · ${fmtDate(p.date)}`;
const catLabel = (p) => `<a href="/category/${p.category}/" class="cat">${esc(catBySlug[p.category]?.name || '')}</a>`;

function layout({ title, description, pathname, body, ogType = 'website', image, jsonld, noindex }) {
  const fullTitle = title ? `${title} | ${cfg.name}` : cfg.name;
  const canonical = SITE_URL + pathname;
  const img = image ? (image.startsWith('http') ? image : SITE_URL + image) : `${SITE_URL}/images/og-default.png`;
  return `<!doctype html>
<html lang="${cfg.language}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(fullTitle)}</title>
<meta name="description" content="${esc(description || cfg.description)}">
<link rel="canonical" href="${canonical}">
${noindex ? '<meta name="robots" content="noindex">' : ''}
${cfg.verification.naver ? `<meta name="naver-site-verification" content="${esc(cfg.verification.naver)}">` : ''}
${cfg.verification.google ? `<meta name="google-site-verification" content="${esc(cfg.verification.google)}">` : ''}
<meta property="og:type" content="${ogType}">
<meta property="og:site_name" content="${esc(cfg.name)}">
<meta property="og:locale" content="${cfg.locale}">
<meta property="og:title" content="${esc(title || cfg.name)}">
<meta property="og:description" content="${esc(description || cfg.description)}">
<meta property="og:url" content="${canonical}">
<meta property="og:image" content="${esc(img)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" type="application/rss+xml" title="${esc(cfg.name)}" href="${SITE_URL}/rss.xml">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#F7F5F0">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="${esc(cfg.app?.shortName || cfg.name)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=Noto+Serif+KR:wght@600;700&display=swap">
<link rel="stylesheet" href="/assets/style.css">
<style>:root{--accent:${cfg.accent}}</style>
${jsonld ? `<script type="application/ld+json">${JSON.stringify(jsonld).replace(/</g, '\\u003c')}</script>` : ''}
</head>
<body>
<a class="skip" href="#main">본문 바로가기</a>
${body}
${footer()}
<script>(function(){var D=${Number(cfg.newBadgeDays) || 0};if(!D)return;var now=Date.now()+9*36e5,day=864e5;document.querySelectorAll('a[data-d]').forEach(function(a){var t=Date.parse(a.getAttribute('data-d')+'T00:00:00Z');if(isNaN(t))return;var age=Math.floor(now/day)-Math.floor(t/day);if(age<0||age>=D)return;var host=a.querySelector('img')?a.querySelector('span'):a;if(!host)return;var b=document.createElement('span');b.className='new-badge';b.textContent='NEW';b.setAttribute('aria-label','새 글');var tn=host.lastChild;if(tn&&tn.nodeType===3){var m=tn.nodeValue.match(/^([\s\S]*?)(\S+)(\s*)$/);if(m){tn.nodeValue=m[1];var k=document.createElement('span');k.className='nb-keep';k.textContent=m[2];k.appendChild(b);host.appendChild(k);return}}host.appendChild(b)})})();</script>
<script>(function(){var n=document.querySelector('.mainnav,.compact');if(!n)return;var t=n.offsetTop;function f(){n.classList.toggle('stuck',window.scrollY>t)}addEventListener('scroll',f,{passive:true});f()})();</script>
<script>if('serviceWorker' in navigator){addEventListener('load',function(){navigator.serviceWorker.register('/sw.js').catch(function(){})})}</script>
</body>
</html>`;
}


// ---------- 출판 ----------
const cover = (b) => `<div class="book-cover">${b.cover ? `<img src="${esc(b.cover)}" alt="${esc(b.title)} 표지">` : `<span>${esc(b.title)}</span>`}</div>`;
function bookCard(b) {
  const href = b.post || (b.links && b.links[0] ? b.links[0].url : '');
  const inner = `${cover(b)}<strong>${esc(b.title)}</strong><span class="status">${esc(b.status)}${b.date ? ` · ${fmtDate(b.date)}` : ''}</span>`;
  return href ? `<a class="book" href="${esc(href)}">${inner}</a>` : `<div class="book">${inner}</div>`;
}
function bookDetail(b) {
  const meta = [b.author && `저자 ${esc(b.author)}`, b.publisher && esc(b.publisher), b.date && `${fmtDate(b.date)} 출간`, b.pages && esc(b.pages), b.isbn && `ISBN ${esc(b.isbn)}`].filter(Boolean).join(' · ');
  return `<article class="book-detail">${cover(b)}<div class="book-info"><span class="status">${esc(b.status)}</span><h2>${esc(b.title)}</h2>
${meta ? `<p class="meta">${meta}</p>` : ''}${b.summary ? `<p>${esc(b.summary)}</p>` : ''}
<div class="book-actions">${b.post ? `<a class="btn-line" href="${esc(b.post)}">소개 기사 읽기</a>` : ''}${(b.links || []).map((l) => `<a class="btn-solid" href="${esc(l.url)}" target="_blank" rel="noopener">${esc(l.label)}에서 보기</a>`).join('')}</div></div></article>`;
}

// ---------- 페이지 ----------
function pageHome(posts) {
  const lead = posts.find((p) => p.featured === true) || posts[0];
  const rest = posts.filter((p) => p !== lead);
  const side = rest.filter((p) => !['column', 'report'].includes(p.category)).slice(0, 3);
  const sections = cfg.homeSections.map((slug) => {
    const c = catBySlug[slug];
    const list = posts.filter((p) => p.category === slug).slice(0, 4);
    if (!list.length) return `<div class="col"><div class="sec-head"><h2>${esc(c.name)}</h2></div><p class="muted">아직 게시된 글이 없다.</p></div>`;
    const [first, ...others] = list;
    return `<div class="col"><div class="sec-head"><h2>${esc(c.name)}</h2><a href="/category/${slug}/">더보기</a></div>
${thumb(first, 'photo')}<a href="${first.url}" class="item-lg">${esc(first.title)}</a>
${others.map((p) => `<a href="${p.url}" class="item">${esc(p.title)}</a>`).join('')}</div>`;
  }).join('');
  const col = posts.find((p) => p.category === 'column');
  const dir = cfg.authors.director;
  const reports = posts.filter((p) => p.category === 'report').slice(0, 2);
  const picks = (posts.filter((p) => p.pick === true).length ? posts.filter((p) => p.pick === true) : posts).slice(0, 5);
  const body = `${headerHome()}
<main id="main" class="wrap main">
${lead ? `<section class="lead-row" aria-label="주요 기사">
<article class="lead">${thumb(lead, 'wide')}${catLabel(lead)}
<h1><a href="${lead.url}">${esc(lead.title)}</a></h1>
${lead.subtitle ? `<p class="dek">${esc(lead.subtitle)}</p>` : ''}<span class="meta">${byline(lead)}</span></article>
${side.length ? `<div class="side-list">${side.map((p) => `<article>${catLabel(p)}<h2><a href="${p.url}">${esc(p.title)}</a></h2><span class="meta">${byline(p)}</span></article>`).join('')}</div>` : ''}
</section>` : '<p>게시된 글이 없다.</p>'}
<section class="cols" aria-label="분야별 글">${sections}</section>
<section class="column-band" aria-label="${col ? '소장 칼럼' : '소장 소개'}">
<div class="portrait">${dir.photo ? `<img src="${esc(dir.photo)}" alt="${esc(dir.name)} 소장">` : ''}</div>
${col ? `<div class="column-text"><span class="eyebrow">DIRECTOR'S COLUMN</span><h2><a href="${col.url}">${esc(col.title)}</a></h2>
<p>${esc(col.excerpt)}</p><span class="meta-inv">${esc(dir.name)} · ${esc(dir.title)}</span></div>`
  : `<div class="column-text"><span class="eyebrow">DIRECTOR</span><h2><a href="/about/">${esc(dir.name)}</a></h2>
<p>${esc(dir.title)}</p><span class="meta-inv"><a href="/about/" class="inv-link">연구소 소개 보기 ›</a></span></div>`}</section>
<section class="split" aria-label="리포트와 추천 글">
<div class="split-main"><div class="sec-head"><h2>리포트</h2><a href="/category/report/">더보기</a></div>
<div class="reports">${reports.length ? reports.map((p) => `<article class="report"><a class="cover" href="${p.url}" tabindex="-1" aria-hidden="true">${p.cover || p.thumbnail ? `<img src="${esc(p.cover || p.thumbnail)}" alt="">` : '<span>REPORT</span>'}</a>
<div><span class="cat-static">REPORT</span><a href="${p.url}" class="item-lg">${esc(p.title)}</a><span class="meta">${fmtDate(p.date)}</span></div></article>`).join('') : '<p class="muted">리포트를 준비 중이다.</p>'}</div></div>
<div class="split-side"><div class="sec-head"><h2>추천 글</h2></div>
<ol class="ranked">${picks.map((p) => `<li><a href="${p.url}">${esc(p.title)}</a></li>`).join('')}</ol></div>
</section>
<section aria-label="출판"><div class="sec-head"><h2>출판</h2><a href="/books/">전체 보기</a></div>
<div class="books">${cfg.books.map(bookCard).join('')}</div></section>
</main>`;
  return layout({ pathname: '/', body,
    jsonld: { '@context': 'https://schema.org', '@type': 'Organization', name: cfg.name, alternateName: cfg.nameEn, url: SITE_URL + '/', logo: SITE_URL + '/favicon.svg', email: cfg.business.email || undefined } });
}

function pagePost(p, posts) {
  const idx = posts.indexOf(p);
  const newer = posts[idx - 1], older = posts[idx + 1];
  const author = cfg.authors[p.author] || {};
  const related = posts.filter((x) => x !== p && x.category === p.category).slice(0, 3);
  const picks = posts.filter((x) => x !== p).slice(0, 3);
  const body = `${headerCompact(p.category)}
<main id="main" class="wrap article-wrap">
<article class="article">
<nav class="crumb" aria-label="현재 위치"><a href="/">홈</a><span aria-hidden="true">›</span>${catLabel(p)}</nav>
<h1>${esc(p.title)}</h1>
${p.subtitle ? `<p class="dek">${esc(p.subtitle)}</p>` : ''}
<div class="byline"><div><strong>${esc(author.name)}</strong> <span class="muted">${esc(author.title)}</span><br>
<span class="meta">입력 ${fmtDate(p.date)}${p.updated ? ` · 수정 ${fmtDate(p.updated)}` : ''}</span></div>
<div class="share"><button type="button" class="circle" data-copy aria-label="링크 복사"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M10 13a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 11a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/></svg></button>
<button type="button" class="circle" data-share aria-label="공유하기"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.6 13.5l6.8 4M15.4 6.5l-6.8 4"/></svg></button>
<button type="button" class="circle" onclick="window.print()" aria-label="인쇄하기"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 9V3h12v6"/><rect x="3" y="9" width="18" height="8" rx="1"/><path d="M6 14h12v7H6z"/></svg></button>
<span class="toast" role="status" aria-live="polite"></span></div></div>
${p.thumbnail ? `<figure class="hero"><img src="${esc(p.thumbnail)}" alt="${esc(p.thumbnail_alt || p.title)}">${p.thumbnail_caption ? `<figcaption>${esc(p.thumbnail_caption)}</figcaption>` : ''}</figure>` : ''}
<div class="prose">${p.html}</div>
${p.references.length ? `<section class="refs" aria-label="참고문헌"><h2>참고문헌</h2><ol>${p.references.map((r) => `<li>${inline(String(r))}</li>`).join('')}</ol></section>` : ''}
${p.tags.length ? `<div class="tags">${p.tags.map((t) => `<span>#${esc(t)}</span>`).join('')}</div>` : ''}
<section class="author-box" aria-label="필자 소개">${author.photo ? `<img class="author-photo" src="${esc(author.photo)}" alt="${esc(author.name)}">` : ''}<div><strong>${esc(author.name)}</strong><span class="accent-text">${esc(author.title)}</span><p>${esc(author.bio)}</p></div></section>
${p.source ? `<p class="muted small">이 글은 ${inline(String(p.source))}에 처음 게재되었다.</p>` : ''}
<p class="muted small">© ${esc(cfg.name)}. 이 글의 무단 전재 및 재배포를 금지한다.</p>
<nav class="prevnext" aria-label="이전 다음 글">
${older ? `<a href="${older.url}"><span class="muted small">이전 글</span>${esc(older.title)}</a>` : '<span></span>'}
${newer ? `<a href="${newer.url}" class="next"><span class="muted small">다음 글</span>${esc(newer.title)}</a>` : '<span></span>'}
</nav>
</article>
<aside class="aside" aria-label="관련 글">
${related.length ? `<div><div class="sec-head"><h2>같은 분야 글</h2></div>${related.map((x) => `<a class="mini" href="${x.url}">${thumb(x, 'mini', false)}<span>${esc(x.title)}</span></a>`).join('')}</div>` : ''}
${picks.length ? `<div><div class="sec-head"><h2>최신 글</h2></div><ol class="ranked small">${picks.map((x) => `<li><a href="${x.url}">${esc(x.title)}</a></li>`).join('')}</ol></div>` : ''}
<a class="contact-card" href="/contact/"><span class="eyebrow">CONTACT</span><strong>강의·자문·기고 문의</strong><span>문의하기 ›</span></a>
</aside>
</main>
<script>
(function(){var t=document.querySelector('.toast');function say(m){t.textContent=m;setTimeout(function(){t.textContent=''},2000)}
function copy(){navigator.clipboard&&navigator.clipboard.writeText(location.href).then(function(){say('링크를 복사했습니다')},function(){say('복사하지 못했습니다')})}
document.querySelector('[data-copy]').addEventListener('click',copy);
document.querySelector('[data-share]').addEventListener('click',function(){if(navigator.share){navigator.share({title:document.title,url:location.href}).catch(function(){})}else{copy()}});})();
</script>`;
  const image = p.thumbnail || undefined;
  return layout({ title: p.title, description: p.summary || p.subtitle || p.excerpt, pathname: p.url, body, ogType: 'article', image,
    jsonld: {
      '@context': 'https://schema.org', '@type': 'Article', headline: p.title, description: p.summary || p.subtitle || p.excerpt,
      datePublished: `${p.date}T09:00:00+09:00`, dateModified: `${p.updated || p.date}T09:00:00+09:00`,
      author: p.author === 'director' ? { '@type': 'Person', name: author.name, jobTitle: author.title, image: author.photo ? SITE_URL + author.photo : undefined } : { '@type': 'Organization', name: author.name },
      publisher: { '@type': 'Organization', name: cfg.name, logo: { '@type': 'ImageObject', url: SITE_URL + '/favicon.svg' } },
      mainEntityOfPage: SITE_URL + p.url, image: image ? [image.startsWith('http') ? image : SITE_URL + image] : undefined,
      inLanguage: 'ko', articleSection: catBySlug[p.category]?.name, keywords: p.tags.join(', ') || undefined,
    } });
}

function pageCategory(c, posts) {
  const list = posts.filter((p) => p.category === c.slug);
  const body = `${headerCompact(c.slug)}
<main id="main" class="wrap list-wrap"><header class="list-head"><h1>${esc(c.name)}</h1><p class="muted">${esc(c.description)}</p></header>
${list.length ? list.map((p) => `<article class="row">${thumb(p, 'photo')}<div class="row-text">${catLabel(p)}<h2><a href="${p.url}">${esc(p.title)}</a></h2><p>${esc(p.subtitle || p.excerpt)}</p><span class="meta">${byline(p)}</span></div></article>`).join('') : '<p class="muted">아직 게시된 글이 없다.</p>'}
</main>`;
  return layout({ title: c.name, description: c.description, pathname: `/category/${c.slug}/`, body });
}

function pageStatic(pg) {
  const body = `${headerCompact()}<main id="main" class="wrap narrow"><h1 class="page-title">${esc(pg.title)}</h1><div class="prose">${pg.html}</div></main>`;
  return layout({ title: pg.title, description: pg.description, pathname: `/${pg.slug}/`, body });
}

function pageBooks() {
  const body = `${headerCompact()}<main id="main" class="wrap narrow"><h1 class="page-title">출판</h1>
${cfg.books.map(bookDetail).join('')}</main>`;
  return layout({ title: '출판', pathname: '/books/', body });
}

function pageSearch(posts) {
  const index = posts.map((p) => ({ t: p.title, s: p.subtitle || p.excerpt, u: p.url, c: catBySlug[p.category]?.name, d: fmtDate(p.date), k: p.tags.join(' ') }));
  const body = `${headerCompact()}<main id="main" class="wrap narrow"><h1 class="page-title">글 검색</h1>
<label for="q" class="sr">검색어</label><input id="q" type="search" class="search-input" placeholder="제목, 요약, 태그로 검색" autocomplete="off">
<p id="count" class="muted small" role="status" aria-live="polite"></p><div id="results"></div></main>
<script>
var IDX=${JSON.stringify(index).replace(/</g, '\\u003c')};
(function(){var q=document.getElementById('q'),r=document.getElementById('results'),c=document.getElementById('count');
function e(s){return String(s).replace(/[&<>"]/g,function(m){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]})}
function run(){var v=q.value.trim().toLowerCase();var hits=v?IDX.filter(function(x){return (x.t+' '+x.s+' '+x.k).toLowerCase().indexOf(v)>-1}):[];
c.textContent=v?hits.length+'건':'';r.innerHTML=hits.map(function(x){return '<article class="row-plain"><span class="cat-static">'+e(x.c)+'</span><h2><a href="'+e(x.u)+'">'+e(x.t)+'</a></h2><p>'+e(x.s)+'</p><span class="meta">'+e(x.d)+'</span></article>'}).join('')}
q.addEventListener('input',run);var p=new URLSearchParams(location.search).get('q');if(p){q.value=p;run()}})();
</script>`;
  return layout({ title: '글 검색', pathname: '/search/', body, noindex: true });
}

function page404() {
  const body = `${headerCompact()}<main id="main" class="wrap narrow"><h1 class="page-title">페이지를 찾을 수 없습니다</h1><p>주소가 바뀌었거나 삭제된 글입니다. <a href="/">홈으로 이동</a>하거나 <a href="/search/">글을 검색</a>해 보세요.</p></main>`;
  return layout({ title: '페이지를 찾을 수 없음', pathname: '/404.html', body, noindex: true });
}

// ---------- 피드·사이트맵 ----------
function rss(posts) {
  const items = posts.slice(0, 30).map((p) => `<item><title>${esc(p.title)}</title><link>${SITE_URL}${p.url}</link><guid isPermaLink="true">${SITE_URL}${p.url}</guid>
<pubDate>${new Date(`${p.date}T09:00:00+09:00`).toUTCString()}</pubDate><category>${esc(catBySlug[p.category]?.name)}</category><description>${esc(p.summary || p.subtitle || p.excerpt)}</description></item>`).join('\n');
  return `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel><title>${esc(cfg.name)}</title><link>${SITE_URL}/</link><description>${esc(cfg.description)}</description><language>ko</language>
${items}
</channel></rss>`;
}
function sitemap(posts, pages) {
  const urls = [{ loc: '/', mod: posts[0]?.date }, ...cfg.categories.map((c) => ({ loc: `/category/${c.slug}/`, mod: posts.find((p) => p.category === c.slug)?.date })),
    { loc: '/books/' }, ...pages.map((pg) => ({ loc: `/${pg.slug}/` })), ...posts.map((p) => ({ loc: p.url, mod: p.updated || p.date }))];
  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map((u) => `<url><loc>${SITE_URL}${u.loc}</loc>${u.mod ? `<lastmod>${u.mod}</lastmod>` : ''}</url>`).join('\n')}
</urlset>`;
}

// ---------- 실행 ----------
fs.rmSync(DIST, { recursive: true, force: true });
const posts = loadPosts();
posts.forEach((p) => { DATE_BY_SLUG[p.slug || p.url.split('/')[2]] = p.date; });
const pages = loadPages();
if (errors.length) {
  console.error('빌드 중단 — 콘텐츠 오류:\n' + errors.map((e) => ' - ' + e).join('\n'));
  process.exit(1);
}
copyDir(path.join(ROOT, 'static'), DIST);
fs.mkdirSync(path.join(DIST, 'assets'), { recursive: true });
fs.copyFileSync(path.join(ROOT, 'src', 'style.css'), path.join(DIST, 'assets', 'style.css'));
write('index.html', pageHome(posts));
for (const p of posts) write(`posts/${p.slug}/index.html`, pagePost(p, posts));
for (const c of cfg.categories) write(`category/${c.slug}/index.html`, pageCategory(c, posts));
for (const pg of pages) write(`${pg.slug}/index.html`, pageStatic(pg));
write('books/index.html', pageBooks());
write('search/index.html', pageSearch(posts));
write('404.html', page404());
write('rss.xml', rss(posts));
write('sitemap.xml', sitemap(posts, pages));
write('manifest.webmanifest', JSON.stringify({
  name: cfg.app?.name || cfg.name,
  short_name: cfg.app?.shortName || cfg.name,
  description: cfg.description,
  lang: cfg.language,
  start_url: '/',
  scope: '/',
  display: 'standalone',
  background_color: '#F7F5F0',
  theme_color: '#F7F5F0',
  icons: [
    { src: '/icons/icon-192.png', sizes: '192x192', type: 'image/png', purpose: 'any' },
    { src: '/icons/icon-512.png', sizes: '512x512', type: 'image/png', purpose: 'any' },
    { src: '/icons/maskable-512.png', sizes: '512x512', type: 'image/png', purpose: 'maskable' },
    { src: '/icons/maskable-1024.png', sizes: '1024x1024', type: 'image/png', purpose: 'maskable' }
  ]
}, null, 2));
write('robots.txt', `User-agent: *\nAllow: /\nSitemap: ${SITE_URL}/sitemap.xml\n`);
console.log(`빌드 완료: 글 ${posts.length}편, 고정 페이지 ${pages.length}개 → dist/`);
