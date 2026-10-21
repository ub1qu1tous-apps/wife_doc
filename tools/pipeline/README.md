# Pipeline scripts (moved out of the session scratchpad)

Set `SCRATCH` to a working folder outside the repo (default `/tmp/wife_doc_scratch`). Scripts that do `import os` at the top need it; add `import os` if missing.

1. `extract.sh` – text from every source file → `$SCRATCH/text/` (needs `$SCRATCH/src.txt` = list of source paths; sources now live under `sources/`, so regenerate src.txt with `find sources -type f \( -name '*.pdf' -o -name '*.docx' -o -name '*.doc' \)` and run from the repo root).
2. `bundle.py` – one de-duplicated text bundle per school+year → `$SCRATCH/bundles/<year>_<SCHOOL>.txt` (path parsing assumes the old layout without the `sources/` prefix – strip it in src.txt or adjust).
3. `run_h1.py` – extracts H1 Q1 wording from all QPs in `tools/h1_manifest.json` (uses `tools/extract_questions.py`; Word files converted to PDF first into `$SCRATCH/pdfcache/<md5[:10]>/`).
4. `crop_h1.py` – crops all Insert resources with `tools/crop_resources.py` → `$SCRATCH/full/img/<year>_<SCHOOL>_H1/R*.png`.
5. `add_topics.py` – one-off: wrote the 2024 `Syllabus topics:` lines.

Doc data: `tools/data/doc2a_questions.json` (doc 2a input; image paths relative to `$SCRATCH/full/`), `tools/data/h1_q1_resources.json` (which resources each H1 Q1 uses).
Key-question rulebook used for labelling: `tools/kq_rules.md`.
