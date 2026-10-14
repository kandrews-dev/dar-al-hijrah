# -*- coding: utf-8 -*-
"""Wasitiyyah L28 -- Part 2, section 7: the ma'iyyah and the nearness of Allah
from the Sunnah, and that they do not contradict His being above His Throne.
Four ahadith. Sharh pp.102-104."""
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
    'Gradings as the matn gives them: the first is <strong>حَسَن</strong>, from '
    '<strong>الطَّبَرَانِيّ</strong> in <em>المُعْجَمُ الكَبِير</em>; the second and fourth are '
    '<strong>مُتَّفَقٌ عَلَيْهِ</strong>; the third is from <strong>مُسْلِم</strong>.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Say what %s teaches about īmān itself, besides the maʿiyyah.'
    % ar('أَفْضَلُ الإِيمَانِ'),
    'Explain how al-Fawzān keeps %s from implying mixture with the creation.'
    % ar('فَإِنَّ اللهَ قِبَلَ وَجْهِهِ'),
    'Divide the four names of the duʿāʾ into their two pairs, and say what each pair affirms.',
    'Give the structure of the answer in %s — what is denied and what is affirmed.'
    % ar('لَا تَدْعُونَ أَصَمَّ وَلَا غَائِبًا'),
])

b += B.heading('٧ · إِثْبَاتُ مَعِيَّةِ اللهِ لِخَلْقِهِ وَأَنَّهَا لَا تُنَافِي عُلُوَّه',
               'Section 7 — The Maʿiyyah, and That It Does Not Contradict His Highness')
b += B.prose(
    'The author arranges Part 2 exactly as he arranged Part 1: the ʿuluww and the istiwāʾ first, '
    'and then immediately the texts of nearness — because these are the texts the muʿaṭṭilah use '
    'to cancel the ones before them. Lesson 17 settled the question from the Qurʾān. '
    '<strong>Here the same resolution arrives four times over from the Sunnah</strong>, and one '
    'of the four states it in a single sentence.')

b += B.heading('١ · «أَفْضَلُ الإِيمَانِ أَنْ تَعْلَمَ أَنَّ اللهَ مَعَكَ حَيْثُمَا كُنْت»',
               'First — "The Best of Faith Is to Know That Allah Is with You Wherever You Are"')
b += B.matn(
    'وَقَوْلُهُ ﷺ: «أَفْضَلُ الإِيمَانِ أَنْ تَعْلَمَ أَنَّ اللهَ مَعَكَ حَيْثُمَا '
    'كُنْتَ» حَدِيثٌ حَسَنٌ، أَخْرَجَهُ الطَّبَرَانِيُّ مِنْ حَدِيثِ عُبَادَةَ بْنِ '
    'الصَّامِتِ.')
b += B.hadith(
    'أَفْضَلُ الإِيمَانِ أَنْ تَعْلَمَ أَنَّ اللهَ مَعَكَ حَيْثُمَا كُنْتَ',
    '"The best of faith is that you know Allah is with you wherever you are."',
    'حَدِيثٌ حَسَنٌ — graded ḥasan in the matn; al-Ṭabarānī in <em>al-Muʿjam al-Kabīr</em>, from '
    'ʿUbādah ibn al-Ṣāmit رضي الله عنه')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>of the best of its qualities</strong></em>. And '
      'al-Fawzān pauses on that, because a second doctrine falls out of the wording: '
      '<em>and <strong>in this is a proof that īmān admits of degrees</strong></em> '
      '(%s).' % (ar('أَفْضَلُ الإِيمَانِ'), ar('أَنَّ الإِيمَانَ يَتَفَاضَلُ'))) +
    p('If faith had no degrees there would be no «best» of it. <strong>That is the position '
      'against the Murjiʾah</strong>, who held that faith is one indivisible thing which does not '
      'increase or decrease — and the author will return to it in Part 6. Here it arrives in '
      'passing, out of a single word.') +
    p('<strong>%s</strong> — <em>that is: <strong>by His knowledge and His observing</strong></em>; '
      '<strong>%s</strong> — <em>in whatever place you are found</em>. This is '
      '<strong>the general maʿiyyah</strong> of Lesson 17, whose entailment is knowledge.'
      % (ar('أَنَّ اللهَ مَعَكَ'), ar('حَيْثُمَا كُنْتَ'))) +
    p('And then the point of the whole ḥadīth, which is not information but <em>effect</em>: '
      '<em>whoever knows that, <strong>his outward and his inward become equal</strong>, and '
      '<strong>he stands in awe of Him in every place.</strong></em>'
      % ()) +
    p('<strong>%s</strong> — a man whose private conduct matches his public conduct. That is the '
      'definition of <em>ikhlāṣ</em> stated from the other end, and the ḥadīth makes it the '
      'product of one piece of knowledge. <em>And in the ḥadīth is a proof for the affirming of '
      'Allah\'s maʿiyyah with His creation by His knowledge and His encompassing of their deeds, '
      '<strong>and that it is obligatory upon the servant to recall that constantly, so that he '
      'does his work well.</strong></em>'
      % ar('اسْتَوَتْ عَلَانِيَتُهُ وَسَرِيرَتُهُ')))

