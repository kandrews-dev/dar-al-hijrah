# -*- coding: utf-8 -*-
"""Verify every quoted ayah on the site against the Uthmani mushaf.

    python _verifyayat.py

Reads each <div class="ayah-block">: the Arabic in .ayah-arabic must actually
occur at the surah:ayah cited in .ayah-source. Comparison is on the consonantal
skeleton (diacritics and alif-carriers dropped, alif-maqsura unified with ya',
the Uthmani waw-spellings of al-salah/al-zakah/al-hayah folded in) so that the
imla'i orthography used on the pages compares equal to the Uthmani text, while a
wrong surah or ayah number still fails loudly.

The self-test at the top asserts five known-good citations verify. If it fails,
the TOOL is broken, not the site -- fix it before trusting any output.
Cache: .quran-uthmani.json (git-ignored, fetched once).
"""
import re, io, os, json, glob, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.quran-uthmani.json')
if not os.path.exists(CACHE):
    import urllib.request
    sys.stderr.write('fetching quran-uthmani (one time) ...' + chr(10))
    with urllib.request.urlopen('https://api.alquran.cloud/v1/quran/quran-uthmani', timeout=120) as r:
        io.open(CACHE, 'w', encoding='utf-8').write(r.read().decode('utf-8'))
Q = json.load(io.open(CACHE, encoding='utf-8'))['data']['surahs']
TEXT = {}
NAMES = {}
for s in Q:
    NAMES[s['number']] = s['englishName']
    for a in s['ayahs']:
        TEXT[(s['number'], a['numberInSurah'])] = a['text']

ALIF = set([0x622, 0x623, 0x625, 0x627, 0x671, 0x621])


def skel(t):
    """Consonantal skeleton so Uthmani and imla'i orthography compare equal."""
    t = unicodedata.normalize('NFC', t)
    out = []
    for c in t:
        o = ord(c)
        if 0x610 <= o <= 0x61A or 0x64B <= o <= 0x65F or 0x6D6 <= o <= 0x6ED or o == 0x670:
            continue
        if o in ALIF:
            continue
        if o == 0x649:
            out.append(u'\u064A'); continue
        if o == 0x624:
            out.append(u'\u0648'); continue
        if o == 0x626:
            out.append(u'\u064A'); continue
        if o == 0x629:
            out.append(u'\u0647'); continue
        if o == 0x640:
            continue
        out.append(c if 0x622 <= o <= 0x64A else ' ')
    r = re.sub(r'\s+', ' ', ''.join(out)).strip()
    # Uthmani writes these with waw; imla'i with alif (already stripped) - unify
    for a, b in ((u'لصلوه', u'لصله'),
                 (u'لزكوه', u'لزكه'),
                 (u'لحيوه', u'لحيه'),
                 (u'ربو', u'رب')):
        r = r.replace(a, b)
    return r


# ---- self-test: known-correct citations MUST verify, else the tool is wrong ----
T = [
    (54, 49, u'\u0625\u0650\u0646\u0651\u064E\u0627 \u0643\u064F\u0644\u0651\u064E \u0634\u064E\u064A\u0652\u0621\u064D \u062E\u064E\u0644\u064E\u0642\u0652\u0646\u064E\u0627\u0647\u064F \u0628\u0650\u0642\u064E\u062F\u064E\u0631\u064D'),
    (8, 39, u'\u0648\u064E\u0642\u064E\u0627\u062A\u0650\u0644\u064F\u0648\u0647\u064F\u0645\u0652 \u062D\u064E\u062A\u0651\u064E\u0649 \u0644\u064E\u0627 \u062A\u064E\u0643\u064F\u0648\u0646\u064E \u0641\u0650\u062A\u0652\u0646\u064E\u0629\u064C'),
    (42, 11, u'\u0644\u064E\u064A\u0652\u0633\u064E \u0643\u064E\u0645\u0650\u062B\u0652\u0644\u0650\u0647\u0650 \u0634\u064E\u064A\u0652\u0621\u064C'),
    (16, 36, u'\u0648\u064E\u0627\u062C\u0652\u062A\u064E\u0646\u0650\u0628\u064F\u0648\u0627 \u0627\u0644\u0637\u0651\u064E\u0627\u063A\u064F\u0648\u062A\u064E'),
    (31, 13, u'\u0644\u064E\u0627 \u062A\u064F\u0634\u0652\u0631\u0650\u0643\u0652 \u0628\u0650\u0627\u0644\u0644\u0651\u064E\u0647\u0650'),
]
_n = lambda z: skel(z).replace(' ', '')
fail = [x for x in T if _n(x[2]) not in _n(TEXT[(x[0], x[1])])]
if fail:
    print("SELF-TEST FAILED - the tool is wrong, not the site:")
    for s, a, q in fail:
        print("  %d:%d\n   page : %s\n   quran: %s" % (s, a, skel(q), skel(TEXT[(s, a)])))
    sys.exit(1)
