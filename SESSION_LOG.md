# Session log

**Next session starts here:** read the "Session 1 HANDOFF" entry, then the entries after it.

**Task in progress (session 2):** build docs 2b, 2c, 2d, 2e, 2f (the user said "build all of them"), each with Review Notes. Build them one after another and commit + push after each.
- Done: 2b (v0.8).
- Next: 2c H1 Essay (H1 Q4–Q6), then 2d, 2e, 2f.
- An hourly scheduled check-in (`trig_01GQooXWiM5ucgbmSySZBKG3`, :12 past each hour) is bound to this session. Delete it and clear this note when all five are done.

## Current state
- **Docs (full):** `docs/1 Topic Grid by School (H1 & H2) v0.7.docx` (key-question level), `docs/2a H1 Fieldwork Questions by Topic v0.5.docx`, `docs/2b H1 Structured Questions by Topic v0.8.docx`, each with a `– Review Notes` companion. Still to build: 2c–2f (each with Review Notes). Built one doc at a time. User's local folder follows the branch `claude/amazing-dirac-mpbgn8`.
- **Current version:** v0.8
- **Sources:** `sources/Other JC Prelims 2024|2025|2026/` (JC prelim H1 8834 & H2 9173 papers, inserts, answers) + syllabus PDFs `sources/8834_y26_sy.pdf`, `sources/9173_y26_sy.pdf`.
- **User spec:** see the "user spec received" log entry. Topics per syllabus (`notes/syllabus_topics.md`). Ignore VJC 2026 H1 QP.
- **Reading notes:** `notes/<year>/<SCHOOL>.md` — **all 47 school-years read** (2024: 15, 2025: 15, 2026: 17). 2025/2026 notes carry syllabus-topic lines; 2024 notes still need them (add at build time).

## Version history
| Version | Date | Changes |
|---|---|---|
| v0.8 | 2026-10-21 | **Doc 2b full build**: H1 Structured questions by topic, 82 questions (full wording + 266 diagrams) |
| v0.7 | 2026-10-21 | **Doc 1 rebuilt at syllabus key-question level** (all 716 questions; 38 pages) |
| v0.6 (preview) | 2026-10-21 | Doc 1 preview at syllabus key-question level (ACJC 2024 row) |
| v0.5 | 2026-10-21 | **Doc 2a full build**: H1 Fieldwork questions by topic, 41 questions (full wording + 166 resource images) |
| v0.4 | 2026-10-21 | **Doc 1 full build**: topic grid for all 47 school-years (H1 + H2 tables, 716 questions), syllabus topic only |
| v0.3 (preview) | 2026-10-21 | Fieldwork split out of doc 2: 6 question docs (2a H1 Fieldwork, 2b H1 Structured, 2c H1 Essay, 2d H2 Fieldwork, 2e H2 Structured, 2f H2 Essay) |
| v0.2 (preview) | 2026-10-20 | Grid shows syllabus topic only; fieldwork grouped by area ("Others" for non-syllabus scenarios); new doc 0 "Items to Review" |
| v0.1 (preview) | 2026-10-20 | Previews of doc 1 (topic grid, ACJC 2024 row) and docs 2a–2d (one topic, one ACJC 2024 question each) |

## Log

### 2026-10-20 — Session 1
- Checked repo: only `README.md` present, no source materials yet.
- User request: consolidate uploaded source materials into a doc organised by school, topic, etc.
- Proposed doc structure (see Current state); awaiting user's answers and uploads.
- User asked for: session logs kept and read for recaps, and the doc to be versioned. Set up `CLAUDE.md` (rules), `SESSION_LOG.md` (this file), `sources/` folder.
- Next: receive uploads → read & catalogue sources → create doc v0.1.

### 2026-10-20 — Session 1 (cont.): sources received
- User pushed source materials to `main` (commit `72548c9` "source material"); merged `origin/main` into `claude/amazing-dirac-mpbgn8`.
- Note: files sit at repo root in `Other JC Prelims 2024/`, `Other JC Prelims 2025/2025 Prelims (students)/`, `Other JC Prelims 2026/` (not in `sources/`). Left as-is.
- Subject: **JC Prelim Geography, H1 (8834) & H2**, papers = QP, Insert, Answers (where provided).
- Schools per year:
  - 2024 (15): ACJC, ASRJC, CJC, DHS, EJC, HCI, JPJC, NJC, NYJC, RVHS, SAJC, TJC, TMJC, VJC, YIJC — folders marked "(Ans)" include answers; JPJC & SAJC have none.
  - 2025 (15): ACJC, ASRJC, CJC, DHS, EJC, HCI, JPJC, NJC, NYJC, RVHS, SAJC, TJC, TMJC, VJC, YIJC.
  - 2026 (17): the 2025 schools plus MI and RI.
