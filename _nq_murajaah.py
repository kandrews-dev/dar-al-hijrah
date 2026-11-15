# -*- coding: utf-8 -*-
"""مُرَاجَعَةُ المَتْن for Nawāqiḍ al-Islām — closes the track.

Per the standing rule, a matn closes with a مُرَاجَعَة, not an exam: prompts
walking the whole book in order, each answer under a tap-to-reveal, each with a
link back to the lesson it comes from. No timer, no score. The reference
implementation is wasitiyyah-murajaah.html; this follows it exactly in markup so
the theme (and dark mode) carry over untouched.

The header/nav and footer are spliced live from u6-nawaqid.html via the builder,
so this page inherits the current site chrome and the no-flash dark-mode script.
"""
import io, os, re
from _nq_15_lib import B, ar

M = B.M

TITLE_AR = u'مُرَاجَعَةُ المَتْن'
TITLE_EN = u'What You Should Now Know — a review of the ten nullifiers'
DESC = (u'The end-of-text review for Nawāqiḍ al-Islām: prompts walking the ten '
        u'nullifiers and the capstone on the barriers to takfīr in order, each '
        u'with its answer under a tap-to-reveal and a link back to the lesson '
        u'it comes from. Not an exam — the check a student makes on himself '
        u'before he says he has read a matn.')