print("self-test: %d/%d known-good citations verify. Tool trusted.\n" % (len(T), len(T)))


def key(s):
    s = re.sub(u'^\\s*(\u0633\u064F?\u0648\u0631\u064E?\u0629\u064F?)\\s*', '', s.strip())
    s = re.sub(r'^(S[uū]rat|S[uū]rah|Sura)\s+', '', s, flags=re.I)
    s = s.lower()
    for a, b in [(u'ā', 'a'), (u'ī', 'i'), (u'ū', 'u'), (u'ḥ', 'h'), (u'ṣ', 's'), (u'ḍ', 'd'),
                 (u'ṭ', 't'), (u'ẓ', 'z'), (u'ḏ', 'd'), (u'ṯ', 't'), (u'ʿ', ''), (u'ʾ', ''),
                 (u'ʼ', ''), (u'’', ''), ("'", ''), ('-', ''), (' ', ''), ('.', ''), (u'·', '')]:
        s = s.replace(a, b)
    return re.sub(r'^(al|ash|ar|at|ad|as|az)', '', s)


NUM = {}
for n, en in NAMES.items():
    NUM.setdefault(key(en), n)
NUM.update({'fatihah': 1, 'baqarah': 2, 'alimran': 3, 'imran': 3, 'nisa': 4, 'maidah': 5,
    'anam': 6, 'araf': 7, 'anfal': 8, 'tawbah': 9, 'yunus': 10, 'hud': 11, 'yusuf': 12,
    'rad': 13, 'ibrahim': 14, 'hijr': 15, 'nahl': 16, 'isra': 17, 'kahf': 18, 'maryam': 19,
    'taha': 20, 'anbiya': 21, 'hajj': 22, 'muminun': 23, 'nur': 24, 'furqan': 25, 'shuara': 26,
    'qasas': 28, 'ankabut': 29, 'rum': 30, 'luqman': 31, 'sajdah': 32, 'ahzab': 33, 'saba': 34,
    'fatir': 35, 'yasin': 36, 'saffat': 37, 'sad': 38, 'zumar': 39, 'ghafir': 40, 'mumin': 40,
    'fussilat': 41, 'shura': 42, 'zukhruf': 43, 'dukhan': 44, 'jathiyah': 45, 'ahqaf': 46,
    'muhammad': 47, 'fath': 48, 'hujurat': 49, 'qaf': 50, 'dhariyat': 51, 'tur': 52, 'najm': 53,
    'qamar': 54, 'rahman': 55, 'waqiah': 56, 'hadid': 57, 'mujadilah': 58, 'hashr': 59,
    'mumtahanah': 60, 'saff': 61, 'jumuah': 62, 'munafiqun': 63, 'taghabun': 64, 'talaq': 65,
    'tahrim': 66, 'mulk': 67, 'qalam': 68, 'haqqah': 69, 'maarij': 70, 'nuh': 71, 'jinn': 72,
    'muzzammil': 73, 'muddaththir': 74, 'qiyamah': 75, 'insan': 76, 'mursalat': 77, 'naba': 78,
    'naziat': 79, 'abasa': 80, 'takwir': 81, 'infitar': 82, 'mutaffifin': 83, 'inshiqaq': 84,
    'buruj': 85, 'tariq': 86, 'ala': 87, 'ghashiyah': 88, 'fajr': 89, 'balad': 90, 'shams': 91,
    'layl': 92, 'duha': 93, 'sharh': 94, 'inshirah': 94, 'tin': 95, 'alaq': 96, 'qadr': 97,
    'bayyinah': 98, 'zalzalah': 99, 'adiyat': 100, 'qariah': 101, 'takathur': 102, 'asr': 103,
    'humazah': 104, 'fil': 105, 'quraysh': 106, 'maun': 107, 'kawthar': 108, 'kafirun': 109,
    'nasr': 110, 'masad': 111, 'lahab': 111, 'ikhlas': 112, 'falaq': 113, 'nas': 114})

