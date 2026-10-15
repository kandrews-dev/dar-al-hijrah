# -*- coding: utf-8 -*-
"""Wasitiyyah L48 -- Part 6: the standing of Ahl al-Bayt, and of the wives of
the Prophet, the Mothers of the Believers. Sharh pp.176-180."""
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
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Say who %s are, and the qualification al-Fawzān attaches to loving them.'
    % ar('أَهْلُ البَيْت'),
    'Give the two reasons the ḥadīth gives for loving the kinsfolk of the Prophet ﷺ.',
    'State precisely in what respect the wives are %s — and in what respect they are not.'
    % ar('أُمَّهَاتُ المُؤْمِنِين'),
    'Give al-Fawzān’s reasoning for why %s is the comparison chosen for ʿĀʾishah.'
    % ar('الثَّرِيد'),
])

b += B.heading('مَكَانَةُ أَهْلِ بَيْتِ النَّبِيِّ ﷺ عِنْدَ أَهْلِ السُّنَّة',
               'The Standing of the Prophet’s ﷺ Household with Ahl al-Sunnah')
b += B.matn(
    'وَيُحِبُّونَ أَهْلَ بَيْتِ رَسُولِ اللهِ ﷺ وَيَتَوَلَّوْنَهُمْ، وَيَحْفَظُونَ '
    'فِيهِمْ وَصِيَّةَ رَسُولِ اللهِ ﷺ حَيْثُ قَالَ: «أُذَكِّرُكُمُ اللهَ فِي أَهْلِ '
    'بَيْتِي». وَقَالَ أَيْضًا لِلْعَبَّاسِ عَمِّهِ — وَقَدِ اشْتَكَى إِلَيْهِ أَنَّ '
    'بَعْضَ قُرَيْشٍ يَجْفُو بَنِي هَاشِمٍ: «وَالَّذِي نَفْسِي بِيَدِهِ لَا '
    'يُؤْمِنُونَ حَتَّى يُحِبُّوكُمْ لِلَّهِ وَلِقَرَابَتِي». وَقَالَ: «إِنَّ اللهَ '
    'اصْطَفَى بَنِي إِسْمَاعِيلَ، وَاصْطَفَى مِنْ بَنِي إِسْمَاعِيلَ كِنَانَةَ، '
    'وَاصْطَفَى مِنْ كِنَانَةَ قُرَيْشًا، وَاصْطَفَى مِنْ قُرَيْشٍ بَنِي هَاشِمٍ».')
b += B.sharh(
    p('<strong>%s</strong> are <em>the family of the Prophet &#65018; <strong>upon whom the '
      'ṣadaqah is forbidden</strong></em> — <strong>بَنُو هَاشِمٍ</strong> and '
      '<strong>بَنُو عَبْدِ المُطَّلِبِ</strong>. <em>And <strong>the wives of the Prophet '
      '&#65018; and his daughters are of his household</strong></em>, as Allah said:'
      % ar('أَهْلُ البَيْت')))
b += B.ayah(
    'إِنَّمَا يُرِيدُ اللَّهُ لِيُذْهِبَ عَنْكُمُ الرِّجْسَ أَهْلَ الْبَيْتِ '
    'وَيُطَهِّرَكُمْ تَطْهِيرًا',
    '"Allah only wishes to remove impurity from you, O people of the House, and to purify you '
    'with a thorough purification."',
    'Sūrat al-Aḥzāb 33:33 · سُورَةُ الأَحْزَاب')
b += B.prose(
    'Read where that āyah sits. <strong>It comes in the middle of a passage addressed to the '
    'wives</strong> — «and remain in your houses… and establish the prayer» — and the words '
    '<em>O people of the House</em> fall inside it. That is why al-Fawzān lists the wives among '
    'Ahl al-Bayt without argument: <strong>the only place the Qurʾān uses the phrase, it is '
    'speaking to them.</strong>')
b += B.sharh(
    p('And the ground of the obligation: <em>loving them and honouring them — '
      '<strong>because Allah and His Messenger have both commanded it</strong></em>:'))