# (question, answer_html, lesson_file, lesson_label)
PARTS = [
    (u'الجُزْءُ الأَوَّل · الشِّرْكُ وَأُصُولُ التَّوْحِيد',
     u'Part 1 — Shirk and the Roots of Tawḥīd',
     u'Nullifiers 1–3 · Lessons 1–3',
     [
      (u'What is the first nullifier, and what single word in the matn gives it '
       u'its reach?',
       u'<p style="margin:0"><strong>الشِّرْكُ فِي عِبَادَةِ الله</strong> — '
       u'associating a partner with Allah in worship. The reach is in the matn’s '
       u'own clause <strong>%s</strong>: whoever directs an act of worship to '
       u'other than Allah has nullified Islām — and «%s» means it needs no '
       u'idol and no denial, only the misdirected act.</p>'
       % (ar(u'وَمِنْهُ الذَّبْحُ لِغَيْرِ الله'),
          ar(u'وَمِنْه')),
       u'nq-l01-shirk-al-ibadah.html', u'Lesson 1'),
      (u'Why is leaving the prayer placed in a book of <em>nullifiers</em>, and '
       u'what is the precise point of disagreement Ibn Bāz marks?',
       u'<p style="margin:0 0 .5rem">Because its abandonment is treated by weighty '
       u'evidence as crossing out of Islām, not merely a major sin. But Ibn Bāz '
       u'draws the line with care: one who <strong>denies</strong> the obligation '
       u'of prayer is a disbeliever «%s»; one who merely <strong>doubts</strong> '
       u'about the abandoner’s ruling is <em>maʿdhūr fī ijtihādihi</em>, because '
       u'that is a place of ijtihād.</p>'
       % ar(u'فِي قَوْلِ الجَمِيع'),
       u'nq-l02-dhabh-wa-tarik-al-salah.html', u'Lesson 2'),
      (u'What makes taking an intermediary between oneself and Allah — asking '
       u'them, relying on them — a nullifier?',
       u'<p style="margin:0">It is the very structure of the first mushrikīn: '
       u'they did not deny Allah, they placed <strong>%s</strong> between '
       u'themselves and Him «%s». To call on them, to seek their intercession, '
       u'is to repeat that act — and it is kufr «%s», by the consensus the '
       u'author names.</p>'
       % (ar(u'وَسَائِط'),
          ar(u'لِيُقَرِّبُونَا إِلَى اللهِ زُلْفَى'),
          ar(u'بِالإِجْمَاع')),
       u'nq-l03-al-wasait.html', u'Lesson 3'),
     ]),
    (u'الجُزْءُ الثَّانِي · المُشْرِكُونَ وَهُدَى النَّبِيّ ﷺ',
     u'Part 2 — The Mushrikīn, and the Guidance of the Prophet ﷺ',
     u'Nullifiers 3–5 · Lessons 4–8',
     [
      (u'The fourth nullifier is <em>not</em> declaring the mushrikīn '
       u'disbelievers — but the sharḥ spends most of its folios on restraint. '
       u'Why, and what is the governing rule?',
       u'<p style="margin:0 0 .5rem">Because the clause is about <strong>the '
       u'establishing of the proof</strong> «each according to his state», and a '
       u'lesson that carried the ruling and dropped that would misteach it. The '
       u'ʿāmmī may say of plain shirk that it is shirk, and must make '
       u'<strong>%s</strong> where a matter is obscure to him.</p>'
       u'<p style="margin:0">And a warning the clause carries about itself: «%s» '
       u'is <em>not a ḥadīth at all</em> — the sharḥ grades it kaḏib lā aṣla '
       u'lah.</p>'
       % (ar(u'التَّوَقُّف'),
          ar(u'مَنْ كَفَّرَ مُسْلِمًا فَقَدْ كَفَر')),
       u'nq-l04-takfir-al-mushrikin.html', u'Lesson 4'),
      (u'The fifth nullifier — believing some guidance more complete than the '
       u'Prophet’s ﷺ — turns on four words. Which, and what do they force?',
       u'<p style="margin:0"><strong>%s</strong> — «even if he acts by it». They '
       u'force the footnote’s distinction: <strong>%s</strong> (hating the '
       u'legislation) nullifies; <strong>%s</strong> — a merely natural dislike '
       u'of a ruling while submitting to it — «%s», and Allah describes the '
       u'believers that way.</p>'
       % (ar(u'وَلَوْ عَمِلَ بِه'),
          ar(u'بُغْضُ التَّشْرِيع'),
          ar(u'بُغْضٌ طَبِيعِيّ'),
          ar(u'فَهَذَا لَيْسَ مِنَ الكُفْرِ فِي شَيْء')),
       u'nq-l08-bughd-ma-jaa-bihi.html', u'Lesson 8'),
      (u'When the third nullifier’s material on legislation is taught, what '
       u'three categories must be kept apart?',
       u'<p style="margin:0">The one who judges by other than what Allah revealed '
       u'<strong>deeming it permitted or better</strong> — that is the kufr that '
       u'nullifies; the one who does so out of <strong>bribe or desire</strong> '
       u'while knowing it is wrong — a major sin; and the <strong>compelled</strong> '
       u'(al-muḍṭarr). <em>The lesson weights these exactly as the sharḥ does — the '
       u'ruling, then the تَفْصِيل that governs it.</em></p>',
       u'nq-l07-mudtarr-wa-tashri.html', u'Lesson 7'),
     ]),
    (u'الجُزْءُ الثَّالِث · الاسْتِهْزَاءُ وَالسِّحْر',
     u'Part 3 — Mockery, and Magic',
     u'Nullifiers 6–7 · Lessons 9–13',
     [
      (u'What is the argument that makes the sixth nullifier — mockery — '
       u'teachable without a premise about <em>intending</em> insult?',
       u'<p style="margin:0">Ibn Bāz does not say mockery is <em>punished as</em> '
       u'contempt — he says it <strong>is</strong> contempt (%s = %s). The objects '
       u'are perfection itself, so «%s» fails in the daleel, and «even in jest» '
       u'follows. <strong>But the ruling and the sentence are two things:</strong> '
       u'«%s».</p>'
       % (ar(u'اسْتِهْزَاء'),
          ar(u'تَنَقُّصٌ وَاحْتِقَار'),
          ar(u'إِنَّمَا كُنَّا نَخُوضُ وَنَلْعَب'),
          ar(u'أَمَّا القَتْلُ فَشَيْءٌ آخَر، يَحْتَاجُ إِلَى اسْتِتَابَة')),
       u'nq-l09-al-istihza.html', u'Lesson 9'),
      (u'The seventh nullifier is the longest clause in the book. On the ruling '
       u'«%s», what is the sharḥ’s verdict, and what carries the ruling instead?'
       % ar(u'حَدُّ السَّاحِرِ ضَرْبُهُ بِالسَّيْف'),
       u'<p style="margin:0">That ḥadīth is graded <strong>weak</strong> by seven '
       u'named scholars — al-Bukhārī («%s»), al-Tirmidhī, al-Dhahabī, Ibn Ḥajar, '
       u'Ibn Ḥazm, Ibn Rajab, and Ibn Bāz («%s»). What carries the ruling is '
       u'<strong>%s</strong> — ṣaḥīḥ in isnād, and Ibn Qudāmah: «%s».</p>'
       % (ar(u'هَذَا لَا شَيْء'),
          ar(u'الرَّاجِحُ وَقْفُهُ عَلَى جُنْدُب'),
          ar(u'أَثَرُ عُمَر'),
          ar(u'اشْتُهِرَ وَلَمْ يُنْكَرْ فَكَانَ إِجْمَاعًا')),
       u'nq-l12-hukm-al-sahir.html', u'Lesson 12'),
      (u'How is the objection answered that the Prophet ﷺ was bewitched, given '
       u'«%s»?' % ar(u'وَاللهُ يَعْصِمُكَ مِنَ النَّاس'),
       u'<p style="margin:0">That āyah is among the <strong>last</strong> revealed, '
       u'and the ʿiṣmah promised is «%s» — protection in <em>conveying the '
       u'message</em>, not from every bodily harm (Uḥud is listed). The siḥr '
       u'touched his body, not the revelation; and ʿĀʾishah’s report stands, the '
       u'claim that Hishām b. ʿUrwah was mukhtaliṭ answered by al-Dhahabī: «%s».</p>'
       % (ar(u'مِمَّا يَمْنَعُ مِنْ تَبْلِيغِ الرِّسَالَة'),
          ar(u'لَمْ يَخْتَلِطْ أَبَدًا')),
       u'nq-l13-al-nushrah-wa-al-ilaj.html', u'Lesson 13'),
     ]),
    (u'الجُزْءُ الرَّابِع · المُوَالَاةُ وَالخُرُوجُ وَالإِعْرَاض',
     u'Part 4 — Alliance, Standing Outside, and Turning Away',
     u'Nullifiers 8–10 · Lessons 14–17',
     [
      (u'The eighth nullifier turns on six words distinguishing two things that '
       u'look alike. Give them.',
       u'<p style="margin:0"><strong>%s</strong> — «%s». To ally with the '
       u'disbelievers in sin (cheering, imitation) is disobedience; to '
       u'<strong>side with them against the Muslims</strong>, «%s», is the '
       u'kufr. <em>A page that collapses the two manufactures a takfīr the '
       u'source refuses.</em></p>'
       % (ar(u'المُوَالَاةُ غَيْرُ التَّوَلِّي'),
          ar(u'المُوَالَاةُ مَعْصِيَة، وَالتَّوَلِّي كُفْر'),
          ar(u'مُسَاعَدَتُهُمْ عَلَى المُسْلِمِين')),
       u'nq-l14-al-muwalah-wa-al-tawalli.html', u'Lesson 14'),
      (u'The spy Ḥāṭib ؓ did an act of betrayal and was not declared a '
       u'disbeliever. Where exactly was his taʾwīl located — and what principle '
       u'does his case open?',
       u'<p style="margin:0 0 .5rem">Not in the concealment — a sin he knew he was '
       u'committing — but in his belief the disclosure <strong>would do no '
       u'harm</strong>; so a man can be sinning and interpreting at once, and '
       u'fourteen imāms named him مُتَأَوِّل.</p>'
       u'<p style="margin:0">His case opens the book’s closing principle: '
       u'<strong>the ruling on an act and the ruling on a particular man are two '
       u'rulings</strong> — which is what مَوَانِعُ تَكْفِيرِ المُعَيَّن is for.</p>',
       u'nq-l15-al-istianah-wa-al-jasus.html', u'Lesson 15'),
      (u'The ninth nullifier is claiming to stand outside the sharīʿah. How does '
       u'the deviant’s own proof-text — al-Khiḍr — refute him?',
       u'<p style="margin:0">Al-Khiḍr was a <strong>%s</strong> with his own '
       u'waḥy, never under Mūsā’s sharīʿah — so he is no precedent for a man who '
       u'claims to rise above the Prophet’s ﷺ law on a <em>feeling</em> «%s». '
       u'Al-Khiḍr had revelation; the claimant has a feeling. And the heart is '
       u'not maʿṣūm: «%s».</p>'
       % (ar(u'نَبِيٌّ مُسْتَقِلّ'),
          ar(u'حَدَّثَنِي قَلْبِي عَنْ رَبِّي'),
          ar(u'المَعْصُومُ مَا ثَبَتَ عَنِ الرَّسُولِ ﷺ أَوْ جَاءَ بِهِ الكِتَاب')),
       u'nq-l16-al-khuruj-an-al-shariah.html', u'Lesson 16'),
      (u'The tenth and last nullifier is turning away (الإِعْرَاض). Where does '
       u'Ibn Bāz locate the real deficiency of our age, and what sign does he '
       u'give?',
       u'<p style="margin:0">Not in access to knowledge — «%s» — but «%s», in '
       u'action and will. The sign of good willed for a person is '
       u'<strong>%s</strong> — «%s» (muttafaq, from Muʿāwiyah ؓ): people are '
       u'between مَحْرُوم and مَرْحُوم. <em>And there is a fitness in it — the '
       u'student who reached and studied the tenth nullifier has, by that act, '
       u'done the opposite of it.</em></p>'
       % (ar(u'أَمَّا العِلْمُ فَمُتَيَسِّر'),
          ar(u'ضَعْفُ الطَّالِبِ وَإِعْرَاضُه'),
          ar(u'الفِقْهُ فِي الدِّين'),
          ar(u'مَنْ يُرِدِ اللهُ بِهِ خَيْرًا يُفَقِّهْهُ فِي الدِّين')),
       u'nq-l17-al-irad-an-al-din.html', u'Lesson 17'),
     ]),
    (u'الجُزْءُ الخَامِس · مَوَانِعُ تَكْفِيرِ المُعَيَّن',
     u'Part 5 — The Barriers to Takfīr of a Particular Person',
     u'The capstone · Lessons 18–20',
     [
      (u'What is the one distinction the whole capstone exists to draw — and '
       u'which earlier nullifier already pointed to it?',
       u'<p style="margin:0">Between the ruling on the <strong>act</strong> (the '
       u'النَّوْع — that it is kufr) and the ruling on a <strong>particular '
       u'person</strong> (the المُعَيَّن — that <em>this</em> man is a '
       u'disbeliever). They are not the same ruling: takfīr of a named person '
       u'requires its conditions met <em>and</em> its barriers absent. The '
       u'eighth nullifier, with the spy Ḥāṭib ؓ, already pointed here.</p>',
       u'nq-l18-mawani-al-ikrah.html', u'Lesson 18'),
      (u'The matn names only one barrier — coercion. State its daleel and Ibn '
       u'Bāz’s two conditions.',
       u'<p style="margin:0">Daleel: <strong>%s</strong> (al-Naḥl 16:106), '
       u'revealed about ʿAmmār ibn Yāsir ؓ. The two conditions: '
       u'<strong>الإِكْرَاه</strong> — that he genuinely cannot escape — '
       u'<strong>and</strong> <strong>الطُّمَأْنِينَةُ بِالإِيمَان</strong>, the '
       u'heart’s rest upon faith. Remove either — no coercion, or a heart gone '
       u'over — and «%s».</p>'
       % (ar(u'إِلَّا مَنْ أُكْرِهَ وَقَلْبُهُ مُطْمَئِنٌّ بِالإِيمَان'),
          ar(u'بَاءَ بِإِثْمِ ذَلِك')),
       u'nq-l18-mawani-al-ikrah.html', u'Lesson 18'),
      (u'Does coercion excuse everything? Name its two limits.',
       u'<p style="margin:0">No. Acting for <strong>a job, a rank or wealth</strong> '
       u'is not coercion — «%s». And coercion never makes lawful the '
       u'<strong>killing of a maʿṣūm</strong>, by the agreement of the Muslims: '
       u'«%s». You may speak a word to save your life; you may not take a '
       u'protected life to save it.</p>'
       % (ar(u'فَهَذَا كُلُّهُ مُنْكَرٌ وَلَيْسَ بِعُذْر'),
          ar(u'فَلَيْسَ حِفْظُ نَفْسِهِ بِقَتْلِ ذَلِكَ المَعْصُومِ أَوْلَى مِنَ العَكْس')),
       u'nq-l18-mawani-al-ikrah.html', u'Lesson 18'),
      (u'The barrier of ignorance turns on one distinction. State it, and where '
       u'ignorance does <em>not</em> excuse.',
       u'<p style="margin:0">Between <strong>%s</strong> — the plain matters known '
       u'from the religion by necessity (that grave-worship is shirk) — where '
       u'ignorance is <strong>no</strong> excuse for one among Muslims reached by '
       u'the Qurʾān; and <strong>%s</strong>, the subtle hidden matters, where it '
       u'can. The man who called on other than Allah «%s».</p>'
       % (ar(u'الأُمُورُ الظَّاهِرَة'),
          ar(u'الأُمُورُ الدَّقِيقَةُ الخَفِيَّة'),
          ar(u'يَكُونُ مُشْرِكًا... لِأَنَّ عَلَيْهِ أَنْ يَتَعَلَّم')),
       u'nq-l19-mani-al-jahl.html', u'Lesson 19'),
      (u'Distinguish البَيَان from التَّبَيُّن — and say why making the wrong '
       u'one the condition would wreck the whole matter.',
       u'<p style="margin:0">On al-Tawbah 9:115: what is obligatory is the '
       u'<strong>bayān</strong> — that the proof be conveyed and made clear — '
       u'«%s», even if <em>tabayyun</em> (the person’s actually grasping it) '
       u'never follows. <strong>Make tabayyun the condition and no stubborn '
       u'man is ever bound by any proof</strong> — he need only refuse to be '
       u'convinced.</p>'
       % ar(u'الوَاجِبُ قِيَامُ الحُجَّةِ فَقَط'),
       u'nq-l19-mani-al-jahl.html', u'Lesson 19'),
      (u'The man who told his family to burn him was excused. The '
       u'grave-worshipper is not. What is the difference, exactly?',
       u'<p style="margin:0">The burned man denied only a <strong>%s</strong> — '
       u'a buried detail of how far Allah’s power reaches — not Allah’s power '
       u'itself nor the resurrection, and «%s». The grave-worshipper denies the '
       u'<strong>plain root</strong>. «%s».</p>'
       % (ar(u'تَفْصِيلًا خَفِيًّا مِنْ تَفَاصِيلِ القُدْرَة'),
          ar(u'مِثْلُهُ يُجْهَل'),
          ar(u'الَّذِي يُعْذَرُ بِالجَهْلِ هُوَ الَّذِي يَجْهَلُ أَمْرًا دَقِيقًا خَفِيًّا')),
       u'nq-l19-mani-al-jahl.html', u'Lesson 19'),
      (u'The report that Muʿādh ؓ prostrated to the Prophet ﷺ is used to stretch '
       u'the excuse of ignorance over grave-worship. What is the ḥadīth-discipline '
       u'verdict on it?',
       u'<p style="margin:0">The prostration report is <strong>weak, even '
       u'bāṭil</strong> — al-Qāsim al-Shaybānī alone narrates it, with great '
       u'iḍṭirāb (five conflicting chains), and «%s». What is <em>ṣaḥīḥ '
       u'thābit</em> is the wording «%s» — <strong>without</strong> the '
       u'prostration. <em>And even granting Muʿādh’s question, it belonged to the '
       u'earliest Islam before the dīn settled.</em></p>'
       % (ar(u'مِثْلُهُ لَا يَحْتَمِلُ التَّفَرُّد'),
          ar(u'لَوْ كُنْتُ آمِرًا أَحَدًا أَنْ يَسْجُدَ لِأَحَد')),
       u'nq-l19-mani-al-jahl.html', u'Lesson 19'),
      (u'What is the barrier of honest error (الخَطَأ), with the sharḥ’s '
       u'example?',
       u'<p style="margin:0">On al-Baqarah 2:286: a word of kufr may leave a '
       u'Muslim’s tongue with no will behind it — «%s». The man who, from the '
       u'intensity of joy at his found mount, meant to say «You are my Lord and '
       u'I am Your servant» and said instead «%s» — the gravest inversion, and '
       u'no kufr, because the heart never moved toward it.</p>'
       % (ar(u'فَلَا يَكْفُرُ بِهَا؛ لِعَدَمِ القَصْد'),
          ar(u'اللَّهُمَّ أَنْتَ عَبْدِي وَأَنَا رَبُّك')),
       u'nq-l20-mani-al-khata-wa-al-tawil.html', u'Lesson 20'),
      (u'Interpretation (التَّأْوِيل) is the barrier most easily abused, so it '
       u'is cut both ways. Give both edges.',
       u'<p style="margin:0 0 .5rem"><strong>A corrupt taʾwīl of a clear text is '
       u'no excuse</strong> — «%s»; Iblīs reasoned against the plain command and '
       u'was not excused but sank deeper, and the Khawārij interpreted '
       u'sincerely, «%s», yet <span dir="rtl" lang="ar">مَرَقُوا</span> from '
       u'Islām.</p>'
       u'<p style="margin:0"><strong>But a taʾwīl in a genuine place of ikhtilāf '
       u'and shubhah does excuse</strong> — the woman who uncovers her face '
       u'thinking it allowed is «عَاصِيَة», not a disbeliever; one who denies the '
       u'siḥr ḥadīth is «مُخْطِئ», not cast out — while denying a plain matter '
       u'after bayān and persisting is kufr.</p>'
       % (ar(u'التَّأْوِيلُ الفَاسِدُ... لَيْسَ عُذْرًا؛ بَلْ زِيَادَةٌ فِي الكُفْر'),
          ar(u'بِاجْتِهَادٍ وَتَقَرُّبٍ إِلَى الله')),
       u'nq-l20-mani-al-khata-wa-al-tawil.html', u'Lesson 20'),
      (u'Read over all four barriers, state in one line what the capstone — and '
       u'the whole book — was built to establish.',
       u'<p style="margin:0"><strong>The ruling on an act and the ruling on a man '
       u'are two rulings.</strong> A deed may be a nullifier in its very type, '
       u'and the person who did it may yet not be a disbeliever — compelled, '
       u'ignorant of a hidden matter, slipping, or holding a doubt a doubt can '
       u'honestly hold. <em>The barriers are real; they are also only barriers — '
       u'lift them, with a cause of takfīr established, and the ruling falls.</em> '
       u'«%s».</p>'
       % ar(u'إِذَا وُجِدَ مُكَفِّرٌ كَفَر'),
       u'nq-l20-mani-al-khata-wa-al-tawil.html', u'Lesson 20'),
     ]),
]


