# -*- coding: utf-8 -*-
"""Strip course-brochure copy: the "How we teach it" method notes, the
"Welcome to X" lesson openers, and the marketing tagline on the home page.

Each replacement keeps whatever TEACHING content the sentence carried and drops
only the frame around it. Nothing is deleted that was explaining something.

Targets are matched with whitespace-tolerant regexes, because the source wraps
lines mid-sentence. Each edit asserts exactly one match, and an edit whose
target is already gone is reported as "already applied" rather than failing --
so the script is safe to re-run.
"""
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')


def ws(s):
    """Literal text, but with every run of whitespace allowed to vary."""
    return r'\s+'.join(re.escape(w) for w in s.split())


EDITS = [

    # ---------------------------------------------------------------- roadmap
    # Keeps the pacing facts (books not calendars, 2-2.5 years, no further
    # vocabulary books) because a student needs them. Drops the comparison to
    # the Egyptian/Madinah institutes, the "every lesson is taught fully
    # on-page" claim, and the "destination, not a prerequisite" slogan.
    ('pages/arabic/roadmap.html',
     'How the two stages fit together — ملاحظة منهجية',
     'الوَتِيرَة · Pacing'),

    ('pages/arabic/roadmap.html',
     'Grammar stays light inside the lugha lessons and is taught in depth on the '
     'separate <a href="../grammar/index.html" '
     'style="color:var(--tab-grammar);font-weight:600">naḥw track</a> — exactly how '
     'the Egyptian and Madinah institutes do it. Every lesson is taught fully '
     'on-page; the classical texts are the destination, not a prerequisite.',
     'Grammar stays light inside the lugha lessons; it is taken in depth on the '
     'separate <a href="../grammar/index.html" '
     'style="color:var(--tab-grammar);font-weight:600">naḥw track</a>.'),

    # ------------------------------------------------------------- islam101 U1
    ('pages/islam101/u1-l0-intro.html',
     'Welcome to <strong>Islam 101</strong> — the foundation that the whole school '
     'is built upon. Before a person can worship Allah correctly,',
     'Before a person can worship Allah correctly,'),

    ('pages/islam101/u1-l0-intro.html',
     'Our school follows the same order — we begin, always, with knowledge.',
     'Knowledge comes first, and everything after it rests upon it.'),

    # ------------------------------------------------------------------- fiqh
    ('pages/fiqh/u1-l0-tahara-intro.html',
     'Welcome to Fiqh — the study of <em>how</em> to worship Allah correctly. We '
     'begin exactly where worship itself begins: with',
     'الفِقْه is the study of <em>how</em> to worship Allah correctly, and it begins '
     'where worship itself begins: with'),

    # ----------------------------------------------------------------- Book 3
    ('pages/arabic/vocab-25-mujizah.html',
     'Welcome to <strong>Book 3, Unit 1</strong>. Every prophet before Muḥammad ﷺ',
     'Every prophet before Muḥammad ﷺ'),

    # -------------------------------------------------------------- home page
    ('index.html',
     'shiʿr &amp; ʿarūḍ. The key to reading the classics.',
     'shiʿr &amp; ʿarūḍ.'),

    # ------------------------------------------------------------- dictionary
    ('pages/arabic/dictionary-index.html',
     ', so nothing is ever taught twice. Entries are built letter by letter, root by '
     'root, exactly as the source orders them.',
     '. Entries run letter by letter and root by root, in the order the source '
     'itself gives them.'),
]

done = skipped = 0
for f, old, new in EDITS:
    h = io.open(f, encoding='utf-8').read()
    rx = re.compile(ws(old))
    hits = rx.findall(h)
    if not hits:
        if new.split()[0] in h:
            print('  = already applied   %s' % f)
            skipped += 1
            continue
        raise AssertionError('%s: no match for\n  %s' % (f, old[:100]))
    assert len(hits) == 1, '%s: %d matches, expected 1' % (f, len(hits))
    io.open(f, 'w', encoding='utf-8', newline='\n').write(rx.sub(lambda m: new, h, 1))
    print('  * edited            %s' % f)
    done += 1

print('%d edits applied, %d already in place' % (done, skipped))
