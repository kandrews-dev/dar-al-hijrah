# -*- coding: utf-8 -*-
"""Wasitiyyah L33 -- Part 3: the obligation of believing in His nearness to His
creation, and that it does not contradict His highness. Sharh pp.118-119."""
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
    'The ḥadīth quoted here is <strong>مُتَّفَقٌ عَلَيْه</strong>; for the report on the '
    'occasion of revelation, see the تَنْبِيه on this page.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Give the question that occasioned al-Baqarah 2:186, and what was striking in the answer.',
    'State the principle %s, and use it on this question.' % ar('الحَقُّ لَا يَتَنَاقَض'),
    'Say what faulty step produces the question “if He is above them, how is He with them?”',
    'Explain each half of %s.' % ar('عَلِيٌّ فِي دُنُوِّهِ، قَرِيبٌ فِي عُلُوِّه'),
])

b += B.heading('وُجُوبُ الإِيمَانِ بِقُرْبِهِ مِنْ خَلْقِهِ وَأَنَّ ذَلِكَ لَا يُنَافِي '
               'عُلُوَّهُ وَفَوْقِيَّتَه',
               'The Obligation of Believing in His Nearness — and That It Does Not Contradict His '
               'Highness')
b += B.matn(
    'وَقَدْ دَخَلَ فِي ذَلِكَ الإِيمَانُ بِأَنَّهُ قَرِيبٌ مُجِيبٌ، كَمَا جَمَعَ بَيْنَ '
    'ذَلِكَ فِي قَوْلِهِ: ﴿وَإِذَا سَأَلَكَ عِبَادِي عَنِّي فَإِنِّي قَرِيبٌ أُجِيبُ '
    'دَعْوَةَ الدَّاعِ إِذَا دَعَانِ﴾، وَقَوْلِهِ ﷺ: «إِنَّ الَّذِي تَدْعُونَهُ '
    'أَقْرَبُ إِلَى أَحَدِكُمْ مِنْ عُنُقِ رَاحِلَتِهِ». وَمَا ذُكِرَ فِي الكِتَابِ '
    'وَالسُّنَّةِ مِنْ قُرْبِهِ وَمَعِيَّتِهِ لَا يُنَافِي مَا ذُكِرَ مِنْ عُلُوِّهِ '
    'وَفَوْقِيَّتِهِ، فَإِنَّهُ سُبْحَانَهُ لَيْسَ كَمِثْلِهِ شَيْءٌ فِي جَمِيعِ '
    'نُعُوتِهِ، وَهُوَ عَلِيٌّ فِي دُنُوِّهِ، قَرِيبٌ فِي عُلُوِّهِ.')
b += B.prose(
    'al-Fawzān marks the turn: <em>when the author had established the obligation of believing in '
    'Allah\'s highness above His creation and His istiwāʾ upon His Throne, '
    '<strong>he gave warning in this section that it is obligatory, along with that, to believe '
    'that He is near to His creation.</strong></em> The order matters — and so does the fact that '
    'both are stated as <em>obligations</em>, not as two permitted opinions.')
b += B.ayah(
    'وَإِذَا سَأَلَكَ عِبَادِي عَنِّي فَإِنِّي قَرِيبٌ أُجِيبُ دَعْوَةَ الدَّاعِ إِذَا '
    'دَعَانِ فَلْيَسْتَجِيبُوا لِي وَلْيُؤْمِنُوا بِي لَعَلَّهُمْ يَرْشُدُونَ',
    '"And when My servants ask you about Me — indeed I am near. I answer the call of the caller '
    'when he calls Me. So let them respond to Me and believe in Me, that they may be rightly '
    'guided."',
    'Sūrat al-Baqarah 2:186 · سُورَةُ البَقَرَة')
