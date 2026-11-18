# -*- coding: utf-8 -*-
"""Ḥadīth 21 — «قُلْ آمَنْتُ بِاللهِ ثُمَّ اسْتَقِمْ». Abū ʿAmr (and it is
said Abū ʿAmrah) Sufyān ibn ʿAbdillāh al-Thaqafī, Ṣaḥīḥ Muslim. Sharḥ of Ibn
ʿUthaymīn, printed folios 235–237 (markers 236–238, offset −1).

One of the most comprehensive ḥadīths: the whole religion in two words. The
Shaykh reads the question (a decisive, comprehensive, preventive statement),
unfolds the two words — «آمَنْتُ بِالله» (the heart's affirmation of tawḥīd)
and «اسْتَقِمْ» (going straight on the sharīʿah) — shows how together they gather
the two conditions of worship (ikhlāṣ + mutābaʿah), brings the three āyāt that
witness to it, corrects «مُلْتَزِم» to «مُسْتَقِيم», and turns it into a rule of
self-inspection.

Rule 8: the ḥadīth is in Ṣaḥīḥ Muslim (Kitāb al-Īmān), so ṣaḥīḥ — named
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
    'Say who narrated this ḥadīth and where it is reported, and what kind of '
    'statement Sufyān asked for — «%s».'
    % ar('قَوْلاً لَا أَسْأَلُ عَنْهُ أَحَدًا غَيْرَك'),
    'Unfold the two words of the answer — «%s» (the heart’s affirmation) and '
    '«%s» (going straight on the sharīʿah).'
    % (ar('آمَنْتُ بِالله'), ar('اسْتَقِمْ')),
    'Show how the two words gather the <strong>two conditions of worship</strong> '
    '— ikhlāṣ and mutābaʿah — so that the whole religion stands in two words.',
    'Name the three āyāt that witness to «%s».' % ar('رَبُّنَا اللهُ ثُمَّ اسْتَقَامُوا'),
    'Correct the common praise «%s» to the Qurʾānic «%s», and turn istiqāmah '
    'into a rule of self-inspection.'
    % (ar('مُلْتَزِم'), ar('مُسْتَقِيم')),
])

b += B.provenance(235, 237)

b += B.hadith_block(
    'عَنْ أَبِي عَمْرٍو، وَقِيلَ: أَبِي عَمْرَةَ، سُفْيَانَ بْنِ عَبْدِ اللهِ '
    'الثَّقَفِيِّ رَضِيَ اللهُ عَنْهُ قَالَ: قُلْتُ: يَا رَسُولَ اللهِ، قُلْ لِي '
    'فِي الإِسْلَامِ قَوْلاً لَا أَسْأَلُ عَنْهُ أَحَدًا غَيْرَكَ. قَالَ: «قُلْ '
    'آمَنْتُ بِاللهِ ثُمَّ اسْتَقِمْ». رَوَاهُ مُسْلِم.',
    'Abū ʿAmr — and it is said Abū ʿAmrah — Sufyān ibn ʿAbdillāh al-Thaqafī '
    '(may Allah be pleased with him) said: I said, "O Messenger of Allah, tell '
    'me a statement about Islam that I will ask no one about besides you." He '
    'said: "Say: I believe in Allah, then be steadfast." Narrated by Muslim.',
    'Narrated by Sufyān ibn ʿAbdillāh al-Thaqafī · رَوَاهُ مُسْلِم — Muslim, in '
    'his Ṣaḥīḥ (Kitāb al-Īmān, bāb jāmiʿ awṣāf al-Islām), so the ḥadīth is '
    'ṣaḥīḥ.')

# ------------------------------------------------------------------ §1
b += B.heading('«قُلْ لِي فِي الإِسْلَام»', 'What Sufyān Asked For')
b += p('<strong>“Tell me a statement about Islam” — that is, about the '
       'sharīʿah.</strong> <em>And «%s» means: a statement that is a '
       '<strong>decisive boundary</strong> (حَدٌّ فَاصِل), <strong>comprehensive '
       'and preventive</strong> (جَامِعٌ مَانِع) — one word he could hold to and '
       'need no other.</em> He did not ask for a long list; he asked for the '
       'kernel.'
       % ar('قَوْلاً لَا أَسْأَلُ عَنْهُ أَحَدًا غَيْرَك'))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.94rem"><strong>An apparent '
    'difficulty — «%s».</strong> Could a Companion really ask no one but the '
    'Messenger ﷺ about the religion?</p>'
    '<p style="margin:0;font-size:.92rem"><em>The answer: yes, a person may ask '
    'someone who surpasses him in knowledge — that happens. And the phrase is '
    'said even when one would not in fact ask another, in order to make the one '
    'questioned give the answer its due weight and care.</em></p>'
    % ar('لَا أَسْأَلُ عَنْهُ أَحَدًا غَيْرَك'))

# ------------------------------------------------------------------ §2
b += B.heading('الكَلِمَتَان', 'The Two Words')
b += p('<strong>The Prophet ﷺ gave him two words</strong> — «%s» and «%s» — and '
       '<em>these two gathered the whole religion.</em>'
       % (ar('آمَنْتُ بِالله'), ar('اسْتَقِمْ')))
b += table([
    row('«%s»' % ar('قُلْ آمَنْتُ'),
        '<em>This takes in the <strong>saying of the tongue</strong> and the '
        '<strong>saying of the heart</strong> together.</em> The people of '
        'knowledge say: the saying of the heart is its <strong>affirmation and '
        'acknowledgement</strong> (إِقْرَارُهُ وَاعْتِرَافُه). The locus of '
        'īmān is the heart.'),
    row('«%s»' % ar('آمَنْتُ بِالله'),
        '<em>“I have affirmed Him”</em> — according to what is obligatory upon '
        'the servant of belief in <strong>His oneness in rubūbiyyah, in '
        'ulūhiyyah, and in His names and attributes</strong> (تَوْحِيدُ '
        'الرُّبُوبِيَّةِ وَالأُلُوهِيَّةِ وَالأَسْمَاءِ وَالصِّفَات).'),
    row('«%s»' % ar('ثُمَّ اسْتَقِمْ'),
        '<em>Go straight on the sharīʿah</em> — <strong>neither to the right '
        'nor to the left</strong> (لَا يَمِينًا وَلَا شِمَالًا): no excess and '
        'no falling short.'),
])

# ------------------------------------------------------------------ §3
b += B.heading('الدِّينُ كُلُّهُ فِي كَلِمَتَيْن', 'The Whole Religion in Two Words')
b += p('<strong>Why is this among the most comprehensive of ḥadīths?</strong> '
       '<em>Because the two words meet the two conditions on which every act of '
       'worship is accepted:</em>')
b += table([
    row('«%s» ⟵ الإِخْلَاص' % ar('آمَنْتُ بِالله'),
        '<em>Belief in Allah entails <strong>ikhlāṣ</strong> — devoting the '
        'worship to Him alone.</em> This is the first condition of worship.'),
    row('«%s» ⟵ المُتَابَعَة' % ar('اسْتَقِمْ'),
        '<em>Istiqāmah entails <strong>mutābaʿah</strong> — walking upon His '
        'sharīʿah ﷺ.</em> This is the second condition of worship.'),
])
b += p('<em>So the Prophet ﷺ was given <strong>jawāmiʿ al-kalim</strong> — '
       'speech that gathers much in little — when he placed the entire dīn in '
       'two words.</em> And the Qurʾān itself bears this out three times, each '
       'joining <strong>«%s»</strong> to <strong>«%s»</strong>:'
       % (ar('قَالُوا رَبُّنَا الله'), ar('ثُمَّ اسْتَقَامُوا')))
b += B.ayah(
    'إِنَّ الَّذِينَ قَالُوا رَبُّنَا اللَّهُ ثُمَّ اسْتَقَامُوا فَلَا خَوْفٌ '
    'عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ',
    'Indeed, those who say, "Our Lord is Allah," and then are steadfast — there '
    'will be no fear concerning them, nor will they grieve.',
    'سُورَةُ الأَحْقَاف · 46:13')
b += B.ayah(
    'إِنَّ الَّذِينَ قَالُوا رَبُّنَا اللَّهُ ثُمَّ اسْتَقَامُوا تَتَنَزَّلُ '
    'عَلَيْهِمُ الْمَلَائِكَةُ أَلَّا تَخَافُوا وَلَا تَحْزَنُوا وَأَبْشِرُوا '
    'بِالْجَنَّةِ الَّتِي كُنتُمْ تُوعَدُونَ',
    'Indeed, those who say, "Our Lord is Allah," and then are steadfast — the '
    'angels descend upon them, [saying], "Fear not, nor grieve, but receive '
    'good tidings of the Paradise which you were promised."',
    'سُورَةُ فُصِّلَت · 41:30')
b += B.ayah(
    'فَاسْتَقِمْ كَمَا أُمِرْتَ وَمَن تَابَ مَعَكَ',
    'So remain on a right course as you have been commanded, [you] and those '
    'who have turned back with you.',
    'سُورَةُ هُود · 11:112')

# ------------------------------------------------------------------ §4
b += B.heading('اسْتِقَامَةٌ لَا الْتِزَام', 'Say “Upright,” Not “Committed”')
b += box(
    '<p style="margin:0;font-size:.94rem"><strong>A point of language the Shaykh '
    'is careful about.</strong> <em>People today, when they want to praise '
    'someone for holding to the religion, say: “Fulān is <strong>multazim</strong> '
    '(مُلْتَزِم).” The correct thing is to say: “Fulān is <strong>mustaqīm</strong> '
    '(مُسْتَقِيم)” — upright — for that is the word that came in the Qurʾān and '
    'the Sunnah.</em> The ḥadīth says «اسْتَقِمْ», and the āyāt say «اسْتَقَامُوا» '
    '— so let the praise follow the revealed word.</p>')

# ------------------------------------------------------------------ §5
b += B.heading('تَفَقُّدُ النَّفْس', 'Inspect Yourself: Am I Upright?')
b += p('<strong>Istiqāmah is not a label one claims once; it is a line one must '
       'keep.</strong> <em>Whoever falls short in the obligations has not stayed '
       'upright — rather deviation (اِنْحِرَاف) has entered, and its severity is '
       'by the measure of what he left of duties or did of forbidden things.</em> '
       'So a person should <strong>always inspect himself</strong>: am I upright '
       'or not? If upright, he praises Allah, thanks Him, and asks Him for '
       'firmness (الثَّبَات); if not, he must straighten his course back to Allah.')
b += p('<strong>Istiqāmah is a general, sweeping description of all one’s '
       'deeds</strong> — and so its opposite shows in every field:')
b += table([
    row('أَخَّرَ الصَّلَاةَ عَنْ وَقْتِهَا',
        '<em>Whoever delays the prayer past its time is <strong>not '
        'upright</strong></em> — he has let the prayer slip.'),
    row('مَنَعَ الزَّكَاة',
        '<em>Whoever withholds the zakāh is not upright</em> — he has let the '
        'zakāh slip.'),
    row('اعْتَدَى عَلَى أَعْرَاضِ النَّاس',
        '<em>Whoever transgresses against people’s honour is not upright</em> — '
        'for doing the forbidden.'),
    row('غَشَّ وَخَادَعَ فِي البَيْعِ وَالشِّرَاء',
        '<em>Whoever cheats and deceives in buying, selling, hiring and the '
        'like is not upright.</em>'),
])

# ------------------------------------------------------------------ vocab
b += B.vocab([
    ('اِسْتَقِمْ', 'istaqim', 'be steadfast, go straight', 'ق-و-م',
     'The command that gathers half the dīn — walk upon the sharīʿah, neither '
     'to the right nor to the left; entails mutābaʿah, following the Prophet ﷺ',
     'قُلْ آمَنْتُ بِاللهِ ثُمَّ اسْتَقِمْ'),
    ('آمَنْتُ بِالله', 'āmantu billāh', 'I believe in Allah', 'أ-م-ن',
     'The heart’s and tongue’s affirmation of Allah’s oneness in rubūbiyyah, '
     'ulūhiyyah, and names and attributes; its locus is the heart; entails '
     'ikhlāṣ',
     'قُلْ آمَنْتُ بِاللهِ ثُمَّ اسْتَقِمْ'),
    ('جَوَامِعُ الكَلِم', 'jawāmiʿ al-kalim', 'comprehensive speech', 'ج-م-ع',
     'Few words carrying much meaning — a gift given to the Prophet ﷺ; here, '
     'the entire religion placed in two words',
     'أُوتِيَ النَّبِيُّ ﷺ جَوَامِعَ الكَلِم'),
    ('حَدٌّ فَاصِل', 'ḥadd fāṣil', 'a decisive boundary', 'ف-ص-ل',
     'What Sufyān wanted — a statement that is jāmiʿ (comprehensive) and māniʿ '
     '(preventive), so that one word suffices and he need ask no other',
     'طَلَبَ قَوْلاً يَكُونُ حَدًّا فَاصِلاً جَامِعًا مَانِعًا'),
    ('الإِخْلَاص', 'al-ikhlāṣ', 'sincerity (to Allah alone)', 'خ-ل-ص',
     'The first condition of accepted worship — entailed by «آمَنْتُ بِالله»: '
     'that the deed be devoted to Allah alone',
     'الإِيمَانُ بِاللهِ يَتَضَمَّنُ الإِخْلَاصَ فِي العِبَادَة'),
    ('المُتَابَعَة', 'al-mutābaʿa', 'following (the Sunnah)', 'ت-ب-ع',
     'The second condition of accepted worship — entailed by «اسْتَقِمْ»: that '
     'the deed follow the sharīʿah of the Prophet ﷺ',
     'الاِسْتِقَامَةُ تَتَضَمَّنُ المُتَابَعَةَ عَلَى شَرِيعَتِه'),
    ('قَوْلُ القَلْب', 'qawl al-qalb', 'the saying of the heart', 'ق-و-ل',
     'Included in «قُلْ آمَنْتُ» alongside the saying of the tongue — and it is '
     'the heart’s affirmation and acknowledgement (إِقْرَارُهُ وَاعْتِرَافُه)',
     'قَوْلُ القَلْبِ هُوَ إِقْرَارُهُ وَاعْتِرَافُه'),
    ('الاِلْتِزَام', 'al-iltizām', 'commitment (the popular term)', 'ل-ز-م',
     'The word people now use to praise religious adherence — «فُلَانٌ '
     'مُلْتَزِم»; the Shaykh corrects it to «مُسْتَقِيم», the word of the '
     'Qurʾān and Sunnah',
     'الصَّوَابُ أَنْ يُقَالَ مُسْتَقِيمٌ لَا مُلْتَزِم'),
])

# ------------------------------------------------------------------ MCQ
b += B.mcq('hd-h21', [
    ('Who narrated this ḥadīth, and where is it reported?',
     ['Abū Hurayrah, in al-Bukhārī',
      'Sufyān ibn ʿAbdillāh al-Thaqafī (Abū ʿAmr / Abū ʿAmrah), in Muslim',
      'Muʿādh ibn Jabal, in al-Tirmidhī',
      'Ibn Masʿūd, in Abū Dāwūd'], 1),
    ('What did Sufyān mean by «قُلْ لِي فِي الإِسْلَام»?',
     ['Teach me the five pillars in order',
      'Tell me a statement about the sharīʿah — the religion',
      'Give me a supplication to recite',
      'Name for me the best of the Companions'], 1),
    ('What kind of statement did he ask for in «لَا أَسْأَلُ عَنْهُ أَحَدًا '
     'غَيْرَك»?',
     ['A long, detailed list of rulings',
      'A decisive boundary (حَدٌّ فَاصِل) — comprehensive and preventive — one '
      'word he could hold to',
      'A secret known to no one else',
      'A poem that is easy to memorise'], 1),
    ('How is the apparent difficulty in «لَا أَسْأَلُ عَنْهُ أَحَدًا غَيْرَك» '
     'resolved?',
     ['A Companion was forbidden to ask anyone but the Prophet ﷺ',
      'One may ask someone who surpasses him in knowledge; and the phrase is '
      'said to make the one questioned weigh his answer carefully',
      'The narration is weak and the phrase is dropped',
      'It means he would only ask in writing'], 1),
    ('What does «قُلْ آمَنْتُ» take in?',
     ['The saying of the tongue only',
      'Both the saying of the tongue and the saying of the heart',
      'An action of the limbs only',
      'A silent intention with no words'], 1),
    ('What is the “saying of the heart,” per the people of knowledge?',
     ['Reciting aloud',
      'Its affirmation and acknowledgement (إِقْرَارُهُ وَاعْتِرَافُه)',
      'A fleeting thought',
      'Love without belief'], 1),
    ('«آمَنْتُ بِالله» is affirmation of Allah’s oneness in which respects?',
     ['Rubūbiyyah only',
      'Rubūbiyyah, ulūhiyyah, and the names and attributes',
      'Ulūhiyyah only',
      'The names and attributes only'], 1),
    ('What does «اسْتَقِمْ» mean here?',
     ['Perform many optional prayers',
      'Go straight on the sharīʿah — neither to the right nor to the left',
      'Withdraw from people',
      'Fast every day of the year'], 1),
    ('How do the two words gather the two conditions of accepted worship?',
     ['«آمَنْتُ» gives fear and «اسْتَقِمْ» gives hope',
      '«آمَنْتُ بِالله» entails ikhlāṣ, and «اسْتَقِمْ» entails mutābaʿah',
      '«آمَنْتُ» is for the heart and «اسْتَقِمْ» is only for the tongue',
      'They do not relate to worship’s conditions'], 1),
    ('Which āyah joins «رَبُّنَا اللهُ ثُمَّ اسْتَقَامُوا» to the angels '
     'descending with glad tidings of Paradise?',
     ['al-Aḥqāf 46:13',
      'Fuṣṣilat 41:30',
      'Hūd 11:112',
      'al-Baqarah 2:112'], 1),
    ('How does the Shaykh correct the common praise «فُلَانٌ مُلْتَزِم»?',
     ['He approves it as the better expression',
      'The correct word is «مُسْتَقِيم» (upright) — the term of the Qurʾān and '
      'the Sunnah',
      'He says both are forbidden to use',
      'He prefers «مُتَدَيِّن»'], 1),
    ('By the measure of istiqāmah, a man who delays the prayer past its time '
     'is…',
     ['still upright, since he prays eventually',
      'not upright (غَيْر مُسْتَقِيم) — he has let the prayer slip',
      'upright only if he makes it up',
      'excused because time is relative'], 1),
])

# ------------------------------------------------------------------ T/F
b += B.tf('hd-h21-tf', [
    ('«آمَنْتُ بِالله» مَحَلُّ الإِيمَانِ فِيهِ القَلْب.',
     'In «I believe in Allah», the locus of faith is the heart.', True),
    ('«قُلْ لِي فِي الإِسْلَام» أَيْ فِي الشَّرِيعَة.',
     '«Tell me about Islam» means: about the sharīʿah.', True),
    ('الصَّوَابُ أَنْ يُثْنَى عَلَى المُتَمَسِّكِ بِالدِّينِ بِأَنَّهُ '
     '«مُلْتَزِم» لَا «مُسْتَقِيم».',
     'The correct praise for one who holds to the religion is “multazim,” not '
     '“mustaqīm.”', False),
    ('«اسْتَقِمْ» مَعْنَاهَا التَّمَشِّي عَلَى شَرِيعَةِ اللهِ لَا يَمِينًا '
     'وَلَا شِمَالًا.',
     '«Be steadfast» means to walk upon the sharīʿah of Allah, neither right '
     'nor left.', True),
    ('الإِيمَانُ بِاللهِ يَتَضَمَّنُ الإِخْلَاصَ، وَالاِسْتِقَامَةُ '
     'تَتَضَمَّنُ المُتَابَعَة.',
     'Belief in Allah entails ikhlāṣ, and istiqāmah entails mutābaʿah.', True),
    ('مَنْ أَخَّرَ الصَّلَاةَ عَنْ وَقْتِهَا فَهُوَ مُسْتَقِيم.',
     'Whoever delays the prayer past its time is upright.', False),
    ('لَا يُمْكِنُ لِأَحَدٍ مِنَ الصَّحَابَةِ أَنْ يَسْأَلَ أَحَدًا غَيْرَ '
     'النَّبِيِّ ﷺ فِي أُمُورِ الدِّين.',
     'It is impossible for any Companion to ask anyone other than the Prophet ﷺ '
     'about matters of religion.', False),
])

b += B.memorize(
    'قُلْ آمَنْتُ بِاللهِ ثُمَّ اسْتَقِمْ',
    'A Companion asked for one word about Islam he would need no other for, and '
    'the Prophet ﷺ gave him the whole religion in two: <strong>آمَنْتُ '
    'بِالله</strong> — the heart’s affirmation of Allah’s oneness, which '
    'carries <strong>ikhlāṣ</strong>; and <strong>اسْتَقِمْ</strong> — go '
    'straight on the sharīʿah, which carries <strong>mutābaʿah</strong>. '
    'Between them stand the two conditions of every accepted deed. The Qurʾān '
    'says it three times — «رَبُّنَا اللهُ ثُمَّ اسْتَقَامُوا». <em>Say it of a '
    'man and mean the revealed word: not “committed,” but '
    '<strong>upright</strong> — and then keep inspecting whether you still '
    'are.</em>')

b += B.nav('h20-idha-lam-tastahi.html', 'Ḥadīth 20 · إِذَا لَمْ تَسْتَحِ',
           'index.html', 'Mark complete · أَتْمَمْتَ الدَّرْس · Hadeeth Hub',
           'hd-h21')

B.write('h21-qul-amantu.html',
        'قُلْ آمَنْتُ بِاللهِ ثُمَّ اسْتَقِمْ',
        'Say “I Believe in Allah,” Then Be Steadfast',
        'Ḥadīth 21 of al-Nawawī’s Forty (Sufyān ibn ʿAbdillāh al-Thaqafī, '
        'Muslim) with the sharḥ of Ibn ʿUthaymīn: the whole religion in two '
        'words. The kind of statement Sufyān asked for; «آmantu billāh» as the '
        'heart’s affirmation of tawḥīd and «istaqim» as going straight on the '
        'sharīʿah; how the two words gather the two conditions of worship '
        '(ikhlāṣ + mutābaʿah); the three āyāt that witness to it (al-Aḥqāf '
        '46:13, Fuṣṣilat 41:30, Hūd 11:112); the correction of «multazim» to '
        '«mustaqīm»; and istiqāmah as a rule of self-inspection.',
        21, 'Muslim', '2', b)
print('wrote h21-qul-amantu.html')
