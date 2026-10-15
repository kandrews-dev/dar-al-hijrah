# -*- coding: utf-8 -*-
"""Wasitiyyah L50 -- Part 7 opens: the madhhab of Ahl al-Sunnah on the karamat
of the awliya'. Sharh pp.187-189."""
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
    'Shaykh al-Islām <strong>ابْنُ تَيْمِيَّةَ</strong>, '
    '<em>الفُرْقَانُ بَيْنَ أَوْلِيَاءِ الرَّحْمَنِ وَأَوْلِيَاءِ الشَّيْطَان</em> — '
    'al-Fawzān names this book here as the full treatment of the subject.',
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
    'Define %s and %s, and say what root the second is derived from.'
    % (ar('الكَرَامَة'), ar('الوَلِيّ')),
    'Give the three groups of people regarding the karāmāt, and the argument of '
    'the first group.',
    'Answer the deniers’ objection in the two ways al-Fawzān answers it.',
    'Distinguish a karāmah from a %s, and give the test that separates '
    'the walī of Allah from the walī of Shayṭān.' % ar('خَارِقٌ شَيْطَانِيّ'),
    'Name the two classes the matn’s own wording divides the karāmāt into, with an '
    'example of each.',
    'State the condition on which the karāmāt continue in this Ummah until the Hour.',
])

# ------------------------------------------------------------------ the matn
b += B.heading('مَذْهَبُ أَهْلِ السُّنَّةِ وَالجَمَاعَةِ فِي كَرَامَاتِ الأَوْلِيَاء',
               'The Position of Ahl al-Sunnah on the Karāmāt of the Awliyāʾ')
b += B.matn(
    'وَمِنْ أُصُولِ أَهْلِ السُّنَّةِ التَّصْدِيقُ بِكَرَامَاتِ الأَوْلِيَاءِ، وَمَا '
    'يَجْرِي اللهُ عَلَى أَيْدِيهِمْ مِنْ خَوَارِقِ العَادَاتِ فِي أَنْوَاعِ '
    'العُلُومِ وَالمُكَاشَفَاتِ، وَأَنْوَاعِ القُدْرَةِ وَالتَّأْثِيرَاتِ؛ '
    'وَالمَأْثُورُ عَنْ سَالِفِ الأُمَمِ فِي سُورَةِ الكَهْفِ وَغَيْرِهَا، وَعَنْ '
    'صَدْرِ هَذِهِ الأُمَّةِ مِنَ الصَّحَابَةِ وَالتَّابِعِينَ وَسَائِرِ فِرَقِ '
    'الأُمَّةِ — وَهِيَ مَوْجُودَةٌ فِيهَا إِلَى يَوْمِ القِيَامَةِ.')
b += B.prose(
    'Part Seven opens, and with it the book turns from what Ahl al-Sunnah '
    '<em>believe</em> to how they <em>are</em>. This first section is the bridge: it is '
    'still a matter of creed — <strong>«and of the foundations of Ahl al-Sunnah»</strong> '
    '— but it is a creed about the people of faith rather than about Allah and the Last '
    'Day. And it is placed here for a reason. <strong>Having just finished defending the '
    'best generation of this Ummah, the author now states what Allah grants to the '
    'righteous of it in every generation after them.</strong>')

# ------------------------------------------------------------------ definitions
b += B.heading('حَدُّ الكَرَامَةِ وَحَدُّ الوَلِيّ',
               'Defining a Karāmah, and Defining a Walī')
b += B.sharh(
    p('<em>His words <strong>%s</strong> — that is: <strong>of the foundations of their '
      'creed</strong></em>. So this is not an optional refinement; '
      '<strong>affirming it is part of the madhhab.</strong>'
      % ar('وَمِنْ أُصُولِ أَهْلِ السُّنَّة')) +
    table([
        row(ar('الكَرَامَة'),
            '<em>plural <strong>%s</strong>; and it is <strong>what Allah brings about '
            'at their hands of the breaking of customary order</strong> — so a karāmah '
            'is <strong>a matter that breaks the custom, that is: what is habitual for '
            'human beings.</strong></em>' % ar('كَرَامَات')),
        row(ar('الوَلِيّ'),
            '<em>plural <strong>%s</strong>; and he is <strong>the believer who has '
            'taqwā</strong></em> — as Allah said in the two āyāt below.' % ar('أَوْلِيَاء')),
    ]))
