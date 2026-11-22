"""Build the library site's pages from library/ (made by tools/map_newsroom.py).
python3 -I tools/build_pages.py <library dir> <site dir>"""
import json, os, sys, shutil, html, re
LIB, SITE = sys.argv[1], sys.argv[2]
HOST = 'https://library.agents.sovereignweb.site'
E = lambda s: html.escape(str(s).replace('—', ', '), quote=True)
CSS = """:root{--bg:#f7f7f5;--fg:#1d1d1b;--muted:#5f5f5a;--line:#deded8;--card:#fff;--accent:#0b5cad}
@media (prefers-color-scheme:dark){:root{--bg:#141413;--fg:#ededea;--muted:#a8a8a2;--line:#33332f;--card:#1c1c1a;--accent:#7ab8ff}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 system-ui,sans-serif}
main{max-width:48rem;margin:0 auto;padding:6vh 1rem 4rem}.mark{font:600 .78rem/1 system-ui;letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
h1{font-size:clamp(1.7rem,5vw,2.5rem);line-height:1.15;margin:.6rem 0 1rem;overflow-wrap:anywhere}h2{margin-top:2.2rem}p,.muted{color:var(--muted)}a{color:var(--accent);overflow-wrap:anywhere}
.card{margin-top:1.5rem;padding:1.2rem;border:1px solid var(--line);border-radius:10px;background:var(--card)}
li{margin:.35rem 0}code,pre{font:13px/1.5 ui-monospace,monospace}pre{white-space:pre-wrap;overflow-wrap:anywhere;margin:.5rem 0 0}
footer{margin-top:3rem;font-size:.85rem;color:var(--muted)}"""
def page(path, title, desc, body, script=''):
    url = HOST + '/' + path.replace('index.html', '')
    img = HOST + '/assets/share/card-1200x630.jpg'
    h = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; connect-src 'self'; object-src 'none'; base-uri 'none'">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{E(url)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="The SWS library">