- Existing consolidated docs from user (2024 only) — the format to follow:
  - `Other JC Prelims H1 (By Topics) 2024.docx`: grid table, rows = schools (incl. SP), columns = SQ1 (GI), SQ2, SQ3, Essay 4–6, cells = short topic labels (e.g. "CC", "Elderly", "Reimaging + SUD").
  - `Other JC Prelims H2 (By Topics) 2024.docx`: same, split Paper 1 (Cluster 1 SQ, Cluster 2 SQ, Essays 3–6) and Paper 2 (SQ1 GI, Cluster 3 SQ, Essays 3–4).
  - `Other JC Prelims 2024 H1/H2 Essays.docx`: per school/paper, screenshots of the essay questions.
- Doc version: none yet.
- Open items: confirm with user the output (replicate 2024 format for 2025 & 2026? combined multi-year doc? Word vs shareable doc).

### 2026-10-20 — Session 1 (cont.): full read-through started
- User instruction: **read everything first; user has not yet specified how they want the consolidation** — do NOT design/build the doc until user says how.
- Extracted text from all files (pdftotext / pandoc / soffice) to scratchpad; bundled per school+year with duplicate (pdf vs docx "for sharing") copies removed → 48 bundles, ~750k words.
- Unreadable: `Other JC Prelims 2026/VJC/2026 JC2 H1 Prelims QP.docx` is **password-protected (encrypted)** — need password or another copy. (VJC 2026 H1 MS/Insert are readable, may contain question text.)
- Inserts: graphs/maps/photos are images; only text/tables/articles are extractable.
- Reading notes go in `notes/<year>/<SCHOOL>.md` (format in `notes/README.md`).
- Read progress (2024): ACJC ✅ ASRJC ✅ | CJC DHS EJC HCI JPJC NJC NYJC RVHS SAJC TJC TMJC VJC YIJC pending. 2025, 2026 pending. (superseded below)

