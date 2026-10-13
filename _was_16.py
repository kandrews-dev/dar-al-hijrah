# -*- coding: utf-8 -*-
"""Wasitiyyah L16 -- sections 18 and 19: the istiwa' of Allah upon His Throne
(seven ayat, the four Arabic senses, and the four refutations of istawla), and
His 'uluww above His creation, closing with al-Fawzan's two-point distinction
between the two attributes. Sharh pp.69-74."""
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
    '<em>شَرْحُ العَقِيدَةِ الوَاسِطِيَّة</em> — a second, fuller sharḥ of these two sections.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Name the seven sūrahs in which %s is affirmed, and the one expression they share.'
    % ar('الاسْتِوَاء'),
    'Give the four senses of %s in the speech of the Arabs.' % ar('اسْتَوَى'),
    'Reproduce all four of al-Fawzān’s refutations of reading %s as %s.'
    % (ar('اسْتَوَى'), ar('اسْتَوْلَى')),
    'State the two differences between %s and %s.' % (ar('العُلُوّ'), ar('الاسْتِوَاء')),
])

b += B.heading('١٨ · إِثْبَاتُ اسْتِوَاءِ اللهِ عَلَى عَرْشِه',
               'Section 18 — The Istiwāʾ of Allah upon His Throne')
b += B.matn(
    'وَقَوْلُهُ فِي سُورَةِ الأَعْرَافِ: ﴿إِنَّ رَبَّكُمُ اللَّهُ الَّذِي خَلَقَ السَّمَاوَاتِ '
    'وَالْأَرْضَ فِي سِتَّةِ أَيَّامٍ ثُمَّ اسْتَوَى عَلَى الْعَرْشِ﴾، وَقَالَ فِي سُورَةِ '
    'يُونُسَ: ﴿إِنَّ رَبَّكُمُ اللَّهُ الَّذِي خَلَقَ السَّمَاوَاتِ وَالْأَرْضَ فِي سِتَّةِ '
    'أَيَّامٍ ثُمَّ اسْتَوَى عَلَى الْعَرْشِ﴾، وَقَالَ فِي سُورَةِ الرَّعْدِ: ﴿اللَّهُ الَّذِي '
    'رَفَعَ السَّمَاوَاتِ بِغَيْرِ عَمَدٍ تَرَوْنَهَا ثُمَّ اسْتَوَى عَلَى الْعَرْشِ﴾، وَقَالَ '
    'فِي سُورَةِ طه: ﴿الرَّحْمَنُ عَلَى الْعَرْشِ اسْتَوَى﴾، وَقَالَ فِي سُورَةِ الفُرْقَانِ: '
    '﴿ثُمَّ اسْتَوَى عَلَى الْعَرْشِ الرَّحْمَنُ﴾، وَقَالَ فِي سُورَةِ الم السَّجْدَةِ: '
    '﴿اللَّهُ الَّذِي خَلَقَ السَّمَاوَاتِ وَالْأَرْضَ وَمَا بَيْنَهُمَا فِي سِتَّةِ أَيَّامٍ '
    'ثُمَّ اسْتَوَى عَلَى الْعَرْشِ﴾، وَقَالَ فِي سُورَةِ الحَدِيدِ: ﴿هُوَ الَّذِي خَلَقَ '
    'السَّمَاوَاتِ وَالْأَرْضَ فِي سِتَّةِ أَيَّامٍ ثُمَّ اسْتَوَى عَلَى الْعَرْشِ﴾.')
b += B.sharh(
    p('al-Fawzān opens with what the matn has just demonstrated by sheer accumulation: '
      '<strong>the affirmation of Allah\'s istiwāʾ upon His Throne has come in seven āyāt of the '
      'Book of Allah</strong> — al-Aʿrāf, Yūnus, al-Raʿd, Ṭā-Hā, al-Furqān, al-Sajdah, al-Ḥadīd '
      '— <strong>and in all of them the affirmation came with one single expression: %s.</strong>'
      % ar('اسْتَوَى عَلَى الْعَرْشِ')) +
    p('And from that uniformity he draws the conclusion: <strong>%s</strong> — '
      '<em>it is explicit in its real meaning; it does not admit of being reinterpreted to some '
      'other meaning.</em> Seven places, one wording, no variant. There is nothing here for a '
      'taʾwīl to get a grip on.'
      % ar('فَهُوَ نَصٌّ فِي مَعْنَاهُ الحَقِيقِيِّ لَا يَحْتَمِلُ التَّأْوِيلَ بِمَعْنًى آخَر')) +
    p('Then the classification: <strong>%s</strong> — <em>a verbal attribute, established for '
      'Allah, in the manner that befits His majesty, like the rest of His attributes.</em> Keep '
      'the phrase %s in view; the whole of Lesson 6 was spent earning the right to say it here '
      'without hesitation.'
      % (ar('الاسْتِوَاءُ صِفَةٌ فِعْلِيَّةٌ ثَابِتَةٌ لِلَّهِ سُبْحَانَهُ عَلَى مَا يَلِيقُ بِجَلَالِه'),
         ar('عَلَى مَا يَلِيقُ بِجَلَالِه'))))
