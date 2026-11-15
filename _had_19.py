# -*- coding: utf-8 -*-
"""Ḥadīth 19 — «يَا غُلَامُ إِنِّي أُعَلِّمُكَ كَلِمَاتٍ: احْفَظِ اللهَ
يَحْفَظْك...». Ibn ʿAbbās, al-Tirmidhī — ḥasan ṣaḥīḥ. Sharḥ of Ibn ʿUthaymīn,
printed folios 224–229 (PDF indices 225–230, offset −1).

One of the greatest aḥādīth — a whole manual of the tawḥīd of reliance,
taught by the Prophet ﷺ to a boy riding behind him. The lesson follows the
Shaykh clause by clause through the kalimāt, then the second riwāyah.

Structure:
  1. The setting — «يَا غُلَام», Ibn ʿAbbās a boy behind the Prophet ﷺ; and
     «أُعَلِّمُكَ كَلِمَات» as a drawing of attention before weighty words.
  2. «احْفَظِ اللهَ يَحْفَظْك» — guard His limits and you are guarded; most of
     all in your dīn (Muḥammad 47:17), and whoever squanders Allah is
     squandered (al-Ḥashr 59:19).
  3. «احْفَظِ اللهَ تَجِدْهُ تُجَاهَك» — find Him before you, guiding and
     guarding; al-Anfāl 8:64.
  4. «إِذَا سَأَلْتَ فَاسْأَلِ اللهَ، وَإِذَا اسْتَعَنْتَ فَاسْتَعِنْ بِاللهِ»
     — the heart of tawḥīd; asking and seeking aid of other than Allah is a
     deficiency in it; al-Naml 27:62.
  5. «لَوِ اجْتَمَعَتِ الأُمَّة...» — benefit and harm are only by what Allah
     wrote; «رُفِعَتِ الأَقْلَامُ وَجَفَّتِ الصُّحُف».
  6. The other riwāyah — «تَعَرَّفْ إِلَى اللهِ فِي الرَّخَاءِ يَعْرِفْكَ فِي
     الشِّدَّة»; «مَا أَخْطَأَكَ لَمْ يَكُنْ لِيُصِيبَك»; «النَّصْرُ مَعَ
     الصَّبْر» (Āl ʿImrān 3:140); «الفَرَجُ مَعَ الكَرْب»; «مَعَ العُسْرِ
     يُسْرًا» (al-Sharḥ 94:5–6).

Rule 8: al-Tirmidhī’s grading «حَسَنٌ صَحِيح» is carried on the matn line; the
second riwāyah is named as «غَيْرِ التِّرْمِذِيّ» the way the sharḥ names it,
with no grading of our own added to it.
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
    'Say who narrated this ḥadīth and how old he was, and what «%s» was '
    'meant to do before the words that followed.' % ar('أُعَلِّمُكَ كَلِمَات'),
    'Explain «%s» in both directions — what guarding Allah means, and what '
    'being guarded means.' % ar('احْفَظِ اللهَ يَحْفَظْك'),
    'Give the two clauses on asking and seeking aid, and the point of tawḥīd '
    'they establish.',
    'State what the ummah can and cannot do to a person, on «%s».'
    % ar('لَوِ اجْتَمَعَت'),
    'Give the meanings of the second riwāyah — knowing Allah in ease, and the '
    'three pairings of victory, relief and ease.',
])

b += B.provenance(224, 229)

b += B.hadith_block(
    'عَنْ أَبِي العَبَّاسِ عَبْدِ اللهِ بْنِ عَبَّاسٍ رَضِيَ اللهُ عَنْهُمَا '
    'قَالَ: كُنْتُ خَلْفَ النَّبِيِّ ﷺ يَوْمًا فَقَالَ: «يَا غُلَامُ، إِنِّي '
    'أُعَلِّمُكَ كَلِمَاتٍ: احْفَظِ اللهَ يَحْفَظْكَ، احْفَظِ اللهَ تَجِدْهُ '
    'تُجَاهَكَ، إِذَا سَأَلْتَ فَاسْأَلِ اللهَ، وَإِذَا اسْتَعَنْتَ فَاسْتَعِنْ '
    'بِاللهِ. وَاعْلَمْ أَنَّ الأُمَّةَ لَوِ اجْتَمَعَتْ عَلَى أَنْ '
    'يَنْفَعُوكَ بِشَيْءٍ لَمْ يَنْفَعُوكَ إِلَّا بِشَيْءٍ قَدْ كَتَبَهُ اللهُ '
    'لَكَ، وَإِنِ اجْتَمَعُوا عَلَى أَنْ يَضُرُّوكَ بِشَيْءٍ لَمْ يَضُرُّوكَ '
    'إِلَّا بِشَيْءٍ قَدْ كَتَبَهُ اللهُ عَلَيْكَ؛ رُفِعَتِ الأَقْلَامُ '
    'وَجَفَّتِ الصُّحُفُ». رَوَاهُ التِّرْمِذِيُّ وَقَالَ: حَدِيثٌ حَسَنٌ '
    'صَحِيحٌ.',
    'Ibn ʿAbbās (may Allah be pleased with them both) said: One day I was '
    'behind the Prophet ﷺ and he said: "O boy, I shall teach you some words: '
    'Guard Allah and He will guard you; guard Allah and you will find Him '
    'before you. When you ask, ask Allah; and when you seek help, seek the help '
    'of Allah. Know that if the whole nation were to gather to benefit you with '
    'something, they would not benefit you except with something Allah had '
    'already written for you; and if they gathered to harm you with something, '
    'they would not harm you except with something Allah had already written '
    'against you. The pens have been lifted and the pages have dried."',
    'Narrated by Ibn ʿAbbās · رَوَاهُ التِّرْمِذِيُّ — al-Tirmidhī, who said: a '
    'ḥasan ṣaḥīḥ ḥadīth. The grading named here is al-Tirmidhī’s own.')

# ------------------------------------------------------------------ §1
b += B.heading('«يَا غُلَام»', 'A Lesson Taught to a Boy')
b += p('<strong>Read the setting, because it is part of the teaching.</strong> '
       '<em>Ibn ʿAbbās was behind the Prophet ﷺ — riding with him or walking '
       'behind him — and he was a <strong>boy</strong>: the Prophet ﷺ passed '
       'away when Ibn ʿAbbās had barely reached puberty, around fifteen or '
       'less.</em> Into that young ear the Prophet ﷺ poured one of the '
       'greatest summaries of tawḥīd in the Sunnah.')
b += p('<em>And «%s» he said <strong>to make him attentive</strong>.</em> '
       '<strong>It is a sunnah of teaching:</strong> one who is about to say '
       'something weighty prefaces it with what draws the listener in — so the '
       'ear is ready before the words arrive.'
       % ar('إِنِّي أُعَلِّمُكَ كَلِمَات'))

# ------------------------------------------------------------------ §2
b += B.heading('«احْفَظِ اللهَ يَحْفَظْك»', 'Guard Allah, and He Will Guard You')
b += p('<strong>The first word, and it runs both ways.</strong> <em>«%s» — '
       'guard His limits and His sharʿ: by doing His commands and avoiding His '
       'prohibitions, and by learning of His religion what your worship and '
       'your dealings stand upon.</em> <em>«%s» — He guards you in your '
       'religion, your family, your wealth and your self, for Allah rewards '
       'the doers of good with His good.</em>'
       % (ar('احْفَظِ الله'), ar('يَحْفَظْك')))
b += box(
    '<p style="margin:0;font-size:.94rem"><strong>And the most important thing '
    'He guards is your religion.</strong> <em>He keeps you from deviation and '
    'misguidance — for the more a person is guided, the more Allah increases '
    'him in guidance.</em></p>')
b += B.ayah(
    'وَالَّذِينَ اهْتَدَوْا زَادَهُمْ هُدًى وَآتَاهُمْ تَقْوَاهُمْ',
    'And those who are guided — He increases them in guidance and grants them '
    'their taqwā.',
    'سُورَةُ مُحَمَّد · 47:17')
b += p('<strong>And the warning folded inside the promise:</strong> <em>one '
       'who does not guard Allah does not deserve that Allah guard him.</em> '
       'To squander the religion of Allah is to be left to oneself —')
b += B.ayah(
    'وَلَا تَكُونُوا كَالَّذِينَ نَسُوا اللَّهَ فَأَنسَاهُمْ أَنفُسَهُمْ',
    'And do not be like those who forgot Allah, so He made them forget '
    'themselves.',
    'سُورَةُ الحَشْر · 59:19')

# ------------------------------------------------------------------ §3
b += B.heading('«احْفَظِ اللهَ تَجِدْهُ تُجَاهَك»', 'Guard Allah, and You Will Find Him Before You')
b += p('<em>«%s» and «%s» are one meaning: you will find Allah '
       '<strong>before you</strong> — guiding you to every good, drawing you '
       'near, warding off every evil — especially when you have guarded Him by '
       '<strong>seeking His aid</strong>.</em> For when a person relies on '
       'Allah, Allah suffices him:'
       % (ar('تَجِدْهُ تُجَاهَك'), ar('تَجِدْهُ أَمَامَك')))
b += B.ayah(
    'يَا أَيُّهَا النَّبِيُّ حَسْبُكَ اللَّهُ وَمَنِ اتَّبَعَكَ مِنَ '
    'الْمُؤْمِنِينَ',
    'O Prophet, sufficient for you is Allah, and for whoever follows you of '
    'the believers.',
    'سُورَةُ الأَنْفَال · 8:64')

# ------------------------------------------------------------------ §4
b += B.heading('«إِذَا سَأَلْتَ فَاسْأَلِ اللهَ، وَإِذَا اسْتَعَنْتَ فَاسْتَعِنْ بِاللهِ»',
               'When You Ask, Ask Allah; When You Seek Help, Seek It of Allah')
b += p('<strong>Here is the heart of the ḥadīth, and the heart of tawḥīd.</strong> '
       '<em>If you have a need, do not ask any but Allah; and if you seek aid, '
       'seek it of none but Allah — for in His hand is the dominion of the '
       'heavens and the earth.</em>')
b += B.ayah(
    'أَمَّن يُجِيبُ الْمُضْطَرَّ إِذَا دَعَاهُ وَيَكْشِفُ السُّوءَ',
    'Is He [not best] who answers the distressed one when he calls upon Him '
    'and removes the evil?',
    'سُورَةُ النَّمْل · 27:62')
b += box(
    '<p style="margin:0 0 .5rem;font-size:.94rem"><strong>But what of asking a '
    'creature for what it can do?</strong> <em>If you ask a person for what is '
    'within his power, know that he is a <strong>means</strong> (sabab), and '
    'the One who brings it about (al-musabbib) is Allah — had He willed, He '
    'would have stopped that person from giving you. So lean on Allah, not on '
    'the means.</em></p>'
    '<p style="margin:0;font-size:.92rem">And these two clauses show that '
    'asking other than Allah is a <strong>deficiency in tawḥīd</strong> — '
    'which is why asking of other than Allah, in little or much, is disliked. '
    '<em>Even when Allah grants your need at the hand of a person, do not '
    'forget the One who made him the means.</em></p>')

# ------------------------------------------------------------------ §5
b += B.heading('«لَوِ اجْتَمَعَتِ الأُمَّة...»', 'Benefit and Harm Are Only by What Allah Has Written')
b += p('<strong>And the proof that steadies the heart against all people:</strong> '
       '<em>the whole nation, from its first to its last, could not benefit '
       'you with anything except what Allah had already written for you; nor '
       'harm you except with what He had already written against you.</em>')
b += box(
    '<p style="margin:0 0 .5rem;font-size:.94rem"><strong>So where does the '
    'benefit people bring you really come from?</strong> <em>From Allah in '
    'truth — for He is the One who wrote it for you.</em> This drives a person '
    'to <strong>lean on Allah alone</strong> and to turn his face from the '
    'creation, who own him neither harm nor benefit.</p>'
    '<p style="margin:0;font-size:.92rem">And if harm reaches you from '
    'someone, know Allah wrote it upon you — so be content with His decree. '
    '<em>There is no objection to your striving to repel the harm</em>, for '
    'Allah said that the recompense of a wrong is a like wrong; but your heart '
    'rests in His writing.</p>')
b += p('<strong>«%s»</strong> — <em>what Allah has written is finished: the '
       'pens have been raised and the pages have dried. There is no changing '
       'the words of Allah.</em> <strong>The ḥadīth that began by teaching a '
       'boy to guard Allah ends by anchoring him in the decree of '
       'Allah.</strong>'
       % ar('رُفِعَتِ الأَقْلَامُ وَجَفَّتِ الصُّحُف'))

# ------------------------------------------------------------------ §6
b += B.heading('الرِّوَايَةُ الأُخْرَى', 'The Other Narration')
b += p('<em>In the other wording come further words, each a counsel for '
       'hardship:</em>')
b += table([
    row('<span dir="rtl" lang="ar">تَعَرَّفْ إِلَى اللهِ فِي الرَّخَاءِ '
        'يَعْرِفْكَ فِي الشِّدَّة</span>',
        '<em>Fulfil the right of Allah in ease, health and wealth, and He '
        'will know you in hardship</em> — when health and riches fall away and '
        'your need is sharp, He acknowledges you by the good that went before.'),
    row('<span dir="rtl" lang="ar">مَا أَخْطَأَكَ لَمْ يَكُنْ '
        'لِيُصِيبَك</span>',
        '<em>What missed you was never to befall you, and what befell you was '
        'never to miss you</em> — the whole matter is in Allah’s hand, which '
        'is a comfort both when a thing you feared comes and when a thing you '
        'loved is lost.'),
    row('<span dir="rtl" lang="ar">النَّصْرُ مَعَ الصَّبْر</span>',
        '<em>Victory is with patience</em> — so a person bears up in order to '
        'attain it: patience upon obedience, away from sin, and over the '
        'painful decrees.'),
    row('<span dir="rtl" lang="ar">الفَرَجُ مَعَ الكَرْب</span>',
        '<em>Relief is with distress</em> — the more affairs press, the nearer '
        'the opening; the hardship is the sign relief is at hand.'),
])
b += p('<strong>And the third pairing the Qurʾān itself states twice over:</strong> '
       '<em>ease comes with hardship — indeed hardship is wrapped in two '
       'eases, one before and one after.</em>')
b += B.ayah(
    'فَإِنَّ مَعَ الْعُسْرِ يُسْرًا * إِنَّ مَعَ الْعُسْرِ يُسْرًا',
    'For indeed, with hardship comes ease. Indeed, with hardship comes ease.',
    'سُورَةُ الشَّرْح · 94:5–6')
b += p('<em>Ibn ʿAbbās said: one hardship will not overcome two eases.</em> '
       '<strong>So when affairs press hard upon you, take refuge in Allah, '
       'awaiting His relief and believing His promise.</strong>')

# ------------------------------------------------------------------ vocab
b += B.vocab([
    ('احْفَظِ الله', 'iḥfaẓi Llāh', 'guard Allah', 'ح-ف-ظ',
     'Guard His limits and His sharʿ — doing the commands, avoiding the '
     'prohibitions, and learning the dīn; and He guards you, above all in your '
     'religion',
     'احْفَظِ اللهَ يَحْفَظْك'),
    ('تُجَاهَك', 'tujāhak', 'before you, facing you', 'و-ج-ه',
     'Same sense as أَمَامَك — you find Allah ahead of you, guiding to every '
     'good and warding off every evil',
     'احْفَظِ اللهَ تَجِدْهُ تُجَاهَك'),
    ('المُضْطَرّ', 'al-muḍṭarr', 'the one in dire distress', 'ض-ر-ر',
     'The one whom none answers when he calls but Allah — the proof that '
     'asking is for Allah alone',
     'أَمَّن يُجِيبُ الْمُضْطَرَّ إِذَا دَعَاه'),
    ('السَّبَبُ وَالمُسَبِّب', 'al-sabab wa-l-musabbib',
     'the means and the Bringer-about', 'س-ب-ب',
     'When you ask a creature for what it can do, it is a sabab; the musabbib '
     '— the One who truly grants — is Allah',
     'هُوَ سَبَبٌ مِنَ الأَسْبَاب، وَالمُسَبِّبُ هُوَ الله'),
    ('نَقْصُ التَّوْحِيد', 'naqṣ al-tawḥīd', 'a deficiency in tawḥīd', 'ن-ق-ص',
     'What asking and seeking aid of other than Allah amounts to — hence '
     'asking of other than Allah is disliked, in little or much',
     'مِنْ نَقْصِ التَّوْحِيدِ أَنْ يَسْأَلَ الإِنْسَانُ غَيْرَ الله'),
    ('رُفِعَتِ الأَقْلَام', 'rufiʿat al-aqlām', 'the pens have been lifted',
     'ر-ف-ع',
     'What Allah wrote is finished — the pens raised, the pages dried; no '
     'changing the words of Allah',
     'رُفِعَتِ الأَقْلَامُ وَجَفَّتِ الصُّحُف'),
    ('تَعَرَّفْ إِلَى الله', 'taʿarraf ilā Llāh', 'make yourself known to Allah',
     'ع-ر-ف',
     'Fulfil His right in ease and health, and He knows you in hardship — the '
     'counsel of the second riwāyah',
     'تَعَرَّفْ إِلَى اللهِ فِي الرَّخَاءِ يَعْرِفْكَ فِي الشِّدَّة'),
    ('النَّصْرُ مَعَ الصَّبْر', 'al-naṣru maʿa al-ṣabr',
     'victory is with patience', 'ص-ب-ر',
     'One of three pairings of the second riwāyah, with «الفَرَجُ مَعَ '
     'الكَرْب» and «مَعَ العُسْرِ يُسْرًا» — hardship is the sign relief is '
     'near',
     'وَاعْلَمْ أَنَّ النَّصْرَ مَعَ الصَّبْر'),
])

# ------------------------------------------------------------------ MCQ
b += B.mcq('hd-h19', [
    ('Who narrated this ḥadīth, and what was notable about his age?',
     ['Abū Hurayrah, an elder Companion',
      'Ibn ʿAbbās, who was a boy — the Prophet ﷺ passed away when he had '
      'barely reached puberty',
      'ʿUmar ibn al-Khaṭṭāb',
      'Muʿādh ibn Jabal, a governor'], 1),
    ('What was «إِنِّي أُعَلِّمُكَ كَلِمَاتٍ» meant to do?',
     ['To test the boy’s memory',
      'To make him attentive — a sunnah of teaching: prefacing weighty words '
      'with what draws the listener in',
      'To shorten the lesson',
      'To command silence'], 1),
    ('What does «احْفَظِ اللهَ» mean, and what is the most important thing one '
     'is guarded in?',
     ['Memorise the Qurʾān; guarded in wealth',
      'Guard His limits and sharʿ — doing commands, avoiding prohibitions, '
      'learning the dīn; and the most important thing He guards is your '
      'RELIGION, from deviation',
      'Guard the mosque; guarded in health',
      'Defend Allah against His enemies; guarded in lineage'], 1),
    ('What is folded inside the promise «يَحْفَظْك»?',
     ['That everyone is guarded equally',
      'A warning: whoever does not guard Allah does not deserve that Allah '
      'guard him — to squander His religion is to be left to oneself',
      'That guarding is optional',
      'That only prophets are guarded'], 1),
    ('What do «إِذَا سَأَلْتَ فَاسْأَلِ اللهَ» and «إِذَا اسْتَعَنْتَ '
     'فَاسْتَعِنْ بِاللهِ» establish?',
     ['That one may ask anyone for anything',
      'The heart of tawḥīd: ask and seek aid of none but Allah; asking other '
      'than Allah is a deficiency in tawḥīd, hence disliked',
      'That asking is always forbidden',
      'That seeking help is only for the poor'], 1),
    ('If you ask a creature for what is within its power, how should you '
     'regard it?',
     ['As the true giver',
      'As a means (sabab) — the One who truly brings it about (al-musabbib) is '
      'Allah, who could have stopped that person from giving you',
      'As a partner with Allah',
      'As forbidden in every case'], 1),
    ('What can the whole ummah do to a person, gathered together?',
     ['Benefit or harm him however they wish',
      'Benefit him only with what Allah had already written for him, and harm '
      'him only with what Allah had already written against him',
      'Nothing at all under any circumstance',
      'Only harm, never benefit'], 1),
    ('What does «رُفِعَتِ الأَقْلَامُ وَجَفَّتِ الصُّحُفُ» mean?',
     ['That writing is forbidden',
      'That what Allah has written is finished — the pens raised, the pages '
      'dried; there is no changing the words of Allah',
      'That the scribes have gone to sleep',
      'That the record is renewed each day'], 1),
    ('Is striving to repel a harm that reaches you contrary to this ḥadīth?',
     ['Yes — one must accept all harm passively',
      'No — there is no objection to striving to repel it, for the recompense '
      'of a wrong is a like wrong; yet the heart rests in Allah’s writing',
      'Yes — repelling harm is a lack of trust',
      'Only scholars may repel harm'], 1),
    ('What does «تَعَرَّفْ إِلَى اللهِ فِي الرَّخَاءِ يَعْرِفْكَ فِي '
     'الشِّدَّةِ» counsel?',
     ['To seek Allah only in hardship',
      'To fulfil Allah’s right in ease, health and wealth — and He will know '
      'you in hardship by the good that went before',
      'To avoid ease and seek hardship',
      'That ease and hardship are the same'], 1),
    ('What are the three pairings of the second riwāyah?',
     ['Knowledge with action, fear with hope, patience with gratitude',
      'Victory with patience, relief with distress, and ease with hardship',
      'Wealth with zakāh, prayer with purity, fasting with charity',
      'Guidance with misguidance, light with darkness'], 1),
    ('How does Ibn ʿAbbās read «مَعَ العُسْرِ يُسْرًا», stated twice?',
     ['That hardship always wins',
      'That one hardship will not overcome two eases — the hardship is wrapped '
      'in an ease before and an ease after',
      'That ease is impossible',
      'That the two verses contradict'], 1),
])

# ------------------------------------------------------------------ T/F
b += B.tf('hd-h19-tf', [
    ('مَعْنَى «احْفَظِ اللهَ» حِفْظُ حُدُودِهِ وَشَرِيعَتِهِ بِفِعْلِ '
     'الأَوَامِرِ وَاجْتِنَابِ النَّوَاهِي.',
     'The meaning of «guard Allah» is guarding His limits and sharʿ by doing '
     'the commands and avoiding the prohibitions.', True),
    ('سُؤَالُ غَيْرِ اللهِ وَالاسْتِعَانَةُ بِهِ كَمَالٌ فِي التَّوْحِيد.',
     'Asking other than Allah and seeking its aid is a perfection in '
     'tawḥīd.', False),
    ('لَوِ اجْتَمَعَتِ الأُمَّةُ عَلَى نَفْعِكَ لَمْ يَنْفَعُوكَ إِلَّا '
     'بِمَا كَتَبَهُ اللهُ لَكَ.',
     'If the whole nation gathered to benefit you, they would benefit you only '
     'with what Allah had written for you.', True),
    ('لَا يَجُوزُ السَّعْيُ فِي دَفْعِ الضَّرَرِ الَّذِي كَتَبَهُ اللهُ.',
     'It is not permitted to strive to repel a harm that Allah has '
     'written.', False),
    ('النَّصْرُ مَعَ الصَّبْر، وَالفَرَجُ مَعَ الكَرْب، وَمَعَ العُسْرِ '
     'يُسْرٌ.',
     'Victory is with patience, relief with distress, and with hardship comes '
     'ease.', True),
    ('مَنْ لَمْ يَحْفَظِ اللهَ فَإِنَّهُ لَا يَسْتَحِقُّ أَنْ يَحْفَظَهُ '
     'الله.',
     'Whoever does not guard Allah does not deserve that Allah guard him.',
     True),
])

b += B.memorize(
    'احْفَظِ اللهَ يَحْفَظْكَ، احْفَظِ اللهَ تَجِدْهُ تُجَاهَكَ، إِذَا '
    'سَأَلْتَ فَاسْأَلِ اللهَ، وَإِذَا اسْتَعَنْتَ فَاسْتَعِنْ بِاللهِ',
    'A whole creed of reliance, taught to a boy riding behind the Prophet ﷺ. '
    '<strong>Guard Allah</strong> — His limits and His law — and He guards '
    'you, most of all in your religion. <strong>When you ask, ask Allah; when '
    'you seek help, seek it of Allah</strong> — for the creation, gathered '
    'from first to last, owns you neither a harm nor a benefit except by what '
    'He has already written, and the pens are lifted and the pages are dry. '
    '<em>Everything the believer leans on, in one breath, returned to the One '
    'who wrote it.</em>')

b += B.nav('h18-ittaqi-allah.html', 'Ḥadīth 18 · اتَّقِ اللهَ حَيْثُمَا كُنْت',
           'index.html', 'Mark complete · أَتْمَمْتَ الدَّرْس · Hadeeth Hub',
           'hd-h19')

B.write('h19-ihfaz-allah.html',
        'يَا غُلَامُ إِنِّي أُعَلِّمُكَ كَلِمَات',
        'O Boy, I Shall Teach You Some Words',
        'Ḥadīth 19 of al-Nawawī’s Forty (Ibn ʿAbbās, al-Tirmidhī — ḥasan '
        'ṣaḥīḥ) with the sharḥ of Ibn ʿUthaymīn: a whole manual of the tawḥīd '
        'of reliance, taught to a boy behind the Prophet ﷺ. Guarding Allah and '
        'being guarded — most of all in one’s religion (Muḥammad 47:17, '
        'al-Ḥashr 59:19); finding Him before you (al-Anfāl 8:64); the heart of '
        'tawḥīd — asking and seeking aid of none but Allah, with the creature '
        'as a means and Allah the Bringer-about (al-Naml 27:62); that the whole '
        'ummah can benefit or harm you only by what Allah has written, the pens '
        'lifted and the pages dried; and the second narration — knowing Allah '
        'in ease, and victory with patience, relief with distress, ease with '
        'hardship (al-Sharḥ 94:5–6).',
        19, 'al-Tirmidhī (ḥasan ṣaḥīḥ)', '2', b)
print('wrote h19-ihfaz-allah.html')
