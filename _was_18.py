# -*- coding: utf-8 -*-
"""Wasitiyyah L18 -- section 21, first part: the affirmation of speech for
Allah. His truthfulness in speech, His saying, His kalimah, His addressing
Musa, and the two kinds of address -- calling out and conferring privately.
Sharh pp.79-81."""
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
    'Shaykh <strong>مُحَمَّدُ بْنُ صَالِحٍ العُثَيْمِين</strong>, '
    '<em>شَرْحُ العَقِيدَةِ الوَاسِطِيَّة</em> — fuller on the attribute of speech.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Show how %s and %s each affirm speech for Allah.' % (ar('حَدِيثًا'), ar('قِيلًا')),
    'Explain why %s in al-Nisāʾ 4:164 is a %s, and what it rules out.'
    % (ar('تَكْلِيمًا'), ar('مَصْدَرٌ مُؤَكِّد')),
    'Distinguish %s from %s as two kinds of speech.' % (ar('المُنَادَاة'), ar('المُنَاجَاة')),
    'Name the three messengers Allah addressed without an intermediary, and the source for the third.',
])

b += B.heading('٢١ · إِثْبَاتُ الكَلَامِ لِلَّهِ تَعَالَى',
               'Section 21 — The Affirmation of Speech for Allah')
b += B.prose(
    'This is one of the longest sections of the book, and deliberately so. The denial of Allah\'s '
    'speech was the doctrine the Jahmiyyah and the Muʿtazilah fought for hardest, and it is the '
    'issue over which Imām Aḥmad was imprisoned and beaten. So the author does not argue; '
    '<strong>he piles up the texts</strong> — sixteen āyāt, each affirming speech from a '
    'different angle: His truthfulness <em>in</em> speech, His saying, His word, His addressing '
    'Mūsā, His calling out, His conferring privately, and the Qurʾān itself being His speech. '
    'This lesson takes the first ten; the next takes the rest and al-Fawzān\'s summary of the '
    'madhhab of Ahl al-Sunnah.')

b += B.heading('١ · أَصْدَقُ الحَدِيثِ وَأَصْدَقُ القِيل', 'First — Truest in Ḥadīth, Truest in Qīl')
b += B.matn(
    'وَقَوْلُهُ: ﴿وَمَنْ أَصْدَقُ مِنَ اللَّهِ حَدِيثًا﴾، ﴿وَمَنْ أَصْدَقُ مِنَ اللَّهِ '
    'قِيلًا﴾.')
b += B.ayah(
    'وَمَنْ أَصْدَقُ مِنَ اللَّهِ حَدِيثًا',
    '"And who is truer than Allah in speech?"',
    'Sūrat al-Nisāʾ 4:87 · سورة النساء')
b += B.sharh(
    p('<strong>%s</strong> — <em>no one is truer than Him سبحانه; so it is '
      '<strong>%s</strong></em>, a rhetorical question meant as a denial, not an enquiry. And '
      '<strong>%s</strong> — <em>in His ḥadīth and His report, His command, His promise and His '
      'threat.</em>' % (ar('وَمَنْ أَصْدَقُ مِنَ اللَّهِ'), ar('اسْتِفْهَامٌ إِنْكَارِيّ'),
                        ar('حَدِيثًا'))))
b += B.ayah(
    'وَعْدَ اللَّهِ حَقًّا وَمَنْ أَصْدَقُ مِنَ اللَّهِ قِيلًا',
    '"The promise of Allah, in truth — and who is truer than Allah in word?"',
    'Sūrat al-Nisāʾ 4:122 · سورة النساء')
b += B.sharh(
    p('<strong>%s</strong> — <em>a verbal noun of %s, like %s; that is: no one is truer in '
      'speech than Allah عز وجل.</em>' % (ar('القِيل'), ar('قَالَ'), ar('القَوْل'))) +
    p('<strong>And the shāhid from the two noble āyāt: that in them is the affirming of '
      '<em>ḥadīth</em> and <em>qīl</em> for Allah سبحانه — so in them is the affirming of speech '
      'for Him.</strong>') +
    p('Follow the shape of that argument, because it is the one the whole section repeats. '
      'Neither āyah sets out to prove that Allah speaks; both are making a point about '
      '<strong>truthfulness</strong>. But truthfulness is a property <em>of speech</em>. '
      '<strong>You cannot be the truest speaker and not be a speaker</strong> — so the attribute '
      'arrives inside a statement about something else, which is why it cannot be argued away '
      'without dismantling the āyah.'))

