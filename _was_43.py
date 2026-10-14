# -*- coding: utf-8 -*-
"""Wasitiyyah L43 -- Part 5: the second degree of the decree (the volition and
the creating), and that there is no conflict between the decree and the Law, nor
between His decreeing sins and His hating them. With Ibn Taymiyyah's three sects
of the misguided in qadar. Sharh pp.152-156."""
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
    'شَيْخُ الإِسْلَامِ <strong>ابْنُ تَيْمِيَّة</strong>, '
    '<em>الرِّسَالَةُ التَّدْمُرِيَّة</em> — the three sects of the misguided in qadar are quoted '
    'from it here, in the author’s own words.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Say what %s and %s mean in the second degree.' % (ar('النَّافِذَة'), ar('الشَّامِلَة')),
    'Name Ibn Taymiyyah’s three sects of those who go astray in qadar, and the error of each.',
    'State the rule on the relation between %s and %s, with an example each way.'
    % (ar('الإِرَادَة'), ar('المَحَبَّة')),
    'Say which of the two irādahs the rule concerns.',
])

b += B.heading('الدَّرَجَةُ الثَّانِيَة · المَشِيئَةُ النَّافِذَةُ وَالقُدْرَةُ الشَّامِلَة',
               'The Second Degree — the Effective Volition and the All-Embracing Power')
b += B.matn(
    'وَأَمَّا الدَّرَجَةُ الثَّانِيَةُ: فَهِيَ مَشِيئَةُ اللهِ النَّافِذَةُ وَقُدْرَتُهُ '
    'الشَّامِلَةُ؛ وَهُوَ الإِيمَانُ بِأَنَّ مَا شَاءَ اللهُ كَانَ، وَمَا لَمْ يَشَأْ '
    'لَمْ يَكُنْ؛ وَأَنَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الأَرْضِ مِنْ حَرَكَةٍ وَلَا '
    'سُكُونٍ إِلَّا بِمَشِيئَةِ اللهِ سُبْحَانَهُ، لَا يَكُونُ فِي مُلْكِهِ مَا لَا '
    'يُرِيدُ؛ وَأَنَّهُ سُبْحَانَهُ عَلَى كُلِّ شَيْءٍ قَدِيرٌ مِنَ المَوْجُودَاتِ '
    'وَالمَعْدُومَاتِ؛ فَمَا مِنْ مَخْلُوقٍ فِي الأَرْضِ وَلَا فِي السَّمَاءِ إِلَّا '
    'اللهُ خَالِقُهُ سُبْحَانَهُ، لَا خَالِقَ غَيْرُهُ، وَلَا رَبَّ سِوَاهُ.')
b += B.sharh(
    p('al-Fawzān first notes the numbering, with a footnote that saves the reader confusion: '
      '<em>this is a statement of <strong>the third level and the fourth level</strong> of the '
      'levels of the decree</em> — <em>and the author reckoned it «the second» '
      '<strong>because he made the knowledge and the writing a single degree.</strong></em>') +
    p('<strong>%s</strong> — <em>is <strong>the effective one, which nothing turns back</strong></em>; '
      '<strong>%s</strong> — <em>is <strong>the general one, over every thing — of the existent '
      'and the non-existent.</strong></em>'
      % (ar('النَّافِذَة'), ar('الشَّامِلَة'))) +
    p('<strong>%s</strong> — <em>that is: <strong>it came to be</strong></em>; '
      '<strong>%s</strong> — <em>that is: <strong>it did not come to be</strong></em>. '
      '<strong>%s</strong> — <em>that is: <strong>nothing of that occurs but that Allah '
      'willed it</strong></em>. <strong>%s</strong> — <em>its occurring, by way of the '
      'universal decree</em>.'
      % (ar('مَا شَاءَ اللهُ كَانَ'), ar('وَمَا لَمْ يَشَأْ لَمْ يَكُنْ'),
         ar('مَا فِي السَّمَاوَاتِ… مِنْ حَرَكَةٍ وَلَا سُكُونٍ إِلَّا بِمَشِيئَةِ اللهِ'),
         ar('لَا يَكُونُ فِي مُلْكِهِ مَا لَا يُرِيدُ'))) +
    p('Note the parenthesis al-Fawzān adds there — <strong>%s, by way of the universal '
      'decree</strong>. He is marking which of the two irādahs the clause is about, because the '
      'whole of the rest of this lesson turns on that distinction. '
      '<strong>«Nothing occurs in His dominion that He does not will» is about the decreeing '
      'will, not about His approving of it.</strong>' % ar('كَوْنًا وَقَدَرًا')) +
    p('<strong>%s</strong> — <em>and in this is <strong>an indication of the fourth level, which '
      'is the level of the creating and the bringing into being</strong>: '
      '<strong>so everything besides Allah is created, and all the actions — their good and their '
      'evil — issue from His creating them and His originating them</strong></em> — '
      '<strong>%s</strong>.'
      % (ar('فَمَا مِنْ مَخْلُوقٍ فِي الأَرْضِ وَلَا فِي السَّمَاءِ إِلَّا اللهُ خَالِقُهُ'),
         ar('لَا خَالِقَ غَيْرُهُ وَلَا رَبَّ سِوَاهُ'))))