b += B.ayah(
    'أَلَا إِنَّ أَوْلِيَاءَ اللَّهِ لَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ '
    'الَّذِينَ آمَنُوا وَكَانُوا يَتَّقُونَ',
    '"Unquestionably, the awliyāʾ of Allah — no fear is upon them, nor will they grieve: '
    'those who believed and used to have taqwā."',
    'Sūrat Yūnus 10:62–63 · سُورَةُ يُونُس')
b += B.sharh(
    p('<strong>Note how the Qurʾān defines the word itself.</strong> It says «the awliyāʾ '
      'of Allah», and then the very next āyah tells you who they are: '
      '<em>those who believed and used to have taqwā</em>. <strong>That is a definition '
      'given by Allah, not one assembled by the scholars</strong> — which is why no '
      'claim of wilāyah can stand against it.') +
    p('And then the etymology, which carries the whole meaning: '
      '<em>he is called a <strong>%s</strong> by derivation <strong>from %s, and it is '
      'love and nearness</strong>. So <strong>the walī of Allah is: the one who allies '
      'himself with Allah by agreeing with Him in what He loves, and by drawing near to '
      'Him through what pleases Him.</strong></em>'
      % (ar('وَلِيّ'), ar('الوَلَاء'))))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem"><strong>Read that definition '
    'closely, because it decides every question in the section:</strong></p>'
    '<p style="margin:0;font-size:.95rem;text-align:center">'
    '<strong>الوَلَاء</strong> &nbsp;=&nbsp; المَحَبَّةُ وَالقُرْب '
    '&nbsp;&nbsp;→&nbsp;&nbsp; '
    '<strong>وَلِيُّ اللهِ</strong> &nbsp;=&nbsp; مَنْ وَالَى اللهَ '
    'بِمُوَافَقَتِهِ فِي مَحْبُوبَاتِهِ وَالتَّقَرُّبِ إِلَيْهِ بِمَرْضَاتِهِ</p>'
    '<p style="margin:.6rem 0 0;font-size:.92rem"><strong>Wilāyah is therefore earned '
    'by obedience and by nothing else.</strong> It is not a station conferred by a '
    'lineage, a robe, a chain of initiation or a tomb. A man is a walī of Allah exactly '
    'to the extent that he agrees with what Allah loves — so <em>the most obedient are '
    'the greatest awliyāʾ</em>, and a man who opposes the Sharīʿah is not one at all, '
    'whatever is reported at his hands.</p>')
b += B.prose(
    'That last sentence is the key the whole section turns on. <strong>Once wilāyah is '
    'defined by taqwā, a wonder worked by a man who abandons the prayer proves nothing '
    'in his favour</strong> — because the definition was never about wonders. Hold on to '
    'it, and the third group below becomes obvious rather than complicated.')
b += B.sharh(
    p('<em>And <strong>the karāmāt of the awliyāʾ are true</strong>; '
      '<strong>the Book, the Sunnah, and the mutawātir reports from the Companions and '
      'the Tābiʿūn have all indicated them.</strong></em>'))

