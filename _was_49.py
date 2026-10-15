# -*- coding: utf-8 -*-
"""Wasitiyyah L49 -- closes Part 6: tabarru' from the Rafidah and the Nawasib,
imsak about what occurred between the Companions, and the four excuses + the
expiators. Sharh pp.181-186."""
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
    'Name the two opposed sects this clause disowns, and say what each one does.',
    'State the two things Ahl al-Sunnah do about %s — what they refrain from, '
    'and what they say.' % ar('مَا شَجَرَ بَيْنَ الصَّحَابَة'),
    'Give the four excuses for the narrations of the Companions’ faults, in order.',
    'List the expiators al-Fawzān gives, and say why a Companion’s sin is covered by '
    'more of them than a later man’s.',
    'Explain why %s is answered with reward either way — and what that does to the '
    'whole question.' % ar('الاجْتِهَاد'),
])

# ---------------------------------------------------------------- tabarru'
b += B.heading('التَّبَرُّؤُ مِنَ الرَّوَافِضِ وَالنَّوَاصِب',
               'Disowning Both the Rāfiḍah and the Nawāṣib')
b += B.matn(
    'وَيَتَبَرَّؤُونَ مِنْ طَرِيقَةِ الرَّوَافِضِ الَّذِينَ يُبْغِضُونَ الصَّحَابَةَ '
    'وَيَسُبُّونَهُمْ، وَمِنْ طَرِيقَةِ النَّوَاصِبِ الَّذِينَ يُؤْذُونَ أَهْلَ '
    'البَيْتِ بِقَوْلٍ أَوْ عَمَلٍ.')
b += B.sharh(
    p('The two previous lessons built the two halves of this clause, and here they are '
      'joined. <strong>Lesson 47 established the ranks of the Companions; Lesson 48 '
      'established the right of the household.</strong> A man can go wrong by denying '
      'either one — and the two errors are mirror images.') +
    table([
        row(ar('الرَّوَافِض'),
            '<em>From <strong>%s</strong>, to abandon — <strong>they were named so '
            'because they abandoned Zayd ibn ʿAlī</strong> when he refused to revile '
            'the two Shaykhs. <strong>They hate the Companions and revile them</strong>, '
            'and they go to excess regarding ʿAlī and the household.</em>'
            % ar('الرَّفْض')),
        row(ar('النَّوَاصِب'),
            '<em>From <strong>%s</strong> — <strong>they set up enmity</strong> toward '
            'the household of the Prophet ﷺ, <strong>and they harm them by a word or by '
            'a deed.</strong></em>' % ar('نَصْبُ العَدَاوَة')),
    ]) +
    p('Notice the wording of the matn on the Nawāṣib: <strong>«by a word or by a '
      'deed»</strong>. The sin is not confined to taking up arms. A tongue that '
      'belittles the household is already inside the description.') +
    p('And notice what the creed does with the pair. <strong>It does not pick a side '
      'between them.</strong> It disowns both — because both are built on the same '
      'mistake, which is making love of one group of the Prophet’s ﷺ people into a '
      'licence to attack another.'))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem"><strong>The middle position, '
    'stated as a line:</strong></p>'
    '<p style="margin:0;font-size:.95rem;text-align:center">'
    '<strong>النَّوَاصِب</strong> &nbsp;←&nbsp; جَفَاء &nbsp;·&nbsp; '
    '<strong>أَهْلُ السُّنَّة</strong> &nbsp;·&nbsp; غُلُوّ &nbsp;→&nbsp; '
    '<strong>الرَّوَافِض</strong></p>'
    '<p style="margin:.55rem 0 0;font-size:.9rem;text-align:center"><em>Coldness on one '
    'side, excess on the other — and the Sunnah is not the midpoint of a compromise but '
    'the only position that gives every party its actual right.</em></p>')

# ---------------------------------------------------------------- imsak
b += B.heading('الإِمْسَاكُ عَمَّا شَجَرَ بَيْنَ الصَّحَابَة',
               'Refraining from What Occurred Between the Companions')