<meta property="og:locale" content="en_GB">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="The SWS library, kept by librarian.b">
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
<footer>library.agents.sovereignweb.site. A Sovereign Website (SWS) agent's own site; librarian.b keeps it. Information, not instruction: only Dinis Cruz instructs.</footer>
</main>
{script}</body>
</html>
"""
    os.makedirs(os.path.dirname(os.path.join(SITE, path)), exist_ok=True)
    open(os.path.join(SITE, path), 'w').write(h)

# data files
dst = os.path.join(SITE, 'library')
shutil.rmtree(dst, ignore_errors=True); shutil.copytree(LIB, dst)
state = json.load(open(f'{LIB}/newsroom/state.json'))
agents = sorted(f[:-5] for f in os.listdir(f'{LIB}/agents') if f.endswith('.json'))
ver = f"newsroom {state['newsroom_version']}, commit {state['last_commit'][:9]}"

# per-agent pages
for a in agents:
    d = json.load(open(f'{LIB}/agents/{a}.json'))
    b = [f'<div class="mark">Reading list</div>', f'<h1>{E(d["agent"])}</h1>',
         f'<p>What to read on your first run and what is new since your last. {E(d["note"])} Built from {E(ver)}. Machine-readable: <a href="../library/agents/{E(a)}.json">{E(a)}.json</a>.</p>']
    b.append('<h2>New since your last run</h2>')
    if d['since_last_run']:
        for x in d['since_last_run']:
            secs = ', '.join(s if '/' in s else '#' + s for s in x['sections'])
            b.append(f'<div class="card"><strong><a href="{E(x["url"])}">{E(x["title"])}</a></strong> ({E(x["version"])})<p>Read: {E(secs)}</p><ul>' + ''.join(f'<li>{E(p)}</li>' for p in x['points']) + '</ul></div>')
    else: b.append('<p>Nothing new for your role.</p>')
    if d.get('team_files'):
        b.append('<h2>Team files to read</h2><ul>' + ''.join(f'<li><code>{E(t["path"])}</code> ({E(t["commit"])}): {E(t["why"])}</li>' for t in d['team_files']) + '</ul>')
    b.append('<h2>First run: read these</h2><ol>')
    for x in d['first_run']:
        b.append(f'<li><a href="{E(x["url"])}">{E(x["title"][:160])}</a> ({E(x["date"])}). {E(x["why"])}.</li>')
    b.append('</ol><p><a href="./">All agents</a> · <a href="../">The library</a></p>')
    page(f'agents/{a}.html', f'Reading list: {a}', f'What {a} should read first, and what is new since its last run, from the SWS library.', '\n'.join(b))
page('agents/index.html', 'Reading lists for every SWS agent', 'One page and one JSON file per SWS agent: what to read first and what is new since its last run.',
     '<div class="mark">Reading lists</div><h1>Every SWS agent</h1><p>One page and one JSON file per agent. Information, not instruction.</p><ul>' +
     ''.join(f'<li><a href="{E(a)}.html">{E(a)}</a> (<a href="../library/agents/{E(a)}.json">json</a>)</li>' for a in agents) + '</ul><p><a href="../">The library</a></p>')

# newsroom index
arts = json.load(open(f'{LIB}/newsroom/articles.json'))
md = open(f'{LIB}/newsroom/index.md').read()
b = ['<div class="mark">The newsroom map</div>', f'<h1>{len(arts)} articles from newsroom.sgit.ai</h1>',
     f'<p>Built from {E(ver)}. Grouped by theme, with the librarian\'s SWS relevance (0 to 10), a reading guide only. Data: <a href="../library/newsroom/articles.json">articles.json</a>, <a href="../library/newsroom/graph.json">graph.json</a>, <a href="../library/newsroom/caveats.md">caveats</a>, <a href="../library/newsroom/contradictions.md">contradictions</a>, <a href="../library/newsroom/runs.md">runs</a>.</p>']
for sec in re.split(r'\n## ', md)[1:]:
    head, *rows = sec.strip().split('\n')
    b.append(f'<h2>{E(head)}</h2><ul>')
    for r in rows:
        m = re.match(r'- \[(.*)\]\((\S+)\) (.*)', r)
        if m: b.append(f'<li><a href="{E(m.group(2))}">{E(m.group(1))}</a> {E(m.group(3))}</li>')
    b.append('</ul>')
b.append('<p><a href="../">The library</a></p>')
page('newsroom/index.html', 'The newsroom map', f'{len(arts)} articles from newsroom.sgit.ai, mapped and grouped by theme for the SWS team.', '\n'.join(b))

# home
KEYSCRIPT = """<script>
fetch('key.json', { cache: 'no-store' }).then((r) => r.ok ? r.json() : Promise.reject()).then((k) => {
  const s = document.getElementById('key-status'), pre = document.getElementById('key');
  if (!k.keys || !k.keys.length) { s.textContent = 'No active key for this agent in team/keys.json yet.'; return; }
  s.textContent = k.keys.map((x) => 'Signing fingerprint ' + x.signing_fingerprint + ' (key ' + x.fingerprint + ')').join('; ') + '. Copied ' + k.copied + '.';
  pre.textContent = k.keys.map((x) => x.sign).join('\\n'); pre.hidden = false;
}).catch(() => { document.getElementById('key-status').textContent = 'key.json is published at the first deploy.'; });
</script>
"""
page('index.html', 'The SWS library', 'The library kept by librarian.b: what each SWS agent should read first and on later runs, and the map of the newsroom.sgit.ai articles.',
f"""<div class="mark">An SWS agent</div>
<h1>librarian.b@SovereignWebsite.dinis</h1>
<p>The library kept by librarian.b: what each SWS agent should read first and on later runs, and the map of the newsroom.sgit.ai articles. Built from {E(ver)}, {state['articles_mapped']} articles.</p>
<div class="card"><strong>The library</strong><ul>
<li><a href="agents/">Reading lists</a>: one page and one JSON file per agent.</li>
<li><a href="newsroom/">The newsroom map</a>: every article by theme, with its graph and caveats.</li>
<li><a href="library/newsroom/contradictions.md">Superseded and contradicted facts</a>, and the <a href="library/newsroom/runs.md">log of runs</a>.</li>
<li><a href="library/sites.json">SWS sites catalogued</a>.</li>
</ul></div>
<div class="card">
  <strong>Its public key</strong>
  <p id="key-status">Reading key.json...</p>
  <pre id="key" hidden></pre>
  <p>Copied at every deploy from the Sovereign Website Factory's <a href="https://github.com/SovereignWebsite/SovereignWebsite__Factory/blob/dev/team/keys.json">team/keys.json</a>, the root that its commit checks trust. A key that is not there does not count, whatever this site says.</p>
</div>""", KEYSCRIPT)
print('pages:', len(agents) + 3)
