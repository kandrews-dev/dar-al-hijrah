# -*- coding: utf-8 -*-
"""Wasitiyyah L53 -- Part 7, second closing fasl (second half): the call to
noble character, the completeness of iman by good character, the three
magnanimities, the rights of the eight classes, and what is forbidden --
al-fakhr, al-khuyala', al-baghy, al-istitalah. Sharh pp.198-200."""
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
    'Distinguish %s from %s, and say which one the ḥadīth is about.'
    % (ar('الخُلْق'), ar('الخَلْق')),
    'Give the two things al-Fawzān says the ḥadīth of the best character establishes '
    'about īmān itself.',
    'State the three magnanimities the matn commends, and what each one inverts.',
    'Name the eight classes whose rights the matn commands, and define %s, %s '
    'and %s.' % (ar('اليَتِيم'), ar('المِسْكِين'), ar('ابْنُ السَّبِيل')),
    'Explain al-Fawzān’s argument for why %s is forbidden whether it is with a '
    'right or without one.' % ar('الاسْتِطَالَة'),
    'Say what %s originally means, and why the image is apt.' % ar('السَّفْسَاف'),
])

b += B.heading('الدَّعْوَةُ إِلَى مَكَارِمِ الأَخْلَاقِ وَمَحَاسِنِ الأَعْمَال',
               'The Call to Noble Character and Beautiful Deeds')
b += B.matn(
    'وَيَدْعُونَ إِلَى مَكَارِمِ الأَخْلَاقِ وَمَحَاسِنِ الأَعْمَالِ، '
    'وَيَعْتَقِدُونَ مَعْنَى قَوْلِهِ ﷺ: «أَكْمَلُ المُؤْمِنِينَ إِيمَانًا '
    'أَحْسَنُهُمْ خُلُقًا»؛ وَيَنْدُبُونَ إِلَى أَنْ تَصِلَ مَنْ قَطَعَكَ، '
    'وَتُعْطِيَ مَنْ حَرَمَكَ، وَتَعْفُوَ عَمَّنْ ظَلَمَكَ؛ وَيَأْمُرُونَ بِبِرِّ '
    'الوَالِدَيْنِ، وَصِلَةِ الأَرْحَامِ، وَحُسْنِ الجِوَارِ، وَالإِحْسَانِ إِلَى '
    'اليَتَامَى وَالمَسَاكِينِ وَابْنِ السَّبِيلِ، وَالرِّفْقِ بِالمَمْلُوكِ؛ '
    'وَيَنْهَوْنَ عَنِ الفَخْرِ وَالخُيَلَاءِ وَالبَغْيِ وَالاسْتِطَالَةِ عَلَى '
    'الخَلْقِ بِحَقٍّ أَوْ بِغَيْرِ حَقٍّ. وَيَأْمُرُونَ بِمَعَالِي الأَخْلَاقِ، '
    'وَيَنْهَوْنَ عَنْ سَفْسَافِهَا. وَكُلُّ مَا يَقُولُونَهُ وَيَفْعَلُونَهُ مِنْ '
    'هَذَا وَغَيْرِهِ، فَإِنَّمَا هُمْ فِيهِ مُتَّبِعُونَ لِلْكِتَابِ '
    'وَالسُّنَّةِ.')
