# -*- coding: utf-8 -*-
"""Ḥadīth 24 — «يَا عِبَادِي إِنِّي حَرَّمْتُ الظُّلْمَ عَلَى نَفْسِي…». Abū
Dharr al-Ghifārī, Ṣaḥīḥ Muslim — the great qudsī ḥadīth. Sharḥ of Ibn
ʿUthaymīn, printed folios 258–277 (markers 259–278, offset −1).

A ḥadīth qudsī in which Allah addresses His servants: He forbade injustice upon
Himself and between us; all are astray, hungry and naked but for Him; He
forgives all sins for those who seek it; creation cannot harm or benefit Him;
all their obedience adds nothing to His dominion and all their asking
diminishes nothing of His treasures; and in the end, "they are only your deeds
that I count for you and repay you in full."

Rule 8: the ḥadīth is in Ṣaḥīḥ Muslim (Kitāb al-Birr wa-l-Ṣilah), so ṣaḥīḥ; the
supporting «مَنْ قَتَلَ مُعَاهَدًا…» and «أَلَا وَإِنَّ فِي الجَسَدِ مُضْغَةً…»
are in al-Bukhārī — named attributions, no grading invented.
"""
import io, os, importlib.util

spec = importlib.util.spec_from_file_location('hb', os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '_hadbuild.py'))
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)


def p(x):
    return '<p style="font-size:.92rem;color:var(--ink-mid);line-height:1.9;' \
           'margin:0 0 .85rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


def box(inner, wash='var(--brand-wash)', edge='var(--brand)'):
    return ('<div style="background:%s;border-right:4px solid %s;'
            'border-radius:var(--radius-sm);padding:var(--space-lg);'
            'margin:0 0 var(--space-md)">%s</div>' % (wash, edge, inner))


def row(k, v):
    return ('<tr><td style="padding:.62rem .8rem;border:1px solid var(--line);'
            'white-space:nowrap;vertical-align:top"><strong>%s</strong></td>'
            '<td style="padding:.62rem .8rem;border:1px solid var(--line)">%s</td></tr>'
            % (k, v))


def table(rows, fs='.91rem'):
    return ('<div style="overflow-x:auto"><table style="width:100%%;'
            'border-collapse:collapse;font-size:%s;margin:0 0 var(--space-md)">%s'
            '</table></div>' % (fs, ''.join(rows)))


b = B.objectives([
    'Say who narrated this ḥadīth, where it is reported, and what a '
    '<strong>ḥadīth qudsī</strong> is — and how it differs from the Qurʾān.',
    'Explain «%s» — that Allah forbade injustice upon Himself though able to '
    'do it, and that a negation affirms the opposite perfection.'
    % ar('حَرَّمْتُ الظُّلْمَ عَلَى نَفْسِي'),
    'Explain the servant’s need laid bare — all are <strong>astray, hungry and '
    'naked</strong> but for Allah — and the two kinds of guidance.',
    'State how Allah forgives all sins for the one who seeks it, and the three '
    'categories sins fall into.',
    'Draw out the perfection of Allah’s <strong>self-sufficiency and '
    'dominion</strong> from the “law anna” passages, and the meaning of «%s».'
    % ar('إِنَّمَا هِيَ أَعْمَالُكُم'),
])

b += B.provenance(258, 277)

