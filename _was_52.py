# -*- coding: utf-8 -*-
"""Wasitiyyah L52 -- Part 7, the second closing fasl (first half): the
completers of the creed -- al-amr bi-l-ma'ruf, the shi'ar with the rulers
whoever they are, the congregations, nasihah, the two hadiths of the body and
the building, and sabr / shukr / rida. Sharh pp.195-197."""
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


def box(inner, wash='var(--brand-wash)', edge='var(--brand)'):
    return ('<div style="background:%s;border-right:4px solid %s;'
            'border-radius:var(--radius-sm);padding:var(--space-md);'
            'margin:0 0 .8rem">%s</div>' % (wash, edge, inner))


def row(k, v):
    return ('<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);'
            'white-space:nowrap;vertical-align:top"><strong>%s</strong></td>'
            '<td style="padding:.6rem .78rem;border:1px solid var(--line)">%s</td></tr>'
            % (k, v))


def table(rows, fs='.91rem'):
    return ('<div style="overflow-x:auto"><table style="width:100%%;'
            'border-collapse:collapse;font-size:%s;margin:0 0 .75rem">%s</table></div>'
            % (fs, ''.join(rows)))


b = B.objectives([
    'Explain why these manners are called %s, and what that says about the '
    'relation between creed and conduct.' % ar('مُكَمِّلَاتُ العَقِيدَة'),
    'State the order the Sharīʿah obliges in forbidding the wrong, and what the '
    'Muʿtazilah hold against it.',
    'Give the two reasons Ahl al-Sunnah hold the Ḥajj, the Jumuʿah and the ʿĪds with '
    'the rulers whether they are righteous or corrupt — and Ibn Taymiyyah’s observation '
    'about those who rebel.',
    'Define %s linguistically and in the Sharīʿah.' % ar('النَّصِيحَة'),
    'Explain why al-Fawzān says the ḥadīth of the body is %s.'
    % ar('خَبَرٌ مَعْنَاهُ الأَمْر'),
    'Give the three holdings-back that make up %s, and define %s.'
    % (ar('الصَّبْر'), ar('مُرُّ القَضَاء')),
])

# ------------------------------------------------------------------ framing
b += B.heading('فَصْلٌ · فِي بَيَانِ مُكَمِّلَاتِ العَقِيدَةِ مِنْ مَكَارِمِ '
               'الأَخْلَاق',
               'A Section on the Completers of the Creed, from Noble Character')
b += B.prose(
    '<em>This section is <strong>like a completion of the section before it</strong>; in '
    'it is a clarification of the qualities of Ahl al-Sunnah <strong>which are of the '
    'completers of the creed</strong>.</em> And the opening words carry the whole idea: '
    '<em>«%s» — that is: <strong>along with their standing by them in knowledge and in '
    'deed, they adorn themselves with qualities which are of their completers and their '
    'fruits.</strong></em>'
    % ar('ثُمَّ هُمْ مَعَ هَذِهِ الأُصُول'))
b += box(
    '<p style="margin:0;font-size:.95rem"><strong>Read that word %s carefully, because '
    'it decides how the whole section is to be taken.</strong> These manners are not a '
    'second subject appended to the creed once the creed is finished. They are what the '
    'creed <em>produces</em> — so a man’s conduct is evidence about his '
    '<em>ʿaqīdah</em>, and a creed that bears no such fruit is being held in some way '
    'other than the way Ahl al-Sunnah hold it.</p>'
    '<p style="margin:.6rem 0 0;font-size:.93rem">Which is why this, and not the '
    'attributes of Allah, is where a book of ʿaqīdah ends. '
    '<strong>The last word of the Wāsiṭiyyah is about character.</strong></p>'
    % ar('ثَمَرَاتُهَا'))
