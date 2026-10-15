# -*- coding: utf-8 -*-
"""Vowel the two mechanical harakat classes left in the site body (rule 1a):

  1. the Arabic surah name appended to an ayah reference line -- "سورة النساء"
  2. the recurring pious formulae -- سبحانه، تعالى، عز وجل، رضي الله عنه ...

Both are whole-phrase substitutions of strings that are currently BARE, so the
pass is idempotent: once vowelled, the bare form no longer occurs. Replacements
are ordered longest-first so that a short entry can never eat part of a longer
one (التوبة inside سورة التوبة, تعالى inside وتعالى).

<title>, <meta>, <script> and <style> are protected: rule 1 exempts titles and
meta descriptions for searchability, and vowelling them would hurt search.
"""
import io, re, sys, glob, os

sys.stdout.reconfigure(encoding='utf-8')

SURAHS = {
    u'البقرة': u'البَقَرَة', u'النحل': u'النَّحْل', u'النساء': u'النِّسَاء',
    u'الأعراف': u'الأَعْرَاف', u'المائدة': u'المَائِدَة', u'التوبة': u'التَّوْبَة',
    u'آل عمران': u'آلُ عِمْرَان', u'الأنعام': u'الأَنْعَام', u'الإسراء': u'الإِسْرَاء',
    u'الفرقان': u'الفُرْقَان', u'طه': u'طَه', u'لقمان': u'لُقْمَان',
    u'الأنفال': u'الأَنْفَال', u'الحديد': u'الحَدِيد', u'الذاريات': u'الذَّارِيَات',
    u'الزمر': u'الزُّمَر', u'الشعراء': u'الشُّعَرَاء', u'الشورى': u'الشُّورَى',
    u'الكهف': u'الكَهْف', u'النجم': u'النَّجْم', u'يونس': u'يُونُس',
    u'الأحزاب': u'الأَحْزَاب', u'الأنبياء': u'الأَنْبِيَاء', u'الحج': u'الحَجّ',
    u'الحشر': u'الحَشْر', u'الزخرف': u'الزُّخْرُف', u'القصص': u'القَصَص',
    u'القمر': u'القَمَر', u'المؤمنون': u'المُؤْمِنُون', u'فصلت': u'فُصِّلَت',
    u'الممتحنة': u'المُمْتَحَنَة', u'الإخلاص': u'الإِخْلَاص', u'التغابن': u'التَّغَابُن',
    u'الرحمن': u'الرَّحْمَن', u'الصافات': u'الصَّافَّات', u'الطور': u'الطُّور',
    u'المزمل': u'المُزَّمِّل', u'فاطر': u'فَاطِر', u'محمد': u'مُحَمَّد',
    u'هود': u'هُود', u'يوسف': u'يُوسُف', u'الجاثية': u'الجَاثِيَة',
    u'الحجرات': u'الحُجُرَات', u'العنكبوت': u'العَنْكَبُوت', u'الفتح': u'الفَتْح',
    u'القدر': u'القَدْر', u'القلم': u'القَلَم', u'القيامة': u'القِيَامَة',
    u'المدثر': u'المُدَّثِّر', u'البروج': u'البُرُوج', u'الجن': u'الجِنّ',
    u'الحاقة': u'الحَاقَّة', u'الحجر': u'الحِجْر', u'الرعد': u'الرَّعْد',
    u'الصف': u'الصَّفّ', u'الطلاق': u'الطَّلَاق', u'الفجر': u'الفَجْر',
    u'المجادلة': u'المُجَادِلَة', u'المطففين': u'المُطَفِّفِين', u'الملك': u'المُلْك',
    u'النمل': u'النَّمْل', u'النور': u'النُّور', u'الواقعة': u'الوَاقِعَة',
    u'غافر': u'غَافِر', u'مريم': u'مَرْيَم', u'نوح': u'نُوح', u'يس': u'يَس',
}

PAIRS = []
# "سورة X" first (longest), then the bare name on its own
for bare, vow in SURAHS.items():
    PAIRS.append((u'سورة ' + bare, u'سُورَةُ ' + vow))
PAIRS.append((u'سورة', u'سُورَة'))
for bare, vow in SURAHS.items():
    PAIRS.append((bare, vow))

