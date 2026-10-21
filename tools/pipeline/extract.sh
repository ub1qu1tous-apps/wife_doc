#!/bin/bash
SP=${SCRATCH:-/tmp/wife_doc_scratch}
cd /home/user/wife_doc
while IFS= read -r f; do
  out="$SP/text/$f.txt"; mkdir -p "$(dirname "$out")"
  case "$f" in
    *.pdf) pdftotext -layout "$f" "$out" 2>/dev/null ;;
    *.docx) pandoc "$f" -t plain --wrap=none -o "$out" 2>/dev/null ;;
    *.doc) d=$(mktemp -d); soffice --headless --convert-to txt:Text --outdir "$d" "$f" >/dev/null 2>&1; mv "$d"/*.txt "$out" 2>/dev/null; rm -rf "$d" ;;
  esac
done < $SP/src.txt