b += B.heading('٢ · إِثْبَاتُ القَوْلِ وَالكَلِمَة', 'Second — His Saying and His Word')
b += B.matn(
    'وَقَوْلُهُ: ﴿وَإِذْ قَالَ اللَّهُ يَا عِيسَى ابْنَ مَرْيَمَ﴾، وَقَوْلُهُ: ﴿وَتَمَّتْ '
    'كَلِمَتُ رَبِّكَ صِدْقًا وَعَدْلًا﴾.')
b += B.ayah(
    'وَإِذْ قَالَ اللَّهُ يَا عِيسَى ابْنَ مَرْيَمَ أَأَنْتَ قُلْتَ لِلنَّاسِ اتَّخِذُونِي '
    'وَأُمِّيَ إِلَهَيْنِ مِنْ دُونِ اللَّهِ',
    '"And when Allah will say: O ʿĪsā son of Maryam, did you say to the people: take me and my '
    'mother as two gods besides Allah?"',
    'Sūrat al-Māʾidah 5:116 · سورة المائدة')
b += B.sharh(
    p('<strong>%s</strong> — the implied verb is <em>recall</em>. And on the timing, '
      '<strong>the majority of the mufassirūn held that this saying from Him سبحانه '
      '<em>will be</em> on the Day of Rising</strong>, <em>and it is a rebuke to those of the '
      'Christians who worshipped the Messiah and his mother.</em>'
      % ar('وَإِذْ قَالَ اللَّهُ')) +
    p('<em>And it is like the two preceding āyāt: in it is the affirming of saying for Allah '
      'تعالى, <strong>and that He says when He wills</strong>.</em>') +
    p('That last clause is doing real work, and it will be the hinge of the next lesson. The āyah '
      'is <em>future</em>. A saying that has not happened yet, and will happen on a named day, is '
      'a saying <strong>tied to His will</strong> — which is precisely why Ahl al-Sunnah call '
      'speech an attribute of His <em>actions</em> as well as of His essence.'))
b += B.ayah(
    'وَتَمَّتْ كَلِمَتُ رَبِّكَ صِدْقًا وَعَدْلًا لَا مُبَدِّلَ لِكَلِمَاتِهِ',
    '"And the word of your Lord has been completed in truth and justice. There is no changer of '
    'His words."',
    'Sūrat al-Anʿām 6:115 · سورة الأنعام')
b += B.sharh(
    p('<strong>What is intended by %s is His speech سبحانه.</strong> And then the two accusatives '
      'are divided precisely: <strong>%s</strong> — <em>in His reports</em> — and '
      '<strong>%s</strong> — <em>in His rulings</em>. Grammatically, <em>%s are manṣūb as '
      '%s</em>, specifying in what respect the completion holds.'
      % (ar('الكَلِمَة'), ar('صِدْقًا'), ar('وَعَدْلًا'), ar('صِدْقًا وَعَدْلًا'),
         ar('التَّمْيِيز'))) +
    p('That division is worth holding on to as a rule for reading the Qurʾān: '
      '<strong>where it reports, it is true; where it rules, it is just.</strong> Those are the '
      'only two things a revelation does, and the āyah claims perfection in both. '
      '<em>And in the āyah is the affirming of speech for Allah تعالى.</em>'))

b += B.heading('٣ · تَكْلِيمُ مُوسَى عَلَيْهِ السَّلَام', 'Third — His Addressing Mūsā')
b += B.matn(
    'وَقَوْلُهُ: ﴿وَكَلَّمَ اللَّهُ مُوسَى تَكْلِيمًا﴾، ﴿مِنْهُمْ مَنْ كَلَّمَ اللَّهُ﴾، '
    '﴿وَلَمَّا جَاءَ مُوسَى لِمِيقَاتِنَا وَكَلَّمَهُ رَبُّهُ﴾.')