b += B.ayah(
    'إِنَّ رَبَّكُمُ اللَّهُ الَّذِي خَلَقَ السَّمَاوَاتِ وَالْأَرْضَ فِي سِتَّةِ أَيَّامٍ '
    'ثُمَّ اسْتَوَى عَلَى الْعَرْشِ',
    '"Indeed your Lord is Allah, who created the heavens and the earth in six days, then rose '
    'over the Throne."',
    'Sūrat al-Aʿrāf 7:54 · سورة الأعراف — and the same wording in Yūnus 10:3')
b += B.sharh(
    p('<strong>%s</strong> — <em>He is your Creator and the One who nurtures you with His '
      'favours, and the One whom it is obligatory upon you to worship alone.</em> The āyah does '
      'not begin with the Throne; it begins with the claim on you.' % ar('إِنَّ رَبَّكُمُ اللَّهُ')) +
    p('<strong>%s</strong> — the six are named: <em>al-aḥad, al-ithnayn, al-thulāthāʾ, '
      'al-arbiʿāʾ, al-khamīs and al-jumuʿah</em>. <em>And on the day of Jumuʿah the whole of the '
      'creation came together, and on it Ādam &#1593;&#1604;&#1610;&#1607; &#1575;&#1604;&#1587;'
      '&#1604;&#1575;&#1605; was created.</em>' % ar('فِي سِتَّةِ أَيَّامٍ')) +
    p('<strong>%s</strong> — <em>He rose and ascended over the Throne, as befits His majesty; and '
      '<strong>this is the place of the shāhid from the āyah.</strong></em>'
      % ar('ثُمَّ اسْتَوَى عَلَى الْعَرْشِ')))
b += B.sharh(
    p('And <strong>%s</strong>? al-Fawzān gives both the lexical sense and what the texts '
      'establish: <em>in the language it is <strong>the bed/couch of the king</strong>. And what '
      'is intended by it here — as the totality of the texts indicates — is '
      '<strong>a couch having legs, borne by the angels, and it is like a dome over the world, '
      'and it is the roof of the created things.</strong></em>' % ar('العَرْش')) +
    p('Note the discipline in that sentence: he does not reason from the lexical meaning to a '
      'picture, and he does not refuse to say anything at all. He says what <em>the totality of '
      'the texts</em> indicates, and stops there.'))
b += B.ayah(
    'اللَّهُ الَّذِي رَفَعَ السَّمَاوَاتِ بِغَيْرِ عَمَدٍ تَرَوْنَهَا ثُمَّ اسْتَوَى عَلَى '
    'الْعَرْشِ وَسَخَّرَ الشَّمْسَ وَالْقَمَرَ',
    '"Allah is He who raised the heavens without pillars that you see, then rose over the Throne, '
    'and made the sun and the moon subservient."',
    'Sūrat al-Raʿd 13:2 · سورة الرعد')
b += B.sharh(
    p('<strong>%s</strong> — <em>He raised them above the earth with a far raising, whose extent '
      'is not attained and not grasped.</em> <strong>%s</strong> are the columns, the plural of '
      '%s: <em>standing without pillars that they rest upon — rather, by His power.</em>'
      % (ar('رَفَعَ السَّمَاوَاتِ'), ar('العَمَد'), ar('عِمَاد'))) +
    p('And <strong>%s</strong> — al-Fawzān reports the two readings fairly and then chooses: '
      '<em>it is an emphasis of the negation of pillars; and it has been said: they have pillars '
      'but we do not see them — <strong>and the first is more correct.</strong></em>'
      % ar('تَرَوْنَهَا')) +
    p('<strong>%s — this is the place of the shāhid from the noble āyah for the affirming of '
      'al-istiwāʾ; and the discussion on the remaining āyāt is like the discussion on this '
      'one.</strong>' % ar('ثُمَّ اسْتَوَى عَلَى الْعَرْشِ')))

