# -*- coding: utf-8 -*-
"""Wasitiyyah L22 -- the opening of Part 2: the Sunnah as the second source, its
standing relative to the Qur'an, and the condition the author attaches to the
ahadith he is about to bring -- with the five conditions of a sahih hadith.
Sharh pp.90-92."""
import io, os, importlib.util

spec = importlib.util.spec_from_file_location('qb', os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '_mutunbuild.py'))
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
B.set_source(os.path.join(B.AQ, 'was-l01-basmalah.html'))
B.FOOT = ('al-ʿAqīdah al-Wāsiṭiyyah of Shaykh al-Islām Ibn Taymiyyah '
          '· sharḥ of Shaykh Ṣāliḥ al-Fawzān · in our own words')
B.READING = [
    'Shaykh <strong>صَالِحٌ الفَوْزَان</strong>, <em>شَرْحُ العَقِيدَةِ الوَاسِطِيَّة</em> '
    '(Riyadh, Presidency of Scholarly Research &amp; Iftāʾ) — the sharḥ this track follows.',
    'For the terminology itself, the <strong>Hadeeth</strong> track on this site covers '
    'مُصْطَلَحُ الحَدِيث — صَحِيح, حَسَن, ضَعِيف, سَنَد, مَتْن, عِلَّة, شُذُوذ — with definitions.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Define %s linguistically and technically.' % ar('السُّنَّة'),
    'Give the four things the author says the Sunnah does for the Qurʾān.',
    'List the five conditions of a %s and name what each one excludes.' % ar('حَدِيثٌ صَحِيح'),
    'Explain what %s adds beyond mere authenticity.'
    % ar('تَلَقَّاهَا أَهْلُ المَعْرِفَةِ بِالقَبُولِ'),
])

b += B.heading('القِسْمُ الثَّانِي · الأَدِلَّةُ مِنَ السُّنَّة',
               'Part Two — The Evidence from the Sunnah')
b += B.prose(
    'Part 1 is finished: twenty-three sections of Qurʾānic evidence, and the author\'s own '
    'verdict that he gave only a selection. He now turns to the second source. But he does not '
    'simply start quoting aḥādīth — <strong>he first states what the Sunnah is, what it does, '
    'and on what condition a ḥadīth may be used in this subject at all.</strong> That '
    'preliminary is this lesson, and it is the methodological heart of Part 2.')
b += B.matn(
    'ثُمَّ فِي سُنَّةِ رَسُولِ اللهِ ﷺ، فَالسُّنَّةُ تُفَسِّرُ القُرْآنَ وَتُبَيِّنُهُ '
    'وَتَدُلُّ عَلَيْهِ وَتُعَبِّرُ عَنْهُ.')
b += B.sharh(
    p('al-Fawzān first locates the sentence grammatically, because it matters: '
      '<strong>%s</strong> <em>is conjoined to his earlier statement</em> — '
      '«<em>and there has entered into this totality what Allah described Himself with in Sūrat '
      'al-Ikhlāṣ…</em>» — <em>that is: <strong>and there has entered into it what the Messenger '
      '&#65018; described his Lord with, in what has come in the authentic Sunnah.</strong></em>'
      % ar('ثُمَّ فِي سُنَّةِ رَسُولِ اللهِ ﷺ')) +
    p('So this is not a new topic. It is the <em>same</em> sentence from the beginning of the '
      'book, still running: what Ahl al-Sunnah believe about Allah is what He said of Himself '
      '<em>and</em> what His Messenger &#65018; said of Him. Part 1 and Part 2 are two halves of '
      'one clause.') +
    p('And why the Sunnah at all? <em>Because <strong>the Sunnah is the second foundation to '
      'which recourse must be had</strong> after the Book of Allah عز وجل.</em>'))
b += B.ayah(
    'فَإِنْ تَنَازَعْتُمْ فِي شَيْءٍ فَرُدُّوهُ إِلَى اللَّهِ وَالرَّسُولِ إِنْ كُنْتُمْ '
    'تُؤْمِنُونَ بِاللَّهِ وَالْيَوْمِ الْآخِرِ',
    '"And if you differ in anything, refer it to Allah and the Messenger, if you believe in Allah '
    'and the Last Day."',
    'Sūrat al-Nisāʾ 4:59 · سورة النساء')
