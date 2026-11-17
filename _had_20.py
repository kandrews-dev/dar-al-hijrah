# -*- coding: utf-8 -*-
"""Ḥadīth 20 — «إِنَّ مِمَّا أَدْرَكَ النَّاسُ مِنْ كَلَامِ النُّبُوَّةِ
الأُولَى: إِذَا لَمْ تَسْتَحِ فَاصْنَعْ مَا شِئْتَ». Abū Masʿūd al-Badrī,
al-Bukhārī. Sharḥ of Ibn ʿUthaymīn, printed folios 230–234 (markers 231–235,
offset −1).

The ḥadīth of ḥayāʾ. The Shaykh parses the sentence, gives the two readings of
«إِذَا لَمْ تَسْتَحِ», then draws the fawāʾid: what reaches us from the earlier
prophethood and the three categories it divides into, the story of Dāwūd against
the slander of Banū Isrāʾīl, the praise of ḥayāʾ and its two divisions, and the
refutation of the Jabriyyah.

Rule 8: the ḥadīth is in Ṣaḥīḥ al-Bukhārī (Kitāb al-Adab), so ṣaḥīḥ; the
supporting «الحَيَاءُ شُعْبَةٌ مِنَ الإِيمَان» is muttafaq ʿalayh (al-Bukhārī &
Muslim) as the sharḥ names it — named attributions, no grading invented.
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
    'Say who narrated this ḥadīth and where it is reported, and parse the '
    'sentence «%s» — where its khabar and its ism fall.'
    % ar('إِنَّ مِمَّا أَدْرَكَ النَّاس'),
    'Give the two readings of «%s» — the one that returns to the doer and the '
    'one that returns to the act.' % ar('إِذَا لَمْ تَسْتَحِ فَاصْنَعْ مَا شِئْت'),
    'State the three categories into which what is transmitted from the earlier '
    'prophethood divides, and the ruling on each.',
    'Use the story of Dāwūd to tell the slander of Banū Isrāʾīl from the real '
    'lesson of the āyāt.',
    'Give the two divisions of ḥayāʾ — by object and by origin — and the one '
    'case in which ḥayāʾ is blameworthy.',
])

b += B.provenance(230, 234)

b += B.hadith_block(
    'عَنْ أَبِي مَسْعُودٍ عُقْبَةَ بْنِ عَمْرٍو الأَنْصَارِيِّ البَدْرِيِّ '
    'رَضِيَ اللهُ عَنْهُ قَالَ: قَالَ رَسُولُ اللهِ ﷺ: «إِنَّ مِمَّا أَدْرَكَ '
    'النَّاسُ مِنْ كَلَامِ النُّبُوَّةِ الأُولَى: إِذَا لَمْ تَسْتَحِ فَاصْنَعْ '
    'مَا شِئْتَ». رَوَاهُ البُخَارِيُّ.',
    'Abū Masʿūd ʿUqbah ibn ʿAmr al-Anṣārī al-Badrī (may Allah be pleased with '
    'him) said: The Messenger of Allah ﷺ said: "Among what people have grasped '
    'from the words of the earliest prophethood is: If you feel no shame, then '
    'do as you wish." Narrated by al-Bukhārī.',
    'Narrated by Abū Masʿūd al-Badrī · رَوَاهُ البُخَارِيُّ — al-Bukhārī, in his '
    'Ṣaḥīḥ (Kitāb al-Adab), so the ḥadīth is ṣaḥīḥ.')

# ------------------------------------------------------------------ §1
b += B.heading('«إِنَّ مِمَّا أَدْرَكَ النَّاس»', 'Reading the Sentence')
b += p('<strong>The sentence is built so that its subject is a saying.</strong> '
       '<em>«%s» is for emphasis; its khabar comes first — «%s» — and its ism '
       'is the quoted saying that follows: «%s», reported as speech. The sense '
       'is: <strong>among what people grasped from the words of the earliest '
       'prophethood is this saying.</strong></em>'
       % (ar('إِنَّ'), ar('مِمَّا أَدْرَكَ النَّاس'),
          ar('إِذَا لَمْ تَسْتَحِ فَاصْنَعْ مَا شِئْت')))
b += p('<em>«%s» — the «%s» is for <strong>partition</strong>: <em>some</em> of '
       'what people grasped, not all of it.</em> <em>And «%s» means the '
       '<strong>earlier</strong> prophethood — the prophets who came before — '
       'for this word reached the people and was passed down among them.</em>'
       % (ar('مِمَّا'), ar('مِنْ'), ar('النُّبُوَّةِ الأُولَى')))

# ------------------------------------------------------------------ §2
b += B.heading('مَا هُوَ الحَيَاء؟', 'What Ḥayāʾ Is')
b += box(
    '<p style="margin:0;font-size:.94rem"><strong>Ḥayāʾ</strong> is <em>a '
    'reaction that arises in a person at doing what does not befit him and does '
    'not adorn him</em> — he recoils within himself, and shame results. It is '
    'the inner brake that holds a person back from the ugly.</p>')

# ------------------------------------------------------------------ §3
b += B.heading('«إِذَا لَمْ تَسْتَحِ فَاصْنَعْ مَا شِئْت»', 'The Two Readings')
b += p('<strong>The words carry two meanings, and the Shaykh keeps both.</strong> '
       'On one, the command is really a <em>statement</em> and a reproach; on '
       'the other, it is a genuine <em>permission</em>. The difference is '
       'whether the clause looks at the <strong>doer</strong> or at the '
       '<strong>act</strong>.')
b += table([
    row('المَعْنَى الأَوَّل · returns to the <strong>doer</strong>',
        '<em>If you have no ḥayāʾ, you do whatever you want.</em> Here the '
        'imperative stands in the place of a <strong>statement</strong>, and it '
        'is <strong>blame</strong> (ذَمّ): a man with no shame does what harms '
        'murūʾah and what does not, caring for nothing.'),
    row('المَعْنَى الثَّانِي · returns to the <strong>act</strong>',
        '<em>If the act is not something to be ashamed of, then do it and do '
        'not mind.</em> Here the imperative is for <strong>permissibility</strong> '
        '(إِبَاحَة): whatever carries no shame in it, there is no blame in '
        'doing — so do not leave it out of a false shame.'),
])

# ------------------------------------------------------------------ §4
b += B.heading('مَا يَبْقَى مِنَ الأُمَمِ السَّابِقَة', 'What Reaches Us From Earlier Nations')
b += p('<strong>First benefit:</strong> <em>reports of the earlier nations may '
       'remain into this ummah</em> — which is exactly what the ḥadīth says: '
       'that this word was grasped «%s». What reaches us travels one of three '
       'roads: by revelation in the <strong>Qurʾān</strong>, by the '
       '<strong>Sunnah</strong>, or by what people <strong>pass down</strong>. '
       'And the Qurʾān itself points to the earliest scriptures:'
       % ar('مِنْ كَلَامِ النُّبُوَّةِ الأُولَى'))
b += B.ayah(
    'إِنَّ هَٰذَا لَفِي الصُّحُفِ الْأُولَىٰ * صُحُفِ إِبْرَاهِيمَ وَمُوسَىٰ',
    'Indeed, this is in the former scriptures — the scriptures of Ibrāhīm and '
    'Mūsā.',
    'سُورَةُ الأَعْلَى · 87:18–19')
b += p('<strong>But what is passed down from the earlier prophethood is not all '
       'of one rank.</strong> <em>The Shaykh divides it into three, and this '
       'division is the justice (العَدْل) in dealing with it:</em>')
b += table([
    row('١ · شَهِدَ شَرْعُنَا بِصِحَّتِه',
        '<em>What our own sharīʿah testifies is true</em> — then it is '
        '<strong>ṣaḥīḥ, accepted</strong> (صَحِيحٌ مَقْبُول).'),
    row('٢ · شَهِدَ شَرْعُنَا بِبُطْلَانِه',
        '<em>What our sharīʿah testifies is false</em> — then it is '
        '<strong>bāṭil, rejected</strong> (بَاطِلٌ مَرْدُود).'),
    row('٣ · لَمْ يَرِدْ شَرْعُنَا بِتَأْيِيدٍ وَلَا تَفْنِيد',
        '<em>What our sharīʿah neither confirms nor denies</em> — then we '
        '<strong>withhold</strong> (نَتَوَقَّفُ فِيه); there is no harm in '
        'mentioning it in admonition, but it is neither believed nor '
        'denied.'),
])

# ------------------------------------------------------------------ §5
b += B.heading('قِصَّةُ دَاوُدَ عَلَيْهِ السَّلَام', 'The Story of Dāwūd — Slander and Truth')
b += p('<strong>A worked example of the third category.</strong> <em>Banū '
       'Isrāʾīl told of Dāwūd ﷺ a vile tale — that he coveted the wife of one '
       'of his soldiers and sent the man to the front to be killed so he could '
       'take her.</em> <strong>This is a lie</strong>: it does not occur from '
       'the common of people, let alone a prophet; it contradicts the ʿiṣmah of '
       'the prophets and the justice they were sent with. <em>What contradicts '
       'the prophets’ protection and character, we know to be false.</em>')
b += p('<strong>So what did the āyāt really tell?</strong> <em>Two disputants '
       'climbed the wall of his prayer-chamber and startled him; one said the '
       'other had ninety-nine ewes to his one, and had pressured him in '
       'speech:</em>')
b += B.ayah(
    'إِنَّ هَٰذَا أَخِي لَهُ تِسْعٌ وَتِسْعُونَ نَعْجَةً وَلِيَ نَعْجَةٌ '
    'وَاحِدَةٌ',
    'Indeed this is my brother; he has ninety-nine ewes, and I have one ewe.',
    'سُورَةُ ص · Ṣād 38:23')
b += p('<em>Dāwūd answered at once that the man had wronged him — and in that '
       'lay the test, for a judge may not rule by one party’s word before '
       'hearing the other:</em>')
b += B.ayah(
    'لَقَدْ ظَلَمَكَ بِسُؤَالِ نَعْجَتِكَ إِلَىٰ نِعَاجِهِ',
    'He has certainly wronged you in demanding your ewe [to add] to his ewes.',
    'سُورَةُ ص · Ṣād 38:24')
b += box(
    '<p style="margin:0 0 .5rem;font-size:.94rem"><strong>The real matter the '
    'āyāt point to was a slip in three things, not the lie of Banū '
    'Isrāʾīl:</strong></p>'
    '<p style="margin:0;font-size:.92rem">(1) He <strong>secluded himself</strong> '
    'in his chamber away from judging between the people, though Allah had made '
    'him a khalīfah to rule. (2) He <strong>locked the door</strong>, forcing '
    'the disputants to climb the wall, with the risk of harm. (3) He '
    '<strong>ruled for one before hearing the other</strong>. So he knew Allah '
    'had tested him — «%s» — and he sought forgiveness, bowed, and turned back '
    'to Allah.</p>'
    % ar('وَظَنَّ دَاوُودُ أَنَّمَا فَتَنَّاهُ فَاسْتَغْفَرَ رَبَّهُ وَخَرَّ '
         'رَاكِعًا وَأَنَاب'))
b += B.ayah(
    'وَظَنَّ دَاوُودُ أَنَّمَا فَتَنَّاهُ فَاسْتَغْفَرَ رَبَّهُ وَخَرَّ '
    'رَاكِعًا وَأَنَابَ',
    'And Dāwūd realised that We had tried him, so he asked forgiveness of his '
    'Lord and fell down bowing and turned in repentance.',
    'سُورَةُ ص · Ṣād 38:24')

# ------------------------------------------------------------------ §6
b += B.heading('الثَّنَاءُ عَلَى الحَيَاء', 'The Praise of Ḥayāʾ, and Its Divisions')
b += p('<strong>On either reading, the ḥadīth praises ḥayāʾ</strong> — the '
       'Prophet ﷺ affirmed: «%s». <em>And ḥayāʾ divides two ways.</em>'
       % ar('الحَيَاءُ شُعْبَةٌ مِنَ الإِيمَان'))
b += p('<strong>First, by what it is owed to:</strong>')
b += table([
    row('حَيَاءٌ مِنَ الله',
        '<em>Toward the right of Allah:</em> that you be ashamed for Allah to '
        'see you where He forbade you, or to miss you where He commanded '
        'you.'),
    row('حَيَاءٌ مِنَ الخَلْق',
        '<em>Toward creation:</em> that you refrain from all that breaks '
        'murūʾah and good character. In a gathering of knowledge, a man in the '
        'front row stretching out his legs is no ḥayāʾ — it breaks murūʾah; yet '
        'among his friends it does not, though to ask leave is better.'),
])
b += p('<strong>Second, by where it comes from:</strong>')
b += table([
    row('غَرِيزِيٌّ طَبِيعِيّ',
        '<em>Innate</em> — Allah grants some people ḥayāʾ from childhood; they '
        'speak and act only at need. <strong>This is the better of the two.</strong>'),
    row('مُكْتَسَب',
        '<em>Acquired</em> — a bold person trains himself and keeps the company '
        'of people of ḥayāʾ and goodness, and takes it from them.'),
])
b += box(
    '<p style="margin:0;font-size:.94rem"><strong>One limit on the praise:</strong> '
    '<em>ḥayāʾ is a praised character <strong>except when it prevents an '
    'obligation or drives one into the forbidden.</strong></em> If shyness '
    'keeps a man from forbidding an evil he is obliged to forbid, that is '
    '<strong>blameworthy</strong> ḥayāʾ — forbid the evil and do not mind, by '
    'its proper levels and conditions. The praised ḥayāʾ is the one that never '
    'drops a duty and never falls into a ḥarām.</p>',
    wash='var(--gold-pale)', edge='var(--gold-warm)')

# ------------------------------------------------------------------ §7
b += B.heading('الرَّدُّ عَلَى الجَبْرِيَّة', 'A Refutation of the Jabriyyah')
b += p('<strong>A last benefit, from the single word «%s».</strong> <em>The '
       'servant is addressed with a real will of his own — «do as you '
       '<strong>wish</strong>» — which affirms the servant’s mashīʾah and '
       'refutes the <strong>Jabriyyah</strong>, who claim a person is compelled '
       'in his deeds with no will at all. He acts by his own choice, under the '
       'will of Allah.</em>' % ar('شِئْت'))

# ------------------------------------------------------------------ vocab
b += B.vocab([
    ('الحَيَاء', 'al-ḥayāʾ', 'modesty, a sense of shame', 'ح-ي-ي',
     'A reaction that arises at doing what does not befit a person, so he '
     'recoils — the inner brake from the ugly; a branch of faith',
     'الحَيَاءُ شُعْبَةٌ مِنَ الإِيمَان'),
    ('النُّبُوَّةُ الأُولَى', 'al-nubuwwa al-ūlā', 'the earlier prophethood', 'ن-ب-أ',
     'The prophets who came before; some of their words reached and were '
     'passed down among the people',
     'مِنْ كَلَامِ النُّبُوَّةِ الأُولَى'),
    ('مِمَّا', 'mimmā', 'part of what / some of what', 'م-ن',
     'The «مِنْ» here is for partition (التَّبْعِيض) — SOME of what people grasped, '
     'not all of it',
     'إِنَّ مِمَّا أَدْرَكَ النَّاس'),
    ('المُرُوءَة', 'al-murūʾa', 'manly virtue, propriety', 'م-ر-أ',
     'The dignity ḥayāʾ guards toward creation; stretching the legs in the '
     'front row of a lesson breaks it',
     'مَا يُخَالِفُ المُرُوءَةَ وَالأَخْلَاق'),
    ('يَتَوَقَّفُ فِيه', 'yatawaqqafu fīh', 'one withholds judgement on it', 'و-ق-ف',
     'The ruling on the third category — what our sharīʿah neither confirms nor '
     'denies; neither believed nor denied, and this is justice',
     'مَا لَمْ يَرِدْ شَرْعُنَا بِتَأْيِيدِهِ وَلَا تَفْنِيدِهِ يُتَوَقَّفُ فِيه'),
    ('الصُّحُفُ الأُولَى', 'al-ṣuḥuf al-ūlā', 'the former scriptures', 'ص-ح-ف',
     'The scriptures of Ibrāhīm and Mūsā — the Qurʾān’s own witness that earlier '
     'revelation reaches this ummah',
     'إِنَّ هَٰذَا لَفِي الصُّحُفِ الأُولَى'),
    ('شُعْبَةٌ مِنَ الإِيمَان', 'shuʿba min al-īmān', 'a branch of faith', 'ش-ع-ب',
     'How the Prophet ﷺ ranked ḥayāʾ — one of the branches of īmān, praised on '
     'either reading of the ḥadīth',
     'الحَيَاءُ شُعْبَةٌ مِنَ الإِيمَان'),
    ('الجَبْرِيَّة', 'al-jabriyya', 'the Jabriyyah (fatalists)', 'ج-ب-ر',
     'Those who claim the servant is compelled with no will; refuted by «فَاصْنَعْ '
     'مَا شِئْت», which affirms the servant’s mashīʾah',
     'فِيهِ الرَّدُّ عَلَى الجَبْرِيَّةِ بِإِثْبَاتِ المَشِيئَةِ لِلْعَبْد'),
])

# ------------------------------------------------------------------ MCQ
b += B.mcq('hd-h20', [
    ('Who narrated this ḥadīth, and where is it reported?',
     ['Abū Hurayrah, in Muslim',
      'Abū Masʿūd ʿUqbah ibn ʿAmr al-Anṣārī al-Badrī, in al-Bukhārī',
      'Ibn ʿAbbās, in al-Tirmidhī',
      'Anas ibn Mālik, in Abū Dāwūd'], 1),
    ('In «إِنَّ مِمَّا أَدْرَكَ النَّاسُ…», what is the ism of «إِنَّ»?',
     ['The word «النَّاس»',
      'The quoted saying «إِذَا لَمْ تَسْتَحِ فَاصْنَعْ مَا شِئْت», reported as '
      'speech; its khabar «مِمَّا أَدْرَكَ النَّاس» comes first',
      'The word «كَلَام»',
      'There is no ism in the sentence'], 1),
    ('What does the «مِنْ» in «مِمَّا أَدْرَكَ النَّاس» indicate?',
     ['The start of a time',
      'Partition (التَّبْعِيض) — SOME of what people grasped, not all',
      'A cause',
      'An oath'], 1),
    ('What is ḥayāʾ, as the Shaykh defines it?',
     ['A weakness of character to be cured',
      'A reaction that arises at doing what does not befit a person, so he '
      'recoils — the inner brake from the ugly',
      'Silence in all gatherings',
      'Fear of people’s opinions only'], 1),
    ('On the FIRST reading of «إِذَا لَمْ تَسْتَحِ…», the clause returns to '
     'the ___ and is ___.',
     ['the act; permission',
      'the doer; blame (ذَمّ) — a shameless man does what harms murūʾah and '
      'what does not, the command standing for a statement',
      'the time; a command',
      'the ruler; praise'], 1),
    ('On the SECOND reading, the clause returns to the ___ and is ___.',
     ['the doer; blame',
      'the act; permissibility (إِبَاحَة) — what carries no shame, there is no '
      'blame in doing',
      'the Prophet; a miracle',
      'the scripture; abrogation'], 1),
    ('By what three roads does what preceded from earlier nations reach us?',
     ['Dreams, poetry, and inscriptions',
      'By the Qurʾān, by the Sunnah, or by what people pass down',
      'Only by the Qurʾān',
      'Only by Jewish and Christian books'], 1),
    ('What is the ruling on a report of the earlier prophethood that our '
     'sharīʿah neither confirms nor denies?',
     ['Accept it fully as true',
      'We withhold (نَتَوَقَّف) — neither believe nor deny it; no harm to '
      'mention it in admonition',
      'Reject it as certainly false',
      'It must be acted upon'], 1),
    ('What was the tale Banū Isrāʾīl told about Dāwūd ﷺ, and how is it judged?',
     ['A true account preserved in the Qurʾān',
      'A slander — that he contrived a soldier’s death to take his wife; it is '
      'a lie, contradicting the ʿiṣmah of the prophets',
      'A minor exaggeration that is accepted',
      'A matter to be withheld on'], 1),
    ('What was the real slip the āyāt of Ṣād point to in Dāwūd’s story?',
     ['That he committed the sin they alleged',
      'Three things: secluding himself from judging, locking the door, and '
      'ruling for one disputant before hearing the other',
      'That he refused to pray',
      'That he doubted his prophethood'], 1),
    ('What are the two divisions of ḥayāʾ BY ORIGIN, and which is better?',
     ['Public and private; public is better',
      'Innate/natural (غَرِيزِيّ) and acquired (مُكْتَسَب) — the innate is '
      'better',
      'Spoken and written; written is better',
      'Male and female; neither is better'], 1),
    ('When is ḥayāʾ blameworthy rather than praised?',
     ['Whenever it is felt before elders',
      'When it prevents an obligation or drives one into the forbidden — e.g. '
      'shyness that stops a man from forbidding an evil he must forbid',
      'It is never blameworthy',
      'Only when it is innate'], 1),
])

# ------------------------------------------------------------------ T/F
b += B.tf('hd-h20-tf', [
    ('الحَيَاءُ انْفِعَالٌ يَحْدُثُ لِلْإِنْسَانِ عِنْدَ فِعْلِ مَا لَا '
     'يُجَمِّلُهُ وَلَا يُزَيِّنُهُ.',
     'Ḥayāʾ is a reaction that arises in a person at doing what does not befit '
     'or adorn him.', True),
    ('«مِنْ» فِي «مِمَّا أَدْرَكَ النَّاس» لِلتَّبْعِيضِ، أَيْ بَعْضُ مَا '
     'أَدْرَكُوه.',
     'The «مِنْ» in «some of what people grasped» is for partition — part of '
     'what they grasped.', True),
    ('كُلُّ مَا يُنْقَلُ عَنِ النُّبُوَّةِ الأُولَى يُقْبَلُ وَيُصَدَّقُ بِهِ '
     'عَلَى كُلِّ حَال.',
     'Everything transmitted from the earlier prophethood is accepted and '
     'believed in every case.', False),
    ('مَا شَهِدَ شَرْعُنَا بِبُطْلَانِهِ مِنْ أَخْبَارِ الأُمَمِ فَهُوَ '
     'بَاطِلٌ مَرْدُود.',
     'What our sharīʿah testifies to be false, of the reports of the nations, '
     'is false and rejected.', True),
    ('مَا رَوَتْهُ بَنُو إِسْرَائِيلَ عَنْ دَاوُدَ مِمَّا يُنَافِي عِصْمَةَ '
     'الأَنْبِيَاءِ نَعْلَمُ أَنَّهُ كَذِب.',
     'What Banū Isrāʾīl narrated about Dāwūd that contradicts the ʿiṣmah of the '
     'prophets, we know to be a lie.', True),
    ('يَجُوزُ لِلْحَاكِمِ أَنْ يَحْكُمَ بِقَوْلِ أَحَدِ الخَصْمَيْنِ قَبْلَ '
     'سَمَاعِ الآخَر.',
     'A judge may rule by the word of one of the two disputants before hearing '
     'the other.', False),
    ('الحَيَاءُ خُلُقٌ مَحْمُودٌ إِلَّا إِذَا مَنَعَ مِنْ وَاجِبٍ أَوْ '
     'أَوْقَعَ فِي مُحَرَّم.',
     'Ḥayāʾ is a praised character except when it prevents an obligation or '
     'drives one into the forbidden.', True),
])

b += B.memorize(
    'إِنَّ مِمَّا أَدْرَكَ النَّاسُ مِنْ كَلَامِ النُّبُوَّةِ الأُولَى: إِذَا '
    'لَمْ تَسْتَحِ فَاصْنَعْ مَا شِئْتَ',
    'A word so old it reached this ummah from the <strong>earliest '
    'prophethood</strong>. It carries two truths at once: <strong>if a man has '
    'no shame, he does whatever he wants</strong> — a reproach that returns to '
    'the doer; and <strong>whatever carries no shame, there is no blame in '
    'doing</strong> — a permission that returns to the act. Around it the Shaykh '
    'gathers the test of Dāwūd and the justice of hearing both sides, the '
    'praise of ḥayāʾ toward Allah and toward people, and — in «<strong>mā '
    'shiʾt</strong>» — the servant’s own will, against those who say he is '
    'compelled. <em>Ḥayāʾ is a branch of faith; keep the shame that keeps '
    'you.</em>')

b += B.nav('h19-ihfaz-allah.html', 'Ḥadīth 19 · احْفَظِ الله',
           'index.html', 'Mark complete · أَتْمَمْتَ الدَّرْس · Hadeeth Hub',
           'hd-h20')

B.write('h20-idha-lam-tastahi.html',
        'إِذَا لَمْ تَسْتَحِ فَاصْنَعْ مَا شِئْت',
        'If You Feel No Shame, Do as You Wish',
        'Ḥadīth 20 of al-Nawawī’s Forty (Abū Masʿūd al-Badrī, al-Bukhārī) with '
        'the sharḥ of Ibn ʿUthaymīn: the ḥadīth of ḥayāʾ. Parsing the sentence '
        'and its two readings — the shameless doer (reproach) and the act with '
        'no shame in it (permission); what reaches us from the earlier '
        'prophethood and the three categories it divides into (al-Aʿlā '
        '87:18–19); the story of Dāwūd against the slander of Banū Isrāʾīl and '
        'the justice of hearing both sides (Ṣād 38:23–24); the two divisions of '
        'ḥayāʾ — toward Allah and toward creation, innate and acquired — and the '
        'one case in which it is blameworthy; and a refutation of the Jabriyyah.',
        20, 'al-Bukhārī', '2', b)
print('wrote h20-idha-lam-tastahi.html')
