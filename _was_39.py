# -*- coding: utf-8 -*-
"""Wasitiyyah L39 -- Part 4: the Hawd of the Prophet, the Sirat over Hellfire,
and the Qantarah between the Garden and the Fire. Sharh pp.136-139."""
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
    'الإِمَامُ <strong>ابْنُ القَيِّم</strong> — quoted here on how many Companions narrated the '
    'aḥādīth of the Ḥawḍ.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Say how many Companions narrated the aḥādīth of the %s, and on whose authority.'
    % ar('الحَوْض'),
    'Define %s linguistically and in the Sharīʿah, and say where it is set.' % ar('الصِّرَاط'),
    'Explain al-Fawzān’s link between the two ṣirāṭs — the moral and the physical.',
    'Say what happens at the %s and why it is needed before the Garden.' % ar('القَنْطَرَة'),
])

b += B.heading('٦ · حَوْضُ النَّبِيِّ ﷺ', 'Sixth — The Ḥawḍ of the Prophet ﷺ')
b += B.matn(
    'وَفِي عَرَصَاتِ القِيَامَةِ الحَوْضُ المَوْرُودُ لِلنَّبِيِّ ﷺ: مَاؤُهُ أَشَدُّ '
    'بَيَاضًا مِنَ اللَّبَنِ، وَأَحْلَى مِنَ العَسَلِ، آنِيَتُهُ كَنُجُومِ السَّمَاءِ، '
    'طُولُهُ شَهْرٌ وَعَرْضُهُ شَهْرٌ، مَنْ شَرِبَ مِنْهُ شَرْبَةً لَا يَظْمَأُ بَعْدَهَا '
    'أَبَدًا.')
b += B.sharh(
    p('al-Fawzān first establishes how firmly this is transmitted, and quotes '
      '<strong>الإِمَامُ ابْنُ القَيِّم</strong> for it: <em>and <strong>the aḥādīth of the Ḥawḍ '
      'were narrated by forty Companions</strong>, <strong>and many of them — or most of them — '
      'are in the authentic collections.</strong></em>') +
    p('<strong>Forty Companions.</strong> That is worth pausing on in a chapter where the '
      'Muʿtazilah will shortly deny the thing: this is not a doctrine resting on one chain.') +
    p('<strong>%s</strong> — <em>in the language is <strong>a gathering-place of water</strong>. '
      'And <strong>Ahl al-Sunnah wa-l-Jamāʿah have reached consensus on affirming the '
      'Ḥawḍ</strong>; <strong>the Muʿtazilah opposed that and did not affirm it, and '
      'reinterpreted the texts that came concerning it and turned them away from their apparent '
      'sense.</strong></em>' % ar('الحَوْض')) +
    p('And the location, which the author gives and which ties back to Lesson 35: '
      '<strong>%s</strong> — the standing-places of the Reckoning, '
      '<em>the wide places in which there is no building</em>. '
      '<strong>The Ḥawḍ is reached before the Garden, in the heat of the waiting.</strong>'
      % ar('فِي عَرَصَاتِ القِيَامَةِ')))
b += B.hadith(
    'حَوْضِي مَسِيرَةُ شَهْرٍ، مَاؤُهُ أَبْيَضُ مِنَ اللَّبَنِ، وَرِيحُهُ أَطْيَبُ مِنَ '
    'المِسْكِ، وَكِيزَانُهُ كَنُجُومِ السَّمَاءِ، مَنْ شَرِبَ مِنْهُ لَا يَظْمَأُ '
    'أَبَدًا',
    '"My Ḥawḍ is a month\'s journey. Its water is whiter than milk, its scent sweeter than musk, '
    'and its drinking-vessels are like the stars of the sky. Whoever drinks from it will never '
    'thirst again."',
    'مُتَّفَقٌ عَلَيْهِ — al-Bukhārī and Muslim, from ʿAbdullāh ibn ʿAmr رضي الله عنهما')
