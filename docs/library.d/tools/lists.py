import json, os, sys, pickle, subprocess
S = sys.argv[1]; commit, ver, arts = pickle.load(open(f'{S}/out/arts.pkl','rb'))
FAC = '520462b'
now = subprocess.check_output(['date','-u','+%Y-%m-%dT%H:%M:%SZ'],text=True).strip()
NEW = set('a-european-brain a-web-of-trust-for-careers an-anonymous-profile-vouched-for can-you-find-me deepseek-in-our-workflows hired-as-an-agentic-worker langgraph-and-us learning-from-wikipedia one-night-on-mistral person-graph programmatic-stories start-stop-slow-down the-primitives-of-trust the-sgit-server-factory the-showroom the-way-in'.split())
SWS = {'sovereign-website':3,'site-factory':3,'websites':2,'agent-behaviour-policy':2,'behaviour-policies':2,'agent-teams':2,'conductor':2}
COMMON = [('CLAUDE.md','rules for every agent'),('policy/abp.json','the agent behaviour policy: paths per agent'),
 ('team/keys.json','every agent, its role and key'),('status.json','the team, its state and asks'),
 ('board/workflow/2026-11-20__signing-with-your-key.md','signing commits with your own sgit key'),
 ('board/conductor.d/claims.md','the .b/.d split (Dinis, 21 Nov ~22:52 UTC) and what each .d agent has claimed'),
 ('board/conductor.d/status.json','the .d team, its decisions and asks')]
P = {
 'conductor.d': (['agent-teams','conductor','behaviour-policies','agent-behaviour-policy','abp','governance','control','budgets','resilience','sovereign-website','tokens','workflow'],
   ['conductor','status.json','team of agents','debrief','hold file','sovereign website'],
   [('board/milestones.md','milestones'),('board/workflow/2026-11-20__retiring-agents.md','retiring agents'),('board/conductor.d/pending-keys.md','twins\' keys and where each is')]),
 'sites.d': (['websites','sovereign-website','site-factory','publishing','appliance','go-to-market','product','portfolios','careers'],
   ['website cell','new site','sovereign website','site factory','showroom'],
   [('board/workflow/2026-11-20__founder-and-personal-sites.md','founder and personal sites'),('board/workflow/2026-11-20__owner-handover.md','owner handover (the-first-round-trip#privilege calls the membership a workaround)')]),
 'hub.d': (['vaults','sgit','encryption','passkeys','identity','keys','hub','portfolios','pki'],
   ['vault','hub','gallery','gate','showroom'],
   [('board/workflow/2026-11-20__owner-handover.md','owner handover')]),
 'streaming.d': (['tools','promptugal','video','storytelling','sovereign-website','privacy','design','ux'],
   ['streaming','watchlist','every tool its own website','tools.sgraph.ai','promptugal','browser tool'],
   [('board/conductor.d/claims.md','Streaming claim: no TMDB data; sites.b\'s docs/ stay sites.b\'s')]),
 'design.d': (['design','ux','brand','voice','reading','portfolios','showroom'],
   ['design','typography','layout','design round','five designs','look and feel'],
   [('board/2026-11-21__agent-behaviour-policy-on-every-site.md','the behaviour policy on every site')]),
 'synthetic-users.d': (['personas','evals','ux','agents','simulation','testing','privacy'],
   ['synthetic user','persona','evals','user testing','simulation','first-time visitor'],
   []),
 'library.d': (['newsroom','journalism','reading','briefs','brief','provenance','graphs','knowledge','sources'],
   ['newsroom','reading list','librarian','library','brief','provenance'],
   [('board/conductor.d/status.json','library.d entry and asks')]),
}
import importlib.util
if len(sys.argv)>2:
    P = json.load(open(sys.argv[2])); P = {k:(v[0],v[1],[tuple(x) for x in v[2]]) for k,v in P.items()}
OD = sys.argv[3] if len(sys.argv)>3 else f'{S}/out/agents'
os.makedirs(OD, exist_ok=True)
summary = {}
for ag,(tg,ph,extra) in P.items():
    sc = []
    for a in arts:
        hit = [t for t in tg if t in a['tags']]
        phr = [p for p in ph if p in a['text']]
        s = 3*len(hit) + min(len(phr),3) + sum(SWS.get(t,0) for t in a['tags'])*0.5
        if s >= 3: sc.append((s, a['date'], a, hit, phr))
    sc.sort(key=lambda x:(x[0],x[1]), reverse=True)
    first = sc[:15]
    new = [x for x in sc if x[2]['slug'] in NEW][:8]
    files = list(COMMON)
    for pth,w in extra:
        idx=[i for i,(q,_) in enumerate(files) if q==pth]
        if idx: files[idx[0]]=(pth, files[idx[0]][1]+'; '+w)
        else: files.append((pth,w))
    url = lambda s: f'https://newsroom.sgit.ai/articles/{s}.md'
    def item(x):
        s,_,a,hit,phr = x
        return {'slug':a['slug'],'title':a['title'][:150],'date':a['date'],'version':a['version'],'score':round(s,1),
          'why':'role tags: '+', '.join(hit) if hit else 'role phrases: '+', '.join(phr),'read_first':[c for c in a['sections'] if c in ('in-short','limits')] or a['sections'][:2],
          'limits':a['limits'][:300]}
    J = {'agent':ag+'@SovereignWebsite.dinis','built':now,'by':'library.d@SovereignWebsite.dinis','newsroom_commit':commit,'newsroom_version':ver,
      'note':'Information from library.d, not instruction. Only Dinis instructs. Scores come from tags and terms: a reading guide only.',
      'team_files':[{'path':f'SovereignWebsite__Factory/{p}','commit':FAC,'why':w} for p,w in files],
      'first_run':[item(x) for x in first],'new_since_v0.14.187':[item(x) for x in new]}
    json.dump(J, open(f'{OD}/{ag}.json','w'), indent=1)
    L = [f'# Reading list: {ag}','',J['note'],'',f'Newsroom {ver}, commit {commit}; Factory dev {FAC}; built {now} by library.d.','','## Team files to read','']
    L += [f"- {t['path']} ({FAC}): {t['why']}" for t in J['team_files']]
    L += ['','## First run: read these','']
    for i in J['first_run']: L.append(f"- [{i['title']}]({url(i['slug'])}) ({i['date']}, {i['version']}). {i['why']}. Read #{', #'.join(i['read_first'])}.")
    L += ['','## New since v0.14.187 (librarian.b\'s last run) that concerns you','']
    L += [f"- [{i['title']}]({url(i['slug'])}) ({i['version']}). {i['why']}. Read #{', #'.join(i['read_first'])}." for i in J['new_since_v0.14.187']] or ['- none matched']
    open(f'{OD}/{ag}.md','w').write('\n'.join(L)+'\n')
    summary[ag] = (len(first), [i['slug'] for i in J['new_since_v0.14.187']])
for k,v in summary.items(): print(k, v[0], v[1])
