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

## Review notes (mandatory)
- Every doc in `docs/` gets a companion `<doc name> – Review Notes vX.docx` with the same version: what the doc is and how it was built, assumptions, items for the user to review (tables with a 'Your decision' column), and things to consider.
- Spec lives in `tools/review/<doc>.json`; build with `python3 tools/review_docs.py <spec> docs`. Update it whenever the doc changes.

## Usage limits and long tasks (mandatory)
- **Token / usage rule:** when about 90% of the session's token budget is used, stop at a safe point: commit and push all work, update the "Next session starts here" line at the top of `SESSION_LOG.md`, and ask the user whether to continue. (Claude can't see the plan's usage meter, so this applies to the session budget it can see.)
  - If the user is near or at a plan usage limit and gives the reset time, save everything. In a cloud session, schedule a message (`send_later`) for just after the reset that says to continue from `SESSION_LOG.md`. On the laptop, the user restarts the session after the reset.
- **Long tasks:** before a long task in a cloud session:
  - Write a short "Task in progress" note at the top of `SESSION_LOG.md` (what is done, what is next).
  - Set up an hourly scheduled task bound to this session saying "if the task in progress in SESSION_LOG.md is not finished, continue it".
  - Work in steps and commit + push after each meaningful step, so a usage-limit cut-off loses at most one step.
  - When the limit stops the session, the hourly check-ins fail quietly until the reset, and the first one after the reset continues the task. This repeats until the task is done.
  - When the task is finished, delete the scheduled task and clear the note.
  - On the laptop, the user restarts the session after the reset.
  - Usage resets: weekly on Wednesday 2 pm SGT. The short limit is a rolling window (use the reset time Claude Code shows).
- **Token use:** quality and efficiency come first. Don't cut checks (e.g. looking at rendered previews or test results) just to save tokens. Avoid only waste: long command output nobody needs, re-reading files already in context, repeated full-size images when a close-up of the changed area shows the same thing.

## Layout
- `sources/` — uploaded source materials (kept as-is).
- `SESSION_LOG.md` — running log + version history.
- `docs/` — consolidated docs + their Review Notes. `previews/` — earlier previews. `notes/` — reading notes per school/year. `tools/` — build scripts.
