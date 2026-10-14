# -*- coding: utf-8 -*-
"""Wasitiyyah L40 -- Part 4 closes: the first to seek the opening of the Garden,
and the intercessions -- eight kinds, two conditions, and the three parties.
Sharh pp.140-143."""
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
    'Lesson 15 of this track, and <em>al-Qawāʿid al-Arbaʿ</em>, cover the courtly analogy that '
    'produced the first of the three errors set out here.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Give the derivation of %s and what the image behind it is.' % ar('الشَّفَاعَة'),
    'Name the three intercessions particular to the Prophet ﷺ.',
    'State the two conditions of a valid intercession, with their proofs.',
    'Name the three parties into which people divided over intercession, and the error of each.',
])

b += B.heading('٩ · أَوَّلُ مَنْ يَسْتَفْتِحُ بَابَ الجَنَّة',
               'Ninth — The First to Seek the Opening of the Garden')
b += B.matn(
    'وَأَوَّلُ مَنْ يَسْتَفْتِحُ بَابَ الجَنَّةِ مُحَمَّدٌ ﷺ، وَأَوَّلُ مَنْ '
    'يَدْخُلُهَا مِنَ الأُمَمِ أُمَّتُهُ. وَلَهُ ﷺ فِي القِيَامَةِ ثَلَاثُ '
    'شَفَاعَاتٍ: أَمَّا الشَّفَاعَةُ الأُولَى فَيَشْفَعُ فِي أَهْلِ المَوْقِفِ حَتَّى '
    'يُقْضَى بَيْنَهُمْ، بَعْدَ أَنْ يَتَرَادَّ الأَنْبِيَاءُ: آدَمُ وَنُوحٌ '
    'وَإِبْرَاهِيمُ وَمُوسَى وَعِيسَى ابْنُ مَرْيَمَ عَنِ الشَّفَاعَةِ حَتَّى '
    'تَنْتَهِيَ إِلَيْهِ. وَأَمَّا الشَّفَاعَةُ الثَّانِيَةُ فَيَشْفَعُ فِي أَهْلِ '
    'الجَنَّةِ أَنْ يَدْخُلُوا الجَنَّةَ؛ وَهَاتَانِ الشَّفَاعَتَانِ خَاصَّتَانِ '
    'لَهُ. وَأَمَّا الشَّفَاعَةُ الثَّالِثَةُ فَيَشْفَعُ فِيمَنِ اسْتَحَقَّ '
    'النَّارَ — وَهَذِهِ الشَّفَاعَةُ لَهُ وَلِسَائِرِ النَّبِيِّينَ '
    'وَالصِّدِّيقِينَ وَغَيْرِهِمْ.')
b += B.sharh(
    p('al-Fawzān marks where the narrative has reached: <em>the Shaykh explains '
      '<strong>what the affair of the believers comes to on the Day of Rising, after they have '
      'passed through those states</strong></em> — Lessons 36 to 39. '
      '<em>So they <strong>do not enter the Garden except after a permission from Allah تعالى and '
      'a request for its gates to be opened.</strong></em>') +
    p('That is the hinge of this lesson, and it is easy to read past. '
      '<strong>The believers are cleared, settled and standing at the gate — and the gate is '
      'still shut.</strong> Everything that follows is about who asks for it to be opened.'))
b += B.hadith(
    'آتِي بَابَ الجَنَّةِ يَوْمَ القِيَامَةِ فَأَسْتَفْتِحُ، فَيَقُولُ الخَازِنُ: مَنْ '
    'أَنْتَ؟ فَأَقُولُ: مُحَمَّدٌ',
    '"I shall come to the gate of the Garden on the Day of Rising and seek its opening. The '
    'keeper will say: who are you? And I shall say: Muḥammad."',
    'فِي الصَّحِيح — from Anas رضي الله عنه')
