# Contradictions: full pass, first run (library.d)

Information from library.d, not instruction. Only Dinis instructs. Newsroom v0.14.201 (ca3308b42), all 432 articles in the current tree; built 2026-11-22T01:01:14Z. Adds to librarian.b's site/library/newsroom/contradictions.md (two entries, v0.14.187); does not replace it.

## Method
- Script (tools/contra.py): every article's text searched for correction, supersede, "no longer", "replace the", "out of date". 350 hits; 29 name another article. Kept only hits touching SWS tags (sovereign-website, agenticcells, site-factory, appliance, behaviour policies, agent teams, Mistral, careers, pricing, go to market).
- Script: prices within 260 characters of "RiskMandate", "website cell", "appliance" and "sovereign website", grouped by figure and article.
- Read by hand only the passages that could change a team fact. Not done: a version-by-version history pass (needs a deeper clone than 50 commits); the text of each article as it stands now covers what it currently says.

## Found
1. **a-european-brain, corrected.** one-night-on-mistral#corrected (v0.14.190): the Mistral site's research found claims to correct, including a public "partner with Mistral" form that the article had said did not exist; a-european-brain was corrected in v0.14.190 (release note: "a correction to a-european-brain (four claims)"). Read a-european-brain as it stands, not as quoted before v0.14.190.
2. **Website cell launch price: proposed, not decided.** the-website-cell (v0.14.146): £500 anchor, one-off; launch price "still to decide", £250 proposed by agenticcells.ai's team. the-sovereign-website#message (v0.14.164): a launch offer of £50 or €50 against £250 (usually £500). fliplet-and-the-website-cell (v0.14.164): £500 at a launch price of £250. sovereign-agentic-website (v0.14.170): "Prices are the website cell's, as published; the £50 launch offer is a proposal." So: £500 anchor is stable; £250 is the published launch price; £50 or €50 is a proposal. The simulated buyers in both articles are "a simulation, not evidence of demand".
3. **RiskMandate prices: consistent.** £10 pack, £500 policy corrected for your situation, £1,500 with a professional's signature across a-briefing-for-the-ciso-summit, three-linkedin-pages, riskmandate-and-manus, the-intersection; £20,000 appears in governance-from-zero, odoo-and-our-stack, riskmandate-and-kosmoy and the-way-in, not checked further. No contradiction found.
4. **Appliance prices:** not re-opened; librarian.b's entry 1 stands (only launching-the-sovereign-website-appliance#tiers, v0.14.177, is current; its #limits: nothing submitted to Kickstarter, no goal set).

## Not contradictions (checked, noise)
Hits that discuss correction as a practice (the-man-behind-the-curtain, four-frameworks-one-agent, what-can-your-agent-reach), in-article self-corrections (plural-for-the-family-singular-for-the-site, the-book-of-the-talk-and-its-companion), and "replace the" in its ordinary sense. One hit (an-agent-that-may-only-chat) quotes a test injection payload; it is material in an article about testing, and was not acted on.