b += B.matn(
    'ثُمَّ هُمْ مَعَ هَذِهِ الأُصُولِ يَأْمُرُونَ بِالمَعْرُوفِ وَيَنْهَوْنَ عَنِ '
    'المُنْكَرِ عَلَى مَا تُوجِبُهُ الشَّرِيعَةُ، وَيَرَوْنَ إِقَامَةَ الحَجِّ '
    'وَالجُمَعِ وَالأَعْيَادِ مَعَ الأُمَرَاءِ أَبْرَارًا كَانُوا أَوْ فُجَّارًا، '
    'وَيُحَافِظُونَ عَلَى الجَمَاعَاتِ، وَيَدِينُونَ بِالنَّصِيحَةِ لِلْأُمَّةِ. '
    'وَيَعْتَقِدُونَ مَعْنَى قَوْلِهِ ﷺ: «المُؤْمِنُ لِلْمُؤْمِنِ كَالْبِنْيَانِ '
    'يَشُدُّ بَعْضُهُ بَعْضًا» وَشَبَّكَ بَيْنَ أَصَابِعِهِ، وَقَوْلِهِ ﷺ: «مَثَلُ '
    'المُؤْمِنِينَ فِي تَوَادِّهِمْ وَتَرَاحُمِهِمْ وَتَعَاطُفِهِمْ كَمَثَلِ '
    'الجَسَدِ، إِذَا اشْتَكَى مِنْهُ عُضْوٌ تَدَاعَى لَهُ سَائِرُ الجَسَدِ '
    'بِالحُمَّى وَالسَّهَرِ». وَيَأْمُرُونَ بِالصَّبْرِ عِنْدَ البَلَاءِ، '
    'وَالشُّكْرِ عِنْدَ الرَّخَاءِ، وَالرِّضَا بِمُرِّ القَضَاءِ.')

# ------------------------------------------------------------------ 1
b += B.heading('١ · الأَمْرُ بِالمَعْرُوفِ وَالنَّهْيُ عَنِ المُنْكَر',
               'Enjoining the Right and Forbidding the Wrong')
b += B.sharh(
    p('<em>As Allah described them with that in His saying:</em>'))
b += B.ayah(
    'كُنْتُمْ خَيْرَ أُمَّةٍ أُخْرِجَتْ لِلنَّاسِ تَأْمُرُونَ بِالْمَعْرُوفِ '
    'وَتَنْهَوْنَ عَنِ الْمُنْكَرِ وَتُؤْمِنُونَ بِاللَّهِ',
    '"You are the best nation brought forth for mankind: you enjoin the right, forbid '
    'the wrong, and believe in Allah."',
    'Sūrat Āl ʿImrān 3:110 · سُورَةُ آلِ عِمْرَان')
b += B.sharh(
    p('<em>And <strong>%s is a comprehensive name for everything Allah loves</strong></em> '
      'of sayings and of deeds. So the duty is not a list of causes; '
      '<strong>it is as wide as what Allah loves.</strong>' % ar('المَعْرُوف')) +
    p('Then the restriction the matn itself attaches — <strong>%s</strong>: '
      '<em>that is, <strong>by the hand, then by the tongue, then by the heart, '
      'according to ability and to maṣlaḥah</strong> — <strong>in opposition to the '
      'Muʿtazilah, who contravene what the Sharīʿah obliges in this.</strong></em>'
      % ar('عَلَى مَا تُوجِبُهُ الشَّرِيعَة')) +
    p('<strong>Two things in that order are easy to miss.</strong> The first is that it '
      'is an order <em>descending by capacity</em>: a man does what he is able to do and '
      'is not asked for what he cannot. The second is <strong>%s</strong> — the benefit. '
      'An act of forbidding that produces a greater evil than the one it removes is not '
      'what the Sharīʿah obliges, and that single word is what separates this clause '
      'from the next one.' % ar('المَصْلَحَة')))

# ------------------------------------------------------------------ 2
b += B.heading('٢ · إِقَامَةُ الشَّعَائِرِ مَعَ الأُمَرَاء',
               'Holding the Rites With the Rulers, Whoever They Are')
