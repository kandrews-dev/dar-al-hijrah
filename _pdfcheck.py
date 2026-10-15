# -*- coding: utf-8 -*-
"""Integrity check for every source PDF and its OCR extract.

Checks, per PDF:
  1. opens at all, and is not encrypted
  2. page count
  3. whether it has a real Arabic text layer -- counting characters in the
     Arabic range [\u0621-\u064a], NOT raw len(). A broken legacy 8-bit
     encoding returns ~1,200 chars/page of mojibake with ZERO Arabic, and
     counting len() once made me tell the user a scanned print had a text
     layer. Sampled across the whole document, not just page 1.
  4. whether a matching extract exists in assets/md/
  5. whether the extract's "## page N" markers cover the PDF's page count --
     a short extract means a truncated OCR run, and any lesson built from the
     missing pages would be built from nothing.
  6. Arabic density per extracted page, to catch pages that OCR'd to noise.

Exit code is non-zero if any PDF fails to open or any extract is short.
"""
import io, os, re, sys, glob

sys.stdout.reconfigure(encoding='utf-8')
AR = u'[\u0621-\u064a]'

try:
    import pypdf
except ImportError:
    print('pypdf not installed'); sys.exit(2)

PDF_DIRS = ['assets/pdfs']
EXTRA = "C:/Users/abdul/OneDrive/Documents/Arabic Pdf's"
if os.path.isdir(EXTRA):
    PDF_DIRS.append(EXTRA)

MD = {os.path.basename(p)[:-3]: p for p in glob.glob('assets/md/*.md')}

problems = []
rows = []

for d in PDF_DIRS:
    for p in sorted(glob.glob(os.path.join(d, '*.pdf'))):
        base = os.path.basename(p)
        stem = base[:-4]
        size = os.path.getsize(p)
        row = {'file': base, 'dir': d, 'mb': size / 1048576.0}
        try:
            r = pypdf.PdfReader(p)
            enc = bool(getattr(r, 'is_encrypted', False))
            n = len(r.pages)
            row['pages'] = n
            row['enc'] = enc
            if enc:
                problems.append((base, 'ENCRYPTED'))
            # sample up to 12 pages spread across the document
            idx = sorted(set(int(i * (n - 1) / 11.0) for i in range(12))) if n > 1 else [0]
            raw = arab = 0
            for i in idx:
                try:
                    t = r.pages[i].extract_text() or ''
                except Exception:
                    t = ''
                raw += len(t)
                arab += len(re.findall(AR, t))
            row['raw'] = raw
            row['arab'] = arab
            row['layer'] = 'text' if arab > 200 else ('MOJIBAKE' if raw > 400 else 'scanned')
            if raw > 400 and arab <= 200:
                problems.append((base, 'raw text present but 0 Arabic -- broken encoding, '
                                       'treat as scanned'))
        except OSError as e:
            # Errno 22 (EINVAL) on a file that HAS a size in the directory listing
            # means a OneDrive Files-On-Demand placeholder: the bytes are in the
            # cloud, not on this disk. The PDF is not corrupt -- it is not here.
            row['pages'] = None
            if e.errno == 22:
                row['layer'] = 'CLOUD-ONLY'
                problems.append((base, 'OneDrive placeholder -- not downloaded locally '
                                       '(not corrupt; right-click > Always keep on this device)'))
            else:
                row['layer'] = 'UNREADABLE'
                problems.append((base, 'CANNOT OPEN: errno %s %s' % (e.errno, str(e)[:60])))
            rows.append(row)
            continue
        except Exception as e:
            row['pages'] = None
            row['layer'] = 'UNREADABLE'
            problems.append((base, 'CANNOT OPEN: %s' % str(e)[:80]))
            rows.append(row)
            continue

        # matching extract?
        ex = MD.get(stem)
        if ex is None:
            # try a looser match on the stem
            for k, v in MD.items():
                if k in stem or stem in k:
                    ex = v; break
        if ex:
            h = io.open(ex, encoding='utf-8').read()
            marks = [int(m.group(1)) for m in re.finditer(r'^## page (\d+)', h, re.M)]
            row['md'] = os.path.basename(ex)
            row['md_pages'] = len(marks)
            row['md_max'] = max(marks) if marks else 0
            row['md_arab'] = len(re.findall(AR, h))
            # _ocrpdf.py numbers its markers 0-BASED, so "## page 207" is the
            # 208th page. Compare the COUNT of markers, not the highest number --
            # comparing max() flagged all four complete extracts as truncated.
            if marks and row['pages'] and len(marks) < row['pages']:
                problems.append((base, 'EXTRACT SHORT: %d pages extracted of %d'
                                 % (len(marks), row['pages'])))
            if marks:
                dens = row['md_arab'] / float(len(marks))
                row['dens'] = dens
                if dens < 150:
                    problems.append((base, 'extract Arabic density only %d chars/page '
                                           '-- OCR may be noise' % dens))
        else:
            row['md'] = None
        rows.append(row)

print('=' * 100)
print('%-46s %5s %6s %-9s %-30s' % ('FILE', 'PAGES', 'MB', 'LAYER', 'EXTRACT'))
print('=' * 100)
cur = None
for r in rows:
    if r['dir'] != cur:
        cur = r['dir']
        print('\n--- %s ---' % cur)
    ex = r.get('md')
    exs = ''
    if ex:
        exs = '%s  p1-%s' % (ex[:22], r.get('md_max'))
        if r.get('dens'):
            exs += ' (%d ch/pg)' % r['dens']
    elif r.get('pages'):
        exs = '(no extract)'
    print('%-46s %5s %6.1f %-9s %-30s'
          % (r['file'][:46], r.get('pages'), r['mb'], r.get('layer'), exs))

print()
print('=' * 100)
if problems:
    print('PROBLEMS: %d' % len(problems))
    for f, m in problems:
        print('  !! %-44s %s' % (f[:44], m))
else:
    print('PROBLEMS: 0 -- every PDF opens, and every extract covers its full page range.')
sys.exit(1 if any('CANNOT OPEN' in m or 'EXTRACT SHORT' in m or 'ENCRYPTED' in m
                  for _, m in problems) else 0)
