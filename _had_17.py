# -*- coding: utf-8 -*-
"""Ḥadīth 17 — «إِنَّ اللهَ كَتَبَ الإِحْسَانَ عَلَى كُلِّ شَيْء». Shaddād ibn
Aws, رَوَاهُ مُسْلِم. Sharḥ of Ibn ʿUthaymīn, printed folios 209–218 (PDF
indices 210–219, Arabic-sharḥ offset −1).

The matn is short and the sharḥ is long, because the Shaykh takes «and when you
slaughter, slaughter well» as the door into the whole fiqh of dhabḥ. The lesson
holds both: the principle that iḥsān is written over everything, and the
detailed rulings the Shaykh hangs on «أَحْسِنُوا الذِّبْحَة».

Structure, following the sharḥ:
  1. «عَلَى كُلِّ شَيْء» — not «إِلَى»: iḥsān is in everything, not confined.
  2. The two examples and the difference between them — the killed is not made
     lawful by the killing (a harmful dog, a snake), the slaughtered is eaten.
  3. كِتَابَةٌ قَدَرِيَّة vs شَرْعِيَّة, and the precise point that in «وَهُوَ
     كُرْهٌ لَكُمْ» the pronoun returns to the fighting, not the decree — a man
     may hate the thing ruled, never the ruling.
  4. إِحْسَانُ القِتْلَة = following the sharʿ (the rājiḥ view), which answers
     the rajm objection; the easiest killing; qiṣāṣ as the exception.
  5. The four shurūṭ of dhabḥ hung on «أَحْسِنُوا الذِّبْحَة»: the slaughterer,
     the instrument (and why tooth and nail are excluded), إنهار الدم, and the
     tasmiyah — with the nasyān question and the «wasting wealth» objection.
  6. حَدُّ الشَّفْرَة and إِرَاحَةُ الذَّبِيحَة — and the close: even disciplining
     one’s family is under «أَحْسِنُوا».

Rule 8: every ḥadīth the Shaykh adduces is given with his own takhrīj — «ما
أنهر الدم» (al-Bukhārī & Muslim), «أما السن فعظم» (the same), شريطة الشيطان
(Abū Dāwūd & Aḥmad), «أمر أن تُحَدَّ الشفار» (Aḥmad). The page names the
collection as the sharḥ names it and adds no grading of its own.
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
    'Explain why the ḥadīth says iḥsān is written <strong>%s</strong> '
    'everything, not <em>toward</em> it — and what that one preposition '
    'settles.' % ar('عَلَى'),
    'Give the two examples the Prophet ﷺ struck, and the difference between '
    'killing and slaughtering.',
    'Distinguish <strong>%s</strong> from <strong>%s</strong>, and say to what '
    'the pronoun in «%s» returns.'
    % (ar('الكِتَابَةُ القَدَرِيَّة'), ar('الكِتَابَةُ الشَّرْعِيَّة'),
       ar('وَهُوَ كُرْهٌ لَكُم')),
    'State what <strong>إِحْسَانُ القِتْلَة</strong> is on the strongest view, '
    'and how that answers the objection about stoning; and name the one '
    'exception to killing in the easiest way.',
    'List the four conditions of a valid <strong>%s</strong>, and say why the '
    'tooth and the nail are excluded from the instrument.' % ar('ذَبْح'),
    'Answer the two hard questions: the one who <em>forgets</em> the tasmiyah, '
    'and the charge that ruling the animal unlawful «wastes people’s wealth».',
    'Give the duties of sharpening the blade and giving the animal rest — and '
    'how the ḥadīth reaches even the disciplining of one’s family.',
])

b += B.provenance(209, 218)

b += B.hadith_block(
    'عَنْ أَبِي يَعْلَى شَدَّادِ بْنِ أَوْسٍ رَضِيَ اللهُ عَنْهُ عَنْ رَسُولِ '
    'اللهِ ﷺ قَالَ: «إِنَّ اللهَ كَتَبَ الإِحْسَانَ عَلَى كُلِّ شَيْء؛ فَإِذَا '
    'قَتَلْتُمْ فَأَحْسِنُوا القِتْلَة، وَإِذَا ذَبَحْتُمْ فَأَحْسِنُوا '
    'الذِّبْحَة، وَلْيُحِدَّ أَحَدُكُمْ شَفْرَتَه، وَلْيُرِحْ ذَبِيحَتَه». '
    'رَوَاهُ مُسْلِم.',
    'Abū Yaʿlā Shaddād ibn Aws (may Allah be pleased with him) reported that '
    'the Messenger of Allah ﷺ said: "Allah has prescribed excellence (iḥsān) '
    'in all things. So when you kill, kill well; and when you slaughter, '
    'slaughter well. Let one of you sharpen his blade and let him spare his '
    'animal [suffering]."',
    'Narrated by Shaddād ibn Aws · رَوَاهُ مُسْلِم — Muslim, Kitāb al-Ṣayd '
    'wa-l-Dhabāʾiḥ')

# ------------------------------------------------------------------ §1
b += B.heading('«عَلَى كُلِّ شَيْء» — لَا «إِلَى»', 'Written “Upon” Everything, Not “Toward” It')
b += p('<strong>The sharḥ begins on a single preposition, and it is not a '
       'pedantry.</strong> <em>He said «%s» — upon every thing — and did '
       '<strong>not</strong> say «%s», toward every thing.</em>'
       % (ar('عَلَى كُلِّ شَيْء'), ar('إِلَى كُلِّ شَيْء')))
b += box(
    '<p style="margin:0;font-size:.95rem"><em>The meaning: that iḥsān is '
    '<strong>not particular to one appointed thing</strong> of life, but is '
    'in the whole of it — «%s».</em></p>'
    % ar('بَلْ هُوَ فِي جَمِيعِ الحَيَاة'))
b += p('<strong>And <em>kataba</em> here means He prescribed it, a firm '
       'legislation</strong> — «%s». So the ḥadīth is not describing a virtue '
       'that is nice to have; it is reporting a thing Allah has <em>written '
       'over</em> every act a person does, the grave and the small alike.'
       % ar('شَرَعَهُ شَرْعًا مُؤَكَّدًا'))

# ------------------------------------------------------------------ §2
b += B.heading('المِثَالَان: القَتْلُ وَالذَّبْح', 'The Two Examples — Killing and Slaughtering')
b += p('<em>Then he struck two examples</em> — «%s» — <em>and the difference '
       'between them is this:</em> that the <strong>killed</strong> is not '
       'made lawful <em>to eat</em> by the killing, while the '
       '<strong>slaughtered</strong> is.'
       % ar('فَإِذَا قَتَلْتُمْ... وَإِذَا ذَبَحْتُمْ'))
b += table([
    row('<span dir="rtl" lang="ar">القَتْل</span><br>'
        '<span style="font-size:.82rem;font-weight:400">killing</span>',
        '<em>What is killed because it must be — a harmful dog, a snake. It is '
        'not eaten; so <strong>«أَحْسِنِ القِتْلَة»</strong> means: take its '
        'life by the <strong>easiest</strong> means available to you.</em>'),
    row('<span dir="rtl" lang="ar">الذَّبْح</span><br>'
        '<span style="font-size:.82rem;font-weight:400">slaughtering</span>',
        '<em>What is slaughtered to be eaten. «أَحْسِنِ الذِّبْحَة» means: do '
        'it by <strong>everything in which there is iḥsān</strong> — which is '
        'why he went on: «%s».</em>' % ar('وَلْيُحِدَّ أَحَدُكُمْ شَفْرَتَه')),
])
b += p('<em>«%s» — let him sharpen his knife: whet it with a file or a stone '
       'until it cuts strongly, so the slaughter is quick. And «%s» — let him '
       'give his animal rest: pass the blade with strength and speed so its '
       'dying is brief.</em> <strong>Both clauses are about the animal’s ease, '
       'not the slaughterer’s convenience.</strong>'
       % (ar('وَلْيُحِدَّ أَحَدُكُمْ شَفْرَتَه'), ar('وَلْيُرِحْ ذَبِيحَتَه')))

# ------------------------------------------------------------------ §3
b += B.heading('كِتَابَةٌ قَدَرِيَّةٌ وَكِتَابَةٌ شَرْعِيَّة', 'Two Kinds of “Writing” — Decree and Law')
b += p('<strong>From «%s» the Shaykh draws that the command and the ruling '
       'belong to Allah — and that His “writing” is of two kinds.</strong>'
       % ar('إِنَّ اللهَ كَتَبَ'))
b += table([
    row('<span dir="rtl" lang="ar">قَدَرِيَّة</span><br>'
        '<span style="font-size:.82rem;font-weight:400">of the decree</span>',
        '<em>What <strong>must</strong> come to pass.</em> Its example is the '
        'promise of Allah in His Book that the righteous shall inherit the '
        'earth — a thing written that will be.'),
    row('<span dir="rtl" lang="ar">شَرْعِيَّة</span><br>'
        '<span style="font-size:.82rem;font-weight:400">of the law</span>',
        '<em>What is <strong>legislated</strong>, and <strong>may</strong> be '
        'done by the children of Ādam or may not.</em> As «%s» — fighting is '
        'written upon you — and «%s» — fasting is written upon you.'
        % (ar('كُتِبَ عَلَيْكُمُ القِتَال'), ar('كُتِبَ عَلَيْكُمُ الصِّيَام'))),
])
b += B.ayah(
    'وَلَقَدْ كَتَبْنَا فِي الزَّبُورِ مِن بَعْدِ الذِّكْرِ أَنَّ الْأَرْضَ '
    'يَرِثُهَا عِبَادِيَ الصَّالِحُونَ',
    'And We have already written in the Scripture, after the [earlier] '
    'mention, that the land shall be inherited by My righteous servants.',
    'سُورَةُ الأَنْبِيَاء · 21:105')
b += B.ayah(
    'كُتِبَ عَلَيْكُمُ الْقِتَالُ وَهُوَ كُرْهٌ لَّكُمْ',
    'Fighting has been prescribed for you, though it is hateful to you.',
    'سُورَةُ البَقَرَة · 2:216')
b += box(
    '<p style="margin:0;font-size:.95rem"><strong>And a precision not to be '
    'missed in «%s».</strong> <em>The pronoun in «%s» returns to '
    '<strong>the fighting</strong>, not to the writing — because the '
    'Companions رَضِيَ اللهُ عَنْهُمْ could not possibly hate an obligation of '
    'Allah; they hated the being-killed, yet fought.</em></p>'
    '<p style="margin:.6rem 0 0;font-size:.92rem"><strong>There is a '
    'difference between a man hating Allah’s ruling and hating the thing '
    'ruled.</strong> To dislike the hardship of a command while submitting to '
    'it is the believer’s state; to hate the command itself is another matter '
    'entirely. <em>The whole of the eighth nullifier’s «%s» distinction sits '
    'inside this one grammatical point.</em></p>'
    % (ar('وَهُوَ كُرْهٌ لَكُم'), ar('وَهُوَ'), ar('بُغْضٌ طَبِيعِيّ')))
b += B.ayah(
    'يَا أَيُّهَا الَّذِينَ آمَنُوا كُتِبَ عَلَيْكُمُ الصِّيَامُ',
    'O you who have believed, fasting has been prescribed for you.',
    'سُورَةُ البَقَرَة · 2:183')

# ------------------------------------------------------------------ §4
b += B.heading('إِحْسَانُ القِتْلَة', 'What “Killing Well” Actually Means')
b += p('<strong>The strongest view is exact, and it heads off a famous '
       'objection.</strong> <em>Killing well, on the rājiḥ view, is '
       '<strong>following the sharʿ in it</strong> — whether that turns out '
       'harder or easier.</em>')
b += box(
    '<p style="margin:0;font-size:.94rem"><strong>Why the precision '
    'matters:</strong> if «killing well» meant simply «by the gentlest '
    'physical means», the stoning of the adulterer (<em>%s</em>) would seem to '
    'violate the ḥadīth. But once إِحْسَان is defined as <strong>conformity '
    'to what Allah legislated</strong>, the difficulty falls away: the ḥadd '
    'prescribed by the sharʿ <em>is</em> the iḥsān in that case. <em>«%s».</em></p>'
    % (ar('رَجْمُ الزَّانِي'), ar('لَا يَرِدُ عَلَيْنَا')))
b += p('<em>Otherwise — where the sharʿ has not fixed the manner — one kills '
       'what may be killed by the <strong>easiest</strong> way.</em> A man '
       'harmed by a dog may kill it a dozen ways; he takes the lightest. '
       '<strong>The one exception is qiṣāṣ:</strong> there the offender is '
       'dealt with <em>as he did</em> — for Allah legislated the like of the '
       'crime in the penalty.')

# ------------------------------------------------------------------ §5
b += B.heading('شُرُوطُ الذَّبْحِ الأَرْبَعَة', 'The Four Conditions of a Valid Slaughter')
b += p('<strong>Here the short matn opens into fiqh.</strong> From «%s» the '
       'Shaykh hangs the conditions of a lawful slaughter — four of them.'
       % ar('فَأَحْسِنُوا الذِّبْحَة'))
b += table([
    row('<span dir="rtl" lang="ar">١ · الذَّابِح</span><br>'
        '<span style="font-size:.82rem;font-weight:400">the slaughterer</span>',
        '<em>He must be a <strong>Muslim or a person of the Book</strong>. The '
        'slaughter of an idolater is not lawful, nor an apostate’s — and so '
        'the slaughter of one who abandons the prayer is not lawful, for he is '
        'neither Muslim nor of the Book. Proof: «%s»; Ibn ʿAbbās said their '
        'food is <strong>what they slaughter</strong>.</em>'
        % ar('وَطَعَامُ الَّذِينَ أُوتُوا الكِتَابَ حِلٌّ لَكُم')),
    row('<span dir="rtl" lang="ar">٢ · الآلَة</span><br>'
        '<span style="font-size:.82rem;font-weight:400">the instrument</span>',
        '<em><strong>Anything that makes the blood flow</strong> — iron, '
        'silver, gold, stone, reed — «%s». Excluded are two: the '
        '<strong>tooth</strong> and the <strong>nail</strong>.</em>'
        % ar('مَا أَنْهَرَ الدَّمَ وَذُكِرَ اسْمُ اللهِ عَلَيْهِ فَكُل')),
    row('<span dir="rtl" lang="ar">٣ · إِنْهَارُ الدَّم</span><br>'
        '<span style="font-size:.82rem;font-weight:400">making blood flow</span>',
        '<em>By cutting the two <strong>wadajān</strong>, the thick vessels '
        'around the windpipe; being joined to the heart, their cutting drains '
        'the blood fast and the death is quick. The Prophet ﷺ forbade '
        '<strong>%s</strong> — the one left to die without its vessels '
        'severed.</em>' % ar('شَرِيطَةَ الشَّيْطَان')),
    row('<span dir="rtl" lang="ar">٤ · التَّسْمِيَة</span><br>'
        '<span style="font-size:.82rem;font-weight:400">naming Allah</span>',
        '<em>Saying the name of Allah at the slaughter — «%s». It is a '
        'condition; Allah stressed it: «%s».</em>'
        % (ar('بِسْمِ الله'),
           ar('وَلَا تَأْكُلُوا مِمَّا لَمْ يُذْكَرِ اسْمُ اللهِ عَلَيْهِ'))),
])
b += p('<strong>Why the tooth and the nail?</strong> Because the Prophet ﷺ '
       'gave the reason: <em>«%s»</em> — as for the tooth, it is a bone; and '
       'as for the nail, it is the knife of the Abyssinians. <em>From «it is a '
       'bone» some scholars took that <strong>no bone at all</strong> makes '
       'slaughter lawful (the <strong>%s</strong> — the ruling follows the '
       'general reason, not the single named thing); and the nail is excluded '
       'both as imitation of the non-Arabs and because, being joined to the '
       'body, making it a blade runs against the fiṭrah.</em>'
       % (ar('أَمَّا السِّنُّ فَعَظْمٌ، وَأَمَّا الظُّفُرُ فَمُدَى الحَبَشَة'),
          ar('عُمُومُ العِلَّة')))
b += B.ayah(
    'وَلَا تَأْكُلُوا مِمَّا لَمْ يُذْكَرِ اسْمُ اللَّهِ عَلَيْهِ وَإِنَّهُ '
    'لَفِسْقٌ',
    'And do not eat of that over which the name of Allah has not been '
    'mentioned, for indeed it is a grave disobedience.',
    'سُورَةُ الأَنْعَام · 6:121')

# ------------------------------------------------------------------ §6
b += B.heading('النِّسْيَانُ وَإِفْسَادُ الأَمْوَال', 'The One Who Forgets, and the Charge of Wasting Wealth')
b += p('<strong>Two hard questions the Shaykh raises against himself.</strong>')
b += p('<strong>First — what of one who <em>forgets</em> the tasmiyah?</strong> '
       '<em>The condition does not drop by forgetfulness</em> — just as a man '
       'who prayed in a state of ḥadath, forgetting, has not prayed validly. '
       '<em>But is he sinful?</em> No: «%s» is answered by Allah’s «%s». '
       '<strong>So he bears no sin for forgetting — yet the animal is still '
       'not eaten</strong>, because the ruling on the meat is one thing and '
       'the sin on the man is another. <em>(And were someone to eat of it in '
       'forgetfulness or ignorance, there is nothing upon him.)</em>'
       % (ar('رَبَّنَا لَا تُؤَاخِذْنَا إِن نَّسِينَا'),
          ar('قَدْ فَعَلْت')))
b += p('<strong>Second — does ruling the animal unlawful «waste people’s '
       'wealth»?</strong> <em>The answer: we did not waste it. A thing left '
       'for the command of Allah is not a loss but an obedience</em> — as we '
       'give the zakāh and do not call it loss. <em>And ruling it unlawful '
       'this once ensures the man «%s» — he will not forget again.</em>')
b += box(
    '<p style="margin:0;font-size:.93rem"><strong>The parallel the Shaykh '
    'draws is worth keeping.</strong> Some object to cutting the thief’s hand '
    'that «half the nation would be one-handed». <em>«You have just admitted '
    'half your nation are thieves — and had you cut one thief’s hand, '
    'thousands would have stopped.»</em> A penalty that looks harsh in the one '
    'case is what protects the many — and the same logic answers the '
    'forgotten tasmiyah.</p>')
b += p('<strong>One mercy in the law, though:</strong> <em>the animal '
       '<strong>not under control</strong> — a camel that bolts, one fallen '
       'in a well beyond reach — is made lawful by a wound in <em>any</em> '
       'part of its body.</em> Where the throat cannot be reached, Allah does '
       'not burden the slaughterer with reaching it.')

# ------------------------------------------------------------------ §7
b += B.heading('حَدُّ الشَّفْرَةِ وَإِرَاحَةُ الذَّبِيحَة', 'Sharpening the Blade, and Giving Rest')
b += p('<strong>Back to the animal’s ease, which is where the matn ends.</strong> '
       'Sharpening the blade is a duty, because it is easier on the animal; '
       'one who slaughters with a dull blade — though the cut be valid and the '
       'meat lawful — <em>is sinful for not having sharpened it</em>.')
b += p('<em>And he must <strong>not sharpen the blade before the animal</strong>, '
       'because the Prophet ﷺ «%s» — ordered that blades be sharpened and '
       '<strong>hidden from the animals</strong>; for the animal knows, and '
       'has been seen to flee the slaughter in fear when the knife is whetted '
       'before it.</em>'
       % ar('أَمَرَ أَنْ تُحَدَّ الشِّفَارُ وَأَنْ تُوَارَى عَنِ البَهَائِم'))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.94rem"><strong>Giving the animal '
    'rest</strong> is by the <em>speed</em> of the slaughter, and by how it is '
    'held: <em>leave its legs free and place your foot on the side of its neck '
    'so it cannot rise — this is easier on it, and drains the blood more '
    'fully, since the movement helps the blood out.</em></p>'
    '<p style="margin:0;font-size:.92rem">What some do — kneeling on the sheep '
    'and pinning its limbs — <em>is a torment to it</em>; and breaking its '
    'neck before it dies, to hasten death, <strong>is not allowed</strong>, '
    'for there is severe pain in it and no need. <em>«%s».</em></p>'
    % ar('نَنْتَظِرُ حَتَّى يَخْرُجَ الدَّم'))
b += p('<strong>And the Shaykh ends where the ḥadīth began — «upon every '
       'thing».</strong> <em>Even the disciplining of one’s family falls under '
       '«%s»:</em> the Prophet ﷺ said in the Farewell Pilgrimage, of '
       'correcting them, «%s» — a striking that is <strong>not '
       'severe</strong>. <em>Discipline with iḥsān, not with violence; and the '
       'fuqahāʾ said that one who beats his child to excess and he dies is '
       'liable, while ordinary correction without violence carries no '
       'liability.</em> <strong>The ḥadīth that opened on a sharpened blade '
       'closes on a raised hand — and the measure in both is the same.</strong>'
       % (ar('أَحْسِنُوا'), ar('ضَرْبًا غَيْرَ مُبَرِّح')))

# ------------------------------------------------------------------ vocab
b += B.vocab([
    ('الإِحْسَان', 'al-iḥsān', 'excellence, doing well', 'ح-س-ن',
     'Written by Allah «عَلَى كُلِّ شَيْء» — upon everything, not confined to '
     'one act; here, the beautiful performance of whatever one does',
     'إِنَّ اللهَ كَتَبَ الإِحْسَانَ عَلَى كُلِّ شَيْء'),
    ('كَتَبَ', 'kataba', 'He prescribed / wrote', 'ك-ت-ب',
     'Of two kinds: قَدَرِيَّة (what must be) and شَرْعِيَّة (what is '
     'legislated and may or may not be done)',
     'كَتَبَ الإِحْسَانَ... أَيْ شَرَعَهُ شَرْعًا مُؤَكَّدًا'),
    ('القِتْلَة', 'al-qitlah', 'the manner of killing', 'ق-ت-ل',
     'The way a thing is killed; «أَحْسِنُوا القِتْلَة» = follow the sharʿ in '
     'it, else by the easiest means',
     'فَإِذَا قَتَلْتُمْ فَأَحْسِنُوا القِتْلَة'),
    ('الذِّبْحَة', 'al-dhibḥah', 'the manner of slaughter', 'ذ-ب-ح',
     'The way an animal is slaughtered for eating; governed by four shurūṭ '
     'the Shaykh hangs on «أَحْسِنُوا الذِّبْحَة»',
     'وَإِذَا ذَبَحْتُمْ فَأَحْسِنُوا الذِّبْحَة'),
    ('الشَّفْرَة', 'al-shafrah', 'the blade, the knife', 'ش-ف-ر',
     'To be sharpened — but not before the animal, and hidden from it; a dull '
     'blade makes the slaughterer sinful though the meat is lawful',
     'وَلْيُحِدَّ أَحَدُكُمْ شَفْرَتَه'),
    ('إِنْهَارُ الدَّم', 'inhār al-dam', 'making the blood flow', 'ن-ه-ر',
     'The third condition: cutting the two wadajān so the blood drains and '
     'death is quick; against شَرِيطَةُ الشَّيْطَان',
     'مَا أَنْهَرَ الدَّمَ وَذُكِرَ اسْمُ اللهِ عَلَيْهِ فَكُل'),
    ('الوَدَجَان', 'al-wadajān', 'the two jugular vessels', 'و-د-ج',
     'The thick vessels around the windpipe, joined to the heart; severing '
     'them drains the blood swiftly',
     'يَكُونُ إِنْهَارُ الدَّمِ بِقَطْعِ الوَدَجَيْن'),
    ('عُمُومُ العِلَّة', 'ʿumūm al-ʿillah', 'the generality of the reason',
     'ع-ل-ل',
     'That a ruling follows its stated reason, not the single named instance '
     '— «أَمَّا السِّنُّ فَعَظْمٌ» excludes all bone, not the tooth alone',
     'العِلَّةُ أَعَمُّ مِنَ المُعَيَّنِ وَهُوَ المَعْلُول'),
])

# ------------------------------------------------------------------ MCQ
b += B.mcq('hd-h17', [
    ('Why does the ḥadīth say iḥsān is written «عَلَى كُلِّ شَيْء» and not '
     '«إِلَى كُلِّ شَيْء»?',
     ['There is no difference; the prepositions are interchangeable',
      'To show iḥsān is not confined to one appointed thing of life but is in '
      'the whole of it — it is written UPON everything',
      'To restrict iḥsān to acts of worship',
      'Because إِلَى is grammatically forbidden here'], 1),
    ('What is the difference between القَتْل and الذَّبْح in the ḥadīth?',
     ['There is none',
      'The killed is not made lawful to eat by the killing (a harmful dog, a '
      'snake) — killed by the easiest means; the slaughtered is eaten, by '
      'everything in which there is iḥsān',
      'Killing is for animals, slaughter for people',
      'Slaughter is always forbidden'], 1),
    ('Distinguish كِتَابَة قَدَرِيَّة from شَرْعِيَّة.',
     ['Qadariyyah is for prophets, sharʿiyyah for everyone',
      'Qadariyyah is what must come to pass (the righteous inheriting the '
      'earth); sharʿiyyah is what is legislated and may or may not be done '
      '(fighting, fasting)',
      'They are the same thing',
      'Sharʿiyyah must occur; qadariyyah may not'], 1),
    ('In «كُتِبَ عَلَيْكُمُ القِتَالُ وَهُوَ كُرْهٌ لَكُمْ», to what does the '
     'pronoun in «وَهُوَ» return, and why does it matter?',
     ['To the writing — the Companions hated the obligation',
      'To the FIGHTING — the Companions could not hate an obligation of Allah; '
      'they hated the being-killed, not the ruling. A man may hate the thing '
      'ruled, never the ruling itself',
      'To Allah',
      'To the believers'], 1),
    ('What is إِحْسَانُ القِتْلَة on the strongest view, and how does it '
     'answer the objection about stoning?',
     ['The gentlest physical means always — so stoning would indeed violate it',
      'Following the sharʿ in it, harder or easier — so the legislated ḥadd of '
      'stoning IS the iḥsān in that case, and the objection falls',
      'Killing as quickly as possible regardless of the sharʿ',
      'It has no bearing on stoning'], 1),
    ('What is the one exception to killing by the easiest means?',
     ['Slaughtering for food',
      'Qiṣāṣ — there the offender is dealt with AS he did, for Allah '
      'legislated the like of the crime in the penalty',
      'Killing a snake',
      'There is no exception'], 1),
    ('Whose slaughter is lawful — and whose is not — under the first '
     'condition?',
     ['Anyone’s slaughter is lawful',
      'A Muslim’s or a Person of the Book’s is lawful; an idolater’s, an '
      'apostate’s — and so one who abandons the prayer’s — is not, for he is '
      'neither Muslim nor of the Book',
      'Only a scholar may slaughter',
      'Only an Arab’s slaughter is lawful'], 1),
    ('Why are the tooth and the nail excluded from the instrument of '
     'slaughter?',
     ['Because they are too weak to cut',
      'The Prophet ﷺ gave the reason — «the tooth is a bone, and the nail is '
      'the knife of the Abyssinians»: from «it is a bone» some took that no '
      'bone makes slaughter lawful (ʿumūm al-ʿillah), and the nail is '
      'imitation of the non-Arabs and against the fiṭrah',
      'Because they carry disease',
      'Because they are not sharp enough to make blood flow'], 1),
    ('What does إِنْهَارُ الدَّم require, and what is forbidden against it?',
     ['Draining all blood before death; nothing is forbidden',
      'Cutting the two wadajān around the windpipe so the blood drains fast; '
      'forbidden is شَرِيطَةُ الشَّيْطَان — the animal left to die without its '
      'vessels severed',
      'A single shallow cut; deep cuts are forbidden',
      'Breaking the neck first'], 1),
    ('What is the ruling on one who FORGETS the tasmiyah — on the meat, and on '
     'the man?',
     ['The meat is lawful and the man sinful',
      'The condition does not drop by forgetfulness, so the animal is not '
      'eaten; but the man bears no sin, for the ruling on the meat and the sin '
      'on the man are two different things',
      'Both the meat is unlawful and the man is sinful',
      'He must repeat the slaughter on the same animal'], 1),
    ('How does the Shaykh answer that ruling the animal unlawful «wastes '
     'people’s wealth»?',
     ['He concedes it is a loss but says it is necessary',
      'A thing left for the command of Allah is not loss but obedience — like '
      'the zakāh — and ruling it unlawful once ensures the man never forgets '
      'again; as cutting one thief’s hand stops thousands',
      'He allows eating it to avoid waste',
      'He says wealth is unimportant'], 1),
    ('How does the ḥadīth reach the disciplining of one’s family?',
     ['It does not; that is a separate topic',
      'Even correction falls under «أَحْسِنُوا» — the Prophet ﷺ allowed in the '
      'Farewell Pilgrimage only «ضَرْبًا غَيْرَ مُبَرِّح», a striking that is '
      'not severe; excess that kills brings liability',
      'It permits severe beating for discipline',
      'It forbids all discipline of family'], 1),
])

# ------------------------------------------------------------------ T/F
b += B.tf('hd-h17-tf', [
    ('الإِحْسَانُ مَكْتُوبٌ عَلَى كُلِّ شَيْء، لَيْسَ خَاصًّا بِشَيْءٍ '
     'مُعَيَّنٍ مِنَ الحَيَاة.',
     'Iḥsān is written upon everything, not particular to one appointed thing '
     'of life.', True),
    ('الضَّمِيرُ فِي «وَهُوَ كُرْهٌ لَكُمْ» يَعُودُ عَلَى الكِتَابَةِ لَا '
     'عَلَى القِتَال.',
     'The pronoun in «though it is hateful to you» returns to the writing, not '
     'to the fighting.', False),
    ('ذَبِيحَةُ تَارِكِ الصَّلَاةِ لَا تَحِلُّ، لِأَنَّهُ لَيْسَ مُسْلِمًا '
     'وَلَا كِتَابِيًّا.',
     'The slaughter of one who abandons the prayer is not lawful, for he is '
     'neither Muslim nor a Person of the Book.', True),
    ('يَحِلُّ الذَّبْحُ بِالسِّنِّ وَالظُّفُر.',
     'Slaughter is lawful with the tooth and the nail.', False),
    ('مَنْ نَسِيَ التَّسْمِيَةَ فَلَا إِثْمَ عَلَيْه، لَكِنْ لَا تُؤْكَلُ '
     'الذَّبِيحَة.',
     'One who forgets the tasmiyah bears no sin, but the animal is not '
     'eaten.', True),
    ('لَا تُحَدُّ الشَّفْرَةُ أَمَامَ الذَّبِيحَة، وَتُوَارَى عَنِ '
     'البَهَائِم.',
     'The blade is not sharpened before the animal, and is hidden from the '
     'beasts.', True),
    ('إِحْسَانُ القِتْلَةِ عَلَى الرَّاجِحِ هُوَ اتِّبَاعُ الشَّرْعِ فِيهَا.',
     'Killing well, on the strongest view, is following the sharʿ in it.',
     True),
])

b += B.memorize(
    'إِنَّ اللهَ كَتَبَ الإِحْسَانَ عَلَى كُلِّ شَيْء',
    'The whole ḥadīth turns on one preposition — <strong>«عَلَى» not '
    '«إِلَى»</strong>. Iḥsān is written <em>upon</em> everything, so there is '
    'no act a person does that falls outside it: not the killing of a harmful '
    'animal, not the slaughter of food, not the sharpening of a blade, not '
    'even the disciplining of one’s own family. <em>The ḥadīth that teaches '
    'the fiqh of the knife is, underneath, teaching that nothing a believer '
    'does is too small for excellence.</em>')

b += B.nav('h16-la-taghdab.html', 'Ḥadīth 16 · لَا تَغْضَبْ',
           'index.html', 'Mark complete · أَتْمَمْتَ الدَّرْس · Hadeeth Hub',
           'hd-h17')

B.write('h17-ihsan.html',
        'إِنَّ اللهَ كَتَبَ الإِحْسَانَ عَلَى كُلِّ شَيْء',
        'Allah Has Prescribed Excellence in All Things',
        'Ḥadīth 17 of al-Nawawī’s Forty (Shaddād ibn Aws, Muslim) with the '
        'sharḥ of Ibn ʿUthaymīn: iḥsān written «upon» everything, not toward '
        'it; the two examples of killing and slaughtering and the difference '
        'between them; the decree-writing versus the law-writing, and that in '
        '«though it is hateful to you» the pronoun returns to the fighting, not '
        'the ruling; killing well as following the sharʿ, which answers the '
        'objection on stoning, with qiṣāṣ as the exception; the four conditions '
        'of a valid slaughter — the slaughterer, the instrument (and why tooth '
        'and nail are excluded), making the blood flow, and the tasmiyah; the '
        'one who forgets it, and the charge of wasting wealth; and the duties '
        'of sharpening the blade and giving the animal rest, reaching even the '
        'discipline of one’s family.',
        17, 'Muslim', '2', b)
print('wrote h17-ihsan.html')