b += B.sharh(
    p('<em>Ahl al-Sunnah give attention to character, <strong>so they adorn themselves '
      'with excellent character and make others desire it</strong>. So they '
      '<strong>%s</strong> — that is: <strong>the best of them</strong>.</em>'
      % ar('يَدْعُونَ إِلَى مَكَارِمِ الأَخْلَاق')) +
    p('Then a distinction that rests on one vowel, and which the matn’s own wording '
      'depends on later in this same passage:') +
    table([
        row('<span dir="rtl" lang="ar">الخُلُق</span><br>'
            '<span style="font-size:.82rem;font-weight:400">ḍammah on the khāʾ and the '
            'lām</span>',
            '<em>plural <strong>أَخْلَاق</strong> — and it is '
            '<strong>الصُّورَةُ البَاطِنَة, the inward form</strong>; '
            '<strong>and it is the religion, the disposition and the nature</strong></em>'),
        row('<span dir="rtl" lang="ar">الخَلْق</span><br>'
            '<span style="font-size:.82rem;font-weight:400">fatḥah on the khāʾ, sukūn '
            'on the lām</span>',
            '<em>it is <strong>الصُّورَةُ الظَّاهِرَة, the outward form</strong></em>'),
    ], fs='.92rem') +
    p('<strong>So the same three letters name a man’s face or a man’s soul, and only '
      'the vowelling tells you which.</strong> Which is why the matn can say, a few '
      'lines later, «overbearing toward %s» using the <em>other</em> word — and why a '
      'student who reads unvowelled Arabic has to decide, at each occurrence, '
      'which of the two is meant.' % ar('الخَلْق')) +
    p('<em>And they call to <strong>%s</strong> — <strong>such as generosity, courage, '
      'truthfulness and trustworthiness</strong>.</em>'
      % ar('مَحَاسِنِ الأَعْمَال')))
b += B.hadith(
    'أَكْمَلُ المُؤْمِنِينَ إِيمَانًا أَحْسَنُهُمْ خُلُقًا',
    '"The most complete of the believers in īmān are the best of them in character."',
    'رَوَاهُ أَحْمَدُ وَالتِّرْمِذِيُّ — وَقَالَ التِّرْمِذِيُّ: حَسَنٌ صَحِيحٌ')
b += B.sharh(
    p('<em>And <strong>%s</strong> — that is: <strong>they believe in it and act by what '
      'it requires.</strong> And his words <strong>%s</strong> mean: '
      '<strong>the most gentle of them, the most courteous of them, and the most '
      'beautiful of them</strong>.</em>'
      % (ar('وَيَعْتَقِدُونَ مَعْنَى قَوْلِهِ ﷺ'), ar('أَحْسَنُهُمْ خُلُقًا'))) +
    p('<em>So in the ḥadīth is <strong>an urging toward being characterized by the best '
      'of character</strong>; and in it is <strong>that deeds enter into the name of '
      'īmān</strong>, and <strong>that īmān admits of degrees.</strong></em>'))
b += box(
    '<p style="margin:0;font-size:.95rem">That second sentence is why this ḥadīth is in '
    'a book of creed at all, and <strong>it quietly closes a question that Part 6 '
    'opened.</strong> Lesson 45 defined īmān as <em>قَوْلٌ بِاللِّسَانِ '
    'وَاعْتِقَادٌ بِالقَلْبِ وَعَمَلٌ بِالجَوَارِح</em>, and set Ahl al-Sunnah against '
    'those who exclude deeds from it or deny that it increases and decreases.</p>'
    '<p style="margin:.6rem 0 0;font-size:.93rem"><strong>This ḥadīth proves both points '
    'at once, and proves them from a ḥadīth about manners.</strong> «The most complete '
    'of the believers in īmān» presupposes that īmān has degrees of completeness; and '
    'the thing that raises a man in those degrees here is <em>character</em> — which is '
    'a deed of the limbs and the tongue. <strong>So the doctrinal claim of Part 6 and '
    'the ethical claim of Part 7 turn out to be one claim.</strong> This is why the two '
    'sections sit together at the close of the book.</p>')

b += B.heading('المَكَارِمُ الثَّلَاث', 'The Three Magnanimities')
b += B.sharh(
    p('<em>And they <strong>%s</strong> — that is, they call to:</em>'
      % ar('يَنْدُبُونَ')) +
    table([
        row(ar('أَنْ تَصِلَ مَنْ قَطَعَك'),
            '<em>that is: <strong>you do good to the one who did evil to you</strong></em>'),
        row(ar('وَتُعْطِيَ مَنْ حَرَمَك'),
            '<em>that is: <strong>you extend the gift</strong> — and it is the freely '
            'given and the present and the like — <strong>to the one who withheld that '
            'from you; because that is of excellence (الإِحْسَان)</strong></em>'),
        row(ar('وَتَعْفُوَ عَمَّنْ ظَلَمَك'),
            '<em>that is: <strong>you forgive the one who transgressed against you in '
            'property, or blood, or honour — because that is of what draws love and '
            'earns reward and recompense</strong></em>'),
    ]))