# ------------------------------------------------------------------ three groups
b += B.heading('النَّاسُ فِيهَا ثَلَاثَةُ أَصْنَاف', 'People Fall Into Three Groups')
b += B.sharh(
    p('al-Fawzān sets the question out as he usually does — the two extremes, then the '
      'position of the Sunnah between them. <strong>And as in Lesson 49, the middle '
      'position is not a compromise between the two: it is the only one that answers '
      'both.</strong>') +
    table([
        row('<strong>١</strong><br><span style="font-size:.8rem;font-weight:400">'
            'النَّافُون</span>',
            '<em><strong>Those who deny them, from the people of innovation — like the '
            '<strong>المُعْتَزِلَة</strong> and the <strong>الجَهْمِيَّة</strong> and '
            '<strong>some of the Ashāʿirah</strong>.</strong></em>'),
        row('<strong>٢</strong><br><span style="font-size:.8rem;font-weight:400">'
            'الغَالُون</span>',
            '<em><strong>Those who go to excess in affirming them</strong>, from the '
            'people of the Ṣūfī orders and <strong>the grave-venerators who practise '
            'deception upon the people</strong> and bring <strong>satanic '
            'wonders</strong>.</em>'),
        row('<strong>٣</strong><br><span style="font-size:.8rem;font-weight:400">'
            'أَهْلُ السُّنَّة</span>',
            '<em><strong>Those the Shaykh mentioned here</strong> — they believe in the '
            'karāmāt of the awliyāʾ and <strong>affirm them according to the measure of '
            'what came in the Book and the Sunnah</strong>.</em>'),
    ], fs='.92rem'))

b += B.heading('شُبْهَةُ النَّافِينَ وَالجَوَابُ عَنْهَا',
               'The Deniers’ Objection, and the Answer to It')
b += B.sharh(
    p('Their objection is worth stating at its strongest, because it is not stupid: '
      '<em><strong>that if it were permissible for the breaking of custom to appear at '
      'the hands of the awliyāʾ, then the prophet would be confused with other than '
      'him</strong> — since the difference between a prophet and another man is '
      '<strong>the muʿjizah, which is a breaking of custom.</strong></em>') +
    p('<strong>In other words: if miracles are the credential of prophethood, and '
      'non-prophets can work them, the credential is worthless.</strong> That is a real '
      'argument, and al-Fawzān answers it in two moves rather than one.') +
    table([
        row('<strong>١</strong>',
            '<em><strong>There are immense distinctions between the Prophets and others '
            'besides the breaking of customs</strong></em> — the revelation, the '
            'message, the law brought, the ʿiṣmah in conveying it. <strong>So the '
            'credential of prophethood was never the wonder alone</strong>, and nothing '
            'is confused by a wonder occurring elsewhere.'),
        row('<strong>٢</strong>',
            '<em><strong>And the walī does not claim prophethood; and were he to claim '
            'it, he would leave wilāyah altogether and become a lying claimant and no '
            'walī.</strong></em> The confusion the objection fears <strong>requires a '
            'claim that a walī by definition does not make.</strong>'),
    ], fs='.92rem'))
b += box(
    '<p style="margin:0;font-size:.95rem"><em>And <strong>it is of the Sunnah of Allah '
    'that He disgraces the liar</strong> — as happened to '
    '<strong>مُسَيْلِمَةَ الكَذَّاب</strong> and others.</em></p>'
    '<p style="margin:.55rem 0 0;font-size:.92rem">That is the third guard, and it is '
    'the one that answers the objection from history rather than from argument. '
    '<strong>False claimants to prophethood are not left standing.</strong> The man who '
    'called himself a prophet in the Prophet’s ﷺ own lifetime is remembered by the title '
    '<em>al-Kadhdhāb</em> — the Liar — which is the disgrace itself, still attached to '
    'his name fourteen centuries later.</p>')

b += B.heading('غُلُوُّ الغَالِينَ وَالجَوَابُ عَنْهُ',
               'The Excess of the Exaggerators, and the Answer to It')
