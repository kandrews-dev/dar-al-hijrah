# -*- coding: utf-8 -*-
"""Wasitiyyah L45 -- Part 6 opens: the reality of iman, the five positions on
its definition, that it increases and decreases, and the ruling on the one who
commits a major sin. Sharh pp.160-165."""
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
    'The ḥadīth «<span dir="rtl" lang="ar">لَا يَزْنِي الزَّانِي…</span>» is '
    '<strong>رَوَاهُ الشَّيْخَان</strong> — al-Bukhārī and Muslim, as the sharḥ notes.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Give the definition of %s with its four parts.' % ar('الإِيمَان'),
    'Distinguish %s from %s, and say which produces which.'
    % (ar('أَقْوَالُ القَلْب'), ar('أَعْمَالُ القَلْب')),
    'Name the five positions on the definition of īmān — and say what separates the Muʿtazilah '
    'from Ahl al-Sunnah, given that their definitions agree.',
    'Explain the difference between %s and %s.'
    % (ar('الإِيمَانُ المُطْلَق'), ar('مُطْلَقُ الإِيمَان')),
])

b += B.heading('القِسْمُ السَّادِس · حَقِيقَةُ الإِيمَانِ وَحُكْمُ مُرْتَكِبِ الكَبِيرَة',
               'Part Six — The Reality of Īmān, and the Ruling on the Major Sinner')
b += B.matn(
    'وَمِنْ أُصُولِ أَهْلِ السُّنَّةِ وَالجَمَاعَةِ: أَنَّ الدِّينَ وَالإِيمَانَ قَوْلٌ '
    'وَعَمَلٌ: قَوْلُ القَلْبِ وَاللِّسَانِ، وَعَمَلُ القَلْبِ وَاللِّسَانِ '
    'وَالجَوَارِحِ. وَأَنَّ الإِيمَانَ يَزِيدُ بِالطَّاعَةِ وَيَنْقُصُ '
    'بِالمَعْصِيَةِ. وَهُمْ مَعَ ذَلِكَ لَا يُكَفِّرُونَ أَهْلَ القِبْلَةِ بِمُطْلَقِ '
    'المَعَاصِي وَالكَبَائِرِ كَمَا يَفْعَلُهُ الخَوَارِجُ؛ بَلِ الأُخُوَّةُ '
    'الإِيمَانِيَّةُ ثَابِتَةٌ مَعَ المَعَاصِي. وَلَا يَسْلُبُونَ الفَاسِقَ المِلِّيَّ '
    'الإِسْلَامَ بِالكُلِّيَّةِ، وَلَا يُخَلِّدُونَهُ فِي النَّارِ كَمَا تَقُولُهُ '
    'المُعْتَزِلَةُ.')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>the foundations upon which their creed is '
      'built</strong></em>. So what follows is not a detail of the subject but one of its '
      'load-bearing walls.' % ar('وَمِنْ أُصُولِ أَهْلِ السُّنَّةِ وَالجَمَاعَةِ')) +
    p('<strong>%s</strong> — <em>is, in the language, <strong>submission and '
      'compliance</strong>; and in the Sharīʿah: <strong>what Allah commanded</strong></em>. '
      '<strong>%s</strong> — <em>in the language is <strong>affirming as true</strong></em>; and '
      'in the Sharīʿah it is what the author states:'
      % (ar('الدِّين'), ar('الإِيمَان'))) +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.97rem;text-align:center" dir="rtl" lang="ar">'
    '<strong>قَوْلٌ وَعَمَلٌ: قَوْلُ القَلْبِ وَاللِّسَانِ، وَعَمَلُ القَلْبِ '
    'وَاللِّسَانِ وَالجَوَارِحِ</strong></p></div>' +
    p('And al-Fawzān unpacks it into its four parts:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.91rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>قَوْلُ القَلْب</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<strong>الاعْتِقَاد</strong> — the creed held</td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>قَوْلُ اللِّسَان</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<strong>التَّكَلُّمُ بِكَلِمَةِ الإِسْلَام</strong> — uttering the word of '
    'Islam</td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>عَمَلُ القَلْب</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<strong>نِيَّةٌ وَإِخْلَاص</strong> — intention and sincerity</td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>عَمَلُ الجَوَارِح</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    'the limbs — <em>such as the prayer, the ḥajj, the jihād</em></td></tr>'
    '</table></div>')