b += B.hadith_block(
    'عَنْ أَبِي ذَرٍّ الغِفَارِيِّ رَضِيَ اللهُ عَنْهُ عَنِ النَّبِيِّ ﷺ '
    'فِيمَا يَرْوِيهِ عَنْ رَبِّهِ عَزَّ وَجَلَّ أَنَّهُ قَالَ: «يَا عِبَادِي، '
    'إِنِّي حَرَّمْتُ الظُّلْمَ عَلَى نَفْسِي وَجَعَلْتُهُ بَيْنَكُمْ '
    'مُحَرَّمًا فَلَا تَظَالَمُوا. يَا عِبَادِي، كُلُّكُمْ ضَالٌّ إِلَّا مَنْ '
    'هَدَيْتُهُ فَاسْتَهْدُونِي أَهْدِكُمْ. يَا عِبَادِي، كُلُّكُمْ جَائِعٌ '
    'إِلَّا مَنْ أَطْعَمْتُهُ فَاسْتَطْعِمُونِي أُطْعِمْكُمْ. يَا عِبَادِي، '
    'كُلُّكُمْ عَارٍ إِلَّا مَنْ كَسَوْتُهُ فَاسْتَكْسُونِي أَكْسُكُمْ. يَا '
    'عِبَادِي، إِنَّكُمْ تُخْطِئُونَ بِاللَّيْلِ وَالنَّهَارِ وَأَنَا '
    'أَغْفِرُ الذُّنُوبَ جَمِيعًا فَاسْتَغْفِرُونِي أَغْفِرْ لَكُمْ. يَا '
    'عِبَادِي، إِنَّكُمْ لَنْ تَبْلُغُوا ضَرِّي فَتَضُرُّونِي وَلَنْ '
    'تَبْلُغُوا نَفْعِي فَتَنْفَعُونِي. يَا عِبَادِي، لَوْ أَنَّ أَوَّلَكُمْ '
    'وَآخِرَكُمْ وَإِنْسَكُمْ وَجِنَّكُمْ كَانُوا عَلَى أَتْقَى قَلْبِ '
    'رَجُلٍ وَاحِدٍ مِنْكُمْ مَا زَادَ ذَلِكَ فِي مُلْكِي شَيْئًا. يَا '
    'عِبَادِي، لَوْ أَنَّ أَوَّلَكُمْ وَآخِرَكُمْ وَإِنْسَكُمْ وَجِنَّكُمْ '
    'كَانُوا عَلَى أَفْجَرِ قَلْبِ رَجُلٍ وَاحِدٍ مِنْكُمْ مَا نَقَصَ '
    'ذَلِكَ مِنْ مُلْكِي شَيْئًا. يَا عِبَادِي، لَوْ أَنَّ أَوَّلَكُمْ '
    'وَآخِرَكُمْ وَإِنْسَكُمْ وَجِنَّكُمْ قَامُوا فِي صَعِيدٍ وَاحِدٍ '
    'فَسَأَلُونِي فَأَعْطَيْتُ كُلَّ وَاحِدٍ مَسْأَلَتَهُ مَا نَقَصَ ذَلِكَ '
    'مِمَّا عِنْدِي إِلَّا كَمَا يَنْقُصُ المِخْيَطُ إِذَا أُدْخِلَ '
    'البَحْرَ. يَا عِبَادِي، إِنَّمَا هِيَ أَعْمَالُكُمْ أُحْصِيهَا لَكُمْ '
    'ثُمَّ أُوَفِّيكُمْ إِيَّاهَا، فَمَنْ وَجَدَ خَيْرًا فَلْيَحْمَدِ '
    'اللهَ، وَمَنْ وَجَدَ غَيْرَ ذَلِكَ فَلَا يَلُومَنَّ إِلَّا '
    'نَفْسَهُ». رَوَاهُ مُسْلِم.',
    'Abū Dharr al-Ghifārī (may Allah be pleased with him) reported that the '
    'Prophet ﷺ said, narrating from his Lord: "O My servants, I have forbidden '
    'injustice for Myself and made it forbidden among you, so do not wrong one '
    'another. O My servants, all of you are astray except those I guide, so '
    'seek guidance of Me and I will guide you. O My servants, all of you are '
    'hungry except those I feed, so ask Me for food and I will feed you. O My '
    'servants, all of you are naked except those I clothe, so ask Me for '
    'clothing and I will clothe you. O My servants, you sin by night and day '
    'and I forgive all sins, so seek My forgiveness and I will forgive you. O '
    'My servants, you will never reach harming Me so as to harm Me, nor '
    'benefiting Me so as to benefit Me. O My servants, were the first of you '
    'and the last, the men of you and the jinn, upon the most pious heart of '
    'any one man among you, that would add nothing to My dominion. O My '
    'servants, were they upon the most wicked heart of any one man among you, '
    'that would subtract nothing from My dominion. O My servants, were the '
    'first of you and the last, the men of you and the jinn, to stand on one '
    'plain and ask of Me, and I gave each one his request, that would diminish '
    'what I have only as a needle diminishes the sea when dipped into it. O My '
    'servants, they are only your deeds that I count for you and then repay you '
    'in full; so whoever finds good, let him praise Allah, and whoever finds '
    'otherwise, let him blame none but himself." Narrated by Muslim.',
    'Narrated by Abū Dharr al-Ghifārī · رَوَاهُ مُسْلِم — Muslim, in his Ṣaḥīḥ '
    '(Kitāb al-Birr wa-l-Ṣilah wa-l-Ādāb, bāb taḥrīm al-ẓulm), so the ḥadīth is '
    'ṣaḥīḥ.')

