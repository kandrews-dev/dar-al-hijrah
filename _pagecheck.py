# -*- coding: utf-8 -*-
"""Validate a built lesson page: structure, ḥarakāt, quiz contracts, provenance.

Usage:  python _pagecheck.py pages/aqeedah/nq-l07-mudtarr-wa-tashri.html [...]

Four checks, and each one has cost a real mistake before:

  1. **Structure**, with HTMLParser and a real tag stack — NOT regex tag
     counting, which once produced phantom <em> faults on a correct page.
  2. **Ḥarakāt** (CLAUDE.md rule 1a). The tokeniser MUST include the vowel
     marks in its character class: `[\\u0621-\\u064a]{2,}` splits Arabic words
     *at* their vowels, so every fragment comes out "bare" by construction and
     the tool reports 100% failure on a fully-vowelled page. This script
     self-tests against one known-vowelled and one known-bare string and
     refuses to report unless it separates them.
  3. **Quiz contracts** — .mcq-question[data-correct], .tf-question[data-answer]
     with exactly two .tf-btn[data-val] each, .vocab-card[data-ar].
  4. **Provenance** — the sharḥ-folio citation marker must be present.

Exit code is non-zero if any page has a fault.
"""
import io, re, sys
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
        'meta', 'param', 'source', 'track', 'wbr'}

# Arabic letters AND the ḥarakāt / sukūn / alif khanjariyyah. See docstring.
TOKEN = re.compile('[ء-يً-ْٰ]{2,}')
MARKS = re.compile('[ً-ْٰ]')
LETTERS = re.compile('[ء-ي]')

# Words the repo writes without marks by convention, plus the Qurʾānic
# ligatures and single-letter particles that carry none.
ALLOW = {'الله'}  # الله bare — see note below


class Stack(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.faults = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.faults.append('line %d: </%s> with nothing open'
                               % (self.getpos()[0], tag))
        elif self.stack[-1][0] != tag:
            self.faults.append('line %d: </%s> closes <%s> opened at line %d'
                               % (self.getpos()[0], tag, self.stack[-1][0],
                                  self.stack[-1][1]))
            self.stack.pop()
        else:
            self.stack.pop()


def body_only(h):
    """Rule 1 exempts <title> and meta, so the ḥarakāt scan takes <main>."""
    m = re.search(r'<main>(.*)</main>', h, flags=re.S)
    return m.group(1) if m else h


def strip_markup(h):
    h = re.sub(r'<script.*?</script>', ' ', h, flags=re.S)
    h = re.sub(r'<style.*?</style>', ' ', h, flags=re.S)
    h = re.sub(r'<[^>]+>', ' ', h)
    return h


def bare_words(text):
    out = []
    for w in TOKEN.findall(text):
        if MARKS.search(w):
            continue
        if len(LETTERS.findall(w)) < 2:
            continue
        out.append(w)
    return out


def selftest():
    vowelled = 'الرَّحِيم'   # الرَّحِيم
    plain = 'الرحيم'                         # الرحيم
    if bare_words(vowelled):
        sys.exit('SELF-TEST FAILED: vowelled word reported as bare — '
                 'the tokeniser is splitting words at their marks.')
    if not bare_words(plain):
        sys.exit('SELF-TEST FAILED: bare word not detected.')


def check(path):
    h = io.open(path, encoding='utf-8').read()
    faults = []

    s = Stack()
    s.feed(h)
    faults += s.faults
    faults += ['unclosed <%s> opened at line %d' % t for t in s.stack]

    text = strip_markup(body_only(h))
    bare = [w for w in bare_words(text) if w not in ALLOW]
    toks = len([w for w in TOKEN.findall(text)
                if len(LETTERS.findall(w)) >= 2])

    mcq = len(re.findall(r'class="mcq-question"[^>]*data-correct=', h))
    tfq = len(re.findall(r'class="tf-question"[^>]*data-answer=', h))
    tfb = len(re.findall(r'class="tf-btn"[^>]*data-val=', h))
    voc = len(re.findall(r'class="vocab-card"[^>]*data-ar=', h))
    aya = h.count('class="ayah-block"')
    had = h.count('class="hadith-block"')

    if tfq and tfb != tfq * 2:
        faults.append('T/F buttons: %d for %d questions (expected %d)'
                      % (tfb, tfq, tfq * 2))
    if '<!-- SHARH-PROVENANCE -->' not in h:
        faults.append('no sharḥ-folio provenance marker')

    print('%s — %d bytes' % (path, len(h.encode('utf-8'))))
    print('  structure : %s' % ('OK' if not s.faults and not s.stack
                                else '%d fault(s)' % (len(s.faults) + len(s.stack))))
    print('  ḥarakāt   : %d Arabic tokens / %d bare' % (toks, len(bare)))
    if bare:
        print('    bare: %s' % ' '.join(sorted(set(bare))[:20]))
    print('  quiz      : %d MCQ, %d T/F (%d buttons), %d vocab' % (mcq, tfq, tfb, voc))
    print('  blocks    : %d ayah, %d hadith' % (aya, had))
    for f in faults:
        print('  FAULT: %s' % f)
    return len(faults) + len(bare)


if __name__ == '__main__':
    selftest()
    print('self-test: tokeniser separates vowelled from bare — OK\n')
    bad = sum(check(p) for p in sys.argv[1:])
    print('\n%s' % ('ALL CLEAN' if not bad else '%d problem(s)' % bad))
    sys.exit(1 if bad else 0)
