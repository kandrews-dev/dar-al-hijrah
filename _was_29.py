# -*- coding: utf-8 -*-
"""Wasitiyyah L29 -- Part 2, section 8 and the close of Part 2: the believers
seeing their Lord, and the position of Ahl al-Sunnah toward the ahadith of the
attributes. Sharh pp.105-107."""
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
    'The ḥadīth of the seeing is <strong>مُتَّفَقٌ عَلَيْه</strong>; and al-Fawzān notes that '
    'the aḥādīth affirming the ruʾyah are <strong>مُتَوَاتِرَة</strong>.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'State precisely what the comparison with the full moon is comparing — and what it is not.',
    'Give both narrations of %s and the meaning they share.' % ar('لَا تُضَامُّونَ'),
    'Say why those two prayers in particular are named in a ḥadīth about the seeing.',
    'Reproduce the four denials in the author’s statement of the position of Ahl al-Sunnah.',
])

b += B.heading('٨ · إِثْبَاتُ رُؤْيَةِ المُؤْمِنِينَ لِرَبِّهِمْ يَوْمَ القِيَامَة',
               'Section 8 — The Believers Seeing Their Lord on the Day of Rising')
b += B.prose(
    'Part 1 ended on the ruʾyah, and so does Part 2 — the same doctrine, reached by the other '
    'route. Lesson 21 took it from four āyāt and answered the three objections. Here one ḥadīth '
    'does the work, and it adds something the āyāt did not: <strong>a comparison, and a '
    'prescription.</strong>')
b += B.matn(
    'وَقَوْلُهُ ﷺ: «إِنَّكُمْ سَتَرَوْنَ رَبَّكُمْ كَمَا تَرَوْنَ القَمَرَ لَيْلَةَ '
    'البَدْرِ، لَا تُضَامُّونَ فِي رُؤْيَتِهِ. فَإِنِ اسْتَطَعْتُمْ أَنْ لَا تُغْلَبُوا '
    'عَلَى صَلَاةٍ قَبْلَ طُلُوعِ الشَّمْسِ وَصَلَاةٍ قَبْلَ غُرُوبِهَا فَافْعَلُوا» '
    'مُتَّفَقٌ عَلَيْهِ.')
b += B.hadith(
    'إِنَّكُمْ سَتَرَوْنَ رَبَّكُمْ كَمَا تَرَوْنَ القَمَرَ لَيْلَةَ البَدْرِ، لَا '
    'تُضَامُّونَ فِي رُؤْيَتِهِ. فَإِنِ اسْتَطَعْتُمْ أَنْ لَا تُغْلَبُوا عَلَى صَلَاةٍ '
    'قَبْلَ طُلُوعِ الشَّمْسِ وَصَلَاةٍ قَبْلَ غُرُوبِهَا فَافْعَلُوا',
    '"You will surely see your Lord as you see the moon on the night it is full; you will not be '
    'wronged in seeing Him. So if you are able not to be overcome regarding a prayer before the '
    'rising of the sun and a prayer before its setting, then do so."',
    'مُتَّفَقٌ عَلَيْهِ — al-Bukhārī and Muslim')
