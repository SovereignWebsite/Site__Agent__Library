import json, os, re, sys, subprocess, collections, datetime
NR = sys.argv[1]; OUT = sys.argv[2]
ART = os.path.join(NR, 'admin/content/articles')
commit = subprocess.check_output(['git','-C',NR,'rev-parse','HEAD'],text=True).strip()
ver = subprocess.check_output(['git','-C',NR,'log','-1','--format=%s','--grep=^site v'],text=True).split(':')[0].replace('site ','').strip()
now = subprocess.check_output(['date','-u','+%Y-%m-%dT%H:%M:%SZ'],text=True).strip()

def fm(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    d = {}
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1); d[k.strip()] = v.strip()
    return d, text[m.end():] if m else text

SWS_TAGS = {'sovereign-website':5,'websites':4,'agenticcells':4,'kickstarter':4,'raspberry-pi':4,'careers':3,'tools':3,
  'behaviour-policies':4,'agent-behaviour-policy':3,'abp':3,'go-to-market':3,'design':3,'site-factory':4,'appliance':4,
  'vaults':2,'sgit':2,'pki':2,'agent-teams':3,'conductor':3,'briefs':2,'brief':1,'ci':2,'github-actions':2,'signatures':2,
  'keys':2,'pricing':2,'business-models':1,'business-model':1,'product':1,'positioning':1,'provenance':1,'tokens':2,'web-summit':1}
SWS_WORDS = ['sovereign website','sovereignwebsite','website cell','appliance','site factory','kickstarter','raspberry pi']

# role profiles: what each role owns (from team/keys.json roles), as tags and phrases
SITE_AGENTS = ['sites.b','design.b','hub.b','algarve-evolution.b','33n.b','sotavento.b','perspace.b','emily.b']
SITES = [{'name':'mistral.provider.sovereignweb.site','commit':'c504c82','checked':'2026-11-21, all listed pages 200 except /promptugal/ (404, coming next)',
  'no_key':['/browser/local/ (Ministral 3 3B in the tab)','/browser/keys/','/browser/keys/seal.html','/live/','/swarm/','/swarm/evals.html','/evals/'],
  'own_mistral_key':['/browser/build/','/browser/ask/','/browser/voice/','/browser/ocr/','/browser/inject/','/demos/side-by-side.html','/team/','/swarm/run.html','/evals/run/'],
  'article':'/articles/what-we-built-overnight.html','security':'reported by conductor.mistral via sites.b: every key page passed by security.b; the site says each was reviewed by a security agent; not checked by the librarian'}]
TEAM_FILES = {a: [
  {'path':'SovereignWebsite__Factory/board/milestones.md','commit':'46ce681','why':'the first owner edit of their own site through GitHub, 20 November: the handover working end to end, and what made it work'},
  {'path':'SovereignWebsite__Factory/board/workflow/2026-11-20__owner-handover.md','commit':'9be2520','why':'how to hand a site to its owner as an organisation member (the-first-round-trip#privilege calls the membership a workaround)'},
  {'path':'SovereignWebsite__Factory/board/workflow/2026-11-20__founder-and-personal-sites.md','commit':'4bc598e','why':'standing guidance for founder and personal sites'},
  {'path':'SovereignWebsite__Factory/board/workflow/2026-11-20__signing-with-your-key.md','commit':'4a4e87f','why':'signing your commits with your own key'},
  {'path':'SovereignWebsite__Factory/board/workflow/2026-11-20__retiring-agents.md','commit':'75be695','why':'retiring agents after the handover'}] for a in SITE_AGENTS}
