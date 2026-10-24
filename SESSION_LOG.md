# Session log

> **Task in progress (session 4):** user said 'do the rest' (2026-10-24): build docs 3c (Topic 2.1), 3d (2.2), 3e (3.1), 3f (3.2) to v1 in the approved 3a/3b format, one topic at a time. Per topic: slot plan → research → charts (`tools/case_charts.py`, prefix 2_1_ etc.) → `tools/data/case_studies_3X.json` → build to docs/ → check pages + docx checks (link URLs, r:ids, rPr order) → Review Notes v1 → log → commit + push. Done so far: 3c v1, 3d v1, 3e v1. Hourly check-in continues this note until it's cleared.

**Next session starts here:** read the "Session 2 HANDOFF" entry and the session 3–4 entries after it. Docs 1 and 2a–2f are built (doc 1 v0.15, docs 2a–2f v0.14). New series 3a–3f (case studies per H2 topic): **3a v1 and 3b v1 done** (`docs/3a …Topic 1.1… v1.docx`, `docs/3b …Topic 1.2… v1.docx`). Next: 3c (Topic 2.1) when the user asks.

## Current state
- **Docs (full):** `docs/1 Topic Grid by School (H1 & H2) v0.15.docx` (key-question level, focus lines, topic shading, frequency summary), `docs/2a H1 Fieldwork Questions by Topic v0.14.docx`, `docs/2b H1 Structured Questions by Topic v0.14.docx`, `docs/2c H1 Essay Questions by Topic v0.14.docx`, `docs/2d H2 Fieldwork Questions by Topic v0.14.docx`, `docs/2e H2 Structured Questions by Topic v0.14.docx`, `docs/2f H2 Essay Questions by Topic v0.14.docx`, each with a `– Review Notes` companion. All planned docs are built. User's local folder follows the branch `claude/amazing-dirac-mpbgn8`.
- **Current version:** v0.15
- **Sources:** `sources/Other JC Prelims 2024|2025|2026/` (JC prelim H1 8834 & H2 9173 papers, inserts, answers) + syllabus PDFs `sources/8834_y26_sy.pdf`, `sources/9173_y26_sy.pdf`.
- **User spec:** see the "user spec received" log entry. Topics per syllabus (`notes/syllabus_topics.md`). Ignore VJC 2026 H1 QP.
- **Reading notes:** `notes/<year>/<SCHOOL>.md` — **all 47 school-years read** (2024: 15, 2025: 15, 2026: 17). All notes carry `Syllabus topics:` and `Syllabus KQs:` lines.

## Version history
| Version | Date | Changes |
|---|---|---|
| 3b v1 | 2026-10-24 | **Doc 3b full build**: Topic 1.2, 16 slots / 18 cases (strong + limited state influence; succeeded + failed unions), a chart per case, Links lines; Review Notes v1 |
| 3a v1 (fix) | 2026-10-24 | 3a v1 rebuilt: Word 2007 said the file was corrupt (link run properties out of schema order); v0.1 preview patched too |
| 3a v1 | 2026-10-24 | **Doc 3a full build**: Topic 1.1, 15 slots / 17 cases (succeeded + failed for both strategy slots), a chart per case, 'Links' line per case; Review Notes v1 |
| 3a v0.1 (preview) | 2026-10-24 | **New doc series 3a–3f** (case studies per H2 topic, own versioning: v0.1 preview → v1 confirmed). Preview of 3a Topic 1.1: slot plan + first 3 cases (Amazon, Cape Town, Nigeria) |
| v0.15 | 2026-10-22 | **Doc 1 rebuilt** with the Review Notes section 7 ideas: H2 split into P1/P2 tables, cells shaded by topic, focus line for all 716 questions, key-question frequency summary by year |
| v0.15 (preview) | 2026-10-22 | Doc 1 preview of Review Notes section 7 ideas: frequency summary by year, topic shading, focus lines, H2 split into P1/P2 tables (ACJC rows) |
| v0.14 | 2026-10-22 | **Docs 2a–2f rebuilt**: each school's question starts on a new page (user request); 2a rebuilt with current scripts (hyphen fixes, re-cropped); resources listed in Insert order |
| v0.13 | 2026-10-21 | **Doc 2f full build**: H2 Essay questions by topic, 282 essays grouped by sub-topic |
| v0.12 | 2026-10-21 | **Doc 2e full build**: H2 Structured questions by topic, 141 questions (full wording + 549 diagrams) |
| v0.11 | 2026-10-21 | **Doc 2d full build**: H2 Fieldwork questions by topic, 47 questions (full wording + 215 diagrams) |
| v0.10 | 2026-10-21 | **Doc 2b fix** (replaces v0.8): NJC 2026 Q3 diagrams corrected (whole R9, real R10); 'Co-operation' hyphen |
| v0.9 | 2026-10-21 | **Doc 2c full build**: H1 Essay questions by topic, 123 essays grouped by sub-topic |
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
- Output: `docs/2b H1 Structured Questions by Topic v0.10.docx` (204 pages, 28 MB) + `– Review Notes v0.8` (spec `tools/review/2b_h1_structured.json`). Data: `tools/data/doc2b_questions.json`, `tools/data/h1_q2q3_resources.json`.
- Next: 2c H1 Essay.