# ------------------------------------------------------------------ §1
b += B.heading('مَا هُوَ الحَدِيثُ القُدْسِيّ؟', 'What a Ḥadīth Qudsī Is')
b += p('<strong>«%s» — a qudsī ḥadīth</strong> is <em>what the Prophet ﷺ '
       'narrates from his Lord.</em> It is the highest rank of isnād, for the '
       'end of a chain is either the Lord (qudsī), the Prophet ﷺ (marfūʿ), a '
       'Companion (mawqūf), or a Tābiʿī (maqṭūʿ). <strong>It is not the Qurʾān, '
       'by ijmāʿ.</strong>'
       % ar('فِيمَا يَرْوِيهِ عَنْ رَبِّه'))
b += table([
    row('القُرْآن',
        'Worshipped by its recitation — ten ḥasanāt for each letter; a '
        'challenge (taḥaddī) was issued to match it; divinely preserved; '
        'recited in the prayer; touched only in purity.'),
    row('الحَدِيثُ القُدْسِيّ',
        'Not recited as an act of worship by the letter; no taḥaddī; among it '
        'is the ṣaḥīḥ and the ḥasan — even the weak has been ascribed to it; '
        'not a condition of the prayer.'),
])
b += box(
    '<p style="margin:0;font-size:.92rem"><strong>The safest word.</strong> '
    '<em>Scholars disputed whether the wording of a qudsī ḥadīth is from Allah '
    'or only its meaning. The safest is to say simply: <strong>it is what the '
    'Prophet ﷺ narrated from his Lord</strong>, and to leave the delving — for '
    'in it is a kind of takalluf (forced depth).</em></p>')

# ------------------------------------------------------------------ §2
b += B.heading('«حَرَّمْتُ الظُّلْمَ عَلَى نَفْسِي»',
               'Allah Forbade Injustice Upon Himself')
b += p('<strong>“I forbade it upon Myself” means: I withheld it though '
       '<em>able</em> to do it.</strong> <em>We say “though able,” for if it '
       'were impossible for Him there would be no praise in it — one is praised '
       'for leaving a thing only when he could have done it.</em> Could Allah '
       'wrong the creation? In power, yes; but we know by His own word that He '
       'will not — «%s».' % ar('وَلَا يَظْلِمُ رَبُّكَ أَحَدًا'))
b += B.ayah(
    'وَلَا يَظْلِمُ رَبُّكَ أَحَدًا',
    'And your Lord does not wrong anyone.',
    'سُورَةُ الكَهْف · 18:49')
b += p('<strong>And Allah has the right to decree upon Himself what He '
       'wills</strong>, for the ruling belongs to Him — «%s». <em>A thing is '
       'forbidden or made binding upon Allah only when <strong>He</strong> '
       'decreed it so; our intellects neither forbid nor oblige anything upon '
       'Him.</em>' % ar('كَتَبَ عَلَى نَفْسِهِ الرَّحْمَة'))
