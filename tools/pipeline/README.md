# Pipeline scripts (moved out of the session scratchpad)

Set `SCRATCH` to a working folder outside the repo (default `/tmp/wife_doc_scratch`). Scripts that do `import os` at the top need it; add `import os` if missing.

1. `extract.sh` – text from every source file → `$SCRATCH/text/` (needs `$SCRATCH/src.txt` = list of source paths; sources now live under `sources/`, so regenerate src.txt with `find sources -type f \( -name '*.pdf' -o -name '*.docx' -o -name '*.doc' \)` and run from the repo root).
2. `bundle.py` – one de-duplicated text bundle per school+year → `$SCRATCH/bundles/<year>_<SCHOOL>.txt` (path parsing assumes the old layout without the `sources/` prefix – strip it in src.txt or adjust).
3. `run_h1.py` – extracts H1 Q1 wording from all QPs in `tools/h1_manifest.json` (uses `tools/extract_questions.py`; Word files converted to PDF first into `$SCRATCH/pdfcache/<md5[:10]>/`).
4. `crop_h1.py` – crops all Insert resources with `tools/crop_resources.py` → `$SCRATCH/full/img/<year>_<SCHOOL>_H1/R*.png`.
5. `add_topics.py` – one-off: wrote the 2024 `Syllabus topics:` lines.

Doc data: `tools/data/doc2a_questions.json` (doc 2a input; image paths relative to `$SCRATCH/full/`), `tools/data/h1_q1_resources.json` (which resources each H1 Q1 uses).
Key-question rulebook used for labelling: `tools/kq_rules.md`.

## Docs 2b–2f (session 2)
All take `SCRATCH` (session 2 used the session scratchpad). Word sources are converted to PDF into `$SCRATCH/pdfcache/<md5[:10]>/` first (same scheme as `run_h1.py`).
- `tools/h2_manifest.json`: `[school, year, P1 QP, P1 Insert, P2 QP, P2 Insert]` for all 47 school-years (TJC 2024/2025 and TJC 2026 P1 combine QP and Insert in one file).
- `run_questions.py <spec>`: wording for a set of slots (`h1b`, `h1c`, `h2p1a`, `h2p1b`, `h2p2a`, `h2p2b`, `h2p2c`) → `$SCRATCH/q_<spec>.json`, with checks (labels in order, marks, no stray `[`).
- `check_vs_notes.py <q_spec.json>`: compares part labels and marks with the reading notes.
- `pick_resources.py <q_spec.json> <H1|H2P1|H2P2>`: each question's resources from its wording → `<q_spec>_res.json` (follows `R7B.alias` files for "Resources 7A and 7B" crops).
- `crop_h1.py` (and the H2 equivalent) then `manual_fixes.py`: crops that need a hand fix (EJC 2024 H1 R7A, TJC 2026 H1 R5/R9).
- `contact_sheets.py <res.json> <prefix>`: sheets of 20 crops for checking by eye.
- `make_doc_data.py <2b..2f> <out.json>`: doc data from the wording, resources and `parse_notes.py` labels (`$SCRATCH/questions.json`), then `tools/build_docs.py <out.json> docs <version> --only bytopic --doc <2b..2f>`.
- `crop_resources.py` changes in session 2: landscape (sideways) pages are cropped and turned upright; crops stop at 'End', 'Sources', 'Acknowledgements' lines; more footer patterns; bottom whitespace and plain side bands (Word comment margin) trimmed.
- `extract_questions.py` changes: marks split over two lines (`[6` / `]`) are joined; the next question may start at a slightly different indent; a question ends at the next number once one of its marks has been seen.
