# -*- coding: utf-8 -*-
"""Wasitiyyah L37 -- Part 4: the Greater Resurrection, the proofs of the ba'th,
and the first two events of the Day -- the sun drawing near, and the Scales.
Sharh pp.129-133."""
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
    'الإِمَامُ <strong>الشَّوْكَانِيّ</strong> — quoted here on the Muʿtazilah’s reinterpretation '
    'of the Scales.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Name the three abodes and the two Resurrections.',
    'Give the five things by which the %s is established.' % ar('البَعْث'),
    'Reproduce the rational argument for the recompense that al-Fawzān draws from the Qurʾān.',
    'Say what is weighed, and what the heaviness is reckoned by.',
])

b += B.heading('٢ · القِيَامَةُ الكُبْرَى وَمَا يَجْرِي فِيهَا',
               'Second — The Greater Resurrection, and What Occurs in It')
b += B.matn(
    'إِلَى أَنْ تَقُومَ القِيَامَةُ الكُبْرَى، فَتُعَادَ الأَرْوَاحُ إِلَى '
    'الأَجْسَادِ، وَتَقُومَ القِيَامَةُ الَّتِي أَخْبَرَ اللهُ بِهَا فِي كِتَابِهِ '
    'وَعَلَى لِسَانِ رَسُولِهِ وَأَجْمَعَ عَلَيْهَا المُسْلِمُونَ؛ فَيَقُومُ النَّاسُ '
    'مِنْ قُبُورِهِمْ لِرَبِّ العَالَمِينَ حُفَاةً عُرَاةً غُرْلًا.')
b += B.sharh(
    p('al-Fawzān first sets the frame, and it is the map for everything that follows: '
      '<em><strong>the abodes are three</strong> — <strong>%s, %s, and %s</strong> — '
      '<strong>and each of these three abodes has rulings particular to it, and events that occur '
      'in it.</strong> And the Shaykh has spoken on what occurs in the abode of al-barzakh</em> '
      '(Lesson 36); <em>and here he begins to speak on what occurs in the Last Abode.</em>'
      % (ar('دَارُ الدُّنْيَا'), ar('دَارُ البَرْزَخ'), ar('الدَّارُ الآخِرَة'))) +
    p('And then a distinction the student will not have met: <em><strong>the Resurrection is of '
      'two kinds</strong></em> —') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.91rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>قِيَامَةٌ صُغْرَى</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<em><strong>and it is death.</strong> This Resurrection <strong>comes upon every human being '
    'individually</strong> — by the going out of his soul and the cutting off of his '
    'striving</em></td></tr>'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>قِيَامَةٌ كُبْرَى</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<em>this one <strong>comes upon all the people together and takes them in a single '
    'seizing</strong></em></td></tr>'
    '</table></div>' +
    p('<em>And it was named a <strong>%s</strong> — a <em>standing</em> — '
      '<strong>because of the people\'s standing up from their graves for the Lord of the '
      'worlds.</strong></em> The name is not about the end of the world; '
      '<strong>it is about what the dead do.</strong>' % ar('قِيَامَة')) +
    p('<em>And this is why he said <strong>%s</strong> — and that is '
      '<strong>when Isrāfīl blows in the Horn</strong>:</em>'
      % ar('فَتُعَادَ الأَرْوَاحُ إِلَى الأَجْسَادِ')))
b += B.ayah(
    'وَنُفِخَ فِي الصُّورِ فَإِذَا هُمْ مِنَ الْأَجْدَاثِ إِلَى رَبِّهِمْ يَنْسِلُونَ '
    'قَالُوا يَا وَيْلَنَا مَنْ بَعَثَنَا مِنْ مَرْقَدِنَا',
    '"And the Horn will be blown, and at once they are hastening from the graves to their Lord. '
    'They will say: woe to us — who has raised us from our resting-place?"',
    'Sūrat Yā-Sīn 36:51–52 · سُورَةُ يس')
