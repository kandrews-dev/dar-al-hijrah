# -*- coding: utf-8 -*-
"""Render a page range of a (possibly scanned) PDF to PNGs for visual reading.

    python _renderbook.py "<abs pdf path>" <first> <last> <out_dir> [dpi]

Used to extract vocabulary from the Bayna Yadayk / IMSIU scans by rendering
each page and reading it by eye (ground truth), rather than trusting OCR on
fully-vowelled Arabic. Pages are written as p<NNN>.png (0-indexed, matching
PyMuPDF page numbers). Keep the copyrighted source PDFs OUT of the repo — read
them from their own location and render into the scratchpad.
"""
import os, sys
import fitz  # PyMuPDF

pdf = sys.argv[1]
first = int(sys.argv[2])
last = int(sys.argv[3])
out_dir = sys.argv[4]
dpi = int(sys.argv[5]) if len(sys.argv) > 5 else 200

os.makedirs(out_dir, exist_ok=True)
doc = fitz.open(pdf)
last = min(last, doc.page_count - 1)
for i in range(first, last + 1):
    png = os.path.join(out_dir, 'p%03d.png' % i)
    doc.load_page(i).get_pixmap(dpi=dpi).save(png)
    print('wrote', png)
print('done: pages %d-%d of %d at %ddpi' % (first, last, doc.page_count, dpi))