b += B.heading('لَا تَعَارُضَ بَيْنَ القَدَرِ وَالشَّرْع',
               'No Conflict between the Decree and the Law')
b += B.matn(
    'وَمَعَ ذَلِكَ فَقَدْ أَمَرَ العِبَادَ بِطَاعَتِهِ وَطَاعَةِ رُسُلِهِ، وَنَهَاهُمْ '
    'عَنْ مَعْصِيَتِهِ. وَهُوَ سُبْحَانَهُ يُحِبُّ المُتَّقِينَ وَالمُحْسِنِينَ '
    'وَالمُقْسِطِينَ، وَيَرْضَى عَنِ الَّذِينَ آمَنُوا وَعَمِلُوا الصَّالِحَاتِ، وَلَا '
    'يُحِبُّ الكَافِرِينَ، وَلَا يَرْضَى عَنِ القَوْمِ الفَاسِقِينَ، وَلَا يَأْمُرُ '
    'بِالفَحْشَاءِ، وَلَا يَرْضَى لِعِبَادِهِ الكُفْرَ، وَلَا يُحِبُّ الفَسَادَ.')
b += B.sharh(
    p('<em>When the Shaykh رحمه الله had established the decree with its four levels — '
      '<strong>the knowledge, the writing, the volition and will, and the creating and bringing '
      'into being</strong> — and that <strong>nothing happens but Allah knew it, wrote it, willed '
      'it, intended it and brought it into being</strong> — '
      '<strong>he made clear here that there is no conflict between that and His having commanded '
      'the servants with His obedience and forbidden them His disobedience; nor between His '
      'decreeing the occurrence of the sin and His hating it.</strong></em>') +
    p('<em>And there is in that no conflict between His Law and His decree — '
      '<strong>as some of the misguided suppose, who set the Law and the decree against each '
      'other.</strong></em>'))
b += B.heading('ثَلَاثُ فِرَقٍ خَاضَتْ فِي القَدَر',
               'Three Sects That Plunged into the Question of Qadar')
b += B.sharh(
    p('And here al-Fawzān quotes the author\'s own words from another of his works — '
      '<em>the Shaykh رحمه الله says on this subject in his treatise '
      '<strong>«التَّدْمُرِيَّة»</strong>: <strong>and the people of misguidance who plunged into '
      'the question of qadar divided into three sects: مَجُوسِيَّة, مُشْرِكِيَّة, '
      'and إِبْلِيسِيَّة.</strong></em>') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.89rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>١ المَجُوسِيَّة</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<em><strong>who belied the decree of Allah, even while they believed in His command and His '
    'prohibition.</strong> <strong>Their extremists denied the knowledge and the Book</strong>; '
    '<strong>and their moderates denied the generality of His volition, His creating and His '
    'power.</strong> <strong>And these are the Muʿtazilah and whoever agreed with '
    'them.</strong></em></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>٢ المُشْرِكِيَّة</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<em><strong>who acknowledged the decree and the measuring, and denied the command and the '
    'prohibition.</strong> — <strong>So whoever argues for the nullifying of the command and '
    'the prohibition is of these.</strong> <strong>And this has become widespread among those of '
    'the ṣūfiyyah who lay claim to «the Reality».</strong></em></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>٣ الإِبْلِيسِيَّة</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<em><strong>who acknowledged both matters</strong> — but '
    '<strong>made this a contradiction on the part of the Lord</strong> '
    'سبحانه وتعالى, and '
    '<strong>impugned His wisdom and His justice</strong> — '
    '<strong>as is related of Iblīs, the foremost of them</strong>, as the authors of the '
    'doctrinal works transmitted, and as is transmitted of the People of the '
    'Book.</em></td></tr>'
    '</table></div>' +
    p('That classification is worth more than a list of names, because it covers every available '
      'move. <strong>There are only three things to do with two premises that look '
      'incompatible</strong> — deny the first, deny the second, or accept both and call the author '
      'of them inconsistent. The Majūsiyyah took the first, the Mushrikiyyah the second, '
      '<strong>and the Iblīsiyyah the third — which is why they are named after Iblīs rather '
      'than after a scholar.</strong>') +
    p('And the second row is the one with a living application. '
      '<strong>«Whoever argues for the nullifying of the command and the prohibition is of '
      'these»</strong> — that is, anyone who answers a rebuke with <em>it was decreed</em>. '
      'And the Qurʾān records the words:'))