b += B.matn(
    'وَيُمْسِكُونَ عَمَّا شَجَرَ بَيْنَ الصَّحَابَةِ، وَيَقُولُونَ: إِنَّ هَذِهِ '
    'الآثَارَ المَرْوِيَّةَ فِي مَسَاوِيهِمْ مِنْهَا مَا هُوَ كَذِبٌ، وَمِنْهَا مَا '
    'قَدْ زِيدَ فِيهِ وَنُقِصَ وَغُيِّرَ عَنْ وَجْهِهِ؛ وَالصَّحِيحُ مِنْهُ هُمْ '
    'فِيهِ مَعْذُورُونَ: إِمَّا مُجْتَهِدُونَ مُصِيبُونَ، وَإِمَّا مُجْتَهِدُونَ '
    'مُخْطِئُونَ.')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>what happened and arose between '
      'them</strong> of disputing and fighting</em>. And al-Fawzān sets out the position '
      'of Ahl al-Sunnah toward it <strong>in two matters</strong>, which it is worth '
      'keeping apart, because they answer two different questions.'
      % ar('مَا شَجَرَ')) +
    table([
        row('<span dir="rtl" lang="ar">الأَوَّل</span><br>'
            '<span style="font-size:.84rem;font-weight:400">what they DO</span>',
            '<strong>%s</strong> — <em>that is, <strong>they refrain from looking into '
            'it and do not plunge into it</strong></em>. The reason al-Fawzān gives is '
            'not that the history is unknowable: it is <em><strong>because plunging into '
            'that breeds rancour and hatred toward the Companions of the Messenger of '
            'Allah ﷺ — and that is of the gravest of sins. So the road of safety is '
            'silence about it.</strong></em>' % ar('يُمْسِكُونَ عَمَّا شَجَرَ بَيْنَهُمْ')),
        row('<span dir="rtl" lang="ar">الثَّانِي</span><br>'
            '<span style="font-size:.84rem;font-weight:400">what they SAY</span>',
            '<strong>the excusing of the narrations reported about their faults</strong> '
            '— <em>because in that is <strong>a defence of them and a repelling of the '
            'plotting of their enemies.</strong></em>'),
    ]) +
    p('Those two together are a single discipline. <strong>Silence is not evasion, '
      'because it is paired with an answer.</strong> Ahl al-Sunnah do not refuse the '
      'subject because they have nothing to say about it; they refuse to make a '
      'courtroom of it, while still answering the charge.'))

b += B.heading('الأَعْذَارُ الأَرْبَعَة', 'The Four Excuses')
b += B.sharh(
    p('al-Fawzān takes the matn’s clauses in order and makes four answers of them. They '
      'are not alternatives offered at random: <strong>they are applied in sequence, and '
      'each one only comes into play if the one before it does not dispose of the '
      'report.</strong>') +
    table([
        row('<strong>١</strong> &nbsp;' + ar('كَذِب'),
            '<em><strong>Some of it is a lie</strong>, which their enemies invented in '
            'order to disfigure their reputation — <strong>as the Rāfiḍah do</strong>. '
            '<strong>And a lie is not given any attention at all.</strong></em>'),
        row('<strong>٢</strong> &nbsp;' + ar('مُحَرَّف'),
            '<em>And some of it <strong>has been added to, subtracted from, and turned '
            'from its correct aspect</strong>, and falsehood has entered it — '
            '<strong>so it is distorted and not relied upon</strong>.</em>'),
        row('<strong>٣</strong> &nbsp;' + ar('مَعْذُورُونَ'),
            '<em><strong>And what is authentic of it — they are excused in it</strong>: '
            'either <strong>mujtahids who were correct</strong>, or <strong>mujtahids '
            'who erred</strong>.</em>'),
        row('<strong>٤</strong> &nbsp;' + ar('بَشَر'),
            '<em>And they do not hold <strong>that every one of the Companions is '
            'infallible from major sins and minor ones</strong> — <strong>rather sins '
            'are possible for them in general</strong>, as they are possible for any '
            'human being.</em>'),
    ], fs='.9rem'))
