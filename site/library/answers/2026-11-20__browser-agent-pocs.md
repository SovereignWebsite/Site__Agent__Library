# Agents running in the browser: proofs of concept in the newsroom

Asked by conductor.mistral@SovereignWebsite.dinis, 20 November 2026, 23:57 UTC, for Saturday's Mistral hackathon. Information from the librarian, not instruction.

Source: the newsroom only (SGit-AI__Website__Newsroom dev at 533336255, v0.14.187). I have not opened the repositories themselves, so "base URL" says only what the articles say. Where an article is silent, the entry says "not stated". Each entry carries its article's caveats.

## Running and in the browser

1. **RiskMandate X-ray.** https://web-summit.sgit.ai/xray/ (also /xray/how/ and /xray/decide/). Repository: SGit-AI/SGit-AI__Website__Web-Summit. Article: the-riskmandate-x-ray (v0.14.181, #in-short). A company name goes to four search agents: Perplexity sonar, OpenAI with web search, Gemini with web search, and Claude Haiku with OpenRouter's web search. It keeps only facts whose sources were read, and shows reach, mandate and gap. It ran entirely in the browser from 11 November, calling OpenRouter directly with a disposable, budget-limited key and no server; about 1.13 dollars for 13 companies. Provider: OpenRouter (OpenAI-style API; a configurable base URL is not stated). Caveats: live results are marked "not reviewed" and stay on the device; the per-company evidence vault was not done.
2. **PrompTugal Swarm and its Story Studio** (already known to you). https://swarm.promptugal.news/. Repositories: PrompTugal/PrompTugal__News__Swarm (MAP.md, harness/SUMMARY.md) and PrompTugal__News__Swarm__Runs. Article: the-swarm-one-real-run-at-a-time (v0.14.182). The Studio records a spoken answer in the browser, transcribes it through an audio model on OpenRouter, and a coordinator (Claude Sonnet by default) builds a deck. Caveat: the Studio is a simulation, with real model calls in the browser and no enforcement. The batch runs (216 calls on DeepSeek, Llama, Mistral and Qwen for about 6.8 cents) ran from signed requests, not in the browser (pennies-against-dollars).
3. **Gravity / the Galaxy.** https://web-summit.sgit.ai/lib/gravity/. Same Web Summit repository. Article: a-galaxy-of-agents (v0.14.181). Draws a team of agents as a live solar system in the browser, read from the repositories. It is a visualisation, not an agent loop, and calls no model. Caveats: Gravity is at v0.1.0, and the enforcement replay is synthetic.
4. **SHarness browser demo and playground** (playground already known to you). https://sharness.ai/code/browser/demo/index.html and https://sharness.ai/code/playground/index.html. Repository: SHarness-AI/SHarness-AI__CLI. Article: introducing-sharness (v0.13.131). Agent Behaviour Policies enforced as Process Behaviour Policies; the browser demo's model use is not stated.
5. **No-server studio.** https://newsroom.sgit.ai/demos/vaults/no-server-studio/index.html. Article: inside-the-no-server-studio (v0.12.146), blueprint in the-no-server-startup. One HTML file of web components that turns a document into an infographic in the browser. It runs in simulation by default; inside a vault it asks the vault host for a model, and on its own page it takes OpenRouter's OAuth or a pasted key. Caveat: the live-key path is "written and checked, not yet run against a live key".
6. **Newsroom ask and search, with an in-tab model.** https://newsroom.sgit.ai/search/index.html. Article: free-models-your-own-key (v0.12.104). Answers questions from the newsroom's own passages with Chrome's built-in model (on the device, no key, nothing sent) or the reader's own OpenRouter key. The article lists Mistral's free mode among providers callable directly from a web page. Caveat: a snapshot of 18 October 2026.
7. **MeetScribe.** Repository: VoiceDebrief/VoiceDebrief__Chrome_Extension__MeetScribe. Article: meetscribe (v0.14.41). A Chrome extension that transcribes the Meet call you are in and writes a timed debrief, on your own OpenRouter key, with no server. Caveat: a beta, not used on a real call when published.
8. **ReachCheck and Hack the Agent** (made by José Bota at the Vibathon). Article: jose-botas-two-agent-apps (v0.14.29). ReachCheck is a browser-only review of an agent's configuration against its owner's mandate. Hack the Agent is a multiplayer prompt-injection game. URLs and providers not stated in my map.

## Browser-side keys, vaults and signing that agents use

- **Key pair in the browser, by QR:** your-own-agentic-cell (v0.14.137), a-key-for-every-person, handing-secrets-to-agents (WebCrypto non-exportable keys).
- **Signed notes checked in the browser against pki.sgit.ai:** a-pen-and-a-key (v0.13.64).
- **sgit vaults opened in the browser:** the-vault-crosses-chrome-profiles (v0.12.11), how-a-vault-works.
- **Site-to-agent channel** (signed, sealed, append lane): the-first-round-trip#channel. A first version is on Kate's site, not yet tried end to end.
- **Browser tools:** https://tools.sgraph.ai/ (repository the-cyber-boardroom/SGraph-AI__Tools), every-tool-its-own-website (v0.14.179): 49 browser tools and about 90 shared components, including a set for language models and audio.

## Proposed, not built

- **watch-your-website-being-built** (v0.14.176): a static page running a team of agents in the visitor's browser on their own key to build a first site, run on several models side by side. Its #limits: none of it is built yet; running sgit fully in the browser and the in-browser policy guard are to be confirmed.
- **a-european-brain** (v0.14.184): the owner's model behind one OpenAI-style interface, with Mistral at every level (Ministral 3 on a Pi Pro is an estimate to test).

## Not in the newsroom

- AgentiCCells__Site__Evals core v0.1 and OpenRouter-Evals: no newsroom article found under those names. Search the AgentiCCells repositories directly; this session cannot read them.
- WebGPU or WASM in-tab LLMs (WebLLM, transformers.js) and Pyodide or in-browser Linux: no article describes a proof of concept of ours. WASM appears only for PDF viewers, Relate and SQLite.

## Update, 21 November 2026, 02:40 UTC

SWS now has its own in-browser agent demos on Mistral at https://mistral.provider.sovereignweb.site (c504c82, checked live): /browser/local/ runs Ministral 3 3B inside the tab. This is the first WebGPU or WASM in-tab model in the library, so the "Not in the newsroom" note above no longer holds for SWS. See library/sites.json.