b += B.prose(
    'Set the description against the scene Lesson 37 described — the sun a mile overhead, the '
    'sweat rising to the mouth like a bridle — and the mercy of the detail becomes plain. '
    '<strong>The one promise made about the water is that the thirst does not come '
    'back.</strong> And the vessels are <em>as many as the stars</em>: nobody is waiting for a cup.')

b += B.heading('٧ · الصِّرَاطُ المَنْصُوبُ عَلَى مَتْنِ جَهَنَّم',
               'Seventh — The Ṣirāṭ, Set Over the Back of Hellfire')
b += B.matn(
    'وَالصِّرَاطُ مَنْصُوبٌ عَلَى مَتْنِ جَهَنَّمَ، وَهُوَ الجِسْرُ الَّذِي بَيْنَ '
    'الجَنَّةِ وَالنَّارِ. يَمُرُّ النَّاسُ عَلَيْهِ عَلَى قَدْرِ أَعْمَالِهِمْ: '
    'فَمِنْهُمْ مَنْ يَمُرُّ كَلَمْحِ البَصَرِ، وَمِنْهُمْ مَنْ يَمُرُّ كَالبَرْقِ، '
    'وَمِنْهُمْ مَنْ يَمُرُّ كَالرِّيحِ، وَمِنْهُمْ مَنْ يَمُرُّ كَالفَرَسِ الجَوَادِ، '
    'وَمِنْهُمْ مَنْ يَمُرُّ كَرِكَابِ الإِبِلِ، وَمِنْهُمْ مَنْ يَعْدُو عَدْوًا، '
    'وَمِنْهُمْ مَنْ يَمْشِي مَشْيًا، وَمِنْهُمْ مَنْ يَزْحَفُ زَحْفًا، وَمِنْهُمْ مَنْ '
    'يُخْطَفُ وَيُلْقَى فِي جَهَنَّمَ؛ فَإِنَّ الجِسْرَ عَلَيْهِ كَلَالِيبُ تَخْطَفُ '
    'النَّاسَ بِأَعْمَالِهِمْ.')
