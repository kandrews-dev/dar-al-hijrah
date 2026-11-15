# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 19 — مَانِعُ الجَهْل: the barrier of ignorance.

The longest of the four barriers in the sharḥ — printed folios 243–272
(PDF indices 240–269, offset +3) — and the one most fought over in our age.
The compiler gathers Ibn Bāz’s words on when ignorance withholds the ruling of
kufr from a particular man, and when it does not.

The spine is a single line the whole barrier keeps drawing:
  • الأُمُورُ الظَّاهِرَة — the matters known from the religion by necessity
    (duʿāʾ of other than Allah, slaughter to other than Allah, grave-worship):
    no excuse of ignorance for one AMONG the Muslims, reached by the Qurʾān
    and Sunnah.
  • الأُمُورُ الدَّقِيقَةُ الخَفِيَّة — the subtle, hidden matters whose
    evidences are obscure: here ignorance CAN excuse; حديث المحرق is the model.

Sections, following the sharḥ:
  1. مدخل — the ẓāhir / khafī divide; the daʿwah-not-reached exception
     (ahl al-fatrah).
  2. الجهل داء — the disease of the Christians (jahl, curable by bayān) vs the
     Jews (ḥasad); jahl condemned in the Qurʾān.
  3. قيام الحجة بالقرآن والسنة — Ibrāhīm 14:52, al-Anʿām 6:19, al-Māʾidah 5:67.
  4. البيان لا التبيّن — «الواجب قيام الحجة فقط»; al-Tawbah 9:115.
  5. حديث المحرق — the model of a genuinely hidden matter; al-Barrāk’s footnote
     (he denied تفاصيل القدرة, not القدرة nor the baʿth).
  6. ليس العذر بالجهل قياسيًّا — no excuse except where the daʿwah has not
     reached; the answer to the contemporaries; «المعيّن لا يُكفَّر — هذا
     الجهل، إذا وُجد مُكفِّر كفر».
  7. سجود معاذ — the rule-8 isnād study: the prostration report is weak/bāṭil
     (تفرد القاسم، اضطراب); «لو كنت آمرًا أحدًا أن يسجد» is the authentic text;
     and even if sound, it was before the dīn settled.
  8. حديث الليثيين — knowing a thing is forbidden suffices; one need not know
     the consequence.