b += B.sharh(
    p('al-Fawzān is concrete about what he means, and the list is not historical: '
      '<em>they bring <strong>satanic wonders — such as entering fire, and striking '
      'themselves with weapons, and handling serpents</strong>, and other than that; '
      'and <strong>what they claim for the occupants of the graves of dispositions over '
      'the creation, which they name karāmāt.</strong></em>') +
    p('Then the answer, in three clauses:') +
    table([
        row('<strong>١</strong>',
            '<em><strong>These are not the awliyāʾ of Allah; rather they are the '
            'awliyāʾ of Shayṭān.</strong></em>'),
        row('<strong>٢</strong>',
            '<em>And what occurs at their hands is <strong>either a lie and a '
            'deception</strong></em> — a trick, not a wonder at all.'),
        row('<strong>٣</strong>',
            '<em><strong>or a trial for them and for others, and an istidrāj</strong></em> '
            '— a real event, granted in order to draw a man on by degrees until he is '
            'taken.'),
    ], fs='.92rem') +
    p('<strong>The third clause is the one that disarms the whole claim.</strong> Even '
      'granting that something genuinely happened, <em>its happening is not a '
      'certificate.</em> An extraordinary event can be a favour and it can equally be a '
      'rope — and the Qurʾān uses the word <strong>%s</strong> precisely for a good '
      'given in order to ruin. <strong>So the event never settles the question; the '
      'man’s adherence to the Sharīʿah does.</strong>' % ar('الاسْتِدْرَاج')))
b += box(
    '<p style="margin:0 0 .45rem;font-size:.95rem"><strong>The test, stated as a '
    'question to put to any reported wonder:</strong></p>'
    '<p style="margin:0;font-size:.94rem">Not <em>«did it happen?»</em> — but '
    '<strong><em>«is this man, by the Qurʾān’s own definition, a believer who has '
      'taqwā?»</em></strong> If he is, the wonder may be a karāmah from Allah. If he '
    'calls upon the dead, circles a tomb, or sets his way against the Sunnah, then '
    'whatever occurred is a deception or a snare — <strong>and the more impressive it '
    'is, the more dangerous.</strong></p>'
    '<p style="margin:.55rem 0 0;font-size:.9rem;color:var(--ink-mid)">al-Fawzān closes '
    'the question by naming where it is treated in full: '
    '<em>and Shaykh al-Islām Ibn Taymiyyah has on this subject a magnificent book, '
    'named <strong>الفُرْقَانُ بَيْنَ أَوْلِيَاءِ الرَّحْمَنِ وَأَوْلِيَاءِ '
    'الشَّيْطَان</strong></em> — <em>The Distinction Between the Allies of the Most '
    'Merciful and the Allies of Shayṭān.</em> The title is the answer: the two are not '
    'told apart by their wonders, but by whose allies they are.</p>',
    wash='#fff8e6', edge='#d4a017')

# ------------------------------------------------------------------ two kinds
b += B.heading('نَوْعَا الكَرَامَة', 'The Two Classes of Karāmah')
b += B.sharh(
    p('Now al-Fawzān reads the matn’s own wording as a division. <em>And in his words '
      '<strong>%s</strong> there is <strong>an indication that of the karāmah there is '
      'what is of the category of knowledge and unveiling… and of it there is what is of '
      'the category of power and effect.</strong></em>'
      % ar('فِي أَنْوَاعِ العُلُومِ وَالمُكَاشَفَاتِ وَأَنْوَاعِ القُدْرَةِ '
           'وَالتَّأْثِيرَات')) +
    p('<strong>The author did not merely list two phrases; he classified.</strong> And '
      'the examples the sharḥ supplies for each are drawn from the Qurʾān first, then '
      'from the Companions.'))