b += B.sharh(
    p('al-Fawzān draws the referral out into its two halves, and the second is the one that '
      'establishes the Sunnah: <em><strong>the referral to Allah</strong> is the returning to '
      '<strong>His Book</strong>; and <strong>the referral to the Messenger &#65018;, after his '
      'death</strong>, is the returning to <strong>his Sunnah</strong>.</em>') +
    p('The āyah commands two referrals, not one. And since the Messenger &#65018; is no longer '
      'present to be asked, obeying the second half of the command <em>is</em> consulting the '
      'Sunnah. <strong>Whoever will not refer to it has not obeyed the āyah</strong> — and the '
      'āyah ties the obedience to belief in Allah and the Last Day.'))
b += B.sharh(
    p('Then the definition, in the two registers the ʿulamāʾ always give:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.92rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.55rem .8rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>لُغَةً</strong> — in the language</td>'
    '<td style="padding:.55rem .8rem;border:1px solid var(--line)">'
    '<span dir="rtl" lang="ar"><strong>الطَّرِيقَة</strong></span> — the way, the '
    'road</td></tr>'
    '<tr><td style="padding:.55rem .8rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>اصْطِلَاحًا</strong> — technically</td>'
    '<td style="padding:.55rem .8rem;border:1px solid var(--line)">what has come from the '
    'Messenger of Allah ٞط of <strong>a statement, or an act, or an '
    'approval</strong></td></tr>'
    '</table></div>' +
    p('Hold the lexical sense in view, because it explains the name of the group this whole book '
      'is about. <strong>%s means <em>the people of the way</em></strong> — not the people of a '
      'theory. Lesson 2 made the same point from the other side: the sects are named after their '
      'innovation, their founder or their deeds, and these are named after <em>the road</em>.'
      % ar('أَهْلُ السُّنَّة')))

b += B.heading('مَكَانَةُ السُّنَّة', 'The Standing of the Sunnah')
b += B.sharh(
    p('The author gives the Sunnah four functions in one line, and al-Fawzān takes them one at a '
      'time. <strong>%s</strong> — <em>that is: it makes clear its meanings and its '
      'aims</em>, <em>for the Prophet &#65018; explains to the people what was sent down to '
      'him</em>:' % ar('فَالسُّنَّةُ تُفَسِّرُ القُرْآنَ')))
b += B.ayah(
    'وَأَنْزَلْنَا إِلَيْكَ الذِّكْرَ لِتُبَيِّنَ لِلنَّاسِ مَا نُزِّلَ إِلَيْهِمْ',
    '"And We sent down to you the Reminder, that you may make clear to the people what was sent '
    'down to them."',
    'Sūrat al-Naḥl 16:44 · سورة النحل')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: it clarifies <strong>what comes in it in summary '
      'form</strong></em>; and al-Fawzān gives the obvious examples: <em>such as the prayer, the '
      'fast, the ḥajj, the zakāh, and <strong>most of the rulings, which come in the Qurʾān in '
      'summary and the Prophetic Sunnah clarifies them.</strong></em>'
      % ar('وَتُبَيِّنُهُ')) +
    p('That single sentence is why the Sunnah is not optional. The Qurʾān commands the prayer and '
      'does not say how many, when, or in what form. <strong>A person holding the Qurʾān alone '
      'could not pray.</strong>') +
    p('<strong>%s</strong> — <em>that is: it indicates what the Qurʾān indicated, and expresses '
      'what the Qurʾān expressed; <strong>so it comes out in agreement with the Qurʾān</strong>, '
      'and the ruling is then from what the Book <em>and</em> the Sunnah have indicated — '
      '<strong>as with the names of Allah and His attributes.</strong></em>'
      % ar('وَتَدُلُّ عَلَيْهِ وَتُعَبِّرُ عَنْهُ')) +
    p('Note where al-Fawzān chooses to point that last function: <em>at this very subject</em>. '
      'The attributes are the case where the Sunnah is not adding rulings the Qurʾān left '
      'summary, and not explaining a difficult word — <strong>it is saying the same thing the '
      'Qurʾān said.</strong> Which is why Part 2 will feel like Part 1 continued rather than a '
      'fresh argument.'))

b += B.heading('شَرْطُ الاسْتِدْلَالِ بِالحَدِيث', 'The Condition for Using a Ḥadīth as Proof')
b += B.matn(
    'وَمَا وَصَفَ الرَّسُولُ بِهِ رَبَّهُ عَزَّ وَجَلَّ مِنَ الأَحَادِيثِ الصِّحَاحِ '
    'الَّتِي تَلَقَّاهَا أَهْلُ المَعْرِفَةِ بِالقَبُولِ وَجَبَ الإِيمَانُ بِهَا كَذَلِكَ.')