b += B.prose(
    'Set the three side by side and the pattern appears: <strong>each one takes the '
    'natural response and inverts it.</strong> Severing is answered with joining, '
    'withholding with giving, wronging with pardon. And al-Fawzān does not justify them '
    'by sentiment — he gives a reason for each: the second <em>is</em> iḥsān, and the '
    'third <strong>draws love and earns reward</strong>. The three magnanimities are '
    'profitable as well as noble, which is a thing the Sharīʿah is content to say out '
    'loud.')

b += B.heading('الحُقُوقُ المَأْمُورُ بِهَا', 'The Rights That Are Commanded')
b += B.sharh(
    p('<em>And <strong>they command</strong> — that is, Ahl al-Sunnah — '
      '<strong>what Allah commanded of giving those who have rights their '
      'rights</strong>:</em>') +
    table([
        row(ar('بِرُّ الوَالِدَيْن'),
            '<em>that is: <strong>obeying them in other than disobedience</strong>, and '
            '<strong>doing good to them by word and by deed</strong></em>'),
        row(ar('صِلَةُ الأَرْحَام'),
            '<em>doing good to the near kin; and <strong>الأَرْحَام is the plural of '
            'رَحِم, and it is whoever a kinship gathers you with</strong></em>'),
        row(ar('حُسْنُ الجِوَار'),
            '<em>doing good to whoever dwells beside you — <strong>by extending what is '
            'good and withholding harm</strong></em>'),
        row(ar('اليَتَامَى'),
            '<em>plural of <strong>يَتِيم</strong>; <strong>لُغَةً المُنْفَرِد, the '
            'solitary one</strong>; <strong>شَرْعًا one whose father died before he '
            'reached puberty</strong> — and doing good to them is '
            '<strong>by tending their circumstances and their property, and by '
            'compassion toward them</strong></em>'),
        row(ar('المَسَاكِين'),
            '<em>plural of <strong>مِسْكِين</strong>, and he is '
            '<strong>the needy one whom need and poverty have made still</strong>; and '
            'doing good to them is <strong>by giving them charity and being gentle with '
            'them</strong></em>'),
        row(ar('ابْنُ السَّبِيل'),
            '<em>and he is <strong>the traveller cut off, whose provision has run out, '
            'or been lost, or been stolen</strong>; <strong>and it is said: he is the '
            'guest</strong></em>'),
        row(ar('الرِّفْقُ بِالمَمْلُوك'),
            '<em>and he is <strong>the owned servant</strong>; '
            '<strong>and the owned among the animals enters into it</strong>. And '
            '<strong>الرِّفْق is the opposite of violence, and it is softness of '
            'side</strong></em>'),
    ], fs='.9rem'))
b += box(
    '<p style="margin:0;font-size:.95rem"><strong>مِسْكِين is from السُّكُون — '
    'stillness.</strong> al-Fawzān’s gloss is not a flourish: the word names a man '
    '<em>whom need has made motionless</em>. Poverty has taken away his capacity to '
    'move, to act, to change his circumstance — and that is what the Arabic is '
    'describing when it calls him a miskīn.</p>'
    '<p style="margin:.6rem 0 0;font-size:.93rem">Which tells you what doing good to him '
    'has to consist of. <strong>Charity and gentleness, in that order</strong> — the '
    'first because he cannot move himself, the second because a man held still by need '
    'is already humiliated and does not need a benefactor’s roughness on top of it.</p>')
b += B.ayah(
    'وَاعْبُدُوا اللَّهَ وَلَا تُشْرِكُوا بِهِ شَيْئًا وَبِالْوَالِدَيْنِ إِحْسَانًا '
    'وَبِذِي الْقُرْبَى وَالْيَتَامَى وَالْمَسَاكِينِ وَالْجَارِ ذِي الْقُرْبَى '
    'وَالْجَارِ الْجُنُبِ وَالصَّاحِبِ بِالْجَنْبِ وَابْنِ السَّبِيلِ وَمَا مَلَكَتْ '
    'أَيْمَانُكُمْ إِنَّ اللَّهَ لَا يُحِبُّ مَنْ كَانَ مُخْتَالًا فَخُورًا',
    '"And worship Allah and associate nothing with Him; and to parents, excellence; and '
    'to the near of kin, and the orphans, and the needy, and the near neighbour, and the '
    'distant neighbour, and the companion at your side, and the wayfarer, and those your '
    'right hands possess. Indeed Allah does not love one who is arrogant and boastful."',
    'Sūrat al-Nisāʾ 4:36 · سُورَةُ النِّسَاء')
