# -*- coding: utf-8 -*-
"""Wasitiyyah L19 -- section 21, second part: the Qur'an itself is the speech of
Allah, no one may change His words, and al-Fawzan's statement of the madhhab of
Ahl al-Sunnah on the attribute of speech. Sharh pp.81-83."""
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
    '<em>شَرْحُ العَقِيدَةِ الوَاسِطِيَّة</em> — fuller on the dhātī/fiʿlī distinction.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Give the āyah that proves the recited Qurʾān is itself %s.' % ar('كَلَامُ اللهِ'),
    'Define %s as al-Fawzān defines it, and say what the Jews did with the Torah.'
    % ar('التَّحْرِيف'),
    'State the madhhab of Ahl al-Sunnah on speech — both of the two kinds of attribute it is.',
    'Give the two reasons al-Fawzān offers for why Allah has never ceased to be a Speaker.',
])

b += B.heading('٥ · القُرْآنُ كَلَامُ الله', 'Fifth — The Qurʾān Is the Speech of Allah')
b += B.prose(
    'Lesson 18 established that Allah speaks. This part of the section establishes '
    '<strong>what His speech is</strong> — that the Book being recited is itself His speech, not '
    'a created report about it — and then that <strong>no one may alter it</strong>, with the '
    'Jews and the Bedouin who stayed behind as the two worked examples.')
b += B.matn(
    'وَقَوْلُهُ: ﴿وَإِنْ أَحَدٌ مِنَ الْمُشْرِكِينَ اسْتَجَارَكَ فَأَجِرْهُ حَتَّى يَسْمَعَ '
    'كَلَامَ اللَّهِ﴾، ﴿وَقَدْ كَانَ فَرِيقٌ مِنْهُمْ يَسْمَعُونَ كَلَامَ اللَّهِ ثُمَّ '
    'يُحَرِّفُونَهُ مِنْ بَعْدِ مَا عَقَلُوهُ وَهُمْ يَعْلَمُونَ﴾، ﴿يُرِيدُونَ أَنْ '
    'يُبَدِّلُوا كَلَامَ اللَّهِ قُلْ لَنْ تَتَّبِعُونَا كَذَلِكُمْ قَالَ اللَّهُ مِنْ '
    'قَبْلُ﴾، ﴿وَاتْلُ مَا أُوحِيَ إِلَيْكَ مِنْ كِتَابِ رَبِّكَ لَا مُبَدِّلَ '
    'لِكَلِمَاتِهِ﴾، ﴿إِنَّ هَذَا الْقُرْآنَ يَقُصُّ عَلَى بَنِي إِسْرَائِيلَ أَكْثَرَ '
    'الَّذِي هُمْ فِيهِ يَخْتَلِفُونَ﴾.')
b += B.ayah(
    'وَإِنْ أَحَدٌ مِنَ الْمُشْرِكِينَ اسْتَجَارَكَ فَأَجِرْهُ حَتَّى يَسْمَعَ كَلَامَ اللَّهِ '
    'ثُمَّ أَبْلِغْهُ مَأْمَنَهُ',
    '"And if any one of the mushrikūn seeks your protection, then grant him protection until he '
    'hears the speech of Allah; then convey him to his place of safety."',
    'Sūrat al-Tawbah 9:6 · سورة التوبة')
b += B.sharh(
    p('<strong>%s</strong> — <em>those whom you were commanded to fight</em> — '
      '<strong>%s</strong> — <em>O Muḥammad, that is: he sought your protection, your shelter and '
      'your security</em> — <strong>%s</strong> — <em>be for him a protector and a guarantor of '
      'safety</em> — <strong>%s</strong> — <em>from you, and ponders it, and comes to stand upon '
      'the reality of what you are calling to.</em>'
      % (ar('مِنَ الْمُشْرِكِينَ'), ar('اسْتَجَارَكَ'), ar('فَأَجِرْهُ'),
         ar('حَتَّى يَسْمَعَ كَلَامَ اللَّهِ'))) +
    p('<strong>And the shāhid from the āyah: that in it is the affirming of speech for Allah '
      'تعالى, and that <em>what is recited</em> is the speech of Allah.</strong>') +
    p('That is the decisive point, and the āyah carries it almost incidentally. The enemy '
      'combatant is given safe passage <em>for the purpose of hearing</em> — and what he is to '
      'hear is named: %s. He will hear it from a human reciter, in Arabic, with his ears. '
      '<strong>And the Qurʾān calls that the speech of Allah.</strong>' % ar('كَلَامَ اللَّهِ')) +
    p('There is something else in the ruling worth noticing. The protection is not withdrawn once '
      'he has heard and refused; <strong>%s</strong> — he is escorted back to safety. '
      '<em>Hearing is not made a trap.</em>' % ar('ثُمَّ أَبْلِغْهُ مَأْمَنَهُ')))
