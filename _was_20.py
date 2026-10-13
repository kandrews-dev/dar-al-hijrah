# -*- coding: utf-8 -*-
"""Wasitiyyah L20 -- section 22: the Qur'an is sent DOWN from Allah. The two
disbelieving objections around it -- that naskh is fabrication, and that a man
teaches him -- with the Qur'an's own answers. Sharh pp.84-86."""
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
    'Say why the author moves from %s to %s, and what the second adds.'
    % (ar('إِثْبَاتِ الكَلَامِ'), ar('إِثْبَاتِ التَّنْزِيلِ')),
    'Define %s and explain al-Fawzān’s account of the wisdom in it.' % ar('النَّسْخ'),
    'Answer the claim that a man was teaching the Prophet ﷺ, in the Qurʾān’s own terms.',
    'Show how the fact of %s is itself a proof of %s.' % (ar('الإِنْزَال'), ar('العُلُوّ')),
])

b += B.heading('٢٢ · إِثْبَاتُ تَنْزِيلِ القُرْآنِ مِنَ اللهِ تَعَالَى',
               'Section 22 — The Qurʾān Is Sent Down from Allah')
b += B.prose(
    'al-Fawzān marks the transition himself: <em>when the author رحمه الله had brought the āyāt '
    'indicating the affirming of speech for Allah تعالى, and that the Mighty Qurʾān is of His '
    'speech سبحانه, <strong>he then proceeded to set out the āyāt indicating that the Qurʾān is '
    'sent down from Allah.</strong></em> Lesson 19 settled <em>whose speech</em> it is; this '
    'section settles <em>how it reached us</em> — and, as it turns out, where it came from.')
b += B.matn(
    'وَقَوْلُهُ: ﴿وَهَذَا كِتَابٌ أَنْزَلْنَاهُ مُبَارَكٌ﴾، ﴿لَوْ أَنْزَلْنَا هَذَا '
    'الْقُرْآنَ عَلَى جَبَلٍ لَرَأَيْتَهُ خَاشِعًا مُتَصَدِّعًا مِنْ خَشْيَةِ اللَّهِ﴾، '
    '﴿وَإِذَا بَدَّلْنَا آيَةً مَكَانَ آيَةٍ وَاللَّهُ أَعْلَمُ بِمَا يُنَزِّلُ قَالُوا '
    'إِنَّمَا أَنْتَ مُفْتَرٍ بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ ۝ قُلْ نَزَّلَهُ رُوحُ '
    'الْقُدُسِ مِنْ رَبِّكَ بِالْحَقِّ لِيُثَبِّتَ الَّذِينَ آمَنُوا وَهُدًى وَبُشْرَى '
    'لِلْمُسْلِمِينَ ۝ وَلَقَدْ نَعْلَمُ أَنَّهُمْ يَقُولُونَ إِنَّمَا يُعَلِّمُهُ بَشَرٌ '
    'لِسَانُ الَّذِي يُلْحِدُونَ إِلَيْهِ أَعْجَمِيٌّ وَهَذَا لِسَانٌ عَرَبِيٌّ مُبِينٌ﴾.')
b += B.ayah(
    'وَهَذَا كِتَابٌ أَنْزَلْنَاهُ مُبَارَكٌ مُصَدِّقُ الَّذِي بَيْنَ يَدَيْهِ',
    '"And this is a Book We have sent down, blessed, confirming what came before it."',
    'Sūrat al-Anʿām 6:92 · سورة الأنعام')
