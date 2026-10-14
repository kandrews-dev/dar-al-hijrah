# -*- coding: utf-8 -*-
"""Wasitiyyah L26 -- Part 2, section 6 (first half): the ruqyah of the sick, the
meaning of "in the heaven", the two kinds of mercy, and "I am the trustee of Him
who is above the heaven". Sharh pp.98-100."""
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
    'The ruqyah ḥadīth is graded <strong>حَسَن</strong> by the author '
    '<strong>ابْنُ تَيْمِيَّة</strong> in the matn itself, reported by '
    '<strong>أَبُو دَاوُد</strong> and others.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Give the two readings of %s and why either one yields the ʿuluww.'
    % ar('الَّذِي فِي السَّمَاءِ'),
    'Explain why %s covers all of Allah’s names.' % ar('تَقَدَّسَ اسْمُكَ'),
    'Distinguish the two kinds of %s, and say which one is asked to be sent down.'
    % ar('رَحْمَةُ الله'),
    'List the six things by which this duʿāʾ performs %s.' % ar('التَّوَسُّل'),
])

b += B.heading('٦ · إِثْبَاتُ عُلُوِّ اللهِ عَلَى خَلْقِهِ وَاسْتِوَائِهِ عَلَى عَرْشِه',
               'Section 6 — His Highness above His Creation, and His Istiwāʾ')
b += B.prose(
    'This is the longest section of Part 2, and the author assembles four separate texts for it. '
    'This lesson takes the first two; the next takes the ḥadīth of the Throne above all created '
    'things, and the ḥadīth of the slave-girl. Note that the section pairs the <em>ʿuluww</em> and '
    'the <em>istiwāʾ</em> exactly as Lesson 16 did from the Qurʾān — <strong>the Sunnah is here '
    'saying what the Qurʾān said</strong>, which is the fourth function of the Sunnah from '
    'Lesson 22.')
b += B.matn(
    'وَقَوْلُهُ ﷺ فِي رُقْيَةِ المَرِيضِ: «رَبَّنَا اللهُ الَّذِي فِي السَّمَاءِ تَقَدَّسَ '
    'اسْمُكَ، أَمْرُكَ فِي السَّمَاءِ وَالأَرْضِ، كَمَا رَحْمَتُكَ فِي السَّمَاءِ اجْعَلْ '
    'رَحْمَتَكَ فِي الأَرْضِ، اغْفِرْ لَنَا حَوْبَنَا وَخَطَايَانَا، أَنْتَ رَبُّ '
    'الطَّيِّبِينَ، أَنْزِلْ رَحْمَةً مِنْ رَحْمَتِكَ وَشِفَاءً مِنْ شِفَائِكَ عَلَى هَذَا '
    'الوَجَعِ فَيَبْرَأَ» حَدِيثٌ حَسَنٌ رَوَاهُ أَبُو دَاوُدَ وَغَيْرُهُ.')