b += B.prose(
    '<strong>Compare that āyah with the matn’s list and the matn turns out to be a '
    'paraphrase of it.</strong> Parents, kin, neighbours, orphans, the needy, the '
    'wayfarer, those the right hands possess — in the same order. '
    '<strong>And the āyah does two further things the matn then copies.</strong> It '
    'opens with <em>worship Allah and associate nothing with Him</em>, putting the '
    'whole list of manners downstream of tawḥīd; and it closes by forbidding exactly '
    'what the matn forbids next — <em>one who is arrogant and boastful</em>. '
    'So the structure of this closing section is the structure of a single āyah of '
    'al-Nisāʾ.')

b += B.heading('المَنْهِيُّ عَنْه', 'What Is Forbidden')
b += B.sharh(
    table([
        row(ar('الفَخْر'),
            '<em>and it is <strong>vaunting with merits and distinctions, of standing '
            'and of lineage</strong></em>'),
        row(ar('الخُيَلَاء'),
            '<em>with a ḍammah on the khāʾ: <strong>arrogance and '
            'self-admiration</strong></em>'),
        row(ar('البَغْي'),
            '<em>and it is <strong>aggression against people</strong></em>'),
        row(ar('الاسْتِطَالَةُ عَلَى الخَلْق'),
            '<em>that is: <strong>raising oneself above them, and holding them in '
            'contempt, and disparaging them</strong></em>'),
    ]))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem"><strong>Then the clause that looks '
    'strange until you see the argument: «%s» — whether with a right or without '
    'one.</strong> How can being overbearing «with a right» be forbidden?</p>'
    '<p style="margin:0;font-size:.95rem"><em>— <strong>because the one who is '
    'overbearing, if he is overbearing WITH a right, then he has boasted (فَقَدِ '
    'افْتَخَرَ); and if he is overbearing WITHOUT a right, then he has transgressed '
    '(فَقَدْ بَغَى) — and neither this nor that is permitted.</strong></em></p>'
    '<p style="margin:.6rem 0 0;font-size:.93rem">That is a small piece of reasoning '
    'worth keeping, because of its shape. <strong>The matn has just forbidden فَخْر and '
    'بَغْي by name; the overbearing man must fall under one or the other, and so the '
    'prohibition is already complete before the exception can be raised.</strong> '
    'Having a right on your side changes what you are owed; '
    '<em>it does not license contempt for the person who owes it.</em> '
    'Which is the hardest case in the section, and the reason it is given.</p>'
    % ar('بِحَقٍّ أَوْ بِغَيْرِ حَقّ'))
b += B.sharh(
    p('<em>And <strong>%s</strong> — that is: Ahl al-Sunnah command the lofty character, '
      'and it is the excellent character. <strong>%s</strong> — that is: '
      '<strong>its base and contemptible kind</strong>.</em>'
      % (ar('وَيَأْمُرُونَ بِمَعَالِي الأَخْلَاق'),
         ar('وَيَنْهَوْنَ عَنْ سَفْسَافِهَا'))) +
    p('<em>And <strong>السَّفْسَاف is the contemptible and base in anything</strong>; '
      'and it is <strong>the opposite of المَعَالِي and المَكَارِم</strong>. '
      '<strong>And its origin is: what flies up of the dust of flour when it is sifted, '
      'and of the earth when it is stirred up.</strong></em>'))
b += B.prose(
    '<strong>That etymology is the best image in the section, so do not read past it.</strong> '
    'Sifting flour or sweeping a floor throws up a fine dust — <em>the lightest part of '
    'the material, the part that rises because it is worth nothing and is thrown '
    'away.</em> So <strong>سَفْسَافُ الأَخْلَاق is the chaff of character</strong>: the '
    'petty, weightless conduct that a man gives off as a by-product and that settles on '
    'everything around him. And the opposite is <strong>مَعَالِي</strong> — the '
    '<em>high</em> things. The Arabic sets a lightness that merely floats against a '
    'height that is climbed.')