b += B.sharh(
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .75rem">'
    '<tr><td style="padding:.7rem .8rem;border:1px solid var(--line);'
    'vertical-align:top;width:34%">'
    '<strong dir="rtl" lang="ar">العِلْمُ وَالكَشْف</strong><br>'
    '<span style="font-size:.84rem">the first class — <em>that the servant '
    '<strong>hears what others do not hear, or sees what others do not see, awake or in '
    'sleep, or knows what others do not know</strong></em></span></td>'
    '<td style="padding:.7rem .8rem;border:1px solid var(--line)">'
    '<em>— <strong>the saying of ʿUmar: «يَا سَارِيَةُ الجَبَل»</strong> while he was '
    'in Madīnah and Sāriyah was in the East<br>'
    '— <strong>Abū Bakr’s informing</strong> that what was in his wife’s womb was a '
    'female<br>'
    '— <strong>ʿUmar’s informing</strong> of which of his offspring would come forth and '
    'be just<br>'
    '— <strong>the story of the companion of Mūsā</strong> and his knowledge of the '
    'state of the boy</em></td></tr>'
    '<tr><td style="padding:.7rem .8rem;border:1px solid var(--line);vertical-align:top">'
    '<strong dir="rtl" lang="ar">القُدْرَةُ وَالتَّأْثِير</strong><br>'
    '<span style="font-size:.84rem">the second class — a wonder in '
    '<em>acting</em> rather than in knowing</span></td>'
    '<td style="padding:.7rem .8rem;border:1px solid var(--line)">'
    '<em>— <strong>the one who had knowledge from the Book</strong>, and his bringing '
    'the throne of Bilqīs to Sulaymān عليه السلام<br>'
    '— <strong>the story of the People of the Cave</strong><br>'
    '— <strong>the story of Maryam</strong><br>'
    '— <strong>the story of Khālid ibn al-Walīd</strong> when he drank poison '
    '<strong>and no harm came to him from it</strong></em></td></tr>'
    '</table></div>')
b += B.ayah(
    'قَالَ الَّذِي عِنْدَهُ عِلْمٌ مِنَ الْكِتَابِ أَنَا آتِيكَ بِهِ قَبْلَ أَنْ '
    'يَرْتَدَّ إِلَيْكَ طَرْفُكَ',
    '"Said the one who had knowledge from the Book: I will bring it to you before your '
    'glance returns to you."',
    'Sūrat al-Naml 27:40 · سُورَةُ النَّمْل')
b += B.prose(
    'And mark how that one reports it when the throne is before him: '
    '<em>«هَذَا مِنْ فَضْلِ رَبِّي لِيَبْلُوَنِي أَأَشْكُرُ أَمْ أَكْفُرُ»</em> — '
    '<strong>this is from the favour of my Lord, to test me: will I be grateful or '
    'ungrateful.</strong> The man at whose hand the wonder occurred '
    '<strong>did not read it as a rank; he read it as a trial</strong> — which is '
    'exactly the opposite of what the exaggerators do with it.')
b += B.sharh(
    p('<em>And his words <strong>%s</strong> point to the karāmāt that occurred and were '
      'mentioned in the Noble Qurʾān and in other sound transmissions. '
      'So of what Allah mentioned in the Qurʾān about the bygone nations: '
      '<strong>Maryam’s conceiving without a husband</strong>, and what is mentioned in '
      'Sūrat al-Kahf of <strong>the story of the People of the Cave</strong>, and '
      '<strong>the story of the companion of Mūsā</strong>, and <strong>the story of Dhū '
      'al-Qarnayn</strong>.</em>'
      % ar('وَالمَأْثُورُ عَنْ سَالِفِ الأُمَمِ فِي سُورَةِ الكَهْفِ وَغَيْرِهَا')) +
    p('<em>And <strong>%s</strong> — that is: <strong>what is transmitted by a sound '
      'chain</strong> — about <strong>%s</strong>, that is: its first part, '
      '<strong>of the Companions and the Tābiʿūn</strong>.</em>'
      % (ar('المَأْثُور'), ar('صَدْرِ هَذِهِ الأُمَّة'))))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem"><strong dir="rtl" lang="ar">'
    'قِصَّةُ سَارِيَةَ</strong> — al-Fawzān tells it twice, so it is worth having '
    'in full.</p>'
    '<p style="margin:0;font-size:.94rem"><em><strong>ʿUmar’s seeing the army of '
    'Sāriyah while he was upon the pulpit of Madīnah</strong> — and the army of Sāriyah '
    'was at <strong>نَهَاوَنْد</strong>, in the East — <strong>and his calling out to '
    'him: «يَا سَارِيَةُ الجَبَل!» · So Sāriyah heard him, and benefited by this '
    'direction, and was saved from the stratagem of the enemy.</strong></em></p>'
    '<p style="margin:.6rem 0 0;font-size:.92rem">Two things in it are instructive. '
    '<strong>It is a karāmah of both classes at once</strong> — a seeing (knowledge) and '
    'a being heard across a continent (effect). And <strong>it was for a purpose '
    'outside itself</strong>: it saved a Muslim army. It was not a display, it was not '
    'sought, and ʿUmar رضي الله عنه built no claim upon it afterwards — which is how the '
    'karāmāt of the awliyāʾ characteristically come.</p>')