ARN = {u'\u0627\u0644\u0641\u0627\u062A\u062D\u0629': 1, u'\u0627\u0644\u0628\u0642\u0631\u0629': 2,
    u'\u0622\u0644 \u0639\u0645\u0631\u0627\u0646': 3, u'\u0627\u0644\u0646\u0633\u0627\u0621': 4,
    u'\u0627\u0644\u0645\u0627\u0626\u062F\u0629': 5, u'\u0627\u0644\u0623\u0646\u0639\u0627\u0645': 6,
    u'\u0627\u0644\u0623\u0639\u0631\u0627\u0641': 7, u'\u0627\u0644\u0623\u0646\u0641\u0627\u0644': 8,
    u'\u0627\u0644\u062A\u0648\u0628\u0629': 9, u'\u064A\u0648\u0646\u0633': 10, u'\u0647\u0648\u062F': 11,
    u'\u064A\u0648\u0633\u0641': 12, u'\u0627\u0644\u0631\u0639\u062F': 13, u'\u0625\u0628\u0631\u0627\u0647\u064A\u0645': 14,
    u'\u0627\u0644\u062D\u062C\u0631': 15, u'\u0627\u0644\u0646\u062D\u0644': 16, u'\u0627\u0644\u0625\u0633\u0631\u0627\u0621': 17,
    u'\u0627\u0644\u0643\u0647\u0641': 18, u'\u0645\u0631\u064A\u0645': 19, u'\u0637\u0647': 20,
    u'\u0627\u0644\u0623\u0646\u0628\u064A\u0627\u0621': 21, u'\u0627\u0644\u062D\u062C': 22,
    u'\u0627\u0644\u0645\u0624\u0645\u0646\u0648\u0646': 23, u'\u0627\u0644\u0646\u0648\u0631': 24,
    u'\u0627\u0644\u0641\u0631\u0642\u0627\u0646': 25, u'\u0627\u0644\u0634\u0639\u0631\u0627\u0621': 26,
    u'\u0627\u0644\u0642\u0635\u0635': 28, u'\u0627\u0644\u0639\u0646\u0643\u0628\u0648\u062A': 29,
    u'\u0627\u0644\u0631\u0648\u0645': 30, u'\u0644\u0642\u0645\u0627\u0646': 31, u'\u0627\u0644\u0633\u062C\u062F\u0629': 32,
    u'\u0627\u0644\u0623\u062D\u0632\u0627\u0628': 33, u'\u0641\u0627\u0637\u0631': 35, u'\u064A\u0633': 36,
    u'\u0627\u0644\u0635\u0627\u0641\u0627\u062A': 37, u'\u0627\u0644\u0632\u0645\u0631': 39, u'\u0641\u0635\u0644\u062A': 41,
    u'\u0627\u0644\u0634\u0648\u0631\u0649': 42, u'\u0645\u062D\u0645\u062F': 47, u'\u0627\u0644\u0641\u062A\u062D': 48,
    u'\u0627\u0644\u062D\u062C\u0631\u0627\u062A': 49, u'\u0627\u0644\u0630\u0627\u0631\u064A\u0627\u062A': 51,
    u'\u0627\u0644\u0646\u062C\u0645': 53, u'\u0627\u0644\u0642\u0645\u0631': 54, u'\u0627\u0644\u0631\u062D\u0645\u0646': 55,
    u'\u0627\u0644\u062D\u062F\u064A\u062F': 57, u'\u0627\u0644\u062D\u0634\u0631': 59, u'\u0627\u0644\u0645\u0644\u0643': 67,
    u'\u0627\u0644\u062C\u0646': 72, u'\u0627\u0644\u0625\u0646\u0633\u0627\u0646': 76, u'\u0627\u0644\u0639\u0644\u0642': 96,
    u'\u0627\u0644\u0642\u064A\u0627\u0645\u0629': 75, u'\u0627\u0644\u0645\u0645\u062A\u062D\u0646\u0629': 60,
    u'\u0627\u0644\u0645\u062F\u0628\u0631': 74, u'\u0627\u0644\u0645\u062F\u062B\u0631': 74,
    u'\u0627\u0644\u0643\u0648\u062B\u0631': 108, u'\u0627\u0644\u0625\u062E\u0644\u0627\u0635': 112,
    u'\u0627\u0644\u0646\u0628\u0623': 78, u'\u0627\u0644\u0637\u0644\u0627\u0642': 65,
    u'\u0627\u0644\u0645\u062C\u0627\u062F\u0644\u0629': 58, u'\u0627\u0644\u0635\u0641': 61,
    u'\u0627\u0644\u062C\u0645\u0639\u0629': 62, u'\u0627\u0644\u0645\u0646\u0627\u0641\u0642\u0648\u0646': 63}

