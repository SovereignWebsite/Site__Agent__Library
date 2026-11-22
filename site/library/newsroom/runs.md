# Librarian runs

## 2026-11-20T13:18:57Z, first run

- Newsroom: SGit-AI__Website__Newsroom dev, up to 8ccc202fd (v0.14.183). Shallow clone, 50 commits.
- Articles mapped: 414 published (the writing guide is not an article). All 414 have a newsroom graph, so none needed extraction.
- Library graph: library/newsroom/graph.json, 5,651 edges (article links, plus shared tags used by 2 to 15 articles).
- Reading lists: library/agents/<agent>.md and .json, 13 agents, 25 articles each, scored by role match plus SWS relevance.
- Briefs sent: none. Held for Dinis's go-ahead; see status.
- Contradictions recorded: 1 (appliance tiers).
- Committed or pushed: nothing. The library repository does not exist yet and I have no signing key.

## 2026-11-20T16:42:24Z, team-file update (no newsroom change)

- From conductor.b's message of 16:43 UTC (information): added board/milestones.md (46ce681) and board/workflow/2026-11-20__owner-handover.md to the reading lists of the 8 site agents. Checked against the Factory on dev.
- Watching: a newsroom article on the first owner handover. None at 8ccc202fd. When one appears, brief the site agents.

## 2026-11-20T20:49:43Z, second run

- Newsroom 8ccc202fd to d0497299f (v0.14.184 to v0.14.186). New: a-european-brain, transcription-for-a-sector, the-first-round-trip. Changed: none. 417 articles mapped.
- Factory reading lists: added founder-and-personal-sites, signing-with-your-key and retiring-agents (board/workflow) to the 8 site agents. conductor.b mentions a "site workflow" file; none under board/workflow/ at 1707b7b.
- Briefs written into library/agents (since_last_run): 8 site agents, factory.b, conductor.b, accountant.b. Not sent: held for Dinis.
- Contradictions: 1 new (owner handover by organisation membership, a workaround per the-first-round-trip#privilege).
- Not done: the new pipeline for library.agents (needs the repository, a key and a push; held).

## 2026-11-20T20:52:54Z, note

- conductor.b, 21:12 UTC (information): agent sites must not copy seed/site-template's pages.yml (it drops the key step). The one to use is seed/agent-template's pages.yml (Factory e50159b), still waiting for Dinis's yes. Nothing was copied or pushed here, so there is nothing to revert. The pipeline item stays held.

## 2026-11-20T21:01:21Z, note

- conductor.b, 21:05 UTC (information): the agent template is in, Factory dev 3d9acd5 and de05b7c, said to be on Dinis's yes. Checked: seed/agent-template/.github/ exists (workflows and ci). Site__Agents__Library now exists (dev 58ccbb8). Not copied or pushed: that needs a go-ahead in this session and a signing key.

## 2026-11-20T23:58:36Z, question answered

- conductor.mistral asked (for Dinis) for every in-browser agent proof of concept. Answer: library/answers/2026-11-20__browser-agent-pocs.md, from the newsroom at 533336255. Reply not sent: held for a go-ahead in this session.
- Newsroom now at v0.14.187 (a correction to the-first-round-trip); not yet re-mapped.

## 2026-11-21T01:54:51Z, question answered

- conductor.mistral asked (for Dinis) about Angelo's and "Sylvie's" visualisations. Answer: library/answers/2026-11-21__agent-visualisations.md. No Sylvie in the newsroom; Silvio Switha is credited. Reply not sent: held.

## 2026-11-21T02:35:03Z, site added

- From conductor.b 02:37 UTC (information): mistral.provider.sovereignweb.site (c504c82). Checked live: listed pages 200, /promptugal/ 404. Catalogued in library/sites.json. Briefs written (not sent) for design.b, sites.b, hub.b, feedback.b, security.b.
- Roster: sarah.b replaced by sarah-cruz.b; security.b and feedback.b added. Not yet profiled: observability.b, startups.b, kate-curtis-evans.b, chiswick-cheese-market.b, design.b.rounds and the Mistral agents.
- library/answers/2026-11-20__browser-agent-pocs.md is now partly out of date: SWS's own in-browser PoCs are on mistral.provider.sovereignweb.site.
- 2026-11-22T00:39:01Z: wrote library/answers/2026-11-22__brief-for-library.d.md for maestro.b (Dinis's request, relayed). Not sent: held.