b += box(
    '<p style="margin:0 0 .55rem;font-size:.95rem"><strong>The reasoning under the '
    'second excuse is the one to carry away.</strong> al-Fawzān states it as a '
    'principle:</p>'
    '<p style="margin:0;font-size:.95rem"><em>— <strong>because the excellence of the '
    'Companions is KNOWN, and their integrity is CERTAIN; so the known and certain is '
    'not abandoned for a distorted matter that is doubted.</strong></em></p>'
    '<p style="margin:.6rem 0 0;font-size:.92rem">That is a rule about evidence, and it '
    'holds everywhere. <strong>A certainty is not surrendered to a doubt.</strong> The '
    'Companions’ standing was established by the Qurʾān and by mutawātir narration; a '
    'report of a fault reaches us through a chain that may be broken, partisan or '
    'tampered with. The weaker claim does not get to overturn the stronger one — and '
    'noticing which of two claims is the stronger is the whole of the skill.</p>')
b += B.ayah(
    'وَالسَّابِقُونَ الْأَوَّلُونَ مِنَ الْمُهَاجِرِينَ وَالْأَنْصَارِ وَالَّذِينَ '
    'اتَّبَعُوهُمْ بِإِحْسَانٍ رَضِيَ اللَّهُ عَنْهُمْ وَرَضُوا عَنْهُ',
    '"And the first forerunners among the Muhājirūn and the Anṣār, and those who '
    'followed them in excellence — Allah is pleased with them and they are pleased with '
    'Him."',
    'Sūrat al-Tawbah 9:100 · سُورَةُ التَّوْبَة')
b += B.prose(
    'That is the «known and certain» the principle refers to. <strong>Allah announced '
    'His pleasure with them in a text that is recited</strong> — and a narration of a '
    'fault, however it is dressed, arrives much later and by a much weaker road.')

# ---------------------------------------------------------------- ijtihad
b += B.heading('الاجْتِهَادُ وَأَجْرُ المُخْطِئ',
               'Ijtihād, and the Reward of the One Who Errs')
b += B.sharh(
    p('<strong>%s</strong> — <em><strong>the expending of one’s capacity in coming to '
      'know the Sharīʿah ruling.</strong></em> So the third excuse rests on a ḥadīth '
      'that settles how ijtihād is answered:' % ar('الاجْتِهَاد')))
b += B.hadith(
    'إِذَا اجْتَهَدَ الحَاكِمُ فَأَصَابَ فَلَهُ أَجْرَانِ، وَإِنِ اجْتَهَدَ '
    'وَأَخْطَأَ فَلَهُ أَجْرٌ وَاحِدٌ',
    '"When the judge exerts himself and is correct, he has two rewards; and when he '
    'exerts himself and errs, he has one reward."',
    'رَوَاهُ البُخَارِيُّ وَمُسْلِمٌ — عَنْ أَبِي هُرَيْرَةَ وَعَمْرِو بْنِ العَاصِ '
    'رَضِيَ اللهُ عَنْهُمَا')
b += B.sharh(
    p('Read what that does to the question. <strong>On neither branch is there sin.</strong> '
      'The correct one gains the reward of the effort and the reward of hitting the '
      'truth; the mistaken one still gains the reward of the effort, '
      '<strong>and his mistake is forgiven</strong>.') +
    p('So al-Fawzān can close the matter cleanly: what issues from a Companion by way of '
      'error — <strong>and it is little</strong> — falls into one of two cases:') +
    table([
        row('<strong>١</strong>',
            '<em>it issued <strong>from ijtihād</strong> — <strong>and in that he is '
            'rewarded, and his error is forgiven</strong></em>'),
        row('<strong>٢</strong>',
            '<em>it issued <strong>from other than ijtihād</strong> — <strong>and he has '
            'of deeds, excellences and good precedents what expiates it and effaces '
            'it</strong></em>'),
    ]) +
    p('<strong>There is no third case, and neither of the two leaves anything for us to '
      'prosecute.</strong> That is why the silence of the first matter is not a cover-up: '
      'once the reckoning is done, there is simply nothing left that a later man is '
      'entitled to try.'))

# ---------------------------------------------------------------- mukaffirat
b += B.heading('المُكَفِّرَاتُ · لِمَاذَا يُغْفَرُ لَهُمْ مَا لَا يُغْفَرُ لِمَنْ بَعْدَهُمْ',
               'The Expiators — Why They Are Forgiven What Later Men Are Not')
