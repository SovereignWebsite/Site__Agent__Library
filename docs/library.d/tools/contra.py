import pickle, re, sys, json
S=sys.argv[1]; commit,ver,arts=pickle.load(open(f'{S}/out/arts.pkl','rb'))
slugs={a['slug'] for a in arts}
PAT=re.compile(r'(correction|corrected|supersed\w*|no longer|we were wrong|replaces? (?:the|our)|retract\w*|instead of what we said|this (?:article|piece) (?:was|is) wrong|out of date|outdated|earlier (?:article|piece) said)')
out=[]
for a in arts:
    body=a['text']
    for m in PAT.finditer(body):
        s=max(0,m.start()-220); ctx=' '.join(body[s:m.end()+220].split())
        refs=[x for x in re.findall(r'([a-z0-9]+(?:-[a-z0-9]+){2,})', ctx) if x in slugs and x!=a['slug']]
        out.append({'slug':a['slug'],'version':a['version'],'date':a['date'],'term':m.group(1),'refs':sorted(set(refs)),'ctx':ctx})
json.dump(out,open(f'{S}/out/contra_candidates.json','w'),indent=1)
import collections
c=collections.Counter(o['term'].split()[0] for o in out); print(len(out), c.most_common(10))
ref=[o for o in out if o['refs']]; print('with article refs:', len(ref))
for o in ref[:40]: print('-',o['slug'],o['version'],o['term'],'->',o['refs'])