Rule 8 governs §7 throughout: every grading named here — ḍaʿīf, bāṭil,
muḍṭarib, ṣaḥīḥ thābit — is the sharḥ’s own, named scholar by named scholar,
not ours.
"""
from _nq_15_lib import B, p, ar, box, qa
from _nq_19_q import QS

b = B.objectives([
    'State the governing distinction of the barrier — '
    '<strong>الأُمُورُ الظَّاهِرَة</strong> versus '
    '<strong>الدَّقِيقَةُ الخَفِيَّة</strong> — and which admits the excuse '
    'of ignorance.',
    'Say when ignorance <em>does</em> excuse in creed, and the one whose '
    'ruling becomes that of <strong>أَهْلِ الفَتْرَة</strong>.',
    'Give the disease of the Christians against that of the Jews, and why the '
    'difference bears on whether <em>bayān</em> cures it.',
    'Distinguish <strong>البَيَان</strong> from '
    '<strong>التَّبَيُّن</strong>, and state what alone is obligatory for the '
    'proof to stand — «%s».' % ar('قِيَامُ الحُجَّةِ فَقَط'),
    'Use the man who asked to be burned as the model of a genuinely hidden '
    'matter — what exactly he denied, and what he did not.',
    'Answer those who fold the grave-worshippers into «%s», and give Ibn '
    'Bāz’s reply to «the particular is never declared a disbeliever».'
    % ar('حَتَّى تُقَامَ عَلَيْهِ الحُجَّة'),
    'Explain why the report that Muʿādh ؓ prostrated is set aside, and how '
    'that is the discipline of ḥadīth applied to a proof of takfīr’s '
    'opponents.',
])

b += B.provenance(243, 272)

# ----------------------------------------------- مدخل
b += B.heading('مَانِعُ الجَهْل', 'The Barrier of Ignorance')
b += B.prose(
    '<strong>The second barrier, and the one our age argues over most.</strong> '
    'Does a man’s not-knowing shield him from the ruling of kufr? Ibn Bāz '
    'answers with a line he draws again and again, and the whole barrier is '
    'that line.')
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.97rem"><strong>Two kinds of '
        'matter, two different rulings:</strong></p>'
        '<p style="margin:0 0 .4rem;font-size:.93rem">① '
        '<strong>الأُمُورُ الظَّاهِرَة</strong> — what is «مَعْلُومٌ مِنَ '
        'الدِّينِ بِالضَّرُورَة»: that one worships Allah alone, that '
        'supplicating the dead and slaughtering to other than Allah is shirk. '
        '<em>For one living among Muslims, reached by the Qurʾān and Sunnah, '
        'ignorance of these is </em>no<em> excuse.</em></p>'
        '<p style="margin:0;font-size:.93rem">② '
        '<strong>الأُمُورُ الدَّقِيقَةُ الخَفِيَّة</strong> — the subtle '
        'matters whose evidences are obscure. <em>Here ignorance '
        '</em>can<em> excuse</em> — «إِذَا اجْتَهَدَ وَطَلَبَ العِلْمَ أَوْ '
        'سَأَلَ أَهْلَ العِلْمِ وَحَصَلَ خَطَأ، فَهُوَ بَيْنَ أَمْرَيْن: إِنْ '
        'أَصَابَ فَلَهُ أَجْرَان، وَإِنْ أَخْطَأَ فَلَهُ أَجْر».</p>',
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('<strong>So the question is never «was he ignorant?» but «ignorant of '
      'what?»</strong> <em>Of the plain root of the religion — that is not a '
      'thing a man among Muslims may plead not to have known. Of a buried '
      'detail whose proof is hard to see — that is exactly what the barrier '
      'was made to cover.</em>'))
b += B.sharh(
    qa('الَّذِي يَدْعُو أَصْحَابَ القُبُورِ أَوِ الأَصْنَامَ وَهُوَ '
       'جَاهِلٌ لَا يَعْلَمُ أَنَّهُ شِرْك — أَيَكُونُ مُشْرِكًا؟',
       '«نَعَم؛ يَكُونُ مُشْرِكًا... <strong>لِأَنَّ عَلَيْهِ أَنْ '
       'يَتَعَلَّم</strong>. أَمَّا إِذَا كَانَ فِي مَكَانٍ بَعِيدٍ عَنِ '
       'المُسْلِمِينَ وَلَمْ يَبْلُغْهُ القُرْآنُ وَلَا السُّنَّة، فَهَذَا '
       'حُكْمُهُ حُكْمُ أَهْلِ الفَتْرَة... وَأَمْرُهُ إِلَى اللهِ يَوْمَ '
       'القِيَامَة؛ يُمْتَحَنُ يَوْمَ القِيَامَة.» <em>Among Muslims: a '
       'mushrik, and taught. Beyond the reach of the message: the ruling of '
       'ahl al-fatrah, tested on the Day.</em>'))

# ----------------------------------------------- الجهل داء
b += B.heading('الجَهْلُ دَاء', 'Ignorance Is a Disease — and the Two Kinds of Sickness')
b += B.prose(
    '<strong>Ibn Bāz will not let ignorance be dressed up as innocence.</strong> '
    'The Qurʾān, he says, is «مَمْلُوءٌ مِنَ التَّنْدِيدِ بِالجَهْلِ وَأَهْلِه» '
    '— full of censure of ignorance and its people. But he also distinguishes '
    'two diseases, and the distinction decides whether teaching can cure a '
    'man.')
b += B.ayah(
    'وَلَٰكِنَّ أَكْثَرَهُمْ يَجْهَلُونَ',
    '…but most of them are ignorant.',
    'سُورَةُ الأَنْعَام · 6:111')
b += B.sharh(
    p('<strong>The Christians and the Jews are not sick with the same '
      'thing.</strong> <em>«فَالنَّصَارَى عِلَّتُهُمُ الجَهْلُ '
      'وَالضَّلَال؛ فَإِذَا عُرِفُوا وَبُيِّنَ لَهُمْ رَجَعَ كَثِيرٌ '
      'مِنْهُمْ إِلَى الحَقّ. أَمَّا عِلَّةُ اليَهُودِ فَلَيْسَتِ الجَهْل، '
      'بَلْ عِلَّتُهُمُ الحَسَدُ وَالبَغْي، وَمُخَالَفَةُ الحَقِّ عَلَى '
      'بَصِيرَة.»</em>') +
    p('<em>This matters for the barrier itself.</em> Jahl is the sickness that '
      '<strong>bayān can reach</strong> — show the ignorant man the proof and '
      'many turn. Ḥasad is sickness against the known truth, and no clarifying '
      'reaches it. <strong>But neither is a licence:</strong> the Christian who '
      'calls to his falsehood «يَحْسَبُ أَنَّهُ عَلَى هُدًى» is still «ضَالٌّ '
      'مُضِلٌّ... إِلَى النَّار». Sincerity of feeling is not the measure; the '
      'truth reached is.'))

# ----------------------------------------------- قيام الحجة
b += B.heading('بِمَاذَا تَقُومُ الحُجَّة؟', 'By What the Proof Is Established')
b += B.prose(
    '<strong>The heart of the barrier: the ḥujjah of Allah stands by the '
    'Book and the Messenger ﷺ.</strong> Where the Qurʾān and the Sunnah have '
    'reached a people, the proof has been established upon them — the reaching '
    '<em>is</em> the establishing.')
b += B.ayah(
    'هَٰذَا بَلَاغٌ لِّلنَّاسِ وَلِيُنذَرُوا بِهِ',
    'This [Qurʾān] is a clear message for mankind, that they may be warned by '
    'it.',
    'سُورَةُ إِبْرَاهِيم · 14:52')
b += B.ayah(
    'وَأُوحِيَ إِلَيَّ هَٰذَا الْقُرْآنُ لِأُنذِرَكُم بِهِ وَمَن بَلَغَ',
    'And this Qurʾān has been revealed to me that I may warn you by it — and '
    'whomever it reaches.',
    'سُورَةُ الأَنْعَام · 6:19')
b += B.ayah(
    'يَا أَيُّهَا الرَّسُولُ بَلِّغْ مَا أُنزِلَ إِلَيْكَ مِن رَّبِّكَ',
    'O Messenger, convey what has been sent down to you from your Lord.',
    'سُورَةُ المَائِدَة · 5:67')
b += B.sharh(
    p('<strong>Ibn Bāz presses the point against a real objection.</strong> '
      '<em>Someone said the grave-worshippers are not disbelievers «حَتَّى '
      'تُقَامَ عَلَيْهِمُ الحُجَّة». He answered:</em> «لَا، هَذَا مِنْ '
      'جَهْلِهِم؛ عُبَّادُ القُبُورِ كُفَّار، وَاليَهُودُ كُفَّار، '
      'وَالنَّصَارَى كُفَّار؛ وَلَكِنْ عِنْدَ القَتْلِ يُسْتَتَاب، فَإِنْ '
      'تَابَ وَإِلَّا قُتِل.» <em>«They say the ḥujjah must be established — '
      '</em>it has been<em>: the Qurʾān reached them.»</em> «بَلَغَهُمُ '
      'القُرْآن... يَسْمَعُونَهُ فِي الإِذَاعَاتِ وَفِي كُلِّ شَيْءٍ وَلَا '
      'يُبَالُون.»'))

# ----------------------------------------------- البيان لا التبيّن
b += B.heading('البَيَانُ لَا التَّبَيُّن', 'Conveying the Proof, Not the Grasping of It')
b += B.prose(
    '<strong>This is the precision the whole question turns on, and it is '
    'constantly blurred.</strong> What is obligatory is that the proof be '
    '<em>conveyed and made clear</em> — not that the person actually come to '
    'understand and accept it.')
b += B.ayah(
    'وَمَا كَانَ اللَّهُ لِيُضِلَّ قَوْمًا بَعْدَ إِذْ هَدَاهُمْ حَتَّىٰ '
    'يُبَيِّنَ لَهُم مَّا يَتَّقُونَ',
    'Allah would never let a people go astray after He has guided them, until '
    'He makes clear to them what they should beware of.',
    'سُورَةُ التَّوْبَة · 9:115')
b += B.sharh(
    qa('قَالَ تَعَالَى: «حَتَّى يُبَيِّنَ لَهُم» — يُبَيِّنُ أَمْ '
       'يَتَبَيَّن؟',
       '«إِيه، حَتَّى يُبَيِّن» — <strong>the duty is the بَيَان</strong>, '
       'the making-clear, «وَلَوْ لَمْ يَحْصُلْ تَبَيُّن». <em>The proof is '
       'established when it is set before a man plainly; whether his heart '
       'then opens to it is another thing, and not the condition of the '
       'ruling.</em>') +
    box('<p style="margin:0;font-size:.93rem"><strong>Why this matters so '
        'much:</strong> <em>make </em>tabayyun<em> (the person’s own '
        'conviction) the condition, and no stubborn man is ever bound by any '
        'proof — he need only refuse to be convinced. The barrier of '
        'ignorance protects the one the message never reached and the one lost '
        'in a buried detail; it does not hand every obstinate heart a veto '
        'over the plain religion.</em></p>'))

# ----------------------------------------------- حديث المحرق
b += B.heading('حَدِيثُ المُحَرَّق', 'The Man Who Asked to Be Burned — the Model of a Hidden Matter')
b += B.prose(
    '<strong>Now the other side of the line, so it is not mistaken for '
    'harshness.</strong> When Ibn Bāz says ignorance <em>can</em> excuse in a '
    'subtle matter, this is his standing example — a ḥadīth in the Ṣaḥīḥayn.')
b += B.sharh(
    p('<em>A man, fearing Allah, told his family: when I die, burn me, grind '
      'me, and scatter me in the sea — thinking that so he might escape his '
      'Lord. Allah gathered him and asked why; he said «خَوْفُكَ يَا رَبّ», '
      'and Allah forgave him.</em> Ibn Bāz: «هَذَا جَهِلَ بَعْضَ الشَّيْءِ '
      'مِنَ الأُمُورِ الخَفِيَّةِ مِنْ كَمَالِ القُدْرَة؛ جَهِلَهَا فَعُذِر، '
      'خَوْفًا مِنَ الله.»') +
    box('<p style="margin:0;font-size:.93rem"><strong>al-Barrāk’s footnote '
        'draws the line to the inch — and this is the whole key:</strong> '
        '<em>«هَذَا الشَّخْصُ... إِنَّمَا أَنْكَرَ <strong>كَمَالَ '
        'تَفَاصِيلِ القُدْرَة</strong> وَلَمْ يُنْكِرْ قُدْرَةَ الله، وَلَمْ '
        'يُنْكِرِ البَعْث... وَالَّذِي حَمَلَهُ عَلَى ذَلِكَ أَمْرَان: '
        'الجَهْلُ وَالخَوْفُ العَظِيم.»</em> Had he denied Allah’s power '
        '<em>itself</em>, or the resurrection, «مَا كَانَ مَعْذُورًا». He '
        'denied a hidden <em>detail</em> of how far that power reaches — and '
        '«مِثْلُهُ يُجْهَل».</p>') +
    p('<strong>Set the two examples side by side and the barrier is '
      'clear.</strong> <em>The grave-worshipper denies the plain root — </em>no '
      'excuse. <em>This man affirmed the root and stumbled on a buried '
      'detail — </em>excused. <strong>«الَّذِي يُعْذَرُ بِالجَهْلِ هُوَ '
      'الَّذِي يَجْهَلُ أَمْرًا دَقِيقًا خَفِيًّا مِثْلُهُ يَجْهَلُه؛ أَمَّا '
      'إِذَا أَنْكَرَ أَمْرًا وَاضِحًا مَعْلُومًا لِعَامَّةِ المُسْلِمِينَ '
      'فَلَا يُقْبَل.»</strong>'))

# ----------------------------------------------- not qiyāsī
b += B.heading('لَيْسَ العُذْرُ بِالجَهْلِ قِيَاسِيًّا', 'Ignorance Is No Sliding Scale')
b += B.sharh(
    p('<strong>He refuses to let the excuse float with the times.</strong> '
      '<em>Asked whether excusing by ignorance shifts with era and land:</em> '
      '«لَيْسَ العُذْرُ بِالجَهْلِ مَسْأَلَةً قِيَاسِيَّةً تَخْتَلِفُ مِنْ '
      'زَمَانٍ إِلَى زَمَان، وَمَكَانٍ إِلَى آخَر؛ لِأَنَّ الجَهْلَ لَيْسَ '
      'بِعُذْرٍ بِالنِّسْبَةِ لِلْعَقِيدَة — إِلَّا إِذَا كَانَ فِي مَكَانٍ '
      'لَمْ تَبْلُغْهُ الدَّعْوَة.»') +
    p('<em>And the sharpest line of the barrier, when it was put to him that '
      '«the particular person is never declared a disbeliever»:</em>') +
    box('<p style="margin:0;font-size:1rem"><span dir="rtl" lang="ar">'
        'قِيلَ لَهُ: بَعْضُ النَّاسِ يَقُول: المُعَيَّنُ لَا يُكَفَّر. '
        'فَأَجَاب: «<strong>هَذَا الجَهْل؛ إِذَا وُجِدَ مُكَفِّرٌ '
        'كَفَر</strong>.»</span></p>',
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('<strong>Read it with the whole section.</strong> <em>The barriers are '
      'real — coercion, ignorance, error, interpretation withhold the ruling. '
      'But they are barriers, not a wall: when a cause of takfīr is '
      'established and no barrier stands, the ruling </em>does<em> fall on the '
      'named man. To say otherwise — that no individual is ever ruled a '
      'disbeliever — is, Ibn Bāz says flatly, itself a kind of ignorance.</em>'))

# ----------------------------------------------- سجود معاذ
b += B.heading('قِصَّةُ سُجُودِ مُعَاذ', 'The Report of Muʿādh’s Prostration — Ḥadīth Discipline on a Proof')
b += B.prose(
    '<strong>Those who stretch the excuse of ignorance over grave-worship lean '
    'on a story: that Muʿādh ibn Jabal ؓ prostrated to the Prophet ﷺ on '
    'returning from Shām, and was not declared a disbeliever.</strong> The '
    'compiler spends folios on it — and the lesson is the method as much as '
    'the verdict.')
b += B.sharh(
    box('<p style="margin:0;font-size:.93rem"><strong>The verdict on the '
        'prostration report:</strong> <em>«فِي صِحَّتِهِ نَظَر» — rather '
        '</em>ḍaʿīf, bāṭil<em>.</em> «تَفَرَّدَ بِهِ القَاسِمُ بْنُ عَوْفٍ '
        'الشَّيْبَانِي، وَلَمْ يَذْكُرْ أَحَدٌ مِنَ الرُّوَاةِ أَنَّ '
        'مُعَاذًا سَجَد؛ وَأَكْثَرُ الرِّوَايَاتِ عَنِ القَاسِمِ لَيْسَ '
        'فِيهَا أَنَّهُ سَجَد.» The compiler lays out seven turuq and shows '
        'al-Qāsim «اضْطَرَبَ فِي رِوَايَتِهِ اضْطِرَابًا كَبِيرًا» — once '
        'from Muʿādh directly, once through Ibn Abī Awfā, once through Zayd '
        'ibn Arqam, once with two intermediaries, once with three — «وَمِثْلُهُ '
        'لَا يَحْتَمِلُ التَّفَرُّد».</p>') +
    p('<strong>What <em>is</em> authentic is the other wording.</strong> '
      '<em>«أَمَّا حَدِيثُ: (لَوْ كُنْتُ آمِرًا أَحَدًا أَنْ يَسْجُدَ '
      'لِأَحَد…): فَصَحِيحٌ ثَابِتٌ مَرْوِيٌّ عَنْ جَمَاعَةٍ مِنَ '
      'الصَّحَابَة.»</em> Notice precisely what carries and what falls: the '
      'Prophet’s ﷺ <em>words</em> forbidding prostration to other than Allah '
      'are firm; the claim that Muʿādh actually <em>did</em> prostrate — the '
      'part the argument needs — «لَا أَصْلَ لَهُ البَتَّة».'))
b += B.sharh(
    p('<strong>And even granting the question Muʿādh asked, it is no proof for '
      'today.</strong> <em>It belonged to the earliest Islam, before the '
      'religion had settled — «هَذَا لَهُ شُبْهَةٌ فِي أَوَّلِ الإِسْلَام، '
      'لَكِنِ اسْتَقَرَّ الدِّين، وَعُرِفَ أَنَّ السُّجُودَ لِله».</em> A '
      'passing doubt in year one, resolved by the plain command, is not a man '
      'circling a grave after the Qurʾān has filled the air around him.'))
b += B.ayah(
    'فَاسْجُدُوا لِلَّهِ وَاعْبُدُوا',
    'So prostrate to Allah and worship [Him].',
    'سُورَةُ النَّجْم · 53:62')

# ----------------------------------------------- الليثيون
b += B.heading('حَدِيثُ اللَّيْثِيِّين', 'Knowing a Thing Is Forbidden Is Enough')
b += B.prose(
    '<strong>One last proof the expanders raise, and its answer is a rule '
    'worth keeping.</strong> Some Bedouin of Banū Layth, offered '
    'compensation and asked «are you content?», said «لَا» — taken by some as '
    'belying the Prophet ﷺ, yet excused, they claim, by ignorance.')
b += B.sharh(
    p('<em>The compiler answers in steps. First, the report does not have them '
      'belying him at all — «إِنَّمَا طَمِعُوا فِي الزِّيَادَة», they were '
      'angling for more, and he gave more and they were content. But grant, '
      'for argument, that their word was kufr:</em>') +
    box('<p style="margin:0;font-size:.95rem"><span dir="rtl" lang="ar">'
        '«عِلْمُهُمْ أَنَّ التَّكْذِيبَ لِلْأَنْبِيَاءِ حَرَامٌ '
        '<strong>كَافٍ فِي كُفْرِهِم</strong>؛ وَلَا يُشْتَرَطُ عِلْمُهُمْ '
        'بِالأَثَرِ المُتَرَتِّبِ عَلَى التَّكْذِيب — كَمَنْ عَلِمَ '
        'بِتَحْرِيمِ السَّرِقَةِ وَلَمْ يَعْلَمْ بِالأَثَرِ المُتَرَتِّبِ '
        'عَلَيْهَا، فَلَا يُشْتَرَطُ فِي القَطْعِ عِلْمُهُ '
        'بِذَلِك.»</span></p>') +
    p('<strong>This is the cleanest statement of the whole barrier’s limit.</strong> '
      '<em>A man need not know the </em>penalty<em> of a sin to be bound by '
      'its </em>prohibition. <em>The thief who never studied the ḥadd is still '
      'a thief; the one who knows belying a Prophet is forbidden is not '
      'excused by not knowing it is called «kufr». Ignorance of the label is '
      'not ignorance of the law.</em>'))

# ----------------------------------------------- vocab, quiz, memorize
b += B.vocab([
    ('مَانِعُ الجَهْل', 'māniʿ al-jahl', 'the barrier of ignorance',
     'The second barrier: not-knowing may withhold the ruling of kufr — but '
     'only in the hidden matters, not the plain root of the religion.'),
    ('مَعْلُومٌ مِنَ الدِّينِ بِالضَّرُورَة',
     'maʿlūm min al-dīn bi-l-ḍarūrah',
     'known from the religion by necessity',
     'The plain matters — tawḥīd, that grave-worship is shirk. No excuse of '
     'ignorance for one among Muslims whom the message has reached.'),
    ('الأُمُورُ الدَّقِيقَةُ الخَفِيَّة', 'al-umūr al-daqīqah al-khafiyyah',
     'the subtle, hidden matters',
     'Where evidences are obscure; here ignorance can excuse, and حديث '
     'المحرق is the model.'),
    ('قِيَامُ الحُجَّة', 'qiyām al-ḥujjah', 'the establishing of the proof',
     'It stands by the Qurʾān and the Sunnah reaching a people — «هَٰذَا '
     'بَلَاغٌ لِّلنَّاس».'),
    ('البَيَانُ لَا التَّبَيُّن', 'al-bayān lā al-tabayyun',
     'conveying, not the grasping',
     'What is obligatory is that the proof be made clear — not that the '
     'person come to accept it. «الوَاجِبُ قِيَامُ الحُجَّةِ فَقَط».'),
    ('أَهْلُ الفَتْرَة', 'ahl al-fatrah', 'those the message never reached',
     'The one true exception in creed: one in a place «لَمْ تَبْلُغْهُ '
     'الدَّعْوَة». Tested on the Day of Resurrection.'),
    ('تَفَاصِيلُ القُدْرَة', 'tafāṣīl al-qudrah',
     'the fine details of [Allah’s] power',
     'What the burned man denied — not Allah’s power itself nor the baʿth. '
     'The hidden-detail kind of error that is excused.'),
    ('الاضْطِرَاب', 'al-iḍṭirāb', 'instability in a chain of narration',
     'Why Muʿādh’s alleged prostration falls: al-Qāsim al-Shaybānī narrates '
     'it five conflicting ways and «لَا يَحْتَمِلُ التَّفَرُّد».'),
])

b += B.mcq('nq-l19-mcq', QS)

b += B.tf('nq-l19-tf', [
    ('الجَاهِلُ الَّذِي يَدْعُو غَيْرَ اللهِ وَهُوَ بَيْنَ المُسْلِمِينَ '
     'قَدْ بَلَغَهُ القُرْآنُ — يَكُونُ مُشْرِكًا وَيُعَلَّم.',
     'The ignorant one who calls on other than Allah while among Muslims, the '
     'Qurʾān having reached him, is a mushrik and is taught.', True),
    ('العُذْرُ بِالجَهْلِ جَارٍ فِي الأُمُورِ الظَّاهِرَةِ المَعْلُومَةِ مِنَ '
     'الدِّينِ بِالضَّرُورَة.',
     'The excuse of ignorance applies in the plain matters known from the '
     'religion by necessity.', False),
    ('الوَاجِبُ هُوَ البَيَان — قِيَامُ الحُجَّة — وَلَوْ لَمْ يَحْصُلْ '
     'تَبَيُّنٌ مِنَ المُخَاطَب.',
     'What is obligatory is the conveying — the establishing of the proof — '
     'even if the addressed one does not come to grasp it.', True),
    ('الَّذِي أَمَرَ أَهْلَهُ أَنْ يُحَرِّقُوهُ أَنْكَرَ قُدْرَةَ اللهِ '
     'وَالبَعْث، وَمَعَ ذَلِكَ عُذِر.',
     'The man who told his family to burn him denied Allah’s power and the '
     'resurrection, and was excused anyway.', False),
    ('عِلَّةُ النَّصَارَى الجَهْل، وَعِلَّةُ اليَهُودِ الحَسَدُ وَالبَغْي.',
     'The disease of the Christians is ignorance; that of the Jews is envy '
     'and transgression.', True),
    ('قَالَ ابْنُ بَاز: المُعَيَّنُ لَا يُكَفَّرُ مُطْلَقًا وَإِنْ وُجِدَ '
     'المُكَفِّر.',
     'Ibn Bāz said the particular person is never declared a disbeliever, even '
     'if a cause of takfīr is present.', False),
    ('رِوَايَةُ سُجُودِ مُعَاذٍ لِلنَّبِيِّ ﷺ ضَعِيفَةٌ، تَفَرَّدَ بِهَا '
     'القَاسِمُ الشَّيْبَانِيُّ وَاضْطَرَبَ فِيهَا.',
     'The report that Muʿādh prostrated to the Prophet ﷺ is weak; al-Qāsim '
     'al-Shaybānī narrated it alone and with instability.', True),
])

b += B.memorize(
    'الَّذِي يُعْذَرُ بِالجَهْلِ هُوَ الَّذِي يَجْهَلُ أَمْرًا دَقِيقًا '
    'خَفِيًّا مِثْلُهُ يَجْهَلُه؛ أَمَّا إِذَا أَنْكَرَ أَمْرًا وَاضِحًا '
    'مَعْلُومًا لِعَامَّةِ المُسْلِمِينَ فَلَا يُقْبَلُ وَلَوِ ادَّعَى '
    'أَنَّهُ يَجْهَل',
    'Ibn Bāz, on the barrier of ignorance. <strong>This one sentence holds the '
    'whole balance.</strong> <em>Ignorance is a real barrier — but it covers '
    'the buried detail whose proof is hard to see, the thing «مِثْلُهُ '
    'يُجْهَل», not the plain root of the religion that every Muslim among '
    'Muslims is reached by. The man who stumbled on a hidden fold of Allah’s '
    'power was excused; the man who circles a grave after the Qurʾān has '
    'reached him is not. And the measure is never how sincerely he felt — it '
    'is what the clear proof set before him.</em>')

b += B.nav('nq-l18-mawani-al-ikrah.html',
           'مَانِعُ الإِكْرَاه',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l19')

B.write('nq-l19-mani-al-jahl.html',
        'مَوَانِعُ التَّكْفِير · مَانِعُ الجَهْل',
        'The Barriers to Takfīr — Ignorance',
        'The second and longest barrier to takfīr of a particular person, from '
        'the words of Shaykh Ibn Bāz: ignorance. The governing distinction '
        'between the plain matters known from the religion by necessity — where '
        'ignorance is no excuse for one among Muslims reached by the Qurʾān and '
        'Sunnah — and the subtle hidden matters, where it can excuse. The '
        'disease of the Christians (ignorance, curable by clarification) versus '
        'the Jews (envy); that the proof of Allah stands by the Qurʾān and '
        'Sunnah reaching a people; the precise distinction between conveying '
        'the proof (obligatory) and the person’s grasping it (not a '
        'condition), on al-Tawbah 9:115; the man who asked to be burned as the '
        'model of a genuinely hidden matter — he denied a detail of Allah’s '
        'power, not His power itself; that excusing by ignorance is no sliding '
        'scale and no individual is beyond ruling when a cause of takfīr is '
        'present; the ḥadīth-discipline verdict that the report of Muʿādh’s '
        'prostration is weak; and that knowing a thing is forbidden suffices '
        'without knowing its named consequence.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ التَّاسِعَ عَشَر', '6', b)
print('wrote nq-l19-mani-al-jahl.html')