b += B.hadith(
    'رَبَّنَا اللهُ الَّذِي فِي السَّمَاءِ تَقَدَّسَ اسْمُكَ، أَمْرُكَ فِي السَّمَاءِ '
    'وَالأَرْضِ، كَمَا رَحْمَتُكَ فِي السَّمَاءِ اجْعَلْ رَحْمَتَكَ فِي الأَرْضِ، اغْفِرْ '
    'لَنَا حَوْبَنَا وَخَطَايَانَا، أَنْتَ رَبُّ الطَّيِّبِينَ، أَنْزِلْ رَحْمَةً مِنْ '
    'رَحْمَتِكَ وَشِفَاءً مِنْ شِفَائِكَ عَلَى هَذَا الوَجَعِ فَيَبْرَأَ',
    '"Our Lord is Allah, who is above the heaven. Hallowed be Your name. Your command is in the '
    'heaven and the earth. As Your mercy is in the heaven, place Your mercy in the earth. Forgive '
    'us our sin and our wrongs. You are the Lord of the pure. Send down a mercy from Your mercy '
    'and a healing from Your healing upon this pain, that it may be cured."',
    'حَدِيثٌ حَسَنٌ — graded ḥasan by the author; reported by Abū Dāwūd and others')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>the reciting over the sick person, seeking his '
      'cure</strong></em>. And al-Fawzān states the ruling in one sentence, which is worth having '
      'before the creed: <em>it is <strong>legislated when it is with the Qurʾān and with '
      'permitted supplications</strong>, and <strong>forbidden when it is with words of shirk or '
      'acts of shirk</strong>.</em>' % ar('فِي رُقْيَةِ المَرِيضِ')) +
    p('So the author\'s proof-text for the ʿuluww is <em>a bedside duʿāʾ</em>. That is itself part '
      'of the argument: this doctrine is not an abstraction defended in debate. '
      '<strong>It is what a Muslim says out loud over a sick child.</strong>'))
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>%s</strong></em>. And al-Fawzān gives the two '
      'ways of taking the %s, both of which arrive at the same place:'
      % (ar('رَبَّنَا اللهُ الَّذِي فِي السَّمَاءِ'), ar('عَلَى السَّمَاءِ'), ar('فِي'))) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>١</strong> <span dir="rtl" lang="ar">فِي</span> = '
    '<span dir="rtl" lang="ar">عَلَى</span></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">“above the heaven” '
    '— as in <span dir="rtl" lang="ar">فَسِيحُوا فِي الْأَرْضِ</span>, “travel '
    '<em>upon</em> the earth” (al-Tawbah 9:2), where nobody reads it as travelling '
    '<em>inside</em> the earth</td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>٢</strong> <span dir="rtl" lang="ar">فِي</span> in its own adverbial sense</td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">and then what is meant by '
    '“the heaven” is <strong>absolute height</strong> — i.e. “in the '
    'loftiness”</td></tr>'
    '</table></div>' +
    p('You met both readings in Lesson 16 on al-Mulk 67:16. <strong>The point of giving two is '
      'that the doctrine does not depend on winning a grammatical argument.</strong> Whichever '
      'way the particle is taken, Allah is above — and no reading available in Arabic puts Him '
      '<em>inside</em> a created heaven.'))
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>Your names are hallowed above every '
      'deficiency</strong></em>. And then a point of grammar with real reach: '
      '<em>it is <strong>a singular annexed</strong>, <strong>so it takes in all of the names of '
      'Allah</strong>.</em>' % ar('تَقَدَّسَ اسْمُكَ')) +
    p('A singular noun in a possessive construction generalises in Arabic. So the worshipper does '
      'not hallow one name and leave the rest; <strong>%s hallows every name He has</strong> — '
      'which is why the clause is enough on its own.' % ar('اسْمُكَ')) +
    p('<strong>%s</strong> — and al-Fawzān splits the command into the two kinds the student has '
      'met before: <em>Your <strong>%s</strong> command, <strong>from which all created things '
      'and all events arise</strong></em> — and of it is His saying:'
      % (ar('أَمْرُكَ فِي السَّمَاءِ وَالأَرْضِ'), ar('الكَوْنِيُّ القَدَرِيّ'))))
b += B.ayah(
    'إِنَّمَا أَمْرُهُ إِذَا أَرَادَ شَيْئًا أَنْ يَقُولَ لَهُ كُنْ فَيَكُونُ',
    '"His command, when He intends a thing, is only that He says to it: be — and it is."',
    'Sūrat Yā-Sīn 36:82 · سورة يس')
b += B.sharh(
    p('<em>— and Your <strong>%s</strong> command, <strong>comprising the legislations which He '
      'legislated for His servants.</strong></em>' % ar('الشَّرْعِيّ')) +
    p('The same division as the two kinds of <em>irādah</em> in Lesson 11 and the two kinds of '
      '<em>ʿibādah</em> on the Islam 101 track: <strong>what He decrees, and what He '
      'commands.</strong> The duʿāʾ says His command runs in the heaven and the earth — and both '
      'senses are true at once.') +
    p('<strong>%s</strong> — <em>this is <strong>a seeking of nearness to Him by His '
      'mercy</strong>, which encompassed all the people of the heavens, <strong>that He should '
      'make a share of it for the people of the earth.</strong></em>'
      % ar('كَمَا رَحْمَتُكَ فِي السَّمَاءِ اجْعَلْ رَحْمَتَكَ فِي الأَرْضِ')))
