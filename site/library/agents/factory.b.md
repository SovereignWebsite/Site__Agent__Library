# Reading list: factory.b

Information from the librarian, not instruction. Only Dinis instructs.

Newsroom v0.14.187, commit 533336255, built 2026-11-21T02:35:07Z.

## Team files to read


## First run: read these

- [sgit in a CI pipeline: encrypted, versioned data in and out of GitHub Actions, between its jobs, through write-only lanes, and a key for eve](https://newsroom.sgit.ai/articles/sgit-in-a-ci-pipeline.md) (2026-10-14). role match: ci, github-actions, pki, sgit, supply-chain. Sections: in-short, why, tested, in-out, between, keys
- [From a commit to a live website: a site factory where a request file in a commit makes a CI pipeline create the GitHub repository, the DNS r](https://newsroom.sgit.ai/articles/from-a-commit-to-a-live-website.md) (2026-11-15). role match: ci, dns, github-actions, sgit. Sections: in-short, question, options, request, pipeline, credentials
- [CI behaviour policies: to create one repository and one DNS record per request, our site factory's pipeline holds the power to create, chang](https://newsroom.sgit.ai/articles/ci-behaviour-policies.md) (2026-11-16). role match: abp, ci, github-actions. Sections: in-short, grant, scale, excuse, policy, update
- [A key for every person: how each person's conductor issues them a key for the team's site, seals what is for them, and how a signed message ](https://newsroom.sgit.ai/articles/a-key-for-every-person.md) (2026-11-04). role match: keys, pki, sgit, signatures. Sections: in-short, problem, key, browser, sealed, lane
- [Deploy sgit in your own environment, from a CI pipeline: one Docker image, ciphertext in your own S3 bucket in the region you choose, an acc](https://newsroom.sgit.ai/articles/deploy-sgit-from-ci.md) (2026-11-17). role match: ci, github-actions, sgit. Sections: in-short, why, what, pipeline, steps, package
- [Policies in practice: four places a behaviour policy earns its keep, measured on a real Google key whose reach is five APIs while the featur](https://newsroom.sgit.ai/articles/policies-in-practice.md) (2026-11-19). role match: abp, ci, keys. Sections: in-short, key, factory, requests, fixes, limits
- [A policy for every skill: Sean Turner's natural-language control for agent skills, the behaviour policy behind it, and using models to need ](https://newsroom.sgit.ai/articles/a-policy-for-every-skill.md) (2026-10-14). role match: agent-behaviour-policy, ci, policy-as-code, supply-chain. Sections: in-short, built, dependency, abp, hope, codify
- [An inbox only your agents can write to: a conductor publishes one append lane per agent, each lane's token sealed to that agent's own key, s](https://newsroom.sgit.ai/articles/an-inbox-only-your-agents-can-write-to.md) (2026-11-04). role match: keys, pki, sgit. Sections: in-short, problem, pattern, use, vault-keys, why
- [sgit in GitHub Actions, side by side: a showcase repository and site that runs four ways of moving a vault between jobs on every run, measur](https://newsroom.sgit.ai/articles/sgit-actions-side-by-side.md) (2026-10-14). role match: ci, github-actions, sgit. Sections: in-short, why, lanes, report, measured, budget
- [Attacks rewritten as mandates: 28 supply-chain incidents, the column each one was missing, and why the next maintainer is an agent](https://newsroom.sgit.ai/articles/attacks-rewritten-as-mandates.md) (2026-10-13). role match: agent-behaviour-policy, sgit, supply-chain. Sections: in-short, ledger, reach, barriers, agents, records
- [Cedar and the policy vault: a debrief on the policy language agents are adopting, where our behaviour policies and sgit vaults meet it, and ](https://newsroom.sgit.ai/articles/cedar-and-the-policy-vault.md) (2026-10-14). role match: agent-behaviour-policy, policy-as-code, sgit. Sections: in-short, why, language, crosswalk, today, demo
- [Where a check runs is part of the policy: tests as enforcers of Agent Behaviour Policies, and what moving them out of the agent's environmen](https://newsroom.sgit.ai/articles/where-a-check-runs.md) (2026-10-22). role match: abp, ci, testing. Sections: in-short, idea, today, where, rule, ready
- [The sidecar repository: a second repository the agent cannot write to, which checks every release against the policy, trusts signed checks i](https://newsroom.sgit.ai/articles/the-sidecar-repository.md) (2026-10-22). role match: abp, ci, pki. Sections: in-short, why, holds, does, trust, compromise
- [The site factory works: three AgentiCCells sites made by hand, then one made by a commit in two minutes and thirty-nine seconds, live over h](https://newsroom.sgit.ai/articles/the-site-factory-works.md) (2026-11-16). role match: ci, site-factory. Sections: in-short, story, flow, wardley, setup, unlocks
- [Our companies and UTH: each company, technology and website we have built, mapped to what UAlgTec Heritage needs to build a European Heritag](https://newsroom.sgit.ai/articles/our-companies-and-uth.md) (2026-11-17). role match: abp, sgit. Sections: in-short, why, foundations, abp, teams, checking
- [Your own agentic cell, end to end: how a person asks for a site like the ones we made for Yiheng Wang and Silvio Switha, through a key pair ](https://newsroom.sgit.ai/articles/your-own-agentic-cell.md) (2026-11-17). role match: pki, site-factory. Sections: in-short, why, ask, approve, welcome, vault
- [PKI everywhere: from now on every message, secret and handover starts with a signature, and how an agent gets its first key](https://newsroom.sgit.ai/articles/pki-everywhere.md) (2026-10-20). role match: keys, pki, sgit. Sections: in-short, decision, pki, first, own, issued
- [A pen and a key: a place on every page to mark it, comment on it and tell the newsroom, and a browser key that pki.sgit.ai vouches for, so a](https://newsroom.sgit.ai/articles/a-pen-and-a-key.md) (2026-10-24). role match: keys, pki, signatures. Sections: in-short, chat, ipad, pen, key, login
- [Chainguard, mapped: what it builds, what it publishes, how far up the stack its context goes, and where an open behaviour policy and an encr](https://newsroom.sgit.ai/articles/chainguard-mapped.md) (2026-10-14). role match: agent-behaviour-policy, sgit, supply-chain. Sections: in-short, why, company, builds, publishes, depth
- [Behaviour policies from the checks: 57 checks taken apart into the 8 behaviours they protect, and where each one is actually kept](https://newsroom.sgit.ai/articles/behaviour-policies-from-the-checks.md) (2026-10-21). role match: abp, ci, testing. Sections: in-short, why, method, behaviours, where, boundary
- [Agentics, ready to sell: what we showed at Agentic Engineering Live, who else is selling agentic services and at what price, the engagement ](https://newsroom.sgit.ai/articles/agentics-ready-to-sell.md) (2026-10-16). role match: agent-behaviour-policy, sgit. Sections: in-short, showed, market, gap, path, marketplace
- [The email agentic cell: why connecting Gmail to agents the usual way is a security mess, and the architecture we will build instead, with on](https://newsroom.sgit.ai/articles/the-email-agentic-cell.md) (2026-11-16). role match: abp, pki. Sections: in-short, why, architecture, flows, signed, altitudes
- [The intersection: SGit, SHarness, Agent Behaviour Policies, RiskMandate and AgentiCCells as one stack of separate companies, now with real c](https://newsroom.sgit.ai/articles/the-intersection.md) (2026-11-16). role match: abp, sgit. Sections: in-short, why, foundations, abp, riskmandate, agenticcells
- [One commit, one site, one owner: the small change to the AgentiCCells site factory that unblocked the most, giving a GitHub account access t](https://newsroom.sgit.ai/articles/one-commit-one-site-one-owner.md) (2026-11-18). role match: site-factory. Sections: in-short, before, change, events, handover, small
- [Are hooks the sweet spot? Moving an agent's rules from hope into hooks, rule by rule, until enforcement moves off the machine](https://newsroom.sgit.ai/articles/are-hooks-the-sweet-spot.md) (2026-10-14). role match: agent-behaviour-policy, hooks, policy-as-code. Sections: in-short, question, own, sandbox, layers, chained

## New since your last run

### [The first round trip](https://newsroom.sgit.ai/articles/the-first-round-trip.md) (v0.14.186)

Read: #privilege, #limits

- #privilege calls organisation membership with base permission none a workaround. Check that org as code matches the handover as written.