b += B.heading('مَعَانِي «اسْتَوَى» فِي لُغَةِ العَرَب', 'The Senses of istawā in the Speech of the Arabs')
b += B.sharh(
    p('Before the refutation, the lexical ground. al-Fawzān: <strong>and it has four meanings in '
      'the language of the Arabs</strong> —') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.5rem .8rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>عَلَا</strong></td>'
    '<td style="padding:.5rem .8rem;border:1px solid var(--line)">he was high over</td></tr>'
    '<tr><td style="padding:.5rem .8rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>ارْتَفَعَ</strong></td>'
    '<td style="padding:.5rem .8rem;border:1px solid var(--line)">he rose</td></tr>'
    '<tr><td style="padding:.5rem .8rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>صَعِدَ</strong></td>'
    '<td style="padding:.5rem .8rem;border:1px solid var(--line)">he ascended</td></tr>'
    '<tr><td style="padding:.5rem .8rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>اسْتَقَرَّ</strong></td>'
    '<td style="padding:.5rem .8rem;border:1px solid var(--line)">he settled</td></tr>'
    '</table></div>' +
    p('<strong>And these four meanings are what the explanations of the Salaf for the istiwāʾ '
      'mentioned in these noble āyāt revolve around.</strong>') +
    p('That is the entire controversy in one observation. The Salaf had four words to hand, and '
      'all four of them are words of <em>height</em>. Not one of them is %s.' % ar('اسْتَوْلَى')))

b += B.heading('أَرْبَعَةُ أَوْجُهٍ فِي رَدِّ تَأْوِيلِ «اسْتَوْلَى»',
               'Four Grounds for Rejecting the Reading "He Seized Power"')
b += B.prose(
    'al-Fawzān states what is derived from all seven āyāt together: <em>the affirming of Allah\'s '
    'istiwāʾ upon His Throne in the manner that befits His majesty — and in them is the '
    '<strong>refutation of whoever reinterpreted al-istiwāʾ as meaning seizing control and '
    'overpowering</strong>, and explained the Throne as meaning the dominion, so he said: '
    '"He rose over the Throne" means "He seized the dominion and overpowered everyone else." '
    '<strong>And this is invalid from many angles</strong>, among them:</em>')
b += B.sharh(
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.93rem">'
    '<p style="margin:0 0 .7rem"><strong>أَوَّلًا · It is a newly invented '
    'interpretation.</strong> It contradicts the explanation of the Salaf — of the '
    'Ṣaḥābah, the Tābiʿīn and those who followed them. '
    '<strong>And the first to say it were the Jahmiyyah and the Muʿtazilah — so it is '
    'rejected.</strong></p>'
    '<p style="margin:0 0 .7rem"><strong>ثَانِيًا · It would make mentioning the Throne '
    'pointless.</strong> Were seizing the dominion what is meant, <em>there would be no '
    'difference between the Throne and the lowest seventh earth and the beasts and all the '
    'created things</em> — because He is in control of all of them and the Owner of all of '
    'them. <strong>So there would be no benefit in the mention of the Throne</strong> at all.</p>'
    '<p style="margin:0 0 .7rem"><strong>ثَالِثًا · The wording never varies.</strong> This '
    'expression <span dir="rtl" lang="ar">اسْتَوَى عَلَى الْعَرْشِ</span> has run consistently '
    'through the Book and the Sunnah, <strong>and not in a single wording has '
    '<span dir="rtl" lang="ar">اسْتَوْلَى عَلَى الْعَرْشِ</span> come</strong> — so that '
    'the remaining texts could be explained by it.</p>'
    '<p style="margin:0"><strong>رَابِعًا · The <span dir="rtl" lang="ar">ثُمَّ</span> '
    'destroys it.</strong> He brought <span dir="rtl" lang="ar">ثُمَّ</span>, which conveys '
    '<em>sequence and an interval</em>. Were the meaning of al-istiwāʾ the seizing of '
    'the Throne and power over it, <strong>that would not have been delayed until after the '
    'creation of the heavens and the earth</strong> — for the Throne existed before the '
    'creation of the heavens and the earth by <strong>fifty thousand years</strong>, as is '
    'established in the two Ṣaḥīḥs. So how could it be permissible that He '
    'was not able, nor in control of it, until He created the heavens and the earth?! '
    '<strong><span dir="rtl" lang="ar">هَذَا مِنْ أَبْطَلِ البَاطِلِ</span></strong> — this '
    'is of the most false of the false. وَاللهُ أَعْلَم.</p></div>' +
    p('The fourth is the one worth sitting with. It does not argue from the lexicon or from the '
      'Salaf; <strong>it argues from a single particle.</strong> %s puts the istiwāʾ <em>after</em> '
      'the creating. If istiwāʾ meant <em>gaining control</em>, then before that moment Allah was '
      'not in control of a Throne that had already existed for fifty thousand years. '
      '<strong>The taʾwīl, followed out honestly, makes Allah deficient — which is the very thing '
      'its authors said they were protecting Him from.</strong>' % ar('ثُمَّ')))

