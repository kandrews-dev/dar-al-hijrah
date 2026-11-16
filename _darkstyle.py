# -*- coding: utf-8 -*-
"""Give each lesson page's own <style> block a dark-mode pass.

Many lesson pages define bespoke didactic components (.scenario, .pillar,
.name-study …) in an inline <style> block with hardcoded light backgrounds
and/or dark text. The global inline catch-alls in main.css only reach
style="" attributes, not <style>-block class rules, so these boxes stay
light (or go dark-on-dark) in dark mode.

This reads each page's <style> rules and, for every selector that sets a
light background or a dark text colour, appends a
    :root[data-mode="dark"] <selector> { background/color: <dark/light> }
override into the same <style> block. Luminance decides light vs dark, and
tinted surfaces/text keep their hue (via HSL) so colour-coding survives.

Idempotent: a block already carrying the marker is skipped. Exam pages are
handled globally in main.css and are excluded.
"""
import re, io, sys, glob, colorsys
sys.stdout.reconfigure(encoding='utf-8')

MARK = '/* __darkpass__ */'

def parse_hex(v):
    v = v.strip().lower()
    if v == 'white': return (1.0, 1.0, 1.0)
    if v == 'black': return (0.0, 0.0, 0.0)
    m = re.fullmatch(r'#([0-9a-f]{3})', v)
    if m:
        return tuple(int(c*2, 16)/255 for c in m.group(1))
    m = re.fullmatch(r'#([0-9a-f]{6})', v)
    if m:
        s = m.group(1)
        return tuple(int(s[i:i+2], 16)/255 for i in (0, 2, 4))
    return None

def lum(rgb):  # perceptual-ish
    r, g, b = rgb
    return 0.2126*r + 0.7152*g + 0.0722*b

def to_hex(rgb):
    return '#' + ''.join('%02x' % max(0, min(255, round(c*255))) for c in rgb)

def dark_bg(rgb):
    """A light background → a dark surface of the same hue (neutral → token)."""
    h, l, s = colorsys.rgb_to_hls(*rgb)
    if s < 0.10:
        return 'var(--surface)'
    r, g, b = colorsys.hls_to_rgb(h, 0.11, min(s, 0.45))
    return to_hex((r, g, b))

def light_text(rgb):
    """A dark text colour → a legible light tint of the same hue."""
    h, l, s = colorsys.rgb_to_hls(*rgb)
    if s < 0.10:
        return 'var(--ink)'
    r, g, b = colorsys.hls_to_rgb(h, 0.74, min(s, 0.6))
    return to_hex((r, g, b))

decl = re.compile(r'(background(?:-color)?|color)\s*:\s*([^;{}]+)')

def build(styles):
    ov = []
    for sel, body in re.findall(r'([^{}]+)\{([^{}]*)\}', styles):
        sel = sel.strip()
        if (not sel or sel.startswith('@') or sel.startswith('/*')
                or ':root' in sel or '%' in sel or sel[0].isdigit()):
            continue
        outs = []
        for prop, val in decl.findall(body):
            val = val.strip(); rgb = parse_hex(val)
            if rgb is None:
                if prop.startswith('background') and re.match(r'rgba\(\s*0\s*,\s*0\s*,\s*0', val):
                    outs.append('background:rgba(255,255,255,.05)')
                continue
            if prop.startswith('background') and lum(rgb) >= 0.80:
                outs.append('background:%s' % dark_bg(rgb))
            elif prop == 'color' and lum(rgb) <= 0.45:
                outs.append('color:%s' % light_text(rgb))
        outs = list(dict.fromkeys(outs))
        if outs:
            ov.append(':root[data-mode="dark"] %s{%s!important}'
                      % (sel, ('!important;'.join(outs))))
    return ov

count = 0
for f in sorted(glob.glob('pages/**/*.html', recursive=True)):
    h = io.open(f, encoding='utf-8').read()
    m = re.search(r'<style>(.*?)</style>', h, re.S)
    if not m:
        continue
    styles = m.group(1)
    if '.exam-q' in styles or MARK in styles:
        continue
    ov = build(styles)
    if not ov:
        continue
    inject = '\n' + MARK + '\n' + '\n'.join(ov) + '\n'
    new_style = m.group(0)[:-len('</style>')] + inject + '</style>'
    h2 = h[:m.start()] + new_style + h[m.end():]
    io.open(f, 'w', encoding='utf-8', newline='\n').write(h2)
    count += 1
    print('%-46s +%d overrides' % (f, len(ov)))

print('\n%d pages patched' % count)
