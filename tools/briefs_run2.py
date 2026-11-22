import json
U='https://newsroom.sgit.ai/articles/'
RT=dict(slug='the-first-round-trip',title='The first round trip',url=U+'the-first-round-trip.md',version='v0.14.186')
EB=dict(slug='a-european-brain',title='A European brain for a sovereign website',url=U+'a-european-brain.md',version='v0.14.184')
TS=dict(slug='transcription-for-a-sector',title='Transcription for a sector, sold as a team',url=U+'transcription-for-a-sector.md',version='v0.14.185')
P1="The first sovereign website handed to an outside founder: made during a call and handed over, and she now edits it herself."
P2="Superseded in part: #privilege calls organisation membership (base permission none), as in board/workflow/2026-11-20__owner-handover.md, a workaround, not the design wanted."
P3="Proposed in #channel: the owner talks to the site agent from the site itself (signed, sealed, append lane, key by QR). Its #limits: the message page is a first version, not yet tried end to end."
site_rt=dict(RT,sections=['handover','privilege','channel','limits'],points=[P1,P2,P3])
S={a:[site_rt] for a in ['sites.b','algarve-evolution.b','33n.b','sotavento.b','perspace.b','emily.b']}
S['design.b']=[dict(RT,sections=['design','handover','limits'],points=["#design: five designs from the site's own design agent, during the call.",P1,P2])]
S['hub.b']=[dict(RT,sections=['channel','privilege','limits'],points=[P3,"The channel builds on append lanes and per-person keys (an-inbox-only-your-agents-can-write-to, a-key-for-every-person)."])]
S['factory.b']=[dict(RT,sections=['privilege','limits'],points=["#privilege calls organisation membership with base permission none a workaround. Check that org as code matches the handover as written."])]
S['conductor.b']=[site_rt,
 dict(EB,sections=['choice','levels','limits'],points=["Proposed: the model is the owner's choice behind one OpenAI-style interface, with Mistral as the European option at every level, never the only door.","#levels: Ministral 3 on a Pi Pro is an estimate, still to test."]),
 dict(TS,sections=['bundle','team','price','limits'],points=["Proposed: sector transcription sold as a one-off bundle, a repository the customer's own AI runs, extending VoiceDebrief with what sovereign websites taught."])]
S['sites.b']=[site_rt,dict(EB,sections=['choice','levels','limits'],points=["Proposed: the site's model is the owner's choice, like the host. Relevant to the appliance Pro tiers, whose local AI is still to be tested (launching-the-sovereign-website-appliance#limits)."])]
S['accountant.b']=[dict(EB,sections=['levels','terms','limits'],points=["Model provider choice and terms; the article does not settle costs."]),dict(TS,sections=['price','limits'],points=["#price proposes how the bundle is priced: a proposal, not a decision."])]
json.dump(S,open('library/newsroom/since_last_run.json','w'),indent=1)