b += B.heading('الخِتَامُ · وَإِنَّمَا هُمْ فِيهِ مُتَّبِعُون',
               'The Close — They Are Only Following in It')
b += B.sharh(
    p('<em>That is: <strong>everything Ahl al-Sunnah say and do, and command and forbid, '
      'of what has preceded being mentioned in this treatise and of what has not been '
      'mentioned — they have derived it from the Book of their Lord and the Sunnah of '
      'their Prophet. They did not innovate it from themselves, and they did not imitate '
      'anyone else in it.</strong></em>'))
b += box(
    '<p style="margin:0;font-size:.96rem"><strong>That sentence is the author’s last '
    'word on the whole treatise, and it is a claim of a particular kind.</strong> '
    'Having spent the book establishing the attributes of Allah, the Last Day, the '
    'Decree, the Companions and now the manners of this group, he ends by saying that '
    '<em>none of it is his.</em> <strong>«They did not innovate it from themselves, and '
    'they did not imitate anyone else in it»</strong> — the two denials together rule out '
    'both originality and partisanship.</p>'
    '<p style="margin:.6rem 0 0;font-size:.93rem">So the Wāsiṭiyyah closes by withdrawing '
    'any authority of its own. <strong>It is not offered as Ibn Taymiyyah’s creed, and '
    'not as one school’s creed against another’s</strong> — which is also why, as Lesson '
    '51 noted, it carries only what is agreed and leaves the disputed to the books of '
    'uṣūl. <em>And the ḥadīths in this are many; of them is what the Shaykh '
    'mentioned.</em></p>')