b += B.heading('١٩ · إِثْبَاتُ عُلُوِّ اللهِ عَلَى مَخْلُوقَاتِه',
               'Section 19 — The ʿUluww of Allah above His Creation')
b += B.matn(
    'وَقَوْلُهُ: ﴿يَا عِيسَى إِنِّي مُتَوَفِّيكَ وَرَافِعُكَ إِلَيَّ﴾، ﴿بَلْ رَفَعَهُ اللَّهُ '
    'إِلَيْهِ﴾، ﴿إِلَيْهِ يَصْعَدُ الْكَلِمُ الطَّيِّبُ وَالْعَمَلُ الصَّالِحُ يَرْفَعُهُ﴾، '
    '﴿يَا هَامَانُ ابْنِ لِي صَرْحًا لَعَلِّي أَبْلُغُ الْأَسْبَابَ ۝ أَسْبَابَ السَّمَاوَاتِ '
    'فَأَطَّلِعَ إِلَى إِلَهِ مُوسَى وَإِنِّي لَأَظُنُّهُ كَاذِبًا﴾، ﴿أَأَمِنْتُمْ مَنْ فِي '
    'السَّمَاءِ أَنْ يَخْسِفَ بِكُمُ الْأَرْضَ فَإِذَا هِيَ تَمُورُ ۝ أَمْ أَمِنْتُمْ مَنْ '
    'فِي السَّمَاءِ أَنْ يُرْسِلَ عَلَيْكُمْ حَاصِبًا فَسَتَعْلَمُونَ كَيْفَ نَذِيرِ﴾.')
b += B.ayah(
    'إِذْ قَالَ اللَّهُ يَا عِيسَى إِنِّي مُتَوَفِّيكَ وَرَافِعُكَ إِلَيَّ',
    '"When Allah said: O ʿĪsā, I am going to take you and raise you to Myself."',
    'Sūrat Āl ʿImrān 3:55 · سورة آل عمران')
b += B.sharh(
    p('<strong>%s</strong> — al-Fawzān reports the majority position: <em>what is intended by '
      '<strong>al-wafāh</strong> here is <strong>sleep</strong></em>, as in %s — «and He is the '
      'One who takes you by night» (al-Anʿām 6:60) — and %s — «Allah takes the souls at the time '
      'of their death, and those that do not die, in their sleep» (al-Zumar 39:42).'
      % (ar('إِنِّي مُتَوَفِّيكَ'), ar('وَهُوَ الَّذِي يَتَوَفَّاكُمْ بِاللَّيْلِ'),
         ar('اللَّهُ يَتَوَفَّى الْأَنْفُسَ حِينَ مَوْتِهَا وَالَّتِي لَمْ تَمُتْ فِي مَنَامِهَا'))) +
    p('<strong>%s</strong> — <em>Allah raised him to Himself in the heaven <strong>while he is '
      'alive</strong>; and this is the place of the shāhid from the āyah, which is the affirming '
      'of al-ʿuluww for Allah — because the raising is to what is above.</em>'
      % ar('وَرَافِعُكَ إِلَيَّ')))
b += B.ayah(
    'بَلْ رَفَعَهُ اللَّهُ إِلَيْهِ وَكَانَ اللَّهُ عَزِيزًا حَكِيمًا',
    '"Rather, Allah raised him to Himself — and Allah is ever Mighty, Wise."',
    'Sūrat al-Nisāʾ 4:158 · سورة النساء')