b += B.sharh(
    p('<em>That is: <strong>Ahl al-Sunnah hold the obligation of establishing these '
      'rites together with the guardians of the Muslims’ affairs</strong> — '
      '<strong>%s</strong>, that is: <strong>whether they are upright and righteous or '
      'corrupt — a corruption that does not take them out of the religion.</strong></em>'
      % ar('أَبْرَارًا كَانُوا أَوْ فُجَّارًا')) +
    p('<strong>That qualifying clause is load-bearing and it is the author’s own, not an '
      'apology added later.</strong> The ruling is about a sinful Muslim ruler. It says '
      'nothing about one who has left Islam, and so it cannot be quoted either way on a '
      'question it does not address.') +
    p('Then the two reasons:') +
    table([
        row('<strong>١</strong>',
            '<em>because <strong>the Muslims’ purpose in this is the gathering of the '
            'word, and distance from division and disagreement</strong></em>'),
        row('<strong>٢</strong>',
            '<em>and because <strong>the corrupt ruler is not deposed by his corruption, '
            'and rebelling against him is not permitted</strong> — because of what '
            'follows from that of <strong>the loss of rights and the spilling of '
            'blood</strong></em>'),
    ], fs='.92rem'))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem">And then al-Fawzān quotes the author '
    'of the matn himself, from elsewhere in his writings — an observation that is '
    'historical rather than theoretical:</p>'
    '<p style="margin:0;font-size:.95rem"><em>Shaykh al-Islām Ibn Taymiyyah رحمه الله '
    'said: <strong>«And perhaps hardly a party is known to have rebelled against a '
    'holder of authority but that in its rebellion there was more corruption than there '
    'was in what it removed.»</strong></em></p>'
    '<p style="margin:.6rem 0 0;font-size:.93rem">Notice the form of the argument. '
    '<strong>It is not a claim that rulers are good; it is a claim about what rebellion '
    'reliably costs.</strong> Ibn Taymiyyah does not deny the injustice being complained '
    'of — he grants it and weighs it against the price of the remedy. And he states it '
    'with the caution of a man reporting a pattern rather than asserting a law: '
    '<em>«perhaps hardly a party is known…»</em></p>')
b += B.sharh(
    p('<em>And Ahl al-Sunnah oppose in this the people of innovation, from '
      '<strong>the Khawārij, the Muʿtazilah and the Shīʿah</strong>, who hold the '
      'fighting of the guardians and rebelling against them <strong>if they do what is '
      'injustice — or supposed it to be injustice</strong> — and they regard that as '
      'being of the category of <strong>enjoining the right and forbidding the '
      'wrong.</strong></em>') +
    p('<strong>That parenthesis — «or supposed it to be injustice» — is the whole '
      'difficulty in four words.</strong> A rebellion is not launched upon a proven '
      'wrong; it is launched upon a wrong as the rebel judges it. And the groups named '
      'do not think of themselves as abandoning the Sharīʿah: '
      '<strong>they file their rebellion under the very duty of the previous '
      'clause.</strong> Which is why the matn put <em>%s</em> into that clause before '
      'arriving at this one.' % ar('عَلَى مَا تُوجِبُهُ الشَّرِيعَة')))

# ------------------------------------------------------------------ 3-4
b += B.heading('٣ · المُحَافَظَةُ عَلَى الجَمَاعَاتِ · ٤ · النَّصِيحَةُ لِلْأُمَّة',
               'Guarding the Congregations · and Sincere Counsel to the Ummah')
b += B.sharh(
    p('<em>That is: <strong>they guard attending the obligatory prayer in congregation, '
      'the Jumuʿah and other than it, because that is of the greatest of the emblems of '
      'Islam</strong>, and an obedience to Allah and His Messenger in it.</em>') +
    table([
        row('<span dir="rtl" lang="ar">خِلَافًا لِلشِّيعَة</span>',
            '<em>who <strong>do not hold the prayer except with the infallible '
            'imām</strong></em>'),
        row('<span dir="rtl" lang="ar">وَخِلَافًا لِلْمُنَافِقِين</span>',
            '<em>who <strong>stay away from the congregational prayer</strong></em>'),
    ], fs='.92rem') +
    p('<strong>Those two are placed side by side on purpose.</strong> One abandons the '
      'congregation out of a doctrine and one out of hypocrisy — and the matn is '
      'indifferent to the reason, because the Sunnah is the attendance either way. '
      '<em>And ḥadīths have come on the excellence of the congregational prayer, the '
      'command to it and the prohibition of abandoning it; this is not the place to '
      'mention them.</em>') +
    p('<em>And <strong>%s</strong> — that is: <strong>they regard it as part of the '
      'religion.</strong></em>' % ar('يَدِينُونَ بِالنَّصِيحَةِ لِلْأُمَّة')) +
    table([
        row('<span dir="rtl" lang="ar">لُغَةً</span>',
            '<em>and the root of <strong>النُّصْح</strong> in the language is '
            '<strong>الخُلُوص — purity, being unmixed</strong></em>'),
        row('<span dir="rtl" lang="ar">شَرْعًا</span>',
            '<em><strong>wanting good for the one counselled, and directing him to what '
            'is in his interests</strong></em>'),
    ], fs='.92rem') +
    p('<strong>The etymology is the test.</strong> If naṣīḥah is from <em>purity</em>, '
      'then advice mixed with the wish to humiliate, to win, or to be seen advising is '
      'not naṣīḥah at all — whatever is true in its content. <em>So Ahl al-Sunnah want '
      'good for the Ummah, and direct it to what its welfare lies in.</em>'))

