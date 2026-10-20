# Session log

## Current state
- **Doc:** not created yet
- **Current version:** —
- **Sources received:** H1/H2 Geography JC Prelim papers 2024–2026 (439 files, ~422 MB; 266 PDF, 168 DOCX, 4 DOC) — pushed by user to `main`, merged into working branch. See Session 1 log entry for breakdown.
- **Planned structure (proposed, awaiting confirmation):** School → Subject/Level → Topic → questions tagged with source (school, year, paper, Q no.), marks/answers where available; topic-frequency summary table at the end.
- **Open questions to user:** source type (past-year/prelim/worksheets/notes)? topic-first vs school-first grouping? include answers?

## Version history
| Version | Date | Changes |
|---|---|---|
| — | — | — |

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
- Read progress (2024): ACJC ✅ ASRJC ✅ | CJC DHS EJC HCI JPJC NJC NYJC RVHS SAJC TJC TMJC VJC YIJC pending. 2025, 2026 pending.