b += B.sharh(
    p('<strong>%s</strong> is <em>the seeking of the opening; <strong>and in this is an ennobling '
      'of him &#65018; and a showing forth of his excellence.</strong></em>'
      % ar('الاسْتِفْتَاح')) +
    p('<strong>%s</strong> — <em>and that is <strong>because of its excellence over the rest of '
      'the nations.</strong></em> Its proof is <em>in the ḥadīth of '
      '<strong>أَبِي هُرَيْرَةَ</strong> which <strong>Muslim</strong> reported, of his saying '
      '&#65018;: <strong>«and we are the first to enter the Garden».</strong></em>'
      % ar('وَأَوَّلُ مَنْ يَدْخُلُهَا مِنَ الأُمَمِ أُمَّتُهُ')))

b += B.heading('الشَّفَاعَةُ · لُغَةً وَعُرْفًا', 'Intercession — in the Language, and in Usage')
b += B.sharh(
    p('<strong>%s</strong> — <em>in the language is <strong>%s — the means</strong>; and in usage '
      'it is <strong>%s — asking good for another.</strong></em>'
      % (ar('الشَّفَاعَة'), ar('الوَسِيلَة'), ar('سُؤَالُ الخَيْرِ لِلْغَيْرِ'))) +
    p('And then the derivation, which carries the whole picture: <em>it is '
      '<strong>derived from %s, which is the opposite of %s — the odd</strong>; '
      '<strong>as though the intercessor joined his request to the request of the one '
      'interceded for, after it had been alone.</strong></em>'
      % (ar('الشَّفْع'), ar('الوَتْر'))) +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.95rem">One request becomes two. <strong>The petitioner was '
    'an odd number and the intercessor makes him even</strong> — which means the '
    '<em>petitioner must already be petitioning</em>. '
    '<strong>Intercession is a second voice added to a request that exists, not a request made '
    'on behalf of someone who is making none.</strong></p></div>' +
    p('The student met this derivation in Lesson 8, on Āyat al-Kursī. '
      '<strong>Here it does doctrinal work</strong>: it is already, by itself, the answer to the '
      'first of the three errors below.'))

b += B.heading('أَنْوَاعُ الشَّفَاعَةِ الثَّمَانِيَة', 'The Eight Kinds of Intercession')
b += B.sharh(
    p('<em>Thus the Shaykh رحمه الله mentioned the kinds of intercession here '
      '<strong>in brief</strong>; and <strong>by way of a full enumeration they are eight '
      'kinds</strong>: <strong>of them what is particular to the Prophet &#65018;, and of them '
      'what is shared between him and others.</strong></em>') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.88rem;margin:0 0 .7rem">'
    '<tr><td colspan="2" style="padding:.5rem .75rem;border:1px solid var(--line);'
    'background:var(--brand-wash);font-weight:700">خَاصَّةٌ بِالنَّبِيِّ ﷺ — particular '
    'to him</td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>١</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">'
    '<strong>الشَّفَاعَةُ العُظْمَى</strong> — and it is '
    '<strong>المَقَامُ المَحْمُود</strong>: <em>that he &#65018; intercede that Allah judge '
    'between His servants, <strong>after the standing has grown long upon them</strong>, and '
    '<strong>after their going from prophet to prophet to undertake it</strong> — and our '
    'Prophet &#65018; undertakes it <strong>after the permission of his Lord</strong></em></td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>٢</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">'
    'his intercession <strong>for the people of the Garden to enter it</strong>, after the '
    'finishing of the Reckoning</td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>٣</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">'
    'his intercession <strong>for his uncle أَبِي طَالِبٍ, that the punishment be lightened for '
    'him</strong> — <em>and this is particular to him, because Allah informed that the '
    'disbelievers are not benefited by the intercession of the intercessors, and our Prophet '
    'informed that <strong>his intercession is particular to the people of tawḥīd</strong>. '
    'So his intercession for his uncle is <strong>particular to him and particular to Abū '
    'Ṭālib</strong></em></td></tr>'
    '<tr><td colspan="2" style="padding:.5rem .75rem;border:1px solid var(--line);'
    'background:var(--ivory);font-weight:700">يُشَارِكُهُ فِيهَا غَيْرُهُ — shared with the '
    'prophets, the angels, the ṣiddīqūn and the martyrs</td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>٤</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">for '
    '<strong>one of the disobedient monotheists who deserved the Fire, that he not enter '
    'it</strong></td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>٥</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">for '
    '<strong>one of the disobedient monotheists who entered the Fire, that he come out of '
    'it</strong></td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>٦</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">for '
    '<strong>the raising of the ranks of some of the people of the Garden</strong></td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>٧</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">for '
    '<strong>those whose good and evil deeds were equal, that they enter the Garden</strong> '
    '— <em>and they are <strong>أَهْلُ الأَعْرَاف</strong>, upon one '
    'statement</em></td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>٨</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">for '
    '<strong>the entry of some believers into the Garden without reckoning or '
    'punishment</strong> — as his intercession for '
    '<strong>عُكَاشَةَ بْنِ مِحْصَنٍ</strong> رضي الله '
    'عنه, when the Prophet &#65018; supplicated that he be of '
    '<strong>the seventy thousand</strong> who enter the Garden without reckoning or '
    'punishment</td></tr>'
    '</table></div>' +
    p('Two observations the table makes visible. First: <strong>the one intercession everybody has '
      'heard of — for sinners to be spared the Fire or taken out of it — is not among the three '
      'that belong to him alone.</strong> The prophets, the angels, the ṣiddīqūn and the martyrs '
      'share it. Second: <strong>the greatest of them is not about rescuing anyone.</strong> '
      '<em>al-Shafāʿah al-ʿUẓmā</em> is a request that the judging <em>begin</em> — made when the '
      'standing has become unbearable and every earlier prophet has declined.'))