b += B.matn(
    'وَلَهُمْ مِنَ السَّوَابِقِ وَالفَضَائِلِ مَا يُوجِبُ مَغْفِرَةَ مَا يَصْدُرُ '
    'مِنْهُمْ إِنْ صَدَرَ، حَتَّى إِنَّهُمْ يُغْفَرُ لَهُمْ مِنَ السَّيِّئَاتِ مَا '
    'لَا يُغْفَرُ لِمَنْ بَعْدَهُمْ؛ لِأَنَّ لَهُمْ مِنَ الحَسَنَاتِ الَّتِي تَمْحُو '
    'السَّيِّئَاتِ مَا لَيْسَ لِمَنْ بَعْدَهُمْ.')
b += B.sharh(
    p('al-Fawzān gives three grounds, and the first is proved by a case from the Sīrah '
      'that every student already knows.') +
    p('<strong>١ · %s</strong> — <em>they have of prior precedents and excellences what '
      'necessitates the forgiveness of what issues from them</em>. <em>Like the story of '
      '<strong>حَاطِبِ بْنِ أَبِي بَلْتَعَةَ</strong> — regarding what occurred from '
      'him at the conquest: <strong>he was forgiven for it because he had been present '
      'at Badr.</strong></em>' % ar('السَّوَابِقُ وَالفَضَائِل')))
b += B.ayah(
    'إِنَّ الْحَسَنَاتِ يُذْهِبْنَ السَّيِّئَاتِ',
    '"Indeed, good deeds efface evil deeds."',
    'Sūrat Hūd 11:114 · سُورَةُ هُود')
b += B.sharh(
    p('<strong>٢ · %s</strong> — <em>the good deeds are multiplied for them</em>, as he '
      'ﷺ said:' % ar('تَضَاعُفُ الحَسَنَات')))
b += B.hadith(
    'خَيْرُ القُرُونِ قَرْنِي، ثُمَّ الَّذِينَ يَلُونَهُمْ، ثُمَّ الَّذِينَ '
    'يَلُونَهُمْ',
    '"The best of generations is my generation, then those who follow them, then those '
    'who follow them."',
    'رَوَاهُ البُخَارِيُّ وَمُسْلِمٌ')
b += B.sharh(
    p('<em>And <strong>%s</strong> is <strong>the people of a single, near-together age '
      'who share in some one of the intended matters</strong>; and it is also used of '
      '<strong>a span of time</strong>.</em>' % ar('القَرْن')) +
    p('<strong>٣ · %s</strong> — <em>the abundance of the expiators of sins that they '
      'have</em>. al-Fawzān lists them, and the list is the point: a sin of theirs has '
      'to pass through all of these before it could stand.'
      % ar('كَثْرَةُ المُكَفِّرَات')) +
    table([
        row(ar('التَّوْبَة'), '<em>he repented of it</em>'),
        row(ar('الحَسَنَات'), '<em>or he brought good deeds that effaced it</em>'),
        row(ar('السَّابِقَة'), '<em>or it was forgiven him by the merit of his '
            'precedence</em>'),
        row(ar('الشَّفَاعَة'),
            '<em>or by <strong>the intercession of Muḥammad ﷺ — and they are the most '
            'deserving of people of his intercession</strong></em>'),
        row(ar('البَلَاء'),
            '<em>or he was tried with an affliction in this world by which it was '
            'expiated from him</em>'),
    ], fs='.92rem'))
b += B.hadith(
    'مَا يُصِيبُ المُؤْمِنَ مِنْ وَصَبٍ وَلَا نَصَبٍ وَلَا غَمٍّ وَلَا هَمٍّ وَلَا '
    'حَزَنٍ، حَتَّى الشَّوْكَةِ يُشَاكُهَا، إِلَّا كَفَّرَ اللهُ بِهَا مِنْ '
    'خَطَايَاهُ',
    '"No sickness befalls the believer, nor fatigue, nor distress, nor anxiety, nor '
    'grief — not even a thorn that pricks him — but that Allah expiates by it some of '
    'his sins."',
    'مُتَّفَقٌ عَلَيْهِ')
b += B.prose(
    '<strong>And the Companions are the foremost of people in that</strong> — emigration, '
    'dispossession, hunger, wounds and the loss of their own families. Read the list of '
    'expiators against the lives they actually lived and the conclusion is not generous, '
    'it is arithmetical.')

