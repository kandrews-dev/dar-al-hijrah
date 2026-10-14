# -*- coding: utf-8 -*-
"""Wasitiyyah L35 -- Part 3 closes: the obligation of believing in the believers'
seeing of their Lord, and the two places in which it occurs.
Sharh pp.124-125."""
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
    'The āyāt and aḥādīth of the ruʾyah, and the three objections of those who deny it, were '
    'covered in Lessons 21 and 29 of this track.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Give al-Fawzān’s argument for why denying the ruʾyah touches three pillars of faith.',
    'Say what %s establishes, and against whom.' % ar('عِيَانًا'),
    'Define %s and name the two places of the seeing.' % ar('العَرَصَات'),
    'State the three positions on who sees Him in the first place — without resolving them.',
])

b += B.heading('وُجُوبُ الإِيمَانِ بِرُؤْيَةِ المُؤْمِنِينَ رَبَّهُمْ · وَمَوَاضِعُ الرُّؤْيَة',
               'The Obligation of Believing in the Ruʾyah — and Where It Occurs')
b += B.matn(
    'وَقَدْ دَخَلَ أَيْضًا فِيمَا ذَكَرْنَاهُ مِنَ الإِيمَانِ بِهِ وَبِكُتُبِهِ '
    'وَبِرُسُلِهِ: الإِيمَانُ بِأَنَّ المُؤْمِنِينَ يَرَوْنَهُ عِيَانًا '
    'بِأَبْصَارِهِمْ، كَمَا يَرَوْنَ الشَّمْسَ صَحْوًا لَيْسَ دُونَهَا سَحَابٌ، '
    'وَكَمَا يَرَوْنَ القَمَرَ لَيْلَةَ البَدْرِ لَا يُضَامُّونَ فِي رُؤْيَتِهِ. '
    'يَرَوْنَهُ سُبْحَانَهُ وَهُمْ فِي عَرَصَاتِ القِيَامَةِ، ثُمَّ يَرَوْنَهُ بَعْدَ '
    'دُخُولِ الجَنَّةِ، كَمَا يَشَاءُ اللهُ.')
