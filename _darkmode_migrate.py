# -*- coding: utf-8 -*-
"""One-time, idempotent: add the early data-mode set to every page's <head>.

The inline head script already sets data-theme from localStorage before the CSS
paints (to avoid a flash of the wrong hue). Dark mode needs the same: set
data-mode from localStorage, or from the OS preference when the viewer has made
no explicit choice. Running again is a no-op.
"""
import io, os

OLD = "document.documentElement.dataset.theme=localStorage.getItem('mdrs_theme')||'lilac';"
NEW = ("var _r=document.documentElement;"
       "_r.dataset.theme=localStorage.getItem('mdrs_theme')||'lilac';"
       "_r.dataset.mode=localStorage.getItem('mdrs_mode')||"
       "(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light');")

changed = skipped = 0
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d != '.git']
    for fn in files:
        if not fn.endswith('.html'):
            continue
        p = os.path.join(root, fn)
        h = io.open(p, encoding='utf-8').read()
        if '_r.dataset.mode' in h:
            skipped += 1
            continue
        if OLD in h:
            io.open(p, 'w', encoding='utf-8', newline='\n').write(h.replace(OLD, NEW, 1))
            changed += 1

print('head script: %d changed, %d already current' % (changed, skipped))