b += B.sharh(
    p('<em>And there has come, regarding <strong>the occasion of this āyah\'s revelation</strong>, '
      'that <strong>a man came to the Prophet &#65018; and said: O Messenger of Allah —</strong></em>') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.98rem;text-align:center" dir="rtl" lang="ar">'
    '<strong>أَقَرِيبٌ رَبُّنَا فَنُنَاجِيهِ، أَمْ بَعِيدٌ فَنُنَادِيهِ؟</strong></p>'
    '<p style="margin:.55rem 0 0;font-size:.92rem;text-align:center"><em>— '
    '<strong>is our Lord near, so that we may confer with Him quietly — or far, so that we '
    'may call out to Him?</strong></em></p>'
    '<p style="margin:.55rem 0 0;font-size:.9rem;text-align:center">'
    '<em>— <strong>so the Prophet &#65018; was silent</strong>, and this āyah was sent '
    'down.</em></p></div>' +
    '<div style="background:#fff8e6;border-right:4px solid #d4a017;'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .9rem">'
    '<p style="margin:0;font-size:.9rem"><strong dir="rtl" lang="ar">تَنْبِيهٌ</strong> — '
    'al-Fawzān attributes this report to <strong>ابْنُ جَرِيرٍ</strong> and '
    '<strong>ابْنُ أَبِي حَاتِمٍ</strong> and others, <strong>without stating a grading for '
    'it</strong>. Per the rule in Lesson 22 this page reports the attribution and '
    '<strong>supplies no grading of its own</strong>. The doctrine does not rest on it: the '
    'āyah and the ḥadīth that follow are the proof, and the report only supplies '
    'the occasion.</p></div>' +
    p('Still, notice what the question assumes and what the answer refuses. '
      '<strong>The man offered two options and asked which.</strong> Near, or far — and in each '
      'case he had worked out the correct etiquette of duʿāʾ to match. '
      '<strong>The āyah takes the first and drops the alternative entirely.</strong>') +
    p('<strong>%s</strong> — <em>near <strong>to the caller</strong></em>; '
      '<strong>%s</strong>. And al-Fawzān draws out the practical consequence the questioner was '
      'after: <em>and <strong>this indicates the directing toward %s in supplication — '
      'conferring quietly, without raising the voice</strong></em>, as in the ḥadīth:'
      % (ar('فَإِنِّي قَرِيبٌ'), ar('أُجِيبُ دَعْوَةَ الدَّاعِ إِذَا دَعَانِ'),
         ar('المُنَاجَاة'))))
b += B.hadith(
    'إِنَّ الَّذِي تَدْعُونَهُ أَقْرَبُ إِلَى أَحَدِكُمْ مِنْ عُنُقِ رَاحِلَتِهِ',
    '"The One you are calling upon is nearer to each of you than the neck of his riding-beast."',
    'مُتَّفَقٌ عَلَيْهِ — al-Bukhārī and Muslim')
b += B.prose(
    'Its explanation came in Lesson 28, where the Companions were told to go easy on themselves on '
    'the march to Khaybar. <strong>Here the author brings it for a different purpose</strong>: '
    'there it answered «why lower your voices», and here it answers «is He near or far». '
    '<em>And in this āyah and this ḥadīth is an indication of <strong>Allah\'s nearness to the '
    'caller, by His answering him</strong>.</em>')

