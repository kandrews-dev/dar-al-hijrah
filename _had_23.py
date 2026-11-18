# -*- coding: utf-8 -*-
"""Ḥadīth 23 — «الطُّهُورُ شَطْرُ الإِيمَان…». Abū Mālik al-Ḥārith ibn ʿĀṣim
al-Ashʿarī, Ṣaḥīḥ Muslim. Sharḥ of Ibn ʿUthaymīn, printed folios 243–258
(markers 244–259, offset −1).

A comprehensive ḥadīth that runs through the whole of worship: purification as
half of faith, the words that fill the Scale, prayer as light, ṣadaqah as a
proof, ṣabr as a radiance (its three kinds), the Qurʾān as a proof for or
against, and every soul sold each morning — freed or destroyed.

Rule 8: the ḥadīth is in Ṣaḥīḥ Muslim (Kitāb al-Ṭahārah), so ṣaḥīḥ — named
attribution, no grading invented.
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
    'Say who narrated this ḥadīth and where it is reported, and give the two '
    'explanations of «%s».' % ar('الطُّهُورُ شَطْرُ الإِيمَان'),
    'Explain how «%s» and «%s» together are negation and affirmation, and that '
    'the Mīzān is real.'
    % (ar('سُبْحَانَ الله'), ar('الحَمْدُ لِله')),
    'Distinguish why prayer is called <strong>nūr</strong>, ṣadaqah a '
    '<strong>burhān</strong>, and ṣabr a <strong>ḍiyāʾ</strong>.',
    'Name the <strong>three kinds of ṣabr</strong> and the rank of riḍā above '
    'it.',
    'Explain how the Qurʾān is «%s», and how every person sells his soul each '
    'morning — freeing it or destroying it.'
    % ar('حُجَّةٌ لَكَ أَوْ عَلَيْك'),
])

b += B.provenance(243, 258)

b += B.hadith_block(
    'عَنْ أَبِي مَالِكٍ الحَارِثِ بْنِ عَاصِمٍ الأَشْعَرِيِّ رَضِيَ اللهُ عَنْهُ '
    'قَالَ: قَالَ رَسُولُ اللهِ ﷺ: «الطُّهُورُ شَطْرُ الإِيمَانِ، وَالحَمْدُ '
    'لِلهِ تَمْلَأُ المِيزَانَ، وَسُبْحَانَ اللهِ وَالحَمْدُ لِلهِ تَمْلَآنِ '
    '— أَوْ تَمْلَأُ — مَا بَيْنَ السَّمَاءِ وَالأَرْضِ، وَالصَّلَاةُ نُورٌ، '
    'وَالصَّدَقَةُ بُرْهَانٌ، وَالصَّبْرُ ضِيَاءٌ، وَالقُرْآنُ حُجَّةٌ لَكَ '
    'أَوْ عَلَيْكَ. كُلُّ النَّاسِ يَغْدُو، فَبَائِعٌ نَفْسَهُ فَمُعْتِقُهَا '
    'أَوْ مُوبِقُهَا». رَوَاهُ مُسْلِم.',
    'Abū Mālik al-Ḥārith ibn ʿĀṣim al-Ashʿarī (may Allah be pleased with him) '
    'said: The Messenger of Allah ﷺ said: "Purification is half of faith; '
    '‘al-ḥamdu lillāh’ fills the Scale; ‘subḥān Allāh’ and ‘al-ḥamdu lillāh’ '
    'fill — or fills — what is between the heaven and the earth; prayer is '
    'light; charity is a proof; patience is a radiance; and the Qurʾān is a '
    'proof for you or against you. Every person goes out in the morning and '
    'sells his soul, either freeing it or destroying it." Narrated by Muslim.',
    'Narrated by Abū Mālik al-Ashʿarī · رَوَاهُ مُسْلِم — Muslim, in his Ṣaḥīḥ '
    '(Kitāb al-Ṭahārah, bāb faḍl al-wuḍūʾ), so the ḥadīth is ṣaḥīḥ.')

# ------------------------------------------------------------------ §1
b += B.heading('«الطُّهُورُ شَطْرُ الإِيمَان»', 'Purification Is Half of Faith')
b += p('<strong>“Shaṭr” means half.</strong> <em>Faith is either a doing or a '
       'leaving: the <strong>leaving</strong> is a kind of purification '
       '(تَطْهِير), and the <strong>doing</strong> is a bringing-into-being. So '
       'purification stands for one of the two halves of faith.</em>')
b += p('<strong>A second explanation</strong> was given: that «shaṭr al-īmān» '
       'means <em>casting off shirk</em>, for shirk is a najāsah — «%s». <em>But '
       'the first meaning is better and more general.</em>'
       % ar('إِنَّمَا المُشْرِكُونَ نَجَس'))
b += B.ayah(
    'إِنَّمَا الْمُشْرِكُونَ نَجَسٌ',
    'Indeed the polytheists are impure.',
    'سُورَةُ التَّوْبَة · 9:28')

# ------------------------------------------------------------------ §2
b += B.heading('كَلِمَاتٌ تَمْلَأُ المِيزَان', 'Words That Fill the Scale')
b += p('<strong>«%s» fills the Scale</strong> — and «%s» joined with it fills '
       'what lies between heaven and earth. <em>These two words are '
       '<strong>negation and affirmation</strong>: «سُبْحَانَ الله» is '
       '<strong>tanzīh</strong> — declaring Allah far above every deficiency '
       '(deficient attributes, any shortfall in His perfection, and any '
       'likeness to creation); «الحَمْدُ لِله» is the <strong>affirmation of '
       'His perfection</strong>, praising the Praised One with perfection '
       'together with love and reverence.</em>'
       % (ar('الحَمْدُ لِله'), ar('سُبْحَانَ الله')))
b += B.ayah(
    'لَيْسَ كَمِثْلِهِ شَيْءٌ وَهُوَ السَّمِيعُ الْبَصِيرُ',
    'There is nothing like unto Him, and He is the All-Hearing, the '
    'All-Seeing.',
    'سُورَةُ الشُّورَى · 42:11')
b += box(
    '<p style="margin:0;font-size:.94rem"><strong>The Mīzān is real.</strong> '
    '<em>Against the Muʿtazilah, who made it a figure for “establishing '
    'justice,” the correct view is that the Scale on the Day of Resurrection is '
    'a true Scale with two pans, by which deeds are weighed.</em> «%s» And how '
    'a deed or a word is weighed though it is not a body — Allah is able to '
    'make deeds and meanings into bodies; He is over all things capable.</p>'
    % ar('وَنَضَعُ المَوَازِينَ القِسْطَ لِيَوْمِ القِيَامَة'))
b += B.ayah(
    'وَنَضَعُ الْمَوَازِينَ الْقِسْطَ لِيَوْمِ الْقِيَامَةِ فَلَا تُظْلَمُ '
    'نَفْسٌ شَيْئًا',
    'And We place the scales of justice for the Day of Resurrection, so no soul '
    'will be treated unjustly at all.',
    'سُورَةُ الأَنْبِيَاء · 21:47')

# ------------------------------------------------------------------ §3
b += B.heading('نُورٌ وَبُرْهَان', 'Prayer Is Light, Charity Is a Proof')
b += table([
    row('«%s»' % ar('الصَّلَاةُ نُور'),
        '<em>The prayer — obligatory and voluntary — is a light: in the heart, '
        'in the face, in the grave, and at the gathering.</em> Pray the true '
        'prayer in which your heart is present and your limbs are humbled, and '
        'you will feel your heart lit; and so he ﷺ said, “the coolness of my '
        'eye was placed in the prayer.”'),
    row('«%s»' % ar('الصَّدَقَةُ بُرْهَان'),
        '<em>Charity is a proof — a proof of the truthfulness of the giver’s '
        'faith.</em> For what he gives away is <strong>wealth</strong>, the '
        'beloved thing; parting with the beloved shows that what he hopes for '
        'with Allah is more beloved to him still.'),
])

# ------------------------------------------------------------------ §4
b += B.heading('«الصَّبْرُ ضِيَاء»', 'Patience Is a Radiance — Its Three Kinds')
b += p('<strong>Ṣabr is holding the soul back</strong> from what it must be '
       'held back from. The people of knowledge make it <strong>three '
       'kinds</strong>:')
b += table([
    row('١ · صَبْرٌ عَلَى الطَّاعَة',
        '<em>Patience upon obedience</em> — a man drawn by his soul to '
        'laziness, his bed, or idle talk, yet he binds himself to stand for the '
        'prayer. <strong>This is the highest in reward as patience</strong>, '
        'for in it is both restraint of the soul and toil of the body.'),
    row('٢ · صَبْرٌ عَنِ المَعْصِيَة',
        '<em>Patience away from disobedience</em> — as Yūsuf ﷺ restrained '
        'himself from the wife of al-ʿAzīz when she had shut the doors and '
        'called him, with the caller strong and the barriers gone — and he did '
        'not do it.'),
    row('٣ · صَبْرٌ عَلَى الأَقْدَار',
        '<em>Patience upon the decrees</em> — holding the heart from '
        'discontent, the tongue from wailing, and the limbs from striking the '
        'cheeks and tearing the garments when an affliction descends.'),
])
b += B.ayah(
    'رَبِّ السِّجْنُ أَحَبُّ إِلَيَّ مِمَّا يَدْعُونَنِي إِلَيْهِ',
    'My Lord, prison is more beloved to me than that to which they invite me.',
    'سُورَةُ يُوسُف · 12:33')
b += box(
    '<p style="margin:0 0 .5rem;font-size:.94rem"><strong>Above ṣabr is '
    'riḍā.</strong> <em>The patient one’s heart may ache and grieve, yet he '
    'holds himself from the ḥarām; the content one’s heart follows the decree '
    'of Allah and is pleased with what He chose.</em> So the people of '
    'knowledge say: <strong>ṣabr is obligatory, and riḍā is '
    'recommended.</strong></p>'
    '<p style="margin:0;font-size:.92rem"><strong>Why ḍiyāʾ and not nūr?</strong> '
    'He called the prayer <em>nūr</em> but ṣabr <em>ḍiyāʾ</em> — and ḍiyāʾ '
    'carries <strong>heat</strong>, as Allah named the sun ḍiyāʾ: «%s». Patience '
    'carries heat and bitterness, for it is hard upon the soul — so it is a '
    'radiance won through hardship.</p>'
    % ar('جَعَلَ الشَّمْسَ ضِيَاء'))
b += B.ayah(
    'هُوَ الَّذِي جَعَلَ الشَّمْسَ ضِيَاءً وَالْقَمَرَ نُورًا',
    'It is He who made the sun a shining light and the moon a derived light.',
    'سُورَةُ يُونُس · 10:5')

# ------------------------------------------------------------------ §5
b += B.heading('«القُرْآنُ حُجَّةٌ لَكَ أَوْ عَلَيْك»',
               'The Qurʾān — a Proof For You or Against You')
b += box(
    '<p style="margin:0;font-size:.94rem"><strong>The creed of Ahl al-Sunnah '
    'on the Qurʾān.</strong> <em>It is the speech of Allah — He truly spoke it; '
    'Jibrīl heard it and brought it down upon the heart of the Prophet ﷺ; its '
    'wording and its meaning are the speech of Allah, <strong>not '
    'created</strong>.</em> Against this the people of innovation said it is '
    'created or a mere “expression” of His speech — and the sound view is what '
    'the Salaf held.</p>')
b += p('<strong>And it is a proof for you or against you.</strong> <em>It is a '
       'proof <strong>for</strong> you if you give it its due and act by it, '
       'and a proof <strong>against</strong> you if you do not.</em> Take «%s»: '
       'the one who establishes the prayer — the Qurʾān is a proof for him; the '
       'one who does not — it is a proof against him. So weigh yourself: have I '
       'acted by it, or not?'
       % ar('وَأَقِيمُوا الصَّلَاةَ وَآتُوا الزَّكَاة'))

# ------------------------------------------------------------------ §6
b += B.heading('«كُلُّ النَّاسِ يَغْدُو»', 'Every Soul Sold Each Morning')
b += p('<strong>Everyone goes out in the morning</strong> and <em>sells his '
       'soul</em> — that is, he burdens it with work and so “sells” it. <em>And '
       'the sellers are two: <strong>one who frees it</strong> (مُعْتِق) and '
       '<strong>one who destroys it</strong> (مُوبِق).</em> Whoever spends it in '
       'the obedience of Allah has freed it from the Fire; whoever spends his '
       'life in loss has destroyed it.')
b += B.ayah(
    'وَمِنَ النَّاسِ مَن يَشْرِي نَفْسَهُ ابْتِغَاءَ مَرْضَاتِ اللَّهِ',
    'And of the people is he who sells himself, seeking the pleasure of Allah.',
    'سُورَةُ البَقَرَة · 2:207')
b += box(
    '<p style="margin:0;font-size:.94rem"><strong>True freedom is obedience.</strong> '
    '<em>Real freedom is to stand in the worship of Allah — not that a person '
    'lets his soul loose to do all it wants.</em> As Ibn al-Qayyim said: men '
    'fled the servitude they were created for, and were tried with the '
    'servitude of the soul and the shayṭān — for whoever flees the worship of '
    'Allah stays in the bondage of the shayṭān.</p>')

# ------------------------------------------------------------------ vocab
b += B.vocab([
    ('الطَّهُور', 'al-ṭahūr', 'purification', 'ط-ه-ر',
     'Called “half of faith” (شَطْرُ الإِيمَان) — faith being either a doing or '
     'a leaving, and purification is of the leaving side',
     'الطُّهُورُ شَطْرُ الإِيمَان'),
    ('شَطْر', 'shaṭr', 'a half', 'ش-ط-ر',
     'Its meaning here — purification is one of the two halves of faith',
     'الطُّهُورُ شَطْرُ الإِيمَان'),
    ('المِيزَان', 'al-mīzān', 'the Scale (of deeds)', 'و-ز-ن',
     'A real Scale on the Day of Resurrection, with two pans, by which deeds '
     'are weighed; «al-ḥamdu lillāh» fills it',
     'وَالحَمْدُ لِلهِ تَمْلَأُ المِيزَان'),
    ('بُرْهَان', 'burhān', 'a proof, a decisive sign', 'ب-ر-ه-ن',
     'What charity is called — a proof of the truthfulness of the giver’s '
     'faith, since he parts with wealth, the beloved thing',
     'وَالصَّدَقَةُ بُرْهَان'),
    ('الصَّبْر', 'al-ṣabr', 'patience', 'ص-ب-ر',
     'Holding the soul back; of three kinds — upon obedience, away from '
     'disobedience, and upon the decrees; a ḍiyāʾ',
     'وَالصَّبْرُ ضِيَاء'),
    ('ضِيَاء', 'ḍiyāʾ', 'radiance (light with heat)', 'ض-و-أ',
     'Unlike nūr, ḍiyāʾ carries heat — as the sun is ḍiyāʾ; ṣabr is a ḍiyāʾ for '
     'the hardship and bitterness in it',
     'جَعَلَ الشَّمْسَ ضِيَاء'),
    ('حُجَّة', 'ḥujjah', 'a proof, an argument', 'ح-ج-ج',
     'The Qurʾān is a ḥujjah for you if you act by it, and a ḥujjah against you '
     'if you do not',
     'وَالقُرْآنُ حُجَّةٌ لَكَ أَوْ عَلَيْك'),
    ('مُوبِق', 'mūbiq', 'one who destroys (his soul)', 'و-ب-ق',
     'The opposite of مُعْتِق (one who frees it); whoever spends his life in '
     'loss has destroyed his soul',
     'فَبَائِعٌ نَفْسَهُ فَمُعْتِقُهَا أَوْ مُوبِقُهَا'),
])

# ------------------------------------------------------------------ MCQ
b += B.mcq('hd-h23', [
    ('Who narrated this ḥadīth, and where is it reported?',
     ['Abū Hurayrah, in al-Bukhārī',
      'Abū Mālik al-Ḥārith ibn ʿĀṣim al-Ashʿarī, in Muslim',
      'Jābir ibn ʿAbdillāh, in al-Tirmidhī',
      'Abū Saʿīd al-Khudrī, in Abū Dāwūd'], 1),
    ('What is the better explanation of «الطُّهُورُ شَطْرُ الإِيمَان»?',
     ['That faith is only purification',
      'Faith is either doing or leaving; the leaving is a purification, so '
      'purification is one of its two halves',
      'That ablution erases all sins alone',
      'That purification is optional in faith'], 1),
    ('How are «سُبْحَانَ الله» and «الحَمْدُ لِله» together described?',
     ['Both are pure affirmation',
      'Negation and affirmation — tasbīḥ declares Allah above all deficiency, '
      'ḥamd affirms His perfection',
      'Both are pure negation',
      'Two phrases with the same single meaning'], 1),
    ('What is the correct view of the Mīzān on the Day of Resurrection?',
     ['A figure of speech for establishing justice',
      'A real Scale with two pans, by which deeds are weighed',
      'Only the record books, not a scale',
      'A scale for the prophets alone'], 1),
    ('Why is charity called a «بُرْهَان» (a proof)?',
     ['Because it is given publicly',
      'Because parting with wealth — the beloved thing — proves the '
      'truthfulness of the giver’s faith',
      'Because it is written in a register',
      'Because it must be witnessed'], 1),
    ('What are the three kinds of ṣabr?',
     ['Of the tongue, the hand, and the eye',
      'Upon obedience, away from disobedience, and upon the decrees (aqdār)',
      'In youth, middle age, and old age',
      'Secret, open, and written'], 1),
    ('Which kind of ṣabr is highest in reward purely as patience?',
     ['Patience upon the decrees',
      'Patience upon obedience — for in it is restraint of the soul and toil '
      'of the body',
      'Patience away from disobedience',
      'They are all equal in every respect'], 1),
    ('How do the scholars rank ṣabr and riḍā?',
     ['Both are obligatory',
      'Ṣabr is obligatory, and riḍā (contentment) is recommended and higher in '
      'state',
      'Riḍā is obligatory and ṣabr recommended',
      'Both are merely recommended'], 1),
    ('Why is ṣabr called ḍiyāʾ while prayer is called nūr?',
     ['Because ṣabr is brighter than prayer',
      'Because ḍiyāʾ carries heat — as the sun is ḍiyāʾ — and ṣabr carries the '
      'heat and bitterness of hardship',
      'Because prayer has no light at all',
      'Because ṣabr is only for the Hereafter'], 1),
    ('What is the creed of Ahl al-Sunnah on the Qurʾān?',
     ['It is created, like the heavens',
      'It is the speech of Allah, uncreated — its wording and meaning — heard '
      'by Jibrīl and brought down upon the Prophet’s ﷺ heart',
      'It is a mere expression of Allah’s speech',
      'It is the Prophet’s ﷺ own words inspired'], 1),
    ('When is the Qurʾān a proof FOR a person?',
     ['When he memorises its words only',
      'When he gives it its due and acts by it; it is against him if he does '
      'not',
      'When he recites it beautifully',
      'When he owns a fine copy of it'], 1),
    ('What does «فَبَائِعٌ نَفْسَهُ فَمُعْتِقُهَا أَوْ مُوبِقُهَا» mean?',
     ['People trade goods each morning',
      'Each person sells his soul daily — freeing it by obeying Allah, or '
      'destroying it by spending his life in loss',
      'People must free a slave each morning',
      'The soul cannot be changed by deeds'], 1),
])

# ------------------------------------------------------------------ T/F
b += B.tf('hd-h23-tf', [
    ('الطُّهُورُ شَطْرُ الإِيمَانِ، وَالإِيمَانُ إِمَّا فِعْلٌ وَإِمَّا تَرْك.',
     'Purification is half of faith, and faith is either a doing or a leaving.',
     True),
    ('«سُبْحَانَ الله» فِيهَا إِثْبَاتُ الكَمَالِ لَا نَفْيُ النَّقْص.',
     '«Subḥān Allāh» is an affirmation of perfection, not a negation of '
     'deficiency.', False),
    ('المِيزَانُ يَوْمَ القِيَامَةِ حِسِّيٌّ حَقِيقِيٌّ تُوزَنُ بِهِ '
     'الأَعْمَال.',
     'The Scale on the Day of Resurrection is real and tangible, by which '
     'deeds are weighed.', True),
    ('الصَّدَقَةُ بُرْهَانٌ لِأَنَّ بَذْلَ المَحْبُوبِ يَدُلُّ عَلَى صِدْقِ '
     'البَاذِل.',
     'Charity is a proof because parting with the beloved thing shows the '
     'truthfulness of the giver.', True),
    ('الرِّضَا بِأَقْدَارِ اللهِ أَعْلَى حَالاً مِنَ الصَّبْرِ عَلَيْهَا.',
     'Contentment with Allah’s decrees is a higher state than patience upon '
     'them.', True),
    ('القُرْآنُ مَخْلُوقٌ عِنْدَ أَهْلِ السُّنَّةِ وَالجَمَاعَة.',
     'The Qurʾān is created according to Ahl al-Sunnah wa-l-Jamāʿah.', False),
    ('الحُرِّيَّةُ الحَقِيقِيَّةُ هِيَ القِيَامُ بِطَاعَةِ اللهِ عَزَّ '
     'وَجَلّ.',
     'True freedom is to stand in the obedience of Allah.', True),
])

b += B.memorize(
    'الطُّهُورُ شَطْرُ الإِيمَانِ، وَالحَمْدُ لِلهِ تَمْلَأُ المِيزَانَ… '
    'وَالصَّلَاةُ نُورٌ، وَالصَّدَقَةُ بُرْهَانٌ، وَالصَّبْرُ ضِيَاءٌ، '
    'وَالقُرْآنُ حُجَّةٌ لَكَ أَوْ عَلَيْكَ',
    'One ḥadīth that walks through the whole of worship: '
    '<strong>purification</strong> is half of faith; the two words of praise '
    '<strong>fill the Scale</strong> and all between heaven and earth — '
    'negation and affirmation; the <strong>prayer</strong> is a light, '
    '<strong>charity</strong> a proof of true faith, <strong>patience</strong> '
    'a radiance won through hardship (its three kinds: upon obedience, away '
    'from sin, upon the decrees); and the <strong>Qurʾān</strong> stands as a '
    'proof — for you if you act by it, against you if you do not. <em>And every '
    'morning you sell your soul: you free it in obedience, or you destroy it. '
    'True freedom is to belong to Allah.</em>')

b += B.nav('h22-araayta-idha-sallaytu.html', 'Ḥadīth 22 · أَرَأَيْتَ إِذَا صَلَّيْت',
           'index.html', 'Mark complete · أَتْمَمْتَ الدَّرْس · Hadeeth Hub',
           'hd-h23')

B.write('h23-al-tuhur-shatr-al-iman.html',
        'الطُّهُورُ شَطْرُ الإِيمَان',
        'Purification Is Half of Faith',
        'Ḥadīth 23 of al-Nawawī’s Forty (Abū Mālik al-Ashʿarī, Muslim) with the '
        'sharḥ of Ibn ʿUthaymīn: a comprehensive ḥadīth through the whole of '
        'worship. Purification as half of faith (al-Tawbah 9:28); the words '
        'that fill the Scale and the reality of the Mīzān (al-Shūrā 42:11, '
        'al-Anbiyāʾ 21:47); prayer as light and charity as a proof; patience as '
        'a radiance and its three kinds, with riḍā above it (Yūsuf 12:33, Yūnus '
        '10:5); the Qurʾān as a proof for or against you and the creed of Ahl '
        'al-Sunnah on it; and every soul sold each morning — freed or destroyed '
        '(al-Baqarah 2:207).',
        23, 'Muslim', '2', b)
print('wrote h23-al-tuhur-shatr-al-iman.html')