b += B.sharh(
    p('And then a distinction most students never get told, which is the hinge of the whole '
      'definition. <strong>%s</strong>: <em>its <strong>sayings</strong> are '
      '<strong>the creedal matters it acknowledges and holds</strong>. As for its '
      '<strong>actions</strong>, they are <strong>its movement which Allah and His Messenger '
      'love</strong> — and that is <strong>the love of good and the firm resolve upon it, and the '
      'hatred of evil and the determination to leave it.</strong></em>'
      % ar('الفَرْقُ بَيْنَ أَقْوَالِ القَلْبِ وَأَعْمَالِه')) +
    p('So the heart does two different things: <strong>it holds a creed, and it moves.</strong> '
      'And then the causal claim that makes the rest of the definition inevitable:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.94rem"><em>— <strong>And the actions of the heart are '
    'what the actions of the limbs and the sayings of the tongue ARISE FROM. And from there, the '
    'sayings of the tongue and the actions of the limbs became part of '
    'īmān.</strong></em></p></div>' +
    p('That is the argument, and it is worth seeing that it is an argument rather than an '
      'assertion. <strong>The deeds are not bolted onto faith as an extra requirement; they are '
      'what faith in the heart <em>does</em> when it is there.</strong> A heart that genuinely '
      'loves good and resolves upon it produces prayer the way a root produces a branch — which '
      'is why removing the deeds from the definition removes the evidence that the root exists.'))

b += B.heading('أَقْوَالُ النَّاسِ فِي تَعْرِيفِ الإِيمَان',
               'Five Positions on the Definition of Īmān')
b += B.sharh(
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.89rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap;'
    'background:var(--brand-wash)"><strong>١</strong> '
    '<span dir="rtl" lang="ar">أَهْلُ السُّنَّةِ وَالجَمَاعَة</span></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line);'
    'background:var(--brand-wash)"><strong>belief in the heart, utterance with the tongue, and '
    'action with the limbs</strong></td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>٢ المُرْجِئَة</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">belief in the heart and '
    'utterance with the tongue <strong>only</strong></td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>٣ الكَرَّامِيَّة</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">utterance with the tongue '
    '<strong>only</strong></td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>٤ الجَبْرِيَّة</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">acknowledgement in the heart, '
    '<strong>or mere knowledge in the heart</strong></td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>٥ المُعْتَزِلَة</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">belief of the heart, '
    'utterance of the tongue, and action of the limbs — '
    '<strong>the same three</strong></td></tr>'
    '</table></div>' +
    p('Look at row 5 and row 1. <strong>The Muʿtazilah define īmān exactly as Ahl al-Sunnah '
      'do.</strong> So al-Fawzān has to say where the parting is, and it is not in the definition '
      'at all:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.94rem"><em>— <strong>the difference between them is that '
    'with the Muʿtazilah the committer of a major sin is stripped of the name of '
    'īmān ENTIRELY and abides forever in the Fire; and with Ahl al-Sunnah he is not '
    'stripped of īmān entirely — rather he is a believer deficient in '
    'īmān, and does not abide forever in the Fire if he enters it.</strong></em></p></div>' +
    p('<strong>Same premise, opposite conclusion.</strong> Which is the most useful thing in this '
      'lesson for reading modern arguments: it shows that «deeds are part of īmān» does not by '
      'itself settle anything. <strong>The question that divides is what follows when a deed is '
      'missing</strong> — and the answer turns on whether īmān has <em>degrees</em>, which is the '
      'next clause of the matn.') +
    p('<em>And <strong>all of these are false statements, and the truth is what Ahl al-Sunnah '
      'wa-l-Jamāʿah said, for many proofs.</strong></em>'))

b += B.heading('يَزِيدُ بِالطَّاعَةِ وَيَنْقُصُ بِالمَعْصِيَة',
               'It Increases with Obedience and Decreases with Disobedience')
b += B.sharh(
    p('<em>That is: and of the foundations of Ahl al-Sunnah is '
      '<strong>that īmān admits of degrees by increase and decrease</strong> — '
      '<strong>obedience increases it and disobedience diminishes it</strong>; and many proofs '
      'indicate that.</em> The student met this in Lesson 28, drawn out of the single word '
      '<em>afḍal</em>; here it is stated as a principle with its texts.'))
b += B.ayah(
    'إِنَّمَا الْمُؤْمِنُونَ الَّذِينَ إِذَا ذُكِرَ اللَّهُ وَجِلَتْ قُلُوبُهُمْ وَإِذَا '
    'تُلِيَتْ عَلَيْهِمْ آيَاتُهُ زَادَتْهُمْ إِيمَانًا وَعَلَى رَبِّهِمْ يَتَوَكَّلُونَ',
    '"The believers are only those who, when Allah is mentioned, their hearts tremble; and when '
    'His āyāt are recited to them, they increase them in faith; and upon their Lord they rely."',
    'Sūrat al-Anfāl 8:2 · سُورَةُ الأَنْفَال')
b += B.ayah(
    'لِيَزْدَادُوا إِيمَانًا مَعَ إِيمَانِهِمْ',
    '"That they might increase in faith, along with their faith."',
    'Sūrat al-Fatḥ 48:4 · سُورَةُ الفَتْح')
b += B.sharh(
    p('al-Fawzān glosses the first: <strong>%s</strong> — <em>that is: '
      '<strong>His greatness and His power are mentioned, and what He warned of to whoever '
      'disobeys Him</strong></em>; <strong>%s</strong> — <em>that is: <strong>they '
      'feared</strong></em>; <strong>%s</strong> — <em>that is: <strong>His revealed āyāt are '
      'recited, or His universal signs are called to mind</strong></em>; '
      '<strong>%s</strong> — <em>that is: <strong>their faith increased by reason of '
      'that</strong></em>; <strong>%s</strong> — <em>that is: '
      '<strong>they commit all their affairs to Him, not to another.</strong></em>'
      % (ar('إِذَا ذُكِرَ اللَّهُ'), ar('وَجِلَتْ قُلُوبُهُمْ'),
         ar('وَإِذَا تُلِيَتْ عَلَيْهِمْ آيَاتُهُ'), ar('زَادَتْهُمْ إِيمَانًا'),
         ar('وَعَلَى رَبِّهِمْ يَتَوَكَّلُونَ'))))

b += B.heading('لَا يُكَفِّرُونَ أَهْلَ القِبْلَةِ بِمُطْلَقِ المَعَاصِي',
               'They Do Not Declare the People of the Qiblah Disbelievers for Sins')
b += B.sharh(
    p('<em>That is: <strong>Ahl al-Sunnah, although they hold that the deeds enter into what is '
      'named by īmān, and that it increases with obedience and decreases with disobedience — they '
      'nevertheless do not rule with disbelief upon one who claims Islam and faces the Kaʿbah, '
      'merely for his committing sins which are short of shirk and disbelief</strong></em> — '
      '<strong>%s</strong>, <em>who said: <strong>whoever commits a major sin is, in this world, '
      'a disbeliever, and in the Hereafter abides forever in the Fire, never coming out of '
      'it.</strong></em>' % ar('كَمَا يَفْعَلُهُ الخَوَارِجُ')) +
    p('And then the author\'s proof that <strong>%s</strong> — '
      '<em>the brotherhood of faith stands together with the sins; <strong>so the disobedient one '
      'is our brother in faith.</strong></em>'
      % ar('الأُخُوَّةُ الإِيمَانِيَّةُ ثَابِتَةٌ مَعَ المَعَاصِي')))
b += B.ayah(
    'فَمَنْ عُفِيَ لَهُ مِنْ أَخِيهِ شَيْءٌ فَاتِّبَاعٌ بِالْمَعْرُوفِ وَأَدَاءٌ إِلَيْهِ '
    'بِإِحْسَانٍ',
    '"And whoever is pardoned something by his brother — then a fair demand, and payment to him '
    'in good measure."',
    'Sūrat al-Baqarah 2:178 · سُورَةُ البَقَرَة')
b += B.sharh(
    p('<em>The meaning: <strong>that when the one who committed the offence is pardoned by the '
      'victim or his guardian from the retaliation, and he is content to take the wealth as '
      'blood-money — then it is upon the one entitled to the money to demand it in a fair way, '
      'without harshness; and upon the one who owes it to pay it without delay.</strong></em>') +
    p('And now the point of evidence, which is the whole reason the author quoted a verse about '
      'blood-money in a chapter on faith: <em>and <strong>the manner of the proof from the āyah is '
      'that He named the killer a BROTHER of the one killed</strong> — '
      '<strong>even though killing is one of the major sins — and even so, the brotherhood of '
      'faith did not depart from him.</strong></em>') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.94rem">That is as strong a case as the question admits. '
    '<strong>If any sin were going to sever the brotherhood, it would be the one where a man has '
    'killed the brother in question</strong> — and the āyah, legislating for exactly '
    'that situation, still calls him <span dir="rtl" lang="ar">أَخِيهِ</span>.</p></div>')
b += B.ayah(
    'وَإِنْ طَائِفَتَانِ مِنَ الْمُؤْمِنِينَ اقْتَتَلُوا فَأَصْلِحُوا بَيْنَهُمَا فَإِنْ '
    'بَغَتْ إِحْدَاهُمَا عَلَى الْأُخْرَى فَقَاتِلُوا الَّتِي تَبْغِي حَتَّى تَفِيءَ '
    'إِلَى أَمْرِ اللَّهِ',
    '"And if two parties of the believers fight each other, make peace between them. But if one '
    'of them transgresses against the other, then fight the one that transgresses until it returns '
    'to the command of Allah."',
    'Sūrat al-Ḥujurāt 49:9 · سُورَةُ الحُجُرَات')
b += B.ayah(
    'إِنَّمَا الْمُؤْمِنُونَ إِخْوَةٌ فَأَصْلِحُوا بَيْنَ أَخَوَيْكُمْ',
    '"The believers are but brothers, so make peace between your two brothers."',
    'Sūrat al-Ḥujurāt 49:10 · سُورَةُ الحُجُرَات')
b += B.sharh(
    p('<em>And the manner of the proof from the two noble āyāt is that '
      '<strong>He named them BELIEVERS despite the existence of the fighting and the transgression '
      'between them, and named them BROTHERS of the believers</strong> with His saying %s.</em>'
      % ar('فَأَصْلِحُوا بَيْنَ أَخَوَيْكُمْ')) +
    p('A point of Arabic on the last clause: <em>and <strong>the singling out of the two for '
      'mention is to establish the obligation of making peace in what is more than two, by way of '
      'the stronger case</strong></em> — if peace must be made between two, then all the more '
      'between twenty.') +
    p('<strong>%s</strong> — <em>a fresh sentence, confirming what came before it of the command '
      'to make peace</em>; <em>and the meaning is that '
      '<strong>they return to one single matter, which is faith — so they are brothers in '
      'religion.</strong></em>' % ar('إِنَّمَا الْمُؤْمِنُونَ إِخْوَةٌ')))

b += B.heading('الفَاسِقُ المِلِّيّ', 'The Fāsiq Who Is Still of the Millah')
b += B.sharh(
    p('<strong>%s</strong> — <em>al-fisq is <strong>going outside the obedience of '
      'Allah</strong>; and what is meant by the fāsiq here is <strong>the one who commits some of '
      'the major sins — such as drinking wine, fornication and theft — '
      '<em>while holding that these are forbidden</em>.</strong></em>'
      % ar('الفَاسِق')) +
    p('<strong>That qualification is doing essential work.</strong> The man described here '
      '<em>agrees</em> that what he did is forbidden. Someone who held it lawful would be in a '
      'different case entirely — and that is the line between a sinner and an apostate, stated in '
      'four words.') +
    p('<strong>%s</strong> — <em>that is: <strong>the one who is upon the millah of Islam and has '
      'not committed of the sins what necessitates his disbelief</strong></em>. '
      '<em>So Ahl al-Sunnah <strong>do not strip him of Islam entirely</strong> and rule him a '
      'disbeliever, as the Khawārij say of him in this world; <strong>and they do not rule him to '
      'abide forever in the Fire</strong> in the Hereafter, <strong>as the Muʿtazilah say</strong> '
      '— and the Khawārij. For the Muʿtazilah hold that the fāsiq is called neither a Muslim nor '
      'a disbeliever, but is with them <strong>%s</strong>; that is his ruling with them in this '
      'world, and in the Hereafter he abides forever in the Fire.</em>'
      % (ar('المِلِّيّ'), ar('بِالمَنْزِلَةِ بَيْنَ المَنْزِلَتَيْن'))))

b += B.heading('الإِيمَانُ المُطْلَقُ وَمُطْلَقُ الإِيمَان',
               'Absolute Īmān, and Īmān Unrestrictedly')
b += B.sharh(
    p('Now the resolution, and it turns on a pair of phrases that differ only in word order. '
      'al-Fawzān states the author\'s two halves and then defines the terms at the very end — so '
      'take the definitions first:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.93rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>الإِيمَانُ المُطْلَق</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<strong>the COMPLETE īmān</strong> — īmān without '
    'qualification</td></tr>'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>مُطْلَقُ الإِيمَان</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<strong>the DEFICIENT īmān</strong> — some īmān, unspecified</td></tr>'
    '</table></div>' +
    p('Two words, reversed, and two different doctrines. <strong>The fāsiq has <em>muṭlaq '
      'al-īmān</em> and not <em>al-īmān al-muṭlaq</em></strong> — he has faith, and he does not '
      'have faith entire.') +
    p('And each half has its proof. <em>The fāsiq <strong>DOES enter</strong> under the name of '
      'īmān unrestrictedly — the one that takes in both the complete and the deficient — as in '
      'His saying %s. <strong>For whoever frees a believing slave, even if the one freeing is '
      'himself a fāsiq, in what requires the freed slave\'s faith — as in the expiation for '
      'ẓihār and for killing — that freeing suffices him, by the agreement of the scholars</strong>, '
      'because it enters into the generality of the āyah even if the one freed is not of the '
      'people of complete faith.</em>' % ar('فَتَحْرِيرُ رَقَبَةٍ مُؤْمِنَةٍ')))
b += B.ayah(
    'وَمَنْ قَتَلَ مُؤْمِنًا خَطَأً فَتَحْرِيرُ رَقَبَةٍ مُؤْمِنَةٍ وَدِيَةٌ مُسَلَّمَةٌ '
    'إِلَى أَهْلِهِ',
    '"And whoever kills a believer by mistake — then the freeing of a believing slave, and '
    'blood-money handed over to his family."',
    'Sūrat al-Nisāʾ 4:92 · سُورَةُ النِّسَاء')
b += B.sharh(
    p('<em>And he <strong>may NOT enter</strong> under the name of absolute īmān — that is, when '
      'what is intended by īmān is <strong>the complete</strong> — as in His saying %s; '
      '<strong>because what is meant by the īmān mentioned in that noble āyah is the complete '
      'īmān, so the fāsiq does not enter into it, because his īmān is deficient.</strong></em>'
      % ar('إِنَّمَا الْمُؤْمِنُونَ الَّذِينَ إِذَا ذُكِرَ اللَّهُ وَجِلَتْ قُلُوبُهُمْ')) +
    p('<strong>%s</strong> there <em>is a particle of restriction, which establishes the ruling '
      'for the one mentioned and negates it of everyone else</em> — which is exactly why the āyah '
      'can exclude a man the other āyah includes. <strong>Two āyāt, two senses of one word, and no '
      'conflict.</strong>' % ar('إِنَّمَا')))
b += B.hadith(
    'لَا يَزْنِي الزَّانِي حِينَ يَزْنِي وَهُوَ مُؤْمِنٌ، وَلَا يَسْرِقُ السَّارِقُ حِينَ '
    'يَسْرِقُ وَهُوَ مُؤْمِنٌ، وَلَا يَشْرَبُ الخَمْرَ حِينَ يَشْرَبُهَا وَهُوَ '
    'مُؤْمِنٌ، وَلَا يَنْتَهِبُ نُهْبَةً ذَاتَ شَرَفٍ يَرْفَعُ النَّاسُ إِلَيْهِ فِيهَا '
    'أَبْصَارَهُمْ حِينَ يَنْتَهِبُهَا وَهُوَ مُؤْمِنٌ',
    '"The fornicator does not fornicate while he is a believer; the thief does not steal while he '
    'is a believer; the wine-drinker does not drink it while he is a believer; nor does he seize a '
    'plunder of note, at which people raise their eyes to him, while he is a believer."',
    'رَوَاهُ الشَّيْخَان — al-Bukhārī and Muslim')
b += B.sharh(
    p('<em>That is: <strong>complete in īmān</strong>. <strong>So what is negated here of the '
      'fornicator, the thief and the drinker is the COMPLETENESS of īmān, not the whole of '
      'it</strong></em> — and al-Fawzān gives a proof for that reading which settles the matter '
      'from an unexpected direction:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.94rem"><em>— <strong>by the proof of the consensus on the '
    'inheritance of the fornicator, the thief and the wine-drinker.</strong></em></p>'
    '<p style="margin:.5rem 0 0;font-size:.92rem">A Muslim does not inherit from a disbeliever. '
    'So the agreed-upon fact that <strong>these men still inherit</strong> proves that the '
    'īmān the ḥadīth denies them cannot be the īmān that makes a '
    'man a Muslim. <strong>The fiqh settles the ʿaqīdah.</strong></p></div>' +
    p('<em>So the ḥadīth indicated that these people, at the time of their doing the sin, '
      '<strong>have had the complete īmān negated of them</strong>; and the many texts of the '
      'Book and the Sunnah have indicated that <strong>they are not apostates by that</strong>. '
      '<strong>So it is known that the īmān negated in this ḥadīth is only the completeness of '
      'the obligatory īmān.</strong></em>') +
    p('And the vocabulary: <strong>%s</strong> — <em>with a ḍammah on the nūn, is '
      '<strong>the thing plundered</strong>; and al-nahb is <strong>the taking of wealth by '
      'overpowering and force</strong></em>. <strong>%s</strong> — <em>that is: '
      '<strong>of consequence</strong>; and it has been said: <strong>one at which people crane '
      'to look, raising their eyes to it.</strong></em>'
      % (ar('النُّهْبَة'), ar('ذَاتَ شَرَفٍ'))))
b += B.sharh(
    p('And then the author\'s verdict, which al-Fawzān calls <strong>%s — the just ruling</strong>, '
      '<em>joining together the texts which negated īmān of him</em> — like «the fornicator does '
      'not fornicate while a believer» — <em>and the texts which affirmed īmān for him</em> — the '
      'āyah of retaliation and the āyah on the transgressing parties:'
      % ar('الحُكْمُ العَادِل')) +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.98rem;text-align:center" dir="rtl" lang="ar">'
    '<strong>هُوَ مُؤْمِنٌ نَاقِصُ الإِيمَانِ، أَوْ مُؤْمِنٌ بِإِيمَانِهِ فَاسِقٌ '
    'بِكَبِيرَتِهِ</strong></p>'
    '<p style="margin:.55rem 0 0;font-size:.92rem;text-align:center"><em>— '
    '<strong>he is a believer deficient in faith; or: a believer by his faith, a fāsiq by '
    'his major sin.</strong></em></p></div>' +
    p('<em>And upon that basis: <strong>%s</strong></em> — <em>that is, the name of complete '
      'īmān</em> — <em><strong>%s</strong></em> — <em>that is, the deficient īmān.</em>'
      % (ar('فَلَا يُعْطَى الاسْمَ المُطْلَقَ'), ar('وَلَا يُسْلَبُ مُطْلَقَ الاسْمِ'))) +
    p('Read the second formula slowly, because it is the finest thing in the lesson: '
      '<strong>a believer <em>by his faith</em>, a fāsiq <em>by his major sin</em>.</strong> '
      'Each name is given on the ground that earns it, and neither cancels the other. '
      '<strong>The Khawārij gave him only the second name; the Murjiʾah gave him only the first; '
      'and the author gives him both, each with its own cause attached.</strong>') +
    p('That is the pattern of Lesson 30 one last time, and it has never varied: '
      '<strong>each sect kept the set of texts it could hold and discarded the rest, and the '
      'middle position is the one that has to throw nothing away.</strong>'))

b += B.vocab([
    ('الدِّين', 'al-dīn', 'the religion',
     'Linguistically: submission and compliance; in the Sharīʿah: what Allah commanded'),
    ('قَوْلُ القَلْب', 'qawl al-qalb', 'the saying of the heart',
     'الاعْتِقَاد — the creedal matters it acknowledges and holds'),
    ('عَمَلُ القَلْب', 'ʿamal al-qalb', 'the action of the heart',
     'Its movement which Allah loves — love of good, resolve upon it, hatred of evil. '
     'The deeds of the limbs ARISE from it'),
    ('الكَرَّامِيَّة', 'al-karrāmiyyah', 'the Karrāmiyyah',
     'Īmān is utterance of the tongue ONLY — the third of the five positions'),
    ('الفِسْق', 'al-fisq', 'going outside obedience',
     'And the fāsiq here commits major sins **while holding them forbidden**'),
    ('المِلِّيّ', 'al-millī', 'one still of the millah',
     'Upon the millah of Islam, having not committed what necessitates disbelief'),
    ('الإِيمَانُ المُطْلَق', 'al-īmān al-muṭlaq', 'absolute īmān',
     'The COMPLETE īmān — which the fāsiq is not given'),
    ('مُطْلَقُ الإِيمَان', 'muṭlaq al-īmān', 'īmān unrestrictedly',
     'The DEFICIENT īmān — which is not stripped from him'),
    ('النُّهْبَة', 'al-nuhbah', 'the plunder',
     'The thing seized; al-nahb is taking wealth by overpowering and force'),
])
b += B.mcq('ws-l45', [
    ('What are the four parts of īmān in the author’s definition?',
     ['Belief, utterance, prayer and charity',
      'Saying of the heart (belief), saying of the tongue (the word of Islam), action of the '
      'heart (intention and sincerity), and action of the limbs',
      'Knowledge, action, calling to it and patience',
      'Islam, īmān, iḥsān and taqwā'], 1),
    ('What is the difference between the sayings of the heart and its actions?',
     ['The sayings are spoken aloud, the actions are hidden',
      'Its sayings are the creedal matters it holds; its actions are its movement — love of good '
      'and resolve upon it, hatred of evil and determination to leave it',
      'Its sayings are obligatory and its actions recommended',
      'There is no difference; they are two names for one thing'], 1),
    ('What follows from the actions of the heart, per al-Fawzān?',
     ['They are the whole of īmān',
      'The actions of the limbs and the sayings of the tongue ARISE from them — and from there '
      'the limbs and the tongue became part of īmān',
      'They are known only to Allah and so are not part of īmān',
      'They vary from person to person'], 1),
    ('How do the Muʿtazilah define īmān?',
     ['Belief in the heart only',
      'Belief of the heart, utterance of the tongue and action of the limbs — the same three as '
      'Ahl al-Sunnah',
      'Utterance of the tongue only',
      'Mere knowledge in the heart'], 1),
    ('So what separates them from Ahl al-Sunnah?',
     ['Their definition of al-dīn',
      'Not the definition but the consequence: with them the major sinner is stripped of the name '
      'of īmān entirely and abides forever in the Fire',
      'Their position on the Companions',
      'Their denial that īmān increases'], 1),
    ('How does the āyah of retaliation prove the brotherhood of faith survives sin?',
     ['Because it commands forgiveness',
      'Because it names the killer a BROTHER of the one killed, though killing is a major sin',
      'Because it mentions blood-money', 'Because it addresses the believers'], 1),
    ('What qualification does al-Fawzān attach to the fāsiq in this discussion?',
     ['That his sins are few',
      'That he commits the major sins <em>while holding that they are forbidden</em>',
      'That he has not been warned', 'That he repents afterwards'], 1),
    ('What is the difference between %s and %s?'
     % (ar('الإِيمَانُ المُطْلَق'), ar('مُطْلَقُ الإِيمَان')),
     ['They are two names for the same thing',
      'Al-īmān al-muṭlaq is the COMPLETE īmān; muṭlaq al-īmān is the DEFICIENT īmān — the fāsiq '
      'has the second and not the first',
      'One is the faith of the prophets, the other of the common people',
      'One is inward and the other outward'], 1),
    ('What proof settles that the ḥadīth negates only the completeness of īmān?',
     ['The consensus of the mufassirūn',
      'The consensus on the INHERITANCE of the fornicator, thief and wine-drinker — a Muslim does '
      'not inherit from a disbeliever',
      'That the ḥadīth is reported by both Shaykhs',
      'That the sins named are only three'], 1),
])
b += B.tf('ws-l45-tf', [
    ('الإِيمَانُ قَوْلٌ وَعَمَلٌ عِنْدَ أَهْلِ السُّنَّةِ.',
     'Īmān is saying and action, according to Ahl al-Sunnah.', True),
    ('المُعْتَزِلَةُ يُوَافِقُونَ أَهْلَ السُّنَّةِ فِي تَعْرِيفِ الإِيمَانِ.',
     'The Muʿtazilah agree with Ahl al-Sunnah in the definition of īmān.', True),
    ('الأُخُوَّةُ الإِيمَانِيَّةُ تَزُولُ بِالكَبِيرَةِ.',
     'The brotherhood of faith departs with a major sin.', False),
    ('المَنْفِيُّ فِي حَدِيثِ «لَا يَزْنِي الزَّانِي» هُوَ جَمِيعُ الإِيمَانِ.',
     'What is negated in the ḥadīth "the fornicator does not fornicate…" is the whole of īmān.',
     False),
])
b += B.memorize(
    'هُوَ مُؤْمِنٌ نَاقِصُ الإِيمَانِ، أَوْ مُؤْمِنٌ بِإِيمَانِهِ فَاسِقٌ بِكَبِيرَتِهِ',
    'The second formula is the one to carry: <em>a believer by his faith, a fāsiq by his major '
    'sin.</em> Each name given on the ground that earns it, and neither cancelling the other. '
    'The Khawārij gave him only the second; the Murjiʾah only the first.')
b += B.aiquiz('The reality of iman and the ruling on the major sinner in al-Aqidah al-Wasitiyyah: '
              'the four parts of the definition, the difference between the sayings of the heart '
              'and its actions and why the deeds of the limbs ARISE from the latter, the five '
              'positions on the definition and why the Mutazilah agree with Ahl al-Sunnah in the '
              'definition but differ in the consequence, how the ayah of retaliation names the '
              'killer a brother, the fasiq milli who holds his sins forbidden, the distinction '
              'between al-iman al-mutlaq and mutlaq al-iman, and the consensus on inheritance as '
              'the proof that the hadith negates only completeness')
b += B.further()
b += B.nav('was-l44-afal-al-ibad.html', 'The Acts of the Servants',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l45')

io.open(os.path.join(B.AQ, 'was-l45-haqiqat-al-iman.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'حَقِيقَةُ الإِيمَانِ وَحُكْمُ مُرْتَكِبِ الكَبِيرَة',
    'The Reality of Īmān, and the Ruling on the Major Sinner',
    'Lesson 45 of al-ʿAqīdah al-Wāsiṭiyyah, opening Part 6: '
    'īmān in its four parts and why the deeds of the limbs arise from the action of the '
    'heart; the five positions on its definition, and why the Muʿtazilah share Ahl '
    'al-Sunnah’s definition yet part from them on the consequence; and the two phrases that '
    'differ only in word order — al-īmān al-muṭlaq and muṭlaq '
    'al-īmān.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الخَامِسُ وَالأَرْبَعُون', '6',
           'حَقِيقَةُ الإِيمَانِ وَحُكْمُ مُرْتَكِبِ الكَبِيرَة',
           'The Reality of Īmān, and the Ruling on the Major Sinner', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l45-haqiqat-al-iman.html')