b += B.ayah(
    'سَيَقُولُ الَّذِينَ أَشْرَكُوا لَوْ شَاءَ اللَّهُ مَا أَشْرَكْنَا وَلَا آبَاؤُنَا '
    'وَلَا حَرَّمْنَا مِنْ شَيْءٍ',
    '"Those who associated others with Allah will say: had Allah willed, we would not have '
    'associated, nor our fathers, nor would we have forbidden anything."',
    'Sūrat al-Anʿām 6:148 · سُورَةُ الأَنْعَام')
b += B.prose(
    'The argument is impeccable as far as it goes, and that is what makes it instructive: '
    '<strong>everything in it is true.</strong> Had Allah willed, they would not have associated. '
    'The error is not in the premise but in <em>what it is being used for</em> — '
    '<strong>a true statement about the decree, produced in order to be excused from the '
    'Law.</strong> And al-Fawzān notes where the move survives: among those of the ṣūfiyyah who '
    'claim to have passed beyond the commands to «the Reality».')
b += B.sharh(
    p('And then the author\'s own summary, which al-Fawzān quotes to the end: '
      '<em>and the point is: <strong>that this is what the people of misguidance say falsely. '
      'As for the people of guidance and success, they believe in THIS and in THAT</strong></em> '
      '— <em>and they believe <strong>that Allah is the Creator of everything, and its Lord and '
      'its Owner; and that what He willed came to be and what He did not will did not come to be; '
      'and that He is Able over everything; and that He has encompassed everything in knowledge; '
      'and that He has counted everything in a clear register.</strong></em>') +
    p('<strong>%s — they believe in this and in that.</strong> That is the whole of the answer, '
      'and it is the method of Lesson 30 in its last application: '
      '<strong>each sect kept one half of the revelation and had to discard the other, and Ahl '
      'al-Sunnah hold both.</strong>' % ar('يُؤْمِنُونَ بِهَذَا وَهَذَا')))

b += B.heading('لَا تَلَازُمَ بَيْنَ الإِرَادَةِ وَالمَحَبَّة',
               'No Necessary Link between the Will and the Love')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>He loves whoever is characterised by the '
      'praiseworthy qualities</strong>, such as taqwā, iḥsān and justice</em>; '
      '<strong>%s</strong>, <em>as He informed in many āyāt, '
      '<strong>for what they were characterised by of faith and righteous action</strong></em>.'
      % (ar('وَهُوَ سُبْحَانَهُ يُحِبُّ المُتَّقِينَ وَالمُحْسِنِينَ وَالمُقْسِطِينَ'),
         ar('وَيَرْضَى عَنِ الَّذِينَ آمَنُوا وَعَمِلُوا الصَّالِحَاتِ'))) +
    p('<strong>%s</strong> — <em>that is: <strong>He is not pleased with whoever is characterised '
      'by the qualities He hates</strong>, such as disbelief and depravity and the rest of the '
      'blameworthy qualities</em>. <strong>%s</strong> — <em>and it is '
      '<strong>what has reached the furthest point of ugliness, of statements and of '
      'actions</strong></em>. <strong>%s</strong> — <em>for He hates them both, '
      '<strong>and for what is in them both of harm to the servants and to the '
      'lands.</strong></em>'
      % (ar('وَلَا يُحِبُّ الكَافِرِينَ، وَلَا يَرْضَى عَنِ القَوْمِ الفَاسِقِينَ'),
         ar('وَلَا يَأْمُرُ بِالفَحْشَاءِ'),
         ar('وَلَا يَرْضَى لِعِبَادِهِ الكُفْرَ وَلَا يُحِبُّ الفَسَادَ'))) +
    p('<em>And the Shaykh رحمه الله intends by this speech <strong>the refutation of whoever '
      'claimed that between the will and the love there is a necessary link</strong> — '
      '<strong>so that if Allah willed a thing He has loved it, and if He decreed a thing He has '
      'loved it.</strong></em>') +
    p('<em>And <strong>this is a false statement.</strong> <strong>And the true statement is: '
      'that there is no necessary link between the will and the love</strong>, or between the '
      'volition and the love — <strong>I mean the universal will and volition.</strong></em>') +
    p('That qualification is the key to the whole question, and it is why al-Fawzān flagged %s '
      'earlier. <strong>The student met the two irādahs in Lesson 11: the %s, which is the '
      'decreeing will and is not tied to love; and the %s, which is the legislative will and '
      '<em>is</em>.</strong> Collapse the two into one word and the question becomes '
      'unanswerable; keep them apart and it dissolves.'
      % (ar('كَوْنًا وَقَدَرًا'), ar('الإِرَادَةُ الكَوْنِيَّة'),
         ar('الإِرَادَةُ الشَّرْعِيَّة'))) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.92rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>قَدْ يَشَاءُ مَا لَا يُحِبُّه</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<em>He may will what He does not love</em> — <strong>example: His volition for the '
    'existence of Iblīs</strong>, and his continuing</td></tr>'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>وَقَدْ يُحِبُّ مَا لَا يَشَاءُ وُجُودَه</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<em>and He may love what He does not will the existence of</em> — '
    '<strong>example: the acts of obedience of the disbelievers</strong>, '
    '<strong>which He did not will to come from them — and had He willed it, it would have '
    'existed.</strong></td></tr>'
    '</table></div>' +
    p('Two examples, one in each direction, and together they settle it. '
      '<strong>Iblīs exists and is not loved; the disbeliever\'s obedience is loved and does not '
      'exist.</strong> So the two things come apart in both directions, which is as complete a '
      'refutation of a claimed necessary link as can be given.') +
    p('And notice what the second example quietly affirms: <strong>had He willed the disbeliever\'s '
      'obedience, it would have existed.</strong> The all-embracing power of the second degree is '
      'not softened in order to make room for the love — <strong>both are stated at full '
      'strength, which is what «they believe in this and in that» means in '
      'practice.</strong>'))