b += B.prose(
    'This is <em>a refutation of the Jews, who claim that they killed the Messiah ʿĪsā the son of '
    'Maryam</em> — against which Allah said: «and they did not kill him, nor did they crucify '
    'him; rather it was made to appear so to them» — <strong>%s</strong> (al-Nisāʾ 4:157). '
    '<em>He raised the Messiah to Himself while he is alive and was not killed; and this is the '
    'place of the shāhid, because in it is the affirming of Allah\'s highness above His creation '
    '— for the raising is to what is above.</em>'
    % ar('وَمَا قَتَلُوهُ وَمَا صَلَبُوهُ وَلَكِنْ شُبِّهَ لَهُمْ'))
b += B.ayah(
    'إِلَيْهِ يَصْعَدُ الْكَلِمُ الطَّيِّبُ وَالْعَمَلُ الصَّالِحُ يَرْفَعُهُ',
    '"To Him ascends the goodly word, and righteous action raises it."',
    'Sūrat Fāṭir 35:10 · سورة فاطر')
b += B.sharh(
    p('<strong>%s</strong> is <em>the remembrance, the recitation and the supplication</em>. And '
      '<strong>%s</strong> — <em>righteous action raises the goodly word</em>, <em>for the goodly '
      'word is not accepted except together with righteous action.</em>'
      % (ar('الكَلِمُ الطَّيِّب'), ar('وَالْعَمَلُ الصَّالِحُ يَرْفَعُهُ'))) +
    p('And then the sentence that should make a student put the book down for a moment: '
      '<strong>%s</strong> — <em>so whoever makes remembrance of Allah and does not discharge His '
      'obligations, <strong>his speech is returned to him</strong>.</em>'
      % ar('فَمَنْ ذَكَرَ اللهَ تَعَالَى وَلَمْ يُؤَدِّ فَرَائِضَهُ رُدَّ كَلَامُه')) +
    p('al-Fawzān brings two of the early generation on it. <strong>إِيَاسُ بْنُ '
      'مُعَاوِيَة</strong>: <em>were it not for righteous action, speech would not be raised.</em> '
      'And <strong>الحَسَنُ</strong> and <strong>قَتَادَةُ</strong>: <em>no statement is accepted '
      'except with action.</em>') +
    p('<strong>And the shāhid from the āyah: that in it is the affirming of Allah\'s highness '
      'above His creation — because ascending and raising are both to what is above.</strong>'))
b += B.ayah(
    'وَقَالَ فِرْعَوْنُ يَا هَامَانُ ابْنِ لِي صَرْحًا لَعَلِّي أَبْلُغُ الْأَسْبَابَ '
    'أَسْبَابَ السَّمَاوَاتِ فَأَطَّلِعَ إِلَى إِلَهِ مُوسَى وَإِنِّي لَأَظُنُّهُ كَاذِبًا',
    '"And Pharaoh said: O Hāmān, build for me a tower, that I may reach the ways — the ways of '
    'the heavens — and look upon the God of Mūsā; and indeed I think him a liar."',
    'Sūrat Ghāfir 40:36–37 · سورة غافر')
b += B.sharh(
    p('<em>This is from the statement of Pharaoh to his minister Hāmān, commanding him to build '
      'him a lofty, high castle.</em> <strong>%s</strong> — <em>the roads of the heavens, or their '
      'gates</em>. And a grammatical note, since the matn quotes it: <strong>%s is manṣūb by an '
      'implied %s after the %s.</strong>'
      % (ar('أَسْبَابَ السَّمَاوَاتِ'), ar('فَأَطَّلِعَ'), ar('أَنْ'), ar('فَاءِ السَّبَبِيَّة'))) +
    p('And the meaning of this statement of his is <em>the belying of Mūsā '
      '&#1593;&#1604;&#1610;&#1607; &#1575;&#1604;&#1587;&#1604;&#1575;&#1605; in that Allah sent '
      'him, or in that he has a God in the heaven — and that is why he said %s.</em>'
      % ar('وَإِنِّي لَأَظُنُّهُ كَاذِبًا')) +
    p('Now follow the logic of the proof, because it is an unusual one. <strong>The shāhid is '
      'that in it is the affirming of Allah\'s highness above His creation — since Mūsā '
      '&#1593;&#1604;&#1610;&#1607; &#1575;&#1604;&#1587;&#1604;&#1575;&#1605; informed of that, '
      'and Pharaoh set about trying to reach the heavens to look into it.</strong> Pharaoh is not '
      'a witness for the truth. He is a witness for <em>what Mūsā had taught</em>: his mockery '
      'takes the form of building upward, which only makes sense if upward is where he had been '
      'told to look. <strong>The enemy\'s own ridicule preserves the doctrine he was '
      'ridiculing.</strong>'))