b += B.ayah(
    'كَتَبَ عَلَىٰ نَفْسِهِ الرَّحْمَةَ',
    'He has decreed upon Himself mercy.',
    'سُورَةُ الأَنْعَام · 6:12')
b += box(
    '<p style="margin:0 0 .5rem;font-size:.92rem"><strong>Two fine points.</strong> '
    '<em>«نَفْس» here means the <strong>Essence</strong> (الذَّات), as in «%s» '
    '— not an attribute among the attributes.</em></p>'
    '<p style="margin:0;font-size:.92rem"><em>And no negation is made of '
    'Allah’s attributes except to affirm the opposite perfection: '
    '<strong>negating injustice affirms perfect justice</strong> '
    '(العَدْل).</em></p>'
    % ar('وَيُحَذِّرُكُمُ اللهُ نَفْسَه'))
b += B.ayah(
    'وَيُحَذِّرُكُمُ اللَّهُ نَفْسَهُ',
    'And Allah warns you of Himself.',
    'سُورَةُ آلِ عِمْرَان · 3:28')
b += p('<strong>«%s» — and He forbade it between us.</strong> <em>Ẓulm turns on '
       'two things: withholding a due owed to another, or burdening another '
       'with what is not owed.</em> Taking the wealth of hostile disbelievers '
       'in war is no ẓulm, for it was made lawful; but the wealth and blood of '
       'the <strong>muʿāhad</strong> — one under a covenant — are protected: '
       '«مَنْ قَتَلَ مُعَاهَدًا لَمْ يَرَحْ رَائِحَةَ الجَنَّةِ» (al-Bukhārī).'
       % ar('وَجَعَلْتُهُ بَيْنَكُمْ مُحَرَّمًا فَلَا تَظَالَمُوا'))

# ------------------------------------------------------------------ §3
b += B.heading('ضَالٌّ، جَائِعٌ، عَارٍ', 'Astray, Hungry, Naked — But for Him')
b += p('<strong>The servant’s utter need, laid bare three times.</strong> '
       '<em>All are astray but for His guidance; all are hungry, for none can '
       'create what bodies live by; all are naked, for we came from our '
       'mothers’ wombs bare.</em> So ask Him — «%s», «%s», «%s» — and you will '
       'find it.'
       % (ar('فَاسْتَهْدُونِي أَهْدِكُم'),
          ar('فَاسْتَطْعِمُونِي أُطْعِمْكُم'),
          ar('فَاسْتَكْسُونِي أَكْسُكُم')))
b += table([
    row('هِدَايَةُ التَّوْفِيق',
        '<em>The guidance of success — to be set firm upon the truth.</em> '
        'This is sought from <strong>Allah alone</strong>; no one can place it '
        'in a heart but Him.'),
    row('هِدَايَةُ الدَّلَالَة',
        '<em>The guidance of showing the way — teaching and directing.</em> '
        'This may be sought from the people of knowledge: “O so-and-so, '
        'instruct me in this.”'),
])
b += p('<strong>And seeking provision means asking Allah and taking the '
       'means.</strong> <em>The sky does not rain gold or bread</em> — «%s». '
       'So turn to Allah for sustenance, then walk out and work for it.'
       % ar('فَانْتَشِرُوا فِي الأَرْضِ وَابْتَغُوا مِنْ فَضْلِ الله'))
b += B.ayah(
    'فَانتَشِرُوا فِي الْأَرْضِ وَابْتَغُوا مِن فَضْلِ اللَّهِ',
    'Then disperse through the land and seek of the bounty of Allah.',
    'سُورَةُ الجُمُعَة · 62:10')

# ------------------------------------------------------------------ §4
b += B.heading('«وَأَنَا أَغْفِرُ الذُّنُوبَ جَمِيعًا»',
               'You Sin — and He Forgives All of It')
b += p('<strong>The son of Adam is much-erring</strong> — «%s» — sinning by '
       'night and day. <em>Yet Allah forgives all sins for the one who '
       '<strong>seeks</strong> His forgiveness</em> — whether by asking in '
       'words (“O Allah, forgive me”) or by the deeds that bring forgiveness.'
       % ar('إِنَّهُ كَانَ ظَلُومًا جَهُولًا'))