b += B.ayah(
    'قُلْ لَا أَسْأَلُكُمْ عَلَيْهِ أَجْرًا إِلَّا الْمَوَدَّةَ فِي الْقُرْبَى',
    '"Say: I ask of you no reward for it, except affection for the kinsfolk."',
    'Sūrat al-Shūrā 42:23 · سُورَةُ الشُّورَى')
b += B.sharh(
    p('<em>Such as <strong>al-ʿAbbās and his sons, and ʿAlī and his sons</strong></em> — and then '
      'the qualification, which the matn does not state and the sharḥ does: '
      '<em><strong>as for one who opposes the Sunnah and does not stand upright upon the '
      'religion, then he is not</strong></em> taken as an ally.') +
    p('<strong>That one clause separates this creed from the Rāfiḍah on one side and the Nawāṣib '
      'on the other.</strong> Kinship to the Prophet &#65018; is a real and honoured right; '
      '<em>it is not an immunity.</em> Loving the household is loving them <strong>as Muslims who '
      'are also his kin</strong> — not a loyalty that survives the abandoning of his Sunnah.') +
    p('<strong>%s</strong> — <em>that is: <strong>they love them</strong>; from %s, with a fatḥah '
      'on the wāw, <strong>and it is love</strong></em>. '
      '<strong>%s</strong> — <em>that is: <strong>they act by it and apply it.</strong></em>'
      % (ar('وَيَتَوَلَّوْنَهُمْ'), ar('الوَلَايَة'),
         ar('وَيَحْفَظُونَ فِيهِمْ وَصِيَّةَ رَسُولِ اللهِ ﷺ'))))
b += B.hadith(
    'أُذَكِّرُكُمُ اللهَ فِي أَهْلِ بَيْتِي',
    '"I remind you of Allah regarding the people of my household."',
    'رَوَاهُ مُسْلِمٌ')
b += B.sharh(
    p('al-Fawzān places it: <em>this was <strong>at غَدِير خُمّ</strong>, a pool on the road to '
      'Madīnah, <strong>which he &#65018; passed on his return from the Farewell Ḥajj</strong>, '
      'and he gave a sermon there — of which was what the Shaykh mentioned.</em>') +
    p('<em>And <strong>%s</strong> means: <strong>I remind you of what Allah commanded concerning '
      'my household — of respecting them, honouring them, and undertaking</strong> their '
      'rights.</em>' % ar('أُذَكِّرُكُمُ اللهَ فِي أَهْلِ بَيْتِي')) +
    p('Note what the wording is and is not. <strong>It is a reminder of an existing command, not '
      'the creation of a new rank.</strong> He &#65018; does not say «obey them» or «follow them» '
      '— he says <em>remember Allah</em> in how you treat them.'))
b += B.hadith(
    'وَالَّذِي نَفْسِي بِيَدِهِ لَا يُؤْمِنُونَ حَتَّى يُحِبُّوكُمْ لِلَّهِ '
    'وَلِقَرَابَتِي',
    '"By the One in whose Hand is my soul, they will not believe until they love you for Allah\'s '
    'sake and for my kinship."',
    'al-Fawzān cites it as رَوَاهُ الإِمَامُ أَحْمَدُ وَغَيْرُهُ')