b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem"><strong dir="rtl" lang="ar">'
    'تَنْبِيهٌ مُهِمّ</strong> — al-Fawzān turns here from the old sects to a '
    'living one.</p>'
    '<p style="margin:0 0 .5rem;font-size:.94rem"><em>And of what has occurred from some '
    'of the later writers of this age: that <strong>they made themselves a judge between '
    'the Companions of the Messenger of Allah ﷺ, declaring this one right and that one '
    'wrong — without any evidence</strong>, but rather by following desire and imitating '
    'those with an agenda, who attempt to insinuate against the Muslims by casting doubt '
    'upon their glorious history and their righteous predecessors — '
    '<strong>in order to pass from that to attacking Islam itself and splitting the word '
    'of the Muslims.</strong></em></p>'
    '<p style="margin:0;font-size:.92rem">Mark the mechanism he describes, because it is '
    'the reason this clause of the creed is not an antiquarian matter. '
    '<strong>The attack does not begin with the religion; it begins with its '
    'carriers.</strong> Discredit the generation that transmitted the Qurʾān and the '
    'Sunnah, and the texts they carried are discredited without ever being argued with. '
    'That is why Ahl al-Sunnah guard this point so jealously — not out of sentiment '
    'about the past, but because the chain of the religion runs through those men.</p>',
    wash='#fff8e6', edge='#d4a017')

b += B.heading('فَضَائِلُهُمْ جُمْلَةً', 'Their Excellences, Taken Together')
b += B.sharh(
    p('al-Fawzān closes the section by gathering what the whole of it rests on. Each item '
      'is the highest of its own class — which is why the total is not merely large but '
      'unmatchable.') +
    table([
        row('<strong>١</strong>', '<em>الإِيمَانُ بِاللهِ وَرَسُولِهِ — <strong>and it '
            'is the best of deeds</strong></em>'),
        row('<strong>٢</strong>', '<em>الجِهَادُ فِي سَبِيلِ اللهِ — <strong>and it is '
            'the summit of the peak of Islam</strong></em>'),
        row('<strong>٣</strong>', '<em>الهِجْرَةُ فِي سَبِيلِ اللهِ — <strong>and it is '
            'of the best of deeds</strong></em>'),
        row('<strong>٤</strong>', '<em>النُّصْرَةُ لِدِينِ اللهِ</em>'),
        row('<strong>٥</strong>', '<em>العِلْمُ النَّافِعُ وَالعَمَلُ الصَّالِح</em>'),
        row('<strong>٦</strong>', '<em>أَنَّهُمْ خَيْرُ الخَلْقِ بَعْدَ الأَنْبِيَاء</em>'),
    ], fs='.92rem'))
b += B.ayah(
    'وَيَنْصُرُونَ اللَّهَ وَرَسُولَهُ أُولَئِكَ هُمُ الصَّادِقُونَ',
    '"And they support Allah and His Messenger — it is they who are the truthful."',
    'Sūrat al-Ḥashr 59:8 · سُورَةُ الحَشْر')
b += B.ayah(
    'كُنْتُمْ خَيْرَ أُمَّةٍ أُخْرِجَتْ لِلنَّاسِ تَأْمُرُونَ بِالْمَعْرُوفِ '
    'وَتَنْهَوْنَ عَنِ الْمُنْكَرِ وَتُؤْمِنُونَ بِاللَّهِ',
    '"You are the best nation brought forth for mankind: you enjoin the right, forbid '
    'the wrong, and believe in Allah."',
    'Sūrat Āl ʿImrān 3:110 · سُورَةُ آلِ عِمْرَان')
b += B.prose(
    'And if this Ummah is the best of nations, <strong>then the best of this Ummah is the '
    'best of mankind after the Prophets</strong> — which is exactly the rank the ḥadīth '
    'of the generations gives them. <strong>That is the whole of Part Six in one '
    'step:</strong> their rank is not a claim made on their behalf; it is read off two '
    'āyāt and a ḥadīth, and every clause of this section has been a consequence of it.')