b += B.ayah(
    'أَأَمِنْتُمْ مَنْ فِي السَّمَاءِ أَنْ يَخْسِفَ بِكُمُ الْأَرْضَ فَإِذَا هِيَ تَمُورُ '
    'أَمْ أَمِنْتُمْ مَنْ فِي السَّمَاءِ أَنْ يُرْسِلَ عَلَيْكُمْ حَاصِبًا فَسَتَعْلَمُونَ '
    'كَيْفَ نَذِيرِ',
    '"Do you feel secure from Him who is above the heaven, that He should cause the earth to '
    'swallow you up — and then it is heaving? Or do you feel secure from Him who is above the '
    'heaven, that He should send upon you a storm of stones? Then you will know how My warning '
    'was."',
    'Sūrat al-Mulk 67:16–17 · سورة الملك')
b += B.sharh(
    p('<strong>%s</strong> — <em>security is the opposite of fear</em>. <strong>%s</strong> — '
      '<em>a punishment from Him who is above the heaven, and He is Allah سبحانه</em>.'
      % (ar('الأَمْن'), ar('مَنْ فِي السَّمَاءِ'))) +
    p('And then the point of Arabic that carries the whole āyah. <strong>The meaning of %s is '
      '%s</strong> — <em>above the heaven</em> — <strong>as in His saying %s</strong>, «and I '
      'will surely crucify you <em>on</em> the trunks of the palm trees» (Ṭā-Hā 20:71), where no '
      'one imagines being crucified <em>inside</em> a trunk. <em>This is if what is intended by '
      '«the heaven» is the built heaven. And if what is intended by «the heaven» is '
      '<strong>absolute height</strong>, then the %s is for the adverbial sense — that is: in the '
      'loftiness.</em>'
      % (ar('فِي السَّمَاءِ'), ar('عَلَى السَّمَاءِ'),
         ar('وَلَأُصَلِّبَنَّكُمْ فِي جُذُوعِ النَّخْلِ'), ar('فِي'))) +
    p('<strong>%s</strong> — <em>He uproots it with you, as He did with Qārūn</em>; '
      '<strong>%s</strong> — <em>it convulses and moves</em>. <strong>%s</strong> — <em>stones '
      'from the sky, as He sent them upon the people of Lūṭ and the Companions of the Elephant; '
      'and it has been said: a cloud with stones in it; and it has been said: a wind with stones '
      'in it.</em> <strong>%s</strong> — <em>My warning, when you behold the punishment</em>.'
      % (ar('أَنْ يَخْسِفَ بِكُمُ الْأَرْضَ'), ar('تَمُورُ'), ar('حَاصِبًا'),
         ar('فَسَتَعْلَمُونَ كَيْفَ نَذِيرِ'))) +
    p('<strong>And the shāhid from the two āyāt: that in them is the affirming of Allah\'s '
      'highness above His creation, since the two of them stated explicitly that He سبحانه is '
      'above the heaven.</strong>'))

b += B.heading('الفَرْقُ بَيْنَ الاسْتِوَاءِ وَالعُلُوّ',
               'The Difference Between al-Istiwāʾ and al-ʿUluww')
b += B.prose(
    'Having established both, al-Fawzān will not let the student run them together. <em>These '
    'āyāt which the author رحمه الله mentioned indicate the affirming of al-ʿuluww, just as these '
    'āyāt before them indicated the affirming of Allah\'s istiwāʾ upon the Throne.</em> They are '
    '<strong>two attributes, not one</strong>, and they differ in two ways.')