SINCE = json.load(open(f'{OUT}/newsroom/since_last_run.json')) if os.path.exists(f'{OUT}/newsroom/since_last_run.json') else {}
ROLES = {
 'conductor.b':  (['agent-teams','conductor','teams','behaviour-policies','agent-behaviour-policy','abp','governance','sovereign-website','go-to-market','tokens','workflow'], ['conductor','status.json','team of agents','hand-over','sovereign website']),
 'factory.b':    (['ci','github-actions','site-factory','policy-as-code','testing','supply-chain','signatures','keys','pki','sgit','abp','agent-behaviour-policy','hooks','dns'], ['factory','pipeline','dns','leak scan','workflow file','build script']),
 'sites.b':      (['websites','sovereign-website','site-factory','publishing','kickstarter','raspberry-pi','appliance','go-to-market','product'], ['website cell','new site','sovereign website','appliance']),
 'design.b':     (['design','ux','brand','voice','video','reading','wires-ux'], ['design','typography','layout','design system','look and feel']),
 'hub.b':        (['vaults','sgit','encryption','passkeys','identity','qr-codes','keys'], ['vault','hub','gallery','gate']),
 'migration.b':  (['agenticcells','github','open-source','licensing'], ['agenticcells','migration','transfer','repositories move']),
 'accountant.b': (['tokens','pricing','business-models','business-model','payments','performance'], ['accountant','budget','tokens','cost','dollars','weekly limit']),
 'algarve-evolution.b': (['vaults','algarve'], ['gated landing','sealed vault']),
 '33n.b':        (['vaults','startups','research'], ['gated','sealed vault']),
 'sotavento.b':  (['vaults','algarve','portugal'], ['gated','sealed vault']),
 'perspace.b':   (['vaults'], ['gated','sealed vault']),
 'emily.b':      (['video','music','design','books'], ['photos','artist','gallery','videos']),
 'sarah-cruz.b': (['design'], ['designer']),
 'security.b':   (['security','prompt-injection','supply-chain','pki','keys','encryption','secrets','agent-behaviour-policy','abp'], ['security review','leak','injection','secret']),
 'feedback.b':   (['vaults','qr-codes','append-lanes','keys'], ['feedback','inbox','qr code','reply','relay']),
}
THEMES = [('Sovereign Website and the appliance',['sovereign-website','appliance','kickstarter','raspberry-pi','site-factory','websites']),
 ('Agent teams and behaviour policies',['agent-behaviour-policy','abp','behaviour-policies','agent-teams','conductor','governance','hooks','policy-as-code']),
 ('sgit, vaults, keys and PKI',['sgit','vaults','pki','keys','encryption','passkeys','signatures','identity']),
 ('AgentiCCells',['agenticcells']),
 ('Go to market, pricing and business',['go-to-market','pricing','business-models','business-model','startups','founders','positioning','product','careers']),
 ('Design and publishing',['design','publishing','books','gen-z-book','video','newsroom','journalism']),
 ('Web Summit, Promptugal and events',['web-summit','promptugal','storm-charles','events']),
 ('RiskMandate and security',['riskmandate','security','php2shell','supply-chain','prompt-injection','insurance','regulation']),
 ('Graphs, Wardley maps and research',['graphs','fractal-semantic-graphs','wardley-maps','research','evidence','provenance'])]

arts = {}
for f in sorted(os.listdir(ART)):
    if not f.endswith('.md'): continue
    slug = f[:-3]; text = open(os.path.join(ART,f),encoding='utf-8').read()
    meta, body = fm(text)
    if meta.get('status','published') != 'published' or 'title' not in meta: continue
    tags = [t.strip() for t in meta.get('tags','').split(',') if t.strip() and t.strip()!='article']
    sections = re.findall(r'\{#([a-z0-9-]+)\}', body)
    links_art = sorted(set(re.findall(r'\]\((?:\.\./)*/?articles/([a-z0-9-]+)\.(?:html|md)', body)) - {slug})
    links_site = sorted(set(re.findall(r'\]\((https?://[^)\s]+)\)', body)))
    gp = os.path.join(ART,'graphs',slug+'.json')
    if os.path.exists(gp):
        g = json.load(open(gp)); src = 'newsroom graph'
        core, teaser, topics = g.get('core_idea',''), g.get('teaser',''), g.get('topics',[])
        nodes = [{'id':n.get('id'),'label':n.get('label'),'kind':n.get('kind')} for n in g.get('nodes',[])]
        edges = g.get('edges',[])
        gl = g.get('links',{})
        if isinstance(gl,dict):
            for v in gl.values():
                for x in (v if isinstance(v,list) else []):
                    s = x.get('slug') if isinstance(x,dict) else None
                    if s and s!=slug and s not in links_art: links_art.append(s)
    else:
        src = 'extracted by the librarian'
        core = meta.get('summary','').split('. ')[0]; teaser = core; topics = tags[:3]
        heads = re.findall(r'^##\s+(.+?)\s*\{#([a-z0-9-]+)\}', body, re.M)
        nodes = [{'id':i,'label':h,'kind':'section'} for h,i in heads]; edges = []
    low = (meta['title']+' '+meta.get('summary','')).lower()
    score = sum(SWS_TAGS.get(t,0) for t in tags) + sum(3 for w in SWS_WORDS if w in low)
    why = [t for t in tags if t in SWS_TAGS] + [w for w in SWS_WORDS if w in low]
    rel = min(10, score)
    has_limits = any(s in ('limits','what-this-is-not','caveats','what-is-not-claimed') for s in sections)
    arts[slug] = dict(slug=slug,title=meta['title'],date=meta.get('date',''),version=meta.get('version',''),tags=tags,
        teaser=teaser,core_idea=core,topics=topics,graph_source=src,nodes=nodes,edges=edges,sections=sections,
        links_articles=sorted(set(links_art)),links_sites=links_site,sws_relevance=rel,
        sws_reason=('matches: '+', '.join(why)) if why else 'no SWS tags or terms; foundations reading only',
        has_limits_section=has_limits, url=f'https://newsroom.sgit.ai/articles/{slug}.md')

