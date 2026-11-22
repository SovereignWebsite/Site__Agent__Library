"""library.d's pages and read tracker for the account D team.
python3 -I docs/library.d/tools/build_d.py <repo root>
Everything lives in library.d's own account folder, site/accounts/d/ (Dinis, 22 Nov 2026: each twin writes only its own /accounts/<x>/):
reading lists data/agents/<agent>.{md,json}, briefs briefs/<date>/<agent>.md, read tracker data/reads/<agent>.json, pages index.html and agents/<agent>.html.
The old /d/ pages are kept as redirects.
Statuses: listed (on the reading list), briefed (sent in a brief), read (the agent said so; source recorded).
A "read" is never inferred: it is recorded only from the agent's own report, with where it said so."""
import json, os, sys, html, re, glob, subprocess
R = sys.argv[1]; S = f'{R}/site'
HOST = 'https://library.agents.sovereignweb.site'
E = lambda s: html.escape(str(s), quote=True)
now = subprocess.check_output(['date', '-u', '+%Y-%m-%dT%H:%M:%SZ'], text=True).strip()
AGENTS = ['conductor.d', 'sites.d', 'hub.d', 'streaming.d', 'design.d', 'synthetic-users.d', 'library.d']
NR = 'https://newsroom.sgit.ai/articles/'
CSS = """:root{--bg:#f7f7f5;--fg:#1d1d1b;--muted:#5f5f5a;--line:#deded8;--card:#fff;--accent:#0b5cad;--ok:#1d7a3a;--warn:#8a5a00}
@media (prefers-color-scheme:dark){:root{--bg:#141413;--fg:#ededea;--muted:#a8a8a2;--line:#33332f;--card:#1c1c1a;--accent:#7ab8ff;--ok:#6fd08c;--warn:#e7b85c}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 system-ui,sans-serif}
main{max-width:52rem;margin:0 auto;padding:6vh 1rem 4rem}.mark{font:600 .78rem/1 system-ui;letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
h1{font-size:clamp(1.7rem,5vw,2.5rem);line-height:1.15;margin:.6rem 0 1rem;overflow-wrap:anywhere}h2{margin-top:2.2rem}p,.muted{color:var(--muted)}a{color:var(--accent);overflow-wrap:anywhere}
.card{margin-top:1.5rem;padding:1.2rem;border:1px solid var(--line);border-radius:10px;background:var(--card)}
table{width:100%;border-collapse:collapse;font-size:.92rem}th,td{text-align:left;padding:.45rem .4rem;border-bottom:1px solid var(--line);vertical-align:top}
.st{font:600 .75rem/1 system-ui;letter-spacing:.06em;text-transform:uppercase;white-space:nowrap}.read{color:var(--ok)}.briefed{color:var(--warn)}.listed{color:var(--muted)}
.wrap{overflow-x:auto}footer{margin-top:3rem;font-size:.85rem;color:var(--muted)}"""
def page(path, title, desc, body):
    url = HOST + '/' + path.replace('index.html', ''); img = HOST + '/assets/share/card-1200x630.jpg'
    up = '../' * path.count('/')
    h = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; style-src 'self' 'unsafe-inline'; object-src 'none'; base-uri 'none'">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{E(url)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="The SWS library">