b += B.ayah(
    'وَنُفِخَ فِي الصُّورِ فَصَعِقَ مَنْ فِي السَّمَاوَاتِ وَمَنْ فِي الْأَرْضِ إِلَّا مَنْ '
    'شَاءَ اللَّهُ ثُمَّ نُفِخَ فِيهِ أُخْرَى فَإِذَا هُمْ قِيَامٌ يَنْظُرُونَ',
    '"And the Horn will be blown, and all in the heavens and all in the earth will fall senseless '
    '— except whom Allah wills. Then it will be blown again, and at once they are standing, '
    'looking on."',
    'Sūrat al-Zumar 39:68 · سُورَةُ الزُّمَر')
b += B.sharh(
    p('<strong>%s</strong> is the plural of %s — <em>and it is <strong>that by which man and other '
      'possessors of souls live</strong>; <strong>and none knows its reality but '
      'Allah</strong></em>:' % (ar('الأَرْوَاح'), ar('رُوح'))))
b += B.ayah(
    'وَيَسْأَلُونَكَ عَنِ الرُّوحِ قُلِ الرُّوحُ مِنْ أَمْرِ رَبِّي وَمَا أُوتِيتُمْ مِنَ '
    'الْعِلْمِ إِلَّا قَلِيلًا',
    '"And they ask you about the soul. Say: the soul is of the affair of my Lord — and you have '
    'not been given of knowledge but a little."',
    'Sūrat al-Isrāʾ 17:85 · سُورَةُ الإِسْرَاء')
b += B.prose(
    'There is a lesson of method in that pairing. <strong>The creed requires you to believe that '
    'the souls are returned to the bodies — and tells you in the same breath that you do not know '
    'what a soul is.</strong> Which is the discipline of the whole book in a new place: '
    '<em>affirm what was reported, and do not pretend to the knowledge that would answer «how».</em>')

b += B.heading('أَدِلَّةُ البَعْث', 'The Proofs of the Resurrection')
b += B.sharh(
    p('The author\'s words <strong>%s</strong> are, al-Fawzān says, '
      '<em>an indication of <strong>the proofs of the resurrection</strong>, and that it is '
      'established by <strong>five things</strong>:</em>'
      % ar('وَتَقُومَ القِيَامَةُ الَّتِي أَخْبَرَ اللهُ بِهَا فِي كِتَابِهِ وَعَلَى لِسَانِ رَسُولِهِ وَأَجْمَعَ عَلَيْهَا المُسْلِمُونَ')) +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.95rem"><strong>the Book</strong> · '
    '<strong>the Sunnah</strong> · <strong>the consensus of the Muslims</strong> · '
    '<strong>reason</strong> · and <strong>the sound innate natures</strong></p></div>' +
    p('<em>For <strong>Allah informed of it in His Book, established the proof for it, and '
      'refuted those who deny the resurrection — in most of the sūrahs of the Qurʾān.</strong> '
      'And since our Prophet Muḥammad &#65018; is <strong>the seal of the prophets</strong>, '
      '<strong>he set out the details of the Hereafter with a clarity not found in many of the '
      'books of the prophets.</strong></em>') +
    p('Note what that last observation implies about the role of this part of the book. '
      '<strong>The detail is itself a mark of the finality of his prophethood</strong> — the last '
      'messenger describes the end most fully, because there will be no further messenger to add '
      'to it.'))
b += B.sharh(
    p('And then the rational argument, which al-Fawzān lays out as the Qurʾān does — '
      '<em>for Allah <strong>alerted the intellects to it in many places of the Qurʾān, where He '
      'reminded them</strong>:</em>') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.94rem">'
    '<p style="margin:0 0 .6rem"><em>— that <strong>it does not befit His wisdom and His '
    'praiseworthiness that He leave people aimless</strong>, or <strong>create them in vain, '
    'neither commanded nor forbidden, neither rewarded nor punished</strong>; and '
    '<strong>that the doer of good should be like the doer of evil</strong>, or '
    '<strong>that He make the Muslims like the criminals</strong>.</em></p>'
    '<p style="margin:0"><em>— <strong>For some of those who do good die before being '
    'recompensed for their good, and some of the criminals die before being recompensed for their '
    'crime. So there must necessarily be an abode in which each of the two is '
    'recompensed.</strong></em></p></div>' +
    p('That is a complete argument, and it is worth seeing that it does not start from scripture. '
      '<strong>It starts from an observation anyone can make</strong> — that the ledger of this '
      'world does not balance — and reasons from Allah\'s wisdom and justice to the necessity of '
      'another. <strong>The recompense is established by reason and occurs in the '
      'Sharīʿah.</strong>') +
    p('And the ruling: <em><strong>and the denier of the resurrection is a disbeliever</strong></em> '
      '— as He said:'))