b += B.ayah(
    'إِنَّهُ كَانَ ظَلُومًا جَهُولًا',
    'Indeed, he was unjust and ignorant.',
    'سُورَةُ الأَحْزَاب · 33:72')
b += table([
    row('الكُفْر',
        'Needs a specific repentance by ijmāʿ — good deeds do not expiate it.'),
    row('الكَبَائِر',
        'The major sins — they need a particular tawbah; the acts of obedience '
        'do not wipe them out.'),
    row('الصَّغَائِر',
        'The minor sins — expiated by the acts of obedience (prayer to prayer, '
        'Jumuʿah to Jumuʿah, Ramaḍān to Ramaḍān), so long as the major sins are '
        'avoided.'),
])

# ------------------------------------------------------------------ §5
b += B.heading('«لَنْ تَبْلُغُوا ضَرِّي… وَلَنْ تَبْلُغُوا نَفْعِي»',
               'You Cannot Harm Him, Nor Benefit Him')
b += p('<strong>The One addressing them is utterly free of them.</strong> '
       '<em>Creation cannot reach to harm Allah nor to benefit Him, for the '
       'Harmer and the Benefiter is Allah alone — out of the perfection of His '
       'riches beyond His servants.</em> Then come the three “law anna” '
       '(“were it that…”) statements that unveil that wealth:')
b += table([
    row('عَلَى أَتْقَى قَلْب',
        '<em>Were all creation — first and last, men and jinn — upon the most '
        'pious heart of one man, that would <strong>add nothing</strong> to '
        'His dominion.</em>'),
    row('عَلَى أَفْجَرِ قَلْب',
        '<em>Were they upon the most wicked heart of one man, that would '
        '<strong>subtract nothing</strong> from His dominion.</em>'),
    row('قَامُوا فِي صَعِيدٍ وَاحِد',
        '<em>Were they to stand on one plain and ask, and He gave each his '
        'request, it would diminish what He has <strong>only as a needle '
        'diminishes the sea</strong> when dipped in.</em>'),
])
b += box(
    '<p style="margin:0;font-size:.92rem"><strong>And the heart is the seat of '
    'it all.</strong> <em>Taqwā and fujūr are measured by the <strong>heart</strong> '
    '— “the most pious heart,” “the most wicked heart” — and so he ﷺ said: in '
    'the body is a morsel; when it is sound the whole body is sound, and when '
    'it is corrupt the whole body is corrupt — and it is the heart. So tend to '
    'your heart.</em></p>')

# ------------------------------------------------------------------ §6
b += B.heading('«إِنَّمَا هِيَ أَعْمَالُكُم»', 'Only Your Deeds, Repaid in Full')
b += p('<strong>The close of the ḥadīth restricts it all to one thing:</strong> '
       '<em>“they are only your deeds that I count for you and repay you in '
       'full.”</em> Allah counts every deed exactly — nothing is lost — and '
       'repays it: «%s».' % ar('فَمَنْ يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًا يَرَه'))
b += B.ayah(
    'فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًا يَرَهُ ۝ وَمَن يَعْمَلْ مِثْقَالَ '
    'ذَرَّةٍ شَرًّا يَرَهُ',
    'So whoever does an atom’s weight of good will see it, and whoever does an '
    'atom’s weight of evil will see it.',
    'سُورَةُ الزَّلْزَلَة · 99:7–8')
b += box(
    '<p style="margin:0;font-size:.94rem"><strong>So the verdict is just.</strong> '
    '<em>Whoever finds good, let him praise Allah — for enabling the deed and '
    'for rewarding it. And whoever finds otherwise, let him blame <strong>none '
    'but himself</strong></em> — for he was not wronged: the messengers '
    'conveyed, the Qurʾān stands as a proof, and still he left it all. The '
    'blame is on no one but him.</p>',
    wash='var(--gold-pale)', edge='var(--gold-warm)')