b += B.sharh(
    p('<strong>%s</strong> — <em>this is a <strong>request for forgiveness</strong>; and %s is '
      '<strong>the covering over, and the shielding from the sin</strong>.</em>'
      % (ar('اغْفِرْ لَنَا حَوْبَنَا وَخَطَايَانَا'), ar('المَغْفِرَة'))) +
    p('And then the etymology, which is the kind of detail that makes a word impossible to forget: '
      '<em>and from it is <strong>%s</strong> — <strong>the helmet worn upon the head, because it '
      'covers it and shields it from the blow.</strong></em>' % ar('المِغْفَر')) +
    p('So <em>maghfirah</em> is not an erasure of the record; the root is '
      '<strong>armour</strong>. To ask Allah\'s forgiveness is to ask Him to put something between '
      'you and what your sin would otherwise do to you.') +
    p('<strong>%s</strong> — <em>is <strong>the sin</strong></em>; and <strong>%s</strong> are '
      '<em>the wrongs</em>. <strong>%s</strong> — <em>this is <strong>another seeking of '
      'nearness</strong>; and al-ṭayyibīn is the plural of %s, and <strong>they are the prophets '
      'and their followers</strong>. And the ascribing of His lordship to these is '
      '<strong>an ascription of honour and ennobling</strong> — otherwise He سبحانه is the Lord '
      'of everything and its Owner.</em>'
      % (ar('الحَوْب'), ar('الخَطَايَا'), ar('أَنْتَ رَبُّ الطَّيِّبِينَ'), ar('طَيِّب'))) +
    p('That last note is the same precision al-Fawzān applied to %s in Lesson 15: naming a '
      'particular group as His does not narrow His lordship — <strong>it honours them.</strong>'
      % ar('عَلَى عَبْدِهِ')))

b += B.heading('نَوْعَا رَحْمَةِ الله', 'The Two Kinds of Allah’s Mercy')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>the created mercy</strong></em>. And here '
      'al-Fawzān makes a distinction the student must have, or half the texts of mercy will be '
      'misread: <em><strong>the mercy of Allah is of two kinds:</strong></em>'
      % ar('أَنْزِلْ رَحْمَةً مِنْ رَحْمَتِكَ')) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .75rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>النَّوْعُ الأَوَّل</strong></td>'
    '<td style="padding:.6rem .75rem;border:1px solid var(--line)">'
    '<strong>His mercy which is an attribute of His attributes</strong> — as in '
    '<span dir="rtl" lang="ar">وَرَحْمَتِي وَسِعَتْ كُلَّ شَيْءٍ</span> '
    '(al-Aʿrāf 7:156)</td></tr>'
    '<tr><td style="padding:.6rem .75rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>النَّوْعُ الثَّانِي</strong></td>'
    '<td style="padding:.6rem .75rem;border:1px solid var(--line)">'
    '<strong>a mercy ascribed to Him by the ascription of the created thing to its '
    'Creator</strong> — as in this ḥadīth, and as in the ḥadīth '
    '«<span dir="rtl" lang="ar">خَلَقَ اللهُ مِائَةَ رَحْمَةٍ</span>», '
    '<em>Allah created a hundred mercies</em> (reported by <strong>Muslim</strong> and '
    '<strong>al-Tirmidhī</strong>)</td></tr>'
    '</table></div>' +
    p('The test is the one al-Fawzān applies: <strong>a mercy that is <em>created</em>, or '
      '<em>sent down</em>, or <em>counted</em>, is of the second kind.</strong> An attribute is '
      'not created, not sent down, and not numbered at a hundred. So when the duʿāʾ says '
      '<em>send down a mercy from Your mercy</em>, it is asking for the created thing that comes '
      '<em>from</em> the attribute — which is why the wording is %s and not merely %s.'
      % (ar('مِنْ رَحْمَتِكَ'), ar('رَحْمَتَكَ'))) +
    p('<em>So he &#65018; asked his Lord to send down this mercy upon the sick person, for his '
      'need of it, <strong>that He might cure him by it.</strong></em>') +
    p('<strong>And the shāhid from the ḥadīth: the affirming of al-ʿuluww for Allah تعالى, and '
      'that He is above the heaven; and <em>al-ʿuluww is an attribute of the Essence</em>, as came '
      'before.</strong> That last clause is the distinction from Lesson 16 restated: ʿuluww '
      'belongs to the Essence, istiwāʾ to the Actions.'))
