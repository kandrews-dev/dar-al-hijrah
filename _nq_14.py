# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 14 — النَّاقِضُ الثَّامِن, part 1: المُوَالَاةُ وَالتَّوَلِّي.

Printed folios 194-204 (PDF indices 191-201, offset +3). The eighth nullifier
runs printed 194-222 — 29 folios — so it takes two lessons. Part 2 takes
205-222, beginning at the book's own heading «الاسْتِعَانَةُ بِالكُفَّارِ عَلَى
الكُفَّار».

**The whole clause turns on one distinction, and Ibn Bāz states it in six
words:** «المُوَالَاةُ غَيْرُ التَّوَلِّي؛ **المُوَالَاةُ مَعْصِيَة،
وَالتَّوَلِّي كُفْر**» — and تَوَلِّي he defines as «مُسَاعَدَتُهُمْ عَلَى
المُسْلِمِين». A page that collapses those two has not taught the clause; it
has manufactured a takfīr the source refuses.

What the sharḥ actually does with it:

  * The أَصْل first: barāʾah from the mushrikīn and from their religion,
    disbelief in it, and walāʾ to the people of tawḥīd — «هَذَا أَصْلٌ
    أَصِيل», grounded in al-Baqarah 2:256. And: «مَحَبَّةُ الكُفْرِ
    وَالرِّضَا بِهِ كُفْرٌ مُسْتَقِلّ **وَإِنْ لَمْ يَفْعَلْهُ
    الإِنْسَان**».
  * **Three divisions, named by Ibn Bāz himself** — «هَذِهِ الأَقْسَامُ
    الثَّلَاثَةُ وَاقِعَة»: (1) aiding them against the Muslims, loving their
    religion, being pleased with kufr → **رِدَّة**; (2) friendship or love for
    a worldly matter, not for love of their religion → **مُنْكَرٌ وَمِنْ
    وَسَائِلِ الشِّرْك** — *not* ridda; (3) cooperation in worldly matters at
    need, and seeking help against another disbeliever → **جَائِز**, with the
    Prophet's ﷺ own precedents: the Jews of Khaybar, al-Muṭʿim ibn ʿAdī, Abū
    Ṭālib, Abū Bakr with Ibn al-Dughunnah, and ʿAbdullāh ibn Urayqiṭ al-Dīlī
    as the guide to Madīnah.
  * **And two refusals to inflate, both concrete and modern.** Asked whether
    raising the tawḥīd banner beside the banner of the cross is تَوَلِّي:
    «**كَلَّا، هَذَا نَوْعُ تَشَبُّه**». Asked about cheering a disbelieving
    footballer: the duty is not to cheer them — «**وَلَيْسَ هَذَا مِنَ
    المُوَالَاةِ المُكَفِّرَة؛ لَكِنَّهُ نَوْعُ مُوَالَاة، مَعْصِيَة**».
    Attending their festivals, laughing with them, being at ease with them —
    «مُوَالَاة، مَعْصِيَة، وَسِيلَةٌ لِلْكُفْر», and he says so in the same
    breath in which he forbids them.
  * الحَرْب against السِّلْم: in war, no aid whatever — «لَا سِلَاحٌ وَلَا
    مَالٌ وَلَا طَعَامٌ وَلَا غَيْرُ ذَلِك». In treaty: giving is fine, gifts,
    kinship, their poor and their disabled — al-Mumtaḥanah 60:8, Asmāʾ bint
    Abī Bakr, and the share of المُؤَلَّفَةُ قُلُوبُهُمْ, with Ṣafwān ibn
    Umayyah's own sentence about what the giving did to him.
  * **The footnote that keeps 60:8 honest**: البِرّ does not entail
    المَحَبَّة — «فَالبِرُّ شَيْء، وَالمَحَبَّةُ شَيْءٌ آخَر» — with the
    answers on al-Qaṣaṣ 28:56, on Ibrāhīm's barāʾah, and on the kitābiyyah
    wife. And its closing line on the method of ahl al-bidaʿ, which is worth
    the whole footnote.
  * الإِعْدَاد and الحَذَر as obligations in war **and** peace (4:102, 8:60) —
    «فَإِنَّ الأَعْدَاءَ لَا يُؤْتَمَنُونَ أَبَدًا» — and then, in the very
    next breath, that none of this blocks daʿwah: «**هَذِهِ البَغْضَاءُ...
    لَا تَمْنَعُ مِنَ الدَّعْوَةِ لَهُمْ وَالحِرْصِ عَلَى
    هِدَايَتِهِم**».
  * الرُّكُون on Hūd 11:113, in two kinds; Balʿam on al-Aʿrāf 7:175 — with Ibn
    Bāz on the story itself: «مِنْ أَخْبَارِ بَنِي إِسْرَائِيل، لَكِنَّ
    القُرْآنَ كَافٍ»; and that التَّوَلِّي is of المَسَائِلُ الظَّاهِرَة, with
    the limit on the excuse of ignorance.