b += B.heading('الحَقُّ لَا يَتَنَاقَض', 'The Truth Does Not Contradict Itself')
b += B.sharh(
    p('<em>And <strong>this nearness does not contradict His highness</strong>; and this is why '
      'the author said: <strong>%s</strong>.</em>'
      % ar('وَمَا ذُكِرَ فِي الكِتَابِ وَالسُّنَّةِ مِنْ قُرْبِهِ وَمَعِيَّتِهِ لَا يُنَافِي مَا ذُكِرَ مِنْ عُلُوِّهِ وَفَوْقِيَّتِهِ')) +
    p('And al-Fawzān gives two reasons, the first of which is a principle that reaches far beyond '
      'this question:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.98rem;text-align:center" dir="rtl" lang="ar">'
    '<strong>لِأَنَّ الكُلَّ حَقٌّ، وَالحَقُّ لَا يَتَنَاقَضُ</strong></p>'
    '<p style="margin:.55rem 0 0;font-size:.92rem;text-align:center"><em>— '
    '<strong>because all of it is true, and the truth does not contradict itself.</strong></em></p></div>' +
    p('That is the sentence to carry out of Part 3. <strong>It is an argument about where to look '
      'when two revealed texts seem to clash.</strong> Not at the texts — at oneself. If both are '
      'established, and truth cannot contradict truth, then the contradiction is in '
      '<em>my reading</em>, and the work is to find which step of it was mine rather than the '
      'text\'s.') +
    p('And the second reason: <em>and because Allah تعالى is <strong>%s</strong> — '
      '<strong>there is nothing like Him <em>in the totality of His descriptions</em></strong>, '
      'that is, His attributes.</em>'
      % ar('لَيْسَ كَمِثْلِهِ شَيْءٌ فِي جَمِيعِ نُعُوتِهِ')) +
    p('Note the author\'s addition of %s. al-Shūrā 42:11 governed each attribute one at a time '
      'through Parts 1 and 2; here it governs <strong>the relations between them</strong>. Not '
      'only is His hearing unlike ours and His height unlike height we know — '
      '<strong>the way His nearness sits with His height is unlike anything we could '
      'model.</strong>' % ar('فِي جَمِيعِ نُعُوتِه')))
b += B.sharh(
    p('<em>So it is not said: <strong>if He is above His creation, how is He with them?</strong> '
      '— because <strong>this question arises from a mistaken conception, which is '
      '%s — his measuring Him سبحانه against His creation; and this is an invalid '
      'analogy</strong>, because Allah سبحانه is %s.</em>'
      % (ar('قِيَاسُهُ سُبْحَانَهُ بِخَلْقِهِ'), ar('لَيْسَ كَمِثْلِهِ شَيْءٌ'))) +
    p('There is the faulty step, named. <strong>The question is not neutral.</strong> It smuggles '
      'in a premise — that whatever is true of being above and being near <em>for us</em> must '
      'hold for Him — and then presents the consequence of that premise as a problem in the '
      'texts. <strong>It is the same move as %s in Lesson 15</strong>: an analogy applied where '
      'no likeness exists.' % ar('ضَرْبُ الأَمْثَالِ لِلَّه')) +
    p('<em>So <strong>the nearness and the highness come together in His case</strong> — '
      '<strong>because of His greatness, His supreme majesty, and His encompassing</strong>; and '
      'because <strong>%s — the seven heavens are in His Hand like a mustard seed in the hand of '
      'a servant.</strong></em>'
      % ar('السَّمَاوَاتُ السَّبْعُ فِي يَدِهِ كَخَرْدَلَةٍ فِي يَدِ العَبْدِ')) +
    p('And then the question turned back on the questioner: <em><strong>so how should it be '
      'impossible, in the case of One some of whose greatness is this, that He be above His '
      'Throne and draw near to His creation however He wills, while He is upon the '
      'Throne?!</strong></em>') +
    p('Which is the right way round. The objection assumed that greatness makes nearness '
      'difficult. <strong>al-Fawzān answers that greatness is exactly what makes it easy</strong> '
      '— a being who holds the seven heavens like a seed in his palm is not strained by attending '
      'to one man calling in the dark.'))

b += B.heading('عَلِيٌّ فِي دُنُوِّهِ، قَرِيبٌ فِي عُلُوِّه',
               '"High in His Nearness, Near in His Highness"')
b += B.sharh(
    p('The author\'s closing formula, and al-Fawzān explains each half separately so that neither '
      'is read as a softening of the other:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.92rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>عَلِيٌّ فِي دُنُوِّهِ</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)"><em>that is: '
    '<strong>in the state of His nearness to His creation</strong></em> — He is high '
    '<em>while</em> near</td></tr>'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>قَرِيبٌ فِي عُلُوِّهِ</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)"><em>that is: '
    '<strong>near to His creation in the state of His highness above His Throne</strong></em> '
    '— He is near <em>while</em> high</td></tr>'
    '</table></div>' +
    p('<em>— <strong>as the texts of the Book and the Sunnah have indicated, and the scholars of '
      'the religion were agreed upon</strong>; <strong>and it is of His particular '
      'characteristics سبحانه</strong></em> (%s).' % ar('مِنْ خَصَائِصِهِ سُبْحَانَهُ')) +
    p('That last clause is the quiet resolution of the whole difficulty, and it is worth stating '
      'plainly. <strong>Being high while near is not a paradox He resolves; it is something that '
      'belongs to Him alone.</strong> No creature is both, which is exactly why the human mind '
      'reaches for a contradiction — it has no instance to reason from. '
      '<strong>And a description that belongs to Allah alone is not refuted by the observation '
      'that nothing else has it.</strong>') +
    p('You met this formula first in Lesson 28, in the Prophetic duʿāʾ of al-Ẓāhir and al-Bāṭin. '
      'There it was the <em>conclusion</em> drawn from two names the Prophet &#65018; placed side '
      'by side. <strong>Here it is the author\'s own statement of the creed</strong>, and the two '
      'arrive at the same words — which is itself a small demonstration of why Part 2 was not a '
      'second argument but the same one.'))

b += B.vocab([
    ('قَرِيبٌ مُجِيب', 'qarībun mujīb', 'Near, Answering',
     'The two joined in al-Baqarah 2:186 — the nearness is stated THROUGH the answering'),
    ('المُنَاجَاة', 'al-munājāh', 'conferring quietly',
     'What the āyah directs to in duʿāʾ — without raising the voice'),
    ('الحَقُّ لَا يَتَنَاقَض', 'al-ḥaqqu lā yatanāqaḍ',
     'the truth does not contradict itself',
     'So where two established texts seem to clash, the fault is in the reading'),
    ('جَمِيعُ نُعُوتِه', 'jamīʿu nuʿūtih',
     'the totality of His descriptions',
     'Al-Shūrā 42:11 governs not only each attribute but the relations between them'),
    ('قِيَاسُ الخَالِقِ بِالخَلْق', 'qiyās al-khāliq bi-l-khalq',
     'measuring the Creator against the creation',
     'The faulty step that produces the question — an invalid analogy'),
    ('خَرْدَلَة', 'khardalah', 'a mustard seed',
     'The seven heavens in His Hand like one, in the hand of a servant'),
    ('مِنْ خَصَائِصِه', 'min khuṣāʾiṣih',
     'of His particular characteristics',
     'Being high while near belongs to Him ALONE — which is why no analogy reaches it'),
])
b += B.mcq('ws-l33', [
    ('What question occasioned al-Baqarah 2:186?',
     ['Whether duʿāʾ is answered for the sinner',
      '"Is our Lord near, so that we may confer with Him quietly — or far, so that we may call '
      'out to Him?"',
      'Whether the fast may be broken for illness',
      'Where Allah is'], 1),
    ('What is striking in how the āyah answers it?',
     ['It answers neither option',
      'The man offered two options and asked which; the āyah takes the first and drops the '
      'alternative entirely',
      'It rebukes the questioner', 'It defers the answer to the Hereafter'], 1),
    ('What practical direction does al-Fawzān draw from %s?' % ar('فَإِنِّي قَرِيبٌ'),
     ['That duʿāʾ should be made in congregation',
      'The directing toward munājāh in supplication — conferring quietly, without raising the '
      'voice',
      'That duʿāʾ should be made facing the qiblah',
      'That duʿāʾ is answered only at night'], 1),
    ('What is the principle %s, and what does it imply?' % ar('الحَقُّ لَا يَتَنَاقَض'),
     ['That weak texts must be rejected',
      'All of it is true and truth cannot contradict truth — so where two established texts seem '
      'to clash, the contradiction is in the reading',
      'That one text must abrogate the other',
      'That the texts’ meanings are unknowable'], 1),
    ('What does the author’s phrase %s add to al-Shūrā 42:11?'
     % ar('فِي جَمِيعِ نُعُوتِهِ'),
     ['That the negation applies only to the Essence',
      'That it governs not only each attribute singly but the relations between them — including '
      'how His nearness sits with His height',
      'That the attributes are innumerable',
      'That only the names are meant'], 1),
    ('What faulty step produces "if He is above them, how is He with them?"',
     ['Trusting a weak narration',
      'Measuring Allah against His creation — an invalid analogy, since nothing is like Him',
      'Reading the āyah out of context',
      'Confusing the ʿuluww with the istiwāʾ'], 1),
    ('How does al-Fawzān use the image of the mustard seed?',
     ['To show the heavens will be destroyed',
      'To turn the objection round: greatness is what makes the nearness easy, not difficult',
      'To show the smallness of this world',
      'To describe the Throne'], 1),
    ('What does al-Fawzān say about being high while near?',
     ['That it is a paradox resolved only in the Hereafter',
      'That it is of His particular characteristics — belonging to Him alone, which is why no '
      'analogy reaches it',
      'That it is a figure of speech',
      'That the scholars differed over it'], 1),
])
b += B.tf('ws-l33-tf', [
    ('الآيَةُ تَدُلُّ عَلَى المُنَاجَاةِ فِي الدُّعَاءِ بِدُونِ رَفْعِ صَوْتٍ.',
     'The āyah indicates conferring quietly in duʿāʾ, without raising the voice.', True),
    ('قُرْبُ اللهِ مِنَ الدَّاعِي يُنَاقِضُ عُلُوَّهُ.',
     'Allah’s nearness to the caller contradicts His highness.', False),
    ('سُؤَالُ «كَيْفَ يَكُونُ مَعَهُمْ وَهُوَ فَوْقَهُمْ؟» نَاشِئٌ عَنْ قِيَاسِ الخَالِقِ بِالخَلْقِ.',
     'The question "how is He with them while above them?" arises from measuring the Creator '
     'against the creation.', True),
    ('كَوْنُهُ عَلِيًّا فِي دُنُوِّهِ مِنْ خَصَائِصِهِ سُبْحَانَهُ.',
     'His being high in His nearness is of His particular characteristics.', True),
])
b += B.memorize(
    'وَهُوَ عَلِيٌّ فِي دُنُوِّهِ، قَرِيبٌ فِي عُلُوِّهِ',
    'The author\'s own words, and the end of a road that began in Lesson 16. Keep al-Fawzān\'s '
    'reason with them — <span dir="rtl" lang="ar">لِأَنَّ الكُلَّ حَقٌّ، وَالحَقُّ لَا '
    'يَتَنَاقَضُ</span> — because that is the tool, and this is only its first use.')
b += B.aiquiz('The obligation of believing in Allah nearness in al-Aqidah al-Wasitiyyah: the '
              'question that occasioned al-Baqarah 2:186 and how the ayah takes one option and '
              'drops the other, the directing toward munajah in dua, the principle that all of '
              'it is true and truth does not contradict itself, how fi jamii nuutih extends '
              'al-Shura 42:11 to the RELATIONS between attributes, the faulty step of measuring '
              'the Creator against the creation, and that being high while near is of His '
              'particular characteristics')
b += B.further()
b += B.nav('was-l32-fi-al-sama.html', 'The Meaning of His Being "in the Heaven"',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l33')

io.open(os.path.join(B.AQ, 'was-l33-qurb.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'وُجُوبُ الإِيمَانِ بِقُرْبِهِ مِنْ خَلْقِه',
    'The Obligation of Believing in His Nearness to His Creation',
    'Lesson 33 of al-ʿAqīdah al-Wāsiṭiyyah: the question that '
    'occasioned al-Baqarah 2:186 — near, or far? — the principle that the truth does '
    'not contradict itself, the faulty step hidden in “how is He with them while above '
    'them?”, and why being high while near belongs to Allah alone.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الثَّالِثُ وَالثَّلَاثُون', '3',
           'وُجُوبُ الإِيمَانِ بِقُرْبِهِ مِنْ خَلْقِه',
           'The Obligation of Believing in His Nearness to His Creation', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l33-qurb.html')