# ------------------------------------------------------------------ 5
b += B.heading('٥ · التَّعَاوُنُ وَالتَّأَلُّمُ لِأَلَمِ المُصَابِين',
               'Cooperation, and Feeling the Pain of the Afflicted')
b += B.hadith(
    'المُؤْمِنُ لِلْمُؤْمِنِ كَالْبِنْيَانِ يَشُدُّ بَعْضُهُ بَعْضًا',
    '"The believer to the believer is like a building, each part of it bracing the '
    'other" — and he ﷺ interlaced his fingers.',
    'رَوَاهُ البُخَارِيُّ وَمُسْلِمٌ')
b += B.hadith(
    'مَثَلُ المُؤْمِنِينَ فِي تَوَادِّهِمْ وَتَرَاحُمِهِمْ وَتَعَاطُفِهِمْ كَمَثَلِ '
    'الجَسَدِ، إِذَا اشْتَكَى مِنْهُ عُضْوٌ تَدَاعَى لَهُ سَائِرُ الجَسَدِ '
    'بِالحُمَّى وَالسَّهَرِ',
    '"The likeness of the believers in their mutual love, mercy and tenderness is the '
    'likeness of the body: when one limb of it is in pain, the rest of the body is '
    'summoned to it with fever and sleeplessness."',
    'رَوَاهُ البُخَارِيُّ وَمُسْلِمٌ وَغَيْرُهُمَا')
b += B.sharh(
    p('<em>So <strong>the two ḥadīths depict what the Muslims ought to be upon of '
      'cooperation and mutual mercy</strong>; and Ahl al-Sunnah act by what the two of '
      'them require.</em> Then al-Fawzān goes through the wording:') +
    table([
        row(ar('المُؤْمِنُ لِلْمُؤْمِن'),
            '<em>and <strong>%s</strong> — what is intended by īmān here is '
            '<strong>the complete īmān</strong></em>' % ar('مَثَلُ المُؤْمِنِين')),
        row(ar('كَالْبِنْيَان'),
            '<em>this likening is intended for <strong>bringing it near to the '
            'understanding</strong></em>'),
        row(ar('يَشُدُّ بَعْضُهُ بَعْضًا'),
            '<em>a clarification of <strong>the point of resemblance</strong></em>'),
        row(ar('وَشَبَّكَ بَيْنَ أَصَابِعِه'),
            '<em><strong>another likening</strong>, also intended to bring it near to '
            'the understanding</em>'),
        row(ar('كَمَثَلِ الجَسَد'),
            '<em>that is: <strong>with respect to all of its limbs, in regard to the '
            'feeling of ease or of weariness</strong></em>'),
        row(ar('تَوَادِّهِم'), '<em>the love of one another</em>'),
        row(ar('تَعَاطُفِهِم'), '<em>the tenderness of one toward another</em>'),
        row(ar('اشْتَكَى'), '<em>was in pain</em>'),
        row(ar('تَدَاعَى'),
            '<em><strong>one part of it shared with the other part in the '
            'pain</strong></em>'),
        row(ar('سَائِرُ الجَسَد'), '<em>the rest of it</em>'),
        row(ar('بِالحُمَّى'),
            '<em>what arises from the pain of heat in the body</em>'),
        row(ar('السَّهَر'), '<em>sleeplessness</em>'),
    ], fs='.9rem'))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem"><strong>And then the observation that '
    'makes the ḥadīth a duty rather than a description:</strong></p>'
    '<p style="margin:0;font-size:.95rem"><em>— <strong>and this ḥadīth is a statement '
    'whose meaning is a command</strong>. That is: just as, when part of his body is in '
    'pain, that pain spreads to the whole of his body — <strong>so too the believers, '
    'that they may be as a single soul: when a calamity strikes one of them, all of them '
    'grieve, and they work at removing it.</strong></em></p>'
    '<p style="margin:.6rem 0 0;font-size:.93rem"><strong>%s</strong> — a grammatical '
    'observation doing moral work. The Prophet ﷺ did not say «feel for one another»; he '
    'said <em>this is what you are like</em>. '
    '<strong>So a man who does not feel it is not merely failing a duty — he is '
    'contradicting a description of himself</strong>, which is a sharper thing to be '
    'told. <em>And in this comparison is a bringing-near to the understanding, and a '
    'showing-forth of meanings in visible forms.</em></p>'
    % ar('خَبَرٌ مَعْنَاهُ الأَمْر'))