Rule 8: no ḥadīth on these folios carries a grading from the sharḥ, and the
narrative reports (Asmāʾ, Ṣafwān, Khaybar, Ibn al-Dughunnah, Ibn Urayqiṭ) are
given as the sharḥ gives them — as the Shaykh's own recounting, without
isnād or grading — so the page says so and supplies none. The Balʿam story is
explicitly left as an isrāʾīlī report on his own instruction.
"""
import io, os, importlib.util

spec = importlib.util.spec_from_file_location('nq', os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '_nqbuild.py'))
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


def box(inner, wash='var(--brand-wash)', edge='var(--brand)'):
    return ('<div style="background:%s;border-right:4px solid %s;'
            'border-radius:var(--radius-sm);padding:var(--space-md);'
            'margin:0 0 .8rem">%s</div>' % (wash, edge, inner))


def row(k, v):
    return ('<tr><td style="padding:.62rem .8rem;border:1px solid var(--line);'
            'white-space:nowrap;vertical-align:top"><strong>%s</strong></td>'
            '<td style="padding:.62rem .8rem;border:1px solid var(--line)">%s</td></tr>'
            % (k, v))


def row3(a, b_, c):
    return ('<tr><td style="padding:.62rem .8rem;border:1px solid var(--line);'
            'vertical-align:top">%s</td>'
            '<td style="padding:.62rem .8rem;border:1px solid var(--line);'
            'vertical-align:top">%s</td>'
            '<td style="padding:.62rem .8rem;border:1px solid var(--line);'
            'vertical-align:top">%s</td></tr>' % (a, b_, c))


def thead3(a, b_, c):
    cell = ('<th style="padding:.5rem .8rem;border:1px solid var(--line);'
            'text-align:left;font-size:.76rem;letter-spacing:.05em;'
            'text-transform:uppercase;color:var(--ink-light)">%s</th>')
    return '<tr>' + (cell % a) + (cell % b_) + (cell % c) + '</tr>'


def table(rows, fs='.91rem'):
    return ('<div style="overflow-x:auto"><table style="width:100%%;'
            'border-collapse:collapse;font-size:%s;margin:0 0 .75rem">%s</table></div>'
            % (fs, ''.join(rows)))


def qa(q, a):
    return ('<div style="margin:0 0 .6rem;padding-right:.8rem;'
            'border-right:2px solid var(--line)">'
            '<p style="margin:0 0 .25rem;font-size:.88rem;color:var(--ink-light)">'
            '<strong>Q —</strong> <em>%s</em></p>'
            '<p style="margin:0;font-size:.93rem"><strong>Ibn Bāz —</strong> %s</p>'
            '</div>' % (q, a))


b = B.objectives([
    'State the %s of this clause — what is obligatory toward the mushrikīn and '
    'toward the people of tawḥīd — and the verse it rests on.' % ar('أَصْل'),
    'Give the <strong>three divisions</strong> Ibn Bāz names, with the ruling '
    'on each and an example of each.',
    'Define %s and %s as he defines them, and state the ruling on each in his '
    'own six words.' % (ar('المُوَالَاة'), ar('التَّوَلِّي')),
    'Give his answer on <strong>raising the banner beside the cross</strong> '
    'and on <strong>cheering a disbelieving sportsman</strong> — and say what '
    'each one is instead.',
    'Distinguish the state of <strong>war</strong> from the state of '
    '<strong>treaty</strong> in what may be given.',
    'Explain why al-Mumtaḥanah 60:8 does <strong>not</strong> establish love of '
    'the peaceful disbeliever — «%s».'
    % ar('فَالبِرُّ شَيْء، وَالمَحَبَّةُ شَيْءٌ آخَر'),
    'State the two obligations of %s and %s, and the thing the sharḥ says the '
    'enmity does <strong>not</strong> prevent.'
    % (ar('الإِعْدَاد'), ar('الحَذَر')),
    'Say when ignorance is an excuse in this clause and when it is not.',
])

b += B.provenance(194, 204)

b += B.matn(
    'الثَّامِن: مُظَاهَرَةُ المُشْرِكِينَ وَمُعَاوَنَتُهُمْ عَلَى '
    'المُسْلِمِين؛ وَالدَّلِيلُ قَوْلُهُ تَعَالَى: '
    '﴿وَمَنْ يَتَوَلَّهُمْ مِنْكُمْ فَإِنَّهُ مِنْهُمْ إِنَّ اللهَ لَا '
    'يَهْدِي القَوْمَ الظَّالِمِينَ﴾.',
    'Read the clause’s own wording before anything else: it names '
    '<strong>مُظَاهَرَة</strong> and <strong>مُعَاوَنَة</strong> — backing and '
    'aiding — and it names what they are <em>against</em>: «عَلَى '
    'المُسْلِمِين».')
b += B.ayah(
    'يَا أَيُّهَا الَّذِينَ آمَنُوا لَا تَتَّخِذُوا الْيَهُودَ '
    'وَالنَّصَارَىٰ أَوْلِيَاءَ بَعْضُهُمْ أَوْلِيَاءُ بَعْضٍ وَمَن '
    'يَتَوَلَّهُم مِّنكُمْ فَإِنَّهُ مِنْهُمْ إِنَّ اللَّهَ لَا يَهْدِي '
    'الْقَوْمَ الظَّالِمِينَ',
    'O you who believe, do not take the Jews and the Christians as allies. '
    'They are allies of one another. And whoever among you allies with them — '
    'then he is one of them. Indeed, Allah does not guide the wrongdoing '
    'people.',
    'سُورَةُ المَائِدَة · 5:51')
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><strong>This clause has a '
        'distinction at its centre, and the sharḥ spends most of twenty-nine '
        'folios on it.</strong> Ibn Bāz states it in six words:</p>'
        '<p style="margin:0 0 .5rem;font-size:1.05rem"><span dir="rtl" lang="ar">'
        '«المُوَالَاةُ غَيْرُ التَّوَلِّي؛ <strong>المُوَالَاةُ مَعْصِيَة، '
        'وَالتَّوَلِّي كُفْر</strong>.»</span></p>'
        '<p style="margin:0;font-size:.93rem"><em>«Allying is not the same as '
        'siding-with; <strong>allying is a sin, and siding-with is '
        'disbelief</strong>»</em> — and siding-with he defines as '
        '<strong>«مُسَاعَدَتُهُمْ عَلَى المُسْلِمِين»</strong>, aiding them '
        'against the Muslims. <strong>A reading that collapses the two has not '
        'taught this clause; it has manufactured a takfīr the source '
        'refuses.</strong></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))

# ---------------------------------------------------------------- the asl
b += B.heading('أَصْلٌ أَصِيل', 'The Foundation, Stated First')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><em>«What is obligatory upon every '
        'Muslim is <strong>disownment of the mushrikīn</strong>, and '
        '<strong>disownment of their religion</strong>, and '
        '<strong>disbelief in that</strong>; and <strong>allegiance to the '
        'people of tawḥīd</strong> and love of them and love of their religion. '
        '<strong>هَذَا أَصْلٌ أَصِيل</strong> — this is a foundational '
        'foundation.»</em></p>') +
    p('<em>And he states it in both directions, because it is one thing with two '
      'faces:</em> <strong>«فَتَجِبُ المَحَبَّةُ لِلْمُؤْمِنِينَ وَمَحَبَّةُ '
      'دِينِهِمْ وَمُوَالَاتُهُمْ عَلَى ذَلِك… وَتَجِبُ المُعَادَاةُ '
      'لِلْكَافِرِينَ، وَالبَغْضُ لَهُمْ، وَتَجِبُ البَرَاءَةُ مِنْ دِينِهِمْ '
      'وَاعْتِقَادُ بُطْلَانِه.»</strong>'))
b += B.ayah(
    'فَمَن يَكْفُرْ بِالطَّاغُوتِ وَيُؤْمِن بِاللَّهِ فَقَدِ اسْتَمْسَكَ '
    'بِالْعُرْوَةِ الْوُثْقَىٰ لَا انفِصَامَ لَهَا',
    'So whoever disbelieves in false objects of worship and believes in Allah '
    'has grasped the most trustworthy handhold, which will not break.',
    'سُورَةُ البَقَرَة · 2:256')
b += B.prose(
    '<strong>Note the order inside the verse, because the sharḥ leans on '
    'it:</strong> the disbelief in the ṭāghūt comes <em>first</em>, and the '
    'belief in Allah second. <em>«فَلَا بُدَّ مِنَ الكُفْرِ بِالطَّاغُوت، '
    'وَالإِيمَانِ بِالله.»</em> Which is why this clause is in a book of '
    'nullifiers at all: <strong>a man who grants allegiance where barāʾah is '
    'obliged has let go of one half of the handhold.</strong>')
b += B.sharh(
    p('And one sentence here is easy to pass over and should not be: '
      '<em>«and likewise <strong>love of disbelief and being pleased with '
      'it</strong> is an independent disbelief — '
      '<strong>وَإِنْ لَمْ يَفْعَلْهُ الإِنْسَان</strong>, even if the person '
      'does not do it.»</em>') +
    p('<em>That is the matn of the seventh nullifier arriving here</em> — '
      '«فَمَنْ فَعَلَهُ <strong>أَوْ رَضِيَ بِهِ</strong>» — '
      '<strong>and it means the clause is not only about deeds.</strong> '
      '<em>But keep reading, because the next thing the sharḥ does is tell you '
      'what is NOT this.</em>'))

# ---------------------------------------------------------------- three divisions
b += B.heading('الأَقْسَامُ الثَّلَاثَة', 'Three Divisions, Named by Him')
b += B.prose(
    '<strong>He sets them out himself and then counts them off</strong> — '
    '<em>«المَقْصُود: أَنَّ هَذِهِ الأَقْسَامَ الثَّلَاثَةَ وَاقِعَة»</em>. '
    '<em>This is the table to learn before anything else on the page.</em>')
b += B.sharh(table([
    thead3('', 'what it is', 'the ruling'),
    row3('<strong>القِسْمُ الأَوَّل</strong>',
         '<em>«Being pleased with disbelief and not denouncing it and not '
         'disowning it, <strong>or aiding the disbelievers against the Muslims '
         'and giving the disbelievers victory over the Muslims</strong>»</em> — '
         'and love of their <em>religion</em>',
         '<strong>رِدَّةٌ عَنِ الإِسْلَام</strong> — «وَمُظَاهَرَةُ '
         'المُشْرِكِينَ رِدَّةٌ عَنِ الإِسْلَام»'),
    row3('<strong>الثَّانِي</strong>',
         '<em>«<strong>Friendship with them or love of them for a worldly '
         'matter</strong>, and allying with them for that — '
         '<strong>not for love of their religion and not for giving them '
         'victory over the Muslims</strong>»</em>: for trade, a partnership, '
         'money hoped for, kinship',
         '<strong>مُنْكَرٌ وَمِنْ وَسَائِلِ الشِّرْك</strong> — forbidden, and '
         'a <em>means</em> to disbelief. <strong>NOT ridda.</strong>'),
    row3('<strong>الثَّالِث</strong>',
         '<em>«That help be sought from them <strong>against the enemies</strong>, '
         'against other disbelievers, or <strong>in the interests of the '
         'Muslims</strong>, without allegiance»</em>',
         '<strong>جَائِز</strong> — «فَهَذَا مِنَ القِسْمِ الجَائِز»'),
]))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><strong>And the third '
        'division is not a modern concession. He proves it entirely from the '
        'Prophet’s ﷺ own life and his Companions’.</strong></p>'
        '<p style="margin:0;font-size:.93rem">The <strong>Jews of '
        'Khaybar</strong>, left for the tilling and cultivation; '
        '<strong>al-Muṭʿim ibn ʿAdī</strong> and others, to restrain the harm of '
        'other wrongdoing disbelievers; his uncle <strong>Abū Ṭālib</strong>, '
        'against the disbelievers; <strong>al-Ṣiddīq</strong> with '
        '<strong>Ibn al-Dughunnah</strong>, a disbeliever, against the '
        'disbelievers — <em>«not for love of his religion, but to fight the '
        'other disbelievers»</em>; and <strong>ʿAbdullāh ibn Urayqiṭ '
        'al-Dīlī</strong>, hired to show the way to Madīnah.</p>'
        '<p style="margin:.5rem 0 0;font-size:.91rem;color:var(--ink-light)">'
        '<em>The sharḥ recounts all five as the Shaykh’s own recollection, '
        'without isnād or grading at this place, and the page reports them as '
        'he gives them.</em></p>'))
b += B.sharh(
    p('<strong>And the Khaybar case is qualified in the footnote rather than '
      'left as a blank licence</strong>, which is the sort of thing this book '
      'does well: <em>«he ﷺ kept the Jews at Khaybar <strong>for a temporary '
      'period</strong> for the tilling and cultivation, <strong>for the severe '
      'need</strong>, because of the Muslims being occupied with jihād. '
      'So the intent is that <strong>this and its like is what is permitted for '
      'a temporary, necessary, severe need — and it is not permissible to '
      'expand and be lax in these matters.</strong>»</em>') +
    p('<em>And ʿUmar’s expulsion of them is explained rather than left as a '
      'contradiction:</em> <em>«ʿUmar expelled them on account of '
      '<strong>events they brought about</strong>, and in <strong>execution of '
      'the Prophet’s ﷺ command</strong> to remove them from the Peninsula; '
      'ʿUmar carried this out in his time because he '
      '<strong>had the leisure</strong> for it and his rule was long — '
      '<strong>unlike al-Ṣiddīq, whose rule was short and who was occupied with '
      'the people of apostasy.</strong>»</em>'))

# ---------------------------------------------------------------- the distinction
b += B.heading('المُوَالَاةُ غَيْرُ التَّوَلِّي', 'The Distinction, and Where Each Line Falls')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><em>«As for taking him as a '
        '<strong>friend and a beloved</strong>, dealing with him as one deals '
        'with a friend — <strong>this is a kind of مُوَالَاة; and مُوَالَاة is '
        'not التَّوَلِّي. المُوَالَاة is a sin, and التَّوَلِّي is disbelief</strong>, '
        'and it is: <strong>aiding them against the Muslims</strong>. '
        'So المُوَالَاة is <strong>less and lower</strong> than '
        'التَّوَلِّي.»</em></p>'))
b += B.sharh(table([
    thead3('', 'المُوَالَاة — مَعْصِيَة', 'التَّوَلِّي — كُفْرٌ وَرِدَّة'),
    row3('<strong>his own examples</strong>',
         '<em>«their love, or <strong>presenting a gift</strong> to them, or '
         '<strong>cheerfulness in their faces</strong>, or '
         '<strong>initiating the greeting</strong> with them — this is a kind of '
         'the forbidden muwālāh»</em>; and attending their festivals, laughing '
         'with them, being at ease with them',
         '<em>«<strong>giving them victory over the Muslims, and aiding them '
         'against the Muslims</strong> — this is apostasy and a nullifier of '
         'Islām»</em>'),
    row3('<strong>its definition</strong>',
         'Friendship and love for a worldly cause — <em>«not for love of their '
         'religion, nor for being pleased with it, nor because it is '
         'true»</em>',
         'Ibn Bāz, asked for the standard: <em>«<strong>التَّوَلِّي هُوَ '
         'النَّصْر</strong>, as the scholars say… <strong>and its root is the '
         'love of hearts</strong>, then giving them victory and backing them '
         'against the Muslims <strong>points to it</strong>»</em>'),
    row3('<strong>what it is called</strong>',
         '<em>«وَتُسَمَّى مُوَالَاة»</em> — and <strong>«وَسَائِلُ مِنْ '
         'وَسَائِلِ الكُفْر وَشَرٌّ عَظِيمٌ يَجِبُ الحَذَرُ مِنْهَا»</strong>',
         '<em>«وَلَكِنَّ التَّوَلِّي كَوْنُهُ يَتَوَلَّاهُمْ '
         'وَيَنْصُرُهُمْ يُعِينُهُمْ عَلَى المُسْلِمِين — هَذَا رِدَّةٌ عَنِ '
         'الإِسْلَام»</em>'),
]) + p('<strong>«هَذَا شَيْءٌ وَهَذَا شَيْء» — this is one thing and that is '
       'another.</strong> <em>He says it in those words, and the reason he '
       'insists is not leniency: it is that the second thing is the '
       'catastrophe</em> — <strong>«حَتَّى لَا تَقَعَ الكَارِثَة»</strong>, '
       '<em>“so that the disaster does not occur.”</em> <strong>The whole point '
       'of keeping the lesser thing lesser is that you can still be warned off '
       'it without being told you have left Islām.</strong>'))
b += B.sharh(
    p('And he does not soften the lesser category while refusing to inflate it. '
      'What is obliged toward the disbeliever one deals with: '
      '<em>«that there be in your heart <strong>his hatred for Allah’s sake and '
      'enmity to him for Allah’s sake</strong>, and that you '
      '<strong>keep away from his friendship and allegiance in any '
      'place</strong>, and that <strong>he know that of you</strong> — and that '
      'you are an enemy to him and he an enemy to you, and that you are free of '
      'him and he is free of you.»</em>') +
    p('<em>And then the reason, which is the hinge:</em> '
      '<strong>«حَتَّى لَا تَقَعَ الكَارِثَة، وَهُوَ المُوَالَاةُ الَّتِي '
      'تَجْعَلُكَ كَافِرًا بِمَحَبَّةِ دِينِهِ أَوْ نُصْرَتِهِ عَلَى '
      'المُسْلِمِين.»</strong> <em>The sin is treated seriously precisely '
      'because it is the road to the nullifier — not because it is the '
      'nullifier.</em>'))

# ---------------------------------------------------------------- two refusals
b += B.heading('قِسْمَانِ: مَعْصِيَةٌ وَمُكَفِّرَة', 'Two Questions He Refuses to Inflate')
b += B.prose(
    '<strong>Here is where the distinction stops being theory.</strong> '
    '<em>Two concrete modern questions were put to him, of exactly the kind that '
    'get answered with takfīr by people quoting this clause — and he answered '
    'both the other way.</em>')
b += B.sharh(
    qa('Raising the banner of tawḥīd beside the banner of the cross — is that '
       'of التَّوَلِّي?',
       '<em>«<strong>كَلَّا</strong> — no. <strong>هَذَا نَوْعُ '
       'تَشَبُّه</strong> — this is a kind of imitation; because التَّوَلِّي, '
       'as I said, is <strong>giving them victory and backing them against the '
       'Muslims</strong>. We ask Allah for soundness.»</em>') +
    qa('Cheering a disbelieving footballer — is that of allegiance to him?',
       '<em>«This has been researched, and it was made clear to them that '
       '<strong>the duty is not to cheer them</strong>, and that the duty is '
       'that this be <strong>confined to the Muslims</strong>, and that the '
       'disbelievers not be cheered. <strong>وَلَيْسَ هَذَا مِنَ '
       'المُوَالَاةِ المُكَفِّرَة؛ لَكِنَّهُ نَوْعُ مُوَالَاة، '
       'مَعْصِيَة.</strong>»</em>') +
    p('And in the same answer he names the two categories outright: '
      '<strong>«المُوَالَاةُ قِسْمَانِ: مَعْصِيَةٌ وَمُكَفِّرَة»</strong> — '
      '<em>honouring him, softening speech with him, and the like, for the sake '
      'of coveting his wealth or something from him, is of the '
      '<strong>forbidden</strong> muwālāh; and the '
      '<strong>disbelief-entailing</strong> muwālāh is '
      '«أَنْ يَنْصُرَ الكُفَّارَ عَلَى المُسْلِمِينَ، وَأَنْ يُوَالِيَهُمْ '
      'ضِدَّ المُسْلِمِين».</em>') +
    p('<em>And attending their festivals, or laughing with them and being at '
      'ease with them:</em> <strong>«هَذِهِ مُوَالَاة، مَعْصِيَة، وَسِيلَةٌ '
      'لِلْكُفْر»</strong> — <em>allegiance, a sin, a means to disbelief.</em> '
      '<strong>Forbidden, and named a sin in the same sentence that forbids '
      'it.</strong>'))
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><strong>Count what he just '
        'declined to call apostasy:</strong> <em>a national banner flown beside '
        'a cross; cheering a sportsman; a gift; a smile; greeting first; '
        'attending a festival; laughing in their company.</em> '
        '<strong>Every one of these is forbidden in his answer, and not one of '
        'them is the nullifier.</strong> <em>The nullifier has one shape — '
        '«نَصْرُهُمْ عَلَى المُسْلِمِين» — and he will not let anything else '
        'wear it.</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))
b += B.heading('التَّوَلِّي العَامّ', 'And the Worst of It')
b += B.sharh(
    qa('التَّوَلِّي العَامّ?',
       '<em>«<strong>التَّوَلِّي العَامُّ هَذَا أَشَرُّهَا</strong> — the '
       'general siding-with, this is the worst of them: '
       '<strong>giving them victory over the Muslims, and backing them against '
       'the Muslims, and aiding them against the Muslims</strong> — this is '
       'apostasy from Islām: «وَمَنْ يَتَوَلَّهُمْ مِنْكُمْ فَإِنَّهُ '
       'مِنْهُمْ».»</em>') +
    qa('Does «وَمَنْ يَتَوَلَّهُمْ مِنْكُمْ فَإِنَّهُ مِنْهُمْ» '
       '<strong>necessitate</strong> disbelief for whoever allies with them?',
       '<em>«<strong>عَلَى حَسَبِ التَّوْلِيَة</strong> — according to the '
       'degree of the allying. <strong>So if he gave them victory and backed '
       'them against the Muslims, he was like them.</strong>»</em>') +
    p('<strong>«عَلَى حَسَبِ التَّوْلِيَة» is the answer to the verse being '
      'used as a blanket.</strong> <em>The verse is not read as a flat '
      'equation; it is read as graduated, and the top of the scale is named. '
      'That is the same move as «فِيهِ التَّفْصِيل» in the seventh nullifier '
      'and «الفَرْدُ وَالفَرْدَانِ فِسْق» in the sixth.</em>'))
b += B.sharh(
    p('He also gives the clearest single case of the nullifier in commerce, and '
      'it is worth having because it is exact: '
      '<em>«it is not permitted to cooperate with any human being upon sin and '
      'transgression — not by selling him grapes to make wine of, nor by selling '
      'him what aids him in gambling, <strong>nor by selling him what aids him '
      'in fighting the Muslims</strong>, as that he should '
      '<strong>sell the disbelievers weapons so that they may fight the Muslims '
      'with them — this is apostasy</strong>… this means '
      '<strong>تَوَلٍّ لِلْكُفَّار</strong>.»</em>') +
    p('<em>And immediately the comparison that keeps it exact:</em> '
      '<strong>«وَإِذَا بَاعَهُ عَلَى قُطَّاعِ الطَّرِيقِ أَوْ عَلَى '
      'البُغَاةِ صَارَ مُعَاوَنَةً عَلَى المَعَاصِي فَيَكُونُ مُحَرَّمًا '
      'وَمُنْكَرًا.»</strong> <em>Same weapon, same seller — and the ruling '
      'turns entirely on <strong>who it is to be used against</strong>. Sold '
      'to disbelievers to fight Muslims: apostasy. Sold to bandits or rebels: '
      'forbidden and an abomination, and not apostasy.</em>'))

# ---------------------------------------------------------------- war and peace
b += B.heading('حَالُ الحَرْبِ وَحَالُ السِّلْم', 'War and Peace Are Not the Same Chapter')
b += B.sharh(
    p('The clause has a hinge that is not about the heart at all — '
      '<strong>it is about whether there is a war on.</strong>') +
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><em>«<strong>But it differs '
        'in the state of war and of peace.</strong> So in the state of war with '
        'the enemies, <strong>it is not permissible that they be aided with '
        'anything at all — not weapons, nor money, nor food, nor anything '
        'else</strong>; because giving them is an aid to them against the '
        'Muslims and a backing of them, <strong>so that becomes disbelief and '
        'apostasy from Islām, and a nullifier of its nullifiers</strong>.»</em></p>'
        '<p style="margin:0;font-size:.94rem"><em>«As for in the state of peace, '
        'and of treaty, and of reconciliation — <strong>there is no objection to '
        'their being given</strong>: the relative gives his relative, and the '
        'Muslim gives the poor one, and the one in authority gives them what he '
        'sees benefit for the Muslims in, <strong>or exchanges gifts with '
        'them</strong>, or other than that in which he sees benefit — '
        '<strong>all of this there is no harm in, within the bounds of the '
        'Muḥammadan Sharīʿah</strong>.»</em></p>'))
b += B.sharh(
    p('And of the <strong>ḥarbī</strong> specifically: <em>«as for the '
      '<strong>warring disbelievers</strong>, it is not permissible to assist '
      'them with anything; rather assisting them against the Muslims is '
      '<strong>of the nullifiers of Islām</strong>»</em> — '
      '<em>«وَمَظَاهَرَةُ الكُفَّارِ وَمُسَاعَدَتُهُمْ وَمُعَاوَنَتُهُمْ '
      'ضِدَّ المُسْلِمِينَ هَذَا مِنْ نَوَاقِضِ الإِسْلَامِ '
      '<strong>عِنْدَ جَمِيعِ العُلَمَاء</strong>»</em>.') +
    p('<strong>And of the treaty state, the list is specific:</strong> '
      '<em>«there is no bar to assisting them and doing good to them in what '
      'they need — <strong>as their poor and their disabled</strong>, and the '
      'like of that, <strong>and the ties of kinship and the womb</strong>.»</em>'))
b += B.ayah(
    'لَّا يَنْهَاكُمُ اللَّهُ عَنِ الَّذِينَ لَمْ يُقَاتِلُوكُمْ فِي '
    'الدِّينِ وَلَمْ يُخْرِجُوكُم مِّن دِيَارِكُمْ أَن تَبَرُّوهُمْ '
    'وَتُقْسِطُوا إِلَيْهِمْ إِنَّ اللَّهَ يُحِبُّ الْمُقْسِطِينَ',
    'Allah does not forbid you from those who did not fight you over religion '
    'and did not expel you from your homes — that you should deal kindly and '
    'justly with them. Indeed, Allah loves the just.',
    'سُورَةُ المُمْتَحَنَة · 60:8')
b += B.sharh(
    p('And the case he brings for it is <strong>Asmāʾ bint Abī Bakr</strong> '
      'رَضِيَ اللهُ عَنْهُمَا: during the truce after the Prophet ﷺ made peace '
      'with the mushrikīn of Makkah on the laying down of war for ten years, '
      '<em>«her mother came in that period as a visitor to Madīnah, seeking her '
      'daughter Asmāʾ for assistance and support; so she asked the Prophet ﷺ for '
      'a ruling on that, <strong>and he ﷺ gave her the fatwā that she should '
      'maintain the tie with her</strong> — meaning: that she should do good to '
      'her with money.»</em>') +
    p('<em>The sharḥ gives that as the Shaykh’s own recounting, without isnād or '
      'grading at this place, and the page reports it as he gives it.</em>'))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><strong>And then he gives '
        'a reason for the kindness that reframes the whole category.</strong></p>'
        '<p style="margin:0 0 .5rem;font-size:.93rem"><em>«Then this doing of '
        'good, in the time of truce and the time of treaty, '
        '<strong>may be a path to guidance</strong>; it may be a cause of the '
        'Islām of the one given and the one treated well, and his entering into '
        'the religion of Allah. <strong>And for this Allah legislated, in the '
        'zakāh and in the treasury, a share for '
        'المُؤَلَّفَةُ قُلُوبُهُمْ</strong> — because a person may be given '
        'wealth while he is a mushrik, and Allah guides him to Islām '
        '<strong>by reason of the giving</strong>.»</em></p>'
        '<p style="margin:0;font-size:.93rem">And the case: '
        '<strong>Ṣafwān ibn Umayyah</strong>, who had held back from Islām, and '
        'the Prophet ﷺ kept giving him and treating him well until Islām entered '
        'upon him — <em>and his own sentence afterwards: '
        '«<strong>مَا كَانَ أَهْلُ بَيْتٍ أَبْغَضَ إِلَيَّ مِنْ رَسُولِ اللهِ '
        'ﷺ، فَلَمْ يَزَلْ يُعْطِينِي وَيُعْطِينِي حَتَّى صَارَ أَحَبَّ '
        'النَّاسِ إِلَيّ</strong>»</em> — “there was no household more hateful '
        'to me than the Messenger of Allah’s ﷺ; and he kept on giving me and '
        'giving me until he became the most beloved of people to me.”</p>',
        wash='var(--accent-wash)', edge='var(--accent)'))

# ---------------------------------------------------------------- birr vs hubb
b += B.heading('البِرُّ شَيْءٌ وَالمَحَبَّةُ شَيْءٌ آخَر', 'What 60:8 Does and Does Not Establish')
b += B.prose(
    '<strong>And the compiler’s footnote here is doing necessary work, because '
    '60:8 is the verse most often stretched.</strong> <em>Some use it to '
    'establish the permissibility of <strong>loving</strong> the peaceful '
    'disbeliever.</em>')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><em>«And this is '
        '<strong>an error</strong>, and the verse does not indicate it; '
        '<strong>because kindness toward a disbeliever does not entail love of '
        'the disbeliever. فَالبِرُّ شَيْء، وَالمَحَبَّةُ شَيْءٌ آخَر</strong> '
        '— kindness is one thing, and love is another. '
        'A person may be kind to an animal, or to one he hopes something '
        'from or fears, <strong>and love of it is not entailed by '
        'that</strong>.»</em></p>'))
b += B.sharh(
    p('<strong>Three further objections are answered, each in a way worth '
      'having:</strong>') +
    table([
        row('«إِنَّكَ لَا تَهْدِي مَنْ أَحْبَبْتَ»',
            'al-Qaṣaṣ 28:56 is read as <em>«you loved <strong>his '
            'guidance</strong>, not his person»</em> — and the occasion of '
            'revelation shows it: <em>he ﷺ was eager for him, loving his '
            'guidance; and when he was not guided, Allah sent down the '
            'verse</em>. <strong>And even granting the other reading</strong>, '
            'there is no argument in it: <em>the verse is Makkan, revealed about '
            'Abū Ṭālib; then Allah sent down in Madīnah «لَا تَجِدُ قَوْمًا '
            'يُؤْمِنُونَ بِاللهِ وَاليَوْمِ الآخِرِ يُوَادُّونَ مَنْ حَادَّ '
            'اللهَ وَرَسُولَه» and «قَدْ كَانَتْ لَكُمْ أُسْوَةٌ حَسَنَةٌ فِي '
            'إِبْرَاهِيم» — <strong>so if he had loved Abū Ṭālib, Allah '
            'forbade it to him after that</strong></em>'),
        row('Ibrāhīm’s barāʾah',
            'Some claimed Ibrāhīm said «%s» only <em>after</em> they hated and '
            'fought him. <strong>«وَهَذَا إِفْكٌ مُبِين»</strong> — and the '
            'refutation is from the verse’s own ending: he made the '
            '<strong>limit</strong> at which the enmity ceases their '
            '<strong>believing in the tawḥīd of Allah</strong> — '
            '«حَتَّى تُؤْمِنُوا بِاللهِ وَحْدَه» — <em>«and he did not say: '
            'until you leave off hating me and opposing me»</em>. '
            '<em>And it entails belittling that noble prophet — as though he '
            'hated them <strong>in his own defence</strong>, and did not hate '
            'them for their violating Allah’s sanctities and associating '
            'partners with Him. «سَاءَ مَا يَحْكُمُون.»</em>'
            % ar('بَدَا بَيْنَنَا وَبَيْنَكُمُ العَدَاوَةُ وَالبَغْضَاءُ '
                 'أَبَدًا')),
        row('the kitābiyyah wife',
            'The argument from marrying a disbelieving woman of the People of '
            'the Book, and the love and companionship it entails. '
            '<strong>Two answers:</strong> either it is '
            '<em>a matter a text has come with, so it is particularised to it '
            'and the ruling confined to it</em>; or <em>love of a disbelieving '
            'wife is <strong>a love of appetite</strong>, like love of a '
            'disbeliever’s food and drink — <strong>not an essential love nor a '
            'religious one</strong></em>. <strong>And the binding '
            'consequence:</strong> on their own reasoning they would have to '
            'permit loving the <em>warring</em> disbelievers too, '
            '<em>«because just as Allah made lawful to us the food and the women '
            'of the People of the Book of the people of dhimmah, so He permitted '
            'to us the food and women of the People of the Book who are at '
            'war»</em>'),
    ]))
b += B.sharh(
    box('<p style="margin:0;font-size:.95rem"><strong>And the footnote closes '
        'with a sentence about method that is worth more than the three answers '
        'put together.</strong></p>'
        '<p style="margin:.5rem 0 0;font-size:.95rem"><em>«And of the habit of '
        'the people of innovation is: <strong>objecting to the universals by '
        'the particulars, and striking the certainties with the probabilities, '
        'and overturning the consensuses by what is of the fallen among the '
        'possibilities.</strong> We seek refuge with Allah from '
        'ignorance.»</em></p>'
        '<p style="margin:.55rem 0 0;font-size:.92rem"><em>Three moves, and once '
        'you can name them you will see them everywhere — including, honestly, '
        'in arguments made on the stricter side of this very clause.</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))

# ---------------------------------------------------------------- idad
b += B.heading('الإِعْدَادُ وَالحَذَر', 'Preparation, Wariness — and Daʿwah')
b += B.sharh(
    p('<em>None of the permitted kindness relaxes two standing obligations, and '
      'he names both as</em> <strong>وَاجِب</strong> <em>in war and peace '
      'alike:</em>') +
    box('<p style="margin:0;font-size:.94rem"><em>«As for what pertains to '
        '<strong>preparation</strong> against them — this is '
        '<strong>obligatory</strong>; and likewise <strong>taking wariness '
        'of them is obligatory in war and peace together</strong>… so '
        'preparation against them and readiness for them and taking wariness of '
        'them, <strong>so that they do not seize us unawares</strong> — this is '
        'obligatory upon the guardians of the Muslims’ affairs: that they '
        'prepare for their enemies what they can of strength, and that they be '
        'ready for jihād, and that they beware the consequence of laxity; '
        '<strong>فَإِنَّ الأَعْدَاءَ لَا يُؤْتَمَنُونَ أَبَدًا</strong> — for '
        'the enemies are never to be trusted.»</em></p>'))
b += B.ayah(
    'يَا أَيُّهَا الَّذِينَ آمَنُوا خُذُوا حِذْرَكُمْ',
    'O you who believe, take your precaution.',
    'سُورَةُ النِّسَاء · 4:71')
b += B.ayah(
    'وَأَعِدُّوا لَهُم مَّا اسْتَطَعْتُم مِّن قُوَّةٍ',
    'And prepare against them whatever you are able of strength.',
    'سُورَةُ الأَنْفَال · 8:60')
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><strong>And then, in the '
        'next sentence, the thing that most readers of this clause never '
        'quote.</strong></p>'
        '<p style="margin:0;font-size:.98rem"><em>«Then <strong>this hatred and '
        'this enmity between us and them does not prevent calling them and being '
        'eager for their guidance</strong>; so the callers and those who direct '
        'to good <strong>are sent to them</strong> — '
        '<strong>perhaps Allah will bring them out of the darknesses into the '
        'light.</strong>»</em></p>'
        '<p style="margin:.55rem 0 0;font-size:.93rem"><em>Barāʾah and daʿwah '
        'in two consecutive sentences, by the same man, with no sense of strain '
        '— because they were never in tension. <strong>You do not call someone '
        'you have no hope for.</strong></em></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))
b += B.prose(
    'He adds the promise that makes the wariness bearable: <em>«but whenever the '
    'Muslims are granted hating them for Allah’s sake and opposing them for '
    'Allah’s sake, and <strong>their patience and their taqwā</strong> — their '
    'plotting will not harm them»</em> — on «%s». '
    '<em>And of the enemies in general, a sentence to hold without '
    'bitterness:</em> <strong>«كُلُّهُمْ يَسُرُّهُمْ مَا يَضُرُّنَا '
    'وَيَسُوؤُهُمْ مَا يَنْفَعُنَا.»</strong>'
    % ar('وَإِنْ تَصْبِرُوا وَتَتَّقُوا لَا يَضُرُّكُمْ كَيْدُهُمْ شَيْئًا'))

# ---------------------------------------------------------------- rukun
b += B.heading('الرُّكُون', 'Leaning On Them — Two Kinds')
b += B.ayah(
    'وَلَا تَرْكَنُوا إِلَى الَّذِينَ ظَلَمُوا فَتَمَسَّكُمُ النَّارُ',
    'And do not incline toward those who have done wrong, lest the Fire touch '
    'you.',
    'سُورَةُ هُود · 11:113')
b += B.sharh(
    p('<em>«This makes clear to us <strong>the danger of inclining</strong>, '
      'and that its affair is grave.»</em> And then, as everywhere in this '
      'clause, two kinds:') +
    table([
        row('الرُّكُونُ الأَوَّل',
            'Inclining <strong>to shirk and its people</strong> — '
            '<em>«هَذَا رِدَّةٌ عَنِ الإِسْلَام»</em>; '
            '<strong>«وَإِذَا نَاصَرَهُمْ وَعَاوَنَهُمْ عَلَى المُسْلِمِينَ '
            'فَهُوَ رِدَّةٌ عَنِ الإِسْلَام»</strong>'),
        row('الرُّكُونُ الثَّانِي',
            'Inclining <strong>to the oppressors</strong> — and aiding the '
            'oppressor in his oppression, the thief in his theft, the sinner in '
            'his sin — <em>«<strong>كُلُّهُ دَاخِلٌ فِي المَعْصِيَة</strong>»</em>. '
            '<strong>A sin, not apostasy.</strong>'),
    ]) +
    p('<em>«فَالوَاجِبُ الحَذَرُ مِنَ الرُّكُونِ لَا إِلَى هَؤُلَاءِ وَلَا '
      'إِلَى هَؤُلَاء» — and the duty is wariness of inclining to either '
      'party.</em> <strong>Both are forbidden; the rulings on them are not the '
      'same.</strong>'))
b += B.ayah(
    'وَاتْلُ عَلَيْهِمْ نَبَأَ الَّذِي آتَيْنَاهُ آيَاتِنَا فَانسَلَخَ '
    'مِنْهَا فَأَتْبَعَهُ الشَّيْطَانُ فَكَانَ مِنَ الْغَاوِينَ',
    'And recite to them the account of the one to whom We gave Our signs, but '
    'he sloughed them off; so Satan followed after him, and he became of those '
    'gone astray.',
    'سُورَةُ الأَعْرَاف · 7:175')
b += B.sharh(
    p('<em>«“فَأَتْبَعَهُ الشَّيْطَان” means: <strong>the devil overtook him and '
      'the devil destroyed him</strong>, until he '
      '<strong>supplicated against Mūsā and his people</strong>; and this is of '
      'apostasy from Islām — we seek refuge with Allah — '
      '<strong>because he supplicated against the people of truth that they be '
      'forsaken, and that the people of shirk and falsehood be given '
      'victory</strong>.»</em>') +
    box('<p style="margin:0;font-size:.93rem"><strong>And asked about the '
        'soundness of the story of Balʿam itself, he said:</strong> '
        '<em>«<strong>مِنْ أَخْبَارِ بَنِي إِسْرَائِيل، لَكِنَّ القُرْآنَ '
        'كَافٍ</strong>»</em> — <em>“of the reports of the Children of Isrāʾīl; '
        'but the Qurʾān is sufficient.”</em></p>'
        '<p style="margin:.5rem 0 0;font-size:.92rem"><em>The same discipline as '
        'the Hārūt and Mārūt stories in the last lesson: '
        '<strong>the lesson is taken from the verse, and the narrative is '
        'left where it belongs.</strong></em></p>'))
b += B.prose(
    '<strong>And notice what the verse is being cited for, because it is the '
    'clause’s deepest point.</strong> <em>The man in it is not a disbeliever who '
    'stayed one. He is a man who <strong>was given the signs</strong> and '
    'sloughed them off — and the act by which he did it was '
    '<strong>a supplication</strong>: that the people of truth be defeated and '
    'the people of shirk be given victory.</em> '
    '<strong>مُظَاهَرَة with no weapon in it at all.</strong>')

# ---------------------------------------------------------------- zahirah
b += B.heading('التَّوَلِّي مِنَ المَسَائِلِ الظَّاهِرَة', 'Where Ignorance Is No Excuse')
b += B.sharh(
    qa('One who does something of the nullifiers of Islām <strong>while '
       'ignorant</strong> of them — what is the ruling on his act? And what is '
       'the standard of ignorance in this question?',
       '<em>«Whoever is <strong>among the Muslims</strong> — no leniency is '
       'shown him in this; meaning: the one who is among the Muslims '
       '<strong>knows these nullifiers</strong> and that they are contrary to '
       'Islām. As for <strong>one who is among the mushrikīn, or in lands where '
       'the matter may be hidden from him</strong> — '
       '<strong>he is warned</strong>; and if he then <strong>persists</strong> '
       'upon that, he disbelieves; and <strong>if he repents, then praise be to '
       'Allah</strong>.»</em>') +
    p('<strong>And then the category this clause belongs to:</strong> '
      '<em>«as for <strong>the manifest matters</strong>, they do not need '
      'clarification — as his associating partners with Allah, or his holding '
      'that the ruling of Zayd and ʿAmr is better than the ruling of Allah and '
      'His Messenger, or his reviling Allah and His Messenger, or the like of '
      'that, <strong>or his giving the disbelievers victory over the Muslims and '
      'aiding them against a Muslim</strong> — '
      '<strong>هَذِهِ أُمُورٌ ظَاهِرٌ كُفْرُهَا</strong>.»</em>') +
    p('<em>«لَكِنْ مَا قَدْ يَخْفَى يُسْأَلُ أَهْلُ العِلْم؛ وَإِذَا '
      'نُبِّهَ عَلَى ذَلِكَ وَتَابَ تَابَ اللهُ عَلَيْه»</em> — '
      '<strong>but what may be obscure: the people of knowledge are asked; and '
      'if he is alerted to it and repents, Allah accepts his '
      'repentance.</strong>'))
b += B.sharh(
    box('<p style="margin:0;font-size:.93rem"><strong>Ibn Taymiyyah’s footnote '
        'here sets the frame exactly</strong>, and it cuts both ways: '
        '<em>«and if it is in <strong>the hidden statements</strong>, it may be '
        'said that he is <strong>mistaken, astray — the proof that makes its '
        'holder a disbeliever has not been established against him</strong>; '
        'but that occurs among groups of them <strong>in the manifest matters, '
        'which the elite and the common people of the Muslims know to be of the '
        'religion of the Muslims</strong> — rather the Jews and the Christians '
        'and the mushrikīn know that Muḥammad ﷺ was sent with them and declared '
        'a disbeliever whoever opposed them: such as his command to worship '
        'Allah alone with no partner, and his prohibition of worshipping anyone '
        'besides Allah… <strong>and such as enmity to the Jews and the '
        'Christians and the mushrikīn</strong>, and such as the prohibition of '
        'the obscenities and ribā and wine and gambling.»</em></p>'
        '<p style="margin:.5rem 0 0;font-size:.92rem"><em>So the excuse of '
        'ignorance is real and has a field — «the hidden statements» — and this '
        'clause, in its core shape, is not in that field.</em></p>'))

b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><strong>Part 2 takes '
        'printed folios ٢٠٥–٢٢٢</strong>, opening at the book’s own heading '
        '<strong>الاسْتِعَانَةُ بِالكُفَّارِ عَلَى الكُفَّار</strong> — where '
        'Ibn Bāz distinguishes seeking help against another disbeliever from '
        'giving disbelievers victory over Muslims, <em>and applies it to a named '
        'contemporary case in his own words.</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))

b += B.vocab([
    ('مُظَاهَرَة', 'muẓāharah', 'backing, lending support',
     'The matn’s own word, and it is transitive in the clause: مُظَاهَرَةُ '
     'المُشْرِكِينَ **عَلَى المُسْلِمِين** — backing them AGAINST the Muslims.'),
    ('التَّوَلِّي', 'al-tawallī', 'siding with, taking as a party',
     'Ibn Bāz: «التَّوَلِّي هُوَ النَّصْر… وَأَصْلُهُ مَحَبَّةُ القُلُوب»; and '
     'its shape is «نَصْرُهُمْ عَلَى المُسْلِمِين». **كُفْرٌ وَرِدَّة.**'),
    ('المُوَالَاة', 'al-muwālāh', 'allying, befriending',
     'The lesser category — a gift, cheerfulness, greeting first, friendship for '
     'a worldly cause. «المُوَالَاةُ مَعْصِيَة، وَالتَّوَلِّي كُفْر»; and '
     '«المُوَالَاةُ قِسْمَانِ: مَعْصِيَةٌ وَمُكَفِّرَة».'),
    ('التَّوَلِّي العَامّ', 'al-tawallī al-ʿāmm', 'the general siding-with',
     '«هَذَا أَشَرُّهَا» — the worst of them. And the verse is read '
     '«عَلَى حَسَبِ التَّوْلِيَة», by the degree, not as a flat equation.'),
    ('تَشَبُّه', 'tashabbuh', 'imitation',
     'What he called raising the banner beside the cross, when asked if it was '
     'tawallī: «كَلَّا، هَذَا نَوْعُ تَشَبُّه». Forbidden — and a different '
     'chapter.'),
    ('البِرّ', 'al-birr', 'kindness, dutiful good treatment',
     'What al-Mumtaḥanah 60:8 permits toward those who did not fight us. '
     'And the footnote’s line: «فَالبِرُّ شَيْء، وَالمَحَبَّةُ شَيْءٌ '
     'آخَر».'),
    ('المُؤَلَّفَةُ قُلُوبُهُمْ', 'al-muʾallafah qulūbuhum',
     'those whose hearts are to be won',
     'A share Allah legislated in the zakāh — Ibn Bāz’s proof that kindness in '
     'the treaty state may itself be «سَبِيلًا إِلَى الهِدَايَة». '
     'Ṣafwān ibn Umayyah is the case.'),
    ('الرُّكُون', 'al-rukūn', 'inclining, leaning upon',
     'Hūd 11:113. Two kinds: to shirk and its people → ridda if he aids them '
     'against Muslims; to the oppressors and sinners → «كُلُّهُ دَاخِلٌ فِي '
     'المَعْصِيَة».'),
    ('المَسَائِلُ الظَّاهِرَة', 'al-masāʾil al-ẓāhirah',
     'the manifest matters',
     'Where ignorance is not an excuse for one living among Muslims. Against '
     'Ibn Taymiyyah’s «المَقَالَاتُ الخَفِيَّة», where the proof may not have '
     'been established.'),
])

b += B.mcq('nq-l14-mcq', [
    ('What are the matn’s two words for the act, and what are they directed '
     'against?',
     ['مُوَالَاة and مَحَبَّة, directed at their religion',
      'مُظَاهَرَة and مُعَاوَنَة — backing and aiding — «عَلَى المُسْلِمِين», '
      'against the Muslims',
      'رُكُون and تَشَبُّه, directed at their customs',
      'سَبّ and اسْتِهْزَاء'], 1),
    ('State the أَصْل of this clause in Ibn Bāz’s own terms.',
     ['Avoiding their lands',
      'Disownment of the mushrikīn and of their religion, and disbelief in that; '
      'and allegiance to the people of tawḥīd, love of them and love of their '
      'religion — «هَذَا أَصْلٌ أَصِيل»',
      'Fighting them wherever they are found',
      'Refusing their trade'], 1),
    ('Which verse does he ground it in, and what is notable about its order?',
     ['al-Māʾidah 5:51; the prohibition precedes the reason',
      'al-Baqarah 2:256 — the disbelief in the ṭāghūt comes FIRST, then the '
      'belief in Allah; «فَلَا بُدَّ مِنَ الكُفْرِ بِالطَّاغُوت، وَالإِيمَانِ '
      'بِالله»',
      'al-Mumtaḥanah 60:4; the barāʾah is stated last',
      'al-Nisāʾ 4:71; the command precedes the warning'], 1),
    ('What does he say about love of disbelief and being pleased with it?',
     ['It is a sin only',
      'It is an independent disbelief — «وَإِنْ لَمْ يَفْعَلْهُ الإِنْسَان», '
      'even if the person does not do it',
      'It is excused if concealed',
      'It is fisq'], 1),
    ('How many divisions does Ibn Bāz name in this question?',
     ['Two', 'Three', 'Four', 'He does not divide it'], 1),
    ('What is the FIRST division, and its ruling?',
     ['Trade with them — forbidden',
      'Being pleased with disbelief and not denouncing or disowning it, or '
      'aiding the disbelievers against the Muslims — رِدَّةٌ عَنِ الإِسْلَام',
      'Imitating them — a sin',
      'Seeking their help — permitted'], 1),
    ('The SECOND division?',
     ['Loving their religion — ridda',
      'Friendship or love for a WORLDLY matter, not for love of their religion '
      'and not for giving them victory over Muslims — مُنْكَرٌ وَمِنْ '
      'وَسَائِلِ الشِّرْك, and NOT ridda',
      'Fighting alongside them — ridda',
      'Visiting their lands — permitted'], 1),
    ('The THIRD division?',
     ['Imitation of their dress — forbidden',
      'Seeking help from them against the enemies, against other disbelievers, '
      'or in the interests of the Muslims, without allegiance — جَائِز',
      'Marrying from them — permitted',
      'Taking their wealth — forbidden'], 1),
    ('How does he establish the third division?',
     ['By analogy with trade',
      'From the Prophet’s ﷺ own life and his Companions’ — the Jews of Khaybar, '
      'al-Muṭʿim ibn ʿAdī, Abū Ṭālib, Abū Bakr with Ibn al-Dughunnah, and '
      'ʿAbdullāh ibn Urayqiṭ al-Dīlī as guide to Madīnah',
      'By the practice of later caliphs',
      'By the absence of a prohibition'], 1),
    ('How is the Khaybar case qualified in the footnote?',
     ['It is left as a general licence',
      'It was «for a temporary period… for the severe need» — «and it is not '
      'permissible to expand and be lax in these matters»',
      'It is said to be abrogated',
      'It is restricted to agriculture forever'], 1),
    ('And how is ʿUmar’s expulsion of them explained, against Abū Bakr’s not '
     'expelling them?',
     ['That ʿUmar was stricter',
      'ʿUmar acted on events they brought about and in execution of the '
      'Prophet’s ﷺ command, and he had the leisure for it and a long rule — '
      'while al-Ṣiddīq’s rule was short and occupied with the people of apostasy',
      'That Abū Bakr was unaware of the command',
      'That the command came after Abū Bakr'], 1),
    ('Give Ibn Bāz’s six-word distinction.',
     ['«الكُفْرُ كُفْرَان: أَكْبَرُ وَأَصْغَر»',
      '«المُوَالَاةُ مَعْصِيَة، وَالتَّوَلِّي كُفْر»',
      '«الوَلَاءُ وَالبَرَاءُ أَصْلَان»',
      '«البِرُّ شَيْءٌ وَالمَحَبَّةُ شَيْءٌ آخَر»'], 1),
    ('And how does he define التَّوَلِّي?',
     ['Loving them inwardly',
      '«مُسَاعَدَتُهُمْ عَلَى المُسْلِمِين» — aiding them against the Muslims; '
      'and asked for the standard: «التَّوَلِّي هُوَ النَّصْر… وَأَصْلُهُ '
      'مَحَبَّةُ القُلُوب»',
      'Living among them',
      'Preferring their laws'], 1),
    ('Which of these did he name as examples of المُوَالَاة — a sin, not '
     'apostasy?',
     ['Selling them weapons to fight Muslims',
      'Their love, presenting a gift, cheerfulness in their faces, initiating '
      'the greeting — and attending their festivals, laughing with them',
      'Fighting in their ranks',
      'Supplicating for their victory'], 1),
    ('Asked whether raising the banner of tawḥīd beside the banner of the cross '
     'is تَوَلِّي, he said:',
     ['«Yes, it is the clearest form of it»',
      '«كَلَّا — this is a kind of تَشَبُّه», because tawallī is giving them '
      'victory and backing them against the Muslims',
      '«It requires research»',
      '«It is permitted»'], 1),
    ('And on cheering a disbelieving sportsman?',
     ['That it is disbelief',
      'That the duty is not to cheer them and to confine it to the Muslims — '
      '«but this is not of the disbelief-entailing muwālāh; rather it is a kind '
      'of muwālāh, a sin»',
      'That it is permitted without restriction',
      'That it depends on the sport'], 1),
    ('«المُوَالَاةُ قِسْمَانِ:…»',
     ['«…ظَاهِرَةٌ وَبَاطِنَة»',
      '«…مَعْصِيَةٌ وَمُكَفِّرَة»',
      '«…قَلْبِيَّةٌ وَعَمَلِيَّة»',
      '«…فِي الحَرْبِ وَفِي السِّلْم»'], 1),
    ('Why does he insist on keeping the lesser category lesser — what reason '
     'does he give for warning against it at all?',
     ['Because it is harmless',
      '«حَتَّى لَا تَقَعَ الكَارِثَة» — so that the disaster does not occur: the '
      'sin is treated seriously because it is the ROAD to the nullifier, not '
      'because it is the nullifier',
      'Because the scholars differ',
      'Because it affects reputation'], 1),
    ('What does he say the Muslim must make known to the disbeliever he deals '
     'with?',
     ['Nothing; it is a matter of the heart',
      'That he is an enemy to him and he an enemy to him, and that he is free of '
      'him and he is free of him — «وَأَنْ يَعْلَمَ ذَلِكَ مِنْك»',
      'That he hopes for his conversion only',
      'That trade is permitted but friendship is not'], 1),
    ('What is التَّوَلِّي العَامّ?',
     ['Allegiance in a particular matter',
      'The general siding-with — «هَذَا أَشَرُّهَا», the worst of them: giving '
      'them victory over the Muslims and backing and aiding them against the '
      'Muslims',
      'Imitation in dress and custom',
      'Love of their religion only'], 1),
    ('Asked whether «وَمَنْ يَتَوَلَّهُمْ مِنْكُمْ فَإِنَّهُ مِنْهُمْ» '
     'necessitates disbelief for anyone who allies with them, he answered:',
     ['«Yes, without distinction»',
      '«عَلَى حَسَبِ التَّوْلِيَة» — according to the degree of the allying; '
      '«so if he gave them victory and backed them against the Muslims, he was '
      'like them»',
      '«The verse is abrogated»',
      '«Only for those who fight»'], 1),
    ('Which earlier nullifiers use the same move as «عَلَى حَسَبِ '
     'التَّوْلِيَة»?',
     ['None of them',
      'The seventh («فِيهِ التَّفْصِيل») and the sixth («الفَرْدُ '
      'وَالفَرْدَانِ فِسْق»)',
      'The first and the second',
      'The fifth alone'], 1),
    ('Selling weapons to the disbelievers so they may fight the Muslims with '
     'them?',
     ['Forbidden, and not apostasy',
      'Apostasy — «this means تَوَلٍّ لِلْكُفَّار»',
      'Permitted in the treaty state',
      'A matter of ijtihād'], 1),
    ('And selling the same weapons to highway robbers or rebels?',
     ['Also apostasy',
      'Aiding upon acts of disobedience — «فَيَكُونُ مُحَرَّمًا وَمُنْكَرًا» — '
      'forbidden and an abomination, not apostasy',
      'Permitted',
      'Fisq only'], 1),
    ('So what does the ruling on the sale turn on?',
     ['The price',
      'WHO the weapon is to be used against',
      'The seller’s intention alone',
      'Whether war has been declared'], 1),
    ('In the state of WAR, what may the enemy be aided with?',
     ['Food and medicine only',
      'Nothing at all — «لَا سِلَاحٌ وَلَا مَالٌ وَلَا طَعَامٌ وَلَا غَيْرُ '
      'ذَلِك»; and such giving «becomes disbelief and apostasy from Islām»',
      'Money but not weapons',
      'Whatever the ruler permits'], 1),
    ('And in the state of treaty and reconciliation?',
     ['The same prohibition applies',
      'There is no objection to their being given — the relative gives his '
      'relative, the Muslim gives the poor, the one in authority gives what he '
      'sees benefit in, and gifts may be exchanged — «within the bounds of the '
      'Muḥammadan Sharīʿah»',
      'Only kinship is excepted',
      'Only the ruler may give'], 1),
    ('Which two groups does he name specifically as permitted recipients in the '
     'treaty state?',
     ['Their scholars and their rulers',
      'Their poor and their disabled — «كَفَقِيرِهِمْ وَزَمِنِهِم» — along with '
      'the ties of kinship',
      'Their traders and their envoys',
      'Their children only'], 1),
    ('Which verse covers kindness to those who did not fight us?',
     ['al-Māʾidah 5:51',
      'al-Mumtaḥanah 60:8 — «that you should deal kindly and justly with them; '
      'indeed Allah loves the just»',
      'al-Baqarah 2:256',
      'al-Anfāl 8:60'], 1),
    ('Which case does he bring for it?',
     ['The treaty of al-Ḥudaybiyah itself',
      'Asmāʾ bint Abī Bakr — whose mother came to Madīnah during the truce '
      'seeking assistance, and the Prophet ﷺ gave the fatwā that she should '
      'maintain the tie with her',
      'Ṣafwān ibn Umayyah',
      'The Jews of Khaybar'], 1),
    ('What reason does he give that reframes the whole category of kindness in '
     'the treaty state?',
     ['That it buys peace',
      'That it «may be a path to GUIDANCE» — and for this Allah legislated a '
      'share in the zakāh for المُؤَلَّفَةُ قُلُوبُهُمْ',
      'That it is required by the treaty',
      'That it prevents retaliation'], 1),
    ('Ṣafwān ibn Umayyah’s own sentence afterwards?',
     ['«I accepted Islām for fear of the sword»',
      '«There was no household more hateful to me than the Messenger of Allah’s '
      'ﷺ; and he kept on giving me and giving me until he became the most '
      'beloved of people to me»',
      '«I was given and I was not guided»',
      '«I hoped for the wealth and found the religion lacking»'], 1),
    ('Some use 60:8 to permit LOVING the peaceful disbeliever. The footnote’s '
     'answer?',
     ['That it is correct',
      '«وَهَذَا خَطَأ» — because kindness toward a disbeliever does not entail '
      'love of him: «فَالبِرُّ شَيْء، وَالمَحَبَّةُ شَيْءٌ آخَر»',
      'That the verse is abrogated',
      'That it applies to relatives only'], 1),
    ('What illustration does it give for birr without love?',
     ['A neighbour one dislikes',
      'A person may be kind to an ANIMAL, or to one he hopes something from or '
      'fears — and love is not entailed by that',
      'A debtor',
      'A guest'], 1),
    ('How is «إِنَّكَ لَا تَهْدِي مَنْ أَحْبَبْتَ» answered?',
     ['It is accepted as proof of love',
      'It is read as «you loved his GUIDANCE, not his person» — the occasion of '
      'revelation shows it; and even granting the other reading, the verse is '
      'Makkan about Abū Ṭālib, and al-Mujādilah and al-Mumtaḥanah came later in '
      'Madīnah',
      'It is said to be weak',
      'It is restricted to prophets'], 1),
    ('Some claimed Ibrāhīm disowned his people only AFTER they hated and fought '
     'him. The refutation?',
     ['That the verse is Madinan',
      '«وَهَذَا إِفْكٌ مُبِين» — from the verse’s own ending: he made the limit '
      'at which the enmity ceases their BELIEVING in Allah’s tawḥīd, «and he did '
      'not say: until you leave off hating me»',
      'That the story is isrāʾīlī',
      'That it concerns Lūṭ, not Ibrāhīm'], 1),
    ('What does that claim entail about Ibrāhīm, in the footnote’s words?',
     ['Nothing objectionable',
      'A belittling of that noble prophet — as though he hated them in his own '
      'defence, and did not hate them for violating Allah’s sanctities and '
      'associating partners with Him. «سَاءَ مَا يَحْكُمُون»',
      'That he was ignorant of tawḥīd',
      'That he recanted'], 1),
    ('The argument from marrying a kitābiyyah is answered how?',
     ['By forbidding such marriage',
      'Either it is a matter a TEXT has come with, so the ruling is confined to '
      'it; or the love of a disbelieving wife is a love of APPETITE, like love '
      'of a disbeliever’s food — not an essential or religious love',
      'By saying the marriage is for procreation only',
      'By restricting it to the dhimmah'], 1),
    ('And what binding consequence does the footnote press on them?',
     ['That they must forbid all marriage',
      'That on their reasoning they would have to permit loving the WARRING '
      'disbelievers too — since Allah permitted us the food and women of the '
      'People of the Book who are at war as well',
      'That they must permit loving idolaters',
      'That they must reject the zakāh share'], 1),
    ('Name the three moves the footnote attributes to ahl al-bidaʿ.',
     ['Innovation, exaggeration and neglect',
      'Objecting to the universals by the particulars; striking the certainties '
      'with the probabilities; and overturning the consensuses by what is of the '
      'fallen among the possibilities',
      'Takfīr, tafsīq and tabdīʿ',
      'Taqlīd, tajahhul and taʾwīl'], 1),
    ('What two things are obligatory in war AND peace together?',
     ['Jihād and hijrah',
      'الإِعْدَاد — preparation — and الحَذَر — wariness: «فَإِنَّ الأَعْدَاءَ '
      'لَا يُؤْتَمَنُونَ أَبَدًا»',
      'Daʿwah and patience',
      'Treaty and tribute'], 1),
    ('And what does he say in the very next breath that the enmity does NOT '
     'prevent?',
     ['Trade with them',
      'Calling them and being eager for their guidance — «so the callers and '
      'those who direct to good are sent to them; perhaps Allah will bring them '
      'out of the darknesses into the light»',
      'Treaties with them',
      'Learning their languages'], 1),
    ('Which verse does he give as the promise that makes the wariness bearable?',
     ['«وَأَعِدُّوا لَهُمْ مَا اسْتَطَعْتُم»',
      '«وَإِنْ تَصْبِرُوا وَتَتَّقُوا لَا يَضُرُّكُمْ كَيْدُهُمْ شَيْئًا»',
      '«خُذُوا حِذْرَكُم»',
      '«إِنَّ اللهَ يُحِبُّ المُقْسِطِين»'], 1),
    ('الرُّكُون in Hūd 11:113 — the two kinds?',
     ['Public and private',
      'Inclining to shirk and its people → ridda if he aids them against the '
      'Muslims; and inclining to the OPPRESSORS, aiding the oppressor, thief or '
      'sinner → «كُلُّهُ دَاخِلٌ فِي المَعْصِيَة»',
      'Of the heart and of the limbs',
      'In war and in peace'], 1),
    ('In al-Aʿrāf 7:175, by what act did the man slough off the signs?',
     ['By selling his knowledge',
      'By a SUPPLICATION — he supplicated against Mūsā and his people, that the '
      'people of truth be forsaken and the people of shirk be given victory',
      'By fighting alongside Pharaoh',
      'By concealing the revelation'], 1),
    ('Why is that the clause’s deepest point?',
     ['Because it concerns a prophet',
      'Because it is مُظَاهَرَة with no weapon in it at all — and by a man who '
      'had BEEN GIVEN the signs',
      'Because it proves the ruling on magic',
      'Because it names the man'], 1),
    ('What did Ibn Bāz say about the soundness of the story of Balʿam itself?',
     ['That it is authentic',
      '«مِنْ أَخْبَارِ بَنِي إِسْرَائِيل، لَكِنَّ القُرْآنَ كَافٍ» — of the '
      'reports of the Children of Isrāʾīl, but the Qurʾān is sufficient',
      'That it is fabricated',
      'That it is mutawātir'], 1),
    ('When is ignorance of this nullifier not an excuse?',
     ['Never; ignorance always excuses',
      'For one who is AMONG THE MUSLIMS — «no leniency is shown him in this», '
      'because such a one knows these nullifiers',
      'Only for scholars',
      'Only after a judge rules'], 1),
    ('And for one among the mushrikīn, or in lands where the matter may be '
     'hidden?',
     ['He is excused permanently',
      'He is WARNED; and if he then persists he disbelieves — «and if he '
      'repents, then praise be to Allah»',
      'He is ruled a disbeliever at once',
      'He must emigrate'], 1),
    ('Which category does giving the disbelievers victory over the Muslims fall '
     'into?',
     ['The hidden statements, where the proof may not be established',
      'The MANIFEST matters — «هَذِهِ أُمُورٌ ظَاهِرٌ كُفْرُهَا» — which do not '
      'need clarification',
      'A place of ijtihād',
      'A matter for the ruler alone'], 1),
    ('What does Ibn Taymiyyah’s footnote establish about the excuse of '
     'ignorance?',
     ['That it does not exist',
      'That it is real and has a field — «the HIDDEN statements», where it may '
      'be said the proof that makes its holder a disbeliever has not been '
      'established — but that the manifest matters are not in that field',
      'That it applies only to new Muslims',
      'That only a judge may apply it'], 1),
])

b += B.tf('nq-l14-tf', [
    ('المُوَالَاةُ وَالتَّوَلِّي شَيْءٌ وَاحِدٌ عِنْدَ ابْنِ بَاز.',
     'Muwālāh and tawallī are one and the same for Ibn Bāz.', False),
    ('التَّوَلِّي هُوَ نَصْرُهُمْ عَلَى المُسْلِمِينَ وَهُوَ رِدَّة.',
     'Tawallī is giving them victory over the Muslims, and it is apostasy.',
     True),
    ('إِهْدَاءُ شَيْءٍ لِلْكَافِرِ أَوِ البَشَاشَةُ فِي وَجْهِهِ رِدَّةٌ '
     'عَنِ الإِسْلَام.',
     'Presenting a gift to a disbeliever, or cheerfulness in his face, is '
     'apostasy from Islām.', False),
    ('رَفْعُ عَلَمِ التَّوْحِيدِ بِجَانِبِ عَلَمِ الصَّلِيبِ تَوَلٍّ '
     'عِنْدَ ابْنِ بَاز.',
     'Raising the banner of tawḥīd beside the banner of the cross is tawallī '
     'for Ibn Bāz.', False),
    ('لَا يَجُوزُ فِي حَالِ الحَرْبِ إِعَانَتُهُمْ بِطَعَامٍ وَلَا '
     'مَال.',
     'In the state of war it is not permissible to aid them with food or money.',
     True),
    ('البِرُّ بِالكَافِرِ المُسَالِمِ يَلْزَمُ مِنْهُ مَحَبَّتُه.',
     'Kindness to a peaceful disbeliever entails loving him.', False),
    ('البَغْضَاءُ بَيْنَنَا وَبَيْنَهُمْ تَمْنَعُ مِنْ دَعْوَتِهِمْ.',
     'The enmity between us and them prevents calling them to Islām.', False),
])

b += B.memorize(
    'المُوَالَاةُ غَيْرُ التَّوَلِّي؛ المُوَالَاةُ مَعْصِيَة، '
    'وَالتَّوَلِّي كُفْر',
    'Ibn Bāz. <strong>Six words, and the whole eighth nullifier turns on '
    'them.</strong> <em>And he meant them: asked about a banner raised beside a '
    'cross he said «كَلَّا، هَذَا نَوْعُ تَشَبُّه»; asked about cheering a '
    'disbelieving sportsman, «لَيْسَ هَذَا مِنَ المُوَالَاةِ المُكَفِّرَة؛ '
    'لَكِنَّهُ نَوْعُ مُوَالَاة، مَعْصِيَة».</em> '
    '<strong>The nullifier has one shape — %s — and he will not let anything '
    'else wear it.</strong> <em>And keep beside it the reason he nevertheless '
    'warns hard against the lesser thing: «حَتَّى لَا تَقَعَ الكَارِثَة» — so '
    'that the disaster does not occur. The sin is the road; it is not the '
    'destination.</em>' % ('«' + ar('نَصْرُهُمْ عَلَى المُسْلِمِين') + '»'))

b += B.nav('nq-l13-al-nushrah-wa-al-ilaj.html',
           'النَّاقِضُ السَّابِع · part 3',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l14')

B.write('nq-l14-al-muwalah-wa-al-tawalli.html',
        'النَّاقِضُ الثَّامِن · المُوَالَاةُ وَالتَّوَلِّي',
        'The Eighth Nullifier, Part 1 — Allying and Siding-With',
        'The eighth nullifier, from the words of Shaykh Ibn Bāz: the foundation '
        'of barāʾah and walāʾ on al-Baqarah 2:256; the three divisions he names, '
        'with the third — seeking help in the Muslims’ interests — established '
        'from the Prophet’s ﷺ own life; and the distinction the whole clause '
        'turns on, «muwālāh is a sin and tawallī is disbelief», with his two '
        'refusals to inflate it — the banner beside the cross is tashabbuh, and '
        'cheering a disbelieving sportsman is a sin and not the '
        'disbelief-entailing kind; war against treaty in what may be given, with '
        'al-Mumtaḥanah 60:8, Asmāʾ bint Abī Bakr and Ṣafwān ibn Umayyah; the '
        'footnote that kindness does not entail love, and its three answers; '
        'preparation and wariness as standing obligations that do not block '
        'daʿwah; al-rukūn in its two kinds; and when ignorance excuses and when '
        'it does not.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ الرَّابِعَ عَشَر', '6', b)
print('wrote nq-l14-al-muwalah-wa-al-tawalli.html')