b += B.sharh(
    p('Again the grammar first: <strong>%s</strong> is the <em>mubtadaʾ</em>, and its '
      '<em>khabar</em> is <strong>%s</strong> — <em>that is: '
      '<strong>just as it is obligatory to believe in what Allah described Himself with in the '
      'Noble Qurʾān.</strong></em>' % (ar('وَمَا وَصَفَ…'), ar('وَجَبَ الإِيمَانُ بِهَا كَذَلِكَ'))) +
    p('<strong>The same obligation, on the same footing.</strong> And the ground for that is that '
      'the speech is not the Prophet\'s &#65018; own:'))
b += B.ayah(
    'وَمَا يَنْطِقُ عَنِ الْهَوَى إِنْ هُوَ إِلَّا وَحْيٌ يُوحَى',
    '"Nor does he speak from desire. It is nothing but a revelation revealed."',
    'Sūrat al-Najm 53:3–4 · سورة النجم')
b += B.sharh(
    p('<em>So <strong>the Sunnah which the Messenger &#65018; uttered is a revelation from '
      'Allah</strong></em> — and al-Fawzān brings a second proof for it from the pairing of the '
      'two things sent down upon him:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.93rem"><span dir="rtl" lang="ar">وَأَنْزَلَ اللَّهُ '
    'عَلَيْكَ الْكِتَابَ وَالْحِكْمَةَ</span> — “and Allah sent down upon you the Book '
    'and the Wisdom” (al-Nisāʾ 4:113). <em>So <strong>the Book is the '
    'Qurʾān, and the Wisdom is the Sunnah.</strong></em> Both are '
    '<em>sent down</em>.</p></div>' +
    p('<em>So it is obligatory to believe in what has come in the Sunnah — '
      '<strong>especially in the chapter of belief</strong></em>:'))
b += B.ayah(
    'وَمَا آتَاكُمُ الرَّسُولُ فَخُذُوهُ وَمَا نَهَاكُمْ عَنْهُ فَانْتَهُوا',
    '"And whatever the Messenger gives you, take it; and whatever he forbids you, abstain from '
    'it."',
    'Sūrat al-Ḥashr 59:7 · سورة الحشر')

b += B.heading('الشُّرُوطُ الخَمْسَةُ لِلْحَدِيثِ الصَّحِيح',
               'The Five Conditions of an Authentic Ḥadīth')
b += B.sharh(
    p('<em>But there is no avoiding, in the accepting of a ḥadīth and the believing in it, '
      '<strong>its being established from the Prophet &#65018;</strong>; and this is why the '
      'Shaykh رحمه الله said <strong>%s</strong>.</em>' % ar('مِنَ الأَحَادِيثِ الصِّحَاحِ')) +
    p('This is the clause that separates this book from the method of those who argue creed from '
      'whatever story supports them. <strong>%s is the plural of %s</strong>, and al-Fawzān then '
      'gives the definition the ḥadīth scholars use:' % (ar('الصِّحَاح'), ar('صَحِيح'))) +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.95rem" dir="rtl" lang="ar"><strong>الحَدِيثُ الصَّحِيحُ: '
    'هُوَ مَا نَقَلَهُ رَاوٍ عَدْلٌ تَامُّ الضَّبْطِ عَنْ مِثْلِهِ، مِنْ غَيْرِ شُذُوذٍ وَلَا '
    'عِلَّةٍ.</strong></p>'
    '<p style="margin:.5rem 0 0;font-size:.9rem">— <em>that which an upright narrator of '
    'complete precision transmitted from one like himself, without irregularity and without a '
    'hidden defect.</em></p></div>' +
    p('<em>So it is that in which <strong>five conditions</strong> have come together:</em>') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.55rem .7rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>١</strong> <span dir="rtl" lang="ar">عَدَالَةُ الرُّوَاةِ</span></td>'
    '<td style="padding:.55rem .7rem;border:1px solid var(--line)">the uprightness of the '
    'narrators — excludes the untrustworthy</td></tr>'
    '<tr><td style="padding:.55rem .7rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>٢</strong> <span dir="rtl" lang="ar">تَمَامُ الضَّبْطِ</span></td>'
    '<td style="padding:.55rem .7rem;border:1px solid var(--line)">complete precision — '
    'excludes the honest but unreliable, who would not lie but misremembers</td></tr>'
    '<tr><td style="padding:.55rem .7rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>٣</strong> <span dir="rtl" lang="ar">اتِّصَالُ السَّنَدِ</span></td>'
    '<td style="padding:.55rem .7rem;border:1px solid var(--line)">the connectedness of the '
    'chain — excludes a chain with a gap in it, however sound its named links</td></tr>'
    '<tr><td style="padding:.55rem .7rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>٤</strong> <span dir="rtl" lang="ar">سَلَامَتُهُ مِنَ الشُّذُوذِ</span></td>'
    '<td style="padding:.55rem .7rem;border:1px solid var(--line)">its freedom from '
    '<em>shudhūdh</em> — excludes the reliable narrator who contradicts those more '
    'reliable than him</td></tr>'
    '<tr><td style="padding:.55rem .7rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>٥</strong> <span dir="rtl" lang="ar">سَلَامَتُهُ مِنَ العِلَّةِ</span></td>'
    '<td style="padding:.55rem .7rem;border:1px solid var(--line)">its freedom from a hidden '
    '<em>ʿillah</em> — excludes the defect that only a specialist detects, in a chain '
    'that looks sound</td></tr>'
    '</table></div>' +
    p('Four of the five are about the <em>people</em>, and the last two are the ones that make '
      'this a science rather than a background check. A ḥadīth can pass every test of honesty and '
      'memory and connection, and still be rejected because <strong>a stronger narrator said '
      'otherwise</strong> (شُذُوذ), or because <strong>something is wrong in it that does not show '
      'on the surface</strong> (عِلَّة).'))
b += B.sharh(
    p('And then the author\'s second clause, which is <em>additional</em> to authenticity: '
      '<strong>%s</strong> — <em>that is: <strong>the people of knowledge of ḥadīth accepted it '
      'and took it</strong></em>.' % ar('تَلَقَّاهَا أَهْلُ المَعْرِفَةِ')) +
    p('Notice what the author has done. He has not written «the aḥādīth which I consider '
      'authentic», nor «the aḥādīth whose chains look sound to the reader». '
      '<strong>He has handed the judgement to the specialists of the field</strong> — and in a '
      'book of creed, where the temptation is to grade a ḥadīth by whether it suits one\'s '
      'position, that is the whole safeguard.') +
    p('This is also the rule this track works under. Every ḥadīth in the lessons that follow '
      'carries <strong>a grading attributed to a named scholar</strong> — al-Bukhārī, Muslim, '
      'or an imām who graded it — and where the sharḥ gives an attribution without a grading, '
      'the page says so plainly rather than supplying one.'))

b += B.vocab([
    ('السُّنَّة', 'al-sunnah', 'the way; the Prophetic example',
     'Linguistically الطَّرِيقَة; technically his ﷺ statement, act or approval'),
    ('الحِكْمَة', 'al-ḥikmah', 'the Wisdom',
     'In al-Nisāʾ 4:113 it is the Sunnah — sent down as the Book was'),
    ('صَحِيح', 'ṣaḥīḥ', 'authentic',
     'An upright narrator of complete precision, from one like him, no shudhūdh, no ʿillah'),
    ('العَدَالَة', 'al-ʿadālah', 'uprightness',
     'Condition 1 — excludes the untrustworthy'),
    ('الضَّبْط', 'al-ḍabṭ', 'precision of retention',
     'Condition 2 — excludes the honest man who misremembers'),
    ('السَّنَد', 'al-sanad', 'the chain',
     'Condition 3 is its اتِّصَال — connectedness, with no gap'),
    ('الشُّذُوذ', 'al-shudhūdh', 'irregularity',
     'Condition 4 — a reliable narrator contradicting those more reliable'),
    ('العِلَّة', 'al-ʿillah', 'a hidden defect',
     'Condition 5 — the flaw that does not show on the surface'),
])
b += B.mcq('ws-l22', [
    ('What does al-Fawzān say %s refers to, after the Prophet’s ﷺ death?'
     % ar('فَرُدُّوهُ إِلَى اللَّهِ وَالرَّسُولِ'),
     ['To the scholars of each age',
      'The referral to Allah is to His Book, and the referral to the Messenger ﷺ is to his Sunnah',
      'To the consensus of the Companions', 'To the ruler'], 1),
    ('What is %s linguistically and technically?' % ar('السُّنَّة'),
     ['A recommended act; and the opposite of an obligation',
      'الطَّرِيقَة — the way; and what came from the Messenger ﷺ of a statement, an act, or an '
      'approval',
      'A narration; and a chain of transmission',
      'An innovation’s opposite; and the practice of Madīnah'], 1),
    ('What are the four things the author says the Sunnah does for the Qurʾān?',
     ['Recites it, preserves it, teaches it, defends it',
      'Explains it, clarifies it, indicates it, and expresses it',
      'Abrogates it, restricts it, generalises it, specifies it',
      'Translates it, summarises it, applies it, enforces it'], 1),
    ('Why does al-Fawzān say a person holding the Qurʾān alone could not pray?',
     ['Because the Qurʾān does not mention prayer',
      'Because the Qurʾān commands most rulings in summary form, and the Sunnah clarifies them',
      'Because prayer was legislated after the Qurʾān',
      'Because the Qurʾān forbids praying without a teacher'], 1),
    ('In al-Nisāʾ 4:113, what is %s?' % ar('الْحِكْمَةَ'),
     ['Sound judgement granted to the Prophet ﷺ', 'The Sunnah',
      'The science of tafsīr', 'The Preserved Tablet'], 1),
    ('Which condition excludes a reliable narrator who contradicts those more reliable than him?',
     ['العَدَالَة', 'السَّلَامَةُ مِنَ الشُّذُوذِ', 'اتِّصَالُ السَّنَدِ',
      'السَّلَامَةُ مِنَ العِلَّةِ'], 1),
    ('What does %s add beyond authenticity?'
     % ar('تَلَقَّاهَا أَهْلُ المَعْرِفَةِ بِالقَبُولِ'),
     ['That the ḥadīth is mutawātir',
      'That the judgement is handed to the specialists of ḥadīth — not to the reader, and not to '
      'whoever the ruling suits',
      'That it appears in al-Bukhārī specifically',
      'That it has at least five chains'], 1),
])
b += B.tf('ws-l22-tf', [
    ('السُّنَّةُ هِيَ الأَصْلُ الثَّانِي بَعْدَ كِتَابِ اللهِ.',
     'The Sunnah is the second foundation after the Book of Allah.', True),
    ('الحَدِيثُ الصَّحِيحُ يَكْفِي فِيهِ اتِّصَالُ السَّنَدِ وَحْدَهُ.',
     'For a ḥadīth to be ṣaḥīḥ, the connectedness of the chain alone suffices.', False),
    ('العِلَّةُ وَصْفٌ خَفِيٌّ لَا يَظْهَرُ عَلَى السَّطْحِ.',
     'An ʿillah is a hidden defect that does not show on the surface.', True),
    ('مَا نَطَقَ بِهِ الرَّسُولُ ﷺ مِنَ السُّنَّةِ وَحْيٌ مِنَ اللهِ.',
     'What the Messenger ﷺ uttered of the Sunnah is a revelation from Allah.', True),
])
b += B.memorize(
    'وَمَا يَنْطِقُ عَنِ الْهَوَى إِنْ هُوَ إِلَّا وَحْيٌ يُوحَى',
    'The āyah on which the whole of Part 2 rests. If what he &#65018; said about his Lord is '
    'revelation, then the aḥādīth of the attributes are not a secondary class of evidence to be '
    'weighed against the Qurʾān — they are the same evidence, reaching us by the other route.')
b += B.aiquiz('The opening of Part 2 of al-Aqidah al-Wasitiyyah: the Sunnah as the second '
              'foundation, al-Nisa 4:59 and the two referrals, the Sunnah defined linguistically '
              'and technically, the four things it does for the Quran, al-Nisa 4:113 where the '
              'Wisdom is the Sunnah, and the five conditions of a sahih hadith with what each one '
              'excludes including shudhudh and illah')
b += B.further()
b += B.nav('was-l21-ruyah.html', 'The Ruʾyah — and the Close of Part One',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l22')

io.open(os.path.join(B.AQ, 'was-l22-sunnah-shart.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'السُّنَّةُ وَشَرْطُ الاسْتِدْلَالِ بِالحَدِيث',
    'The Sunnah, and the Condition for Using a Ḥadīth',
    'Lesson 22 of al-ʿAqīdah al-Wāsiṭiyyah, opening Part 2: the '
    'Sunnah as the second foundation, the two referrals of al-Nisāʾ 4:59, the four '
    'things the Sunnah does for the Qurʾān, and the five conditions of an authentic '
    'ḥadīth — with what each one excludes.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الثَّانِي وَالعِشْرُون', '3',
           'السُّنَّةُ وَشَرْطُ الاسْتِدْلَالِ بِالحَدِيث',
           'The Sunnah, and the Condition for Using a Ḥadīth', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l22-sunnah-shart.html')