b += B.sharh(
    p('<strong>%s</strong> — <em>the address is <strong>to the believers</strong>; and the %s is '
      'the sīn of futurity, <strong>and emphasis is intended by it</strong>.</em> '
      '<strong>%s</strong> — <em>that is: <strong>you will behold Him with your eyes</strong>.</em>'
      % (ar('إِنَّكُمْ سَتَرَوْنَ رَبَّكُمْ'), ar('السِّين'), ar('تَرَوْنَ رَبَّكُمْ'))) +
    p('<em>And <strong>the aḥādīth that have come affirming the believers\' seeing of their Lord '
      'are %s</strong></em> — mass-transmitted. That is the strongest category in the science of '
      'ḥadīth, above even the single ṣaḥīḥ report, and the student met the term in Lesson 21 '
      'where al-Fawzān used it of this same doctrine.' % ar('مُتَوَاتِرَة')))
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>the night of its completeness, and it is the '
      'fourteenth night of the month</strong>, for on that night it has been filled with '
      'light</em>.' % ar('كَمَا تَرَوْنَ القَمَرَ لَيْلَةَ البَدْرِ')) +
    p('And now the sentence that the entire comparison hangs on, and which a careless reader will '
      'get backwards. <em>What is intended by this comparison is '
      '<strong>the establishing of the seeing and the emphasising of it, and the negating of '
      'figurativeness from it</strong></em> —') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.97rem;text-align:center" dir="rtl" lang="ar">'
    '<strong>وَهُوَ تَشْبِيهٌ لِلرُّؤْيَةِ بِالرُّؤْيَةِ، لَا تَشْبِيهٌ لِلْمَرْئِيِّ '
    'بِالمَرْئِيِّ</strong></p>'
    '<p style="margin:.55rem 0 0;font-size:.92rem;text-align:center"><em>— it is '
    '<strong>a likening of the seeing to the seeing, not a likening of the One seen to the thing '
    'seen</strong> — because He سبحانه is '
    '<span dir="rtl" lang="ar">لَيْسَ كَمِثْلِهِ شَيْءٌ</span>.</em></p></div>' +
    p('Read it slowly. The ḥadīth does <strong>not</strong> say <em>your Lord is like the '
      'moon</em>. The <em>kāf</em> attaches to the verb, not to the object: '
      '<strong>you will see Him <em>as</em> you see the moon</strong> — that is, '
      '<em>with your eyes, with certainty, with no crowding and no dispute about it.</em> '
      '<strong>The comparison is between two acts of seeing, not between two things seen.</strong>') +
    p('And notice what that does to the usual objection. The muʿaṭṭilah hear a comparison and '
      'conclude <em>tamthīl</em>. But the thing compared here is <em>our vision</em>, and our '
      'vision really is like our vision. <strong>The ḥadīth likens the clarity, and al-Shūrā 42:11 '
      'governs the rest</strong> — which is precisely the discipline of Lesson 6, now applied to '
      'a simile rather than to an attribute.'))
b += B.sharh(
    p('<strong>%s</strong> — and al-Fawzān gives both ways it is transmitted, because the '
      'vowelling changes the picture:' % ar('لَا تُضَامُّونَ فِي رُؤْيَتِهِ')) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>لَا تُضَامُونَ</strong><br>'
    '<span style="font-size:.82rem">بِضَمِّ التَّاءِ وَتَخْفِيفِ المِيمِ</span></td>'
    '<td style="padding:.6rem .75rem;border:1px solid var(--line)">from '
    '<span dir="rtl" lang="ar">الضَّيْم</span>, <strong>wrong</strong> — <em>no wrong will '
    'befall you, such that some of you see Him and others do not</em></td></tr>'
    '<tr><td style="padding:.6rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>لَا تَضَامُّونَ</strong><br>'
    '<span style="font-size:.82rem">بِفَتْحِ التَّاءِ وَتَشْدِيدِ المِيمِ</span></td>'
    '<td style="padding:.6rem .75rem;border:1px solid var(--line)">from '
    '<span dir="rtl" lang="ar">التَّضَامّ</span>, <strong>crowding together</strong> — '
    '<em>you will not press up against one another in order to see Him; you will not be gathered '
    'into one place for it so that there is a crush</em></td></tr>'
    '</table></div>' +
    p('<em>And <strong>the meaning upon both narrations is: that you will see Him with a seeing '
      'that is realised — <strong>each one of you seeing Him while he is in his own '
      'place.</strong></strong></em>') +
    p('Which is the answer to a question nobody dares ask out loud: <em>how will everyone get a '
      'view?</em> The ḥadīth settles it in a single word, on either reading. '
      '<strong>No queue, no obstruction, no one at the back.</strong>'))
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>that you do not become overcome</strong></em> — '
      '<strong>%s</strong>, <em>and it is <strong>the Fajr prayer</strong></em>; '
      '<strong>%s</strong>, <em>and it is <strong>the ʿAṣr prayer</strong></em>; '
      '<strong>%s</strong> — <em>that is: <strong>guard these two prayers in congregation, in '
      'their times.</strong></em>'
      % (ar('فَإِنِ اسْتَطَعْتُمْ أَنْ لَا تُغْلَبُوا'), ar('عَلَى صَلَاةٍ قَبْلَ طُلُوعِ الشَّمْسِ'),
         ar('وَصَلَاةٍ قَبْلَ غُرُوبِهَا'), ar('فَافْعَلُوا'))) +
    p('And why <em>these</em> two, in a ḥadīth about seeing Allah? al-Fawzān gives the chain: '
      '<em>and he singled out these two prayers <strong>because of the gathering of the angels at '
      'them</strong>, so they are <strong>the most excellent of the prayers</strong> — so '
      '<strong>it was fitting that whoever guards them should be recompensed with the most '
      'excellent of gifts, which is the looking at the Face of Allah تعالى.</strong></em>') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.93rem"><strong>The most excellent prayers → the most '
    'excellent gift.</strong> And notice where the two prayers fall: the one '
    '<em>before the sun rises</em> and the one <em>before it sets</em> — the two hardest to '
    'reach, at the two ends of the day. The ḥadīth does not merely report a doctrine; '
    '<strong>it names the price and tells you to pay it.</strong></p></div>' +
    p('<strong>And the shāhid from the ḥadīth: the affirming of the believers\' seeing of their '
      'Lord <em>with their own eyes</em> on the Day of Rising</strong> — <em>and the mention of '
      'who opposed in that, along with the refutation of him, has already come</em>, at the āyāt '
      'of the ruʾyah in Lesson 21.'))

