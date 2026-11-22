import json, os, re, sys, subprocess, collections
NR, OUT = sys.argv[1], sys.argv[2]
ART = os.path.join(NR, 'admin/content/articles')
git = lambda *a: subprocess.check_output(['git','-C',NR,*a],text=True).strip()
commit = git('rev-parse','--short=9','HEAD')
ver = git('log','-1','--format=%s','--grep=^site v').split(':')[0].replace('site ','').strip()
def fm(t):
    m = re.match(r'^---\n(.*?)\n---\n', t, re.S); d = {}
    if m:
        for l in m.group(1).splitlines():
            if ':' in l: k,v = l.split(':',1); d[k.strip()] = v.strip().strip('"\'')
    return d, t[m.end():] if m else t
def tags(v):
    return [x.strip().strip('"\'') for x in v.strip('[]').split(',') if x.strip()] if v else []
arts = []
for f in sorted(os.listdir(ART)):
    if not f.endswith('.md'): continue
    slug = f[:-3]; t = open(os.path.join(ART,f), encoding='utf-8').read(); d, body = fm(t)
    if not d.get('title'): continue
    secs = re.findall(r'^#+ .*?\{#([\w-]+)\}', body, re.M)
    lim = ''
    m = re.search(r'^(#+) .*?\{#limits\}\s*\n(.*?)(?=^#{1,2} |\Z)', body, re.M|re.S)
    if m: lim = ' '.join(m.group(2).split())[:600]
    g = {}
    gp = os.path.join(ART,'graphs',slug+'.json')
    if os.path.exists(gp):
        try: g = json.load(open(gp))
        except Exception: g = {}
    arts.append({'slug':slug,'title':d.get('title',''),'date':d.get('date',''),'version':d.get('version',''),
      'tags':tags(d.get('tags','')),'sections':secs,'limits':lim,'core_idea':str(g.get('core_idea',''))[:400],
      'links':sorted(set(re.findall(r'/articles/([\w-]+)\.(?:md|html)', body)) - {slug}),'text':body.lower()})
json.dump({'newsroom_commit':commit,'newsroom_version':ver,'count':len(arts),
  'articles':[{k:v for k,v in a.items() if k!='text'} for a in arts]}, open(os.path.join(OUT,'articles.json'),'w'), indent=1)
import pickle; pickle.dump((commit,ver,arts), open(os.path.join(OUT,'arts.pkl'),'wb'))
print(commit, ver, len(arts), 'with limits:', sum(1 for a in arts if a['limits']), 'with graph core:', sum(1 for a in arts if a['core_idea']))