b += B.sharh(
    p('<strong>%s</strong> — <em>in the language is <strong>the clear road</strong>. And in the '
      'Sharīʿah it is what the Shaykh explained: <strong>the bridge which is between the Garden '
      'and the Fire</strong>.</em> And its place: <strong>%s</strong> — <em>that is, '
      '<strong>upon the back of the Fire</strong></em>.'
      % (ar('الصِّرَاط'), ar('عَلَى مَتْنِ جَهَنَّمَ'))) +
    p('And the timing, which the author does not state but al-Fawzān supplies: '
      '<em>the time of passing over it is <strong>after the people\'s departure from the standing, '
      'the gathering and the Reckoning</strong>. For <strong>upon the Ṣirāṭ the believers are '
      'saved from the Fire into the Garden, and the people of the Fire fall from it into '
      'it</strong>, as is established in the aḥādīth.</em>') +
    p('<strong>%s</strong> — <em>that is: <strong>they are, in the speed of the passage and its '
      'slowness, according to their faith and the righteous deeds they sent ahead in this '
      'world.</strong></em>' % ar('يَمُرُّ النَّاسُ عَلَيْهِ عَلَى قَدْرِ أَعْمَالِهِمْ')) +
    p('And then al-Fawzān states the principle that organises the whole list, which is the finest '
      'thing in the section:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.95rem"><em>— <strong>So according to a person’s '
    'uprightness upon the religion of Islam, and his firmness upon it, will be his firmness and '
    'his passage upon the Ṣirāṭ.</strong> <strong>Whoever stood firm upon the '
    'MORAL ṣirāṭ — and it is Islam — stands firm upon the PHYSICAL '
    'ṣirāṭ set over the back of Hellfire; and whoever slipped from the moral '
    'ṣirāṭ slips from the physical one.</strong></em></p></div>' +
    p('<strong>Two ṣirāṭs, and the second is the shape of the first.</strong> That is why the '
      'list of nine speeds is not arbitrary and not a curiosity: '
      '<em>it is the measure of how steadily each man walked the straight path when nobody was '
      'making him.</em> And it gives the <em>ṣirāṭ mustaqīm</em> of al-Fātiḥah — asked for '
      'seventeen times a day — a second and very literal meaning.'))
b += B.sharh(
    p('The vocabulary of the matn, as al-Fawzān glosses it: <strong>%s</strong> — '
      '<em>that is: <strong>he runs at a run</strong></em>. <strong>%s</strong> — <em>that is: '
      '<strong>he moves along on his backside instead of his legs</strong></em>.'
      % (ar('يَعْدُو عَدْوًا'), ar('يَزْحَفُ زَحْفًا'))) +
    p('<strong>%s</strong> — the plural of %s — <em>and they are '
      '<strong>an iron hook with a bent head</strong></em>. <strong>%s</strong> — '
      '<em>from %s, which is <strong>the taking of a thing swiftly</strong></em>.'
      % (ar('كَلَالِيب'), ar('كَلُّوب'), ar('تَخْطَفُ'), ar('الخَطْف'))) +
    p('And the last phrase is where the two ṣirāṭs meet again, and it is exact: '
      '<strong>%s</strong> — <em>that is: <strong>by reason of their evil deeds</strong>. '
      '<strong>So the hooks\' snatching of them on the ṣirāṭ of Hellfire will be according to the '
      'snatching of them away from the straight path, in this world, by the doubts and the '
      'desires.</strong></em>' % ar('بِأَعْمَالِهِمْ')) +
    p('<strong>%s and %s</strong> — doubts and desires. Those are the two things that pull a man '
      'off the road here, and the hooks are their image there. '
      '<strong>What snatched at you then, snatches at you then.</strong>'
      % (ar('الشُّبُهَات'), ar('الشَّهَوَات'))))
b += B.heading('مُخَالَفَةُ المُعْتَزِلَةِ فِي الصِّرَاط',
               'The Muʿtazilah’s Opposition over the Ṣirāṭ')
b += B.sharh(
    p('<em>And <strong>Ahl al-Sunnah wa-l-Jamāʿah believe in the Ṣirāṭ set over the back of '
      'Hellfire, and the people\'s passing over it, according to what the authentic aḥādīth from '
      'the Prophet &#65018; came with.</strong> And <strong>القَاضِي عَبْدُ الجَبَّارِ '
      'المُعْتَزِلِيّ</strong> opposed that, and many of his followers, and they said: '
      '<strong>what is meant by the ṣirāṭ mentioned is the road of the Garden</strong>, pointed to '
      'in His saying %s — and <strong>the road of the Fire</strong>, pointed to in His saying '
      '%s.</em>' % (ar('سَيَهْدِيهِمْ وَيُصْلِحُ بَالَهُمْ'),
                    ar('فَاهْدُوهُمْ إِلَى صِرَاطِ الْجَحِيمِ'))))
b += B.ayah(
    'سَيَهْدِيهِمْ وَيُصْلِحُ بَالَهُمْ',
    '"He will guide them and set right their state."',
    'Sūrat Muḥammad 47:5 · سُورَةُ مُحَمَّد')
b += B.ayah(
    'فَاهْدُوهُمْ إِلَى صِرَاطِ الْجَحِيمِ',
    '"Then lead them to the path of the Blaze."',
    'Sūrat al-Ṣāffāt 37:23 · سُورَةُ الصَّافَّات')
b += B.sharh(
    p('<em>And <strong>this is a false statement, and a rejection of the authentic texts without '
      'any evidence.</strong> <strong>And what is obligatory is to carry the texts upon their '
      'apparent meaning.</strong></em>') +
    p('Notice the form of the error, because it is a new variety. The muʿaṭṭilah of Parts 1 and 2 '
      'reinterpreted a word; <strong>here the move is to replace an event with a metaphor by '
      'citing two āyāt that are about something else.</strong> Neither āyah denies a bridge — '
      'they speak of guidance and of being driven — and so neither is evidence against the '
      'aḥādīth. <strong>Producing a text that is merely compatible with your view is not '
      'producing a text against the other.</strong>'))

b += B.heading('٨ · القَنْطَرَةُ بَيْنَ الجَنَّةِ وَالنَّار',
               'Eighth — The Qanṭarah between the Garden and the Fire')
b += B.matn(
    'فَمَنْ مَرَّ عَلَى الصِّرَاطِ دَخَلَ الجَنَّةَ؛ فَإِذَا عَبَرُوا عَلَيْهِ وَقَفُوا '
    'عَلَى قَنْطَرَةٍ بَيْنَ الجَنَّةِ وَالنَّارِ، فَيُقْتَصُّ لِبَعْضِهِمْ مِنْ '
    'بَعْضٍ؛ فَإِذَا هُذِّبُوا وَنُقُّوا أُذِنَ لَهُمْ فِي دُخُولِ الجَنَّةِ.')
b += B.sharh(
    p('<strong>%s</strong> — <em>and the one who passes over the Ṣirāṭ has succeeded</em>, as '
      'Allah said:' % ar('فَمَنْ مَرَّ عَلَى الصِّرَاطِ دَخَلَ الجَنَّةَ')))
b += B.ayah(
    'فَمَنْ زُحْزِحَ عَنِ النَّارِ وَأُدْخِلَ الْجَنَّةَ فَقَدْ فَازَ',
    '"So whoever is drawn away from the Fire and admitted to the Garden has indeed succeeded."',
    'Sūrat Āl ʿImrān 3:185 · سُورَةُ آلُ عِمْرَان')
b += B.ayah(
    'فَرِيقٌ فِي الْجَنَّةِ وَفَرِيقٌ فِي السَّعِيرِ',
    '"A party in the Garden, and a party in the Blaze."',
    'Sūrat al-Shūrā 42:7 · سُورَةُ الشُّورَى')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>they crossed the Ṣirāṭ and were saved from '
      'falling into the Fire</strong></em> — <strong>%s</strong>: '
      '<em>and it is <strong>the bridge, and what is raised up of a building</strong></em>.'
      % (ar('فَإِذَا عَبَرُوا عَلَيْهِ'), ar('وَقَفُوا عَلَى قَنْطَرَةٍ'))) +
    p('And on what exactly it is, al-Fawzān reports two views without choosing: '
      '<em>and <strong>this qanṭarah, it has been said, is the end of the Ṣirāṭ on the side '
      'nearest the Garden; and it has been said it is another ṣirāṭ particular to the '
      'believers.</strong></em>') +
    p('<strong>%s</strong> — <em>that is: <strong>the retaliation is carried out among them in the '
      'matters of wrongdoing: the wronged one is given his right from the one who wronged '
      'him.</strong></em>' % ar('فَيُقْتَصُّ لِبَعْضِهِمْ مِنْ بَعْضٍ')) +
    p('<strong>%s</strong> — <em>that is: <strong>they were freed from the liabilities and the '
      'claims</strong></em> — <strong>%s</strong>.'
      % (ar('فَإِذَا هُذِّبُوا وَنُقُّوا'), ar('أُذِنَ لَهُمْ فِي دُخُولِ الجَنَّةِ'))))
