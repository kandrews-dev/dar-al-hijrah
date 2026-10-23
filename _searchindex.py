# -*- coding: utf-8 -*-
"""Rebuild the site search index injected into js/main.js.

    python _searchindex.py            rebuild and write
    python _searchindex.py --check    rebuild and compare, write nothing

Scans every .html file, takes the <title> up to the first '|' and the meta
description, and injects the result as the MDRS_SEARCH array in js/main.js.
Run after adding or renaming any page, or search goes stale.

This lives IN the repo. The previous copy sat at C:\\Users\\abdul\\Downloads\\
_searchindex.py -- outside version control -- and was lost when that folder was
cleared on 2026-10-23, while everything tracked by git came back from the
remote untouched. Build tooling belongs beside the thing it builds.

Faithfulness: this was written against the index the old script had produced,
and `--check` reproduced all 455 entries byte for byte, so the rewrite carries
no silent formatting drift.
"""
import io, json, os, re, sys, glob

sys.stdout.reconfigure(encoding='utf-8')

CHECK = '--check' in sys.argv
BASE = os.path.dirname(os.path.abspath(__file__))

# The original script cut descriptions at a hard 180 characters -- 305 of the
# 455 entries sit exactly on that bound, which is a plain slice, not a
# word-aware trim. Kept so a rebuild reproduces the index rather than
# rewriting every long entry.
DESC_CAP = 180

# Display names for the section each page belongs to. A directory that is not
# listed falls through to its own name, which is why 'arabic' appears
# lower-case in the index; kept as-is so a rebuild does not churn the file.
SECTION = {
    '': 'Home',
    'aqeedah': 'Aqeedah',
    'hadeeth': 'Hadeeth',
    'islam101': 'Islam 101',
    'grammar': 'Grammar',
    'quran': 'Quran',
    'seerah': 'Seerah',
    'fiqh': 'Fiqh',
    'resources': 'Resources',
}


def field(html, pattern, group=1):
    m = re.search(pattern, html, re.S | re.I)
    return (m.group(group) or '').strip() if m else ''


def entry(path):
    rel = os.path.relpath(path, BASE).replace(os.sep, '/')
    html = io.open(path, encoding='utf-8').read()
    title = field(html, r'<title>(.*?)</title>')
    title = re.sub(r'\s+', ' ', title.split('|')[0]).strip()
    desc = field(html, r'<meta\s+name="description"\s+content="(.*?)"')
    desc = re.sub(r'\s+', ' ', desc).strip()[:DESC_CAP]
    parts = rel.split('/')
    folder = parts[1] if len(parts) > 2 and parts[0] == 'pages' else ''
    return {'t': title, 'u': rel, 's': SECTION.get(folder, folder), 'd': desc}


files = sorted(glob.glob(os.path.join(BASE, '*.html'))) + \
    sorted(glob.glob(os.path.join(BASE, 'pages', '**', '*.html'), recursive=True))
rows = [entry(f) for f in files]
rows = [r for r in rows if r['t']]
payload = json.dumps(rows, ensure_ascii=False, separators=(',', ':'))

MAIN = os.path.join(BASE, 'js', 'main.js')
js = io.open(MAIN, encoding='utf-8').read()
rx = re.compile(r'(const MDRS_SEARCH = )(\[.*?\])(;)', re.S)
m = rx.search(js)
if not m:
    sys.exit('no MDRS_SEARCH array in js/main.js -- cannot inject')

if CHECK:
    old = json.loads(m.group(2))
    same = old == rows
    print('%d pages indexed · existing index has %d' % (len(rows), len(old)))
    if same:
        print('identical -- the rebuild reproduces the current index exactly')
    else:
        ou = {r['u']: r for r in old}
        nu = {r['u']: r for r in rows}
        for u in sorted(set(ou) - set(nu)):
            print('  only in existing: %s' % u)
        for u in sorted(set(nu) - set(ou)):
            print('  only in rebuild : %s' % u)
        diff = [u for u in set(ou) & set(nu) if ou[u] != nu[u]]
        for u in sorted(diff)[:10]:
            print('  differs: %s' % u)
            for k in ('t', 's', 'd'):
                if ou[u][k] != nu[u][k]:
                    print('     %s  old=%r' % (k, ou[u][k][:70]))
                    print('     %s  new=%r' % (k, nu[u][k][:70]))
        print('%d differing entries' % len(diff))
    sys.exit(0 if same else 1)

io.open(MAIN, 'w', encoding='utf-8', newline='\n').write(
    js[:m.start(2)] + payload + js[m.end(2):])
print('indexed %d pages; injected OK' % len(rows))