def detail(n, q, a, href, label):
    return (
        u'<details style="border:1px solid var(--ivory-dark);'
        u'border-radius:var(--radius-md);background:white;'
        u'padding:var(--space-md) var(--space-lg);margin:0 0 .7rem">\n'
        u'  <summary style="cursor:pointer;font-size:.95rem;color:var(--ink);'
        u'line-height:1.8;font-weight:600;list-style:none">'
        u'<span style="color:var(--ink-faint);font-weight:400;font-size:.8rem;'
        u'margin-left:.4rem">%d</span> %s</summary>\n'
        u'  <div style="font-size:.92rem;color:var(--ink-mid);line-height:1.9;'
        u'margin-top:.8rem;padding-top:.8rem;border-top:1px solid var(--line)">%s\n'
        u'    <p style="margin:.75rem 0 0;font-size:.78rem">'
        u'<a href="%s" style="color:var(--teal-deep);font-weight:600">%s →</a></p>\n'
        u'  </div>\n</details>\n' % (n, q, a, href, label))


def divider(ar_t, en_t, sub):
    return (
        u'<div style="margin:var(--space-xl) 0 var(--space-md);padding-bottom:.6rem;'
        u'border-bottom:2px solid var(--brand)">\n'
        u'  <p style="font-family:var(--font-arabic);font-size:1.25rem;'
        u'direction:rtl;color:var(--teal-deep);font-weight:700;margin:0 0 2px">%s</p>\n'
        u'  <p style="font-size:.86rem;font-weight:600;color:var(--ink-mid);margin:0">%s'
        u'<span style="color:var(--ink-faint);font-weight:400"> · %s</span></p>\n'
        u'</div>\n' % (ar_t, en_t, sub))