b += B.heading('٢ · «فَإِنَّ اللهَ قِبَلَ وَجْهِه»', 'Second — "Allah Is before His Face"')
b += B.matn(
    'وَقَوْلُهُ ﷺ: «إِذَا قَامَ أَحَدُكُمْ إِلَى الصَّلَاةِ فَلَا يَبْصُقْ قِبَلَ '
    'وَجْهِهِ، فَإِنَّ اللهَ قِبَلَ وَجْهِهِ، وَلَا عَنْ يَمِينِهِ، وَلَكِنْ عَنْ '
    'يَسَارِهِ أَوْ تَحْتَ قَدَمِهِ» مُتَّفَقٌ عَلَيْهِ.')
b += B.hadith(
    'إِذَا قَامَ أَحَدُكُمْ إِلَى الصَّلَاةِ فَلَا يَبْصُقْ قِبَلَ وَجْهِهِ، فَإِنَّ اللهَ '
    'قِبَلَ وَجْهِهِ، وَلَا عَنْ يَمِينِهِ، وَلَكِنْ عَنْ يَسَارِهِ أَوْ تَحْتَ قَدَمِهِ',
    '"When one of you stands to pray, let him not spit before his face, for Allah is before his '
    'face; nor to his right; but to his left, or beneath his foot."',
    'مُتَّفَقٌ عَلَيْهِ — al-Bukhārī and Muslim')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: when he has begun it</em>. <strong>%s</strong> — '
      '<em>that is: in front of him</em> — <strong>and %s is vowelled with a kasrah on the ق and '
      'a fatḥah on the ب.</strong>'
      % (ar('إِذَا قَامَ أَحَدُكُمْ إِلَى الصَّلَاةِ'), ar('قِبَلَ وَجْهِهِ'), ar('قِبَلَ'))) +
    p('<strong>%s</strong> — <em>this is <strong>the reason given for the prohibition</strong> of '
      'spitting in the direction of the one praying\'s qiblah: that Allah سبحانه is %s — '
      '<strong>facing him</strong>.</em>' % (ar('فَإِنَّ اللهَ قِبَلَ وَجْهِهِ'), ar('مُوَاجِهُهُ'))) +
    p('And then al-Fawzān guards it in the same breath, because this is precisely the wording an '
      'opponent would seize: <em>and <strong>this facing is as befits Allah سبحانه</strong>. '
      '<strong>It does not follow from it that He سبحانه is mixed with His creation</strong> — '
      'rather <strong>He is above His heavens, established upon His Throne, and He is near to His '
      'creation, encompassing them.</strong></em>') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.93rem">That single sentence holds all three together: '
    '<strong>above His heavens</strong> · <strong>established upon His Throne</strong> '
    '· <strong>near to His creation and encompassing them</strong>. Ahl al-Sunnah are not '
    'balancing two claims against each other; they are reporting all the texts.</p></div>' +
    p('<strong>%s</strong> — <em>out of <strong>honouring the right side</strong>, and because '
      '<strong>the two angels are on his right</strong>, as comes in a narration of '
      'al-Bukhārī.</em> <strong>%s</strong> — <em>but let him spit in the direction of his left, '
      'or beneath his foot.</em>' % (ar('وَلَا عَنْ يَمِينِهِ'),
                                     ar('وَلَكِنْ عَنْ يَسَارِهِ أَوْ تَحْتَ قَدَمِهِ'))) +
    p('<strong>And the shāhid: the affirming of Allah\'s nearness to His praying servant '
      '<em>and His turning toward him</em> — <strong>while He سبحانه is above him.</strong></strong>'))

