# -*- coding: utf-8 -*-
"""Wasitiyyah L32 -- Part 3: what must be held regarding His highness and
withness, the meaning of His being "in the heaven", and the two grounds against
supposing the heaven carries or shades Him. Sharh pp.116-117."""
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
    'Distinguish %s from %s, and say which the author permits.'
    % (ar('التَّحْرِيف'), ar('الصِّيَانَةُ عَنِ الظُّنُونِ الكَاذِبَة')),
    'Define %s and %s, and state the false supposition they name.'
    % (ar('تُقِلّه'), ar('تُظِلّه')),
    'Reproduce the consensus in its two-way form.',
    'Lay out the argument from the Kursī and the Throne, and the argument from Allah’s holding up '
    'the heavens.',
])

b += B.heading('مَا يَجِبُ اعْتِقَادُهُ فِي عُلُوِّهِ وَمَعِيَّتِهِ · وَمَعْنَى كَوْنِهِ فِي السَّمَاء',
               'What Must Be Held regarding His Highness and Withness — and the Meaning of His '
               'Being "in the Heaven"')
b += B.matn(
    'وَكُلُّ هَذَا الكَلَامِ الَّذِي ذَكَرَهُ اللهُ مِنْ أَنَّهُ فَوْقَ العَرْشِ، '
    'وَأَنَّهُ مَعَنَا — حَقٌّ عَلَى حَقِيقَتِهِ، لَا يَحْتَاجُ إِلَى تَحْرِيفٍ، '
    'وَلَكِنْ يُصَانُ عَنِ الظُّنُونِ الكَاذِبَةِ، مِثْلُ أَنْ يُظَنَّ أَنَّ ظَاهِرَ '
    'قَوْلِهِ ﴿فِي السَّمَاءِ﴾ أَنَّ السَّمَاءَ تُقِلُّهُ أَوْ تُظِلُّهُ. وَهَذَا '
    'بَاطِلٌ بِإِجْمَاعِ أَهْلِ العِلْمِ وَالإِيمَانِ، فَإِنَّ اللهَ قَدْ ﴿وَسِعَ '
    'كُرْسِيُّهُ السَّمَاوَاتِ وَالْأَرْضَ﴾، وَهُوَ الَّذِي ﴿يُمْسِكُ السَّمَاوَاتِ '
    'وَالْأَرْضَ أَنْ تَزُولَا﴾، ﴿وَيُمْسِكُ السَّمَاءَ أَنْ تَقَعَ عَلَى الْأَرْضِ '
    'إِلَّا بِإِذْنِهِ﴾، ﴿وَمِنْ آيَاتِهِ أَنْ تَقُومَ السَّمَاءُ وَالْأَرْضُ '
    'بِأَمْرِهِ﴾.')