b += B.sharh(
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><th style="padding:.5rem .7rem;border:1px solid var(--line);text-align:right"></th>'
    '<th style="padding:.5rem .7rem;border:1px solid var(--line);text-align:left" dir="rtl"'
    ' lang="ar">العُلُوّ</th>'
    '<th style="padding:.5rem .7rem;border:1px solid var(--line);text-align:left" dir="rtl"'
    ' lang="ar">الاسْتِوَاء</th></tr>'
    '<tr><td style="padding:.5rem .7rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>١</strong> kind of attribute</td>'
    '<td style="padding:.5rem .7rem;border:1px solid var(--line)">of the attributes of '
    '<strong>the Essence</strong> — His highness above His creation is a description '
    '<strong>necessarily belonging</strong> to His Essence</td>'
    '<td style="padding:.5rem .7rem;border:1px solid var(--line)">of the attributes of '
    '<strong>the Actions</strong> — an act among His acts, which He does by His will and His '
    'power when He wills; and that is why He said <span dir="rtl" lang="ar">ثُمَّ اسْتَوَى</span>, '
    'and it was <strong>after</strong> the creation of the heavens and the earth</td></tr>'
    '<tr><td style="padding:.5rem .7rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>٢</strong> how established</td>'
    '<td style="padding:.5rem .7rem;border:1px solid var(--line)">established by '
    '<strong>reason and transmission</strong> both</td>'
    '<td style="padding:.5rem .7rem;border:1px solid var(--line)">established by '
    '<strong>transmission, not reason</strong></td></tr>'
    '</table></div>' +
    p('The second row is the quiet methodological lesson. <em>ʿUluww</em> the intellect can reach '
      '— perfection is above deficiency, and the Creator is not contained by what He created. '
      '<em>Istiwāʾ</em> it cannot: no amount of reasoning would have told you that He rose over '
      'the Throne <strong>after</strong> creating the heavens and the earth. <strong>That is '
      'known only because He said it</strong> — which is exactly why the one who tries to reason '
      'his way to a meaning for it ends up at %s.' % ar('اسْتَوْلَى')))