# ------------------------------------------------------------------ 6
b += B.heading('٦ · الثَّبَاتُ فِي مَوَاقِفِ الامْتِحَان',
               'Standing Firm in the Places of Testing')
b += B.sharh(
    p('<em>And of the qualities of Ahl al-Sunnah: <strong>their firmness in the '
      'situations of testing</strong></em> — and the matn gives three, one for each kind '
      'of circumstance a man meets: <strong>hardship, ease, and what he simply cannot '
      'alter.</strong>'))
b += B.sharh(
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .75rem">'
    '<tr><td style="padding:.7rem .8rem;border:1px solid var(--line);vertical-align:top;'
    'width:30%"><strong dir="rtl" lang="ar">الصَّبْرُ عِنْدَ البَلَاء</strong><br>'
    '<span style="font-size:.84rem"><em>البَلَاء: the testing by calamities and '
    'hardships</em></span></td>'
    '<td style="padding:.7rem .8rem;border:1px solid var(--line)">'
    '<em>الصَّبْر <strong>linguistically: الحَبْس — holding back</strong>; and its '
    'meaning here is <strong>three holdings-back at once</strong>:<br>'
    '— <strong>holding the soul back from anguish</strong><br>'
    '— <strong>holding the tongue back from complaining and from discontent</strong><br>'
    '— <strong>holding the limbs back from striking the cheeks and tearing the '
    'garments</strong></em></td></tr>'
    '<tr><td style="padding:.7rem .8rem;border:1px solid var(--line);vertical-align:top">'
    '<strong dir="rtl" lang="ar">الشُّكْرُ عِنْدَ الرَّخَاء</strong><br>'
    '<span style="font-size:.84rem"><em>الرَّخَاء: the widening of blessing</em></span>'
    '</td>'
    '<td style="padding:.7rem .8rem;border:1px solid var(--line)">'
    '<em>الشُّكْر: <strong>an act that announces the magnifying of the Bestower, because '
    'He is the Bestower</strong> — <strong>and it is the servant’s expending of what '
    'Allah has favoured him with in obedience to Him</strong></em></td></tr>'
    '<tr><td style="padding:.7rem .8rem;border:1px solid var(--line);vertical-align:top">'
    '<strong dir="rtl" lang="ar">الرِّضَا بِمُرِّ القَضَاء</strong><br>'
    '<span style="font-size:.84rem"><em>الرِّضَا: the opposite of '
    'السَّخَط</em></span></td>'
    '<td style="padding:.7rem .8rem;border:1px solid var(--line)">'
    '<em>القَضَاء <strong>linguistically: the ruling</strong>; and in usage: '
    '<strong>the will of Allah connected to things as they are</strong>. '
    '<strong>And مُرُّ القَضَاء is what passes over the servant of what he dislikes</strong> '
    '— <strong>such as sickness, poverty, the harm of people, heat, cold, and '
    'pains.</strong></em></td></tr>'
    '</table></div>')