# the recurring formulae and the handful of other bare strings in ref lines
PAIRS += [
    (u'صلوات الله وسلامه عليهما', u'صَلَوَاتُ اللهِ وَسَلَامُهُ عَلَيْهِمَا'),
    (u'صلوات الله وسلامه عليهم', u'صَلَوَاتُ اللهِ وَسَلَامُهُ عَلَيْهِمْ'),
    (u'صلوات الله وسلامه عليه', u'صَلَوَاتُ اللهِ وَسَلَامُهُ عَلَيْهِ'),
    (u'صلى الله عليه وسلم', u'صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ'),
    (u'نصيحة لقمان لابنه', u'نَصِيحَةُ لُقْمَانَ لِابْنِهِ'),
    (u'قال لقمان لابنه', u'قَالَ لُقْمَانُ لِابْنِهِ'),
    (u'سبحانه وتعالى', u'سُبْحَانَهُ وَتَعَالَى'),
    (u'رضي الله عنهن', u'رَضِيَ اللهُ عَنْهُنَّ'),
    (u'رضي الله عنهما', u'رَضِيَ اللهُ عَنْهُمَا'),
    (u'رضي الله عنها', u'رَضِيَ اللهُ عَنْهَا'),
    (u'رضي الله عنهم', u'رَضِيَ اللهُ عَنْهُمْ'),
    (u'رضي الله عنه', u'رَضِيَ اللهُ عَنْهُ'),
    (u'عليهما الصلاة والسلام', u'عَلَيْهِمَا الصَّلَاةُ وَالسَّلَام'),
    (u'عليهم الصلاة والسلام', u'عَلَيْهِمُ الصَّلَاةُ وَالسَّلَام'),
    (u'عليه الصلاة والسلام', u'عَلَيْهِ الصَّلَاةُ وَالسَّلَام'),
    (u'عليهما السلام', u'عَلَيْهِمَا السَّلَام'),
    (u'عليهم السلام', u'عَلَيْهِمُ السَّلَام'),
    (u'عليه السلام', u'عَلَيْهِ السَّلَام'),
    (u'رواه أبو داود', u'رَوَاهُ أَبُو دَاوُد'),
    (u'بيعة الرضوان', u'بَيْعَةُ الرِّضْوَان'),
    (u'والله أعلم', u'وَاللهُ أَعْلَم'),
    (u'اليوم الآخر', u'اليَوْمُ الآخِر'),
    (u'آخر الآية', u'آخِرُ الآيَة'),
    (u'رحمه الله', u'رَحِمَهُ اللهُ'),
    (u'جل وعلا', u'جَلَّ وَعَلَا'),
    (u'عز وجل', u'عَزَّ وَجَلَّ'),
    (u'وتعالى', u'وَتَعَالَى'),
    (u'سبحانه', u'سُبْحَانَهُ'),
    (u'تعالى', u'تَعَالَى'),
    (u'الشرك', u'الشِّرْك'),
    (u'مضارع', u'مُضَارِع'),
    (u'فتحة', u'فَتْحَة'),
    (u'كسرة', u'كَسْرَة'),
    (u'صحيح', u'صَحِيح'),
    (u'ياء', u'يَاء'),
    (u'حرف', u'حَرْف'),
    (u'اسم', u'اسْم'),
]

# Second tranche: words with exactly ONE correct vowelling whatever the context.
# Deliberately EXCLUDED as context-dependent, and left for the reading pass:
#   من (مَنْ / مِنْ) · أن (أَنْ / أَنَّ) · فعل (فِعْل / فَعَلَ) · جمع (جَمْع / جَمَعَ)
#   القسم (القِسْم / القَسَم) · الله (case ending varies with position)
PAIRS += [
    (u'الذي', u'الَّذِي'),
    (u'الآيات', u'الآيَات'),
    (u'الإيمان', u'الإِيمَان'),
    (u'الإسلام', u'الإِسْلَام'),
    (u'التفسير', u'التَّفْسِير'),
    (u'الكلمة', u'الكَلِمَة'),
    (u'النحو', u'النَّحْو'),
    (u'العين', u'العَيْن'),
    (u'مفعول', u'مَفْعُول'),
    (u'تعبير', u'تَعْبِير'),
    (u'مصدر', u'مَصْدَر'),
    (u'فاعل', u'فَاعِل'),
    (u'كيف', u'كَيْفَ'),
    (u'إلا', u'إِلَّا'),
    (u'في', u'فِي'),
    (u'ما', u'مَا'),
    (u'به', u'بِهِ'),
    (u'هو', u'هُوَ'),
    (u'لا', u'لَا'),
]
# longest first, so a short entry can never eat part of a longer one
PAIRS.sort(key=lambda p: -len(p[0]))

PROT = re.compile(r'(<title>.*?</title>|<meta\b[^>]*>|<script\b.*?</script>|'
                  r'<style\b.*?</style>)', re.S | re.I)

# An Arabic letter or mark on either side means we are INSIDE a longer word, not
# at one. Without this, اسم matches inside اسمك and حرف inside منحرف, leaving a
# half-vowelled word -- worse than the bare one we started with.
AR = u'ء-يً-ْٰ'
RX = [(re.compile(u'(?<![%s])%s(?![%s])' % (AR, re.escape(bare), AR)), vow)
      for bare, vow in PAIRS]


def convert(h):
    parts = PROT.split(h)
    n = 0
    for i in range(len(parts)):
        if i % 2 == 1:          # a protected chunk
            continue
        s = parts[i]
        for rx, vow in RX:
            s, k = rx.subn(vow, s)
            n += k
        parts[i] = s
    return ''.join(parts), n


files = sorted(glob.glob('pages/**/*.html', recursive=True)) + sorted(glob.glob('*.html'))
touched = total = 0
for f in files:
    h = io.open(f, encoding='utf-8').read()
    out, n = convert(h)
    if n:
        io.open(f, 'w', encoding='utf-8', newline='\n').write(out)
        touched += 1
        total += n
print('vowelled %d instances across %d of %d files' % (total, touched, len(files)))