b += B.sharh(
    p('Now the reason the Qanṭarah is needed at all, which al-Fawzān states and which is the '
      'point of the section: <em>so that <strong>they enter the Garden while they are in the most '
      'complete state, having been cleared of the wrongs.</strong></em>') +
    p('<strong>These are people who have already crossed.</strong> The Fire is behind them and the '
      'Garden is in front, and they are halted — not to be judged again, but to '
      '<em>settle with each other</em>. Everything owed between them is paid before anyone goes '
      'in. <strong>Nothing unresolved is carried through the gate.</strong>') +
    p('<em>And <strong>what was in the hearts of some of them against others, of rancour, has '
      'gone</strong></em> — as Allah said:'))
b += B.ayah(
    'وَنَزَعْنَا مَا فِي صُدُورِهِمْ مِنْ غِلٍّ إِخْوَانًا عَلَى سُرُرٍ مُتَقَابِلِينَ',
    '"And We shall remove whatever was in their breasts of rancour — brothers, upon couches, '
    'facing one another."',
    'Sūrat al-Ḥijr 15:47 · سُورَةُ الحِجْر')
b += B.prose(
    'Read the āyah as the completion of the Qanṭarah and it stops being a decorative promise. '
    '<strong>The retaliation settles what was owed; the removing of the rancour settles what was '
    '<em>felt</em>.</strong> And the word the āyah then uses for them is '
    '<strong>%s — brothers</strong>, sitting <em>facing one another</em>: the posture of people '
    'with nothing left between them. <strong>Paid in full, and then able to look each other in '
    'the eye.</strong>' % ar('إِخْوَانًا'))