b += B.prose(
    'Set the definition of <strong>شُكْر</strong> beside the definition of '
    '<strong>صَبْر</strong> and the symmetry appears. <strong>Ṣabr is defined entirely '
    'by restraint, and shukr entirely by expenditure</strong> — the one is three things '
    'a man holds <em>in</em>, the other is everything he has, spent <em>outward</em> in '
    'obedience. Which is the answer to a common confusion: gratitude in this definition '
    'is not a warm feeling about a blessing. <strong>It is the use the blessing is put '
    'to.</strong> A man who says «al-ḥamdu lillāh» over wealth he spends in disobedience '
    'has not performed shukr by the definition at all.')
b += B.prose(
    'And notice that the third is the hardest, which is why it is placed last. '
    'Ṣabr is asked of a man in a calamity and shukr in ease — <strong>but riḍā is asked '
    'of him about the bitterness itself.</strong> Not that he should like sickness or '
    'poverty, which the definition of مُرّ concedes he dislikes, but that '
    '<strong>he should not be displeased with the Decree that brought it</strong>. '
    'That is a station above patience, and it belongs here because Part 5 established '
    'what the Decree is.')

b += B.vocab([
    ('مُكَمِّلَاتُ العَقِيدَة', 'mukammilāt al-ʿaqīdah', 'the completers of the creed',
     'Qualities that are the creed’s ثَمَرَات, its fruits — so conduct is evidence '
     'about belief, not an appendix to it'),
    ('المَعْرُوف', 'al-maʿrūf', 'the right, the recognized good',
     'اسْمٌ جَامِعٌ لِكُلِّ مَا يُحِبُّهُ اللهُ — a comprehensive name for everything '
     'Allah loves, of sayings and of deeds'),
    ('المَصْلَحَة', 'al-maṣlaḥah', 'benefit, welfare',
     'The second half of «according to ability and maṣlaḥah» — a forbidding that '
     'produces a greater evil is not what the Sharīʿah obliges'),
    ('النُّصْح', 'al-nuṣḥ', 'sincere counsel',
     'لُغَةً الخُلُوص, purity; شَرْعًا wanting good for the one counselled and directing '
     'him to his interests'),
    ('تَدَاعَى', 'tadāʿā', 'was summoned together',
     'One part of the body shared with the other in the pain — the verb that makes the '
     'likeness work'),
    ('الحُمَّى', 'al-ḥummā', 'fever',
     'What arises from the pain of heat in the body; paired with السَّهَر, sleeplessness'),
    ('الصَّبْر', 'al-ṣabr', 'patience',
     'لُغَةً الحَبْس, holding back — of the soul from anguish, the tongue from '
     'complaint, and the limbs from striking the cheeks'),
    ('الشُّكْر', 'al-shukr', 'gratitude',
     'An act announcing the magnifying of the Bestower — the servant’s expending of what '
     'he was favoured with in obedience'),
    ('القَضَاء', 'al-qaḍāʾ', 'the decree',
     'لُغَةً الحُكْم, the ruling; عُرْفًا إِرَادَةُ اللهِ المُتَعَلِّقَةُ '
     'بِالأَشْيَاءِ عَلَى مَا هِيَ عَلَيْه'),
    ('مُرُّ القَضَاء', 'murr al-qaḍāʾ', 'the bitterness of the decree',
     'What passes over the servant of what he dislikes — sickness, poverty, the harm of '
     'people, heat, cold and pains'),
])
b += B.mcq('ws-l52', [
    ('Why are these manners called مُكَمِّلَاتُ العَقِيدَة?',
     ['Because they are optional refinements once the creed is settled',
      'Because they are the creed’s completers and its FRUITS — so conduct is evidence '
      'about belief rather than an appendix to it',
      'Because they complete the obligations of the Sharīʿah',
      'Because they were added by later scholars'], 1),
    ('What is المَعْرُوف?',
     ['The five pillars specifically',
      'A comprehensive name for everything Allah loves, of sayings and of deeds — so the '
      'duty is as wide as what He loves',
      'What the scholars of an age have agreed upon',
      'What is customary among the Muslims'], 1),
    ('What order does «according to what the Sharīʿah obliges» impose?',
     ['By the tongue only, never by the hand',
      'By the hand, then the tongue, then the heart — according to ability and to '
      'maṣlaḥah',
      'By the heart first, then the tongue, then the hand',
      'By whichever means is most effective'], 1),
    ('What does the word مَصْلَحَة add to the duty?',
     ['That the one forbidding must be a scholar',
      'That a forbidding which produces a greater evil than the one it removes is not '
      'what the Sharīʿah obliges',
      'That the wrong must be public',
      'That it must be done in private first'], 1),
    ('What qualification does al-Fawzān attach to «righteous or corrupt»?',
     ['That the ruler must be a descendant of Quraysh',
      'A corruption that does not take them out of the religion — so the ruling concerns '
      'a sinful Muslim ruler and addresses nothing else',
      'That it applies only to the Jumuʿah, not the Ḥajj',
      'That the ruler must have been appointed by consultation'], 1),
    ('What are the two reasons given for holding the rites with them?',
     ['That the rites are invalid otherwise, and that the ruler owns the mosques',
      'That the Muslims’ purpose is the gathering of the word and distance from '
      'division; and that a corrupt ruler is not deposed by his corruption, rebellion '
      'bringing the loss of rights and the spilling of blood',
      'That obedience to rulers is unconditional, and that patience is rewarded',
      'That the Companions did so, and that the scholars agreed'], 1),
    ('What exactly does Ibn Taymiyyah’s observation claim?',
     ['That all rulers are righteous',
      'That hardly a party is known to have rebelled but that its rebellion held more '
      'corruption than what it removed — a claim about what rebellion costs, not about '
      'the ruler’s goodness',
      'That rebellion is disbelief',
      'That injustice must be denied rather than weighed'], 1),
    ('What four words identify the real difficulty with the Khawārij position?',
     ['«if they do what is injustice»',
      '«or supposed it to be injustice» — a rebellion is launched on a wrong as the '
      'rebel judges it',
      '«they regard that as enjoining the right»',
      '«the fighting of the guardians»'], 1),
    ('Under what duty do the Khawārij, Muʿtazilah and Shīʿah file their rebellion?',
     ['Jihād in the path of Allah',
      'Enjoining the right and forbidding the wrong — which is why the matn restricted '
      'that duty to what the Sharīʿah obliges BEFORE arriving at this clause',
      'The obligation of hijrah',
      'Commanding obedience to the infallible imām'], 1),
    ('What is النُّصْح linguistically, and why does it matter?',
     ['From النَّصْب, effort — so advice must be laborious',
      'From الخُلُوص, purity — so advice mixed with the wish to humiliate or to be seen '
      'advising is not naṣīḥah at all, whatever is true in its content',
      'From النَّصِيب, a share — so each Muslim owes a portion',
      'From النَّصّ, a text — so advice must cite evidence'], 1),
    ('What does al-Fawzān mean by calling the ḥadīth of the body خَبَرٌ مَعْنَاهُ '
     'الأَمْر?',
     ['That its chain is weaker than its meaning suggests',
      'That it is phrased as a statement of what believers ARE like, so a man who does '
      'not feel it contradicts a description of himself rather than merely failing a '
      'duty',
      'That its command was abrogated',
      'That it applies only to those of complete īmān'], 1),
    ('What are the three holdings-back that make up ṣabr?',
     ['Of the eyes, the ears and the tongue',
      'Of the soul from anguish, the tongue from complaining and discontent, and the '
      'limbs from striking the cheeks and tearing the garments',
      'Of the hand, the tongue and the heart',
      'Of food, drink and speech'], 1),
    ('How is shukr defined here, and what follows from it?',
     ['As saying al-ḥamdu lillāh upon receiving a blessing',
      'As an act announcing the magnifying of the Bestower — the servant’s expending of '
      'what he was favoured with IN OBEDIENCE; so it is the use a blessing is put to, '
      'not a feeling about it',
      'As refraining from complaint in times of ease',
      'As distributing a fifth of one’s wealth'], 1),
    ('What is asked of a man by الرِّضَا بِمُرِّ القَضَاء?',
     ['That he should like sickness and poverty',
      'Not that he should like them — the word مُرّ concedes he dislikes them — but that '
      'he should not be displeased with the Decree that brought them',
      'That he should not seek a remedy',
      'That he should conceal his affliction from people'], 1),
])
b += B.tf('ws-l52-tf', [
    ('مَكَارِمُ الأَخْلَاقِ ثَمَرَةٌ لِلْعَقِيدَةِ لَا شَيْءٌ زَائِدٌ عَلَيْهَا.',
     'Noble character is a fruit of the creed, not something added on top of it.', True),
    ('النَّهْيُ عَنِ المُنْكَرِ وَاجِبٌ بِالْيَدِ وَلَوْ أَفْضَى إِلَى مُنْكَرٍ '
     'أَعْظَمَ.',
     'Forbidding the wrong by the hand is obligatory even if it leads to a greater '
     'wrong.', False),
    ('الوَالِي الفَاسِقُ يَنْعَزِلُ بِفِسْقِهِ.',
     'A corrupt ruler is deposed by his corruption.', False),
    ('أَصْلُ النُّصْحِ فِي اللُّغَةِ الخُلُوصُ.',
     'The root of naṣīḥah in the language is purity.', True),
    ('الشُّكْرُ صَرْفُ العَبْدِ مَا أَنْعَمَ اللهُ بِهِ عَلَيْهِ فِي طَاعَتِهِ.',
     'Shukr is the servant’s expending of what Allah favoured him with in obedience to '
     'Him.', True),
])
b += B.memorize(
    'الصَّبْرُ عِنْدَ البَلَاءِ، وَالشُّكْرُ عِنْدَ الرَّخَاءِ، وَالرِّضَا بِمُرِّ '
    'القَضَاء',
    'Three circumstances, and between them they exhaust a life: '
    '<strong>what hurts you, what pleases you, and what you cannot change.</strong> '
    'Ṣabr is three things held in; shukr is everything you have spent outward in '
    'obedience; and riḍā is asked about the bitterness itself — not that you should like '
    'it, but that you should not be displeased with the One who decreed it. '
    '<strong>A creed that does not produce these three has not been understood, however '
    'accurately it is recited.</strong>')