b += B.sharh(
    p('al-Fawzān begins with the question the author\'s wording raises: '
      '<strong>why is belief in the seeing placed inside belief in Allah, His Books and His '
      'Messengers?</strong> And the answer is an argument worth having, because it applies to '
      'every item of creed established by report:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.94rem"><em>That <strong>Allah '
    'سبحانه informed of it in His Book, and His Messenger '
    '&#65018; informed of it</strong> — <strong>so whoever does not believe in it is '
    'belying Allah, and His Books, and His Messengers.</strong> For '
    '<strong>the one who believes in Allah and His Books and His Messengers believes in '
    'everything they informed of.</strong></em></p></div>' +
    p('Follow the structure of it. <strong>Faith in a messenger is not a feeling about him; it is '
      'the acceptance of what he reported.</strong> So a man cannot say «I believe in Allah and '
      'His Book and His Prophet» and then set aside a thing all three of them stated. '
      '<strong>The denial is not a separate error standing beside his faith — it is a '
      'contradiction inside it.</strong>') +
    p('And that is why the author did not give the ruʾyah a pillar of its own. '
      '<strong>It is not an extra article; it is a test of whether the three he already listed '
      'were meant.</strong>'))
b += B.sharh(
    p('<strong>%s</strong> — <em>with a kasrah on the ع; that is: '
      '<strong>a realised seeing in which there is no obscurity</strong> — '
      '<strong>so it is not figurative, as the muʿaṭṭilah say.</strong></em>'
      % ar('عِيَانًا')) +
    p('One word, and it closes the only escape left. Everything in Lessons 21 and 29 established '
      '<em>that</em> He is seen; <strong>%s establishes that the seeing is seeing</strong> — not '
      'a knowing, not an unveiling of the heart, not a manner of speaking about nearness. The '
      'author put it in because he knew where the reinterpretation would go.' % ar('عِيَانًا')) +
    p('<strong>%s</strong> — <em>that is: <strong>a real seeing in which there is no '
      'hardship</strong>, as the āyāt and the aḥādīth indicated, whose explanation came '
      'before.</em>'
      % ar('كَمَا يَرَوْنَ الشَّمْسَ صَحْوًا لَيْسَ دُونَهَا سَحَابٌ، وَكَمَا يَرَوْنَ القَمَرَ لَيْلَةَ البَدْرِ')) +
    p('Keep Lesson 29\'s clause fixed to both comparisons: <strong>%s</strong> — a likening of '
      'the <em>seeing</em> to the seeing, not of the One seen to the thing seen. The sun and the '
      'moon are named for one property only — <strong>that you look at them and there is nothing '
      'in the way.</strong>'
      % ar('تَشْبِيهٌ لِلرُّؤْيَةِ بِالرُّؤْيَةِ، لَا تَشْبِيهٌ لِلْمَرْئِيِّ بِالمَرْئِيّ')))

b += B.heading('مَوْضِعَانِ لِلرُّؤْيَة', 'Two Places of the Seeing')
b += B.prose(
    '<em>This is a statement of <strong>the places in which the seeing occurs</strong>, and that '
    'is <strong>in two places</strong>.</em> The author is not merely affirming the doctrine '
    'again; he is locating it — and the two locations are not the same event.')
b += B.sharh(
    p('<strong>المَوْضِعُ الأَوَّل</strong> — <strong>%s</strong>. And the word first: '
      '<em>%s is the plural of %s, and it is <strong>the wide place in which there is no '
      'building</strong>; and «the ʿaraṣāt of the Resurrection» are '
      '<strong>%s — the standing-places of the Reckoning.</strong></em>'
      % (ar('فِي عَرَصَاتِ القِيَامَة'), ar('العَرَصَات'), ar('عَرْصَة'),
         ar('مَوَاقِفُ الحِسَاب'))) +
    p('An open plain with nothing built on it — which is the picture the word carries, and part of '
      'why the two comparisons of the sun and the moon fit: <strong>in that place there is '
      'nothing in the way.</strong>') +
    p('<em>And <strong>is the seeing in this place particular to the believers?</strong> On the '
      'question there are <strong>three statements</strong>:</em>') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.91rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>١</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">it has been said: '
    'He is seen in the ʿaraṣāt by <strong>the believers, the hypocrites and the '
    'disbelievers</strong></td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>٢</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">and it has been said: '
    'by <strong>the believers and the hypocrites only</strong>, not the '
    'disbelievers</td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>٣</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">and it has been said: '
    'by <strong>the believers only</strong></td></tr>'
    '</table></div>' +
    p('al-Fawzān states the three and closes with <strong>%s</strong> — '
      '<em>and Allah knows best</em>. <strong>He does not choose between them, and neither does '
      'this lesson.</strong> It is worth noticing that he can leave a question open here without '
      'any loss: the <em>doctrine</em> — that the believers see their Lord — is settled by '
      'mutawātir texts and consensus, and this is a question about <em>who else</em>, at '
      '<em>one</em> of the two places. <strong>Being precise about what is established is also '
      'being precise about what is not.</strong>' % ar('وَاللهُ أَعْلَم')))
b += B.sharh(
    p('<strong>المَوْضِعُ الثَّانِي</strong> — <em>the believers see Him '
      '<strong>after their entering the Garden</strong>, as that is established in the proofs '
      'from the Book and the Sunnah; and some of those proofs have been mentioned with their '
      'explanation before</em> — Lesson 21\'s %s and %s, and Lesson 29\'s ḥadīth of the full '
      'moon — <em>and the objections of those who deny the seeing, along with the refutation of '
      'them, were also mentioned.</em>'
      % (ar('وَزِيَادَةٌ'), ar('وَلَدَيْنَا مَزِيدٌ'))) +
    p('And on the word <strong>%s</strong>: <em>in the language it is <strong>the garden, the '
      'orchard</strong>; and what is intended by it here is <strong>the abode which Allah has '
      'prepared for His allies</strong> — <strong>and it is the abode of bliss that is absolute '
      'and complete.</strong></em>' % ar('الجَنَّة')) +
    p('<em>Absolute and complete</em> is not decoration. It is the reason the <em>ziyādah</em> of '
      'Lesson 21 had to be the looking at His Face: a bliss described as complete '
      '<strong>cannot have its best thing withheld.</strong>'))

b += B.heading('كَمَا يَشَاءُ اللهُ', '"As Allah Wills"')
b += B.sharh(
    p('The author ends the <em>fasl</em> on three words, and al-Fawzān will not let them pass as '
      'a pious flourish: <strong>%s</strong> — <em>that is: '
      '<strong>%s — without any encompassing of Him, and without any describing of the manner of '
      'the seeing of Him.</strong></em>'
      % (ar('كَمَا يَشَاءُ اللهُ'), ar('مِنْ غَيْرِ إِحَاطَةٍ وَلَا تَكْيِيفٍ لِرُؤْيَتِه'))) +
    p('Both halves of that gloss have been earned earlier in the track, and it is worth seeing '
      'them land together:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.91rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>مِنْ غَيْرِ إِحَاطَة</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">Lesson 21: '
    '<span dir="rtl" lang="ar">لَا تُدْرِكُهُ الْأَبْصَارُ</span> negates '
    '<strong>encompassing</strong>, not seeing — <strong>they see Him and do not take Him '
    'in</strong></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>وَلَا تَكْيِيف</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">Lesson 4: the third of the '
    'four closed doors — and <strong>impossible rather than merely forbidden</strong>, '
    'since no one has the knowledge it would require</td></tr>'
    '</table></div>' +
    p('So the final clause of the section applies the book\'s whole method to its last doctrine. '
      '<strong>The seeing is real, with the eyes, without obscurity</strong> — against the '
      'muʿaṭṭilah. <strong>And it is not comprehended and not pictured</strong> — against the '
      'mushabbihah, and against our own curiosity. <strong>Affirm, and do not ask '
      'how.</strong>'))
b += B.prose(
    'With this the author closes Part 3. <strong>The standing of Ahl al-Sunnah among the sects; '
    'the obligation of holding the highness and the withness together; the meaning of His being '
    '«in the heaven»; the obligation of holding His nearness; that the Qurʾān is His speech in '
    'reality; and the obligation of holding the seeing.</strong> Six sections, and every one of '
    'them is a <em>wājib</em> rather than a proof — because Parts 1 and 2 had already brought the '
    'proofs. <strong>Part 3 is where the reader is told what he is now responsible for.</strong>')

b += B.vocab([
    ('عِيَانًا', 'ʿiyānan', 'plainly, with the eye',
     'A realised seeing with no obscurity — so it is not figurative'),
    ('صَحْوًا', 'ṣaḥwan', 'in a clear sky',
     'The sun with no cloud before it — named for one property: nothing in the way'),
    ('العَرَصَات', 'al-ʿaraṣāt', 'the open plains',
     'Plural of عَرْصَة, a wide place with no building — the standing-places of the Reckoning'),
    ('مَوَاقِفُ الحِسَاب', 'mawāqif al-ḥisāb', 'the standing-places of the Reckoning',
     'What «ʿaraṣāt al-qiyāmah» means'),
    ('الجَنَّة', 'al-jannah', 'the Garden',
     'In the language: the orchard; here: the abode of absolute and complete bliss'),
    ('الإِحَاطَة', 'al-iḥāṭah', 'encompassing',
     'What is negated — they see Him and do not take Him in'),
    ('التَّكْيِيف', 'al-takyīf', 'describing the manner',
     'Also negated — the third of the four closed doors of Lesson 4'),
])
b += B.mcq('ws-l35', [
    ('Why is belief in the ruʾyah placed inside belief in Allah, His Books and His Messengers?',
     ['Because it is mentioned in all the earlier scriptures',
      'Because Allah informed of it in His Book and His Messenger ﷺ informed of it — so whoever '
      'denies it is belying all three',
      'Because the angels will witness it',
      'Because it is the greatest of the rewards'], 1),
    ('What does the author’s word %s establish?' % ar('عِيَانًا'),
     ['That the seeing is in the Garden only',
      'That the seeing is realised with no obscurity — so it is not figurative, as the muʿaṭṭilah '
      'say',
      'That all people will see Him', 'That the seeing is brief'], 1),
    ('For what single property are the sun and the moon named in the comparison?',
     ['Their brightness',
      'That you look at them and there is nothing in the way',
      'Their being created', 'Their rising and setting'], 1),
    ('What is an %s?' % ar('عَرْصَة'),
     ['A gathering of the angels', 'A wide place in which there is no building',
      'A stage of the Reckoning', 'A level of the Garden'], 1),
    ('How many positions does al-Fawzān report on who sees Him in the ʿaraṣāt, and does he choose?',
     ['Two, and he chooses the second',
      'Three — believers, hypocrites and disbelievers; or believers and hypocrites only; or '
      'believers only — and he closes with وَاللهُ أَعْلَم without choosing',
      'Three, and he chooses the third',
      'One, which is the believers only'], 1),
    ('What are the two places of the seeing?',
     ['The grave and the Garden',
      'The ʿaraṣāt of the Resurrection, and after entering the Garden',
      'The Ṣirāṭ and the Ḥawḍ', 'This world in dreams, and the Hereafter'], 1),
    ('What does al-Fawzān say %s means?' % ar('كَمَا يَشَاءُ اللهُ'),
     ['That some will see Him and some will not',
      'Without any encompassing of Him, and without describing the manner of the seeing',
      'That the seeing is as long as He wills',
      'That He appears in a form He chooses'], 1),
])
b += B.tf('ws-l35-tf', [
    ('مَنْ لَمْ يُؤْمِنْ بِالرُّؤْيَةِ كَانَ مُكَذِّبًا لِلَّهِ وَلِكُتُبِهِ وَلِرُسُلِهِ.',
     'Whoever does not believe in the seeing is belying Allah, His Books and His Messengers.',
     True),
    ('الرُّؤْيَةُ مَجَازٌ لَا حَقِيقَةٌ.', 'The seeing is figurative, not real.', False),
    ('رَجَّحَ الفَوْزَانُ أَحَدَ الأَقْوَالِ الثَّلَاثَةِ فِي العَرَصَاتِ.',
     'al-Fawzān favoured one of the three positions on the ʿaraṣāt.', False),
    ('يَرَى المُؤْمِنُونَ رَبَّهُمْ مِنْ غَيْرِ إِحَاطَةٍ وَلَا تَكْيِيفٍ.',
     'The believers see their Lord without encompassing Him and without a described manner.',
     True),
])
b += B.memorize(
    'يَرَوْنَهُ سُبْحَانَهُ وَهُمْ فِي عَرَصَاتِ القِيَامَةِ، ثُمَّ يَرَوْنَهُ بَعْدَ '
    'دُخُولِ الجَنَّةِ، كَمَا يَشَاءُ اللهُ',
    'Two places, and then three words that govern both. Learn the ending with the rest or you '
    'will be tempted to picture it: <em>as Allah wills</em> — without encompassing Him, and '
    'without asking how.')
b += B.aiquiz('The obligation of believing in the believers seeing their Lord in al-Aqidah '
              'al-Wasitiyyah: why denying it belies Allah and His Books and His Messengers at '
              'once, what iyanan establishes against the muattilah, the arasat as wide places '
              'with no building and the three reported positions on who sees Him there without '
              'choosing between them, the Garden as the abode of absolute and complete bliss, '
              'and kama yashaa Allah meaning without encompassing and without takyif')
b += B.further()
b += B.nav('was-l34-quran-kalam-haqiqatan.html', 'The Qurʾān Is Allah’s Speech in Reality',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l35')

io.open(os.path.join(B.AQ, 'was-l35-ruyah-mawadi.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'وُجُوبُ الإِيمَانِ بِالرُّؤْيَةِ · وَمَوَاضِعُهَا',
    'The Obligation of Believing in the Seeing, and Where It Occurs',
    'Lesson 35 of al-ʿAqīdah al-Wāsiṭiyyah, closing Part 3: why '
    'denying the ruʾyah belies Allah, His Books and His Messengers at once; what '
    'ʿiyānan rules out; the two places of the seeing with the three reported views on '
    'the first; and the three words that govern both.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الخَامِسُ وَالثَّلَاثُون', '3',
           'وُجُوبُ الإِيمَانِ بِالرُّؤْيَةِ · وَمَوَاضِعُهَا',
           'The Obligation of Believing in the Seeing, and Where It Occurs', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l35-ruyah-mawadi.html')