b += B.heading('شَرْطَا الشَّفَاعَة', 'The Two Conditions of Intercession')
b += B.sharh(
    p('<em>And <strong>Ahl al-Sunnah wa-l-Jamāʿah believe in all of these intercessions</strong>, '
      'because of the establishment of their proofs — <strong>and that they do not occur except '
      'by two conditions</strong>:</em>') +
    p('<strong>الشَّرْطُ الأَوَّل · %s</strong> — <em>Allah\'s permission to the intercessor that '
      'he intercede</em>:' % ar('إِذْنُ اللهِ لِلشَّافِعِ أَنْ يَشْفَعَ')))
b += B.ayah(
    'مَنْ ذَا الَّذِي يَشْفَعُ عِنْدَهُ إِلَّا بِإِذْنِهِ',
    '"Who is there that can intercede with Him except by His permission?"',
    'Sūrat al-Baqarah 2:255 · سُورَةُ البَقَرَة')
b += B.ayah(
    'مَا مِنْ شَفِيعٍ إِلَّا مِنْ بَعْدِ إِذْنِهِ',
    '"There is no intercessor except after His permission."',
    'Sūrat Yūnus 10:3 · سُورَةُ يُونُس')
b += B.sharh(
    p('<strong>الشَّرْطُ الثَّانِي · %s</strong> — <em>Allah\'s being pleased with the one '
      'interceded for</em>:' % ar('رِضَا اللهِ عَنِ المَشْفُوعِ لَهُ')))
b += B.ayah(
    'وَلَا يَشْفَعُونَ إِلَّا لِمَنِ ارْتَضَى',
    '"And they do not intercede except for one with whom He is pleased."',
    'Sūrat al-Anbiyāʾ 21:28 · سُورَةُ الأَنْبِيَاء')
b += B.sharh(p('<em>And <strong>the two conditions are gathered together</strong> in His saying:</em>'))
b += B.ayah(
    'وَكَمْ مِنْ مَلَكٍ فِي السَّمَاوَاتِ لَا تُغْنِي شَفَاعَتُهُمْ شَيْئًا إِلَّا مِنْ '
    'بَعْدِ أَنْ يَأْذَنَ اللَّهُ لِمَنْ يَشَاءُ وَيَرْضَى',
    '"And how many an angel there is in the heavens whose intercession avails nothing at all — '
    'except after Allah permits, for whom He wills and is pleased with."',
    'Sūrat al-Najm 53:26 · سُورَةُ النَّجْم')
