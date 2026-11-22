# Reading list: hub.d

Information from library.d, not instruction. Only Dinis instructs. Scores come from tags and terms: a reading guide only.

Newsroom v0.14.201, commit ca3308b42; Factory dev 520462b; built 2026-11-22T01:00:29Z by library.d.

## Team files to read

- SovereignWebsite__Factory/CLAUDE.md (520462b): rules for every agent
- SovereignWebsite__Factory/policy/abp.json (520462b): the agent behaviour policy: paths per agent
- SovereignWebsite__Factory/team/keys.json (520462b): every agent, its role and key
- SovereignWebsite__Factory/status.json (520462b): the team, its state and asks
- SovereignWebsite__Factory/board/workflow/2026-11-20__signing-with-your-key.md (520462b): signing commits with your own sgit key
- SovereignWebsite__Factory/board/conductor.d/claims.md (520462b): the .b/.d split (Dinis, 21 Nov ~22:52 UTC) and what each .d agent has claimed
- SovereignWebsite__Factory/board/conductor.d/status.json (520462b): the .d team, its decisions and asks
- SovereignWebsite__Factory/board/workflow/2026-11-20__owner-handover.md (520462b): owner handover

## First run: read these

- [A key for every person: how each person's conductor issues them a key for the team's site, seals what is for them, and how a signed message turns the ](https://newsroom.sgit.ai/articles/a-key-for-every-person.md) (2026-11-04, v0.14.62). role tags: sgit, encryption, keys, pki. Read #in-short, #limits.
- [An inbox only your agents can write to: a conductor publishes one append lane per agent, each lane's token sealed to that agent's own key, so everythi](https://newsroom.sgit.ai/articles/an-inbox-only-your-agents-can-write-to.md) (2026-11-04, v0.14.63). role tags: vaults, sgit, keys, pki. Read #in-short, #limits.
- [No tech stack to maintain: it is not that there is no backend, it is that the only code you own is HTML, CSS and JavaScript, with every other primitiv](https://newsroom.sgit.ai/articles/no-tech-stack-to-maintain.md) (2026-11-03, v0.14.51). role tags: vaults, sgit, passkeys, pki. Read #in-short, #limits.
- [Agents have an identity now: a key pair made in every session, published with its role, so any agent can seal a secret to it, and the piece the cloud ](https://newsroom.sgit.ai/articles/agents-have-an-identity-now.md) (2026-10-29, v0.13.130). role tags: vaults, identity, keys, pki. Read #in-short, #limits.
- [PKI everywhere: from now on every message, secret and handover starts with a signature, and how an agent gets its first key](https://newsroom.sgit.ai/articles/pki-everywhere.md) (2026-10-20, v0.12.155). role tags: sgit, identity, keys, pki. Read #in-short, #limits.
- [A directory of people and their keys: pki.sgit.ai for the people I work with, verified by me first, then by each other, and a link that only counts wh](https://newsroom.sgit.ai/articles/a-directory-of-people-and-keys.md) (2026-10-18, v0.12.114). role tags: sgit, passkeys, identity, pki. Read #in-short, #limits.
- [Handing secrets to agents and browsers: SG/Send's next focus, a key pair where the work runs, one-time drops, and a brief for a site that does only th](https://newsroom.sgit.ai/articles/handing-secrets-to-agents.md) (2026-10-15, v0.12.80). role tags: vaults, sgit, passkeys, pki. Read #in-short, #limits.
- [secrets.sgit.ai on public keys: no more shared keys, eight ways a secret moves, a vault for the private key, and the commercial service it becomes](https://newsroom.sgit.ai/articles/secrets-on-public-keys.md) (2026-10-15, v0.12.65). role tags: vaults, sgit, passkeys, pki. Read #in-short, #limits.
- [A hub for agentic sites: every site AgentiCCells builds in a repository and an sgit vault, served at its own address, and listed on hub.agenticcells.s](https://newsroom.sgit.ai/articles/a-hub-for-agentic-sites.md) (2026-11-15, v0.14.102). role tags: vaults, sgit, hub. Read #in-short, #limits.
- [How a vault works: an encrypted store that acts like a database, where a server that is fully compromised leaks nothing, one mutable file lets every o](https://newsroom.sgit.ai/articles/how-a-vault-works.md) (2026-11-03, v0.14.50). role tags: vaults, sgit, encryption. Read #in-short, #limits.
- [Seven IAM predictions for 2027, checked against an agent team that runs today: where we already are, where we agree, and the two where I would bet the](https://newsroom.sgit.ai/articles/seven-iam-predictions-already-here.md) (2026-10-30, v0.14.5). role tags: passkeys, identity, pki. Read #in-short, #limits.
- [What sgit does that Git does not: ten releases in October, minutes turned into seconds, and an honest map of where Git is still ahead](https://newsroom.sgit.ai/articles/what-sgit-does-that-git-does-not.md) (2026-10-27, v0.13.112). role tags: vaults, sgit, encryption. Read #in-short, #limits.
- [The showroom: what the Sovereign Website hub shows after its first days, 33 live sites from one pipeline, people's portfolios with five designs each, ](https://newsroom.sgit.ai/articles/the-showroom.md) (2026-11-21, v0.14.190). role tags: hub, portfolios. Read #in-short, #limits.
- [investor.sgit.ai: a brief for a website where investors and founders use our tools, not read about them, with the news, contracts as graphs, deal room](https://newsroom.sgit.ai/articles/investor-sgit-ai.md) (2026-10-29, v0.13.130). role tags: vaults, sgit, pki. Read #in-short, #limits.
- [The push is the authorisation: a new agent session publishes its public key to the team repository, that push is how I accept it, and so who can push ](https://newsroom.sgit.ai/articles/the-push-is-the-authorisation.md) (2026-10-28, v0.13.123). role tags: identity, keys, pki. Read #in-short, #limits.

## New since v0.14.187 (librarian.b's last run) that concerns you

- [The showroom: what the Sovereign Website hub shows after its first days, 33 live sites from one pipeline, people's portfolios with five designs each, ](https://newsroom.sgit.ai/articles/the-showroom.md) (v0.14.190). role tags: hub, portfolios. Read #in-short, #limits.
- [A web of trust for careers: everyone with their own keys and their own repository, links that count only when both sides sign them, companies and univ](https://newsroom.sgit.ai/articles/a-web-of-trust-for-careers.md) (v0.14.194). role tags: identity, pki. Read #in-short, #limits.
- [Person Graph: one picture of what we have been building, people and their agents with their own keys and repositories, links that count only both ways](https://newsroom.sgit.ai/articles/person-graph.md) (v0.14.197). role tags: identity. Read #in-short, #limits.
- [The primitives of trust: why a web of trust between people works now when my earlier attempts at a key store did not, a site per person, keys made in ](https://newsroom.sgit.ai/articles/the-primitives-of-trust.md) (v0.14.200). role tags: identity, pki. Read #in-short, #limits.
- [An anonymous profile, vouched for: how someone who needs to leave their job without going public can publish a persona that shows the depth of their w](https://newsroom.sgit.ai/articles/an-anonymous-profile-vouched-for.md) (v0.14.194). role tags: identity. Read #in-short, #limits.
- [LangGraph and us: how the way we build agent pipelines maps to LangChain, LangGraph, LangSmith and the agent testing toolkits, what is the same, what ](https://newsroom.sgit.ai/articles/langgraph-and-us.md) (v0.14.192). role tags: vaults. Read #in-short, #limits.
- [The SGit Server Factory, a brief: an agent and a pipeline that deploy SG/Send and sgit servers the way the site factory makes websites, a request file](https://newsroom.sgit.ai/articles/the-sgit-server-factory.md) (v0.14.191). role tags: sgit. Read #in-short, #limits.
- [Hired as an agentic worker: what a sovereign website offers someone looking for a job, from a better CV that shows the depth of your work, you in acti](https://newsroom.sgit.ai/articles/hired-as-an-agentic-worker.md) (v0.14.191). role phrases: hub, gate, showroom. Read #in-short, #limits.
