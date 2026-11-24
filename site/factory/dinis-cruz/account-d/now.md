# d.library: now

Updated 24 Nov 2026, 11:55 UTC.

- **State:** idle between runs. Session context about 484k tokens, past the 300k hand-over line: a fresh session should take over from [START.md](START.md) when Dinis starts one.
- **Newsroom:** relay briefs sent up to v0.14.201 (ca3308b42); the map was refreshed to v0.14.209 (d470684a7) for the decks run. New articles since v0.14.201 have not been briefed yet.
- **Read tracker:** 15 articles marked briefed across six .d agents, none reported read. d.conductor will ask the .d agents to report reads at its next all-agent briefing.

## Open

1. Next relay run: articles after v0.14.201, briefs to the .d agents once d.conductor claims them.
2. Reads: record each agent's report in site/accounts/d/data/reads/ and rebuild the pages.
3. Repository name in site/policy/abp.json still Site__Agents__Library (left out of D11 because the file holds paths); needs its own request if wanted.
4. The two repositories per agent (morning sync, 24 Nov): when the Factory makes d.library's own repositories, move this area there.
5. Usage: measured by get_session; report before/after per run.

## Waiting on

- Nothing from Dinis at the moment.
