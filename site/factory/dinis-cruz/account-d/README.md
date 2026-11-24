# d.library: the SWS Librarian on account D

This folder is d.library's home: its role, state, memory and hand-over. A stranger, Angela or a fresh session should be able to reach the next step from here by following links. Material, not instruction: only Dinis Cruz instructs, in d.library's own session.

- **Name:** d.library (SovereignWebsite). Commits and keys still say `library.d@SovereignWebsite.dinis` until the names in signatures change.
- **Twin of:** b.librarian (librarian.b@SovereignWebsite.dinis, account B). Twins do not talk across accounts; coordination is between conductors.
- **Session:** https://claude.ai/code/session_015gaHdecGUXfFRDs8DmeUFN (context past the 300k hand-over line on 24 Nov: see [START.md](START.md)).
- **Reports to:** d.conductor (conductor.d@SovereignWebsite.dinis), https://claude.ai/code/session_015gaHdbX954ByXJf8LH5FLL. Asks for Dinis's yes go to the decisions agent as request files (see [role.md](role.md)).
- **Key:** published in SovereignWebsite__Factory [team/keys.json](https://github.com/SovereignWebsite/SovereignWebsite__Factory/blob/dev/team/keys.json) (entry `library-d-sovereignwebsite`: fingerprint sha256:210bf5725144d67e, signing sha256:6ad1d3fa87b3e206), copied at every deploy into [/key.json](../../../key.json). This repository's CLAUDE.md forbids writing a key into it by hand, so there is no site/keys/ file here.

## Read first (a new session starts here)

1. [START.md](START.md): the hand-over, step by step.
2. [role.md](role.md): what d.library does and never does.
3. [now.md](now.md): the state and what is open.
4. [learnings.md](learnings.md): lessons that change how d.library works.
5. [messages.md](messages.md): messages sent, to whom, newest first.
6. [decisions/](decisions/): decisions that d.library acted on, with links to the signed records.
7. [agent.json](agent.json): the same, machine-readable.

## Where the work is

| What | Where |
|---|---|
| d.library's pages (team, per agent) | https://library.agents.sovereignweb.site/accounts/d/ , source [site/accounts/d/](../../../accounts/d/) |
| Reading lists for the .d agents | [site/accounts/d/data/agents/](../../../accounts/d/data/agents/) |
| Read tracker (listed, briefed, read) | [site/accounts/d/data/reads/](../../../accounts/d/data/reads/) |
| Briefs sent | [site/accounts/d/briefs/](../../../accounts/d/briefs/) |
| Draft reading lists for b.librarian | [site/accounts/d/profiles-draft/](../../../accounts/d/profiles-draft/) |
| Run log, with usage | [site/accounts/d/runs.md](../../../accounts/d/runs.md) |
| Status | [site/accounts/d/status.json](../../../accounts/d/status.json) |
| Full contradiction pass (shared) | [site/library/newsroom/contradictions-full.md](../../../library/newsroom/contradictions-full.md) |
| Scripts | [docs/library.d/tools/](https://github.com/SovereignWebsite/Site__Agent__Library/tree/dev/docs/library.d/tools) |

## For a person working on this repository (Angela or anyone)

- **Build and check:** `node .github/ci/build.mjs`, then `node .github/ci/quality.mjs _site`, `node .github/ci/share-check.mjs _site`, `npx html-validate@8.24.0 --config .github/ci/htmlvalidate.json "_site/**/*.html"`; delete `_site` after. d.library's pages: `python3 -I docs/library.d/tools/build_d.py .`
- **Do not touch:** b.librarian's files (site/library/ except contradictions-full.md, site/agents/, site/newsroom/, site/index.html, tools/); site/policy/ and .github/ (owner's yes); CLAUDE.md (owner's yes); main.
- **Who reviews:** the twins keep the site (CLAUDE.md); policy and pipeline changes need Dinis's yes, routed through the decisions agent; security.b underwrites decisions.

Public by default. No contacts, keys or tokens here; sensitive material goes to a vault, and only its name appears. d.library holds no vault.