b += B.heading('٣ · الأَوَّلُ وَالآخِرُ وَالظَّاهِرُ وَالبَاطِن',
               'Third — the First, the Last, the Outermost, the Innermost')
b += B.matn(
    'وَقَوْلُهُ ﷺ: «اللَّهُمَّ رَبَّ السَّمَاوَاتِ السَّبْعِ وَرَبَّ العَرْشِ '
    'العَظِيمِ، رَبَّنَا وَرَبَّ كُلِّ شَيْءٍ، فَالِقَ الحَبِّ وَالنَّوَى، مُنْزِلَ '
    'التَّوْرَاةِ وَالإِنْجِيلِ وَالقُرْآنِ، أَعُوذُ بِكَ مِنْ شَرِّ نَفْسِي، وَمِنْ '
    'شَرِّ كُلِّ دَابَّةٍ أَنْتَ آخِذٌ بِنَاصِيَتِهَا. أَنْتَ الأَوَّلُ فَلَيْسَ '
    'قَبْلَكَ شَيْءٌ، وَأَنْتَ الآخِرُ فَلَيْسَ بَعْدَكَ شَيْءٌ، وَأَنْتَ الظَّاهِرُ '
    'فَلَيْسَ فَوْقَكَ شَيْءٌ، وَأَنْتَ البَاطِنُ فَلَيْسَ دُونَكَ شَيْءٌ، اقْضِ '
    'عَنِّي الدَّيْنَ وَأَغْنِنِي مِنَ الفَقْرِ» رَوَاهُ مُسْلِمٌ.')
b += B.sharh(
    p('<strong>%s</strong> — <em>its origin is <strong>%s</strong>; <strong>the mīm is a '
      'substitute for the yāʾ of calling</strong>.</em>' % (ar('اللَّهُمَّ'), ar('يَا اللهُ'))) +
    p('<strong>%s</strong> — <em>their Creator and their Owner</em>; <strong>%s</strong> — '
      '<em>the Great, <strong>whose measure none can measure but Allah</strong>, for it is '
      '<strong>the greatest of the created things</strong></em>. <strong>%s</strong> — '
      '<em>our Creator and our Provider, and the Creator of everything and its Owner</em> — '
      '<em>so in it is <strong>the affirming of His lordship over everything</strong>.</em>'
      % (ar('رَبَّ السَّمَاوَاتِ السَّبْعِ'), ar('وَرَبَّ العَرْشِ العَظِيمِ'),
         ar('رَبَّنَا وَرَبَّ كُلِّ شَيْءٍ'))) +
    p('<strong>%s</strong> — <em>the Splitter of the grain of food and the date-stone, '
      '<strong>for sprouting</strong></em>. <strong>%s</strong> — upon Mūsā, <em>and '
      '<strong>%s</strong></em> — upon ʿĪsā, <em>and <strong>%s</strong></em> — upon Muḥammad '
      '&#65018;. <em>And in that is <strong>a proof of the excellence of these Books, and that '
      'they are sent down from Allah تعالى.</strong></em>'
      % (ar('فَالِقَ الحَبِّ وَالنَّوَى'), ar('مُنْزِلَ التَّوْرَاةِ'), ar('وَالإِنْجِيلِ'),
         ar('وَالقُرْآنِ'))) +
    p('<strong>%s</strong> — <em>I take refuge and I hold fast</em>. <strong>%s</strong> — '
      '<em>every creature that crawls upon the face of the earth</em>. '
      '<strong>%s</strong> — <em>al-nāṣiyah is <strong>the forelock, the front of the '
      'head</strong>; that is: <strong>it is beneath Your overpowering and Your authority; You '
      'dispose of it however You will</strong> — so that You may turn its harm away from '
      'me.</em>'
      % (ar('أَعُوذُ'), ar('مِنْ شَرِّ كُلِّ دَابَّةٍ'), ar('أَنْتَ آخِذٌ بِنَاصِيَتِهَا'))))