b += B.vocab([
    ('النَّافِذَة', 'al-nāfidhah', 'the effective',
     'Of His volition — the one nothing turns back'),
    ('الشَّامِلَة', 'al-shāmilah', 'the all-embracing',
     'Of His power — over the existent and the non-existent'),
    ('كَوْنًا وَقَدَرًا', 'kawnan wa-qadaran', 'by way of the universal decree',
     'al-Fawzān’s marker for WHICH will is meant'),
    ('المَجُوسِيَّة', 'al-majūsiyyah', 'the Magian sect',
     'Belied the decree while believing in the command — the Muʿtazilah'),
    ('المُشْرِكِيَّة', 'al-mushrikiyyah', 'the associating sect',
     'Acknowledged the decree and denied the command — answering a rebuke with «it was '
     'decreed»'),
    ('الإِبْلِيسِيَّة', 'al-iblīsiyyah', 'the Iblīsian sect',
     'Accepted both and called the Lord inconsistent — named after Iblīs, their '
     'foremost'),
    ('التَّلَازُم', 'al-talāzum', 'a necessary link',
     'What does NOT hold between the universal will and the love'),
    ('الفَحْشَاء', 'al-faḥshāʾ', 'gross indecency',
     'What has reached the furthest point of ugliness, in word or deed'),
])
b += B.mcq('ws-l43', [
    ('What do %s and %s mean?' % (ar('النَّافِذَة'), ar('الشَّامِلَة')),
     ['The hidden and the manifest',
      'The effective, which nothing turns back; and the general, over the existent and the '
      'non-existent',
      'The eternal and the created', 'The legislative and the universal'], 1),
    ('Why does al-Fawzān add %s to the clause about His dominion?' % ar('كَوْنًا وَقَدَرًا'),
     ['To show the clause is about this world only',
      'To mark WHICH will is meant — the decreeing will, not His approving of what occurs',
      'To limit it to the believers', 'To indicate it is figurative'], 1),
    ('What was the error of the Majūsiyyah?',
     ['They denied the command and the prohibition',
      'They belied the decree while believing in His command — their extremists denying the '
      'knowledge and the Book, their moderates the generality of His volition and power',
      'They accepted both and impugned His wisdom',
      'They said the servant creates nothing at all'], 1),
    ('What was the error of the Mushrikiyyah, and where does al-Fawzān say it survives?',
     ['Denying the decree; among the philosophers',
      'Acknowledging the decree and denying the command and prohibition — widespread among those '
      'of the ṣūfiyyah who lay claim to "the Reality"',
      'Denying the knowledge; among the astrologers',
      'Impugning His justice; among the People of the Book'], 1),
    ('Why are the third sect named after Iblīs?',
     ['Because they worship him',
      'Because they accepted both matters and called this a contradiction on the Lord’s '
      'part, impugning His wisdom and justice — as is related of Iblīs, the foremost of them',
      'Because they deny the decree entirely',
      'Because they claim he was wronged'], 1),
    ('What is wrong with the argument in al-Anʿām 6:148?',
     ['Its premise is false — Allah did not will their shirk',
      'Everything in it is true; the error is what it is used FOR — a true statement about the '
      'decree produced in order to be excused from the Law',
      'It confuses the two kinds of will',
      'It was spoken only in the Hereafter'], 1),
    ('What is the true position on the will and the love?',
     ['Whatever He wills, He loves',
      'There is no necessary link between the UNIVERSAL will and the love: He may will what He '
      'does not love, and love what He does not will the existence of',
      'He loves only what He commands and wills only what He loves',
      'The question cannot be answered'], 1),
    ('What are the two examples, one in each direction?',
     ['The sins of the believers, and the good of the disbelievers',
      'His volition for the existence of Iblīs — willed and not loved; and the acts of obedience '
      'of the disbelievers — loved and not willed to exist',
      'Laylat al-Qadr, and the Day of Judgement',
      'The command to Ādam, and the command to Iblīs'], 1),
])
b += B.tf('ws-l43-tf', [
    ('مَا شَاءَ اللهُ كَانَ وَمَا لَمْ يَشَأْ لَمْ يَكُنْ.',
     'What Allah willed came to be, and what He did not will did not come to be.', True),
    ('كُلُّ مَا أَرَادَهُ اللهُ كَوْنًا فَقَدْ أَحَبَّهُ.',
     'Everything Allah willed universally, He loved.', False),
    ('يُحِبُّ اللهُ طَاعَاتِ الكُفَّارِ وَلَمْ يَشَأْ وُجُودَهَا مِنْهُمْ.',
     'Allah loves the acts of obedience of the disbelievers but did not will them to come from '
     'them.', True),
    ('مَنِ احْتَجَّ بِالقَدَرِ عَلَى تَعْطِيلِ الأَمْرِ وَالنَّهْيِ فَهُوَ مِنَ المُشْرِكِيَّةِ.',
     'Whoever argues by the decree for nullifying the command and prohibition is of the '
     'Mushrikiyyah.', True),
])
b += B.memorize(
    'يُؤْمِنُونَ بِهَذَا وَهَذَا',
    'Ibn Taymiyyah\'s own four words for the people of guidance, after naming the three sects who '
    'each kept one half. Learn them as the test you apply to your own reasoning: if holding two '
    'established things together feels impossible, the fault is in the holding — not in one of '
    'the two.')