b += B.aiquiz('The completers of the creed in al-Aqidah al-Wasitiyyah: why noble '
              'character is called mukammilat and thamarat of the aqidah, al-maruf as a '
              'comprehensive name for all Allah loves, the order by the hand then the '
              'tongue then the heart according to ability and maslahah against the '
              'Mutazilah, holding the Hajj and Jumuah and the Ids with rulers righteous '
              'or corrupt with the qualification that the corruption does not take them '
              'out of the religion, the two reasons and Ibn Taymiyyahs observation that '
              'hardly a party rebelled but that its rebellion held more corruption than '
              'it removed, the four words or supposed it to be injustice, guarding the '
              'congregations against the Shia and the hypocrites, nasihah from al-khulus '
              'meaning purity, the two hadiths of the building and the body with the '
              'point that it is a statement whose meaning is a command, and the three '
              'holdings-back of sabr with the definitions of shukr qada and murr al-qada')
b += B.further()
b += B.nav('was-l51-sifat-ahl-al-sunnah.html',
           'The Qualities of Ahl al-Sunnah, and Why They Are So Named',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l52')

io.open(os.path.join(B.AQ, 'was-l52-mukammilat-al-aqidah.html'), 'w',
        encoding='utf-8', newline='\n').write(B.shell(
    'مُكَمِّلَاتُ العَقِيدَةِ مِنْ مَكَارِمِ الأَخْلَاق',
    'The Completers of the Creed, from Noble Character',
    'Lesson 52 of al-ʿAqīdah al-Wāsiṭiyyah: why noble character is the creed’s fruit '
    'rather than its appendix; the order the Sharīʿah obliges in forbidding the wrong, '
    'and the word maṣlaḥah inside it; the rites with the rulers whoever they are, with '
    'Ibn Taymiyyah on what rebellion costs; naṣīḥah from purity; the ḥadīth of the body '
    'as a statement whose meaning is a command; and ṣabr, shukr and riḍā.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الثَّانِي وَالخَمْسُون', '6',
           'مُكَمِّلَاتُ العَقِيدَةِ مِنْ مَكَارِمِ الأَخْلَاق',
           'The Completers of the Creed, from Noble Character', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l52-mukammilat-al-aqidah.html')