b += B.prose(
    'Both conditions are about Allah, and neither is about the intercessor\'s standing. '
    '<strong>The angels are named in the third āyah precisely because they are the most exalted '
    'creatures anyone could appeal to</strong> — and their intercession <em>avails nothing at '
    'all</em> until He permits it and is pleased with its object. '
    '<strong>So intercession is not influence brought to bear on Allah; it is something He grants '
    'twice over before it happens.</strong>')

b += B.heading('مُخَالَفَةُ المُعْتَزِلَة', 'The Muʿtazilah’s Opposition')
b += B.sharh(
    p('<em>And <strong>the Muʿtazilah opposed over the intercession for the people of the major '
      'sins among the believers</strong> — <strong>for the one of them who deserved the Fire, '
      'that he not enter it; and the one who entered it, that he come out</strong>. And '
      '<strong>they argue with His saying:</strong></em>'))
b += B.ayah(
    'فَمَا تَنْفَعُهُمْ شَفَاعَةُ الشَّافِعِينَ',
    '"So the intercession of the intercessors will not avail them."',
    'Sūrat al-Muddaththir 74:48 · سُورَةُ المُدَّثِّر')
b += B.sharh(
    p('<strong>The answer:</strong> <em>that <strong>it came concerning the disbelievers</strong> '
      '— <strong>they are the ones whom the intercession of the intercessors does not benefit. '
      'As for the believers, the intercession benefits them, with its conditions.</strong></em>') +
    p('And the answer is simply a matter of reading the preceding āyāt, which name who «them» is. '
      '<strong>The Muʿtazilī argument requires the pronoun to mean <em>sinners</em> when the '
      'passage has been describing <em>deniers</em></strong> — and the point of difference between '
      'the two parties is exactly the question of whether a major sin makes a man one of the '
      'latter, which Lesson 30 showed it does not.'))

b += B.heading('ثَلَاثَةُ أَصْنَافٍ فِي أَمْرِ الشَّفَاعَة',
               'Three Parties in the Matter of Intercession')