b += B.sharh(
    p('Now the heart of it — the four names, which the student met in Lesson 9 from al-Ḥadīd 57:3. '
      'Here the Prophet &#65018; supplies the commentary himself, a clause for each. '
      '<em>These four names are <strong>two pairs</strong>:</em>') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .75rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>الأَوَّل · الآخِر</strong></td>'
    '<td style="padding:.6rem .75rem;border:1px solid var(--line)">two names for '
    '<strong>His beginninglessness and His endlessness</strong> '
    '(<span dir="rtl" lang="ar">أَزَلِيَّتِهِ وَأَبَدِيَّتِهِ</span>) — '
    '<em>nothing before You, nothing after You</em></td></tr>'
    '<tr><td style="padding:.6rem .75rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>الظَّاهِر · البَاطِن</strong></td>'
    '<td style="padding:.6rem .75rem;border:1px solid var(--line)">two names for '
    '<strong>His highness and His nearness</strong> '
    '(<span dir="rtl" lang="ar">عُلُوِّهِ وَقُرْبِهِ</span>) — '
    '<em>nothing above You, nothing nearer than You</em></td></tr>'
    '</table></div>' +
    p('<em>And <strong>these two are the place of the shāhid</strong> from the ḥadīth, because in '
      'them is <strong>the affirming of Allah\'s highness and His nearness, and that the two '
      'do not conflict and do not contradict</strong>.</em>') +
    p('And then al-Fawzān states it in the sentence this whole question has been working toward:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:1.02rem;font-weight:700;text-align:center" dir="rtl"'
    ' lang="ar">فَهُوَ قَرِيبٌ فِي عُلُوِّهِ، عَلِيٌّ فِي دُنُوِّهِ</p>'
    '<p style="margin:.55rem 0 0;font-size:.92rem;text-align:center">'
    '<em>— He is <strong>near in His highness, high in His nearness</strong>.</em></p></div>' +
    p('Note that the resolution is not a compromise between two attributes, and not a ranking of '
      'one over the other. <strong>Each is asserted <em>in</em> the other.</strong> And it is not '
      'a formula a theologian devised afterwards to patch a difficulty — it is the structure of a '
      'duʿāʾ the Prophet &#65018; taught, in which the two names sit side by side, each with its '
      'own explanatory clause attached by him.'))
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>what is upon me of the rights of Allah and the '
      'rights of the creation</strong>; and in this is <strong>a disavowal of one\'s own might '
      'and power</strong>.</em>' % ar('اقْضِ عَنِّي الدَّيْنَ')) +
    p('<strong>%s</strong> — <em>al-faqr is <strong>need</strong>; and al-faqīr is '
      '<strong>one who finds nothing, or finds some part of sufficiency</strong>.</em>'
      % ar('وَأَغْنِنِي مِنَ الفَقْرِ')) +
    p('<em>And in the ḥadīth also is <strong>the legislated practice of seeking nearness to Allah '
      'سبحانه وتعالى by His names and His attributes</strong>, in the fulfilling of a need and the '
      'answering of a supplication.</em> Which is what the duʿāʾ demonstrates rather than states: '
      '<strong>eight lines of naming Him, and two lines of asking.</strong>'))