b += B.vocab([
    ('الاسْتِوَاء', 'al-istiwāʾ', 'rising over',
     'A verbal attribute, as befits His majesty — established by transmission'),
    ('العُلُوّ', 'al-ʿuluww', 'highness',
     'An attribute of the Essence — established by reason and transmission'),
    ('العَرْش', 'al-ʿarsh', 'the Throne',
     'In the language: the king’s couch; here: a couch with legs, borne by the angels'),
    ('العَمَد', 'al-ʿamad', 'pillars',
     'Plural of عِمَاد — the heavens stand by His power, without them'),
    ('الوَفَاة', 'al-wafāh', 'the taking',
     'Here: sleep — as in يَتَوَفَّاكُمْ بِاللَّيْلِ'),
    ('الكَلِمُ الطَّيِّب', 'al-kalim al-ṭayyib', 'the goodly word',
     'Remembrance, recitation and supplication — raised by righteous action'),
    ('الصَّرْح', 'al-ṣarḥ', 'the tower',
     'The lofty castle Pharaoh ordered, to look for the God of Mūsā'),
    ('حَاصِب', 'ḥāṣib', 'a storm of stones',
     'As sent on the people of Lūṭ and the Companions of the Elephant'),
])
b += B.mcq('ws-l16', [
    ('In how many āyāt is Allah’s istiwāʾ upon the Throne affirmed, and with what wording?',
     ['In three āyāt, with varying wordings',
      'In seven āyāt, all with the one expression %s' % ar('اسْتَوَى عَلَى الْعَرْشِ'),
      'In seven āyāt, with seven different expressions',
      'In one āyah only, in Sūrat Ṭā-Hā'], 1),
    ('What are the four senses of %s in the speech of the Arabs?' % ar('اسْتَوَى'),
     ['عَلَا، ارْتَفَعَ، صَعِدَ، اسْتَقَرَّ',
      'اسْتَوْلَى، قَهَرَ، مَلَكَ، دَبَّرَ',
      'جَلَسَ، قَعَدَ، نَزَلَ، حَلَّ',
      'عَلِمَ، أَرَادَ، قَدَرَ، خَلَقَ'], 0),
    ('Who, according to al-Fawzān, were the first to interpret the istiwāʾ as %s?'
     % ar('اسْتَوْلَى'),
     ['The Ṣaḥābah', 'The Jahmiyyah and the Muʿtazilah',
      'The Tābiʿīn', 'Ibn Kathīr and al-Ṭabarī'], 1),
    ('What is the second ground of refutation — the one about the Throne itself?',
     ['That the Throne is not mentioned in the Sunnah',
      'That if seizing dominion were meant, there would be no difference between the Throne and '
      'the lowest earth and the beasts — so mentioning the Throne would serve no purpose',
      'That the Throne was created last',
      'That the Throne is the dominion'], 1),
    ('How does the particle %s refute the taʾwīl?' % ar('ثُمَّ'),
     ['It shows the istiwāʾ was eternal',
      'It conveys sequence and interval — so if istiwāʾ meant gaining power, Allah would not have '
      'had power over a Throne that already existed fifty thousand years before',
      'It is merely for emphasis and has no bearing',
      'It shows the creating came after the istiwāʾ'], 1),
    ('What does al-Fawzān say of the one who makes dhikr but does not discharge the obligations?',
     ['His reward is merely reduced', 'His speech is returned to him',
      'He is rewarded for the dhikr regardless', 'He must repeat the dhikr'], 1),
    ('How is Pharaoh’s tower a proof of al-ʿuluww?',
     ['Because Pharaoh believed Allah is above the heaven',
      'Because Mūsā had informed of it, and Pharaoh set about building upward to look into it — '
      'his mockery takes the shape of the doctrine he mocked',
      'Because the tower actually reached the heaven',
      'Because Hāmān was a believer'], 1),
    ('What are the two differences between al-ʿuluww and al-istiwāʾ?',
     ['ʿUluww is figurative, istiwāʾ real',
      'ʿUluww is an attribute of the Essence established by reason and transmission; istiwāʾ is an '
      'attribute of the Actions established by transmission alone',
      'ʿUluww is an act, istiwāʾ is essential',
      'There is no difference; the two are one attribute'], 1),
])
b += B.tf('ws-l16-tf', [
    ('لَفْظُ «اسْتَوْلَى عَلَى العَرْشِ» وَارِدٌ فِي الكِتَابِ وَالسُّنَّةِ.',
     'The wording "He seized the Throne" occurs in the Book and the Sunnah.', False),
    ('العَرْشُ كَانَ مَوْجُودًا قَبْلَ خَلْقِ السَّمَاوَاتِ وَالْأَرْضِ بِخَمْسِينَ أَلْفَ سَنَةٍ.',
     'The Throne existed fifty thousand years before the heavens and the earth.', True),
    ('مَعْنَى «فِي السَّمَاءِ» أَيْ: عَلَى السَّمَاءِ.',
     'The meaning of "in the heaven" is: above the heaven.', True),
    ('الاسْتِوَاءُ مِنْ صِفَاتِ الذَّاتِ.', 'Al-istiwāʾ is of the attributes of the Essence.', False),
])
b += B.memorize(
    'الرَّحْمَنُ عَلَى الْعَرْشِ اسْتَوَى',
    'The shortest of the seven, and the one the Salaf quoted most. Four words, and every attempt '
    'to make them mean something else has had to invent a word the Qurʾān never used.')
b += B.aiquiz('The istiwa of Allah upon His Throne and His uluww above His creation in '
              'al-Aqidah al-Wasitiyyah: the seven ayat and their single wording, the four Arabic '
              'senses of istawa, al-Fawzan four refutations of reading it as istawla including '
              'the argument from the particle thumma and the fifty thousand years, and the '
              'two-point distinction between uluww as an attribute of the Essence and istiwa as '
              'an attribute of the Actions')
b += B.further()
b += B.nav('was-l15-nafy-sharik-tamanu.html', 'Completing the Negation of a Partner',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l16')

io.open(os.path.join(B.AQ, 'was-l16-istiwa-uluww.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'الاسْتِوَاءُ عَلَى العَرْشِ وَالعُلُوُّ عَلَى المَخْلُوقَات',
    'The Istiwāʾ upon the Throne, and the Highness above the Creation',
    'Lesson 16 of al-ʿAqīdah al-Wāsiṭiyyah: the seven '
    'āyāt of al-istiwāʾ and the one wording they share, the four senses of '
    'istawā in Arabic, al-Fawzān’s four grounds for rejecting the reading '
    '“he seized power” — including the argument from the particle thumma — '
    'and the two differences between al-ʿuluww and al-istiwāʾ.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ السَّادِسَ عَشَر', '3',
           'الاسْتِوَاءُ عَلَى العَرْشِ وَالعُلُوُّ عَلَى المَخْلُوقَات',
           'The Istiwāʾ upon the Throne, and the Highness above the Creation', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l16-istiwa-uluww.html')