# ------------------------------------------------------------------ vocab
b += B.vocab([
    ('الحَدِيثُ القُدْسِيّ', 'al-ḥadīth al-qudsī', 'a sacred (qudsī) ḥadīth',
     'ق-د-س',
     'What the Prophet ﷺ narrates from his Lord — the highest rank of isnād; '
     'it is not the Qurʾān by ijmāʿ, and differs from it in many rulings',
     'عَنِ النَّبِيِّ ﷺ فِيمَا يَرْوِيهِ عَنْ رَبِّه'),
    ('الظُّلْم', 'al-ẓulm', 'injustice, wrongdoing', 'ظ-ل-م',
     'Allah forbade it upon Himself though able to do it, and between His '
     'servants; it turns on withholding a due or burdening with what is not '
     'owed',
     'إِنِّي حَرَّمْتُ الظُّلْمَ عَلَى نَفْسِي'),
    ('ضَالّ', 'ḍāll', 'astray, lost from the way', 'ض-ل-ل',
     'All of creation is astray except whom Allah guides — so guidance is '
     'sought from Him',
     'كُلُّكُمْ ضَالٌّ إِلَّا مَنْ هَدَيْتُه'),
    ('اِسْتَهْدُونِي', 'istahdūnī', 'seek guidance from Me', 'ه-د-ي',
     'The command on which hidāyat al-tawfīq (the guidance of success) turns — '
     'sought from Allah alone',
     'فَاسْتَهْدُونِي أَهْدِكُم'),
    ('صَعِيد', 'ṣaʿīd', 'open level ground', 'ص-ع-د',
     'Were all creation to stand on one ṣaʿīd and ask, and each were given his '
     'request, it would not diminish Allah’s treasures',
     'لَوْ قَامُوا فِي صَعِيدٍ وَاحِدٍ فَسَأَلُونِي'),
    ('المِخْيَط', 'al-mikhyaṭ', 'a needle', 'خ-ي-ط',
     'Giving all creation their every request diminishes what Allah has only '
     'as a needle diminishes the sea when dipped into it',
     'إِلَّا كَمَا يَنْقُصُ المِخْيَطُ إِذَا أُدْخِلَ البَحْر'),
    ('أُوَفِّيكُم', 'uwaffīkum', 'I repay you in full', 'و-ف-ي',
     'Allah counts the deeds exactly and repays them in full — nothing is lost '
     'and no one is wronged',
     'أُحْصِيهَا لَكُمْ ثُمَّ أُوَفِّيكُمْ إِيَّاهَا'),
    ('المُعَاهَد', 'al-muʿāhad', 'one under a covenant/treaty', 'ع-ه-د',
     'His wealth and blood are protected — betraying or killing him is ẓulm: '
     '«لَمْ يَرَحْ رَائِحَةَ الجَنَّةِ»',
     'مَنْ قَتَلَ مُعَاهَدًا لَمْ يَرَحْ رَائِحَةَ الجَنَّة'),
])