b += B.ayah(
    'وَكَلَّمَ اللَّهُ مُوسَى تَكْلِيمًا',
    '"And Allah spoke to Mūsā with a direct speaking."',
    'Sūrat al-Nisāʾ 4:164 · سورة النساء')
b += B.sharh(
    p('<em>This is an ennobling of Mūsā عليه السلام, in that Allah spoke to him — that is: '
      '<strong>He made him hear His speech</strong>; and this is why he is called '
      '<strong>%s</strong>.</em>' % ar('الكَلِيم')) +
    p('And now the single most quoted grammatical point in this whole subject. '
      '<strong>%s is %s</strong> — <em>a verbal noun brought for emphasis, '
      '<strong>to repel the speaking being figurative</strong>.</em>'
      % (ar('تَكْلِيمًا'), ar('مَصْدَرٌ مُؤَكِّد'))) +
    p('This is worth being slow about. In Arabic, a verb reinforced by its own maṣdar '
      '(%s) is the construction that forecloses metaphor. One may say «the wall spoke to me» '
      'loosely; one does not say «the wall spoke to me <em>with a speaking</em>». '
      '<strong>So the āyah does not merely say that Allah spoke to Mūsā — it says so in the one '
      'grammatical form Arabic has for ruling out that the words were meant loosely.</strong> '
      'The taʾwīl was blocked before it was ever proposed. <em>So in the āyah is the affirming of '
      'speech for Allah, and that He spoke to Mūsā عليه السلام.</em>'
      % ar('كَلَّمَ … تَكْلِيمًا')))
b += B.ayah(
    'تِلْكَ الرُّسُلُ فَضَّلْنَا بَعْضَهُمْ عَلَى بَعْضٍ مِنْهُمْ مَنْ كَلَّمَ اللَّهُ '
    'وَرَفَعَ بَعْضَهُمْ دَرَجَاتٍ',
    '"Those messengers — We favoured some of them over others. Among them is he to whom Allah '
    'spoke, and some of them He raised in degrees."',
    'Sūrat al-Baqarah 2:253 · سورة البقرة')
b += B.sharh(
    p('<strong>%s</strong> — <em>of the messengers عليهم الصلاة والسلام</em> — '
      '<strong>%s</strong> — <em>He made him hear His speech <strong>without an '
      'intermediary</strong>.</em>' % (ar('مِنْهُمْ'), ar('مَنْ كَلَّمَ اللَّهُ'))) +
    p('And al-Fawzān names them: <em>meaning <strong>Mūsā and Muḥammad</strong> عليهما الصلاة '
      'والسلام; <strong>and likewise Ādam</strong>, as has come in the ḥadīth in '
      '<strong>صَحِيحُ ابْنِ حِبَّان</strong>.</em> <em>So in the āyah is the affirming of speech '
      'for Allah تعالى, and that He spoke to some of the messengers.</em>') +
    p('Note the care in the attribution. al-Fawzān does not leave the third name resting on '
      'nothing; he tells you which collection carries it. That is the standard this track holds '
      'itself to, and it is why the <em>Further reading</em> below names the sharḥ rather than '
      'asking you to take the lesson\'s word for it.'))
b += B.ayah(
    'وَلَمَّا جَاءَ مُوسَى لِمِيقَاتِنَا وَكَلَّمَهُ رَبُّهُ',
    '"And when Mūsā came to Our appointed meeting and his Lord spoke to him."',
    'Sūrat al-Aʿrāf 7:143 · سورة الأعراف')
b += B.sharh(
    p('<strong>%s</strong> — <em>his coming took place at the time Allah had appointed with him '
      'for it</em>. <strong>%s</strong> — <em>He made him hear His speech '
      '<strong>without an intermediary</strong>.</em>'
      % (ar('وَلَمَّا جَاءَ مُوسَى لِمِيقَاتِنَا'), ar('وَكَلَّمَهُ رَبُّهُ'))) +
    p('al-Fawzān gathers the three: <em>so the āyāt contain the affirming of speech for Allah '
      'تعالى, <strong>and that He speaks whenever He wills</strong> سبحانه, and that He spoke to '
      'Mūsā عليه السلام without an intermediary.</em>'))