b += B.ayah(
    'زَعَمَ الَّذِينَ كَفَرُوا أَنْ لَنْ يُبْعَثُوا قُلْ بَلَى وَرَبِّي لَتُبْعَثُنَّ ثُمَّ '
    'لَتُنَبَّؤُنَّ بِمَا عَمِلْتُمْ وَذَلِكَ عَلَى اللَّهِ يَسِيرٌ',
    '"Those who disbelieve claim that they will not be raised. Say: yes, by my Lord, you will '
    'surely be raised, and then you will surely be informed of what you did — and that is easy '
    'for Allah."',
    'Sūrat al-Taghābun 64:7 · سُورَةُ التَّغَابُن')

b += B.heading('حُفَاةً عُرَاةً غُرْلًا', '"Barefoot, Naked, Uncircumcised"')
b += B.sharh(
    p('<strong>%s</strong> — the plural of %s, <em>and he is <strong>the one upon whose foot there '
      'is neither sandal nor shoe</strong></em>. <strong>%s</strong> — the plural of %s, '
      '<em>and he is <strong>the one upon whom there is no clothing</strong></em>. '
      '<strong>%s</strong> — the plural of %s, <em>and he is <strong>the uncircumcised '
      'one</strong></em>.'
      % (ar('حُفَاةً'), ar('حَافٍ'), ar('عُرَاةً'), ar('عَارٍ'), ar('غُرْلًا'), ar('أَغْرَل'))) +
    p('<em>And <strong>these three descriptions are what they will be in when they stand up from '
      'their graves</strong>; and <strong>this is established in the authentic from the Prophet '
      '&#65018;.</strong></em>'))
b += B.hadith(
    'إِنَّكُمْ تُحْشَرُونَ إِلَى اللهِ يَوْمَ القِيَامَةِ حُفَاةً عُرَاةً غُرْلًا',
    '"You will be gathered to Allah on the Day of Rising barefoot, naked, uncircumcised."',
    'فِي الصَّحِيحَيْنِ — al-Bukhārī and Muslim, from ʿĀʾishah رضي الله عنها')
b += B.prose(
    'The third word is the one that makes the point. Barefoot and naked a man can imagine; '
    '<strong>uncircumcised returns the body to the state it was in on the day it was born</strong> '
    '— undoing even the one mark a person did not choose and could not remove. '
    '<strong>Nothing acquired comes with you.</strong>')

b += B.heading('٣ · دُنُوُّ الشَّمْسِ · وَنَصْبُ المَوَازِين',
               'Third — The Sun Draws Near, and the Scales Are Set Up')
b += B.matn(
    'وَتَدْنُو مِنْهُمُ الشَّمْسُ، وَيُلْجِمُهُمُ العَرَقُ. وَتُنْصَبُ المَوَازِينُ، '
    'فَتُوزَنُ بِهَا أَعْمَالُ العِبَادِ: ﴿فَمَنْ ثَقُلَتْ مَوَازِينُهُ فَأُولَئِكَ هُمُ '
    'الْمُفْلِحُونَ ۝ وَمَنْ خَفَّتْ مَوَازِينُهُ فَأُولَئِكَ الَّذِينَ خَسِرُوا '
    'أَنْفُسَهُمْ فِي جَهَنَّمَ خَالِدُونَ﴾.')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>it comes close to their heads</strong></em>; as '
      '<strong>Muslim</strong> reported from <strong>المِقْدَادِ</strong> رضي الله عنه, who said: '
      '<em>I heard the Messenger of Allah &#65018; say: <strong>«when it is the Day of Rising the '
      'sun will be brought near to the servants, until it is at the measure of a mile or '
      'two».</strong></em>' % ar('وَتَدْنُو مِنْهُمُ الشَّمْسُ')) +
    p('<strong>%s</strong> — <em>that is: <strong>it reaches their mouths, so that it becomes like '
      'a bridle, preventing them from speech</strong>; and that is the result of the sun\'s '
      'drawing near to them.</em> And the qualification: <em>and that is '
      '<strong>with respect to most of the creation</strong>; and '
      '<strong>there are excepted from it the prophets, and whomever Allah wills.</strong></em>'
      % ar('وَيُلْجِمُهُمُ العَرَقُ')))