b += B.aiquiz('The second degree of the decree in al-Aqidah al-Wasitiyyah: al-nafidhah and '
              'al-shamilah, why al-Fawzan marks the clause kawnan wa-qadaran, Ibn Taymiyyahs '
              'three sects from al-Tadmuriyyah -- the Majusiyyah who denied the decree, the '
              'Mushrikiyyah who denied the command and survive among those claiming the Reality, '
              'and the Iblisiyyah who accepted both and called the Lord inconsistent -- why the '
              'argument of al-Anam 6:148 is true in every premise and still wrong, and that there '
              'is no necessary link between the universal will and the love, with Iblis and the '
              'obedience of the disbelievers as the two examples')
b += B.further()
b += B.nav('was-l42-qadar-ilm-kitabah.html', 'The Decree — the Knowledge and the Writing',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l43')

io.open(os.path.join(B.AQ, 'was-l43-mashiah-khalq.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'المَشِيئَةُ وَالخَلْقُ · وَلَا تَعَارُضَ بَيْنَ القَدَرِ وَالشَّرْع',
    'The Volition and the Creating — and No Conflict between the Decree and the Law',
    'Lesson 43 of al-ʿAqīdah al-Wāsiṭiyyah: the third and fourth '
    'levels of the decree; Ibn Taymiyyah’s three sects of those who plunge into qadar, which '
    'between them cover every available move; why the argument “had Allah willed” is '
    'true in every premise and still wrong; and the two examples that break the supposed link '
    'between His will and His love.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الثَّالِثُ وَالأَرْبَعُون', '5',
           'المَشِيئَةُ وَالخَلْقُ · وَلَا تَعَارُضَ بَيْنَ القَدَرِ وَالشَّرْع',
           'The Volition and the Creating — and No Conflict with the Law', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l43-mashiah-khalq.html')