b += B.heading('٤ · النِّدَاءُ وَالمُنَاجَاة', 'Fourth — Calling Out and Conferring Privately')
b += B.matn(
    'وَقَوْلُهُ: ﴿وَنَادَيْنَاهُ مِنْ جَانِبِ الطُّورِ الْأَيْمَنِ وَقَرَّبْنَاهُ نَجِيًّا﴾، '
    '﴿وَإِذْ نَادَى رَبُّكَ مُوسَى أَنِ ائْتِ الْقَوْمَ الظَّالِمِينَ﴾، ﴿وَنَادَاهُمَا '
    'رَبُّهُمَا أَلَمْ أَنْهَكُمَا عَنْ تِلْكُمَا الشَّجَرَةِ﴾، ﴿وَيَوْمَ يُنَادِيهِمْ '
    'فَيَقُولُ مَاذَا أَجَبْتُمُ الْمُرْسَلِينَ﴾.')
b += B.ayah(
    'وَنَادَيْنَاهُ مِنْ جَانِبِ الطُّورِ الْأَيْمَنِ وَقَرَّبْنَاهُ نَجِيًّا',
    '"And We called him from the right side of the Mount, and We brought him near, conferring '
    'privately."',
    'Sūrat Maryam 19:52 · سورة مريم')
b += B.sharh(
    p('<strong>%s</strong> — <em>Allah تعالى called out to Mūsā عليه السلام; and '
      '<strong>%s is the raised voice</strong>.</em> <strong>%s</strong> — <em>a mountain between '
      'Egypt and Madyan.</em>' % (ar('وَنَادَيْنَاهُ'), ar('النِّدَاء'), ar('الطُّور'))) +
    p('And then a precision that shows how carefully the mufassirūn read: <strong>%s</strong> '
      'means <em>the right side <strong>of Mūsā</strong> when he went seeking a burning brand '
      'from the fire he had seen</em> — <strong>and what is intended is not the right of the '
      'mountain itself, for mountains have no right and no left.</strong>'
      % ar('الأَيْمَن')) +
    p('<strong>%s</strong> — <em>We drew him near until We spoke to him</em>; '
      '<strong>%s</strong> — <em>conferring in secret</em>. And <em>al-munājāh is the opposite of '
      'al-munādāh</em>.' % (ar('وَقَرَّبْنَاهُ'), ar('نَجِيًّا'))) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:.2rem 0 .7rem">'
    '<tr><td style="padding:.55rem .8rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>المُنَادَاة</strong></td>'
    '<td style="padding:.55rem .8rem;border:1px solid var(--line)">with a '
    '<strong>raised</strong> voice</td></tr>'
    '<tr><td style="padding:.55rem .8rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>المُنَاجَاة</strong></td>'
    '<td style="padding:.55rem .8rem;border:1px solid var(--line)">with a voice that is '
    '<strong>not raised</strong></td></tr>'
    '</table></div>' +
    p('<em>And in the noble āyah is the affirming of speech for Allah تعالى, and that He calls '
      'out and confers privately — <strong>and these are two kinds of speech</strong>.</em> The '
      'single āyah contains both, which is why it is the one the author picked.'))
b += B.ayah(
    'وَإِذْ نَادَى رَبُّكَ مُوسَى أَنِ ائْتِ الْقَوْمَ الظَّالِمِينَ',
    '"And when your Lord called Mūsā: go to the wrongdoing people."',
    'Sūrat al-Shuʿarāʾ 26:10 · سورة الشعراء')
b += B.sharh(
    p('<strong>%s</strong> — the implied verb is <em>recite</em>, or <em>recall</em>. And '
      '<strong>%s is the calling</strong>. The %s of %s may be '
      '<strong>explanatory</strong> or <strong>maṣdariyyah</strong> — either way the sense is: '
      '<em>go to…</em>' % (ar('وَإِذْ'), ar('النِّدَاء'), ar('أَنْ'), ar('أَنِ ائْتِ'))) +
    p('And why were they described as <strong>%s</strong>? <em>Because they joined together '
      '<strong>the disbelief by which they wronged themselves</strong> and '
      '<strong>the acts of disobedience by which they wronged others</strong> — such as their '
      'enslaving of the Children of Israel and the slaughtering of their sons.</em>'
      % ar('الظَّالِمِينَ')) +
    p('A definition of ẓulm in two directions, dropped in passing: it runs inward before it runs '
      'outward. <em>And in the noble āyah is the affirming of speech for Allah تعالى, and that He '
      'calls whom He wills of His servants and makes him hear His speech.</em>'))