b += B.sharh(
    p('al-Fawzān then counts what else is in the duʿāʾ, and the list is a lesson in how to praise '
      'Allah before asking Him. <em>In the ḥadīth is <strong>the seeking of nearness to Allah '
      'تعالى by praising Him</strong></em> —') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.93rem">'
    '<p style="margin:0">by <strong>His lordship</strong> '
    '(<span dir="rtl" lang="ar">رَبَّنَا</span>) · <strong>His godhood</strong> '
    '(<span dir="rtl" lang="ar">اللهُ</span>) · <strong>His holiness</strong> '
    '(<span dir="rtl" lang="ar">تَقَدَّسَ اسْمُكَ</span>) · <strong>His highness</strong> '
    '(<span dir="rtl" lang="ar">الَّذِي فِي السَّمَاءِ</span>) · <strong>the generality of '
    'His command</strong> (<span dir="rtl" lang="ar">أَمْرُكَ فِي السَّمَاءِ '
    'وَالأَرْضِ</span>) · and <strong>His mercy</strong> — <em>and then in the '
    'ḥadīth is the request for forgiveness from Allah, and the healing of the '
    'illness.</em></p></div>' +
    p('Six praises, then two requests. <strong>The creed is not an appendix to the duʿāʾ; it is '
      'the first two-thirds of it.</strong>'))

b += B.heading('«وَأَنَا أَمِينُ مَنْ فِي السَّمَاءِ»',
               '"And I Am the Trustee of Him Who Is above the Heaven"')
b += B.matn('وَقَوْلُهُ ﷺ: «أَلَا تَأْمَنُونِي وَأَنَا أَمِينُ مَنْ فِي السَّمَاءِ».')
b += B.hadith(
    'أَلَا تَأْمَنُونِي وَأَنَا أَمِينُ مَنْ فِي السَّمَاءِ',
    '"Will you not trust me, when I am the trustee of Him who is above the heaven?"',
    'al-Fawzān comments on it without restating a source at this point')