cit = re.compile(r'(\d{1,3})\s*:\s*(\d{1,3})(?:\s*[-\u2013\u2014]\s*(\d{1,3}))?')
NP = re.compile(u'([A-Za-z\u0100\u012A\u016A\u1E24\u1E62\u1E0C\u1E6C\u1E92\u02BF\u02BE]'
                u'[A-Za-z\u0101\u012B\u016B\u1E25\u1E63\u1E0D\u1E6D\u1E93\u0100\u012A\u016A'
                u'\u1E24\u1E62\u1E0C\u1E6C\u1E92\u02BF\u02BE\u02BC\'\u2019\\- ]{2,28}?)\\s*\\d{1,3}\\s*:')
blocks = re.compile(r'<div class="ayah-block".*?(?=<div class="ayah-block"|</main>)', re.S)
gar = re.compile(r'class="ayah-arabic"[^>]*>(.*?)</p>', re.S)
gsr = re.compile(r'class="ayah-source"[^>]*>(.*?)</p>', re.S)

ok = 0
probs = []
unres = []
for f in sorted(glob.glob('pages/**/*.html', recursive=True)) + sorted(glob.glob('*.html')):
    h = io.open(f, encoding='utf-8').read()
    for b in blocks.findall(h):
        ma, ms = gar.search(b), gsr.search(b)
        if not (ma and ms):
            continue
        ar = skel(re.sub('<[^>]+>', '', ma.group(1)))
        src = re.sub('<[^>]+>', '', ms.group(1)).strip()
        mc = cit.search(src)
        if not mc:
            unres.append((f, src, 'no n:n')); continue
        s, a1 = int(mc.group(1)), int(mc.group(2))
        a2 = int(mc.group(3)) if mc.group(3) else a1
        sn = None; shown = ''
        mn = NP.search(src)
        if mn:
            shown = mn.group(1).strip(); sn = NUM.get(key(shown))
        if sn is None:
            best = -1
            for an, n in sorted(ARN.items(), key=lambda kv: -len(kv[0])):
                i = src.rfind(an, 0, mc.start())
                if i > best:
                    best, sn, shown = i, n, an
            if best < 0:
                sn = None
                for an, n in sorted(ARN.items(), key=lambda kv: -len(kv[0])):
                    if an in src:
                        sn, shown = n, an; break
        if sn is None:
            unres.append((f, src, 'unresolved name "%s"' % shown)); continue
        if sn != s:
            probs.append((f, 'NAME-NUM', src, '"%s" = surah %d, cited %d' % (shown, sn, s))); continue
        hi = a2 + (12 if re.search(u'[,\u060C]\\s*\\d', src) else 0)
        pool = ' '.join(skel(TEXT.get((s, i), '')) for i in range(a1, hi + 1))
        if not pool.strip():
            probs.append((f, 'NO SUCH AYAH', src, '%d:%d' % (s, a1))); continue
        frags = [x.strip() for x in re.split(u'\\.\\.\\.|\u2026|\\s-\\s|\\s\u2014\\s', ar) if len(x.strip()) > 8]
        if not frags:
            frags = [ar] if len(ar) > 5 else []
        pw = set(w for w in pool.split() if len(w) > 1)
        aw = [w for w in ar.split() if len(w) > 1]
        if not aw:
            ok += 1; continue
        hit = sum(1 for w in aw if w in pw)
        score = hit / float(len(aw))
        nsp = lambda z: z.replace(' ', '')
        dy = lambda z: z.replace(u'ي', '')
        ar2, pool2 = dy(ar), dy(pool)
        pw2 = set(w for w in pool2.split() if len(w) > 1)
        aw2 = [w for w in ar2.split() if len(w) > 1]
        score2 = (sum(1 for w in aw2 if w in pw2) / float(len(aw2))) if aw2 else 1.0
        if nsp(ar) in nsp(pool) or score >= 0.80 or nsp(ar2) in nsp(pool2) or score2 >= 0.85:
            ok += 1
        else:
            probs.append((f, 'TEXT-REF %d%%' % round(score * 100), src,
                          ' '.join(w for w in aw if w not in pw)[:90]))

print("=== AYAH VERIFICATION (whole site) ===")
print("VERIFIED: %d   PROBLEMS: %d   UNPARSED: %d\n" % (ok, len(probs), len(unres)))
for p in probs:
    print("  [%s] %s\n     ref : %s\n     text: %s\n" % (p[1], p[0], p[2], p[3]))
print("--- unparsed (%d) ---" % len(unres))
for f, s, r in unres:
    print("  %s: %s   (%s)" % (f, s, r))
