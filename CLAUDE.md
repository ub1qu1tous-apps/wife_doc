# wife_doc — working rules

Consolidating exam/source materials into one revision doc, organised by school, subject and topic.

## Session log (mandatory)
- **Before doing anything, or when you need a recap, read `SESSION_LOG.md`.** It is the source of truth for what has been done, decisions made, and the current doc version/link.
- After every meaningful step (files received, doc created/updated, decisions taken), append an entry to `SESSION_LOG.md` and commit it.
- Entry format: date, what was done, files touched, doc version, open items.

## Doc versioning (mandatory)
- The consolidated doc carries a version number in its title/header, e.g. `v0.1`, `v0.2`, ...
- Bump the version on every update to the doc: minor (`v0.1` → `v0.2`) for content additions/edits, major (`v0.x` → `v1.0`) for restructures or a "complete" milestone.
- Each version gets a line in the Version history table in `SESSION_LOG.md` (version, date, change summary).

## Layout
- `sources/` — uploaded source materials (kept as-is).
- `SESSION_LOG.md` — running log + version history.