b += B.sharh(
    '<div style="background:#fff8e6;border-right:4px solid #d4a017;'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .9rem">'
    '<p style="margin:0;font-size:.9rem"><strong dir="rtl" lang="ar">تَنْبِيهٌ</strong> — '
    'al-Fawzān gives this ḥadīth’s attribution <strong>without stating a '
    'grading</strong>. Per the rule in Lesson 22 this page reports the attribution and '
    '<strong>supplies no grading of its own</strong>. The obligation does not rest on it alone: '
    'the āyah of al-Shūrā and the ḥadīth of Ghadīr Khumm '
    '(<strong>Muslim</strong>) establish it.</p></div>' +
    p('<em>He is <strong>العَبَّاسُ بْنُ عَبْدِ المُطَّلِبِ</strong>; <strong>%s</strong> means '
      '<strong>he informed him of what he disliked</strong>; and <strong>%s is the abandoning of '
      'kindness and of the ties of kinship.</strong></em>'
      % (ar('وَقَدِ اشْتَكَى إِلَيْهِ'), ar('الجَفَاء'))) +
    p('<strong>%s</strong> — <em>that is: <strong>the complete obligatory faith</strong></em>, as '
      'in Lesson 45. And <strong>%s</strong> — <em>that is, <strong>for two things</strong>:</em>'
      % (ar('لَا يُؤْمِنُونَ'), ar('حَتَّى يُحِبُّوكُمْ لِلَّهِ وَلِقَرَابَتِي'))) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.92rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>لِلَّهِ</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<em>seeking nearness to Allah by it — <strong>because they are of His '
    'allies</strong></em></td></tr>'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>وَلِقَرَابَتِي</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<em>because they are <strong>the kinsfolk of the Messenger of Allah &#65018;</strong> '
    '— <strong>and in that is a pleasing of him and an honouring of him</strong></em></td></tr>'
    '</table></div>' +
    p('The first reason is the one that supplies the qualification given above. '
      '<strong>They are to be loved «for Allah» because they are of His allies</strong> — so the '
      'love is owed on a ground that a man can forfeit, alongside a ground of kinship that he '
      'cannot.'))
b += B.hadith(
    'إِنَّ اللهَ اصْطَفَى بَنِي إِسْمَاعِيلَ، وَاصْطَفَى مِنْ بَنِي إِسْمَاعِيلَ '
    'كِنَانَةَ، وَاصْطَفَى مِنْ كِنَانَةَ قُرَيْشًا، وَاصْطَفَى مِنْ قُرَيْشٍ بَنِي '
    'هَاشِمٍ، وَاصْطَفَانِي مِنْ بَنِي هَاشِمٍ',
    '"Allah chose the children of Ismāʿīl, and chose Kinānah from the children of Ismāʿīl, and '
    'chose Quraysh from Kinānah, and chose Banū Hāshim from Quraysh, and chose me from Banū '
    'Hāshim."',
    'رَوَاهُ أَحْمَدُ وَمُسْلِمٌ')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>chose</strong>; and %s is <strong>the choicest '
      'part</strong></em>. <strong>%s</strong> — <em>the son of Ibrāhīm al-Khalīl</em> '
      'عليهما السلام. <strong>%s</strong> — <em>the name of a tribe; their father is '
      '<strong>كِنَانَةُ بْنُ خُزَيْمَةَ</strong></em>. And <strong>بَنُو هَاشِمٍ</strong> are '
      'the descendants of <em>هَاشِمِ بْنِ عَبْدِ مَنَافِ بْنِ قُصَيِّ بْنِ كِلَابٍ</em>.'
      % (ar('اصْطَفَى'), ar('الصَّفْوَة'), ar('بَنِي إِسْمَاعِيلَ'), ar('كِنَانَة'))) +
    p('<em>And the shāhid of the ḥadīth: that in it is <strong>a proof of the excellence of the '
      'Arabs, and that Quraysh are the best of the Arabs, and that Banū Hāshim are the best of '
      'Quraysh, and that the Messenger &#65018; is the best of Banū Hāshim</strong> — '
      '<strong>so he is the best of creation in himself and the best of them in '
      'lineage.</strong></em>') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.95rem;text-align:center">'
    'بَنُو إِسْمَاعِيل &nbsp;→&nbsp; '
    'كِنَانَة &nbsp;→&nbsp; قُرَيْش '
    '&nbsp;→&nbsp; بَنُو هَاشِم &nbsp;→&nbsp; '
    '<strong>مُحَمَّد ط</strong></p>'
    '<p style="margin:.5rem 0 0;font-size:.9rem;text-align:center"><em>Four narrowings, each one '
    'a choosing — and the last term is a single man.</em></p></div>' +
    p('And notice what that does to the question this section is really about. '
      '<strong>The honour of Banū Hāshim is derived — it is the honour of being the house the '
      'chosen one came from.</strong> It is not a standing that competes with his, and it is not '
      'inherited independently of him. Which is why loving them is counted as '
      '<em>honouring him</em> in the previous ḥadīth.'))

