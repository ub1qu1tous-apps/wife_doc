"""Crop every H2 Insert's resources with tools/crop_resources.py -> $SCRATCH/full/img/<year>_<SCHOOL>_H2P1|H2P2/R*.png.
Runs 6 at a time. Then run manual_fixes.py."""
import concurrent.futures as cf, hashlib, json, os, subprocess

S = os.environ.get('SCRATCH', '/tmp/wife_doc_scratch')


def pdf(f):
    if f.endswith('.pdf'):
        return 'sources/' + f
    return f'{S}/pdfcache/{hashlib.md5(f.encode()).hexdigest()[:10]}/' + os.path.splitext(os.path.basename(f))[0] + '.pdf'


jobs = []
for s, y, q1, i1, q2, i2 in json.load(open('tools/h2_manifest.json')):
    jobs += [(f'{y}_{s}_H2P1', i1), (f'{y}_{s}_H2P2', i2)]


def run(job):
    tag, f = job
    r = subprocess.run(['python3', '-I', 'tools/crop_resources.py', pdf(f), f'{S}/full/img/{tag}'], capture_output=True, text=True)
    return tag, r.returncode, r.stderr[-300:], r.stdout


with cf.ThreadPoolExecutor(6) as ex:
    for tag, rc, err, out in ex.map(run, jobs):
        if rc:
            print(tag, 'ERR', err)
        for line in out.splitlines():
            if 'CONTINUED' in line:
                print(tag, line.split('/')[-1][:100])
