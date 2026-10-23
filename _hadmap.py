# -*- coding: utf-8 -*-
"""Map each of the 42 ḥadīth to its pages in the Arabic ʿUthaymīn sharḥ.

The sharḥ carries a running header naming the ḥadīth — «الحديث الثاني: …» —
so the start of each one can be read straight off the OCR. A ḥadīth then runs
to the page before the next one starts.

Two things this has to get right, both learned the hard way:

  * **Fold alif maqṣūra to yāʾ.** H12's header is printed «الحديث الثانى عشر»
    with ى where the ordinal is normally spelled with ي. Without that fold the
    header is missed on its real page (index 182) and the first match lands in
    the back matter at index 440, putting H12 after H41.
  * **Stop before the fihris**, which repeats every heading. It begins at
    index 440.

Folio offset for this file is **-1** — PDF index 40 carries printed folio 39,
index 41 carries 40, verified by rendering the pages and reading the numbers
rather than trusting OCR of the digits. Printed = index - 1.

`ranges()` returns {n: (first_printed, last_printed)} ready for
_hadbuild.provenance().
"""
import io, os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
OCR = os.path.join(BASE, 'assets', 'md', 'sharh-arbaeen-nawawi-uthaymin-ar.md')
PRINT_OFFSET = -1
BACK_MATTER = 440

ORD = ['الأول', 'الثاني', 'الثالث', 'الرابع', 'الخامس', 'السادس', 'السابع',
       'الثامن', 'التاسع', 'العاشر', 'الحادي عشر', 'الثاني عشر', 'الثالث عشر',
       'الرابع عشر', 'الخامس عشر', 'السادس عشر', 'السابع عشر', 'الثامن عشر',
       'التاسع عشر', 'العشرون', 'الحادي والعشرون', 'الثاني والعشرون',
       'الثالث والعشرون', 'الرابع والعشرون', 'الخامس والعشرون',
       'السادس والعشرون', 'السابع والعشرون', 'الثامن والعشرون',
       'التاسع والعشرون', 'الثلاثون', 'الحادي والثلاثون', 'الثاني والثلاثون',
       'الثالث والثلاثون', 'الرابع والثلاثون', 'الخامس والثلاثون',
       'السادس والثلاثون', 'السابع والثلاثون', 'الثامن والثلاثون',
       'التاسع والثلاثون', 'الأربعون', 'الحادي والأربعون', 'الثاني والأربعون']


def norm(t):
    t = re.sub(u'[ً-ْٰـ]', '', t)
    t = re.sub(u'[آأإٱ]', u'ا', t)
    return t.replace(u'ى', u'ي')          # alif maqsura -> ya'


def pages():
    raw = io.open(OCR, encoding='utf-8').read()
    parts = re.split(r'^## page (\d+)\s*$', raw, flags=re.M)
    return {int(parts[i]): norm(parts[i + 1]) for i in range(1, len(parts), 2)}


def starts():
    """{hadith number: first PDF page index}, monotonic."""
    pg = pages()
    out, floor = {}, 0
    for i, o in enumerate(ORD, 1):
        needle = norm('الحديث ' + o)
        hit = next((n for n in sorted(pg)
                    if n >= floor and n < BACK_MATTER and needle in pg[n]), None)
        if hit is None:
            raise AssertionError('no header found for hadith %d (%s)' % (i, o))
        out[i] = hit
        floor = hit            # headers appear in order; never look backwards
    return out


def ranges():
    """{hadith number: (first printed folio, last printed folio)}."""
    s = starts()
    out = {}
    for i in range(1, len(ORD) + 1):
        a = s[i]
        b = (s[i + 1] - 1) if i + 1 in s else (BACK_MATTER - 1)
        out[i] = (a + PRINT_OFFSET, max(a, b) + PRINT_OFFSET)
    return out


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    s, r = starts(), ranges()
    prev = -1
    bad = []
    for i in sorted(s):
        if s[i] <= prev:
            bad.append(i)
        prev = s[i]
    print('%-5s %-12s %-14s %s' % ('H', 'INDEX', 'PRINTED', 'pages'))
    print('-' * 46)
    for i in sorted(r):
        a, b = r[i]
        print('%-5d %-12s %-14s %d' % (i, s[i], 'ص %d-%d' % (a, b), b - a + 1))
    print('\n42 located, monotonic: %s' % ('YES' if not bad else 'NO %s' % bad))
    print('offset %d (printed = index %+d)' % (PRINT_OFFSET, PRINT_OFFSET))