b += B.sharh(
    p('al-Fawzān parses it before explaining it. <strong>%s</strong> is a demonstrative pointing '
      'to the Noble Qurʾān, and it is the <em>mubtadaʾ</em>; its <em>khabar</em> is '
      '<strong>%s</strong>; and <strong>%s</strong> are two descriptions of %s.'
      % (ar('هَذَا'), ar('كِتَابٌ'), ar('أَنْزَلْنَاهُ مُبَارَكٌ'), ar('كِتَاب'))) +
    p('And then an observation about word order that is worth more than it first looks: '
      '<strong>%s</strong> — <em>and He <strong>put the description of the sending-down '
      'first</strong>, because the disbelievers were denying it.</em>'
      % ar('وَقَدَّمَ صِفَةَ الإِنْزَالِ')) +
    p('The Qurʾān does not arrange its descriptions decoratively. Of the two things said about '
      'the Book — that it was sent down, and that it is blessed — the <em>contested</em> one is '
      'placed first. <strong>The order of the words answers the objection before the objection is '
      'stated.</strong>') +
    p('<strong>%s</strong> — <em>abundant in blessing, for what it comprises of religious and '
      'worldly benefits.</em>' % ar('المُبَارَك')))
b += B.ayah(
    'لَوْ أَنْزَلْنَا هَذَا الْقُرْآنَ عَلَى جَبَلٍ لَرَأَيْتَهُ خَاشِعًا مُتَصَدِّعًا مِنْ '
    'خَشْيَةِ اللَّهِ',
    '"Had We sent down this Qurʾān upon a mountain, you would have seen it humbled, split apart '
    'from fear of Allah."',
    'Sūrat al-Ḥashr 59:21 · سورة الحشر')