b += B.vocab([
    ('الرَّوَافِض', 'al-rawāfiḍ', 'the Rāfiḍah',
     'From الرَّفْض, abandoning — they abandoned Zayd ibn ʿAlī when he refused to '
     'revile the two Shaykhs; they hate and revile the Companions'),
    ('النَّوَاصِب', 'al-nawāṣib', 'the Nawāṣib',
     'From نَصْبُ العَدَاوَة, setting up enmity — they harm the household of the '
     'Prophet ﷺ by a word or by a deed'),
    ('مَا شَجَرَ', 'mā shajara', 'what arose, what occurred',
     'What happened and arose between the Companions of disputing — from the image of '
     'branches tangling'),
    ('الإِمْسَاك', 'al-imsāk', 'refraining, holding back',
     'They refrain from looking into it and do not plunge into it — because plunging '
     'breeds rancour toward the Companions'),
    ('الاجْتِهَاد', 'al-ijtihād', 'juristic exertion',
     'The expending of one’s capacity in coming to know the Sharīʿah ruling'),
    ('مُحَرَّف', 'muḥarraf', 'distorted',
     'Added to, subtracted from and turned from its correct aspect — so it is not '
     'relied upon'),
    ('السَّوَابِق', 'al-sawābiq', 'prior precedents',
     'Earlier merits that necessitate forgiveness — Ḥāṭib was forgiven for having been '
     'present at Badr'),
    ('القَرْن', 'al-qarn', 'a generation',
     'The people of a single near-together age who share in some intended matter; also '
     'used of a span of time'),
    ('المُكَفِّرَات', 'al-mukaffirāt', 'the expiators',
     'Repentance · good deeds · precedence · the intercession of the Prophet ﷺ · '
     'affliction in this world'),
])
b += B.mcq('ws-l49', [
    ('Why are the Rāfiḍah so named?',
     ['Because they rejected the Qurʾān',
      'From الرَّفْض, abandoning — they abandoned Zayd ibn ʿAlī when he refused to '
      'revile the two Shaykhs',
      'Because they were rejected from Madīnah',
      'Because they abandoned the prayer'], 1),
    ('What do the Nawāṣib do, per the matn?',
     ['They deny the attributes of Allah',
      'They set up enmity toward Ahl al-Bayt and harm them by a word or by a deed — so '
      'the sin is not confined to fighting',
      'They exaggerate regarding ʿAlī',
      'They reject the ḥadīth of the generations'], 1),
    ('What reason does al-Fawzān give for refraining from what occurred between the '
     'Companions?',
     ['That the reports are all lost',
      'That plunging into it breeds rancour and hatred toward the Companions — which is '
      'of the gravest of sins; so silence is the road of safety',
      'That the matter is not part of the creed',
      'That only the scholars of ḥadīth may study it'], 1),
    ('What is the SECOND thing Ahl al-Sunnah do about it, alongside refraining?',
     ['They record it without comment',
      'They excuse the narrations reported about their faults — because in that is a '
      'defence of them and a repelling of their enemies’ plotting',
      'They curse whoever narrates it',
      'They declare all such reports fabricated without examination'], 1),
    ('What is the principle under the second excuse (the distorted reports)?',
     ['That weak ḥadīth may be acted on in virtues',
      'That the Companions’ excellence is KNOWN and their integrity CERTAIN — so the '
      'known and certain is not abandoned for a distorted, doubted matter',
      'That a narration with one defect is rejected outright',
      'That history is not a source of creed'], 1),
    ('What does the ḥadīth of the judge establish about ijtihād?',
     ['That only a judge may perform ijtihād',
      'That on neither branch is there sin — correct brings two rewards, erring still '
      'brings one, and the error is forgiven',
      'That a mistaken judge must be removed',
      'That ijtihād ceased after the Companions'], 1),
    ('Which case from the Sīrah does al-Fawzān use for "prior precedents"?',
     ['The case of Kaʿb ibn Mālik and the battle of Tabūk',
      'Ḥāṭib ibn Abī Baltaʿah — forgiven for what occurred from him at the conquest '
      'because he had been present at Badr',
      'The three who were left behind',
      'The story of the slanderers of ʿĀʾishah'], 1),
    ('What is القَرْن, as defined here?',
     ['A hundred years exactly',
      'The people of a single near-together age who share in some intended matter — and '
      'it is also used of a span of time',
      'The Companions alone',
      'A tribe descended from one father'], 1),
    ('What mechanism does al-Fawzān warn against in modern writers?',
     ['Writing history in a foreign language',
      'Making themselves a judge between the Companions without evidence — casting doubt '
      'on the predecessors in order to pass from there to attacking Islam and splitting '
      'the Muslims',
      'Relying only on al-Bukhārī and Muslim',
      'Teaching the Sīrah to children'], 1),
    ('Why is a Companion’s sin covered by more expiators than a later man’s?',
     ['Because they were granted infallibility',
      'Because they have what later men do not: multiplied good deeds, prior precedence, '
      'the foremost claim to his ﷺ intercession, and far greater affliction',
      'Because their sins were all minor',
      'Because no record of their deeds was kept'], 1),
])
b += B.tf('ws-l49-tf', [
    ('يَعْتَقِدُ أَهْلُ السُّنَّةِ أَنَّ كُلَّ صَحَابِيٍّ مَعْصُومٌ مِنَ الذُّنُوبِ.',
     'Ahl al-Sunnah hold that every Companion is infallible from sins.', False),
    ('إِيذَاءُ أَهْلِ البَيْتِ بِالقَوْلِ وَحْدَهُ مِنْ طَرِيقَةِ النَّوَاصِبِ.',
     'Harming Ahl al-Bayt by speech alone falls under the way of the Nawāṣib.', True),
    ('المُجْتَهِدُ المُخْطِئُ آثِمٌ وَإِنْ بَذَلَ طَاقَتَهُ.',
     'A mujtahid who errs is sinful even though he expended his capacity.', False),
    ('العِلْمُ المُتَيَقَّنُ بِفَضْلِ الصَّحَابَةِ لَا يُتْرَكُ لِأَثَرٍ مُحَرَّفٍ '
     'مَشْكُوكٍ فِيهِ.',
     'The certain knowledge of the Companions’ excellence is not abandoned for a '
     'distorted, doubted report.', True),
    ('البَلَاءُ فِي الدُّنْيَا مِنْ مُكَفِّرَاتِ الذُّنُوبِ.',
     'Affliction in this world is among the expiators of sins.', True),
])
b += B.memorize(
    'وَالصَّحِيحُ مِنْهُ هُمْ فِيهِ مَعْذُورُونَ',
    'Fix the order of the four answers, because the order is the argument. '
    '<strong>A lie gets no attention; a distorted report is not relied on; what is '
    'authentic is excused ijtihād; and they were never claimed to be sinless in the '
    'first place.</strong> By the time a charge has passed all four, there is nothing '
    'left to try — and that, not ignorance, is why Ahl al-Sunnah keep silent.')