b += B.sharh(
    p('al-Fawzān closes Part 4 by dividing people three ways, and the pattern is the one from '
      'Lesson 30 — <strong>two excesses and a middle</strong>:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.89rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>الصِّنْفُ الأَوَّل</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<strong>they went to excess in AFFIRMING it</strong> — <em>and they are '
    '<strong>the Christians, the mushrikūn, the extremists of the ṣūfiyyah, and '
    'the grave-worshippers</strong>: <strong>in that they made the intercession of the one they '
    'venerate, with Allah, like the intercession known in this world before kings</strong> '
    '— <strong>so they sought it from other than Allah</strong>, as Allah mentioned that of '
    'the mushrikūn</em></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>الصِّنْفُ الثَّانِي</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<strong>they went to excess in DENYING it</strong> — <em>and they are '
    '<strong>the Muʿtazilah and the Khawārij</strong>: '
    '<strong>they denied the intercession of the Prophet &#65018; and of others for the people of '
    'the major sins</strong></em></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top;background:var(--brand-wash)">'
    '<strong>الصِّنْفُ الثَّالِث</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line);'
    'background:var(--brand-wash)"><strong>أَهْلُ السُّنَّةِ وَالجَمَاعَة</strong> — '
    '<em>they <strong>affirmed the intercession in accordance with what the Qurʾānic '
    'texts and the Prophetic aḥādīth came with — so they affirmed the '
    'intercession WITH ITS CONDITIONS.</strong></em></td></tr>'
    '</table></div>' +
    p('Stop on the first party, because it is where this part of the book joins the beginning of '
      'the track. <strong>Their error is named as the courtly analogy</strong> — '
      '<em>like the intercession known in this world before kings</em> — which is word for word '
      'the mechanism of Lesson 15, where the Qurʾān forbade %s by name, and the whole subject of '
      '<em>al-Qawāʿid al-Arbaʿ</em>.' % ar('ضَرْبَ الأَمْثَالِ لِلَّهِ')) +
    p('And now see what the derivation of the word has been doing all along. '
      '<strong>%s means the intercessor makes the petitioner\'s request <em>even</em> — so the '
      'petitioner must be the one petitioning.</strong> The grave-worshipper reverses it: he asks '
      '<em>the intercessor</em> instead of asking Allah, which is not intercession at all but '
      'worship directed elsewhere. <strong>The error is visible in the word\'s own '
      'etymology.</strong>' % ar('الشَّفَاعَة')) +
    p('And the middle position is characteristically the one that needs no text explained away. '
      '<strong>The first party kept the intercession and lost the tawḥīd; the second kept the '
      'tawḥīd by throwing out the aḥādīth.</strong> Ahl al-Sunnah affirm every text — '
      '<em>and the two conditions are what make that possible</em>, because an intercession that '
      'requires His permission and His pleasure takes nothing away from Him.'))

b += B.vocab([
    ('الاسْتِفْتَاح', 'al-istiftāḥ', 'seeking the opening',
     'And in it is an ennobling of the Prophet ط'),
    ('الشَّفَاعَة', 'al-shafāʿah', 'intercession',
     'Linguistically الوَسِيلَة; in usage: asking good for another'),
    ('الشَّفْع', 'al-shafʿ', 'the even number',
     'Opposite of الوَتْر — the intercessor joins his request to one already being made'),
    ('المَقَامُ المَحْمُود', 'al-maqām al-maḥmūd', 'the praised station',
     'The Greatest Intercession — that the judging BEGIN'),
    ('أَهْلُ الأَعْرَاف', 'ahl al-aʿrāf', 'the people of the Heights',
     'Those whose good and evil were equal — upon one statement'),
    ('المَشْفُوعُ لَه', 'al-mashfūʿ lah', 'the one interceded for',
     'The second condition is Allah’s being pleased with him'),
    ('القُبُورِيُّون', 'al-qubūriyyūn', 'the grave-worshippers',
     'Of the first party — who sought the intercession FROM other than Allah'),
])
b += B.mcq('ws-l40', [
    ('What is the state of the believers when the intercession for entry is needed?',
     ['They are still being reckoned with',
      'They are cleared and settled and standing at the gate — and the gate is still shut',
      'They are on the Ṣirāṭ', 'They are at the Ḥawḍ'], 1),
    ('What is %s derived from, and what does that imply?' % ar('الشَّفَاعَة'),
     ['From الشَّفَا, the brink; implying rescue from danger',
      'From الشَّفْع, the even — the intercessor makes the petitioner’s request even, so the '
      'petitioner must already be petitioning',
      'From الشِّفَاء, healing; implying relief',
      'From الشَّفَة, the lip; implying speech'], 1),
    ('Which three intercessions are particular to the Prophet ﷺ?',
     ['Those for sinners, for ranks, and for Abū Ṭālib',
      'The Greatest Intercession (al-Maqām al-Maḥmūd), that the people of the Garden enter it, '
      'and that his uncle Abū Ṭālib’s punishment be lightened',
      'Those for the seventy thousand, for ahl al-aʿrāf, and for ranks',
      'All eight are particular to him'], 1),
    ('What is the Greatest Intercession actually for?',
     ['That the sinners be forgiven',
      'That Allah judge between His servants — asked after the standing has grown long and every '
      'earlier prophet has declined',
      'That the Garden’s gates be opened',
      'That the Fire be emptied'], 1),
    ('What are the two conditions of a valid intercession?',
     ['The intercessor’s rank, and the sinner’s repentance',
      'Allah’s permission to the intercessor, and Allah’s being pleased with the one '
      'interceded for',
      'That it be in the Hereafter, and that it be asked of a prophet',
      'The intercessor’s nearness, and the number of intercessors'], 1),
    ('Why does al-Najm 53:26 name the angels?',
     ['Because they are the only intercessors',
      'Because they are the most exalted creatures anyone could appeal to — and their '
      'intercession avails nothing until He permits and is pleased',
      'Because they intercede for the disbelievers',
      'Because they are nearer than the prophets'], 1),
    ('How is the Muʿtazilī proof from al-Muddaththir 74:48 answered?',
     ['By declaring the āyah abrogated',
      'It came concerning the disbelievers — they are the ones the intercession does not benefit; '
      'the believers it benefits, with its conditions',
      'By saying intercession is only for ranks',
      'By reading شَافِعِين as the idols'], 1),
    ('What was the error of the first party — the Christians, mushrikūn, extremist ṣūfīs and '
     'grave-worshippers?',
     ['They denied intercession for the sinners',
      'They made the intercession of the one they venerate like the intercession known before '
      'kings — and so sought it FROM other than Allah',
      'They restricted it to the prophets',
      'They made it conditional on repentance'], 1),
])
b += B.tf('ws-l40-tf', [
    ('الشَّفَاعَةُ فِي عُصَاةِ المُوَحِّدِينَ خَاصَّةٌ بِالنَّبِيِّ ﷺ.',
     'The intercession for the disobedient monotheists is particular to the Prophet ﷺ.', False),
    ('لَا تَكُونُ الشَّفَاعَةُ إِلَّا بِإِذْنِ اللهِ وَرِضَاهُ عَنِ المَشْفُوعِ لَهُ.',
     'Intercession occurs only by Allah’s permission and His pleasure with the one '
     'interceded for.', True),
    ('شَفَاعَةُ النَّبِيِّ ﷺ لِعَمِّهِ أَبِي طَالِبٍ خَاصَّةٌ بِهِ.',
     'The Prophet’s ﷺ intercession for his uncle Abū Ṭālib is particular to him.', True),
    ('أَثْبَتَ أَهْلُ السُّنَّةِ الشَّفَاعَةَ بِلَا شُرُوطٍ.',
     'Ahl al-Sunnah affirmed the intercession without conditions.', False),
])
b += B.memorize(
    'إِلَّا مِنْ بَعْدِ أَنْ يَأْذَنَ اللَّهُ لِمَنْ يَشَاءُ وَيَرْضَى',
    'Both conditions in one clause, said of the angels — the most exalted creatures anyone could '
    'appeal to. Learn it and the whole business of seeking intercession from the dead collapses: '
    'what is granted twice over by Allah cannot be obtained by asking someone else for it.')
b += B.aiquiz('The intercessions in al-Aqidah al-Wasitiyyah: the believers standing at a shut '
              'gate, al-shafaah derived from al-shaf the even number and what that implies, the '
              'eight kinds with the three particular to the Prophet including al-Maqam al-Mahmud '
              'and Abu Talib, the two conditions with al-Baqarah 2:255 Yunus 10:3 al-Anbiya 21:28 '
              'and both gathered in al-Najm 53:26, the answer to the Mutazili proof from '
              'al-Muddaththir 74:48, and the three parties with the courtly analogy of the '
              'grave-worshippers')
b += B.further()
b += B.nav('was-l39-hawd-sirat-qantarah.html', 'The Ḥawḍ, the Ṣirāṭ and the Qanṭarah',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l40')

io.open(os.path.join(B.AQ, 'was-l40-shafaat.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'الشَّفَاعَاتُ وَشَرْطَاهَا',
    'The Intercessions, and Their Two Conditions',
    'Lesson 40 of al-ʿAqīdah al-Wāsiṭiyyah, closing Part 4: the '
    'believers cleared and standing at a shut gate; al-shafāʿah derived from the even '
    'number, and what that already settles; the eight kinds with the three that belong to the '
    'Prophet ط alone; the two conditions; and the three parties, whose first error is the '
    'courtly analogy of Lesson 15.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الأَرْبَعُون', '4',
           'الشَّفَاعَاتُ وَشَرْطَاهَا',
           'The Intercessions, and Their Two Conditions', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l40-shafaat.html')