b += B.ayah(
    'وَقَدْ كَانَ فَرِيقٌ مِنْهُمْ يَسْمَعُونَ كَلَامَ اللَّهِ ثُمَّ يُحَرِّفُونَهُ مِنْ '
    'بَعْدِ مَا عَقَلُوهُ وَهُمْ يَعْلَمُونَ',
    '"And a group of them used to hear the speech of Allah, then distort it after they had '
    'understood it — and they knew."',
    'Sūrat al-Baqarah 2:75 · سورة البقرة')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>the Jews</strong></em>. And a point of language: '
      '<strong>%s is a collective noun which has no singular from its own root.</strong>'
      % (ar('فَرِيقٌ مِنْهُمْ'), ar('الفَرِيق'))) +
    p('<strong>%s</strong> — <em>that is: <strong>the Torah</strong></em>. '
      '<strong>%s</strong> — <em>they interpret it upon other than its interpretation</em> — '
      'which is al-Fawzān\'s working definition of taḥrīf and worth having exactly: '
      '<strong>not the deleting of a text, but the reading of it against its meaning.</strong>'
      % (ar('يَسْمَعُونَ كَلَامَ اللَّهِ'), ar('ثُمَّ يُحَرِّفُونَهُ'))) +
    p('<strong>%s</strong> — <em>that is: after they had understood it</em>; '
      '<em>and with this they oppose it <strong>with open eyes</strong></em>. '
      '<strong>%s</strong> — <em>that they are in error in what they went to, of distorting it '
      'and reinterpreting it.</em>'
      % (ar('مِنْ بَعْدِ مَا عَقَلُوهُ'), ar('وَهُمْ يَعْلَمُونَ'))) +
    p('Read the sequence: <em>they heard, they understood, then they distorted, and they knew they '
      'were doing it.</em> Taḥrīf in this āyah is not a mistake made by the ignorant. '
      '<strong>It is comprehension followed by evasion</strong> — which is exactly why the author '
      'quotes it in a book written against people who reinterpret texts they understand '
      'perfectly well.') +
    p('<strong>And the shāhid: in it is the affirming of speech for Allah تعالى, and that the '
      'Torah is from His speech تعالى, and that the Jews distorted it, and altered and substituted '
      'in it.</strong>'))
b += B.ayah(
    'يُرِيدُونَ أَنْ يُبَدِّلُوا كَلَامَ اللَّهِ قُلْ لَنْ تَتَّبِعُونَا كَذَلِكُمْ قَالَ '
    'اللَّهُ مِنْ قَبْلُ',
    '"They wish to change the speech of Allah. Say: you shall not follow us. Thus did Allah say '
    'beforehand."',
    'Sūrat al-Fatḥ 48:15 · سورة الفتح')
b += B.sharh(
    p('<strong>%s</strong> — <em>the ones left behind, from among the Bedouin, who chose to '
      'remain with their families and their occupations and abandoned setting out with the '
      'Messenger of Allah &#65018; when he went out in the year of al-Ḥudaybiyah.</em>'
      % ar('يُرِيدُونَ')) +
    p('<strong>%s</strong> — <em>they would alter the speech of Allah by which Allah had promised '
      '<strong>the people of al-Ḥudaybiyah specifically</strong> the spoils of Khaybar.</em> '
      'So the «changing» at issue is concrete: a promise was made to a named body of people, and '
      'those who had stayed behind wanted its terms rewritten in their favour.'
      % ar('أَنْ يُبَدِّلُوا كَلَامَ اللَّهِ')) +
    p('<strong>%s</strong> — and the grammar matters: <em>this is a negation carrying the meaning '
      'of a prohibition</em> — that is, <strong>do not follow us</strong>. '
      '<strong>%s</strong> — <em>Allah promised the people of al-Ḥudaybiyah that the spoils of '
      'Khaybar were theirs specifically.</em>'
      % (ar('قُلْ لَنْ تَتَّبِعُونَا'), ar('كَذَلِكُمْ قَالَ اللَّهُ مِنْ قَبْلُ'))) +
    p('<strong>And the shāhid: in it is the affirming of speech for Allah and the affirming of '
      'saying for Him; and that Allah سبحانه speaks and says when He wills, if He wills; and that '
      '<em>it is not permitted to alter His speech</em> سبحانه — rather it is obligatory to act '
      'by it and to follow it.</strong>'))