# ------------------------------------------------------------------ until the Hour
b += B.heading('وَهِيَ مَوْجُودَةٌ إِلَى يَوْمِ القِيَامَة',
               'And They Continue Until the Day of Standing')
b += B.sharh(
    p('<em>His words <strong>%s</strong> — that is: <strong>the karāmāt do not cease to '
      'be present in this Ummah until the Day of Standing — so long as wilāyah is found '
      'in them, with its conditions.</strong> And Allah knows best.</em>'
      % ar('وَهِيَ مَوْجُودَةٌ فِيهَا إِلَى يَوْمِ القِيَامَة')) +
    p('<strong>Do not read past the final clause.</strong> The matn’s promise is open — '
      'they continue to the end of time — but al-Fawzān attaches the condition the '
      'definition already contained: <em>%s</em>. '
      '<strong>The karāmāt continue wherever the taqwā continues</strong>, and not '
      'elsewhere. Which means the section ends exactly where it began, with the two āyāt '
      'of Yūnus — and the claim of a wonder has still never been allowed to stand in '
      'the place of faith and taqwā.'
      % ar('مَا وُجِدَتْ فِيهِمُ الوَلَايَةُ بِشُرُوطِهَا')))

b += B.vocab([
    ('الكَرَامَة', 'al-karāmah', 'a karāmah, an honouring',
     'What Allah brings about at the hands of His awliyāʾ of the breaking of customary '
     'order — that is, of what is habitual for human beings'),
    ('الوَلِيّ', 'al-walī', 'an ally of Allah',
     'المُؤْمِنُ المُتَّقِي — the believer who has taqwā; Yūnus 10:62–63 defines the '
     'word itself'),
    ('الوَلَاء', 'al-walāʾ', 'allegiance',
     'المَحَبَّةُ وَالقُرْب — love and nearness; the root the word وَلِيّ is derived '
     'from'),
    ('خَوَارِقُ العَادَات', 'khawāriq al-ʿādāt', 'breakings of custom',
     'What departs from مَأْلُوفُ الآدَمِيِّين, the habitual course of human affairs'),
    ('المُعْجِزَة', 'al-muʿjizah', 'a prophetic miracle',
     'The breaking of custom at the hand of a prophet — never the sole credential of '
     'prophethood, which is the answer to the deniers'),
    ('المُكَاشَفَة', 'al-mukāshafah', 'an unveiling',
     'The first class: he hears, sees or knows what others do not — awake or in sleep'),
    ('الاسْتِدْرَاج', 'al-istidrāj', 'being drawn on by degrees',
     'A real event granted in order to draw a man on until he is seized — which is why '
     'a wonder is never a certificate'),
    ('التَّدْجِيل', 'al-tadjīl', 'deception, charlatanry',
     'What the grave-venerators practise upon the people; the wonder that is not a '
     'wonder but a trick'),
    ('صَدْرُ هَذِهِ الأُمَّة', 'ṣadr hādhihi al-ummah', 'the first part of this Ummah',
     'The Companions and the Tābiʿūn — and المَأْثُور is what is transmitted from them '
     'by a sound chain'),
])
b += B.mcq('ws-l50', [
    ('What is a karāmah, per al-Fawzān’s definition?',
     ['Any unusual event, from whatever source',
      'What Allah brings about at the hands of His awliyāʾ of the breaking of customary '
      'order — what is habitual for human beings',
      'A miracle identical in kind to a prophet’s, granted to a saint',
      'An answered supplication'], 1),
    ('Who is a walī, and where is the definition from?',
     ['One given a chain of initiation by a shaykh',
      'المُؤْمِنُ المُتَّقِي, the believer who has taqwā — and Yūnus 10:62–63 defines the '
      'word in the āyah immediately following it',
      'A descendant of the Prophet ﷺ',
      'One at whose hand wonders have been witnessed'], 1),
    ('What root is وَلِيّ derived from, and what does it mean?',
     ['From الوَلَد, offspring — nearness of lineage',
      'From الوَلَاء — love and nearness; so the walī of Allah is one who agrees with '
      'Him in what He loves and draws near by what pleases Him',
      'From الوِلَايَة, governance — authority over people',
      'From الأَوَّل — precedence in faith'], 1),
    ('What is the deniers’ objection?',
     ['That the reports are not authentic',
      'That if wonders could appear at the hands of non-prophets, the prophet would be '
      'confused with others — since the muʿjizah is what distinguishes him',
      'That the Qurʾān mentions no karāmāt',
      'That affirming them leads to grave-veneration'], 1),
    ('What are al-Fawzān’s two answers to that objection?',
     ['That the reports are mutawātir, and that the Ummah has agreed on them',
      'That there are immense distinctions between prophets and others besides wonders; '
      'and that a walī makes no claim to prophethood — were he to claim it he would '
      'leave wilāyah and be a lying claimant',
      'That muʿjizāt are greater in degree than karāmāt',
      'That karāmāt occur only in sleep'], 1),
    ('What third consideration answers the deniers from history?',
     ['That no one has claimed prophethood since',
      'That it is of the Sunnah of Allah that He disgraces the liar — as happened to '
      'Musaylimah, remembered by the title al-Kadhdhāb',
      'That the Caliphs executed every false claimant',
      'That wonders ceased after the Companions'], 1),
    ('What does al-Fawzān say of the wonders of the grave-venerators?',
     ['That they are lesser karāmāt',
      'That they are satanic wonders — either a lie and a deception, or a trial and an '
      'istidrāj; and these are awliyāʾ of Shayṭān, not of Allah',
      'That they are permissible if the man prays',
      'That they must be judged case by case with no ruling'], 1),
    ('Why does istidrāj mean that a wonder can never settle the question?',
     ['Because no event can be verified',
      'Because a real event may be granted precisely in order to draw a man on by '
      'degrees until he is seized — so the man’s adherence to the Sharīʿah decides, not '
      'the event',
      'Because only prophets receive genuine wonders',
      'Because the Sharīʿah forbids investigating such reports'], 1),
    ('What two classes does the matn’s own wording divide the karāmāt into?',
     ['The witnessed and the reported',
      'العِلْمُ وَالمُكَاشَفَة — knowledge and unveiling; and القُدْرَةُ وَالتَّأْثِير '
      '— power and effect',
      'Those in this world and those in the next',
      'Those of the Companions and those of later generations'], 1),
    ('How did the one who brought the throne of Bilqīs read what happened at his hand?',
     ['As proof of his rank over Sulaymān’s court',
      'As a favour from his Lord that was a TEST — «will I be grateful or ungrateful» — '
      'which is the opposite of what the exaggerators do with wonders',
      'As a sign that prophethood had passed to him',
      'As something he had earned by his knowledge'], 1),
    ('Why is the story of Sāriyah instructive twice over?',
     ['Because it is narrated by al-Bukhārī and Muslim',
      'Because it joins both classes at once — a seeing and a being heard across a '
      'continent — and it served a purpose outside itself, saving a Muslim army, with no '
      'claim built upon it afterwards',
      'Because ʿUmar رضي الله عنه claimed prophetic knowledge by it',
      'Because it occurred in a dream'], 1),
    ('What condition does al-Fawzān attach to the karāmāt continuing until the Hour?',
     ['That a living chain of shaykhs is preserved',
      'So long as wilāyah is found in them WITH ITS CONDITIONS — so they continue '
      'wherever the taqwā continues, and not elsewhere',
      'That the Ummah remains united',
      'That they occur only in the two Ḥarams'], 1),
])
b += B.tf('ws-l50-tf', [
    ('التَّصْدِيقُ بِكَرَامَاتِ الأَوْلِيَاءِ مِنْ أُصُولِ أَهْلِ السُّنَّةِ.',
     'Affirming the karāmāt of the awliyāʾ is of the foundations of Ahl al-Sunnah.',
     True),
    ('الوَلِيُّ مَنْ ظَهَرَتْ عَلَى يَدِهِ الخَوَارِقُ وَلَوْ خَالَفَ الشَّرِيعَةَ.',
     'A walī is one at whose hand wonders appear, even if he opposes the Sharīʿah.',
     False),
    ('لَوِ ادَّعَى الوَلِيُّ النُّبُوَّةَ خَرَجَ عَنِ الوَلَايَةِ وَصَارَ مُدَّعِيًا '
     'كَذَّابًا.',
     'Were a walī to claim prophethood he would leave wilāyah and become a lying '
     'claimant.', True),
    ('كُلُّ خَارِقٍ يَجْرِي عَلَى يَدِ رَجُلٍ فَهُوَ كَرَامَةٌ لَهُ.',
     'Every wonder occurring at a man’s hand is a karāmah in his favour.', False),
    ('الكَرَامَاتُ بَاقِيَةٌ فِي الأُمَّةِ إِلَى يَوْمِ القِيَامَةِ مَا وُجِدَتْ '
     'فِيهِمُ الوَلَايَةُ بِشُرُوطِهَا.',
     'The karāmāt remain in the Ummah until the Day of Standing so long as wilāyah with '
     'its conditions is found in them.', True),
])
b += B.memorize(
    'الَّذِينَ آمَنُوا وَكَانُوا يَتَّقُونَ',
    'Four words, and they settle the whole section. <strong>Allah named the awliyāʾ and '
    'then defined them Himself, in the very next āyah — by faith and taqwā, and by '
    'nothing else.</strong> So no robe, no lineage, no tomb and no wonder can make a man '
    'one, and none of them can keep him one. Memorize the definition and you will never '
    'need to adjudicate a reported marvel again: you will ask about the man, not about '
    'the marvel.')