b += B.sharh(
    p('The author draws a distinction here that is easy to miss and that the whole section turns '
      'on. The texts <strong>%s — are true upon their reality</strong>; they '
      '<strong>%s — do not stand in need of taḥrīf</strong>. '
      '<strong>But</strong> — <strong>%s</strong> — they '
      '<strong>are to be <em>guarded</em> from false suppositions</strong>.'
      % (ar('حَقٌّ عَلَى حَقِيقَتِهِ'), ar('لَا يَحْتَاجُ إِلَى تَحْرِيفٍ'),
         ar('وَلَكِنْ يُصَانُ عَنِ الظُّنُونِ الكَاذِبَةِ'))) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.91rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .75rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>التَّحْرِيف</strong></td>'
    '<td style="padding:.6rem .75rem;border:1px solid var(--line)">changing what the text '
    '<em>says</em> — <strong>forbidden</strong>, and the text needs none of it</td></tr>'
    '<tr><td style="padding:.6rem .75rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>الصِّيَانَة</strong></td>'
    '<td style="padding:.6rem .75rem;border:1px solid var(--line)">ruling out what the text '
    '<em>does not say</em> — <strong>obligatory</strong></td></tr>'
    '</table></div>' +
    p('These are opposite operations, and the muʿaṭṭilah collapse them. '
      '<strong>They say: the apparent meaning would be absurd, therefore the wording must be '
      'reinterpreted.</strong> Ahl al-Sunnah answer: the apparent meaning is true, '
      '<em>and the absurd thing you imagined was never the apparent meaning.</em> '
      '<strong>You do not have to move the text to be rid of a supposition you brought to '
      'it.</strong>') +
    p('al-Fawzān names what is being refused: <em>it is obligatory to believe in it as Allah '
      'informed, <strong>and it is not permitted to reinterpret it and turn it from its apparent '
      'sense, as the muʿaṭṭilah of the Jahmiyyah and the Muʿtazilah and their like do</strong>, '
      'claiming that it is not real but figurative. So they reinterpret '
      '<strong>the istiwāʾ upon the Throne as the seizing of dominion</strong>, and '
      '<strong>Allah\'s highness over His creation as the loftiness of His rank and His '
      'overpowering</strong>, and the like of these false reinterpretations, '
      '<strong>which are a distorting of the speech of Allah from its places.</strong></em>') +
    p('And the other extreme, which is the mirror error: <em>and <strong>among them are those who '
      'say that the meaning of His being with us is that He is indwelling in every place</strong>, '
      'as <strong>%s</strong> and others say — تَعَالَى اللهُ عَمَّا يَقُولُونَ عُلُوًّا '
      'كَبِيرًا.</em> One party emptied the texts of height; the other filled all of space with '
      'Him. <strong>Both read %s as <em>mixed in among</em></strong>, and then differed only over '
      'which half to sacrifice.' % (ar('حُلُولِيَّةُ الجَهْمِيَّة'), ar('مَعَكُمْ'))))

b += B.heading('تُقِلُّهُ أَوْ تُظِلُّه', '"Carries Him, or Shades Him"')
b += B.sharh(
    p('Now the two words of the false supposition, defined: <strong>%s</strong> — <em>that is: '
      '<strong>carries Him</strong></em>; <strong>%s</strong> — <em>that is: '
      '<strong>covers Him over</strong>; and %s is <strong>the thing that shades you from '
      'above</strong>.</em>' % (ar('تُقِلُّه'), ar('تُظِلُّه'), ar('الظُّلَّة'))) +
    p('So the supposition is a picture: <strong>the sky as a floor He stands on, or a canopy over '
      'His head.</strong> And al-Fawzān: <em>and <strong>these two meanings are not what is '
      'intended</strong> in His being سبحانه in the heaven. <strong>And whoever supposes that has '
      'erred the utmost error</strong></em> — <em>and that is for two reasons.</em>'))