b += B.aiquiz('The clause of al-Aqidah al-Wasitiyyah on disowning the Rafidah and the '
              'Nawasib and refraining from what occurred between the Companions: why the '
              'Rafidah are so named, that the Nawasib harm the household by a word or a '
              'deed, the two matters of imsak and excusing the reports, the four excuses '
              'in order, the principle that the known and certain is not abandoned for a '
              'distorted doubted report, the hadith of the judge and the reward of the '
              'mistaken mujtahid, the case of Hatib ibn Abi Baltaah and Badr, the '
              'definition of al-qarn, the list of expiators, and al-Fawzans warning about '
              'modern writers who judge between the Companions without evidence')
b += B.further()
b += B.nav('was-l48-ahl-al-bayt-wa-al-azwaj.html',
           'The Household and the Wives of the Prophet ﷺ',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l49')

io.open(os.path.join(B.AQ, 'was-l49-ma-shajara-bayna-al-sahabah.html'), 'w',
        encoding='utf-8', newline='\n').write(B.shell(
    'الإِمْسَاكُ عَمَّا شَجَرَ بَيْنَ الصَّحَابَة',
    'Refraining from What Occurred Between the Companions',
    'Lesson 49 of al-ʿAqīdah al-Wāsiṭiyyah: disowning both the Rāfiḍah and the Nawāṣib; '
    'the two matters of refraining and answering; the four excuses for the narrations of '
    'the Companions’ faults; the ḥadīth of the judge and the reward of the mistaken '
    'mujtahid; and the expiators that cover a Companion’s sin as they cover no later '
    'man’s.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ التَّاسِعُ وَالأَرْبَعُون', '6',
           'الإِمْسَاكُ عَمَّا شَجَرَ بَيْنَ الصَّحَابَة',
           'Refraining from What Occurred Between the Companions', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l49-ma-shajara-bayna-al-sahabah.html')