b += B.heading('٤ · «ارْبَعُوا عَلَى أَنْفُسِكُم»', 'Fourth — "Go Easy on Yourselves"')
b += B.matn(
    'وَقَوْلُهُ ﷺ لَمَّا رَفَعَ الصَّحَابَةُ أَصْوَاتَهُمْ بِالذِّكْرِ: «أَيُّهَا '
    'النَّاسُ، ارْبَعُوا عَلَى أَنْفُسِكُمْ، فَإِنَّكُمْ لَا تَدْعُونَ أَصَمَّ وَلَا '
    'غَائِبًا، إِنَّمَا تَدْعُونَ سَمِيعًا بَصِيرًا قَرِيبًا، إِنَّ الَّذِي تَدْعُونَهُ '
    'أَقْرَبُ إِلَى أَحَدِكُمْ مِنْ عُنُقِ رَاحِلَتِهِ» مُتَّفَقٌ عَلَيْهِ.')
b += B.hadith(
    'أَيُّهَا النَّاسُ، ارْبَعُوا عَلَى أَنْفُسِكُمْ، فَإِنَّكُمْ لَا تَدْعُونَ أَصَمَّ '
    'وَلَا غَائِبًا، إِنَّمَا تَدْعُونَ سَمِيعًا بَصِيرًا قَرِيبًا، إِنَّ الَّذِي '
    'تَدْعُونَهُ أَقْرَبُ إِلَى أَحَدِكُمْ مِنْ عُنُقِ رَاحِلَتِهِ',
    '"O people, go easy on yourselves. You are not calling upon one who is deaf, nor one who is '
    'absent. You are only calling upon One who hears, sees, and is near. The One you are calling '
    'upon is nearer to each of you than the neck of his riding-beast."',
    'مُتَّفَقٌ عَلَيْهِ — al-Bukhārī and Muslim')