b += B.vocab([
    ('الخُلُق', 'al-khuluq', 'character',
     'الصُّورَةُ البَاطِنَة, the inward form — the religion, disposition and nature; '
     'against الخَلْق, the outward form'),
    ('مَحَاسِنُ الأَعْمَال', 'maḥāsin al-aʿmāl', 'beautiful deeds',
     'Such as generosity, courage, truthfulness and trustworthiness'),
    ('يَنْدُبُون', 'yandubūn', 'they urge, they call to',
     'The verb of the three magnanimities — joining the one who severed, giving the one '
     'who withheld, pardoning the one who wronged'),
    ('اليَتِيم', 'al-yatīm', 'the orphan',
     'لُغَةً المُنْفَرِد, the solitary; شَرْعًا one whose father died before he reached '
     'puberty'),
    ('المِسْكِين', 'al-miskīn', 'the destitute one',
     'From السُّكُون — the needy one whom need and poverty have made STILL, robbed of '
     'the capacity to move'),
    ('ابْنُ السَّبِيل', 'ibn al-sabīl', 'the wayfarer',
     'The traveller cut off, whose provision has run out or been lost or stolen; and it '
     'is said: the guest'),
    ('الرِّفْق', 'al-rifq', 'gentleness',
     'The opposite of violence — لِينُ الجَانِب, softness of side; commanded even toward '
     'owned animals'),
    ('الفَخْر', 'al-fakhr', 'boasting',
     'Vaunting with merits and distinctions, of standing and of lineage'),
    ('الخُيَلَاء', 'al-khuyalāʾ', 'haughtiness',
     'With a ḍammah on the khāʾ — arrogance and self-admiration'),
    ('الاسْتِطَالَة', 'al-istiṭālah', 'overbearing',
     'Raising oneself above people, holding them in contempt and disparaging them — '
     'forbidden with a right (it is فَخْر) and without one (it is بَغْي)'),
    ('السَّفْسَاف', 'al-safsāf', 'the base and petty',
     'The contemptible in anything; originally the dust that flies up when flour is '
     'sifted or earth is stirred — the chaff of character'),
    ('مَعَالِي الأَخْلَاق', 'maʿālī al-akhlāq', 'the lofty character',
     'The high traits — the opposite of السَّفْسَاف; a height climbed against a '
     'lightness that merely floats'),
])
b += B.mcq('ws-l53', [
    ('What is the difference between الخُلُق and الخَلْق?',
     ['One is singular and the other plural',
      'الخُلُق (ḍammah) is الصُّورَةُ البَاطِنَة, the inward form — the disposition and '
      'nature; الخَلْق (fatḥah, sukūn) is الصُّورَةُ الظَّاهِرَة, the outward form',
      'One refers to Allah’s creating and the other to His decreeing',
      'They are two dialectal forms of one word'], 1),
    ('What two things does al-Fawzān say the ḥadīth establishes about īmān?',
     ['That it is in the heart alone, and that it cannot be lost',
      'That deeds enter into the name of īmān, and that īmān admits of degrees',
      'That it is identical with Islam, and that it is one indivisible thing',
      'That it is complete at the moment of testimony'], 1),
    ('Why does that matter for Part 6 of this creed?',
     ['Because it names the sects',
      'Because Lesson 45 defined īmān as statement, belief and deed against those who '
      'exclude deeds or deny that it increases — and this ḥadīth proves both points from '
      'a ḥadīth about manners',
      'Because it settles the ruling on the one who commits a major sin',
      'Because it establishes the ranks of the Companions'], 1),
    ('What pattern do the three magnanimities share?',
     ['Each concerns property',
      'Each inverts the natural response — severing answered with joining, withholding '
      'with giving, wronging with pardon',
      'Each is obligatory rather than recommended',
      'Each applies only to relatives'], 1),
    ('What reason does the matn give for pardoning the one who wronged you?',
     ['That vengeance is forbidden outright',
      'That it is of what draws love and earns reward and recompense',
      'That the wrongdoer may repent',
      'That the ruler alone may exact punishment'], 1),
    ('What does بِرُّ الوَالِدَيْن consist of?',
     ['Financial support alone',
      'Obeying them in other than disobedience, and doing good to them by word and by '
      'deed',
      'Obeying them in everything without exception',
      'Living with them until their death'], 1),
    ('What is a يَتِيم in the Sharīʿah, as against in the language?',
     ['In the language, one who lost both parents; in the Sharīʿah, one who lost his '
      'mother',
      'In the language, المُنْفَرِد, the solitary; in the Sharīʿah, one whose father '
      'died before he reached puberty',
      'In the language, a child; in the Sharīʿah, anyone in need',
      'The two meanings are identical'], 1),
    ('What does the word مِسْكِين describe about the man?',
     ['That he begs from people',
      'That need and poverty have made him STILL — robbed of the capacity to move or '
      'change his circumstance',
      'That he owns no dwelling',
      'That he is a traveller'], 1),
    ('Who is ابْنُ السَّبِيل?',
     ['Anyone born on a journey',
      'The traveller cut off, whose provision has run out or been lost or stolen — and '
      'it is said: the guest',
      'A beggar in the marketplace',
      'One who has no family'], 1),
    ('Who falls under الرِّفْقُ بِالمَمْلُوك?',
     ['Owned servants only',
      'The owned servant — and owned animals enter into it as well',
      'Employees and labourers',
      'Prisoners of war'], 1),
    ('What does al-Nisāʾ 4:36 do that the matn then copies?',
     ['It lists the five pillars',
      'It puts the whole list of manners downstream of «worship Allah and associate '
      'nothing with Him», and closes by forbidding the arrogant and boastful — exactly '
      'what the matn forbids next',
      'It abrogates an earlier command about neighbours',
      'It restricts the rights to the believers among them'], 1),
    ('How is الاسْتِطَالَة forbidden even «with a right»?',
     ['Because a right must be waived to be valid',
      'Because the overbearing man with a right has boasted (فَخْر), and without a right '
      'has transgressed (بَغْي) — and both were already forbidden by name',
      'Because rights belong to the ruler to enforce',
      'Because claiming a right publicly is prohibited'], 1),
    ('What does السَّفْسَاف originally mean?',
     ['A worn-out garment',
      'The dust that flies up when flour is sifted or earth is stirred — the lightest '
      'part, which rises because it is worthless',
      'A broken vessel',
      'Chatter and idle speech'], 1),
    ('What is the author’s last word on everything in the treatise?',
     ['That it is the creed of the Ḥanbalī school',
      'That they derived all of it from the Book and the Sunnah — they did not innovate '
      'it from themselves, and did not imitate anyone else in it',
      'That it is his own ijtihād and may be differed with',
      'That it is established by the consensus of the four imāms'], 1),
])
b += B.tf('ws-l53-tf', [
    ('الخُلُقُ بِضَمِّ الخَاءِ هُوَ الصُّورَةُ البَاطِنَةُ.',
     'الخُلُق with a ḍammah is the inward form.', True),
    ('الحَدِيثُ يَدُلُّ عَلَى أَنَّ الأَعْمَالَ تَدْخُلُ فِي مُسَمَّى الإِيمَانِ '
     'وَأَنَّ الإِيمَانَ يَتَفَاضَلُ.',
     'The ḥadīth indicates that deeds enter into the name of īmān and that īmān admits '
     'of degrees.', True),
    ('طَاعَةُ الوَالِدَيْنِ وَاجِبَةٌ فِي المَعْصِيَةِ أَيْضًا.',
     'Obeying parents is obligatory in disobedience as well.', False),
    ('الاسْتِطَالَةُ عَلَى الخَلْقِ بِحَقٍّ جَائِزَةٌ.',
     'Being overbearing toward people with a right is permitted.', False),
    ('الرِّفْقُ مَأْمُورٌ بِهِ حَتَّى فِي البَهَائِمِ المَمْلُوكَةِ.',
     'Gentleness is commanded even regarding owned animals.', True),
])
b += B.memorize(
    'أَكْمَلُ المُؤْمِنِينَ إِيمَانًا أَحْسَنُهُمْ خُلُقًا',
    'This is why a book about the attributes of Allah ends with manners. '
    '<strong>«The most complete in īmān» presupposes that īmān has degrees; and the '
    'thing that raises a man through them, in this ḥadīth, is his character.</strong> So '
    'the doctrinal claim of Part 6 — that deeds are part of īmān and that īmān increases '
    '— and the ethical claim of Part 7 are not two claims. '
    '<em>A creed is measured by what it produces in a man.</em>')