b += B.heading('الأَمْرُ الأَوَّل · خِلَافُ الإِجْمَاع', 'First — It Contradicts the Consensus')
b += B.sharh(
    p('<em>That <strong>this contradicts what the people of knowledge and faith were agreed '
      'upon</strong>: for they were agreed that He سبحانه is '
      '<strong>above His Throne, separate from His creation</strong></em> — and then the clause '
      'to memorise, because it closes the door in both directions at once:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.97rem;text-align:center" dir="rtl" lang="ar">'
    '<strong>لَيْسَ فِي ذَاتِهِ شَيْءٌ مِنْ مَخْلُوقَاتِهِ، وَلَا فِي مَخْلُوقَاتِهِ '
    'شَيْءٌ مِنْ ذَاتِهِ</strong></p>'
    '<p style="margin:.55rem 0 0;font-size:.92rem;text-align:center"><em>— '
    '<strong>there is nothing of His creation in His Self, and nothing of His Self in His '
    'creation.</strong></em></p></div>' +
    p('Two denials, and each one answers a different error. '
      '<strong>«Nothing of His creation in His Self»</strong> rules out the sky carrying Him or '
      'shading Him — the very supposition this section is guarding against, in which something '
      'created becomes part of His situation. '
      '<strong>«Nothing of His Self in His creation»</strong> rules out the <em>ḥulūliyyah</em> — '
      'the indwelling in every place. <strong>One sentence, both extremes.</strong>') +
    p('<em>And the discussion of the explanation of His saying %s has already come</em> — '
      'Lesson 16 and Lesson 26: <em>if what is intended by «the heaven» is the built heaven, then '
      '%s is in the sense of %s — that is, <strong>above the heaven</strong>, as in His saying '
      '%s, meaning <em>upon</em> the trunks of the palm trees; and if what is intended by «the '
      'heaven» is <strong>the height</strong>, then the meaning of «in the heaven» is '
      '<strong>in the loftiness</strong>. وَاللهُ أَعْلَم.</em>'
      % (ar('مَنْ فِي السَّمَاءِ'), ar('فِي'), ar('عَلَى'),
         ar('وَلَأُصَلِّبَنَّكُمْ فِي جُذُوعِ النَّخْلِ'))))

b += B.heading('الأَمْرُ الثَّانِي · مُصَادَمَةُ أَدِلَّةِ القُرْآن',
               'Second — It Collides with the Proofs of the Qurʾān')
b += B.sharh(
    p('<em>That <strong>this supposition opposes and collides with the proofs of the Qurʾān</strong> '
      'which indicate <strong>the greatness of Allah, and His freedom from need of His creation, '
      'and His creation\'s need of Him.</strong></em> And the author brought four āyāt for it. '
      'Take the first:'))
b += B.ayah(
    'وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالْأَرْضَ وَلَا يَئُودُهُ حِفْظُهُمَا وَهُوَ '
    'الْعَلِيُّ الْعَظِيمُ',
    '"His Kursī extends over the heavens and the earth, and their preservation does not weary Him '
    '— and He is the Most High, the Most Great."',
    'Sūrat al-Baqarah 2:255 · سُورَةُ البَقَرَة')
b += B.sharh(
    p('al-Fawzān sets out the scale, and the argument is simply a matter of following it: '
      '<em>and <strong>the Kursī is a mighty created thing before the Throne</strong>, '
      '<strong>and it is greater than the heavens and the earth</strong>; '
      '<strong>and the Throne is greater than it.</strong></em>') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.95rem">'
    '<p style="margin:0 0 .5rem;text-align:center">the heavens and the earth &nbsp;&lt;&nbsp; '
    '<strong>the Kursī</strong> &nbsp;&lt;&nbsp; <strong>the Throne</strong> '
    '&nbsp;&lt;&nbsp; <strong>Allah, greater than everything</strong></p>'
    '<p style="margin:0;text-align:center"><em>— <strong>so how should the heaven contain '
    'Him, or carry Him, or shade Him?!</strong></em></p></div>' +
    p('That is the whole refutation, and notice that it never leaves the Qurʾān\'s own vocabulary. '
      'The supposition needs the sky to be <em>big enough to hold Him</em>. '
      '<strong>The āyah says the sky is not even big enough to hold a single one of His created '
      'things.</strong>'))
b += B.ayah(
    'إِنَّ اللَّهَ يُمْسِكُ السَّمَاوَاتِ وَالْأَرْضَ أَنْ تَزُولَا',
    '"Indeed Allah holds the heavens and the earth lest they cease."',
    'Sūrat Fāṭir 35:41 · سُورَةُ فَاطِر')
b += B.ayah(
    'وَيُمْسِكُ السَّمَاءَ أَنْ تَقَعَ عَلَى الْأَرْضِ إِلَّا بِإِذْنِهِ',
    '"And He holds the heaven from falling upon the earth, except by His permission."',
    'Sūrat al-Ḥajj 22:65 · سُورَةُ الحَجّ')
b += B.ayah(
    'وَمِنْ آيَاتِهِ أَنْ تَقُومَ السَّمَاءُ وَالْأَرْضُ بِأَمْرِهِ',
    '"And among His signs is that the heaven and the earth stand by His command."',
    'Sūrat al-Rūm 30:25 · سُورَةُ الرُّوم')
b += B.sharh(
    p('<em>So <strong>these āyāt indicate that the heavens and the earth are in need of '
      'Him</strong>: for <strong>He is the One who holds them lest they cease or fall</strong>, '
      'and <strong>their standing is by His command alone.</strong></em>') +
    p('And then the conclusion, which is the finest turn in the section: '
      '<em><strong>so it is not conceivable, along with this, that He سبحانه should be in need of '
      'them, so that they might carry Him or shade Him.</strong> '
      'تَعَالَى اللهُ عَنْ هَذَا الظَّنِّ البَاطِلِ عُلُوًّا كَبِيرًا.</em>') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.95rem">Follow the inversion, because it is exact. The false '
    'supposition has <strong>the heaven holding Him up</strong>. The āyāt have '
    '<strong>Him holding the heaven up</strong> — and say that without Him it would fall. '
    '<strong>So the supposition does not merely exaggerate; it reverses the relation the '
    'Qurʾān states.</strong></p></div>' +
    p('And note which attribute the supposition would have cost Him: not the height, but '
      '<strong>the %s — the freedom from all need.</strong> The one who imagines the sky as His '
      'floor has made the Creator dependent on a thing He made. '
      '<strong>That is why the author calls it a <em>false supposition</em> rather than a weak '
      'opinion</strong> — it is not a small mistake about where Allah is; it is a mistake about '
      'what He is.' % ar('الغِنَى')))

b += B.vocab([
    ('حَقٌّ عَلَى حَقِيقَتِه', 'ḥaqqun ʿalā ḥaqīqatih',
     'true upon its reality',
     'The texts need no taḥrīf — only guarding from what they never said'),
    ('الصِّيَانَة', 'al-ṣiyānah', 'guarding',
     'Ruling out what the text does NOT say — the opposite operation to taḥrīf'),
    ('الظُّنُونُ الكَاذِبَة', 'al-ẓunūn al-kādhibah', 'false suppositions',
     'What the reader brings to the text, not what the text carries'),
    ('تُقِلُّه', 'tuqilluh', 'carries Him',
     'The first false picture — the sky as a floor'),
    ('تُظِلُّه', 'tuẓilluh', 'shades Him',
     'The second — the sky as a canopy; الظُّلَّة is what shades you from above'),
    ('حُلُولِيَّةُ الجَهْمِيَّة', 'ḥulūliyyat al-jahmiyyah',
     'the indwelling Jahmiyyah',
     'Who said His being with us means He indwells every place'),
    ('الكُرْسِيّ', 'al-kursī', 'the Kursī',
     'A mighty created thing before the Throne — greater than the heavens and the earth'),
    ('الغِنَى', 'al-ghinā', 'freedom from need',
     'The attribute the false supposition would cost Him'),
])
b += B.mcq('ws-l32', [
    ('What distinction does the author draw between taḥrīf and ṣiyānah?',
     ['Both are forbidden ways of handling the text',
      'Taḥrīf changes what the text says and is forbidden; ṣiyānah rules out what the text does '
      'not say and is obligatory',
      'Taḥrīf is for the scholars and ṣiyānah for the layman',
      'They are two names for the same operation'], 1),
    ('How do Ahl al-Sunnah answer "the apparent meaning would be absurd"?',
     ['By conceding and reinterpreting the wording',
      'By saying the apparent meaning is true, and the absurdity imagined was never the apparent '
      'meaning',
      'By declaring the text’s meaning unknowable',
      'By rejecting the text'], 1),
    ('What do %s and %s mean?' % (ar('تُقِلُّه'), ar('تُظِلُّه')),
     ['Exalts Him and magnifies Him',
      'Carries Him and covers Him over — the sky as a floor, or as a canopy',
      'Contains Him and limits Him', 'Points to Him and indicates Him'], 1),
    ('What is the two-way form of the consensus?',
     ['He is above His Throne and His knowledge is with us',
      'There is nothing of His creation in His Self, and nothing of His Self in His creation',
      'He is neither inside nor outside the world',
      'He is above by His Self and near by His power'], 1),
    ('Which two errors does that one sentence answer?',
     ['The Murjiʾah and the Waʿīdiyyah',
      'The supposition that the sky carries or shades Him; and the ḥulūliyyah, that He indwells '
      'every place',
      'The Rāfiḍah and the Khawārij',
      'The Jabriyyah and the Qadariyyah'], 1),
    ('What is the order of magnitude al-Fawzān sets out?',
     ['The Throne, then the Kursī, then the heavens, then the earth',
      'The heavens and the earth are smaller than the Kursī, the Kursī smaller than the Throne, '
      'and Allah greater than everything',
      'The Kursī and the Throne are the same thing',
      'The heavens are greater than the Kursī'], 1),
    ('What is the inversion in the argument from Fāṭir, al-Ḥajj and al-Rūm?',
     ['That the heavens will cease on the Last Day',
      'The supposition has the heaven holding Him up; the āyāt have Him holding the heaven up — '
      'so it reverses the relation the Qurʾān states',
      'That the heavens were created before the earth',
      'That the heaven falls only by His permission'], 1),
    ('Which attribute would the false supposition cost Him?',
     ['The ʿuluww', 'Al-ghinā — His freedom from all need',
      'The istiwāʾ', 'The encompassing knowledge'], 1),
])
b += B.tf('ws-l32-tf', [
    ('كَلَامُ اللهِ عَنْ عُلُوِّهِ وَمَعِيَّتِهِ يَحْتَاجُ إِلَى تَحْرِيفٍ.',
     'Allah’s speech about His highness and withness stands in need of taḥrīf.', False),
    ('أَجْمَعُوا أَنَّهُ لَيْسَ فِي مَخْلُوقَاتِهِ شَيْءٌ مِنْ ذَاتِهِ.',
     'They agreed that there is nothing of His Self in His creation.', True),
    ('الكُرْسِيُّ أَعْظَمُ مِنَ السَّمَاوَاتِ وَالْأَرْضِ.',
     'The Kursī is greater than the heavens and the earth.', True),
    ('السَّمَاوَاتُ وَالأَرْضُ تَقُومُ بِنَفْسِهَا لَا بِأَمْرِهِ.',
     'The heavens and the earth stand by themselves, not by His command.', False),
])
b += B.memorize(
    'لَيْسَ فِي ذَاتِهِ شَيْءٌ مِنْ مَخْلُوقَاتِهِ، وَلَا فِي مَخْلُوقَاتِهِ شَيْءٌ مِنْ '
    'ذَاتِهِ',
    'The consensus of the people of knowledge and faith, and the most economical sentence in this '
    'part of the book: one clause closes the door on the sky carrying Him, the other on His '
    'indwelling the world. Learn it and you will not need to argue either case twice.')
b += B.aiquiz('What must be held regarding the highness and the withness in al-Aqidah '
              'al-Wasitiyyah: the distinction between tahrif, which changes what the text says, '
              'and siyanah, which rules out what it does not say; tuqilluhu and tuzilluhu as the '
              'two false pictures; the two-way consensus that nothing of His creation is in His '
              'Self and nothing of His Self in His creation; the scale of the Kursi and the '
              'Throne; and the inversion whereby the ayat have Him holding the heaven up')
b += B.further()
b += B.nav('was-l31-wujub-istiwa-maiyyah.html', 'The Obligation of Believing in Both',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l32')

io.open(os.path.join(B.AQ, 'was-l32-fi-al-sama.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'مَعْنَى كَوْنِهِ «فِي السَّمَاءِ» · وَالظُّنُونُ الكَاذِبَة',
    'The Meaning of His Being "in the Heaven", and the False Suppositions',
    'Lesson 32 of al-ʿAqīdah al-Wāsiṭiyyah: why the texts need '
    'guarding rather than reinterpreting, the two false pictures of the sky as a floor or a '
    'canopy, the consensus that closes both doors in one sentence, and the inversion whereby the '
    'Qurʾān has Him holding the heaven up.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الثَّانِي وَالثَّلَاثُون', '3',
           'مَعْنَى كَوْنِهِ «فِي السَّمَاءِ» · وَالظُّنُونُ الكَاذِبَة',
           'The Meaning of His Being "in the Heaven", and the False Suppositions', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l32-fi-al-sama.html')