b += B.ayah(
    'وَاتْلُ مَا أُوحِيَ إِلَيْكَ مِنْ كِتَابِ رَبِّكَ لَا مُبَدِّلَ لِكَلِمَاتِهِ',
    '"And recite what has been revealed to you of the Book of your Lord. There is no changer of '
    'His words."',
    'Sūrat al-Kahf 18:27 · سورة الكهف')
b += B.sharh(
    p('<em>Allah commanded His Prophet to <strong>keep constant</strong> upon the recitation of '
      'the Book revealed to him.</em> And on the word itself: <strong>%s is informing with '
      'speed and concealment</strong> — <em>and it has modes which are mentioned in the books of '
      'the principles of tafsīr.</em>' % ar('الوَحْي')) +
    p('<strong>%s</strong> is a clarification of that which was revealed to him. '
      '<strong>%s</strong> — <em>no alterer of them, and no distorter, and no remover.</em>'
      % (ar('مِنْ كِتَابِ رَبِّكَ'), ar('لَا مُبَدِّلَ لِكَلِمَاتِهِ'))) +
    p('<strong>And the shāhid from the āyah: the affirming of <em>the words</em> for Allah '
      'تعالى.</strong> Set it beside the previous āyah and the pair is complete: men '
      '<em>wish</em> to change His speech (al-Fatḥ 48:15), and there <em>is</em> no changer of it '
      '(here). The wish is real; the capacity is not.'))
b += B.ayah(
    'إِنَّ هَذَا الْقُرْآنَ يَقُصُّ عَلَى بَنِي إِسْرَائِيلَ أَكْثَرَ الَّذِي هُمْ فِيهِ '
    'يَخْتَلِفُونَ',
    '"Indeed this Qurʾān relates to the Children of Israel most of that over which they '
    'differ."',
    'Sūrat al-Naml 27:76 · سورة النمل')
b += B.sharh(
    p('<strong>%s</strong> — <em>and they are the bearers of the Torah and the Gospel</em>. '
      '<strong>%s</strong> — <em>as their differing over ʿĪsā</em>: '
      '<strong>the Jews fabricated against him, and the Christians went to excess regarding '
      'him.</strong>' % (ar('بَنِي إِسْرَائِيلَ'), ar('أَكْثَرَ الَّذِي هُمْ فِيهِ يَخْتَلِفُونَ'))) +
    p('<em>So the Qurʾān came with <strong>%s</strong> — the middle, true statement: '
      '<strong>that he is the servant of Allah, and His messenger, and His word which He cast to '
      'Maryam, and a spirit from Him.</strong></em>' % ar('القَوْلِ الوَسَطِ الحَقِّ')) +
    p('There is the pattern of the opening lessons again, arriving from a new direction. Two '
      'parties erred in opposite directions on one man, and the truth was neither of their '
      'positions — it was the middle. The <em>wasaṭ</em> of this book\'s title is not a '
      'temperament; it is a method.') +
    p('<strong>And the shāhid: that in it is the affirming that the Qurʾān is the speech of Allah '
      'تعالى</strong>, <em>because of what it contains of encompassing the previous books and of '
      'judging with equity in the disputes between the sects of the People of the Book — '
      '<strong>and this could not be from anyone except Allah.</strong></em>') +
    p('That is an argument from the <em>content</em>, not from a claim. A book that settles, '
      'justly, the internal disputes of two older scriptural communities — disputes its reciter '
      'had no access to — is evidence about its own origin.'))

b += B.heading('مَذْهَبُ أَهْلِ السُّنَّةِ فِي الكَلَام',
               'The Madhhab of Ahl al-Sunnah on the Attribute of Speech')
b += B.prose(
    'al-Fawzān now gathers the whole section. <em>And what is derived from the totality of the '
    'āyāt the author brought is: <strong>the affirming of speech for Allah.</strong> And the '
    'madhhab of Ahl al-Sunnah wa-l-Jamāʿah is the affirming of what the Book and the Sunnah have '
    'indicated — that <strong>Allah is described with speech.</strong></em>')
