// 기사별 조회수·반응 수 집계 API
// GET  /api/stats/<slug>                → { views, useful, agree, more }
// POST /api/stats/<slug> {action:"view"}             → 하루 1회 조회 집계 후 수치 반환
// POST /api/stats/<slug> {action:"react", r, delta}  → 반응 +1 / -1 후 수치 반환
// 개인정보: IP·브라우저 정보는 원문을 저장하지 않고, 날마다 바뀌는 무작위 값과 함께 해시한 값만 2일간 보관한다.

const KINDS = ['views', 'useful', 'agree', 'more'];
const REACTIONS = ['useful', 'agree', 'more'];
const json = (data, status = 200) => new Response(JSON.stringify(data), {
  status, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' },
});
const kstDay = (offset = 0) => new Date(Date.now() + 9 * 3600e3 + offset * 864e5).toISOString().slice(0, 10);

async function ensureSchema(db) {
  await db.batch([
    db.prepare('CREATE TABLE IF NOT EXISTS counts (slug TEXT NOT NULL, kind TEXT NOT NULL, n INTEGER NOT NULL DEFAULT 0, PRIMARY KEY (slug, kind))'),
    db.prepare('CREATE TABLE IF NOT EXISTS seen (h TEXT PRIMARY KEY, day TEXT NOT NULL)'),
    db.prepare('CREATE TABLE IF NOT EXISTS salts (day TEXT PRIMARY KEY, s TEXT NOT NULL)'),
  ]);
}

async function read(db, slug) {
  const { results } = await db.prepare('SELECT kind, n FROM counts WHERE slug = ?').bind(slug).all();
  const out = Object.fromEntries(KINDS.map((k) => [k, 0]));
  for (const r of results) if (KINDS.includes(r.kind)) out[r.kind] = r.n;
  return out;
}

async function bump(db, slug, kind, delta) {
  await db.prepare(`INSERT INTO counts (slug, kind, n) VALUES (?1, ?2, MAX(?3, 0))
    ON CONFLICT(slug, kind) DO UPDATE SET n = MAX(n + ?3, 0)`).bind(slug, kind, delta).run();
}

async function dailySalt(db, day) {
  await db.prepare('INSERT OR IGNORE INTO salts (day, s) VALUES (?, ?)').bind(day, crypto.randomUUID() + crypto.randomUUID()).run();
  const row = await db.prepare('SELECT s FROM salts WHERE day = ?').bind(day).first();
  return row.s;
}

async function sha256(text) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, '0')).join('');
}

async function postExists(env, request, slug) {
  if (!env.ASSETS) return true;
  const res = await env.ASSETS.fetch(new URL(`/posts/${slug}/`, request.url));
  return res.status === 200;
}

export async function onRequest({ request, env, params }) {
  const slug = String(params.slug || '');
  if (!/^[a-z0-9-]{1,120}$/.test(slug)) return json({ error: 'bad slug' }, 400);
  if (!env.DB) return json({ error: 'db not bound' }, 503);
  const db = env.DB;
  await ensureSchema(db);

  if (request.method === 'GET') return json(await read(db, slug));
  if (request.method !== 'POST') return json({ error: 'method' }, 405);
  if (!(await postExists(env, request, slug))) return json({ error: 'not found' }, 404);

  let body = {};
  try { body = await request.json(); } catch { return json({ error: 'bad body' }, 400); }

  if (body.action === 'view') {
    const day = kstDay();
    const salt = await dailySalt(db, day);
    const ip = request.headers.get('cf-connecting-ip') || '';
    const ua = request.headers.get('user-agent') || '';
    const h = await sha256(`${salt}|${ip}|${ua}|${slug}`);
    const ins = await db.prepare('INSERT OR IGNORE INTO seen (h, day) VALUES (?, ?)').bind(h, day).run();
    if (ins.meta.changes > 0) await bump(db, slug, 'views', 1);
    // 2일이 지난 해시와 비밀값은 삭제한다.
    const cutoff = kstDay(-1);
    await db.batch([
      db.prepare('DELETE FROM seen WHERE day < ?').bind(cutoff),
      db.prepare('DELETE FROM salts WHERE day < ?').bind(cutoff),
    ]);
    return json(await read(db, slug));
  }

  if (body.action === 'react') {
    const r = String(body.r || '');
    const delta = body.delta === -1 ? -1 : 1;
    if (!REACTIONS.includes(r)) return json({ error: 'bad reaction' }, 400);
    await bump(db, slug, r, delta);
    return json(await read(db, slug));
  }

  return json({ error: 'bad action' }, 400);
}