b += B.vocab([
    ('الحَوْض', 'al-ḥawḍ', 'the Basin',
     'In the language: a gathering-place of water — narrated by forty Companions'),
    ('كِيزَان', 'kīzān', 'drinking-vessels',
     'As many as the stars of the sky — nobody waits for a cup'),
    ('الصِّرَاط', 'al-ṣirāṭ', 'the Path',
     'In the language: the clear road; in the Sharīʿah: the bridge between the Garden '
     'and the Fire'),
    ('مَتْنُ جَهَنَّم', 'matn jahannam', 'the back of Hellfire',
     'Where the Ṣirāṭ is set'),
    ('كَلَالِيب', 'kalālīb', 'hooks',
     'Plural of كَلُّوب — an iron hook with a bent head'),
    ('الخَطْف', 'al-khaṭf', 'snatching',
     'The taking of a thing swiftly — as the doubts and desires snatch here'),
    ('القَنْطَرَة', 'al-qanṭarah', 'the Causeway',
     'The bridge, or what is raised up of a building — where the retaliation is settled'),
    ('الغِلّ', 'al-ghill', 'rancour',
     'Removed from the breasts, so they sit as brothers facing one another'),
])
b += B.mcq('ws-l39', [
    ('How many Companions narrated the aḥādīth of the Ḥawḍ, and on whose authority is that said?',
     ['Ten, per al-Bukhārī', 'Forty, per Ibn al-Qayyim — most of them in the authentic collections',
      'Seventy, per Ibn Kathīr', 'Four, per Muslim'], 1),
    ('Where is the Ḥawḍ reached?',
     ['After entering the Garden',
      'In the ʿaraṣāt of the Resurrection — before the Garden, in the heat of the waiting',
      'At the gate of the Garden', 'On the Ṣirāṭ itself'], 1),
    ('What is %s in the language and in the Sharīʿah?' % ar('الصِّرَاط'),
     ['The straight way; and the religion of Islam',
      'The clear road; and the bridge between the Garden and the Fire, set over the back of '
      'Hellfire',
      'A narrow passage; and the gate of the Garden',
      'A journey; and the gathering'], 1),
    ('What is al-Fawzān’s link between the two ṣirāṭs?',
     ['That the physical one is a metaphor for the moral one',
      'Whoever stood firm on the moral ṣirāṭ — Islam — stands firm on the physical one; and '
      'whoever slipped from the moral one slips from the physical',
      'That only prophets cross the physical one',
      'That the moral one is in this world and has no counterpart'], 1),
    ('What do the hooks correspond to?',
     ['The sins of the limbs',
      'The doubts and the desires which snatched people away from the straight path in this world',
      'The questions of the two angels', 'The deeds weighed in the Scales'], 1),
    ('What was al-Qāḍī ʿAbd al-Jabbār’s claim, and what is wrong with his two āyāt?',
     ['That the Ṣirāṭ is only for the disbelievers; and his āyāt are weak',
      'That the ṣirāṭ means the road of the Garden and the road of the Fire; but neither āyah '
      'denies a bridge — a text merely compatible with your view is not a text against the other',
      'That the Ṣirāṭ is in this world; and his āyāt are abrogated',
      'That the aḥādīth are not authentic; and his āyāt are misquoted'], 1),
    ('What happens at the Qanṭarah?',
     ['The deeds are weighed a second time',
      'Retaliation is carried out among them in the matters of wrongdoing — the wronged is given '
      'his right from the one who wronged him',
      'The records are handed out', 'The Prophet ﷺ intercedes for them'], 1),
    ('Why is that needed before the Garden?',
     ['To delay their entry until the Garden is prepared',
      'So that they enter while in the most complete state, cleared of the wrongs — nothing '
      'unresolved is carried through the gate',
      'To distinguish the ranks of the believers',
      'Because the gate admits only one at a time'], 1),
])
b += B.tf('ws-l39-tf', [
    ('رَوَى أَحَادِيثَ الحَوْضِ أَرْبَعُونَ صَحَابِيًّا.',
     'Forty Companions narrated the aḥādīth of the Ḥawḍ.', True),
    ('الصِّرَاطُ مَنْصُوبٌ عَلَى مَتْنِ جَهَنَّمَ.',
     'The Ṣirāṭ is set over the back of Hellfire.', True),
    ('المُرُورُ عَلَى الصِّرَاطِ سَوَاءٌ لِجَمِيعِ النَّاسِ.',
     'The passage over the Ṣirāṭ is the same for all people.', False),
    ('يَدْخُلُ المُؤْمِنُونَ الجَنَّةَ قَبْلَ أَنْ يُقْتَصَّ لِبَعْضِهِمْ مِنْ بَعْضٍ.',
     'The believers enter the Garden before the retaliation among them is settled.', False),
])
b += B.memorize(
    'يَمُرُّ النَّاسُ عَلَيْهِ عَلَى قَدْرِ أَعْمَالِهِمْ',
    'Learn it with al-Fawzān\'s principle, because it turns the whole list of nine speeds into a '
    'single question about today: <em>whoever stood firm on the moral ṣirāṭ stands firm on the '
    'physical one.</em> The <span dir="rtl" lang="ar">صِرَاط مُسْتَقِيم</span> you ask for '
    'seventeen times a day is the same road, met twice.')