b += B.ayah(
    'فَمَنْ ثَقُلَتْ مَوَازِينُهُ فَأُولَئِكَ هُمُ الْمُفْلِحُونَ وَمَنْ خَفَّتْ '
    'مَوَازِينُهُ فَأُولَئِكَ الَّذِينَ خَسِرُوا أَنْفُسَهُمْ فِي جَهَنَّمَ خَالِدُونَ',
    '"So whoever\'s scales are heavy — those are the successful. And whoever\'s scales are light — '
    'those are the ones who have lost themselves; in Hell they abide."',
    'Sūrat al-Muʾminūn 23:102–103 · سُورَةُ المُؤْمِنُون')
b += B.sharh(
    p('<strong>%s</strong> is the plural of %s — <em>and it is <strong>that by which the good '
      'deeds and the evil deeds are weighed</strong>; <strong>and it is a real scale, having a '
      'tongue and two pans</strong>. And <strong>it is of the matters of the Hereafter: we believe '
      'in it as it came, and we do not enquire into its manner except in the light of what has '
      'come in the texts.</strong></em>'
      % (ar('المَوَازِين'), ar('مِيزَان'))) +
    p('<em>And <strong>the wisdom in the weighing of the deeds is the making apparent of their '
      'measures, so that the recompense may be according to them.</strong></em>') +
    p('<strong>%s</strong> — <em>that is: <strong>his good deeds outweighed his evil deeds</strong></em> '
      '— <strong>%s</strong>, <em>the winners, and those saved from the Fire, deserving of '
      'entering the Garden</em>. <strong>%s</strong> — <em>that is: '
      '<strong>his evil deeds outweighed his good deeds</strong></em> — '
      '<strong>%s</strong>, <em>they were ruined and came to the Fire</em>.'
      % (ar('فَمَنْ ثَقُلَتْ مَوَازِينُهُ'), ar('فَأُولَئِكَ هُمُ الْمُفْلِحُونَ'),
         ar('وَمَنْ خَفَّتْ مَوَازِينُهُ'), ar('خَسِرُوا أَنْفُسَهُمْ'))) +
    p('And then a point that gathers the apparently conflicting texts, which is the most useful '
      'thing in the section: <em>the totality of the texts has conveyed that '
      '<strong>the doer is weighed, and the deed is weighed, and the pages are weighed — '
      'and there is no conflict between them: all of it is weighed. But '
      '<span style="white-space:nowrap">the reckoning</span> of heaviness and lightness is '
      '<strong>by the deed itself</strong>, not by the person of the doer, nor by the '
      'page.</strong> وَاللهُ أَعْلَم.</em>') +
    p('Three sets of texts, three things weighed, and <strong>one of them is what the verdict '
      'turns on.</strong> That is the same move as <em>al-ḥaqqu lā yatanāqaḍ</em> in Lesson 33: '
      'the texts were never in competition, and the resolution was to find what each was '
      'reporting.'))