### 2026-10-21 — Session 2: doc 2c (H1 Essay) full build v0.9
- **Wording:** `run_questions.py h1c` (Q4–Q6, Section C). Extractor fixes: an essay ends at its mark, or at the blank line after it when words follow the mark (TMJC 2026 Q4); a one-line essay with its mark now ends correctly; the section heading is the one followed by the question (YIJC 2024 lists "Section C" on its cover); the last question stops at end-of-paper lines and Insert covers (TJC combined files). 2a and 2b wording re-checked: unchanged.
- **Checks:** 123 essays, all 13 marks; wording matches the notes' verbatim wording for all 123 (`check_essays_vs_notes.py`; differences are only the notes' abbreviations).
- **Filing:** by sub-topic of the key question; 9 essays have two key questions, 5 of them across sub-topics (listed in the Review Notes). 1.1.1: 7, 1.1.2: 29, 1.1.3: 34, 1.2.1: 9, 1.2.2: 11, 1.2.3: 33.
- Output: `docs/2c H1 Essay Questions by Topic v0.9.docx` (19 pages) + `– Review Notes v0.9` (spec `tools/review/2c_h1_essay.json`). Data: `tools/data/doc2c_questions.json`.
- Next: 2d H2 Fieldwork.

### 2026-10-21 — Session 2: doc 2b fixed (v0.10); H2 wording extracted
- **Error found in 2b v0.8:** the NJC 2026 H1 Insert has a hidden "Resource 10" label under the R9 picture. The cropper split R9 at that label and dropped the real R10 (the IPCC precipitation map) as a duplicate. The contact-sheet check missed it because both halves looked like plausible resources. Fix: a label covered by a picture is ignored when the same label also appears elsewhere. A broader rule (ignore every covered label) broke 20+ real headings in Word-converted inserts, so it was narrowed. All H1 and H2 crops were re-run and compared with the previous run: the only changes are NJC 2026 H1 R9/R10 and SAJC 2026 H2 P1 R2 (now includes its axis label).
- The cropper now also stacks a resource whose heading is repeated on a continuation page (MI 2026 H2 P1 R1, TJC 2025 H2 P1 R3, TJC 2026 H2 P1 R2/R6) instead of dropping the second part.
- Extractor: words broken at a hyphen over two lines are joined ('problem-solving'), except before and/or/to ('low- and high-income').
- 2b rebuilt as **v0.10** (v0.8 files removed); its Review Notes say what changed.
- **H2 wording:** P2 fieldwork Q1 is 40 marks (not 30). Extractor fixes for H2: labels and marks printed down a column over three lines (SAJC Word files), bare part labels ('(f)' on its own line), the question number repeated before (a) on a new page (TMJC 2024 P2), a wrapped stem line starting with the next question number (CJC 2024, RVHS 2025: the question number is the leftmost), papers that letter their sections differently (MI, TMJC 2025, YIJC: P2 has only Sections A and B), and cover pages that list sections (ACJC 2026). SAJC 2024 P2 Q1(g) '[10]' is printed one character per line, so its mark is set by hand (`MARK_FIXES` in `run_questions.py`).
- **Checks:** P2 Q1 (47), P1 Q1–Q2 (94), P2 Q2 (47): every part label and mark matches the notes. Essays P1 Q3–Q6 (188) and P2 Q3–Q4 (94): wording matches the notes (3 differ only by the notes' paraphrase).
- Known: doc 2a (v0.5) still has a few words split at a line-end hyphen (e.g. 'self- recording'); fixed if 2a is rebuilt.

### 2026-10-21 — Session 2: doc 2d (H2 Fieldwork) full build v0.11
- **Diagrams:** `tools/pipeline/crop_h2.py` crops all 94 H2 Inserts (P1, P2). Cropper changes: headings side by side on one line are split into columns (JPJC 2026 R7A/7B, SAJC 2024 R2A/2B, SAJC 2025 R4/R5, ASRJC 2024; also fixed a broken RVHS 2024 H2 P1 R6A); plural headings ('Resources 4A and 4B for Question 2') give one crop with an alias, unless each part has its own heading later (JPJC). Every re-crop was compared with the previous run; only the intended crops changed (ASRJC 2024 H1 R5 is now two crops – same content as in 2b).
- `pick_resources.py`: a question's 'Resource 2A/2B' falls back to the Insert's single 'Resource 2' (TMJC 2026). All H2 P1/P2 crops are used by some question; no referenced resource is missing.
- Hand fixes added to `manual_fixes.py`: CJC 2026 P2 R4 (table placed above its heading in the converted PDF – heading moved back on top), SAJC 2026 P2 R1 (picture turned 90° in Word – turned upright).
- **Builder:** images taller than 1.9 × their width are split across pages at blank rows instead of being shrunk to one page (multi-page questionnaires). No 2b image is affected.
- **Checks:** 47 questions, 40 marks each, labels/marks match the notes. All 215 diagrams checked by eye on contact sheets.
- Areas: Community response to CC 22, Fluvial flood risk 15, Elderly needs 6, Others 4 (JPJC 2024, NJC 2025, NJC 2026, RVHS 2026).
- Output: `docs/2d H2 Fieldwork Questions by Topic v0.11.docx` (197 pages, 25 MB) + `– Review Notes v0.11` (spec `tools/review/2d_h2_fieldwork.json`). Data: `tools/data/doc2d_questions.json`, `tools/data/h2_p2q1_resources.json`.
- Next: 2e H2 Structured.

### 2026-10-21 — Session 2: doc 2e (H2 Structured) full build v0.12
- **Filing:** 81 of the 141 questions test two topics. Marks were counted part by part for each: 62 agree with the first-listed key question, 6 tie (first-listed kept), 13 go to the other topic (`PRIMARY_OVERRIDE` in `make_doc_data.py`; listed in the Review Notes). Result: 1.1: 22, 1.2: 25, 2.1: 20, 2.2: 27, 3.1: 28, 3.2: 19.
- **Cropper fixes found on the 2e contact sheets:** combined QP + Insert files (TJC 2025/2026) no longer take question-paper lines such as 'Resource 3. [5]' as headings (R3/R2/R6 were whole QP pages); a heading repeated at the foot of a cover page is replaced by the full one (MI 2026 P1 R1); pictures running to the page foot are no longer cut off (VJC 2026 P2 R5 was only its heading; JPJC 2024 P1 R2B and CJC 2026 P1 R1 were cut short). Hand fix: CJC 2024 P1 R1/R2 maps turned upright. Each re-crop was compared with the previous one; doc 2d's crops and picks are unchanged.
- **Checks:** 141 questions, all 30 marks, labels/marks match the notes. All 549 diagrams checked by eye (22 contact sheets).
- Output: `docs/2e H2 Structured Questions by Topic v0.12.docx` (438 pages, 61 MB) + `– Review Notes v0.12` (spec `tools/review/2e_h2_structured.json`). Data: `tools/data/doc2e_questions.json`.
- Next: 2f H2 Essay.

### 2026-10-21 — Session 2: doc 2f (H2 Essay) full build v0.13
- 282 essays (P1 Q3–Q6, P2 Q3–Q4), all 20 marks, no diagrams. Wording matches the notes (279 exactly; 3 differ only by the notes' paraphrase). Every school's P1 Q3–Q4 are Cluster 1 and Q5–Q6 Cluster 2, so the section lines are right.
- Filed by sub-topic of the key question; 34 essays have two key questions, 14 across sub-topics (listed in the Review Notes).
- Output: `docs/2f H2 Essay Questions by Topic v0.13.docx` (43 pages) + `– Review Notes v0.13` (spec `tools/review/2f_h2_essay.json`). Data: `tools/data/doc2f_questions.json`.
- All five docs done: the hourly check-in was deleted and the "Task in progress" note cleared.

### 2026-10-21 — Session 2 HANDOFF
**Read this entry first in the next session.**

**Where things stand**
- Branch `claude/amazing-dirac-mpbgn8` holds everything; the user's local folder follows it. `main` has only the user's files plus `CLAUDE.md` (added this session, same as the branch copy). Don't merge into `main` or open a PR unless asked; if a merge is ever needed, revert `e0ae977` first.
- All planned docs are built, each with Review Notes: 1 (v0.7), 2a (v0.5), 2b (v0.10), 2c (v0.9), 2d (v0.11), 2e (v0.12), 2f (v0.13).
- `CLAUDE.md` now also has the usage-limit, long-task and token-use rules (session 2).

**Waiting on the user**
- Feedback on docs 2b–2f.
- Decisions in the Review Notes: doc 1 ("Others" fieldwork list, inconsistent fieldwork filing, 28 borderline key-question calls); 2b (8 two-topic questions); 2c (5 essays across sub-topics); 2d (layout items); 2e (13 questions filed under their second-listed topic, 6 ties); 2f (14 essays across sub-topics).
- Ideas offered in the Review Notes: split 2e (61 MB) by cluster; group by key question; contents lists; new page per question.

**Known small issues (not yet fixed)**
- Doc 2a (v0.5) still has a few words split at a line-end hyphen ('self- recording', 'pre- packaged'). The extractor now joins them; rebuilding 2a would fix it (bump the version).
- In 2b v0.10, ASRJC 2024 Q2 R5 is one crop holding both 5A and 5B side by side (content complete). The cropper now splits them; a rebuild would show two crops.

**How to rebuild any doc** (see `tools/pipeline/README.md`, section "Docs 2b–2f")
1. `SCRATCH=<dir>`; convert Word sources to PDF into `$SCRATCH/pdfcache/` (snippet in session 2's first build step: md5 of the manifest path, first 10 chars).
2. `python3 tools/parse_notes.py > $SCRATCH/questions.json`
3. `run_questions.py <spec>` → `check_vs_notes.py` / `check_essays_vs_notes.py`.
4. `crop_h1.py`, `crop_h2.py`, then `manual_fixes.py`; `pick_resources.py`; check `contact_sheets.py` output by eye.
5. `make_doc_data.py <2b..2f> <out.json>` → `tools/build_docs.py <out.json> docs <version> --only bytopic --doc <id>`.
6. Update `tools/review/<doc>.json`, run `tools/review_docs.py`, log here, commit, push.

### 2026-10-22 — Session 3: docs 2a–2f v0.14 (new page per school)
- User request: "For all doc 2 start each school's question on a new page for printing."
- Long-task note and an hourly check-in (`trig_013f89DV5XTYYt44tDM4j9NF`) were set up at the start; both removed now that the task is done.
- **Builder (`tools/build_docs.py`):** each school-year's question(s) start on a new page; a cluster/topic heading moves to the new page with its first question; two questions from the same school under the same heading share a page (6 essays in 2c, 1 in 2f, 2 structured in 2b). Removed the empty paragraph after each question (it made 8 blank pages when a question exactly filled its last page).
- **2a** rebuilt from the current pipeline (`run_h1.py`, current crops, `pick_resources.py`) instead of the session-1 data: 5 hyphen splits fixed; same resources per question; all 166 crops checked by eye on contact sheets. Section lines kept from v0.5.
- `pick_resources.py` now lists a question's resources in Insert order (R1, R2, R3A, …); changes 6 questions in 2d, and 2a/2b back to number order. 2b: ASRJC 2024 Q2 R5A/R5B now separate crops (267 diagrams).
- **Checks on the rendered PDFs (all six):** no page holds two schools' questions, no blank pages, no cluster/topic heading left at a page foot; sample pages viewed.
- Pages: 2a 179, 2b 229, 2c 117, 2d 223, 2e 487, 2f 281. Sizes as before (2e 61 MB).
- Review Notes v0.14 for all six: page counts, a "Changes in v0.14" line, the page layout added to assumptions, and the "new page" idea removed from "To consider". Old v0.5/v0.9–v0.13 doc 2 files removed.
- Data: `tools/data/doc2[a-f]_questions.json`, `h1_q1_resources.json`, `h1_q2q3_resources.json`, `h2_p2q1_resources.json` updated.
- Open: user's feedback and the Review Notes decisions (see Session 2 HANDOFF).

### 2026-10-22 — Session 3: doc 1 preview v0.15 (Review Notes section 7)
- User: "from 1 Topic Grid … Review Notes v0.7 do number 7", then "do a preview for all 4 ideas in 1 doc". Section 7 ("To consider") = (1) frequency summary, (2) shade cells by topic, (3) focus line under each code, (4) split H2 into P1 and P2 tables.
- Note: idea 3 brings back a case/focus line in grid cells, which the user had removed at v0.2 ("syllabus topic only"); the preview lets them decide.
- **Builder (`tools/build_docs.py`):** H2 grid split into Paper 1 and Paper 2 tables; each cell shaded by the topic it is filed under in doc 2 (H1 Cluster 1 uses the same yellows as H2 Cluster 3, since the content is the same; fieldwork peach), with a colour key under each table; optional grey focus line from `tools/data/focus_lines.json`; new section "How often each key question was tested" (per level, KQ × 2024/2025/2026/Total, fieldwork areas included; counts every question once per KQ it tests); `--rows ACJC` limits grid rows for a preview.
- Filing overrides moved from `make_doc_data.py` into `tools/data/primary_overrides.json` (shared by doc 1 shading and doc 2 filing; 2e data re-made and identical).
- Focus lines written by hand for the 48 ACJC cells only (from the notes; the notes' bold titles often just restate the topic, so they can't be used directly).
- Checks: fieldwork totals in the frequency table = 41 (H1) and 47 (H2), matching docs 2a/2d. Pages viewed.
- Output: `previews/1 Topic Grid by School (H1 & H2) v0.15 PREVIEW.docx` (6 pages).
- The hourly check-in set up for this task (`trig_01JqXZqiJLfKKWX8cSNr55Kk`) was deleted once the preview was done, since the next step waits on the user.
- Next (on approval): write focus lines for the other 668 cells, rebuild doc 1 as v0.15, update its Review Notes (section 7 done; new assumptions on shading and counts).

### 2026-10-22 — Session 3: doc 1 v0.15 (all four section 7 ideas)
- User approved the preview: "Do all 4 ideas for doc 1." Long-task note and hourly check-in (`trig_01BnuHuQSVB7Yj9ztodXLPnR`) used; both removed now.
- **Focus lines:** written by hand for all 716 cells in `tools/data/focus_lines.json` (case/place for structured and fieldwork questions, a short paraphrase for essays; max 48 characters), one commit per year. Helpers: `tools/pipeline/focus_sources.py <year>` lists cells still without a line next to the note's title; `tools/pipeline/add_focus.py` merges lines and rejects unknown cells.
- **Build:** `tools/build_docs.py questions.json docs v0.15 --only grid` → `docs/1 Topic Grid by School (H1 & H2) v0.15.docx` (39 pages: H1 table, H2 P1 table 17 pages, H2 P2 table, frequency summary, code legend).
- **Checks:** every focus line appears in the rendered PDF (5 YIJC cells confirmed by eye where the PDF text order hid them); all 47 school-years present; fieldwork totals 41/47; pages viewed (H1, H2 P1, H2 P2, frequency tables).
- **Review Notes v0.15:** layout and shading described, new assumptions (hand-written focus lines; shading follows doc 2 filing incl. the 13 overrides; how counts work and schools per year H1 13/14/14, H2 15/15/17); section 7 now has new ideas (mark 'due' key questions, same focus line in doc 2 headings, shorter cells for printing). Sections 3–6 (items for the user) unchanged. v0.7 files removed.
- Open: user's feedback and Review Notes decisions.

### 2026-10-24 — Session 4: case-study docs 3a–3f, 3a v0.1 preview
- User request: a doc for each of the 6 main topics (H2 9173 Topics 1.1–3.2). For each case-study point (factor, impact, characteristic, strategy, trend, challenges, actors), find a real case from 2015 or later. Strategy points get a succeeded and a failed case. Preview the first 3, each case about 1 page with 1 image. Title 'v0.1' for the preview, 'v1' when confirmed.
- Docs 3a–3f carry their own version numbers (v0.1 → v1), separate from the repo-wide numbers used for docs 1 and 2.
- Topic 1.1 split into 15 case-study slots from the syllabus content (table on page 1 of 3a). The preview covers slots 1–3 (all 1.1.1): trade-offs = Amazon deforestation, Brazil 2019–2025; limits = Cape Town Day Zero 2015–2018; measuring progress = Nigeria's census gap and 2025 GDP rebasing.
- Limits of this cloud session: photo sites (commons.wikimedia.org etc.) are blocked by the network policy, and page fetches fail (DNS), so only web search works. Each image is a chart drawn from the sourced figures (`tools/case_charts.py`). Figures come from search results quoting the sources; the ones to spot-check are in the Review Notes.
- New files: `tools/build_case_studies.py`, `tools/case_charts.py`, `tools/data/case_studies_3a.json`, `tools/data/case_charts/1_1_*.png`, `tools/review/3a_case_studies.json`.
- Output: `previews/3a Case Studies – Topic 1.1 Environment and Resources v0.1.docx` (4 pages: slot plan + 3 one-page cases) + `– Review Notes v0.1`. Rendered pages checked by eye.
- matplotlib is not preinstalled: `pip install matplotlib`.
- Open: user feedback on the slot plan, the format, charts vs photos, and the cases. Then build 3a v1 (slots 4–15), then 3b–3f.

### 2026-10-24 — Session 4: doc 3a v1 (Topic 1.1 complete)
- User approved the v0.1 preview: "everything ok. case choice anywhere that best fits. to consider, is good, do as you said. start with generating topic 1.1." Long-task note and hourly check-in (`trig_01PnbGu2rXrBtMpuofkoLvBz`) used; both removed now.
- Slots 4–15 added: Sri Lanka 2022 (economic and political challenges), Lithium Triangle (demand and technology), Indonesia 2015 fires (human activities), West Africa small fish (regenerative capacity), Bangladesh (Malthus vs Boserup), Vietnam solar, Laos hydropower, Mekong 2019 (transboundary impact), Central Asia (succeeded) and Indus treaty (failed), Oyu Tolgoi (characteristics), Guyana vs Niger Delta (variation), Indonesia nickel ban (succeeded) and Brumadinho (failed).
- 'Links' line under every case (other slots and topics where it fits), per Review Notes v0.1 section 5. Cases 1–3 unchanged apart from the new line.
- Charts for all 14 new cases in `tools/case_charts.py` (bars, timelines, a schematic for the Mekong, number tiles for the Indonesian fires). New helpers: `bars`, `timeline`, `even_timeline`, `tiles`.
- Builder: 'Links' line; plan table shading only while slots are pending.
- Output: `docs/3a Case Studies – Topic 1.1 Environment and Resources v1.docx` (18 pages: slot plan + 17 one-page cases; checked page by page that no case overflows) + `– Review Notes v1` (10 figures to spot-check, 4 choices). The v0.1 preview stays in `previews/`.
- Same limits as before: photo sites blocked, page fetches fail; figures come from search results quoting sources.
- Open: user feedback on 3a v1 and the Review Notes; then 3b (Topic 1.2).

### 2026-10-24 — Session 4: Word 2007 'corrupt file' fix
- User sent a screenshot: Word 2007 refused to open 3a v1 ("problems with the contents").
- Cause: in the source-link runs the builder wrote `w:u` before `w:sz`; the OOXML schema wants `color, sz, u`. LibreOffice ignores this, Word 2007 does not.
- Fix in `tools/build_case_studies.py`; 3a v1 rebuilt (same version, content unchanged); 3a v0.1 preview patched in place. A schema-order check of rPr/pPr/tcPr/tblPr in document.xml found no other problems.
- Rule for later builds: run the rPr order check on every new docx before sending (see the 3b entry).

### 2026-10-24 — Session 4: doc 3b v1 (Topic 1.2 complete)
- User: "yes please" to starting 3b. Built straight to v1 in 3a's approved format. Long-task note and hourly check-in (`trig_01EquomwFnrQU98zbh6YVQja`) used; both removed now.
- 16 slots / 18 cases: SE Asia HDI gaps; Vietnam trade and FDI; Philippine remittances; Ethiopia's industrial parks; China's shift to services; 2021 chip shortage; Apple's iPhone GPN and India; Bangladesh garments (host); Dyson (home); India/TikTok (strong state) and Ireland/Apple (limited state); TSMC Arizona (labour characteristics); UAW 2023 (union succeeded) and Amazon Bessemer (union failed); Singapore Platform Workers Act; RCEP (ASEAN); WTO and Indonesia's nickel ban; World Bank Doing Business.
- Charts `tools/data/case_charts/1_2_*.png` (new helper `hbars`). Pages checked by eye; rPr schema-order check passed.
- Output: `docs/3b Case Studies – Topic 1.2 Development and the Global Economy v1.docx` (19 pages) + `– Review Notes v1` (9 figures to spot-check, 4 choices).
- Open: does the fixed 3a open in the user's Word? Feedback on 3b; then 3c (Topic 2.1).

### 2026-10-24 — Session 4: 3a still 'corrupt' in Word 2007 — real cause found
- User: 3a v1 still would not open after the rPr fix.
- Cause: one source link (Kyoto University PDF, slot 8) had spaces in its URL; a link target must be a valid URI, and Word refuses the whole file. The v0.1 preview had no such link, which is why the problem started with v1.
- Fix: `hyperlink()` in `tools/build_case_studies.py` now percent-encodes every URL. 3a v1 and 3b v1 rebuilt (content unchanged). Checks: no invalid URL characters, every r:id resolves, rPr order OK.
- Check to run on every new docx: link targets valid, r:ids resolve, rPr order.

### 2026-10-24 — Session 4: doc 3c v1 (Topic 2.1 complete)
- Part of 'do the rest'. 11 slots / 12 cases: climate zones (Singapore, Niamey, Riyadh); 2020 Sahel floods (Hadley/ITCZ); India's driest August 2023 (monsoon); Cyclone Freddy 2023; 2015–16 El Niño and 2020–23 La Niña (Lismore); Amazon 2021 flood vs 2023 drought (water balance); Jakarta groundwater (storage); Chennai 2015 (pathways); Kerala 2018 (flood factors); Pakistan 2022 (impacts, vulnerability); KL SMART Tunnel (succeeded) and Jakarta 2020 floods (failed).
- New `tools/check_docx.py` (link URLs, r:ids, rPr order) — all 3a–3c files pass.
- Output: `docs/3c Case Studies – Topic 2.1 Tropical Climates and Drainage Basins v1.docx` (13 pages) + `– Review Notes v1`.

### 2026-10-24 — Session 4: doc 3d v1 (Topic 2.2 complete)
- 9 slots / 9 cases: Angkor sandstone (weathering); Petrópolis 2022 (mass movement); Mekong sand mining (fluvial processes); Ha Long Bay–Cat Ba (karst features); Son Doong (cave formation); Perak limestone quarrying (karst services); Brahmaputra/Majuli (braided channels); Mekong Delta shrinking (delta formation); Sundarbans (delta services).
- `tiles()` now shrinks long headline numbers so they fit (affects tile charts in 3a–3c too; their docs will be rebuilt at the end so the images match).
- Output: `docs/3d Case Studies – Topic 2.2 Landforms in the Tropics v1.docx` (10 pages) + `– Review Notes v1`. check_docx OK.

### 2026-10-24 — Session 4: doc 3e v1 (Topic 3.1 / H1 1.1 complete)
- 16 slots / 21 cases: Arcadis index (measuring SUD); Lagos (rapid growth); Detroit (population loss); Mexico City water (demand on environment); Koshe landfill (waste problems); South Korea food waste (succeeded) / Lebanon 2015 (failed); Dharavi (slums); KOTAKU (succeeded) / Otodo-Gbame (failed); Expo 2020 Dubai (reimaging reasons); Paris 2024 (succeeded) / Rio 2016 (failed); EIU index (subjective liveability); Cross Island Line (SUD vs liveability); Japan dying alone (elderly issues); Kampung Admiralty (succeeded) / South Korea old-age poverty (failed); Delhi women (issues); Delhi pink tickets (succeeded) / Mexico City women-only cars (failed).
- Output: `docs/3e Case Studies – Topic 3.1 Cities in a Sustainable Future v1.docx` (22 pages) + `– Review Notes v1`. check_docx OK.

