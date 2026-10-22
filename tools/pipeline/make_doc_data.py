"""Assemble a doc-2 data file from the extracted wording, the picked resources and the notes' syllabus labels.

usage: SCRATCH=... python3 tools/pipeline/make_doc_data.py <doc> <out.json>
doc = 2b | 2c | 2d | 2e | 2f. Inputs: $SCRATCH/questions.json (tools/parse_notes.py), $SCRATCH/q_<spec>.json and
$SCRATCH/q_<spec>_res.json (run_questions.py, pick_resources.py). Image paths are relative to $SCRATCH/full/.
Grouping ('primary'): structured -> the topic with the most marks: the topic of the first key-question code (codes are
listed by marks), except where a part-by-part mark count of a question that spans topics says otherwise
(PRIMARY_OVERRIDE); essay -> sub-topic of its first code; fieldwork -> '2' (H1) / '4' (H2).
"""
import json, os, sys

S = os.environ.get('SCRATCH', '/tmp/wife_doc_scratch')
DOCS = {  # doc: (level, kind, [(spec, paper, section line)])
    '2b': ('H1', 'structured', [('h1b', 'H1 Paper 1 (8834/01)', 'Section B — Cluster 1: Sustainable Future and Climate Change')]),
    '2c': ('H1', 'essay', [('h1c', 'H1 Paper 1 (8834/01)', 'Section C — Cluster 1: Sustainable Future and Climate Change')]),
    '2d': ('H2', 'fieldwork', [('h2p2a', 'H2 Paper 2 (9173/02)', 'Section A — Cluster 4: Fieldwork')]),
    '2e': ('H2', 'structured', [('h2p1a', 'H2 Paper 1 (9173/01)', 'Section A'), ('h2p2b', 'H2 Paper 2 (9173/02)', 'Section B — Cluster 3')]),
    '2f': ('H2', 'essay', [('h2p1b', 'H2 Paper 1 (9173/01)', 'Section B'), ('h2p2c', 'H2 Paper 2 (9173/02)', 'Section C — Cluster 3')]),
}
H2P1_CLUSTER = {'Q1': 'Cluster 1: Global Development and Natural Resources', 'Q2': 'Cluster 2: Tropical Environments',
                'Q3': 'Cluster 1', 'Q4': 'Cluster 1', 'Q5': 'Cluster 2', 'Q6': 'Cluster 2'}
# Structured questions whose part-by-part mark count puts more marks in another topic than the first-listed key
# question's (counted by hand from the wording, 2026-10-21). Ties keep the first key question: NJC 2024 P2 Q2,
# TJC 2025 P1 Q1, VJC 2025 P1 Q1, RVHS 2026 P1 Q2, SAJC 2026 P2 Q2, TJC 2026 P2 Q2.
PRIMARY_OVERRIDE = {k: v for k, v in json.load(open('tools/data/primary_overrides.json')).items() if not k.startswith('_')}

doc, out = sys.argv[1], sys.argv[2]
level, kind, specs = DOCS[doc]
labels = {f"{r['school']}_{r['year']}_{r['slot']}": r for r in json.load(open(f'{S}/questions.json')) if r['level'] == level}
data = []
for spec, paper, section in specs:
    qs = json.load(open(f'{S}/q_{spec}.json'))
    res = json.load(open(f'{S}/q_{spec}_res.json'))
    for key, q in qs.items():
        lab = labels[key]
        school, year, slot = lab['school'], lab['year'], lab['slot']
        qno = slot.split()[-1]
        sec = section
        if spec.startswith('h2p1'):
            sec = f"{section} — {H2P1_CLUSTER[qno]}"
        first = lab['topics'][0]
        primary = (PRIMARY_OVERRIDE.get(key) or first[:3]) if kind == 'structured' else \
            first[:5] if kind == 'essay' else first
        marks = sum(m or 0 for *_, m in q['parts']) or q.get('marks')
        rec = dict(school=school, year=year, level=level, slot=slot, paper=paper, qno=qno, kind=kind, marks=marks,
                   topics=lab['topics'], primary=primary, stem=[sec] + q['stem'], parts=q['parts'], resources=res.get(key, []))
        if lab.get('fieldwork_area'):
            rec['fieldwork_area'] = lab['fieldwork_area']
        data.append(rec)
json.dump(data, open(out, 'w'), indent=1, ensure_ascii=False)
print(len(data), 'questions,', sum(len(r['resources']) for r in data), 'resources ->', out)