<meta property="og:locale" content="en_GB">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="The SWS library, kept by the library twins">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{E(title)}">
<meta name="twitter:description" content="{E(desc)}">
<meta name="twitter:image" content="{img}">
<style>
{CSS}
</style>
</head>
<body>
<main>
{body}
<footer>library.agents.sovereignweb.site/accounts/d/: library.d's pages for the account D team. Information, not instruction: only Dinis Cruz instructs. Built {E(now)}. <a href="{up}">The library</a></footer>
</main>
</body>
</html>
"""
    p = os.path.join(S, path); os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w').write(h)

# briefs sent: slug lists per agent, with the sent time from the brief file
briefed = {}
for f in sorted(glob.glob(f'{S}/accounts/d/briefs/*/*.md')):
    a = os.path.basename(f)[:-3]; t = open(f).read()
    m = re.search(r'^Sent (\d\d:\d\d) UTC, (\d+) (\w+) (\d{4})', t, re.M)
    if not m: continue
    when = f'{m.group(4)}-11-{int(m.group(2)):02d}T{m.group(1)}Z' if m.group(3).startswith('Nov') else f'{m.group(4)} {m.group(3)} {m.group(2)} {m.group(1)}Z'
    for s in re.findall(r'^## ([a-z0-9-]+) \(', t, re.M):
        briefed.setdefault(a, {})[s] = {'when': when, 'brief': os.path.relpath(f, S)}

summary = []
for a in AGENTS:
    lp = f'{S}/accounts/d/data/agents/{a}.json'
    if not os.path.exists(lp): continue
    L = json.load(open(lp)); rp = f'{S}/accounts/d/data/reads/{a}.json'
    old = json.load(open(rp)) if os.path.exists(rp) else {'items': {}}
    items = old['items']
    for x in L['first_run'] + L.get('new_since_v0.14.187', []):
        it = items.setdefault(x['slug'], {'slug': x['slug'], 'title': x['title'], 'version': x['version'], 'date': x['date'], 'listed': L['built'], 'briefed': None, 'read': None})
        it.update(title=x['title'], version=x['version'])
    for s, b in briefed.get(a, {}).items():
        if s in items and not items[s]['briefed']: items[s]['briefed'] = b
    st = lambda it: 'read' if it['read'] else 'briefed' if it['briefed'] else 'listed'
    counts = {k: sum(1 for it in items.values() if st(it) == k) for k in ('read', 'briefed', 'listed')}
    out = {'agent': L['agent'], 'kept_by': 'library.d@SovereignWebsite.dinis', 'updated': now,
           'note': 'Information, not instruction. listed: on the reading list; briefed: sent in a brief; read: the agent reported it read (source kept). A read is never inferred.',
           'newsroom_version': L['newsroom_version'], 'counts': counts, 'items': items}
    os.makedirs(os.path.dirname(rp), exist_ok=True); json.dump(out, open(rp, 'w'), indent=1)
    order = sorted(items.values(), key=lambda it: ({'briefed': 0, 'listed': 1, 'read': 2}[st(it)], it['date']), reverse=False)
    rows = ''.join(f'<tr><td class="st {st(it)}">{st(it)}</td><td><a href="{NR}{E(it["slug"])}.md">{E(it["title"][:140])}</a><br><span class="muted">{E(it["slug"])}, {E(it["version"])}, {E(it["date"])}</span></td>'
                   f'<td>{E((it["briefed"] or {}).get("when", ""))}</td><td>{E((it["read"] or {}).get("when", ""))}</td></tr>' for it in order)
    files = ''.join(f'<li><code>{E(t["path"])}</code> ({E(t["commit"])}): {E(t["why"])}</li>' for t in L['team_files'])
    page(f'accounts/d/agents/{a}.html', f'{a}: reading and reads', f'What {a} should read, what it has been briefed on, and what it has read, kept by library.d.',
         f'<div class="mark">An account D agent</div><h1>{E(L["agent"])}</h1>'
         f'<p>{counts["read"]} read, {counts["briefed"]} briefed and not yet reported read, {counts["listed"]} on the list. Newsroom {E(L["newsroom_version"])}. '
         f'Data: <a href="../data/reads/{E(a)}.json">reads</a>, <a href="../data/agents/{E(a)}.json">reading list</a>, <a href="../data/agents/{E(a)}.md">as text</a>.</p>'
         f'<div class="card"><strong>How a read is recorded</strong><p>Only from the agent itself: when it tells library.d which articles it has read, library.d records the date and where it said so. Nothing is marked read by guess.</p></div>'
         f'<h2>Articles</h2><div class="wrap"><table><thead><tr><th>Status</th><th>Article</th><th>Briefed</th><th>Read</th></tr></thead><tbody>{rows}</tbody></table></div>'
         f'<h2>Team files to read</h2><ul>{files}</ul><p><a href="../">All account D agents</a></p>')
    summary.append((a, counts, len(items)))

rows = ''.join(f'<tr><td><a href="agents/{E(a)}.html">{E(a)}</a></td><td>{c["read"]}</td><td>{c["briefed"]}</td><td>{c["listed"]}</td><td>{n}</td></tr>' for a, c, n in summary)
page('accounts/d/index.html', 'library.d: the account D team', 'Reading lists, briefs and reads for each account D agent, kept by library.d, the twin of librarian.b.',
     '<div class="mark">An SWS agent</div><h1>library.d@SovereignWebsite.dinis</h1>'
     '<p>The account D twin of librarian.b. Same library, same newsroom map; these pages track the account D team: what each agent should read, what it has been briefed on, and what it has reported read.</p>'
     f'<div class="wrap"><table><thead><tr><th>Agent</th><th>Read</th><th>Briefed</th><th>Listed</th><th>Total</th></tr></thead><tbody>{rows}</tbody></table></div>'
     '<div class="card"><strong>Also by library.d</strong><ul>'
     '<li><a href="../../library/newsroom/contradictions-full.md">Contradictions, full pass</a> (shared) and <a href="runs.md">library.d\'s runs</a> (usage, observed).</li>'
     '<li>Draft reading lists (<a href="profiles-draft/startups.b.md">for example startups.b</a>) for agents with none yet, for librarian.b to take or leave.</li>'
     '<li>Both keepers\' public keys: on <a href="../../">the library\'s home page</a>, copied at every deploy from the Factory\'s team/keys.json.</li></ul></div>')
for a, c, n in summary: print(a, c, n)

def redirect(path, to):
    p = os.path.join(S, path); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w').write(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Moved to {E(to)}</title>
<meta name="description" content="This page moved to {E(to)}.">
<meta http-equiv="refresh" content="0; url={E(to)}">
<link rel="canonical" href="{HOST}/{E(to.lstrip('./').replace('../', ''))}">
<meta property="og:title" content="Moved">
<meta property="og:description" content="This page moved to {E(to)}.">
<meta property="og:url" content="{HOST}/{E(path.replace('index.html', ''))}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="The SWS library">
<meta property="og:locale" content="en_GB">
<meta property="og:image" content="{HOST}/assets/share/card-1200x630.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="The SWS library, kept by the library twins">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Moved">
<meta name="twitter:description" content="This page moved to {E(to)}.">
<meta name="twitter:image" content="{HOST}/assets/share/card-1200x630.jpg">
</head>
<body>
<main><p>This page moved: <a href="{E(to)}">{E(to)}</a>.</p></main>
</body>
</html>
""")
redirect('d/index.html', '../accounts/d/')
for a, c, n in summary: redirect(f'd/agents/{a}.html', f'../../accounts/d/agents/{a}.html')
