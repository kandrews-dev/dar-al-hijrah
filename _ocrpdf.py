# -*- coding: utf-8 -*-
"""OCR a scanned Arabic PDF in assets/pdfs/ to a text extract in assets/md/.

    python _ocrpdf.py <stem> [first_page] [last_page]

e.g. python _ocrpdf.py sharh-qawaid-arba-al-shaykh

Renders each page with PyMuPDF at 300dpi and runs Tesseract with the user-local
Arabic traineddata. Scanned mutun need this; pypdf returns 0 chars on them.
Output: assets/md/<stem>.md, one "## page N" heading per source page, so a later
session can grep the matn and sharh without re-reading the PDF.
"""
import io, os, sys, subprocess, tempfile

TESS = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
TESSDATA = r'C:\Users\abdul\tessdata-local'
BASE = os.path.dirname(os.path.abspath(__file__))

stem = sys.argv[1]
first = int(sys.argv[2]) if len(sys.argv) > 2 else 0
last = int(sys.argv[3]) if len(sys.argv) > 3 else None

import fitz  # PyMuPDF

pdf = os.path.join(BASE, 'assets', 'pdfs', stem + '.pdf')
out = os.path.join(BASE, 'assets', 'md', stem + '.md')
doc = fitz.open(pdf)
n = doc.page_count
last = n - 1 if last is None else min(last, n - 1)

sys.stderr.write('OCR %s: pages %d-%d of %d\n' % (stem, first, last, n))
chunks = ['# %s\n' % stem,
          '_OCR of assets/pdfs/%s.pdf (%d pages) via Tesseract ara. '
          'Machine-read: verify any wording before quoting it on a lesson page._\n' % (stem, n)]
tmp = tempfile.mkdtemp()
for i in range(first, last + 1):
    png = os.path.join(tmp, 'p.png')
    doc.load_page(i).get_pixmap(dpi=300).save(png)
    base = os.path.join(tmp, 'o')
    r = subprocess.run([TESS, png, base, '-l', 'ara', '--tessdata-dir', TESSDATA,
                        '--psm', '6'], capture_output=True)
    txt = ''
    if os.path.exists(base + '.txt'):
        txt = io.open(base + '.txt', encoding='utf-8', errors='replace').read().strip()
    chunks.append('\n## page %d\n\n%s\n' % (i, txt if txt else '_(no text recovered)_'))
    if (i - first) % 10 == 0:
        sys.stderr.write('  ...page %d\n' % i)
io.open(out, 'w', encoding='utf-8', newline='\n').write('\n'.join(chunks))
sys.stderr.write('wrote assets/md/%s.md (%d chars)\n'
                 % (stem, sum(len(c) for c in chunks)))