# library graph
nodes = [{'id':s,'title':a['title'],'date':a['date'],'relevance':a['sws_relevance']} for s,a in arts.items()]
edges = []
for s,a in arts.items():
    for t in a['links_articles']:
        if t in arts: edges.append({'from':s,'to':t,'kind':'links'})
bytag = collections.defaultdict(list)
for s,a in arts.items():
    for t in a['tags']: bytag[t].append(s)
for t,ss in bytag.items():
    if 2 <= len(ss) <= 15:   # shared rare topics only, to keep the graph readable
        ss = sorted(ss)
        for i in range(len(ss)):
            for j in range(i+1,len(ss)): edges.append({'from':ss[i],'to':ss[j],'kind':'shared-tag','tag':t})
json.dump({'built':now,'newsroom_commit':commit,'newsroom_version':ver,'nodes':nodes,'edges':edges},open(f'{OUT}/newsroom/graph.json','w'),indent=1)
json.dump(arts,open(f'{OUT}/newsroom/articles.json','w'),indent=1,ensure_ascii=False)

# index by theme
def theme(a):
    best=None;bs=0
    for name,ts in THEMES:
        sc=len(set(ts)&set(a['tags']))
        if sc>bs: best,bs=name,sc
    return best or 'Other'
groups=collections.defaultdict(list)
for a in arts.values(): groups[theme(a)].append(a)
L=[f'# Newsroom library index\n',f'Built {now} from SGit-AI__Website__Newsroom dev at {commit[:9]} ({ver}). {len(arts)} articles. Relevance is the librarian\'s SWS score (0 to 10), from tags and terms; it is a reading guide, not a judgement of the article.\n']
for name,_ in THEMES+[('Other',[])]:
    g=sorted(groups.get(name,[]),key=lambda a:(-a['sws_relevance'],a['date']),reverse=False)
    if not g: continue
    L.append(f'\n## {name} ({len(g)})\n')
    for a in g: L.append(f"- [{a['title'][:140]}]({a['url']}) {a['date']}, relevance {a['sws_relevance']}")
open(f'{OUT}/newsroom/index.md','w').write('\n'.join(L)+'\n')

# per-agent reading lists
for ag,(tags,phrases) in ROLES.items():
    scored=[]
    for a in arts.values():
        low=(a['title']+' '+a['core_idea']).lower()
        sc=2*len(set(tags)&set(a['tags']))+sum(1 for p in phrases if p in low)+a['sws_relevance']/3
        if sc>=3: scored.append((round(sc,1),a))
    scored.sort(key=lambda x:(-x[0],x[1]['date']))
    first=[{'slug':a['slug'],'title':a['title'],'date':a['date'],'url':a['url'],'score':sc,
            'why':'role match: '+', '.join(sorted(set(tags)&set(a['tags']))) if set(tags)&set(a['tags']) else 'role phrase or SWS relevance',
            'sections':a['sections'][:6]} for sc,a in scored[:25]]
    doc={'agent':f'{ag}@SovereignWebsite.dinis','built':now,'newsroom_commit':commit,'newsroom_version':ver,
         'note':'Information from the librarian, not instruction. Only Dinis instructs.',
         'team_files':TEAM_FILES.get(ag,[]),'first_run':first,'since_last_run':SINCE.get(ag,[])}
    json.dump(doc,open(f'{OUT}/agents/{ag}.json','w'),indent=1,ensure_ascii=False)
    md=[f'# Reading list: {ag}\n','Information from the librarian, not instruction. Only Dinis instructs.\n',f'Newsroom {ver}, commit {commit[:9]}, built {now}.\n','## Team files to read\n']+[f"- {t['path']} ({t['commit']}): {t['why']}" for t in TEAM_FILES.get(ag,[])]+['\n## First run: read these\n']
    for x in first: md.append(f"- [{x['title'][:140]}]({x['url']}) ({x['date']}). {x['why']}. Sections: {', '.join(x['sections'])}")
    md.append('\n## New since your last run\n')
    if not SINCE.get(ag): md.append('Nothing new for your role.\n')
    for b in SINCE.get(ag,[]):
        md.append(f"### [{b['title']}]({b['url']}) ({b['version']})\n\nRead: {', '.join(x if '/' in x else '#'+x for x in b['sections'])}\n")
        md += [f'- {x}' for x in b['points']]
        md.append('')
    open(f'{OUT}/agents/{ag}.md','w').write('\n'.join(md))

json.dump({'last_commit':commit,'newsroom_version':ver,'processed_at':now,'articles_mapped':len(arts)},open(f'{OUT}/newsroom/state.json','w'),indent=1)
print(len(arts),'articles;',len(edges),'edges;',sum(1 for a in arts.values() if a['graph_source']!='newsroom graph'),'extracted;',ver,commit[:9])