b += B.sharh(
    p('Then the classification, and this is the part to learn precisely, because it is where most '
      'people go wrong by choosing one half:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>مِنْ صِفَاتِهِ الذَّاتِيَّة</strong></td>'
    '<td style="padding:.6rem .75rem;border:1px solid var(--line)">— <em>because it subsists '
    'with Him and He is described by it.</em> Speech belongs to Him as He is, not as something '
    'added to Him.</td></tr>'
    '<tr><td style="padding:.6rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>وَمِنْ صِفَاتِهِ الفِعْلِيَّة</strong></td>'
    '<td style="padding:.6rem .75rem;border:1px solid var(--line)">— <em>occurring by His '
    'will and His power.</em> <strong>So He speaks if He wills, how He wills, with what He '
    'wills.</strong></td></tr>'
    '</table></div>' +
    p('<strong>Both</strong>, not one. This is the resolution of a dispute that split the schools. '
      'Make speech purely <em>dhātī</em> and you must say Allah speaks eternally and necessarily, '
      'with no choice in it — and then the āyāt in which He speaks to Mūsā at an appointed time, '
      'or speaks to ʿĪsā on the Day of Rising, have to be explained away. Make it purely '
      '<em>fiʿlī</em> and you have said there was a time when He was not a Speaker, '
      'which is a deficiency. <strong>Ahl al-Sunnah affirm both and need explain nothing '
      'away.</strong>') +
    p('Hence the formula: <strong>%s</strong> — <em>and He has never ceased to be Speaking and '
      'will never cease to be Speaking.</em> And al-Fawzān gives two reasons for it:'
      % ar('وَلَمْ يَزَلْ مُتَكَلِّمًا وَلَا يَزَالُ مُتَكَلِّمًا')) +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.93rem">'
    '<p style="margin:0 0 .6rem"><strong>الأَوَّل ·</strong> <em>Because He has never ceased '
    'and will never cease being <strong>Perfect</strong> — and speech is of the attributes '
    'of perfection.</em> The argument from Lesson 16 again: an attribute of perfection cannot '
    'have been absent from the Perfect.</p>'
    '<p style="margin:0"><strong>الثَّانِي ·</strong> <em>And because <strong>Allah '
    'described Himself with it, and His Messenger described Him with it.</strong></em> The '
    'tawqīfī principle: the subject is received, not reasoned out.</p></div>' +
    p('Two reasons, and notice they are of two different kinds — one rational, one transmitted. '
      'That is the signature of this book\'s method, and the same pairing you met in Lesson 16 on '
      'al-ʿuluww.') +
    p('<em>And the mention of the madhhab of the opponents in this question, along with the '
      'refutation of it, is to come, إِنْ شَاءَ اللهُ.</em> The author keeps his polemic for '
      'later and his texts for now — which is worth imitating.'))

b += B.vocab([
    ('التَّحْرِيف', 'al-taḥrīf', 'distortion',
     'To interpret a text upon other than its interpretation — after understanding it'),
    ('الفَرِيق', 'al-farīq', 'a group',
     'A collective noun with no singular from its own root'),
    ('التَّبْدِيل', 'al-tabdīl', 'alteration, substitution',
     'لَا مُبَدِّلَ لِكَلِمَاتِهِ — men wish it; none can do it'),
    ('الوَحْي', 'al-waḥy', 'revelation',
     'Informing with speed and concealment'),
    ('القَوْلُ الوَسَط', 'al-qawl al-wasaṭ', 'the middle statement',
     'On ʿīsā: a servant of Allah and His messenger — against both excesses'),
    ('الصِّفَاتُ الذَّاتِيَّة', 'al-ṣifāt al-dhātiyyah',
     'the attributes of the Essence',
     'Speech is one — because it subsists with Him'),
    ('الصِّفَاتُ الفِعْلِيَّة', 'al-ṣifāt al-fiʿliyyah',
     'the attributes of the Actions',
     'Speech is also one — occurring by His will and power'),
])
b += B.mcq('ws-l19', [
    ('How does al-Tawbah 9:6 prove the recited Qurʾān is the speech of Allah?',
     ['By calling it a revelation',
      'Because the mushrik is granted protection in order to <em>hear</em> — and what he hears '
      'from a human reciter is named "the speech of Allah"',
      'Because it forbids fighting outright',
      'Because it mentions his place of safety'], 1),
    ('How does al-Fawzān define the taḥrīf in al-Baqarah 2:75?',
     ['Deleting verses from the text',
      'Interpreting the text upon other than its interpretation — after having understood it',
      'Mispronouncing the words', 'Translating it into another language'], 1),
    ('What specifically did those left behind in al-Fatḥ 48:15 wish to change?',
     ['The direction of the qiblah',
      'Allah’s promise of the spoils of Khaybar to the people of al-Ḥudaybiyah specifically',
      'The terms of the treaty itself', 'The number of those permitted to fight'], 1),
    ('What is the grammatical point in %s?' % ar('قُلْ لَنْ تَتَّبِعُونَا'),
     ['It is a question meant as denial',
      'It is a negation carrying the meaning of a prohibition: do not follow us',
      'It is an emphatic verbal noun', 'It is a tamyīz'], 1),
    ('What was the middle statement the Qurʾān brought on ʿĪsā?',
     ['That he was a prophet but not a messenger',
      'That he is the servant of Allah, His messenger, and His word cast to Maryam, and a spirit '
      'from Him — against the Jews’ fabrication and the Christians’ excess',
      'That his case is to be left unspoken of',
      'That he will return as a judge'], 1),
    ('What is the madhhab of Ahl al-Sunnah on the attribute of speech?',
     ['That it is an attribute of the Essence only',
      'That it is of His attributes of the Essence — subsisting with Him — AND of His attributes '
      'of the Actions, occurring by His will: He speaks if He wills, how He wills, with what He '
      'wills',
      'That it is an attribute of the Actions only',
      'That its meaning is left unknown'], 1),
    ('What two reasons does al-Fawzān give that Allah never ceased being a Speaker?',
     ['Consensus and analogy',
      'That He never ceased being Perfect and speech is of the attributes of perfection; and that '
      'He described Himself with it and His Messenger described Him with it',
      'The practice of the Companions and the Arabic language',
      'That the Qurʾān is eternal and uncreated'], 1),
])
b += B.tf('ws-l19-tf', [
    ('الَّذِي يُتْلَى هُوَ كَلَامُ اللهِ.', 'That which is recited is the speech of Allah.', True),
    ('التَّحْرِيفُ فِي آيَةِ البَقَرَةِ وَقَعَ مِنْ جَهْلٍ بِالمَعْنَى.',
     'The taḥrīf in the āyah of al-Baqarah occurred out of ignorance of the meaning.', False),
    ('الكَلَامُ مِنْ صِفَاتِ اللهِ الذَّاتِيَّةِ وَالفِعْلِيَّةِ مَعًا.',
     'Speech is of Allah’s attributes of both the Essence and the Actions together.', True),
    ('يُمْكِنُ لِأَحَدٍ أَنْ يُبَدِّلَ كَلِمَاتِ اللهِ.',
     'It is possible for someone to change the words of Allah.', False),
])
b += B.memorize(
    'لَا مُبَدِّلَ لِكَلِمَاتِهِ',
    'Four words to set against al-Fatḥ 48:15, where men <em>wish</em> to change His speech. The '
    'wish has never been in doubt. The āyah answers the capacity.')
b += B.aiquiz('The Quran as the speech of Allah in al-Aqidah al-Wasitiyyah: how al-Tawbah 9:6 '
              'proves the recited Quran is His speech, tahrif as interpreting a text against its '
              'meaning after understanding it, the promise of Khaybar in al-Fath 48:15, the '
              'middle statement on Isa, and the madhhab of Ahl al-Sunnah that speech is an '
              'attribute of both the Essence and the Actions with the two reasons He never '
              'ceased being a Speaker')
b += B.further()
b += B.nav('was-l18-kalam-allah.html', 'The Affirmation of Speech for Allah',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l19')

io.open(os.path.join(B.AQ, 'was-l19-quran-kalam-allah.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'القُرْآنُ كَلَامُ اللهِ وَلَا مُبَدِّلَ لِكَلِمَاتِه',
    'The Qurʾān Is the Speech of Allah, and None Can Change His Words',
    'Lesson 19 of al-ʿAqīdah al-Wāsiṭiyyah: how al-Tawbah 9:6 '
    'proves the recited Qurʾān is the speech of Allah, taḥrīf as reading a '
    'text against its meaning after understanding it, and the madhhab of Ahl al-Sunnah that '
    'speech is an attribute of the Essence AND of the Actions — He speaks if He wills, how '
    'He wills, with what He wills.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ التَّاسِعَ عَشَر', '3',
           'القُرْآنُ كَلَامُ اللهِ وَلَا مُبَدِّلَ لِكَلِمَاتِه',
           'The Qurʾān Is the Speech of Allah, and None Can Change His Words', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l19-quran-kalam-allah.html')
