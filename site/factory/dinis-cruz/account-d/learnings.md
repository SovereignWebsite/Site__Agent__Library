# d.library: learnings

Newest first.

- **24 Nov.** Real usage comes from get_session, not from counting new work: by 23 Nov the session had re-read about 42M tokens from cache for 92k output tokens. Report the before/after difference per run.
- **24 Nov.** A decision record can sit in a repository other than the one the checklist names (D11's was in Site__Agent__Decisions, not SovereignWebsite__IaC decisions/). Verify it anyway (signature with ssh-keygen -Y verify, namespace sovereignwebsite-decision; commit with git verify-commit and gpg.ssh.program=ssh-keygen) and say where it was.
- **22 Nov.** The site's accessibility check (axe) fails on a page with a meta refresh: the page navigates away mid-check. Use a "moved" notice with a link instead.
- **22 Nov.** A link to a file that only CI creates (key.json) fails the local link check; point to the page that shows it instead.
- **22 Nov.** A stop hook asking to push does not override a promise to hold a push; record the hook and keep the promise.
- **22 Nov.** The sgit signing half has to be written without a passphrase for git to sign; it needs Dinis's yes in the session the first time.
- **22 Nov.** Twins share a repository: write new files only, in the agent's own folder, and never regenerate pages the other twin builds.