b += B.aiquiz('The closing manners of al-Aqidah al-Wasitiyyah: al-khuluq as the inward '
              'form against al-khalq as the outward, the hadith that the most complete in '
              'iman are the best in character and the two things it establishes (that '
              'deeds enter the name of iman and that iman admits of degrees), the three '
              'magnanimities of joining the one who severed and giving the one who '
              'withheld and pardoning the one who wronged, the rights of parents kin '
              'neighbours orphans the destitute the wayfarer and the owned, the '
              'definitions of yatim and miskin from al-sukun and ibn al-sabil, al-Nisa '
              '4:36 as the structure of the whole section, why al-istitalah is forbidden '
              'with a right (fakhr) and without one (baghy), the origin of al-safsaf as '
              'the dust that flies up from sifted flour, and the authors closing claim '
              'that they innovated none of it and imitated no one in it')
b += B.further()
b += B.nav('was-l52-mukammilat-al-aqidah.html',
           'The Completers of the Creed, from Noble Character',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l53')

io.open(os.path.join(B.AQ, 'was-l53-makarim-al-akhlaq.html'), 'w',
        encoding='utf-8', newline='\n').write(B.shell(
    'مَكَارِمُ الأَخْلَاقِ وَمَحَاسِنُ الأَعْمَال',
    'Noble Character and Beautiful Deeds',
    'Lesson 53 of al-ʿAqīdah al-Wāsiṭiyyah: al-khuluq against al-khalq; the ḥadīth that '
    'the most complete in īmān are the best in character, and the two things it '
    'establishes about īmān itself; the three magnanimities; the rights of the eight '
    'classes, with yatīm, miskīn and ibn al-sabīl defined; why being overbearing is '
    'forbidden with a right and without one; and the origin of al-safsāf.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الثَّالِثُ وَالخَمْسُون', '6',
           'مَكَارِمُ الأَخْلَاقِ وَمَحَاسِنُ الأَعْمَال',
           'Noble Character and Beautiful Deeds', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l53-makarim-al-akhlaq.html')