b += B.heading('مَكَانَةُ أَزْوَاجِ النَّبِيِّ ﷺ · أُمَّهَاتُ المُؤْمِنِين',
               'The Wives of the Prophet ﷺ — the Mothers of the Believers')
b += B.matn(
    'وَيَتَوَلَّوْنَ أَزْوَاجَ النَّبِيِّ ﷺ أُمَّهَاتِ المُؤْمِنِينَ، وَيُؤْمِنُونَ '
    'بِأَنَّهُنَّ أَزْوَاجُهُ فِي الآخِرَةِ؛ خُصُوصًا خَدِيجَةَ رَضِيَ اللهُ عَنْهَا، '
    'أُمَّ أَكْثَرِ أَوْلَادِهِ، وَأَوَّلَ مَنْ آمَنَ بِهِ وَعَاضَدَهُ عَلَى أَمْرِهِ، '
    'وَكَانَ لَهَا مِنْهُ المَنْزِلَةُ العَالِيَةُ؛ وَالصِّدِّيقَةَ بِنْتَ '
    'الصِّدِّيقِ رَضِيَ اللهُ عَنْهَا، الَّتِي قَالَ فِيهَا النَّبِيُّ ﷺ: «فَضْلُ '
    'عَائِشَةَ عَلَى النِّسَاءِ كَفَضْلِ الثَّرِيدِ عَلَى سَائِرِ الطَّعَامِ».')
b += B.sharh(
    p('<em>That is: <strong>they love them and revere them</strong>, because they are '
      '<strong>%s</strong></em> — and here al-Fawzān draws a distinction that a great deal of '
      'confusion turns on:' % ar('أُمَّهَاتُ المُؤْمِنِين')) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.91rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);vertical-align:top">'
    '<strong>mothers IN</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<em><strong>respect and reverence, and the forbiddance of marrying them to the '
    'Ummah</strong></em></td></tr>'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);vertical-align:top">'
    '<strong>but NOT in</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<em>the remaining rulings — <strong>their ruling is the ruling of unrelated women</strong>, '
    'as regards <strong>the forbiddance of seclusion with them and of looking at them</strong></em></td></tr>'
    '</table></div>' +
    p('<strong>Motherhood here is a legal status, not a biological fiction.</strong> It gives '
      'reverence and it closes marriage — and it does not open what maḥram status would open. '
      'The Qurʾān itself shows this: it calls them mothers in one āyah, and in another commands '
      'the believers to address them <em>from behind a screen</em>.'))
b += B.ayah(
    'النَّبِيُّ أَوْلَى بِالْمُؤْمِنِينَ مِنْ أَنْفُسِهِمْ وَأَزْوَاجُهُ أُمَّهَاتُهُمْ',
    '"The Prophet is closer to the believers than their own selves, and his wives are their '
    'mothers."',
    'Sūrat al-Aḥzāb 33:6 · سُورَةُ الأَحْزَاب')
b += B.ayah(
    'وَإِذَا سَأَلْتُمُوهُنَّ مَتَاعًا فَاسْأَلُوهُنَّ مِنْ وَرَاءِ حِجَابٍ ذَلِكُمْ '
    'أَطْهَرُ لِقُلُوبِكُمْ وَقُلُوبِهِنَّ وَمَا كَانَ لَكُمْ أَنْ تُؤْذُوا رَسُولَ '
    'اللَّهِ وَلَا أَنْ تَنْكِحُوا أَزْوَاجَهُ مِنْ بَعْدِهِ أَبَدًا',
    '"And when you ask them for something, ask them from behind a screen; that is purer for your '
    'hearts and theirs. And it is not for you to hurt the Messenger of Allah, nor ever to marry '
    'his wives after him."',
    'Sūrat al-Aḥzāb 33:53 · سُورَةُ الأَحْزَاب')
