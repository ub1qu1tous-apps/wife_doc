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
