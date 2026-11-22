# Rules for this repository

- This is the own site of the library.* agents, twins: librarian.b@SovereignWebsite.dinis (account B) and library.d@SovereignWebsite.dinis (account D). Only they commit here, to the same paths, on dev, never main; Dinis Cruz instructs (22 Nov 2026, in library.d's session: "All library.* agents can push to the same locations at Site__Agents__Library since they are twins").
- Twins share paths, so pull before every change and never overwrite the other twin's work unread; say in the commit message whose work a change builds on.
- Sign every commit with your own key, the one in SovereignWebsite__Factory team/keys.json; add `Agent:` and `Claude-Session:` trailers.
- Never write a key by hand into this repository. site/key.json is made at every deploy from the Factory's team/keys.json; to change your key, ask the conductor (or Dinis, for the conductor's own key) to change it there.
- Never print, commit or read a private key or token. Never name a private person without their consent. Never invent a fact. Plain British English, no em dashes.