b += B.heading('مَوْقِفُ أَهْلِ السُّنَّةِ مِنْ هَذِهِ الأَحَادِيث',
               'The Position of Ahl al-Sunnah toward These Aḥādīth')
b += B.matn(
    'إِلَى أَمْثَالِ هَذِهِ الأَحَادِيثِ الَّتِي يُخْبِرُ فِيهَا رَسُولُ اللهِ ﷺ عَنْ '
    'رَبِّهِ بِمَا يُخْبِرُ بِهِ. فَإِنَّ الفِرْقَةَ النَّاجِيَةَ أَهْلَ السُّنَّةِ '
    'وَالجَمَاعَةِ يُؤْمِنُونَ بِذَلِكَ كَمَا يُؤْمِنُونَ بِمَا أَخْبَرَ اللهُ بِهِ فِي '
    'كِتَابِهِ، مِنْ غَيْرِ تَحْرِيفٍ وَلَا تَعْطِيلٍ، وَمِنْ غَيْرِ تَكْيِيفٍ وَلَا '
    'تَمْثِيلٍ.')
b += B.sharh(
    p('<em>This is <strong>a statement of the position of Ahl al-Sunnah wa-l-Jamāʿah toward the '
      'aḥādīth of the attributes</strong> that have come from the Messenger &#65018; — '
      '<strong>that it is like their position toward the āyāt of the attributes in the Qurʾān, '
      'exactly the same</strong>.</em>') +
    p('And that equivalence is the point of the whole of Part 2. The author did not need a second '
      'methodology for the Sunnah. <strong>The same four doors are closed, in the same '
      'order</strong> — and the student met them in Lesson 4, before a single proof-text had been '
      'brought.') +
    p('<em>And it is: <strong>believing in them, and holding as creed what they indicate, upon its '
      'reality</strong></em> —') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>مِنْ غَيْرِ تَحْرِيفٍ</strong></td>'
    '<td style="padding:.6rem .75rem;border:1px solid var(--line)">'
    '<em>they do not turn them away from their apparent meaning by the kinds of '
    '<strong>false taʾwīl</strong></em></td></tr>'
    '<tr><td style="padding:.6rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>وَلَا تَعْطِيلٍ</strong></td>'
    '<td style="padding:.6rem .75rem;border:1px solid var(--line)">'
    '<em>and they do not <strong>negate what they indicate</strong>, thereby stripping '
    'them</em></td></tr>'
    '<tr><td style="padding:.6rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>وَلَا تَكْيِيفٍ</strong></td>'
    '<td style="padding:.6rem .75rem;border:1px solid var(--line)">'
    '<em>and they do not ask <strong>how</strong></em> — which L04 showed is not merely '
    'forbidden but <strong>impossible</strong></td></tr>'
    '<tr><td style="padding:.6rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>وَلَا تَمْثِيلٍ</strong></td>'
    '<td style="padding:.6rem .75rem;border:1px solid var(--line)">'
    '<em>and they do not <strong>liken the attributes mentioned in them to the attributes of the '
    'created</strong></em> — because Allah is '
    '<span dir="rtl" lang="ar">لَيْسَ كَمِثْلِهِ شَيْءٌ</span></td></tr>'
    '</table></div>')
