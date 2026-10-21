# Session log

## Current state
- **Docs:** `docs/1 Topic Grid by School (H1 & H2) v0.4.docx` (full). Docs 0 and 2a–2f: previews only (v0.3, `previews/`). Build is going one doc at a time.
- **Current version:** v0.4
- **Sources:** `sources/Other JC Prelims 2024|2025|2026/` (JC prelim H1 8834 & H2 9173 papers, inserts, answers) + syllabus PDFs `sources/8834_y26_sy.pdf`, `sources/9173_y26_sy.pdf`.
- **User spec:** see the "user spec received" log entry. Topics per syllabus (`notes/syllabus_topics.md`). Ignore VJC 2026 H1 QP.
- **Reading notes:** `notes/<year>/<SCHOOL>.md` — **all 47 school-years read** (2024: 15, 2025: 15, 2026: 17). 2025/2026 notes carry syllabus-topic lines; 2024 notes still need them (add at build time).

## Version history
| Version | Date | Changes |
|---|---|---|
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