b += B.sharh(
    p('<em>And he &#65018; died leaving <strong>nine</strong>: <strong>عَائِشَة · حَفْصَة · '
      'زَيْنَبُ بِنْتُ جَحْشٍ · أُمُّ سَلَمَةَ · صَفِيَّة · مَيْمُونَة · أُمُّ حَبِيبَةَ · '
      'سَوْدَة · جُوَيْرِيَة</strong> رضي الله عنهن.</em>') +
    p('<em>As for <strong>خَدِيجَة</strong>, he married her <strong>before the prophethood, and '
      'did not marry another alongside her until she died</strong>. And he &#65018; married '
      '<strong>زَيْنَبَ بِنْتَ خُزَيْمَةَ الهِلَالِيَّةَ</strong>, and she remained only a '
      'short while, then died. <strong>These are the total of those he consummated marriage with: '
      'eleven</strong> رضي الله عنهن.</em>') +
    p('<em>And they believe <strong>that they are his wives in the Hereafter</strong> — '
      '<strong>and in this is an honour for them and a mighty excellence.</strong></em>'))

b += B.heading('خَدِيجَةُ رَضِيَ اللهُ عَنْهَا', 'Khadījah رضي الله عنها')
b += B.sharh(
    p('al-Fawzān numbers the four merits the author singles out:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>١</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<strong>the mother of most of his children</strong> — <em>for all his children were '
    'from her except Ibrāhīm, who was from Māriyah al-Qibṭiyyah</em></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>٢</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<strong>the first to believe in him</strong> — <em>unrestrictedly, on one view (which '
    'is the one the Shaykh mentions here); or the first of the WOMEN to believe, on the '
    'other</em></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>٣</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<strong>the first to support and aid him at the beginning of his affair</strong> — '
    '<em>and <strong>her support of him was in the greatest of the times of need</strong></em></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>٤</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<strong>she had the highest standing with him</strong> — <em>he loved her and '
    'mentioned her often and praised her</em></td></tr>'
    '</table></div>' +
    p('The third is the one that is easy to read past. <strong>Anyone can support a cause that is '
      'winning.</strong> Khadījah\'s support came when there was no cause yet — one man, one '
      'terrified night, and a wife who believed him before there was anything to join.'))

b += B.heading('الصِّدِّيقَةُ بِنْتُ الصِّدِّيق', 'al-Ṣiddīqah, Daughter of al-Ṣiddīq')
b += B.sharh(
    p('<em>That is: <strong>عَائِشَةُ بِنْتُ أَبِي بَكْرٍ</strong>; and <strong>%s is '
      'one who goes to the utmost in truthfulness</strong> — <strong>and the Prophet &#65018; '
      'gave Abū Bakr that title.</strong></em>' % ar('الصِّدِّيق')) +
    p('And her excellences, as al-Fawzān lists them: <em><strong>she was the most beloved of the '
      'Prophet\'s &#65018; wives to him</strong>; <strong>he married no virgin besides her</strong>; '
      '<strong>the revelation would descend upon him while he was in her blanket</strong>; '
      '<strong>Allah declared her innocent of what the people of the slander accused her '
      'of</strong>; <strong>she was the most learned in fiqh of his wives</strong>; '
      '<strong>and the senior Companions, when a matter was difficult for them, would ask her for '
      'a ruling</strong>; <strong>and the Messenger &#65018; died in her house, between her chest '
      'and her throat, and was buried in her house.</strong></em>') +
    p('<strong>The senior Companions used to ask her.</strong> That is not a domestic detail; it '
      'is a statement about the transmission of the religion — and it is why reviling her is not '
      'a private insult but an attack on a channel the Sharīʿah came through.'))
b += B.hadith(
    'فَضْلُ عَائِشَةَ عَلَى النِّسَاءِ كَفَضْلِ الثَّرِيدِ عَلَى سَائِرِ الطَّعَامِ',
    '"The excellence of ʿĀʾishah over women is like the excellence of tharīd over all other '
    'food."',
    'رَوَاهُ البُخَارِيُّ وَمُسْلِمٌ وَغَيْرُهُمَا')
b += B.sharh(
    p('Why <em>tharīd</em>, of all comparisons? al-Fawzān works it out, and the reasoning is a '
      'small pleasure in itself:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.94rem">'
    '<p style="margin:0 0 .6rem"><em>— <strong>al-tharīd is the best of foods, because '
    'it is bread and meat.</strong></em></p>'
    '<p style="margin:0 0 .6rem"><em>— <strong>And the bread is from wheat, and it is the '
    'best of the staples; and the meat is the best of what is eaten with bread.</strong></em></p>'
    '<p style="margin:0"><em>— <strong>So if the meat is the master of what accompanies, and '
    'the wheat is the master of the staple — and the two of them together are the '
    'tharīd — then the tharīd is the best.</strong></em></p></div>' +
    p('So the comparison is not «a nice dish». <strong>It is the one food that is the best of two '
      'categories at once</strong>, which is a precise way of saying what is being claimed for '
      'her: not merely the best in one respect, but the joining of excellences that are usually '
      'found apart. <strong>And the ḥadīth is a comparison of excellences, not of '
      'persons</strong> — it says <em>faḍl</em>, as Lesson 29 said of the moon.'))

b += B.vocab([
    ('أَهْلُ البَيْت', 'ahl al-bayt', 'the people of the House',
     'Banū Hāshim and Banū ʿAbd al-Muṭṭalib, upon whom '
     'ṣadaqah is forbidden — and his wives and daughters'),
    ('الوَلَايَة', 'al-walāyah', 'allegiance, love',
     'With a fatḥah on the wāw — and it is love'),
    ('الجَفَاء', 'al-jafāʾ', 'coldness',
     'The abandoning of kindness and of the ties of kinship'),
    ('غَدِيرُ خُمّ', 'Ghadīr Khumm', 'the pool of Khumm',
     'On the road to Madīnah, passed on the return from the Farewell Ḥajj'),
    ('الصَّفْوَة', 'al-ṣafwah', 'the choicest part',
     'From اصطفى, to choose — four narrowings to one man'),
    ('أُمَّهَاتُ المُؤْمِنِين', 'ummahāt al-muʿminīn',
     'the Mothers of the Believers',
     'In reverence and the forbiddance of marriage — NOT in the rulings of maḥram'),
    ('الصِّدِّيق', 'al-ṣiddīq', 'the utterly truthful',
     'One who goes to the utmost in truthfulness — the Prophet ط titled Abū Bakr so'),
    ('الثَّرِيد', 'al-tharīd', 'tharīd',
     'Bread and meat — the master of the staple joined to the master of what accompanies it'),
])
b += B.mcq('ws-l48', [
    ('Who are Ahl al-Bayt, per al-Fawzān?',
     ['ʿAlī, Fāṭimah, al-Ḥasan and al-Ḥusayn only',
      'Banū Hāshim and Banū ʿAbd al-Muṭṭalib — those upon whom ṣadaqah is forbidden — and his '
      'wives and daughters',
      'All of Quraysh', 'His descendants through Fāṭimah alone'], 1),
    ('What qualification does al-Fawzān attach to taking them as allies?',
     ['That they must be known personally',
      'That one who opposes the Sunnah and does not stand upright upon the religion is not — '
      'kinship is a right, not an immunity',
      'That they must be descendants in the male line',
      'That they must be living in the Ḥaramayn'], 1),
    ('What is notable about where al-Aḥzāb 33:33 sits?',
     ['It comes after the verse of the ḥijāb',
      'It falls in the middle of a passage addressed to the WIVES — so the one place the Qurʾān '
      'uses "people of the House", it is speaking to them',
      'It was revealed at Ghadīr Khumm',
      'It abrogates an earlier ruling'], 1),
    ('What two reasons does the ḥadīth give for loving the kinsfolk?',
     ['Their lineage and their knowledge',
      'For Allah — because they are of His allies; and for his kinship ﷺ — in which is a pleasing '
      'and an honouring of him',
      'Their precedence and their jihād',
      'Their poverty and their patience'], 1),
    ('What does the chain of choosing establish?',
     ['That lineage determines a man’s rank with Allah',
      'That the Arabs, then Quraysh, then Banū Hāshim, then the Messenger ﷺ — so he is the best '
      'of creation in himself AND in lineage',
      'That only Banū Hāshim may lead the prayer',
      'That Ismāʿīl was better than Isḥāq'], 1),
    ('In what respect are the wives "Mothers of the Believers" — and in what respect not?',
     ['In every respect, as with a birth mother',
      'In respect and reverence and the forbiddance of marrying them; but their ruling is that of '
      'unrelated women regarding seclusion and looking',
      'Only in inheritance', 'Only in being addressed as "mother"'], 1),
    ('Which of Khadījah’s four merits concerns the timing of her support?',
     ['That she was the mother of most of his children',
      'That she was the first to support and aid him at the beginning of his affair — and her '
      'support was in the greatest of the times of need',
      'That she had the highest standing with him',
      'That he married no one alongside her'], 1),
    ('Why is tharīd the comparison chosen for ʿĀʾishah?',
     ['Because it was the Prophet’s ﷺ favourite dish',
      'Because it is bread and meat — the master of the staple joined to the master of what '
      'accompanies it, so it is the best of two categories at once',
      'Because it was the food of the poor',
      'Because it is easily shared'], 1),
])
b += B.tf('ws-l48-tf', [
    ('أَزْوَاجُ النَّبِيِّ ﷺ وَبَنَاتُهُ مِنْ أَهْلِ بَيْتِهِ.',
     'The wives and daughters of the Prophet ﷺ are of his household.', True),
    ('مَنْ خَالَفَ السُّنَّةَ مِنْ أَهْلِ البَيْتِ يُتَوَلَّى لِقَرَابَتِهِ.',
     'One of Ahl al-Bayt who opposes the Sunnah is still taken as an ally for his kinship.',
     False),
    ('أُمَّهَاتُ المُؤْمِنِينَ حُكْمُهُنَّ حُكْمُ المَحَارِمِ فِي الخَلْوَةِ وَالنَّظَرِ.',
     'The Mothers of the Believers have the ruling of maḥrams regarding seclusion and looking.',
     False),
    ('كَانَ أَكَابِرُ الصَّحَابَةِ يَسْتَفْتُونَ عَائِشَةَ رَضِيَ اللهُ عَنْهَا.',
     'The senior Companions used to ask ʿĀʾishah رضي الله عنها for rulings.', True),
])
b += B.memorize(
    'أُذَكِّرُكُمُ اللهَ فِي أَهْلِ بَيْتِي',
    'Note what he ﷺ asked for and what he did not. Not obedience to them, and not a station — '
    'but that you remember <em>Allah</em> in how you treat them. The right is real, and it is a '
    'right of honour and kindness, which is exactly how Ahl al-Sunnah hold it.')
b += B.aiquiz('Ahl al-Bayt and the wives of the Prophet in al-Aqidah al-Wasitiyyah: who Ahl '
              'al-Bayt are and the qualification that one who opposes the Sunnah is not taken as '
              'an ally, how al-Ahzab 33:33 sits inside a passage addressed to the wives, the two '
              'reasons for loving the kinsfolk, the four narrowings of the hadith of istifa, the '
              'precise sense in which the wives are Mothers of the Believers and the sense in '
              'which they are not, Khadijahs four merits with the timing of her support, and why '
              'tharid is the comparison for Aishah')
b += B.further()
b += B.nav('was-l47-maratib-al-sahabah.html', 'The Ranks of the Companions',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l48')

io.open(os.path.join(B.AQ, 'was-l48-ahl-al-bayt-wa-al-azwaj.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'أَهْلُ البَيْتِ وَأَزْوَاجُ النَّبِيِّ ﷺ',
    'The Household and the Wives of the Prophet ﷺ',
    'Lesson 48 of al-ʿAqīdah al-Wāsiṭiyyah: who Ahl al-Bayt are '
    'and why kinship is a right rather than an immunity; the two reasons for loving the '
    'kinsfolk; the four narrowings that end in one man; and the precise sense in which the wives '
    'are Mothers of the Believers — together with the sense in which they are not.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الثَّامِنُ وَالأَرْبَعُون', '6',
           'أَهْلُ البَيْتِ وَأَزْوَاجُ النَّبِيِّ ﷺ',
           'The Household and the Wives of the Prophet ﷺ', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l48-ahl-al-bayt-wa-al-azwaj.html')