b += B.ayah(
    'وَنَادَاهُمَا رَبُّهُمَا أَلَمْ أَنْهَكُمَا عَنْ تِلْكُمَا الشَّجَرَةِ',
    '"And their Lord called out to them: did I not forbid you both that tree?"',
    'Sūrat al-Aʿrāf 7:22 · سورة الأعراف')
b += B.prose(
    '<em>Allah تعالى called out to Ādam and Ḥawwāʾ عليهما السلام, saying to them: '
    '«did I not forbid you both that tree» — that is, from eating of it. '
    '<strong>And this is a reproach from Allah to them both, and a rebuke, since they did not '
    'take care against what He had warned them against.</strong> And in the noble āyah is the '
    'affirming of speech for Allah تعالى, and of the calling out from Him to Ādam and his wife.</em>')
b += B.ayah(
    'وَيَوْمَ يُنَادِيهِمْ فَيَقُولُ مَاذَا أَجَبْتُمُ الْمُرْسَلِينَ',
    '"And on the Day He will call out to them and say: what answer did you give the messengers?"',
    'Sūrat al-Qaṣaṣ 28:65 · سورة القصص')
b += B.sharh(
    p('<em>Allah سبحانه will call out to these mushrikūn on the Day of Rising, '
      '<strong>and will say</strong> to them: %s — that is: <strong>what was your answer to those '
      'of the prophets who were sent to you, when they conveyed My messages to you?</strong></em>'
      % ar('مَاذَا أَجَبْتُمُ الْمُرْسَلِينَ')) +
    p('<strong>And the shāhid from the āyah: the affirming of speech for Allah, and that He '
      'speaks when He wills.</strong>') +
    p('Four āyāt of calling out, and look at the range of who is called: Mūsā at the Mount, Ādam '
      'and Ḥawwāʾ in the Garden, and the mushrikūn on the Day of Rising. '
      '<strong>Past, primordial and future.</strong> The attribute is not confined to one event '
      'that might be explained away as a special case — and each one is a <em>speaking</em>, with '
      'a question in it that expects an answer.'))