intro = (
    u'<div style="background:var(--brand-wash);border:1px solid var(--brand);'
    u'border-radius:var(--radius-lg);padding:var(--space-lg);'
    u'margin-bottom:var(--space-lg)">\n'
    u'<p style="font-size:.93rem;color:var(--ink-mid);line-height:1.9;margin:0">'
    u'Read the question, answer it <strong>from memory and out loud</strong>, and '
    u'only then open the answer. An item you cannot answer is not a mark lost — it '
    u'is a lesson to go back to, and each one carries its link.</p>\n'
    u'<p style="font-size:.88rem;color:var(--ink-light);line-height:1.85;'
    u'margin:.7rem 0 0">This is not a test and nothing is recorded. It is the '
    u'check a student makes on himself before he says he has read a matn: '
    u'<span dir="rtl" lang="ar">هَلْ تَحْفَظُ المَعَانِيَ أَمْ قَرَأْتَ '
    u'فَحَسْب؟</span> — <em>do you hold the meanings, or did you merely '
    u'read?</em></p>\n</div>\n')

n = 0
body_parts = []
for ar_t, en_t, sub, items in PARTS:
    body_parts.append(divider(ar_t, en_t, sub))
    for q, a, href, label in items:
        n += 1
        body_parts.append(detail(n, q, a, href, label))