b += B.aiquiz('The Hawd, the Sirat and the Qantarah in al-Aqidah al-Wasitiyyah: the forty '
              'Companions who narrated the Hawd per Ibn al-Qayyim and its place in the arasat, '
              'the Sirat defined linguistically and in the Shariah and al-Fawzan link between the '
              'moral sirat and the physical one, the hooks corresponding to the doubts and '
              'desires that snatch in this world, al-Qadi Abd al-Jabbar reinterpretation and why '
              'his two ayat are no evidence, and the retaliation at the Qantarah with the '
              'removing of the rancour in al-Hijr 15:47')
b += B.further()
b += B.nav('was-l38-dawawin-hisab.html', 'The Registers Spread Open, and the Reckoning',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l39')

io.open(os.path.join(B.AQ, 'was-l39-hawd-sirat-qantarah.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'الحَوْضُ وَالصِّرَاطُ وَالقَنْطَرَة',
    'The Ḥawḍ, the Ṣirāṭ, and the Qanṭarah',
    'Lesson 39 of al-ʿAqīdah al-Wāsiṭiyyah: the Baṣin narrated '
    'by forty Companions and reached in the heat of the waiting; the Path over the back of '
    'Hellfire, where firmness is measured by firmness on the moral path; and the Causeway, where '
    'everything owed between the believers is settled before anyone goes in.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ التَّاسِعُ وَالثَّلَاثُون', '4',
           'الحَوْضُ وَالصِّرَاطُ وَالقَنْطَرَة',
           'The Ḥawḍ, the Ṣirāṭ, and the Qanṭarah', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l39-hawd-sirat-qantarah.html')