b += B.vocab([
    ('القِيل', 'al-qīl', 'word, utterance',
     'A verbal noun of قَالَ, like القَوْل — none is truer in it than Allah'),
    ('اسْتِفْهَامٌ إِنْكَارِيّ', 'istifhām inkārī',
     'a question meant as denial',
     '"Who is truer than Allah?" is not asking — it is denying there is one'),
    ('مَصْدَرٌ مُؤَكِّد', 'maṣdar muʾakkid', 'an emphatic verbal noun',
     'تَكْلِيمًا — brought to repel the speaking being figurative'),
    ('الكَلِيم', 'al-kalīm', 'the one addressed',
     'Mūsā’s title, because Allah made him hear His speech'),
    ('التَّمْيِيز', 'al-tamyīz', 'specification',
     'صِدْقًا وَعَدْلًا — true in His reports, just in His rulings'),
    ('المُنَادَاة', 'al-munādāh', 'calling out',
     'Speech with a raised voice'),
    ('المُنَاجَاة', 'al-munājāh', 'conferring privately',
     'Speech with a voice not raised — the opposite of al-munādāh'),
    ('الطُّور', 'al-ṭūr', 'the Mount',
     'A mountain between Egypt and Madyan'),
])
b += B.mcq('ws-l18', [
    ('How do %s and %s affirm speech for Allah?' % (ar('حَدِيثًا'), ar('قِيلًا')),
     ['By naming the Qurʾān directly',
      'Because truthfulness is a property of speech — the truest speaker must be a speaker',
      'Because both words mean "command"',
      'Because they are addressed to the Prophet ﷺ'], 1),
    ('What is %s in al-Nisāʾ 4:164, and what does it do?' % ar('تَكْلِيمًا'),
     ['A ḥāl, describing Mūsā’s state',
      'An emphatic verbal noun, brought to repel the speaking being figurative',
      'A tamyīz, specifying the manner', 'A badal for the name of Mūsā'], 1),
    ('How are %s divided in al-Anʿām 6:115?' % ar('صِدْقًا وَعَدْلًا'),
     ['Truth in the past, justice in the future',
      'True in His reports, just in His rulings',
      'Truth for the believers, justice for the disbelievers',
      'Both refer only to the Torah'], 1),
    ('Which messengers does al-Fawzān name as spoken to without an intermediary?',
     ['Mūsā alone',
      'Mūsā and Muḥammad ﷺ, and likewise Ādam — the last per a hadith in Ṣaḥīḥ Ibn Ḥibbān',
      'Mūsā and ʿĪsā', 'All of the messengers without exception'], 1),
    ('What is the difference between %s and %s?' % (ar('المُنَادَاة'), ar('المُنَاجَاة')),
     ['One is to prophets, the other to angels',
      'Munādāh is with a raised voice; munājāh with a voice not raised',
      'One is in this world, the other in the Hereafter',
      'One is speech, the other is inspiration'], 1),
    ('What does %s refer to in Sūrat Maryam 19:52?' % ar('الأَيْمَن'),
     ['The right side of the mountain',
      'The right side of Mūsā as he approached the fire — mountains have no right or left',
      'The more blessed of two mountains', 'The right hand of the angel'], 1),
    ('Why were Pharaoh’s people called %s?' % ar('الظَّالِمِينَ'),
     ['Because they rejected Mūsā only',
      'Because they joined the disbelief by which they wronged themselves to the disobedience by '
      'which they wronged others',
      'Because they were tyrants in trade', 'Because they worshipped the Nile'], 1),
])
b += B.tf('ws-l18-tf', [
    ('«وَمَنْ أَصْدَقُ مِنَ اللَّهِ» اسْتِفْهَامٌ إِنْكَارِيٌّ.',
     '"Who is truer than Allah" is a rhetorical question meant as a denial.', True),
    ('«تَكْلِيمًا» تُفِيدُ أَنَّ الكَلَامَ مَجَازٌ.',
     'The word taklīman indicates that the speaking is figurative.', False),
    ('المُنَاجَاةُ ضِدُّ المُنَادَاةِ.', 'Munājāh is the opposite of munādāh.', True),
    ('قَوْلُ اللهِ لِعِيسَى فِي المَائِدَةِ يَكُونُ يَوْمَ القِيَامَةِ عِنْدَ جُمْهُورِ المُفَسِّرِينَ.',
     'The majority of mufassirūn held that Allah’s address to ʿĪsā in al-Māʾidah will be on '
     'the Day of Rising.', True),
])
b += B.memorize(
    'وَكَلَّمَ اللَّهُ مُوسَى تَكْلِيمًا',
    'Four words that took an imām to prison. Memorize the grammar with the āyah: the verb is '
    'reinforced by its own maṣdar, and that is the one construction in Arabic which says — '
    'plainly, in advance — that the words are not to be read loosely.')
b += B.aiquiz('The affirmation of speech for Allah in al-Aqidah al-Wasitiyyah: how hadithan and '
              'qilan affirm it through truthfulness, why taklimwith the emphatic masdar rules out '
              'a figurative reading, the division of sidqan wa-adlan into reports and rulings, '
              'the messengers addressed without an intermediary, and munadah versus munajah as '
              'two kinds of speech')
b += B.further()
b += B.nav('was-l17-maiyyah.html', 'The Maʿiyyah: General and Particular',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l18')

io.open(os.path.join(B.AQ, 'was-l18-kalam-allah.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'إِثْبَاتُ الكَلَامِ لِلَّهِ تَعَالَى',
    'The Affirmation of Speech for Allah',
    'Lesson 18 of al-ʿAqīdah al-Wāsiṭiyyah: how truthfulness in '
    'speech affirms speech, why the emphatic verbal noun in <em>kallamaʾLlāhu '
    'Mūsā taklīman</em> forecloses a figurative reading, the messengers addressed '
    'without an intermediary, and calling out versus conferring privately as two kinds of speech.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الثَّامِنَ عَشَر', '3',
           'إِثْبَاتُ الكَلَامِ لِلَّهِ تَعَالَى',
           'The Affirmation of Speech for Allah', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l18-kalam-allah.html')