b += B.sharh(
    '<div style="background:#fff8e6;border-right:4px solid #d4a017;'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .9rem">'
    '<p style="margin:0;font-size:.9rem"><strong dir="rtl" lang="ar">تَنْبِيهٌ</strong> — '
    'al-Fawzān explains this ḥadīth’s wording <strong>without restating a '
    'source or a grading for it here</strong>, having given gradings for the texts around it. '
    'This page therefore <strong>does not supply a grading of its own</strong>, per the rule set '
    'out in Lesson 22: the ḥadīth is among those the author brought under his own '
    'condition — <em>the authentic aḥādīth which the people of knowledge '
    'received with acceptance</em> — and the ʿuluww it evidences rests on the other '
    'three texts of this section as well.</p></div>' +
    p('<strong>%s</strong> — <em>this is an address from him &#65018; '
      '<strong>to the one who objected against him regarding some of his distribution of '
      'wealth</strong></em>. And <strong>%s</strong> is <em>a particle of opening and of calling '
      'to attention</em>.' % (ar('أَلَا تَأْمَنُونِي'), ar('أَلَا'))) +
    p('<strong>%s</strong> — <em>from %s, and it is <strong>the absence of favouritism and of '
      'betrayal</strong></em>; that is: <em>will you not trust me in the distribution of the '
      'wealth?</em>' % (ar('تَأْمَنُونِي'), ar('الأَمَانَة'))) +
    p('<strong>%s</strong> — <em>and He is Allah سبحانه. <strong>He has entrusted me with His '
      'revelation, and His message, and the conveying of His law</strong> — '
      '<strong>and that suffices as a testimony to his trustworthiness and his truthfulness '
      '&#65018;.</strong></em>' % ar('وَأَنَا أَمِينُ مَنْ فِي السَّمَاءِ')) +
    p('The argument is one a child can follow and an objector cannot escape. '
      '<strong>The man was questioning the Prophet\'s &#65018; handling of money.</strong> And '
      'the reply is: the One above the heaven trusted me with His revelation — '
      '<em>and you are worried about the dates?</em>') +
    p('<strong>And the shāhid: the affirming of al-ʿuluww for Allah سبحانه — since he said '
      '%s</strong>, and the explanation of that phrase came just above.' % ar('مَنْ فِي السَّمَاءِ')))

b += B.vocab([
    ('الرُّقْيَة', 'al-ruqyah', 'reciting over the sick',
     'Legislated with the Qurʾān and permitted duʿāʾ; forbidden with '
     'words or acts of shirk'),
    ('تَقَدَّسَ اسْمُك', 'taqaddasa ismuk', 'hallowed be Your name',
     'A singular annexed — so it takes in ALL of His names'),
    ('الأَمْرُ الكَوْنِيّ', 'al-amr al-kawnī', 'the decreeing command',
     'From which all created things and events arise — كُنْ فَيَكُونُ'),
    ('المَغْفِرَة', 'al-maghfirah', 'forgiveness',
     'Covering over and shielding — from المِغْفَر, the helmet that shields the head'),
    ('الحَوْب', 'al-ḥawb', 'sin',
     'With الخَطَايَا, the wrongs'),
    ('الطَّيِّبُون', 'al-ṭayyibūn', 'the pure',
     'The prophets and their followers — an ascription of honour, not of restriction'),
    ('الرَّحْمَةُ المَخْلُوقَة', 'al-raḥmah al-makhlūqah', 'the created mercy',
     'The second kind — it is created, sent down and counted; an attribute is none of these'),
    ('الأَمَانَة', 'al-amānah', 'trustworthiness',
     'The absence of favouritism and of betrayal'),
])
b += B.mcq('ws-l26', [
    ('What does al-Fawzān say about the ruling of ruqyah?',
     ['It is forbidden in all cases',
      'Legislated when it is with the Qurʾān and permitted supplications; forbidden when it is '
      'with words or acts of shirk',
      'Permitted only for the Prophet ﷺ', 'Recommended only in Ramaḍān'], 1),
    ('Which āyah does al-Fawzān use to show %s can mean %s?'
     % (ar('فِي'), ar('عَلَى')),
      ['%s (al-Mulk 67:16)' % ar('مَنْ فِي السَّمَاءِ'),
       '%s — "travel upon the earth" (al-Tawbah 9:2)' % ar('فَسِيحُوا فِي الْأَرْضِ'),
       '%s (Yā-Sīn 36:82)' % ar('إِنَّمَا أَمْرُهُ'),
       '%s (al-Aʿrāf 7:156)' % ar('وَرَحْمَتِي وَسِعَتْ كُلَّ شَيْءٍ')], 1),
    ('Why does %s cover all of Allah’s names?' % ar('تَقَدَّسَ اسْمُكَ'),
     ['Because the name Allah comprises them all',
      'Because it is a singular noun in annexation, and such a construction generalises',
      'Because the ḥadīth says so explicitly',
      'Because the duʿāʾ is repeated three times'], 1),
    ('What is the test that distinguishes the created mercy from the attribute?',
     ['Whether it is mentioned in the Qurʾān or the Sunnah',
      'A mercy that is created, sent down or counted is the created kind — an attribute is none '
      'of those',
      'Whether it reaches the disbelievers',
      'Whether it is ascribed to Allah by a pronoun'], 1),
    ('What is the root-image behind %s?' % ar('المَغْفِرَة'),
     ['Washing away',
      'Covering and shielding — from المِغْفَر, the helmet that shields the head from the blow',
      'Weighing on a scale', 'Loosening a knot'], 1),
    ('What does al-Fawzān say about ascribing Allah’s lordship to %s?' % ar('الطَّيِّبِينَ'),
     ['That it restricts His lordship to the believers',
      'That it is an ascription of honour and ennobling — otherwise He is the Lord of everything',
      'That it refers to the angels only',
      'That it is a figure of speech'], 1),
    ('What was the context of %s?' % ar('أَلَا تَأْمَنُونِي'),
     ['A dispute over the direction of prayer',
      'Someone objecting against the Prophet ﷺ regarding some of his distribution of wealth',
      'A question about the Hour', 'A challenge from the hypocrites of Madīnah'], 1),
])
b += B.tf('ws-l26-tf', [
    ('مَعْنَى «فِي السَّمَاءِ» أَيْ: عَلَى السَّمَاءِ.',
     'The meaning of "in the heaven" is: above the heaven.', True),
    ('العُلُوُّ صِفَةٌ فِعْلِيَّةٌ.', 'Al-ʿuluww is an attribute of the Actions.', False),
    ('الرَّحْمَةُ المَذْكُورَةُ فِي «أَنْزِلْ رَحْمَةً مِنْ رَحْمَتِكَ» هِيَ الرَّحْمَةُ المَخْلُوقَةُ.',
     'The mercy in "send down a mercy from Your mercy" is the created mercy.', True),
    ('الرُّقْيَةُ بِأَلْفَاظٍ شِرْكِيَّةٍ جَائِزَةٌ لِلْحَاجَةِ.',
     'Ruqyah with words of shirk is permitted out of need.', False),
])
b += B.memorize(
    'رَبَّنَا اللهُ الَّذِي فِي السَّمَاءِ تَقَدَّسَ اسْمُكَ',
    'The opening of a duʿāʾ said over the sick — and the author\'s proof that Allah is above His '
    'creation. Learn it as both. A creed you would say at a bedside is a creed you actually hold.')