# ------------------------------------------------------------------ MCQ
b += B.mcq('hd-h24', [
    ('Who narrated this ḥadīth, and where is it reported?',
     ['Muʿādh ibn Jabal, in al-Tirmidhī',
      'Abū Dharr al-Ghifārī, in Muslim',
      'Abū Hurayrah, in al-Bukhārī',
      'Ibn ʿUmar, in Abū Dāwūd'], 1),
    ('What is a ḥadīth qudsī?',
     ['A verse of the Qurʾān recited in prayer',
      'What the Prophet ﷺ narrates from his Lord — the highest rank of isnād, '
      'but not the Qurʾān',
      'A saying of a Companion',
      'A ḥadīth graded weak by all scholars'], 1),
    ('Which is TRUE of the Qurʾān but NOT of a qudsī ḥadīth?',
     ['It is attributed to Allah',
      'It is worshipped by its recitation (ten ḥasanāt a letter) and a '
      'challenge was issued to match it',
      'It conveys commands and prohibitions',
      'The Prophet ﷺ conveyed it to the ummah'], 1),
    ('Why do we say Allah forbade injustice upon Himself “though able to do '
     'it”?',
     ['Because He is in fact unable to do it',
      'Because one is praised for leaving a thing only when he could have done '
      'it — so His leaving it is a perfection',
      'Because injustice is good for others',
      'Because the angels prevent Him'], 1),
    ('What does «نَفْس» mean in «حَرَّمْتُ الظُّلْمَ عَلَى نَفْسِي»?',
     ['An attribute among His attributes',
      'The Essence (الذَّات) itself, as in «وَيُحَذِّرُكُمُ اللهُ نَفْسَهُ»',
      'The soul of the Prophet ﷺ',
      'A created spirit'], 1),
    ('“Negating injustice of Allah” affirms what?',
     ['That He is unable',
      'Perfect justice (العَدْل) — for no attribute is negated of Allah except '
      'to affirm the opposite perfection',
      'That justice is optional',
      'Nothing at all'], 1),
    ('What are the two kinds of guidance in «فَاسْتَهْدُونِي أَهْدِكُم»?',
     ['Guidance of wealth and guidance of health',
      'Hidāyat al-tawfīq (success — from Allah alone) and hidāyat al-dalālah '
      '(showing the way — sought also from the people of knowledge)',
      'Guidance of the body and guidance of the tongue',
      'Public and private guidance'], 1),
    ('What does seeking provision (الاسْتِطْعَام) require, alongside asking '
     'Allah?',
     ['Nothing — provision comes without any effort',
      'Taking the means — the sky rains no gold; «فَانْتَشِرُوا فِي الأَرْضِ»',
      'Only reciting duʿāʾ a fixed number',
      'Abandoning all work and trusting fate'], 1),
    ('For whom does Allah forgive all sins, per «فَاسْتَغْفِرُونِي أَغْفِرْ '
     'لَكُم»?',
     ['Everyone, whether they seek it or not',
      'The one who seeks His forgiveness — by words or by the deeds that bring '
      'it',
      'Only the prophets',
      'Only those free of all minor sins'], 1),
    ('How are sins categorised in this lesson?',
     ['Spoken, written, and intended',
      'Kufr (needs tawbah by ijmāʿ), kabāʾir (need a particular tawbah), and '
      'ṣaghāʾir (expiated by acts of obedience)',
      'Small, medium, and large by count',
      'Hidden and open only'], 1),
    ('What do the three “law anna” statements establish?',
     ['That creation can increase or decrease Allah’s kingdom',
      'The perfection of Allah’s self-sufficiency and dominion — all obedience '
      'adds nothing, all sin subtracts nothing, all giving diminishes nothing',
      'That the jinn are more numerous than mankind',
      'That duʿāʾ has no effect'], 1),
    ('What does «فَمَنْ وَجَدَ غَيْرَ ذَلِكَ فَلَا يَلُومَنَّ إِلَّا '
     'نَفْسَهُ» teach?',
     ['That Allah wrongs some of His servants',
      'That the one who finds evil was not wronged — the proof was established '
      'and he left it, so the blame is on himself alone',
      'That deeds are not recorded',
      'That repentance is useless'], 1),
])