b += B.sharh(
    p('And then al-Fawzān names the two parties this position stands between — the same two that '
      'the next part of the book will set out in full:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.93rem">'
    '<p style="margin:0 0 .7rem">— <em>And by that they <strong>differ from the way of the '
    'innovators, of the Jahmiyyah, the Muʿtazilah and the Ashāʿirah</strong>, '
    'whose position toward these texts was <strong>the position of one who denies them, or one '
    'who reinterprets what they indicate</strong>.</em></p>'
    '<p style="margin:0">— <em>And <strong>contrary to the Mushabbihah</strong>, '
    '<strong>who went to excess in the affirmation until they likened Allah to His '
    'creation</strong> — <span dir="rtl" lang="ar">تَعَالَى اللهُ عَمَّا يَقُولُونَ '
    'عُلُوًّا كَبِيرًا</span>.</em></p></div>' +
    p('Two errors in opposite directions, and the position of Ahl al-Sunnah is not a midpoint '
      'arrived at by splitting the difference. <strong>It is what you are left holding when you '
      'accept every text and add nothing.</strong> The deniers subtracted; the likeners added; '
      'and the people of the Sunnah reported.') +
    p('With this the evidence from the Sunnah is complete — <strong>eight sections, and the '
      'position toward them stated.</strong> What follows in Part 3 is the author\'s account of '
      'why this middle standing is where the people of the Sunnah are found on '
      '<em>every</em> question, not only this one: between the Jabriyyah and the Qadariyyah on '
      'Allah\'s actions, between the Murjiʾah and the Waʿīdiyyah on His threat, and between the '
      'Rāfiḍah and the Khawārij on the Companions of the Messenger of Allah &#65018;.'))

b += B.vocab([
    ('مُتَوَاتِر', 'mutawātir', 'mass-transmitted',
     'The strongest category — and the aḥādīth of the ru\02beyah are of it'),
    ('لَيْلَةُ البَدْر', 'laylat al-badr', 'the night of the full moon',
     'The fourteenth night, when it has been filled with light'),
    ('تَشْبِيهُ الرُّؤْيَةِ بِالرُّؤْيَة', 'tashbīh al-ru\02beyah bi-l-ru\02beyah',
     'likening the seeing to the seeing',
     'NOT likening the One seen to the thing seen — the whole key to the ḥadīth'),
    ('الضَّيْم', 'al-ḍaym', 'wrong, injustice',
     'One reading: no wrong, such that some see Him and some do not'),
    ('التَّضَامّ', 'al-taḍāmm', 'crowding together',
     'The other reading: no pressing together, no crush'),
    ('التَّحْرِيف', 'al-taḥrīf', 'distortion',
     'Turning a text from its apparent meaning by false taʾwīl'),
    ('التَّعْطِيل', 'al-taʿṭīl', 'divesting',
     'Negating what the text indicates'),
    ('المُشَبِّهَة', 'al-mushabbihah', 'the likeners',
     'Who went to excess in affirming until they likened Allah to His creation'),
])
b += B.mcq('ws-l29', [
    ('What exactly does the comparison with the full moon compare?',
     ['The light of Allah with the light of the moon',
      'The seeing with the seeing — not the One seen with the thing seen',
      'The night of the Resurrection with the fourteenth night',
      'The believers’ faces with the moon'], 1),
    ('What is the purpose of the comparison, according to al-Fawzān?',
     ['To indicate that the seeing is at night',
      'To establish the seeing, emphasise it, and negate figurativeness from it',
      'To show that only some will see Him',
      'To compare the reward with the moonlight'], 1),
    ('What does %s mean on the reading with a ḍammah on the tāʾ?' % ar('لَا تُضَامُّونَ'),
     ['You will not crowd together',
      'No wrong will befall you, such that some of you see Him and others do not',
      'You will not be prevented', 'You will not be separated'], 1),
    ('What meaning do both narrations share?',
     ['That the seeing is in a dream',
      'That you will see Him with a realised seeing, each one of you seeing Him while in his own '
      'place',
      'That only the foremost believers will see Him',
      'That the seeing is brief'], 1),
    ('Why are Fajr and ʿAṣr named in this ḥadīth?',
     ['Because they are the shortest prayers',
      'Because of the gathering of the angels at them, so they are the most excellent prayers — '
      'and it was fitting that guarding them be repaid with the most excellent gift',
      'Because they fall outside working hours',
      'Because they were the first prayers legislated'], 1),
    ('What does the author say is the position of Ahl al-Sunnah toward the aḥādīth of the '
     'attributes?',
     ['That they are accepted but their meanings are left unknown',
      'Exactly their position toward the āyāt: believing in them, without taḥrīf, taʿṭīl, takyīf '
      'or tamthīl',
      'That they are accepted only if mutawātir',
      'That they are referred to the scholars without belief'], 1),
    ('Which two parties does al-Fawzān name as opposing this position?',
     ['The Rāfiḍah and the Khawārij',
      'The innovators who deny or reinterpret — Jahmiyyah, Muʿtazilah, Ashāʿirah — and the '
      'Mushabbihah who went to excess in affirming',
      'The Jabriyyah and the Qadariyyah', 'The Murjiʾah and the Waʿīdiyyah'], 1),
])
b += B.tf('ws-l29-tf', [
    ('الأَحَادِيثُ فِي رُؤْيَةِ المُؤْمِنِينَ لِرَبِّهِمْ مُتَوَاتِرَةٌ.',
     'The aḥādīth on the believers seeing their Lord are mutawātir.', True),
    ('الحَدِيثُ يُشَبِّهُ المَرْئِيَّ بِالمَرْئِيِّ.',
     'The ḥadīth likens the One seen to the thing seen.', False),
    ('يَرَى كُلُّ وَاحِدٍ مِنْهُمْ رَبَّهُ وَهُوَ فِي مَكَانِهِ.',
     'Each one of them will see his Lord while he is in his own place.', True),
    ('مَوْقِفُ أَهْلِ السُّنَّةِ مِنْ أَحَادِيثِ الصِّفَاتِ كَمَوْقِفِهِمْ مِنْ آيَاتِهَا.',
     'The position of Ahl al-Sunnah toward the aḥādīth of the attributes is like their position '
     'toward its āyāt.', True),
])
b += B.memorize(
    'إِنَّكُمْ سَتَرَوْنَ رَبَّكُمْ كَمَا تَرَوْنَ القَمَرَ لَيْلَةَ البَدْرِ',
    'Memorize the ḥadīth with al-Fawzān\'s clause attached, or you will misread it the first time '
    'someone presses you: <em>a likening of the seeing to the seeing, not of the One seen to the '
    'thing seen.</em> And then notice what the ḥadīth asks of you in return — two prayers, at the '
    'two hardest hours of the day.')
b += B.aiquiz('The believers seeing their Lord from the Sunnah and the close of Part 2 of '
              'al-Aqidah al-Wasitiyyah: that the comparison with the full moon likens the seeing '
              'to the seeing and not the One seen to the thing seen, the two narrations of la '
              'tudammuna and the meaning they share, why Fajr and Asr are named as the price of '
              'the most excellent gift, and the position of Ahl al-Sunnah toward the ahadith of '
              'the attributes without tahrif tatil takyif or tamthil')
b += B.further()
b += B.nav('was-l28-maiyyah-qurb-sunnah.html', 'The Maʿiyyah and the Nearness in the Sunnah',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l29')

io.open(os.path.join(B.AQ, 'was-l29-ruyah-mawqif.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'الرُّؤْيَةُ فِي السُّنَّةِ · وَمَوْقِفُ أَهْلِ السُّنَّة',
    'The Seeing in the Sunnah, and the Position of Ahl al-Sunnah',
    'Lesson 29 of al-ʿAqīdah al-Wāsiṭiyyah, closing Part 2: why '
    'the comparison with the full moon likens the seeing and not the One seen, the two narrations '
    'of “you will not be crowded,” the two prayers named as the price of the most '
    'excellent gift, and the four doors closed against the aḥādīth of the '
    'attributes exactly as against the āyāt.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ التَّاسِعُ وَالعِشْرُون', '3',
           'الرُّؤْيَةُ فِي السُّنَّةِ · وَمَوْقِفُ أَهْلِ السُّنَّة',
           'The Seeing in the Sunnah, and the Position of Ahl al-Sunnah', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l29-ruyah-mawqif.html')