inner = (
    u'  <div style="max-width:860px;margin:0 auto;padding:var(--space-xl)">\n'
    u'    <a href="u6-nawaqid.html" style="font-size:.82rem;color:var(--ink-light);'
    u'text-decoration:none">← نَوَاقِضُ الإِسْلَام</a>\n\n'
    u'    <div class="lesson-card" style="margin-top:var(--space-md)">\n'
    u'      <div class="lesson-card-header">\n'
    u'        <span class="lesson-number">نَوَاقِضُ الإِسْلَام · المُرَاجَعَة</span>'
    u'<span class="year-badge" data-year="6">Year 6</span>\n'
    u'        <div class="lesson-title-wrap">\n'
    u'          <p class="lesson-title-ar">مُرَاجَعَةُ المَتْن</p>\n'
    u'          <p class="lesson-title-en">What You Should Now Know — a review of '
    u'the ten nullifiers and the barriers</p>\n'
    u'        </div>\n'
    u'      </div>\n\n'
    u'      <div class="lesson-card-body">\n\n'
    + intro + u''.join(body_parts) +
    u'\n      </div>\n'
    u'    </div>\n'
    u'  </div>\n')

pre = re.sub(r'<title>.*?</title>',
             u'<title>%s — What You Should Now Know | العقيدة | دار الهجرة</title>'
             % TITLE_AR, M.PRE, flags=re.S)
pre = re.sub(r'(<meta name="description" content=")(.*?)(">)',
             lambda m: m.group(1) + DESC + m.group(3), pre, count=1, flags=re.S)
post = re.sub(r'(<footer class="site-footer">.*?<p>)(.*?)(</p>)',
              lambda m: m.group(1) + B.FOOT + m.group(3), M.POST, count=1, flags=re.S)

html = pre + u'<main>\n' + inner + u'\n' + post
path = os.path.join(B.AQ, 'nawaqid-murajaah.html')
io.open(path, 'w', encoding='utf-8', newline='\n').write(html)
print('wrote nawaqid-murajaah.html — %d review items' % n)