# ------------------------------------------------------------------ T/F
b += B.tf('hd-h24-tf', [
    ('الحَدِيثُ القُدْسِيُّ هُوَ مَا رَوَاهُ النَّبِيُّ ﷺ عَنْ رَبِّهِ عَزَّ '
     'وَجَلّ.',
     'A qudsī ḥadīth is what the Prophet ﷺ narrated from his Lord.', True),
    ('القُرْآنُ وَالحَدِيثُ القُدْسِيُّ سَوَاءٌ فِي كُلِّ الأَحْكَام.',
     'The Qurʾān and the qudsī ḥadīth are the same in every ruling.', False),
    ('اللهُ تَعَالَى قَادِرٌ عَلَى الظُّلْمِ لَكِنَّهُ حَرَّمَهُ عَلَى '
     'نَفْسِهِ لِكَمَالِ عَدْلِه.',
     'Allah is able to do injustice, but He forbade it upon Himself out of the '
     'perfection of His justice.', True),
    ('هِدَايَةُ التَّوْفِيقِ تُطْلَبُ مِنَ النَّاسِ كَهِدَايَةِ الدَّلَالَة.',
     'The guidance of success is sought from people, like the guidance of '
     'showing the way.', False),
    ('لَوْ كَانَ الخَلْقُ كُلُّهُمْ عَلَى أَتْقَى قَلْبِ رَجُلٍ مَا زَادَ '
     'ذَلِكَ فِي مُلْكِ الله.',
     'Were all creation upon the most pious heart of one man, that would add '
     'nothing to Allah’s dominion.', True),
    ('مَحَلُّ التَّقْوَى وَالفُجُورِ هُوَ القَلْب.',
     'The seat of taqwā and fujūr is the heart.', True),
    ('مَنْ وَجَدَ غَيْرَ الخَيْرِ فَإِنَّ اللهَ قَدْ ظَلَمَهُ.',
     'Whoever finds other than good — Allah has wronged him.', False),
])

b += B.memorize(
    'يَا عِبَادِي، إِنِّي حَرَّمْتُ الظُّلْمَ عَلَى نَفْسِي وَجَعَلْتُهُ '
    'بَيْنَكُمْ مُحَرَّمًا فَلَا تَظَالَمُوا… إِنَّمَا هِيَ أَعْمَالُكُمْ '
    'أُحْصِيهَا لَكُمْ ثُمَّ أُوَفِّيكُمْ إِيَّاهَا',
    'Allah speaks directly to His servants. He <strong>forbade injustice upon '
    'Himself</strong> — though able — and between us, so we wrong no one. He '
    'lays bare our need: all <strong>astray, hungry, naked</strong> but for '
    'Him, so ask Him. He <strong>forgives every sin</strong> for the one who '
    'seeks it. We cannot <strong>harm or benefit Him</strong>: all our '
    'obedience adds nothing to His dominion, all our sin takes nothing from it, '
    'all our asking diminishes His treasures only as a needle diminishes the '
    'sea. <em>And it closes on justice: they are only your deeds, counted and '
    'repaid in full — so whoever finds good, let him praise Allah; and whoever '
    'finds otherwise, let him blame none but himself.</em>')

b += B.nav('h23-al-tuhur-shatr-al-iman.html', 'Ḥadīth 23 · الطُّهُورُ شَطْرُ الإِيمَان',
           'index.html', 'Mark complete · أَتْمَمْتَ الدَّرْس · Hadeeth Hub',
           'hd-h24')

B.write('h24-ya-ibadi-innii-harramtu-al-zulm.html',
        'يَا عِبَادِي إِنِّي حَرَّمْتُ الظُّلْم',
        'O My Servants, I Have Forbidden Injustice',
        'Ḥadīth 24 of al-Nawawī’s Forty (Abū Dharr al-Ghifārī, Muslim) with the '
        'sharḥ of Ibn ʿUthaymīn — the great qudsī ḥadīth. What a ḥadīth qudsī '
        'is and how it differs from the Qurʾān; Allah forbidding injustice upon '
        'Himself though able, and a negation affirming the opposite perfection '
        '(al-Kahf 18:49, al-Anʿām 6:12, Āl ʿImrān 3:28); the servant astray, '
        'hungry and naked but for Allah, and the two kinds of guidance '
        '(al-Jumuʿah 62:10); forgiveness of all sins for the one who seeks it '
        'and the three categories of sin (al-Aḥzāb 33:72); the perfection of '
        'Allah’s self-sufficiency and dominion; and “only your deeds, counted '
        'and repaid in full” (al-Zalzalah 99:7–8).',
        24, 'Muslim', '2', b)
print('wrote h24-ya-ibadi-innii-harramtu-al-zulm.html')