b += B.aiquiz('The uluww of Allah from the Sunnah in al-Aqidah al-Wasitiyyah: the ruqyah of the '
              'sick as a proof text, the two readings of alladhi fi al-samaa and why either '
              'yields the uluww, taqaddasa ismuka as a singular annexed covering all His names, '
              'the kawni and sharii command, maghfirah from al-mighfar the helmet, the two kinds '
              'of mercy with the test that a created mercy is sent down and counted, and ana '
              'aminu man fi al-samaa')
b += B.further()
b += B.nav('was-l25-qadam-nida-sawt.html', 'The Foot, and the Calling Out with a Voice',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l26')

io.open(os.path.join(B.AQ, 'was-l26-uluww-sunnah.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'العُلُوُّ فِي السُّنَّةِ · رُقْيَةُ المَرِيض',
    'The Highness in the Sunnah — the Ruqyah of the Sick',
    'Lesson 26 of al-ʿAqīdah al-Wāsiṭiyyah: a bedside '
    'duʿāʾ as the proof that Allah is above His creation, the two readings of '
    '“who is in the heaven,” why hallowing “Your name” covers every name, '
    'the two kinds of mercy and the test that tells them apart, and “I am the trustee of Him '
    'who is above the heaven.”',
    B.card('الوَاسِطِيَّة · الدَّرْسُ السَّادِسُ وَالعِشْرُون', '3',
           'العُلُوُّ فِي السُّنَّةِ · رُقْيَةُ المَرِيض',
           'The Highness in the Sunnah — the Ruqyah of the Sick', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l26-uluww-sunnah.html')