b += B.sharh(
    p('<em>This is an informing about the <strong>immensity</strong> of the Qurʾān, and that it is '
      'deserving that hearts should be humbled before it.</em> And al-Fawzān lays out the '
      'reasoning as a comparison from the greater to the lesser:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.93rem">For <em>if it were sent down upon a mountain</em> '
    '— <strong>along with its being at the utmost of hardness and the extreme of '
    'solidity</strong> — <em>were it to understand this Qurʾān, it would be '
    'humbled and would split apart out of fear of Allah, in wariness of His punishment.</em> '
    '<strong>So how is it fitting for you, O mankind, that your hearts should not soften and be '
    'humbled — and you have understood from Allah His command, and pondered His Book?!</strong></p></div>' +
    p('The force of it is in the aside about the mountain. A mountain is the hardest thing the '
      'listener can picture, and the āyah says even <em>that</em> would break. '
      '<strong>The comparison is not between a man and a mountain in strength, but in '
      'hardness</strong> — and it is the man who comes out harder.'))

b += B.heading('الشُّبْهَةُ الأُولَى · النَّسْخُ افْتِرَاء',
               'The First Objection — That Abrogation Is Fabrication')
b += B.ayah(
    'وَإِذَا بَدَّلْنَا آيَةً مَكَانَ آيَةٍ وَاللَّهُ أَعْلَمُ بِمَا يُنَزِّلُ قَالُوا '
    'إِنَّمَا أَنْتَ مُفْتَرٍ بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ',
    '"And when We substitute an āyah in place of an āyah — and Allah knows best what He sends '
    'down — they say: you are only a fabricator. Rather, most of them do not know."',
    'Sūrat al-Naḥl 16:101 · سورة النحل')
b += B.sharh(
    p('<em>This is a proceeding from Him سبحانه into mentioning a <strong>disbelieving '
      'objection</strong> surrounding the Noble Qurʾān, together with the refutation of it.</em>') +
    p('<strong>%s</strong> — and the definition is exact: <em>the meaning of %s is '
      '<strong>the lifting of a thing together with the placing of something else in its '
      'place</strong></em>; and <em>the substituting of an āyah is the lifting of it by another '
      'āyah besides it — <strong>and that is its abrogation</strong> by an āyah other than it.</em>'
      % (ar('بَدَّلْنَا'), ar('التَّبْدِيل'))) +
    p('<strong>%s</strong> — <em>that is: <strong>the disbelievers of Quraysh, who were ignorant '
      'of the wisdom in abrogation</strong></em>. <strong>%s</strong> — O Muḥammad — '
      '<strong>%s</strong> — <em>a liar, an inventor, speaking falsely against Allah</em>, '
      '<em>since you claim that He commanded you with a thing, and then you claim that He '
      'commanded you with its opposite.</em>'
      % (ar('قَالُوا'), ar('إِنَّمَا أَنْتَ'), ar('مُفْتَرٍ'))) +
    p('State the objection plainly and it is not a foolish one: <em>a message that changes its own '
      'rulings looks like a message its bearer is making up as he goes.</em> That is the charge, '
      'and the āyah does not dodge it.'))
b += B.sharh(
    p('<strong>So Allah refuted them with what conveys their ignorance</strong>, saying '
      '<strong>%s</strong> — which al-Fawzān reads in two possible ways: <em>they do not know '
      'anything of knowledge <strong>at all</strong>, or they do not know '
      '<strong>the wisdom in abrogation</strong>.</em>' % ar('بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ')) +
    p('And then the wisdom itself: <em>for it is <strong>built upon the benefits which Allah '
      'سبحانه knows</strong>. So there may be in the legislating of this thing '
      '<strong>a benefit limited to a time</strong>; then, after that time, the benefit lies in '
      'the legislating of something else.</em>') +
    p('That is the whole answer, and it is an answer about <em>knowledge</em>, not about '
      'consistency. A ruling fitted to a situation is not falsified when the situation changes — '
      'unless the one who gave it could not see the change coming. <strong>The objection assumes '
      'a legislator who does not know the future.</strong>') +
    p('al-Fawzān closes it with a sentence worth keeping: <em>and <strong>had the covering been '
      'lifted</strong> for these disbelievers, <strong>they would have known that this is the '
      'face of correctness, and the path of justice, and of gentleness, and of '
      'kindness.</strong></em> Not merely permissible — <em>kind</em>. The staged legislation was '
      'a mercy to the people it was staged for.'))
b += B.ayah(
    'قُلْ نَزَّلَهُ رُوحُ الْقُدُسِ مِنْ رَبِّكَ بِالْحَقِّ لِيُثَبِّتَ الَّذِينَ آمَنُوا '
    'وَهُدًى وَبُشْرَى لِلْمُسْلِمِينَ',
    '"Say: the Spirit of Holiness brought it down from your Lord in truth, to make firm those who '
    'believe — and as guidance and glad tidings for the Muslims."',
    'Sūrat al-Naḥl 16:102 · سورة النحل')
b += B.sharh(
    p('<em>Then He refuted them regarding their claim that this substituting was from Muḥammad, '
      'and that he was thereby a fabricator against Allah.</em> The answer names the chain of '
      'transmission: <strong>%s</strong> — <em>that is, the Qurʾān</em> — <strong>%s</strong> — '
      '<em>that is, <strong>Jibrīl</strong></em>.' % (ar('نَزَّلَهُ'), ar('رُوحُ الْقُدُسِ'))) +
    p('And a point of Arabic on the title: <strong>%s is purity</strong>, and the meaning is '
      '<em>the <strong>purified</strong> Spirit brought it down</em> — <em>so it is of the kind '
      'where <strong>the thing described is annexed to its own description</strong></em> '
      '(%s).' % (ar('القُدْس'), ar('إِضَافَةُ المَوْصُوفِ إِلَى صِفَتِه'))) +
    p('<strong>%s</strong> — <em>that is: <strong>the beginning of its sending down is from '
      'Allah</strong> سبحانه</em>. <strong>%s</strong> — <em>in the position of naṣb as a '
      'ḥāl</em>, that is: <em>characterised by being true</em>.'
      % (ar('مِنْ رَبِّكَ'), ar('بِالْحَقِّ'))) +
    p('So the āyah answers the charge by giving the route in full and in order: '
      '<strong>from your Lord → by Jibrīl → in truth</strong>. The Prophet &#65018; is not in the '
      'list of authors.') +
    p('<strong>%s</strong> — <em>upon faith; so they say: <strong>each of the abrogating and the '
      'abrogated is from our Lord.</strong></em> <em>And because, when they come to know the '
      'benefits in abrogation, they become firm upon faith.</em> And <strong>%s</strong> are '
      '<em>conjoined to the position of %s</em> — <em>that is: as a making firm for them, and a '
      'guidance, and glad tidings.</em>'
      % (ar('لِيُثَبِّتَ الَّذِينَ آمَنُوا'), ar('وَهُدًى وَبُشْرَى'), ar('لِيُثَبِّتَ'))) +
    p('Notice the inversion. The same feature of the revelation that the disbelievers took as '
      'proof of fraud is named here as what makes the believers <em>firm</em>. '
      '<strong>Naskh is not a difficulty the Qurʾān survives; it is listed among its '
      'mercies.</strong>'))

b += B.heading('الشُّبْهَةُ الثَّانِيَة · بَشَرٌ يُعَلِّمُه',
               'The Second Objection — That a Man Was Teaching Him')
b += B.ayah(
    'وَلَقَدْ نَعْلَمُ أَنَّهُمْ يَقُولُونَ إِنَّمَا يُعَلِّمُهُ بَشَرٌ لِسَانُ الَّذِي '
    'يُلْحِدُونَ إِلَيْهِ أَعْجَمِيٌّ وَهَذَا لِسَانٌ عَرَبِيٌّ مُبِينٌ',
    '"And We certainly know that they say: a man is only teaching him. The tongue of the one they '
    'incline towards is foreign, while this is a clear Arabic tongue."',
    'Sūrat al-Naḥl 16:103 · سورة النحل')
b += B.sharh(
    p('al-Fawzān spells out the objection in full, including the part of it that is an argument '
      'and not merely an insult: <em>these disbelievers say: <strong>a human being from the '
      'children of Ādam is teaching Muḥammad the Qurʾān, and not an angel from the '
      'angels</strong>. And this human who teaches him had studied the Torah, the Gospel and the '
      'foreign books — <strong>because Muḥammad is an unlettered man, and it is not possible that '
      'he should come with what is mentioned in the Qurʾān of the reports of the earliest '
      'generations.</strong></em>') +
    p('Grant them their premise and the inference is reasonable. An unlettered man in Makkah '
      'should not know the histories of Israel. <strong>So they posited a source.</strong> The '
      'Qurʾān\'s reply does not deny the premise — it examines the source they named.') +
    p('<strong>%s</strong> — <em>the tongue of the one they <strong>incline towards</strong>, and '
      'claim is teaching you, O Muḥammad, is <strong>foreign</strong></em> — that is, '
      '<em>non-Arab: <strong>he does not speak Arabic.</strong></em> '
      '<strong>%s</strong> — <em>and this Qurʾān possesses <strong>Arabic eloquence and clear '
      'expression</strong>.</em>' % (ar('لِسَانُ الَّذِي يُلْحِدُونَ إِلَيْهِ أَعْجَمِيٌّ'),
                                    ar('وَهَذَا لِسَانٌ عَرَبِيٌّ مُبِينٌ'))) +
    p('And then the question the āyah leaves them with, which al-Fawzān puts at full force: '
      '<em>so <strong>how do you claim that a human being from the non-Arabs teaches the Prophet '
      '&#65018;</strong> — when <strong>you yourselves</strong> were unable to oppose it, or to '
      'oppose a single sūrah or some sūrahs of it, <strong>and you are the people of the Arabic '
      'tongue, the men of eloquence, and the leaders of rhetoric?!</strong></em>') +
    p('The refutation has two blades and both are factual. Their candidate '
      '<strong>cannot speak the language the Book is in</strong>; and the acknowledged masters of '
      'that language <strong>could not produce the like of one sūrah of it</strong>. A foreigner '
      'is being credited with an Arabic the Arabs could not match.'))

b += B.heading('مَا يُسْتَفَادُ مِنَ الآيَات', 'What the Āyāt Yield')
b += B.sharh(
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.93rem">— <strong>the affirming that the Qurʾān '
    'is sent down from Allah</strong> تعالى, and that it is '
    '<strong>His speech</strong> جل وعلا — '
    '<em>not the speech of anyone else, of the angels or of mankind</em>; and '
    '<strong>the refutation of whoever claimed that it is created speech</strong>. And in the '
    'āyāt also is <strong>the affirming of al-ʿuluww for Allah</strong> '
    'سبحانه — <em>because the sending DOWN cannot be except '
    'from what is ABOVE.</em> واللهُ أعلم.</p></div>' +
    p('That last line is the quietest argument in the section and perhaps the most far-reaching. '
      'Nobody disputes that the Qurʾān was <em>sent down</em>; the word %s is on every page and '
      'in every creed, including those of the people who deny that Allah is above His creation. '
      '<strong>But a thing is only sent down from somewhere higher.</strong> So the ʿuluww of '
      'Lesson 16 is not resting only on the āyāt gathered for it — <strong>it is built into the '
      'vocabulary that everyone already uses about revelation.</strong>' % ar('أَنْزَلَ')))

b += B.vocab([
    ('التَّنْزِيل', 'al-tanzīl', 'the sending down',
     'And a sending DOWN can only be from what is ABOVE'),
    ('المُبَارَك', 'al-mubārak', 'blessed',
     'Abundant in blessing, for the religious and worldly benefits it comprises'),
    ('التَّبْدِيل', 'al-tabdīl', 'substitution',
     'Lifting a thing and putting another in its place — i.e. abrogation'),
    ('النَّسْخ', 'al-naskh', 'abrogation',
     'Built on benefits Allah knows: a ruling fitted to a time, then another'),
    ('مُفْتَرٍ', 'muftarin', 'a fabricator',
     'A liar, an inventor, speaking falsely against Allah — their charge'),
    ('رُوحُ القُدْس', 'rūḥ al-qudus', 'the Spirit of Holiness',
     'Jibrīl; القُدْس is purity — the purified Spirit'),
    ('إِضَافَةُ المَوْصُوفِ إِلَى صِفَتِه', 'iḍāfat al-mawṣūf ilā ṣifatih',
     'annexing the described to its description',
     'The construction in رُوحُ القُدْسِ'),
    ('أَعْجَمِيّ', 'aʿjamī', 'foreign, non-Arab',
     'Their candidate could not speak the language of the Book'),
])
b += B.mcq('ws-l20', [
    ('Why is the description %s placed before %s in al-Anʿām 6:92?'
     % (ar('أَنْزَلْنَاهُ'), ar('مُبَارَكٌ')),
     ['For reasons of rhyme',
      'Because the disbelievers were denying the sending-down — the contested description comes '
      'first',
      'Because blessing follows revelation in time',
      'Because مُبَارَك is the khabar'], 1),
    ('What is the force of the comparison in al-Ḥashr 59:21?',
     ['That mountains are stronger than men',
      'That even the hardest, most solid thing would split from fear — so how do human hearts, '
      'which have understood, stay unsoftened?',
      'That the Qurʾān was offered to the mountains first',
      'That mountains will be levelled on the Last Day'], 1),
    ('How does al-Fawzān define %s?' % ar('التَّبْدِيل'),
     ['Changing the wording while keeping the ruling',
      'The lifting of a thing together with the placing of something else in its place',
      'Reciting one āyah instead of another', 'Translating an āyah'], 1),
    ('What is the wisdom in abrogation, as al-Fawzān explains it?',
     ['That the earlier ruling was an error later corrected',
      'That it is built on benefits Allah knows: a benefit limited to a time, after which the '
      'benefit lies in legislating something else',
      'That it tests the believers’ obedience only',
      'That the Arabs demanded easier rulings'], 1),
    ('What does %s mean, and what construction is it?' % ar('رُوحُ الْقُدُسِ'),
     ['The Holy Qurʾān; a possessive annexation',
      'Jibrīl — القُدْس being purity, so "the purified Spirit": annexing the described to its '
      'description',
      'The soul of the believer; a descriptive annexation',
      'The Preserved Tablet; an appositive'], 1),
    ('What are the two parts of the answer to "a man is teaching him"?',
     ['That he was unlettered, and that he had no books',
      'That their candidate did not speak Arabic at all, and that the Arabs themselves — masters '
      'of the language — could not oppose even one sūrah of it',
      'That the man had died, and that the Qurʾān continued',
      'That angels brought it, and that men cannot see angels'], 1),
    ('How do these āyāt affirm al-ʿuluww?',
     ['By mentioning the Throne',
      'Because a sending DOWN can only be from what is ABOVE',
      'Because Jibrīl ascends', 'Because the mountain was humbled'], 1),
])
b += B.tf('ws-l20-tf', [
    ('قَدَّمَ اللهُ صِفَةَ الإِنْزَالِ لِأَنَّ الكُفَّارَ يُنْكِرُونَهَا.',
     'The description of the sending-down was placed first because the disbelievers denied it.',
     True),
    ('النَّسْخُ مَبْنِيٌّ عَلَى المَصَالِحِ الَّتِي يَعْلَمُهَا اللهُ.',
     'Abrogation is built upon benefits which Allah knows.', True),
    ('الَّذِي زَعَمُوا أَنَّهُ يُعَلِّمُ النَّبِيَّ ﷺ كَانَ عَرَبِيَّ اللِّسَانِ.',
     'The one they claimed was teaching the Prophet ﷺ was an Arabic speaker.', False),
    ('الإِنْزَالُ لَا يَكُونُ إِلَّا مِنْ أَعْلَى.',
     'A sending down can only be from what is above.', True),
])
b += B.memorize(
    'لَوْ أَنْزَلْنَا هَذَا الْقُرْآنَ عَلَى جَبَلٍ لَرَأَيْتَهُ خَاشِعًا مُتَصَدِّعًا مِنْ '
    'خَشْيَةِ اللَّهِ',
    'Read it as the argument it is, not as an image. The mountain is named because it is the '
    'hardest thing you can picture — and the āyah says even that would break. Then ask which of '
    'the two of you has actually understood the Book.')
b += B.aiquiz('The sending down of the Quran from Allah in al-Aqidah al-Wasitiyyah: why the '
              'description of the inzal is placed first, the argument of al-Hashr 59:21 from the '
              'hardness of the mountain, naskh defined and its wisdom in benefits limited to a '
              'time, Ruh al-Qudus as annexing the described to its description, the two-bladed '
              'answer to the claim that a man taught him, and how the inzal itself proves the '
              'uluww because a sending down can only be from above')
b += B.further()
b += B.nav('was-l19-quran-kalam-allah.html', 'The Qurʾān Is the Speech of Allah',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l20')

io.open(os.path.join(B.AQ, 'was-l20-tanzil-quran.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'تَنْزِيلُ القُرْآنِ مِنَ اللهِ تَعَالَى',
    'The Sending Down of the Qurʾān from Allah',
    'Lesson 20 of al-ʿAqīdah al-Wāsiṭiyyah: why the sending-down is '
    'described first, the argument from the hardness of the mountain, abrogation and the wisdom '
    'in it, the Qurʾān’s two-bladed answer to the claim that a man was teaching '
    'the Prophet ط, and how the inzāl itself proves that Allah is above His creation.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ العِشْرُون', '3',
           'تَنْزِيلُ القُرْآنِ مِنَ اللهِ تَعَالَى',
           'The Sending Down of the Qurʾān from Allah', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l20-tanzil-quran.html')