b += B.heading('تَأْوِيلُ المُعْتَزِلَةِ لِلْمِيزَان', 'The Muʿtazilah’s Reinterpretation of the Scales')
b += B.sharh(
    p('<em>And <strong>the Muʿtazilah reinterpreted the texts concerning that</strong>, claiming '
      '<strong>that what is meant by the weighing and the Scales is <em>justice</em></strong> — '
      'and <strong>that there is no real weighing and no real scale.</strong> '
      '<strong>And this is a corrupt reinterpretation, contradicting the texts and the consensus '
      'of the predecessors of the Ummah and its imāms.</strong></em>') +
    p('And al-Fawzān answers with al-Shawkānī, whose words are worth having in full because they '
      'name the method rather than only the error:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.94rem"><em>— <strong>and the utmost of what they clung to '
    'is mere rational improbabilities</strong>, and <strong>there is no proof in that against '
    'anyone.</strong> <strong>So if their intellects did not accept this, then it was accepted by '
    'the intellects of a people stronger than their intellects</strong> — '
    '<strong>of the Ṣaḥābah, the Tābiʿūn and those who followed '
    'them</strong> — <strong>until the innovations came like a dark night, and each said '
    'whatever he wished, and they left the Sharīʿah behind their backs.</strong></em></p></div>' +
    p('<strong>%s</strong> — <em>rational improbabilities</em>. That is the name for the whole '
      'class of argument, and the student has met it four times now: the sky cannot carry Him, so '
      'reinterpret; mercy cannot speak, so reinterpret; a foot cannot be placed, so reinterpret; '
      'a deed cannot be weighed, so reinterpret. <strong>In each case the premise is that what '
      'the speaker cannot picture cannot have happened.</strong>'
      % ar('الاسْتِبْعَادَاتُ العَقْلِيَّة')) +
    p('And al-Shawkānī\'s reply is not that reason is worthless, but that '
      '<strong>this particular reason is not strong enough to overturn that '
      'testimony</strong> — the Companions found no difficulty here, and they were not the '
      'weaker minds. <em>And the matters of the Hereafter are not of what the intellects '
      'grasp. وَاللهُ أَعْلَم.</em>'))

b += B.vocab([
    ('دَارُ البَرْزَخ', 'dār al-barzakh', 'the intervening abode',
     'The second of the three abodes, each with its own rulings and events'),
    ('قِيَامَةٌ صُغْرَى', 'qiyāmah ṣughrā', 'the lesser Resurrection',
     'Death — which comes upon each person individually'),
    ('قِيَامَةٌ كُبْرَى', 'qiyāmah kubrā', 'the Greater Resurrection',
     'Which takes all people in a single seizing'),
    ('الصُّور', 'al-ṣūr', 'the Horn',
     'Blown by Isrāfīl — and the souls return to the bodies'),
    ('غُرْلًا', 'ghurlan', 'uncircumcised',
     'Plural of أَغْرَل — the body returned to the state it was born in'),
    ('يُلْجِمُهُمُ العَرَق', 'yuljimuhum al-ʿaraq', 'the sweat bridles them',
     'Reaching the mouth like a bridle, preventing speech'),
    ('المِيزَان', 'al-mīzān', 'the Scale',
     'A real scale with a tongue and two pans — believed in as it came'),
    ('الاسْتِبْعَادَاتُ العَقْلِيَّة', 'al-istibʿādāt al-ʿaqliyyah',
     'rational improbabilities',
     'al-Shawkānī’s name for the whole class — “no proof against '
     'anyone”'),
])
b += B.mcq('ws-l37', [
    ('What are the three abodes?',
     ['The grave, the Garden and the Fire',
      'The abode of this world, the abode of al-barzakh, and the Last Abode',
      'The heavens, the earth and the Throne',
      'Childhood, maturity and old age'], 1),
    ('What is the %s?' % ar('قِيَامَةٌ صُغْرَى'),
     ['The resurrection of a single nation',
      'Death — which comes upon every human being individually, by the going out of his soul',
      'The first blowing of the Horn', 'The questioning in the grave'], 1),
    ('Why is the Day called a %s?' % ar('قِيَامَة'),
     ['Because the world is brought to an end',
      'Because of the people’s standing up from their graves for the Lord of the worlds',
      'Because the Scales are set up', 'Because the Horn is blown'], 1),
    ('By what five things is the resurrection established?',
     ['The Qurʾān, the Sunnah, analogy, consensus and necessity',
      'The Book, the Sunnah, the consensus of the Muslims, reason, and the sound innate natures',
      'The Book, the Sunnah and the consensus only',
      'Reason and transmission only'], 1),
    ('What is the rational argument for the recompense?',
     ['That Allah has promised it and does not break a promise',
      'That it does not befit His wisdom to leave people aimless or make the good-doer like the '
      'evil-doer — and some of each die before being recompensed, so there must be an abode where '
      'each is',
      'That the soul is immortal',
      'That the prophets all reported it'], 1),
    ('What does %s add beyond "barefoot and naked"?' % ar('غُرْلًا'),
     ['That they are without provisions',
      'It returns the body to the state it was born in — undoing even the one mark a person did '
      'not choose and could not remove',
      'That they are without family',
      'That they are without shade'], 1),
    ('What is weighed, and what is the heaviness reckoned by?',
     ['The deeds only, reckoned by their number',
      'The doer, the deed and the pages are all weighed — but the reckoning of heaviness is by '
      'the deed itself, not the person of the doer nor the page',
      'The pages only, reckoned by their length',
      'The doer only, reckoned by his sincerity'], 1),
    ('What was al-Shawkānī’s reply to the Muʿtazilah?',
     ['That the texts are mutawātir and so cannot be reinterpreted',
      'That the utmost they clung to is mere rational improbabilities, which are no proof against '
      'anyone — and what their intellects would not accept was accepted by stronger intellects, '
      'the Ṣaḥābah and those after them',
      'That the Scales are mentioned in the Torah too',
      'That justice requires a real scale'], 1),
])
b += B.tf('ws-l37-tf', [
    ('القِيَامَةُ الكُبْرَى تَأْخُذُ النَّاسَ جَمِيعًا أَخْذَةً وَاحِدَةً.',
     'The Greater Resurrection takes all people in a single seizing.', True),
    ('يُعْلَمُ حَقِيقَةُ الرُّوحِ بِالعَقْلِ.',
     'The reality of the soul is known by the intellect.', False),
    ('المِيزَانُ مِيزَانٌ حَقِيقِيٌّ لَهُ لِسَانٌ وَكَفَّتَانِ.',
     'The Scale is a real scale with a tongue and two pans.', True),
    ('مُنْكِرُ البَعْثِ كَافِرٌ.', 'The denier of the resurrection is a disbeliever.', True),
])
b += B.memorize(
    'فَمَنْ ثَقُلَتْ مَوَازِينُهُ فَأُولَئِكَ هُمُ الْمُفْلِحُونَ',
    'Learn it with al-Fawzān\'s clause: the doer is weighed, and the pages, and the deeds — but '
    'the heaviness is reckoned <em>by the deed</em>. Nothing about who you were will tip the pan; '
    'only what you actually did.')
b += B.aiquiz('The Greater Resurrection in al-Aqidah al-Wasitiyyah: the three abodes and the two '
              'Resurrections, the blowing of the Horn with Yasin 36:51 and al-Zumar 39:68, that '
              'the reality of the soul is known only to Allah, the five things establishing the '
              'bath including reason and the sound fitrah with the argument that the ledger of '
              'this world does not balance, hufatan uratan ghurlan, the sun drawing near, and '
              'what is weighed versus what the heaviness is reckoned by')
b += B.further()
b += B.nav('was-l36-fitnat-al-qabr.html', 'The Examination of the Grave',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l37')

io.open(os.path.join(B.AQ, 'was-l37-qiyamah-kubra.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'القِيَامَةُ الكُبْرَى وَنَصْبُ المَوَازِين',
    'The Greater Resurrection, and the Setting Up of the Scales',
    'Lesson 37 of al-ʿAqīdah al-Wāsiṭiyyah: the three abodes and '
    'the two Resurrections, the five things by which the resurrection is established — '
    'including the argument that the ledger of this world does not balance — and what is '
    'weighed on the Day against what the heaviness is reckoned by.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ السَّابِعُ وَالثَّلَاثُون', '4',
           'القِيَامَةُ الكُبْرَى وَنَصْبُ المَوَازِين',
           'The Greater Resurrection, and the Setting Up of the Scales', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l37-qiyamah-kubra.html')
