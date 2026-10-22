# -*- coding: utf-8 -*-
"""Detect OCR extracts whose "Arabic" is really mis-OCR'd Latin.

Why this exists
---------------
`_pdfcheck.py` already refuses to trust len(text) and counts characters in the
Arabic range instead, because a broken 8-bit encoding yields ~1,200 chars/page
of mojibake with ZERO Arabic. That check is necessary and is not sufficient.

An English book OCR'd with `-l ara` produces a file that is ~700 Arabic
characters per page and passes every test in _pdfcheck: it opens, the page
count matches, the extract covers the range, the density is high. It is still
unusable. That is exactly what happened to the Ibn 'Uthaymeen sharh of the
Nawawi 40: the PDF is an ENGLISH translation, it was OCR'd as Arabic, and the
194,962 "Arabic characters" are Arabic letters spelling nothing.

The test
--------
Real Arabic prose is saturated with a short list of function words -- من، في،
على، أن، ما، لا، قال، الله، هذا، عن، إلى. Mis-OCR'd Latin produces Arabic
letter-strings that almost never coincide with them. So: tokenise, and measure
what share of tokens are in that list. Arabic prose runs high; mojibake runs at
or near zero.

Self-tested below against one known-good and one known-bad extract before any
number it prints is believed.
"""
import io, os, re, sys, glob

sys.stdout.reconfigure(encoding='utf-8')

# Function words and ultra-common forms. Deliberately short and uncontroversial:
# every one of these appears constantly in any Arabic religious prose.
COMMON = set(u"""من في على عن إلى أن إن ما لا قال الله هذا هذه ذلك التي الذي
و أو ثم قد كان كل بن بين عليه وسلم صلى رضي تعالى عز وجل أي يعني أهل قوله
له لم لن هو هي هم إذا حتى بعد قبل عند مع غير سبحانه رسول النبي كتاب باب""".split())

MARKS = u'[ً-ٰٓـ]'


def tokens(t):
    t = re.sub(MARKS, '', t)
    t = re.sub(u'[آأإٱ]', u'ا', t)
    return re.findall(u'[ء-ي]{1,}', t)


def score(text):
    """Share of tokens that are common Arabic words. Real prose >> mojibake."""
    tk = tokens(text)
    if len(tk) < 50:
        return None, len(tk)
    hit = sum(1 for w in tk if w in COMMON)
    return hit / float(len(tk)), len(tk)


# --------------------------------------------------------------- self-test
# Nothing this script prints is trusted until it separates a known-good extract
# from a known-bad one by a wide margin.
GOOD = 'assets/md/sharh-wasitiyyah-fawzan.md'     # real Arabic, built 54 lessons from it
BAD = 'assets/md/sharh-arbaeen-nawawi-uthaymin.md'  # English book OCR'd as Arabic

print('self-test')
ok = True
for label, path in (('known GOOD', GOOD), ('known BAD ', BAD)):
    if not os.path.exists(path):
        print('  %s  %-46s MISSING -- cannot self-test' % (label, path))
        ok = False
        continue
    s, n = score(io.open(path, encoding='utf-8').read())
    print('  %s  %-46s %5.1f%% common-word tokens (%d tokens)'
          % (label, os.path.basename(path), (s or 0) * 100, n))
    # Measured: the good extract scores 18.3%, the bad one 4.6% -- a 4x gap.
    # The bars sit either side of that gap with margin, and are set from the
    # measurement rather than guessed (a first pass guessed 20%, which the
    # good file failed, and the self-test correctly refused to run).
    if label.startswith('known GOOD') and (s is None or s < 0.14):
        ok = False
    if label.startswith('known BAD') and (s is not None and s > 0.07):
        ok = False
if not ok:
    sys.exit('self-test FAILED -- the detector does not separate the two known '
             'cases, so its verdicts on other files mean nothing')
print('  -> separates the two known cases. Tool trusted.\n')

THRESH = 0.10          # between the measured 4.6% and 18.3%, with margin either side

print('%-52s %8s %9s  %s' % ('EXTRACT', 'TOKENS', 'COMMON%', 'VERDICT'))
print('-' * 86)
bad = []
for f in sorted(glob.glob('assets/md/*.md')):
    s, n = score(io.open(f, encoding='utf-8').read())
    if s is None:
        v = 'too short to judge (%d tokens)' % n
    elif s < THRESH:
        v = '!! NOT ARABIC PROSE -- re-OCR with the right -l'
        bad.append(os.path.basename(f))
    else:
        v = 'ok'
    print('%-52s %8d %8.1f%%  %s' % (os.path.basename(f)[:52], n, (s or 0) * 100, v))

print('\n%d extract(s) failed' % len(bad))
for b in bad:
    print('   !! %s' % b)
sys.exit(1 if bad else 0)