### 2026-10-20 — Session 1 (cont.): 2024 read-through complete
- All 15 schools for 2024 read; notes in `notes/2024/*.md` (every question verbatim with marks, resources, answer-scheme key points, the user's 2024 grid labels for comparison, file issues).
- Findings worth flagging to the user:
  - NJC & RVHS 2024: H2 only (no H1 papers).
  - SAJC 2024: H1 has no answers; H1 R5 says "Kibera, Nigeria" (source error — Kibera is in Kenya).
  - JPJC 2024: mark schemes are present even though folder isn't marked "(Ans)".
  - HCI 2024: H1 and H2 P2 share Q1–Q2; H2 P2 MS Q3 wording differs from QP.
  - EJC 2024 H2 P1: MS essay order differs from QP.
  - TMJC 2024 H2 P2: PDF answers fuller than Word copy.
  - User's 2024 grid often labels H1 SQ1 (fieldwork) as "CC" etc. where the topic differs — noted as [sic] per school.
- Files: `notes/2024/{NYJC,RVHS,SAJC,TJC,TMJC,VJC,YIJC}.md` (added), `SESSION_LOG.md`.
- Doc version: none yet (waiting on user's consolidation spec).
- Read progress: 2024 ✅ all | 2025 pending (15) | 2026 pending (17).

### 2026-10-20 — Session 1 (cont.): 2025 & 2026 read-through in progress
- 32 bundles (15 × 2025, 17 × 2026) split into 9 parallel reading batches; each writes `notes/<year>/<SCHOOL>.md` in the 2024 format, with a "Grid label (suggested)" line per paper instead of the user's grid labels (which only exist for 2024).
- VJC 2026 H1 QP is encrypted, so its questions will be rebuilt from the H1 MS/Insert and flagged.
- Next: review every note, commit, then report to the user and wait for the consolidation spec.

### 2026-10-20 — Session 1 (cont.): user spec received; syllabus added; previews v0.1
- User pushed `rearrange` to main: sources moved into `sources/`, syllabus PDFs added (`sources/8834_y26_sy.pdf`, `sources/9173_y26_sy.pdf`). PR #1 had been merged, so the branch was restarted from `origin/main` and the unmerged notes commits were cherry-picked on top.
- **User's consolidation spec:**
  1. **Doc 1**: table, columns = paper question slots (Q1, Q2, ...), rows = school + year, cell = topic of the question **per the H1/H2 syllabus**. Separate tables for H1 and H2. **Ignore VJC 2026 H1 QP** (encrypted).
  2. **Doc 2**: listed by topic; under each topic, school + year, then the full question plus diagram(s) if any. Split into 4 docs: H1 structured, H1 essay, H2 structured, H2 essay.
  - Wanted: a preview of doc 1 with one school row, and of each doc-2 file with one topic and one school question.
- Syllabus taxonomy written to `notes/syllabus_topics.md` and `tools/syllabus_topics.json`: Cluster → Topic (e.g. 1.2) → sub-topic/Key Question group (e.g. 1.2.2).
- Builder `tools/build_docs.py` (python-docx): grid doc + 4 by-topic docs. Diagrams = Resource blocks cropped from Insert PDFs (scratchpad `tools/crop_resources.py`).
- Choices made for the preview (to confirm with user): Word .docx; grid cell = sub-topic code + short name, plus grey line with case/focus; rows sorted school then year; structured Qs filed under their main Topic (most marks) and tagged with all sub-topics; essays filed by sub-topic; question text typed from the QP, diagrams as images.
- Previews (sample = ACJC 2024): `previews/1 Topic Grid by School (H1 & H2) v0.1 PREVIEW.docx`, `2a`–`2d ... v0.1 PREVIEW.docx`.
- 2025/2026 read-through resumed after a usage-limit pause; notes now end each paper with "Syllabus topics:" lines. Done so far: 2025 ACJC, ASRJC, RVHS, DHS.
- Doc version: v0.1 (preview only).
- Open: user feedback on previews → full build v0.1.

### 2026-10-20 — Session 1 (cont.): 2025 notes complete; 2026 nearly complete
- Notes written for all 15 schools in 2025, and for 2026 ACJC, ASRJC, CJC, DHS, EJC, HCI, JPJC, MI, NJC, NYJC, RI, RVHS and SAJC. Still running: 2026 TJC, TMJC, VJC, YIJC. Each note ends every paper with a "Syllabus topics:" line.
- **Extraction gap:** pandoc dropped text inside Word text boxes. I checked every .docx. What was lost is almost all Insert content (resource text, questionnaires, a climograph header) plus cover headers. No question wording was lost. The worst cases:
  - RVHS 2024/2026 inserts
  - SAJC 2025 H2 P1 insert
  - VJC 2024 inserts
  - EJC 2024 H2 P2 insert
  The docs themselves are not affected: diagrams are cropped from rendered pages, and Word inserts will be converted to PDF with soffice before cropping.
- Fieldwork questions outside the syllabus areas are labelled "Fieldwork – Other (…)", e.g. NJC food waste and JPJC recycling. Asked the user whether to group them under CC response.
- The source errors found so far (wrong resource numbers, marks that don't match, factual slips in answer schemes) are recorded in the header of each school's note.

### 2026-10-20 — Session 1 (cont.): read-through complete
- Last batch done: 2026 TJC, TMJC, VJC (H2 only; H1 QP excluded per user), YIJC.
- All 47 school-years have notes. Checked that no "Grid label" lines remain and that every 2025/2026 paper has a "Syllabus topics:" line.
- No answer scheme for:
  - 2024: SAJC H1.
  - 2025: RVHS, DHS (none at all); CJC H1 and H2 P2; TMJC H1 and H2 P2; JPJC H1; TJC H1.
  - 2026: EJC, NYJC (none at all); DHS H2 P2; YIJC H2 P1.
- No H1 paper: NJC 2024, RVHS 2024/2025/2026, MI 2026.
- Next: user feedback on the previews, then the full v0.1 build (2024 notes need syllabus labels first).

### 2026-10-20 — Session 1 (cont.): user decisions; previews v0.2
- User decisions:
  - Leave out password-protected files. The only one is VJC 2026 H1 QP; a scan of all sources found no others.
  - Questions only, no answers.
  - Doc 1 grid cells show the syllabus topic only.
  - A structured question is filed under the topic with the most marks.
  - Rows go by school, with the year beside the school ("ACJC 2024").
  - Fieldwork outside the syllabus areas goes under "Fieldwork – Others" for now, and a separate doc lists things for the user to review.
- New doc **0 Items to Review** has three sections:
  1. Fieldwork questions filed under Others, with a column for the user's decision.
  2. Files left out.
  3. Problems in the question papers and inserts.
- Builder updated: topic-only grid, fieldwork grouped by area with Others last, review doc. Preview data saved as `tools/preview_questions.json` and `tools/preview_review.json`.
- Files: `previews/0`, `1`, `2a`–`2d` `... v0.2 PREVIEW.docx` (v0.1 previews removed).
- Doc version: v0.2 (preview).
- Next: on approval, do the full build. Steps: label the 2024 notes with syllabus topics, collect every question's text, and crop every insert (Word inserts are converted to PDF first).

### 2026-10-21 — Session 1 (cont.): previews moved to `previews/`
- User asked for the previews to be in their own folder in git. Moved `output/preview/` → `previews/` at the repo root (v0.2 PREVIEW docs 0, 1, 2a–2d).

### 2026-10-21 — Session 1 (cont.): previews v0.3, fieldwork split out
- User asked for fieldwork to be separated out of part 2, giving 6 full-question docs: H1 Fieldwork, H1 Structured, H1 Essay, H2 Fieldwork, H2 Structured, H2 Essay. User asked for the preview before the full build.
- Builder: questions now have kind = fieldwork | structured | essay. Fieldwork docs group questions by syllabus fieldwork area, with Others last.
- Preview samples added: ACJC 2024 H1 Q1 (Bukit Merah elderly, R1–R3) and H2 P2 Q1 (Punggol flood risk, R1–R4).
- Files: `previews/0`, `1`, `2a`–`2f` `... v0.3 PREVIEW.docx` (v0.2 removed).
- Doc version: v0.3 (preview).

### 2026-10-21 — Session 1 (cont.): doc 1 (topic grid) full build v0.4
- User decisions:
  - Review doc: section 1 (Fieldwork – Others) is OK; ignore sections 2 and 3.
  - Build one document at a time to save tokens, starting with doc 1.
- 2024 notes now have "Syllabus topics:" lines, labelled from the question wording and sub-part marks (all 15 schools).
- `tools/parse_notes.py` reads every note's "Syllabus topics:" lines: 716 questions across 47 school-years, with no count mismatches and no question missing a topic.
- Fieldwork areas: CC response 37, Elderly needs 23, Flood risk 15, Others 13. Others = the 7 approved earlier plus 6 from 2024:
  - ASRJC H1 – Green Hub
  - CJC H1 – single-use plastics
  - DHS H1 – Reuse & Return
  - EJC H1 – Green Hub
  - JPJC H1 and H2 P2 – cycling promotion
  These are to be added to review-doc section 1 when that doc is built.
- Two labels cross clusters because the question really does: CJC 2025 H2 P1 Q2 also tags 1.1.3 (transboundary water context), and HCI 2025 H2 P1 Q1 also tags 2.2.3 (delta).
- Builder changes:
  - Rows can't split across pages.
  - A footnote lists school-years with no paper at that level: H1 – MI 2026, NJC 2024, RVHS 2024–26, VJC 2026 (password-protected).
  - Syllabus code legend at the end.
  - `--only grid|review|bytopic` flag.
- Output: `docs/1 Topic Grid by School (H1 & H2) v0.4.docx` (12 pages, landscape).
- Next: user to check doc 1, then the next doc.

### 2026-10-21 — Session 1 (cont.): doc 2a (H1 Fieldwork) full build v0.5
- **Sources:** `tools/h1_manifest.json` lists the H1 QP and Insert for all 41 school-years that have H1 (VJC 2026 left out because its QP is password-protected). Word files were converted to PDF with soffice in a scratchpad cache.
- **Question wording:** `tools/extract_questions.py` takes Q1 (Section A) from each QP's `pdftotext -layout` text. Checked automatically: sub-parts in order and summing to 30 marks for all 41; no footer text or stray "[n]" marks left in the text. Fixes needed along the way:
  - "a)" style part labels.
  - Labels split across lines.
  - Marks printed mid-line.
  - ASRJC page footer ("ASRJC 2026 JC2 H1 Geography Prelim").
  - Ending a question at a stem line that happened to start with "2".
- **Diagrams:** `tools/crop_resources.py` crops each "Resource N" block from the insert. Fixes needed along the way:
  - Skip copyright-page lines (VJC 2024 lists "Resource N <url>").
  - Skip question-paper sentences ("Resource 1 shows ...") in combined QP+Insert files (TJC).
  - Merge a bare "Resource 4" heading into 4A/4B.
  - Stop at sideways (landscape) pages.
  - Leave out page-footer logos.
  - Continue onto the next page only when the page is full (EJC 2024 heading sat at the bottom of a page; HCI 2025 R4 runs over two pages).
- **Which resources go with each question:** taken from the resources the question's wording refers to (`tools/resource_refs.py`), not from the insert labels. YIJC 2024 insert labels R7 "for Question 1" (an insert error); JPJC R1A/R1B have no "for Question" label.
- **Checking:** every selected crop was checked by eye on contact sheets.
- **Doc:** grouped under Cluster 2 Fieldwork by area: Community response to CC (15), Elderly needs (17), Others (9). Schools sorted by name then year.
- **File size:** images are capped at 1300 px and saved as JPEG or 256-colour PNG, whichever is smaller. That cut the file from 100 MB to 20.6 MB (166 pages).
- Next: user to check doc 2a, then the next doc.

### 2026-10-21 — Session 1 (cont.): doc 1 at key-question level (preview v0.6)
- User asked for doc 1 to be more detailed, below sub-topic level. Example: ACJC 2024 Q4 is "SUD", but which part of SUD?
- Added the syllabus Key Questions as a 4th level, coded a/b/c, e.g. `1.1.1b SUD: Urban population trends`. They're in `tools/syllabus_topics.json` (`kq`) and `notes/syllabus_topics.md`. Builder updated: grid cells and the code legend now show key-question labels.
- Preview: `previews/1 Topic Grid by School (H1 & H2) v0.6 PREVIEW.docx` (ACJC 2024 row).
- Next: on approval, relabel all 716 questions at key-question level and rebuild doc 1.

### 2026-10-21 — Session 1 (cont.): PR #2 merged
- User merged PR #2 into `main` (up to commit `66c3baa`, previews v0.2 in `previews/`). Later work (previews v0.3, doc 1 v0.4, doc 2a v0.5, preview v0.6) is not on `main` yet. Merged `main` into the working branch so the branch stays current (no force-push).

### 2026-10-21 — Session 1 (cont.): main reverted; user follows the branch
- The user removed their local clone and asked for `main` to go back to its state before the merges.
- First checked that the branch `claude/amazing-dirac-mpbgn8` on GitHub has everything: 441 source files, notes for 47 school-years, docs 1 and 2a, previews, tools.
- Pushed one revert commit to `main` (`e0ae977`) undoing the PR #1 and PR #2 merges. `main` now matches the user's own "rearrange" commit `6396e50`: only `README.md` and `sources/`. Nothing was force-pushed; history is kept.
- From now on the user's local folder follows the branch `claude/amazing-dirac-mpbgn8`, and all work is pushed there.
- Note for later: if this branch is ever merged into `main` again, the revert must be reverted first. Otherwise the earlier work won't come back.

### 2026-10-21 — Session 1 (cont.): doc 1 rebuilt at key-question level (v0.7)
- The user approved the key-question level, so every note now has a `Syllabus KQs:` line under each `Syllabus topics:` line.
- ACJC 2024 was labelled by me (the agreed example). The other 46 school-years were split over 6 parallel helpers, all following one rulebook (scratchpad `kq_rules.md`): every sub-part of a structured question gets a code, codes are ordered by marks, essays usually get one code, and boundary rules are spelled out.
- `tools/parse_notes.py` now prefers key-question codes. Validation:
  - 716 questions; every code is on the syllabus list; no question is left at sub-topic level.
  - Only 2 cross-cluster tags, both real: CJC 2025 H2 P1 Q2 → 1.1.3b; HCI 2025 H2 P1 Q1 → 2.2.3c.
  - Codes per question: 1 code ×366, 2 ×70, 3 ×74, 4 ×69, 5 ×37, 6 ×11, 7 ×1.
- Spot-checked 30 random essays against their wording; all fit.
- Ambiguous calls that the helpers flagged (kept as chosen): e.g. "natural vs human causes" essays get one code; "interdependence" sub-parts → 1.2.2a; ITCZ-driven monsoon rainfall → 2.1.1c; sea-level-rise mechanisms → x.2.2a. TMJC 2026 H2 P1 Q2(e) (Amazon deforestation location, 4 marks) has no matching key question, so it carries no code.
- Output: `docs/1 Topic Grid by School (H1 & H2) v0.7.docx` (38 pages; legend now lists every key question); the old v0.4 file was removed.

### 2026-10-21 — Session 1 (cont.): Review Notes for every doc
- User asked for every doc to have its own document of assumptions and things to review and consider. This is now a working rule in `CLAUDE.md`.
- Added `tools/review_docs.py`, which builds a review doc from a spec in `tools/review/<doc>.json`. Each review doc has four parts: what the doc is and how it was built, assumptions, items to review (tables with a "Your decision" column), and things to consider.
- `docs/1 Topic Grid by School (H1 & H2) – Review Notes v0.7.docx`:
  - assumptions
  - the 13 "Others" fieldwork questions
  - inconsistent fieldwork filing: BCRS, cycling and recycling scenarios are split between "CC response" and "Others" (suggested rule given)
  - 28 borderline key-question calls, each with an alternative
  - the TMJC 2026 part with no matching key question, the cross-cluster cases, and ideas to consider
- `docs/2a H1 Fieldwork Questions by Topic – Review Notes v0.5.docx`:
  - assumptions: how resources are chosen, Word→PDF conversion, image compression
  - places where the text or crops aren't a perfect copy: flattened tables, page numbers and footers in some crops, JPJC 2026 comment margin
  - ideas, e.g. tagging sub-parts by fieldwork stage
- The per-doc Review Notes replace the earlier single "0 Items to Review" doc (that preview stays in `previews/`). Following the user's earlier instruction, errors printed in schools' papers are not listed.

### 2026-10-21 — Session 1 HANDOFF (continue in a new cloud session)
**Read this entry first in the next session.**

**Where things stand**
- Branch: `claude/amazing-dirac-mpbgn8`. All work is here. The user's local GitHub Desktop folder follows this branch.
  - `main` was deliberately reverted to the user's own files (commit `e0ae977`).
  - Don't merge into `main` or open a PR unless the user asks. If a merge is ever needed, revert `e0ae977` first.
- Done and delivered (each doc has a `– Review Notes` companion):
  - `docs/1 Topic Grid by School (H1 & H2) v0.7.docx`: topic grid at syllabus key-question level, 716 questions, 47 school-years.
  - `docs/2a H1 Fieldwork Questions by Topic v0.5.docx`: 41 H1 fieldwork questions with full wording and 166 cropped diagrams, about 21 MB.
- Still to build, one doc at a time, each with Review Notes, the next one only when the user names it. The user was last asked which comes next and hasn't answered.
  - 2b H1 Structured (H1 Q2, Q3)
  - 2c H1 Essay (H1 Q4–Q6)
  - 2d H2 Fieldwork (P2 Q1)
  - 2e H2 Structured (P1 Q1, P1 Q2, P2 Q2)
  - 2f H2 Essay (P1 Q3–Q6, P2 Q3–Q4)
- Open review items for the user are in the two Review Notes docs: the "Others" fieldwork list, inconsistent fieldwork filing (a rule is suggested), and 28 borderline key-question calls.

**User's decisions so far (keep to them)**
- Leave out password-protected files. The only one is VJC 2026 H1 QP.
- Questions only, no answers.
- Doc 1 shows syllabus topics only, now at key-question level (e.g. `1.1.1b SUD: Urban population trends`). Rows are by school, with the year beside the school name.
- Doc 2 is split into 6 files: H1/H2 × fieldwork/structured/essay. Topic → school + year → full question + diagrams.
- A structured question is filed under the topic with the most marks.
- Fieldwork outside the syllabus areas goes under "Others".
- Show a preview before a new kind of output. Build one doc at a time to save tokens.
- Every doc gets Review Notes. Don't list errors printed in schools' papers.
- Bump the version on every doc update and log it here (latest: v0.7).

**How to build the next doc**
1. Labels: `python3 tools/parse_notes.py > questions.json` gives every question's `topics` (key-question codes) and `fieldwork_area`.
2. Sources:
   - Write a manifest like `tools/h1_manifest.json` (school, year, QP path, Insert path) for the papers the doc needs.
   - Paths are under `sources/`. Convert Word files to PDF with `soffice` first.
   - Some PDFs combine the QP and Insert (TJC).
3. Question wording: `tools/extract_questions.py` (`extract(pdf, qno, section)`).
   - Section letters: H1 B = Q2–Q3, C = Q4–Q6. H2 P1 A = Q1–Q2, B = Q3–Q6. H2 P2 A = Q1, B = Q2, C = Q3–Q4.
   - The extractor was built for Q1 in Section A. For other questions, check that it handles the start and end of each question in a section with several questions.
   - Validate every question: part labels in order, marks add up (H1 Sec B = 22; H2 structured = 30, usually), no footer text or `[n]` left in the text.
4. Diagrams: `tools/crop_resources.py <insert.pdf> <outdir>`, then choose each question's resources from its wording (`tools/resource_refs.py`). Check every crop by eye on contact sheets.
5. Build: `tools/build_docs.py <data.json> docs <version> --only bytopic --doc 2b`. The data format is like `tools/data/doc2a_questions.json`; the first `stem` entry is the section line.
6. Review Notes: write `tools/review/<doc>.json` and run `python3 tools/review_docs.py tools/review/<doc>.json docs`.
7. Log here, add a version-history row, commit, push to the branch, and send the file to the user.

**Other references**
- Pipeline scripts and notes: `tools/pipeline/README.md`.
- Syllabus codes: `notes/syllabus_topics.md` and `tools/syllabus_topics.json` (`kq` = key questions).
- Key-question labelling rules: `tools/kq_rules.md`.
- The reading notes in `notes/<year>/<SCHOOL>.md` record each question's wording and marks, plus `Syllabus topics:` and `Syllabus KQs:` lines.
- The scratchpad from session 1 (text extracts, crops, PDF cache) is not in the repo. Regenerate it as needed (see the pipeline README).

### 2026-10-21 — Session 2: usage-limit and long-task rules
- Read the handoff. Asked the user which of 2b–2f to build next; not yet answered.
- User asked for new working rules. Added to `CLAUDE.md` under "Usage limits and long tasks":
  - stop at about 90% of the session token budget
  - schedule a resume message after a plan usage-limit reset
  - for long cloud tasks, a "Task in progress" note plus an hourly scheduled check-in
  - don't cut checks just to save tokens
- Added a "Next session starts here" line at the top of this log.
- User chose to put the rules on both branches. `CLAUDE.md` was also committed to `main`, identical to the branch copy, so a later merge has no conflict there. No other work went to `main`.
- Files: `CLAUDE.md`, `SESSION_LOG.md`. Doc version unchanged (v0.7).

### 2026-10-21 — Session 2: doc 2b (H1 Structured) full build v0.8
- User: "build all of them" (2b–2f). Long-task note at the top of this log and an hourly check-in set up, per the new rule.
- **Sources:** H1 manifest as for 2a. New `tools/h2_manifest.json` for the H2 docs (47 school-years). All 68 Word files converted to PDF.
- **Wording:** `tools/pipeline/run_questions.py h1b` (Q2–Q3, Section B). Extractor fixes: marks split over two lines (TMJC 2026), next question at a different indent (SAJC 2024), part marks on the first line (TMJC 2024/2025). Q1 wording for 2a re-checked: unchanged.
- **Checks:** all 82 questions have parts in order, marks summing to 22, and labels/marks matching the reading notes (`check_vs_notes.py`). No footer text left in the wording.
- **Diagrams:** 266. Cropper now handles sideways pages (NYJC 2024, TJC 2024/2025, HCI 2026, YIJC 2026, EJC 2024), stops at 'End'/'Sources'/'Acknowledgements', drops more footers, trims bottom whitespace and the JPJC 2026 grey margin. Hand fixes in `manual_fixes.py`: EJC 2024 R7A/7B maps taken from the Word file (lost in conversion); TJC 2026 R5/R9 rebuilt from the Word file (shown sideways). All 266 checked by eye on contact sheets.
- **Filing:** by topic with the most marks. 8 questions span 1.1 and 1.2; counted part by part, all agree with the first-listed key question (1.1: 43, 1.2: 39).
- **Builder:** `topic_label` shows key-question names on each question's Syllabus line.
- Output: `docs/2b H1 Structured Questions by Topic v0.8.docx` (204 pages, 28 MB) + `– Review Notes v0.8` (spec `tools/review/2b_h1_structured.json`). Data: `tools/data/doc2b_questions.json`, `tools/data/h1_q2q3_resources.json`.
- Next: 2c H1 Essay.