b += B.aiquiz('The karamat of the awliya in al-Aqidah al-Wasitiyyah: the definition of '
              'karamah as the breaking of what is habitual for human beings, the walli as '
              'al-mumin al-muttaqi with Yunus 10:62-63 defining the word, the derivation '
              'from al-wala meaning love and nearness, the three groups of people, the '
              'deniers objection that the prophet would be confused with others and the '
              'two answers plus the disgracing of the liar as happened to Musaylimah, the '
              'satanic wonders of the grave-venerators and the three-clause answer '
              'including istidraj, the two classes of knowledge-and-unveiling against '
              'power-and-effect with their examples, the story of Sariyah and Nahawand, '
              'how the one who brought the throne of Bilqis read it as a test, and the '
              'condition that they continue only so long as wilayah with its conditions '
              'is found')
b += B.further()
b += B.nav('was-l49-ma-shajara-bayna-al-sahabah.html',
           'Refraining from What Occurred Between the Companions',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l50')

io.open(os.path.join(B.AQ, 'was-l50-karamat-al-awliya.html'), 'w',
        encoding='utf-8', newline='\n').write(B.shell(
    'كَرَامَاتُ الأَوْلِيَاء',
    'The Karāmāt of the Awliyāʾ',
    'Lesson 50 of al-ʿAqīdah al-Wāsiṭiyyah, opening Part 7: what a karāmah is and who a '
    'walī is — with the Qurʾān defining the word itself; the three groups of people '
    'regarding the karāmāt; the deniers’ objection that the prophet would be confused '
    'with others, and the two answers to it; why istidrāj means a wonder is never a '
    'certificate; the two classes of karāmah; and the condition on which they continue '
    'until the Hour.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الخَمْسُون', '6',
           'كَرَامَاتُ الأَوْلِيَاء',
           'The Karāmāt of the Awliyāʾ', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l50-karamat-al-awliya.html')
