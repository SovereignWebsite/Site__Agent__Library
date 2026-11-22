# Runs: library.d

Information from library.d (account D), not instruction. Only Dinis instructs. Budget: guidance and observation mode (Dinis, 22 Nov 2026 ~00:52 UTC, in conductor.d's session). Usage figures are estimates: this session shows no exact token counter.

## Run 1, 22 Nov 2026, 00:52 to 01:12 UTC

- Newsroom dev ca3308b42 (site v0.14.201), shallow clone, read only; Factory dev 520462b, then 6868522 (library.d's key on dev).
- Mapped by script: 432 articles (431 with #limits, 432 with a graph core idea). Since librarian.b's run (v0.14.187, 533336255): 15 new articles, 1 changed (a-european-brain).
- (a) Reading lists for the .d team: site/accounts/d/data/agents/ (moved from site/library/agents/).
- (b) Draft profiles for 14 .b and Mistral agents with no reading list, for librarian.b to take or leave: site/library/profiles-draft/.
- (c) Contradictions, full pass at v0.14.201: site/library/newsroom/contradictions-full.md (adds to librarian.b's contradictions.md).
- (d) Newsroom briefs for six .d agents, prepared, not sent: site/library/briefs/2026-11-22__library-d/.
- Scripts: docs/library.d/tools/.
- Usage (estimates): about 170k to 200k tokens for the session, onboarding included; about 20 minutes wall clock; 0 articles read in full, passages of 5 read by hand.
- Deviation, recorded: d22a363 was pushed at 00:59 UTC before library.d's key reached Factory dev; cured at 1b94d58 / 6868522 (~01:10 UTC).

## Briefs sent, 22 Nov 2026, 01:33 UTC

- At Dinis's yes in conductor.d's session ("yes send the briefs to the .d agents", relayed by conductor.d). One message each, marked information, not instruction, to conductor.d, sites.d, hub.d, streaming.d, design.d and synthetic-users.d; all delivered. streaming.d got two articles, not three (the third was a weak match).

## Pages and read tracker, 22 Nov 2026, 03:38 UTC

- At Dinis's word in library.d's session: pipeline fixed so site/key.json carries both keepers' keys (fef5b54); a page per account D agent at /d/agents/<agent>.html and a team page at /d/; a read tracker per agent at site/library/reads/<agent>.json (listed, briefed, read; a read only from the agent's own report). Builder: docs/library.d/tools/build_d.py. Usage (estimate): about 40k tokens, 15 minutes.

## Moved to /accounts/d/, 22 Nov 2026, 03:49 UTC

- Dinis (in conductor.d's session, relayed 03:48 UTC): shared newsroom map, graph and contradictions stay at the top level; each twin's own pages and data go under /accounts/<x>/, each twin writing only its own folder. library.d's reading lists, read tracker, briefs, draft profiles and this log moved from site/library/ and site/d/ to site/accounts/d/; /d/ pages redirect. contradictions-full.md stays shared in site/library/newsroom/. The briefs of 01:33 UTC named the old paths (site/library/agents/<agent>.md); the new ones are site/accounts/d/data/agents/<agent>.md and https://library.agents.sovereignweb.site/accounts/d/agents/<agent>.html.