b += B.sharh(
    p('al-Fawzān gives the occasion: <em>and that was <strong>in the expedition of Khaybar</strong>, '
      'as comes in some of the routes of the ḥadīth; and <strong>the dhikr with which they raised '
      'their voices was the takbīr: %s</strong>.</em>'
      % ar('اللهُ أَكْبَرُ، لَا إِلَهَ إِلَّا اللهُ')) +
    p('So this is not a rebuke of people doing something wrong. <strong>They were magnifying '
      'Allah on a march.</strong> The correction is to the volume only, and the reason given for '
      'it is a point of creed.') +
    p('<strong>%s</strong> — <em>that is: <strong>be gentle</strong></em>. '
      '<strong>%s</strong> — <em>a reason given for the command to gentleness</em>.'
      % (ar('ارْبَعُوا'), ar('فَإِنَّكُمْ'))) +
    p('Now watch the structure of the sentence, because al-Fawzān points it out and it is the '
      'cleanest example in the book of the method from Lesson 6 — <strong>negate the deficiency, '
      'affirm its opposite</strong>:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>النَّفْي</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">'
    '<span dir="rtl" lang="ar">لَا تَدْعُونَ أَصَمَّ وَلَا غَائِبًا</span> — '
    '<em>He negated <strong>the defect preventing hearing</strong> and '
    '<strong>the defect preventing sight</strong></em></td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>الإِثْبَات</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">'
    '<span dir="rtl" lang="ar">إِنَّمَا تَدْعُونَ سَمِيعًا بَصِيرًا قَرِيبًا</span> — '
    '<em>and he affirmed <strong>their opposites</strong></em></td></tr>'
    '</table></div>' +
    p('<strong>So there is no cause for raising the voice.</strong> <em>%s — so '
      '<strong>He is near to whoever calls upon Him and remembers Him</strong>. So there is no '
      'need for raising the voices, when He is near, hearing them when they are lowered just as '
      'He hears them when they are raised.</em>'
      % ar('إِنَّ الَّذِي تَدْعُونَهُ أَقْرَبُ إِلَى أَحَدِكُمْ مِنْ عُنُقِ رَاحِلَتِهِ')) +
    p('And note the comparison he &#65018; chose. A man on a journey is sitting <em>on</em> the '
      'animal; its neck is the nearest thing in the world to him, right under his hands. '
      '<strong>Nearer than that</strong> — said to men shouting across a desert.'))
b += B.heading('حَصِيلَةُ هَذِهِ الأَحَادِيث', 'What These Aḥādīth Yield Together')
b += B.sharh(
    p('<em>So <strong>all of these aḥādīth together</strong> conveyed: <strong>the affirming of '
      'Allah\'s maʿiyyah with His creation, and His nearness to them, and His hearing of their '
      'voices, and His seeing of their movements</strong> — <strong>and that does not contradict '
      'His highness and His istiwāʾ upon His Throne.</strong> And the discussion of the maʿiyyah, '
      'its kinds and its evidences from the Noble Qurʾān, along with the explanation of those '
      'evidences, has already come.</em>') +
    p('That closing cross-reference is the author\'s own: <strong>he is pointing the reader back '
      'to Lesson 17.</strong> Part 1 established the two kinds of maʿiyyah and the moon analogy; '
      'Part 2 brings four Prophetic texts that say the same, and one of them — '
      '<em>near in His highness, high in His nearness</em> — states the resolution as a formula. '
      '<strong>The Sunnah here is doing its fourth function from Lesson 22: indicating what the '
      'Qurʾān indicated, and expressing what the Qurʾān expressed.</strong>'))

b += B.vocab([
    ('يَتَفَاضَل', 'yatafāḍal', 'admits of degrees',
     'From «أَفْضَلُ الإِيمَانِ» — if there is a best of it, it has degrees'),
    ('قِبَلَ وَجْهِه', 'qibala wajhih', 'before his face',
     'With kasrah on the ق — and Allah is مُوَاجِهُهُ, facing him'),
    ('النَّاصِيَة', 'al-nāṣiyah', 'the forelock',
     'The front of the head — every creature is held by it'),
    ('الأَوَّلُ وَالآخِر', 'al-awwal wa-l-ākhir', 'the First and the Last',
     'Two names for His beginninglessness and endlessness'),
    ('الظَّاهِرُ وَالبَاطِن', 'al-ẓāhir wa-l-bāṭin',
     'the Outermost and the Innermost',
     'Two names for His highness and His nearness — which do not conflict'),
    ('ارْبَعُوا', 'irbaʿū', 'go easy, be gentle',
     'Said of the volume, not of the dhikr itself'),
    ('الفَقْر', 'al-faqr', 'poverty, need',
     'And al-faqīr: one who finds nothing, or some part of sufficiency'),
])
b += B.mcq('ws-l28', [
    ('What second doctrine does al-Fawzān derive from the words %s?'
     % ar('أَفْضَلُ الإِيمَانِ'),
     ['That faith is only belief in the heart',
      'That īmān admits of degrees — for if there is a "best" of it, it is not one indivisible '
      'thing',
      'That faith is complete only with the Sunnah', 'That faith can be lost entirely'], 1),
    ('What effect does the ḥadīth say this knowledge has on a person?',
     ['It increases his dhikr',
      'His outward and his inward become equal, and he stands in awe of Him in every place',
      'It makes him fear travelling alone', 'It makes him pray at night'], 1),
    ('How does al-Fawzān keep %s from implying mixture with creation?'
     % ar('فَإِنَّ اللهَ قِبَلَ وَجْهِهِ'),
     ['By saying the ḥadīth is about the qiblah only',
      'By saying the facing is as befits Him: He is above His heavens, established on His Throne, '
      'and near to His creation, encompassing them',
      'By reading "Allah" as "the angel of Allah"',
      'By restricting it to the Prophet ﷺ'], 1),
    ('Why may the one praying not spit to his right?',
     ['Because the qiblah is to the right',
      'Out of honouring the right side, and because the two angels are on his right',
      'Because it is the direction of the imām', 'Because the ground is harder there'], 1),
    ('Into what two pairs does al-Fawzān divide the four names of the duʿāʾ?',
     ['Names of the Essence and names of the Actions',
      'الأَوَّل and الآخِر for His beginninglessness and endlessness; الظَّاهِر and البَاطِن for '
      'His highness and His nearness',
      'Names of mercy and names of might',
      'Names known to all and names known only to Him'], 1),
    ('What is al-Fawzān’s formula resolving the highness and the nearness?',
     ['He is high, and His nearness is His knowledge only',
      '%s — near in His highness, high in His nearness'
      % ar('فَهُوَ قَرِيبٌ فِي عُلُوِّهِ، عَلِيٌّ فِي دُنُوِّهِ'),
      'He is near to the believers and high above the disbelievers',
      'The two are affirmed without any relation between them'], 1),
    ('What is the structure of %s followed by %s?'
     % (ar('لَا تَدْعُونَ أَصَمَّ وَلَا غَائِبًا'), ar('إِنَّمَا تَدْعُونَ سَمِيعًا بَصِيرًا قَرِيبًا')),
     ['A rebuke followed by a consolation',
      'The negation of the defects preventing hearing and sight, then the affirming of their '
      'opposites',
      'A general statement then a specific one',
      'A command then its reason'], 1),
])
b += B.tf('ws-l28-tf', [
    ('الإِيمَانُ يَتَفَاضَلُ.', 'Īmān admits of degrees.', True),
    ('مُوَاجَهَةُ اللهِ لِلْمُصَلِّي تَقْتَضِي أَنَّهُ مُخْتَلِطٌ بِخَلْقِهِ.',
     'Allah’s facing the one praying entails that He is mixed with His creation.', False),
    ('«الظَّاهِرُ وَالبَاطِنُ» اسْمَانِ لِعُلُوِّهِ وَقُرْبِهِ.',
     'Al-Ẓāhir and al-Bāṭin are two names for His highness and His nearness.', True),
    ('نَهَى النَّبِيُّ ﷺ الصَّحَابَةَ عَنِ الذِّكْرِ نَفْسِهِ.',
     'The Prophet ﷺ forbade the Companions the dhikr itself.', False),
])
b += B.memorize(
    'أَنْتَ الظَّاهِرُ فَلَيْسَ فَوْقَكَ شَيْءٌ، وَأَنْتَ البَاطِنُ فَلَيْسَ دُونَكَ شَيْءٌ',
    'Two names and two clauses, and the Prophet ﷺ attached the clauses himself. Nothing is above '
    'Him, and nothing is nearer than He is. Carry al-Fawzān\'s summary with it: '
    '<span dir="rtl" lang="ar">قَرِيبٌ فِي عُلُوِّهِ، عَلِيٌّ فِي دُنُوِّهِ</span>.')
b += B.aiquiz('The maiyyah and nearness of Allah from the Sunnah in al-Aqidah al-Wasitiyyah: that '
              'iman admits of degrees from afdal al-iman, how the facing of the one praying does '
              'not imply mixture with creation, the four names of the dua divided into two pairs '
              'with qaribun fi uluwwih aliyyun fi dunuwwih, and the negation of the defects '
              'preventing hearing and sight followed by the affirming of their opposites in '
              'irbau ala anfusikum')
b += B.further()
b += B.nav('was-l27-arsh-jariyah.html', 'The Throne above Creation, and the Slave-Girl',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l28')

io.open(os.path.join(B.AQ, 'was-l28-maiyyah-qurb-sunnah.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'المَعِيَّةُ وَالقُرْبُ فِي السُّنَّة',
    'The Maʿiyyah and the Nearness in the Sunnah',
    'Lesson 28 of al-ʿAqīdah al-Wāsiṭiyyah: four '
    'aḥādīth of nearness, the four names of the Prophetic duʿāʾ in '
    'their two pairs, and the formula that settles the whole question — near in His '
    'highness, high in His nearness.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الثَّامِنُ وَالعِشْرُون', '3',
           'المَعِيَّةُ وَالقُرْبُ فِي السُّنَّة',
           'The Maʿiyyah and the Nearness in the Sunnah', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l28-maiyyah-qurb-sunnah.html')
