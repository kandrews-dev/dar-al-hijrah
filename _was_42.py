# -*- coding: utf-8 -*-
"""Wasitiyyah L42 -- Part 5 opens: belief in al-qadar, its four levels, and the
first degree -- the knowledge and the writing. With the general and the
particular decree. Sharh pp.146-151."""
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
    'The ḥadīth of the Pen is reported by <strong>أَبُو دَاوُد</strong> in his <em>Sunan</em> '
    'from <strong>عُبَادَةَ بْنِ الصَّامِتِ</strong> رضي الله عنه; the ḥadīth of the foetus from '
    '<strong>ابْنِ مَسْعُود</strong> رضي الله عنه.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Define %s and name its four %s.' % (ar('القَدَر'), ar('مَرَاتِب')),
    'Say why the author treats the knowledge and the writing as one degree.',
    'Give both readings of %s and the meaning each yields.'
    % ar('أَوَّلُ مَا خَلَقَ اللهُ القَلَم'),
    'Name the three kinds of particular decree, each with its proof.',
])

b += B.heading('القِسْمُ الخَامِس · الإِيمَانُ بِالقَدَر',
               'Part Five — Belief in the Decree')
b += B.matn(
    'وَتُؤْمِنُ الفِرْقَةُ النَّاجِيَةُ — أَهْلُ السُّنَّةِ وَالجَمَاعَةِ — بِالقَدَرِ '
    'خَيْرِهِ وَشَرِّهِ. وَالإِيمَانُ بِالقَدَرِ عَلَى دَرَجَتَيْنِ، كُلُّ دَرَجَةٍ '
    'تَتَضَمَّنُ شَيْئَيْنِ.')
b += B.sharh(
    p('<strong>%s</strong> — <em>is a maṣdar of <strong>%s</strong>, when you '
      '<strong>encompass its measure</strong>; and what is intended by it here is: '
      '<strong>the attachment of Allah\'s knowledge to the things that come to be, and His will '
      'for them, in eternity before their existence.</strong> '
      '<strong>So there is no event but Allah has decreed it</strong> — that is, '
      '<strong>His knowledge of it preceded, and His will attached to it.</strong></em>'
      % (ar('القَدَر'), ar('قَدَرْتَ الشَّيْءَ'))) +
    p('And the obligation: <em>belief in al-qadar is <strong>one of the six pillars of '
      'faith</strong>; and it is <strong>belief in the decree, its good and its evil.</strong></em>') +
    p('al-Fawzān then notices what the author\'s phrasing implies, and it is a sharp reading: '
      '<em>in the Shaykh\'s saying <strong>«and the saved sect — Ahl al-Sunnah wa-l-Jamāʿah — '
      'believe in al-qadar»</strong> is <strong>an indication that whoever does not believe in '
      'al-qadar is not of Ahl al-Sunnah wa-l-Jamāʿah</strong>.</em> '
      '<em>And this is what the texts require, as in the ḥadīth of Jibrīl, when he asked the '
      'Prophet &#65018; about faith, and he said: <strong>«faith is that you believe in Allah, '
      'His angels, His Books, His Messengers and the Last Day, and that you believe in the '
      'decree, its good and its evil»</strong> — so he &#65018; '
      '<strong>made belief in al-qadar the sixth of the pillars of faith; so whoever denies it is '
      'not a believer, just as if he had not believed in another of the pillars.</strong></em>') +
    p('The student met that ḥadīth in full on the Islam 101 track. '
      '<strong>Here it does the work of establishing that this part of the book is not an '
      'advanced topic but one sixth of the minimum.</strong>'))

b += B.heading('مَرَاتِبُ القَدَرِ الأَرْبَع', 'The Four Levels of the Decree')
b += B.sharh(
    p('<em>And the Shaykh mentioned here that <strong>belief in al-qadar comprises four levels, '
      'which in summary are as follows</strong>:</em>') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.91rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>الأُولَى · العِلْم</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<strong>Allah’s eternal knowledge of everything</strong> — and of that is '
    '<strong>His knowledge of the deeds of the servants before they do them</strong></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>الثَّانِيَة · الكِتَابَة</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<strong>the writing of that in al-Lawḥ al-Maḥfūẓ</strong></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>الثَّالِثَة · المَشِيئَة</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<strong>His all-embracing volition and His complete power over every event</strong></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>الرَّابِعَة · الخَلْق</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<strong>Allah’s bringing all created things into being</strong> — and '
    '<strong>that He is the Creator and everything besides Him is created</strong></td></tr>'
    '</table></div>' +
    p('And a note on the counting, which otherwise confuses the reader: '
      '<strong>the author speaks of two <em>degrees</em>, each comprising two things</strong> — so '
      'the four <em>levels</em> are grouped into two pairs. '
      '<em>al-Fawzān remarks on this where the author calls the volition «the second»: '
      '<strong>he reckoned it so because he made the knowledge and the writing a single '
      'degree.</strong></em>') +
    p('Which is not arbitrary. <strong>The first pair is about what Allah knew and recorded; the '
      'second is about what He willed and brought about.</strong> Knowing and writing belong '
      'together because neither of them makes anything happen.'))

b += B.heading('الدَّرَجَةُ الأُولَى · العِلْمُ وَالكِتَابَة',
               'The First Degree — the Knowledge and the Writing')
b += B.matn(
    'فَالدَّرَجَةُ الأُولَى: الإِيمَانُ بِأَنَّ اللهَ تَعَالَى عَلِيمٌ بِمَا الخَلْقُ '
    'عَامِلُونَ، بِعِلْمِهِ القَدِيمِ الَّذِي هُوَ مَوْصُوفٌ بِهِ أَزَلًا وَأَبَدًا، '
    'وَعَلِمَ جَمِيعَ أَحْوَالِهِمْ مِنَ الطَّاعَاتِ وَالمَعَاصِي وَالأَرْزَاقِ '
    'وَالآجَالِ. ثُمَّ كَتَبَ اللهُ فِي اللَّوْحِ المَحْفُوظِ مَقَادِيرَ الخَلْقِ: '
    'فَأَوَّلُ مَا خَلَقَ اللهُ القَلَمَ قَالَ لَهُ: اكْتُبْ. قَالَ: مَا أَكْتُبُ؟ '
    'قَالَ: اكْتُبْ مَا هُوَ كَائِنٌ إِلَى يَوْمِ القِيَامَةِ. فَمَا أَصَابَ '
    'الإِنْسَانَ لَمْ يَكُنْ لِيُخْطِئَهُ، وَمَا أَخْطَأَهُ لَمْ يَكُنْ '
    'لِيُصِيبَهُ. جَفَّتِ الأَقْلَامُ وَطُوِيَتِ الصُّحُفُ.')
b += B.sharh(
    p('The vocabulary first, as al-Fawzān gives it: <strong>%s</strong> — '
      '<em>is <strong>the pre-eternity which has no beginning</strong></em>; '
      '<strong>%s</strong> — <em>is <strong>the perpetuity in the future which has no '
      'end</strong></em>.' % (ar('أَزَلًا'), ar('أَبَدًا'))) +
    p('<strong>%s</strong> — <em>the plural of %s, and it is <strong>agreement with the '
      'command</strong></em>. <strong>%s</strong> — <em>the plural of %s, and it is '
      '<strong>contravening the command</strong></em>. <strong>%s</strong> — <em>the plural of '
      '%s, and it is <strong>what benefits</strong></em>. <strong>%s</strong> — <em>the plural of '
      '%s, and it is <strong>the duration of a thing</strong>; and a man\'s ajal is '
      '<strong>the end of his time in this world, by death</strong></em>.'
      % (ar('الطَّاعَات'), ar('طَاعَة'), ar('المَعَاصِي'), ar('مَعْصِيَة'),
         ar('الأَرْزَاق'), ar('رِزْق'), ar('الآجَال'), ar('أَجَل'))) +
    p('<strong>%s</strong> — <em>and it is <strong>%s — the Mother of the Book</strong>; '
      '<strong>%s — guarded from any addition to it or subtraction from it.</strong></em>'
      % (ar('اللَّوْحُ المَحْفُوظ'), ar('أُمُّ الكِتَاب'), ar('مَحْفُوظ'))))
b += B.sharh(
    p('<strong>المَرْتَبَةُ الأُولَى</strong> — <em>belief in <strong>Allah\'s knowledge, '
      'encompassing everything of the existent and the non-existent</strong>; '
      '<strong>this knowledge which is an attribute of His attributes of the Essence, with which '
      'He never ceases to be described, in eternity and perpetually.</strong> And of that is '
      '<strong>His knowledge of the deeds of the creation — of the acts of obedience and of '
      'disobedience — and His knowledge of their states, of the provisions and the appointed '
      'terms and other things.</strong></em>') +
    p('Note the phrase <strong>%s — the existent and the non-existent.</strong> That is the '
      'reach of it: not only what is and was, <strong>but what never happened</strong>. The '
      'knowledge is not a record of events; it is complete independently of whether they occur.'
      % ar('المَوْجُودَاتِ وَالمَعْدُومَات')) +
    p('<strong>المَرْتَبَةُ الثَّانِيَة</strong> — <em><strong>the level of the writing</strong>: '
      'that <strong>Allah wrote in al-Lawḥ al-Maḥfūẓ the measures of the creation</strong>; '
      '<strong>so nothing occurs in the universe but Allah knew it and wrote it before it '
      'occurred.</strong></em>'))
b += B.hadith(
    'أَوَّلُ مَا خَلَقَ اللهُ القَلَمَ، فَقَالَ لَهُ: اكْتُبْ. قَالَ: وَمَا أَكْتُبُ؟ '
    'قَالَ: اكْتُبْ مَقَادِيرَ كُلِّ شَيْءٍ حَتَّى تَقُومَ السَّاعَةُ',
    '"The first thing Allah created was the Pen. He said to it: write. It said: and what shall I '
    'write? He said: write the measures of everything until the Hour comes."',
    'رَوَاهُ أَبُو دَاوُدَ فِي سُنَنِهِ — from ʿUbādah ibn al-Ṣāmit رضي الله عنه')
b += B.sharh(
    p('<em>So this ḥadīth indicates <strong>the level of the writing, and that the measures are '
      'all of them written.</strong></em>') +
    p('And then a point of vowelling with two whole meanings hanging on it. '
      '<em><strong>%s</strong> is narrated with <strong>%s and %s in the accusative</strong>, on '
      'the basis that the speech is <strong>a single sentence</strong>; and its meaning is: '
      '<strong>that at the first of His creating the Pen, He said to it: write.</strong></em>'
      % (ar('أَوَّلُ مَا خَلَقَ اللهُ القَلَمَ'), ar('أَوَّل'), ar('القَلَم'))) +
    p('<em>And it is narrated with <strong>%s and %s in the nominative</strong>, on the basis that '
      'the speech is <strong>two sentences</strong>: the first <strong>«the first thing Allah '
      'created was the Pen»</strong>, and <strong>«He said to it: write»</strong> a second '
      'sentence. So the meaning would be: <strong>that the first of the created things of this '
      'world is the Pen.</strong></em>' % (ar('أَوَّل'), ar('القَلَم'))) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>بِالنَّصْب</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">one sentence — '
    '<em>when He first created the Pen, He commanded it</em>. Says nothing about what was created '
    'before</td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>بِالرَّفْع</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">two sentences — '
    '<em>the Pen is the first created thing of this world</em>, and then the command</td></tr>'
    '</table></div>' +
    p('al-Fawzān reports both without choosing, and that is worth imitating: '
      '<strong>the level of the writing is established on either reading, and the question of '
      'what was created first is a separate matter the ḥadīth may or may not be settling.</strong>') +
    p('And a point of attribution the student should not miss: <em>and his saying '
      '<strong>%s</strong> is <strong>from the speech of ʿUbādah ibn al-Ṣāmit, the narrator of '
      'the ḥadīth</strong></em> — not from the Prophet &#65018;. '
      '<em>That is: <strong>whatever reaches a man of what benefits him or harms him is decreed '
      'for him; it must befall him, and its opposite will not befall him.</strong></em> '
      '<strong>The matn carries it, and the sharḥ tells you whose words they are.</strong>'
      % ar('فَمَا أَصَابَ الإِنْسَانَ لَمْ يَكُنْ لِيُخْطِئَهُ')) +
    p('<strong>%s</strong> — <em>is <strong>a figure for the priorness of the writing of the '
      'measures and the finishing of it</strong></em>; <em>and it is the meaning of what came in '
      'the ḥadīth of Ibn ʿAbbās: <strong>«the pens have been lifted and the pages have dried»</strong> '
      '— reported by <strong>al-Tirmidhī</strong>.</em>'
      % ar('جَفَّتِ الأَقْلَامُ وَطُوِيَتِ الصُّحُفُ')))
b += B.ayah(
    'أَلَمْ تَعْلَمْ أَنَّ اللَّهَ يَعْلَمُ مَا فِي السَّمَاءِ وَالْأَرْضِ إِنَّ ذَلِكَ فِي '
    'كِتَابٍ إِنَّ ذَلِكَ عَلَى اللَّهِ يَسِيرٌ',
    '"Do you not know that Allah knows what is in the heaven and the earth? Indeed that is in a '
    'Book. Indeed that is easy for Allah."',
    'Sūrat al-Ḥajj 22:70 · سُورَةُ الحَجّ')
b += B.sharh(
    p('<strong>%s</strong> — <em>the interrogative is <strong>%s — for affirmation</strong>; '
      'that is: <strong>you have come to know, O Muḥammad, and are certain.</strong></em>'
      % (ar('أَلَمْ تَعْلَمْ'), ar('لِلتَّقْرِير'))) +
    p('And now see how neatly the āyah contains both levels of the first degree: '
      '<em><strong>%s — in it is the encompassing of His knowledge of the upper world and the '
      'lower world, and this is the level of the KNOWLEDGE.</strong> '
      '<strong>%s — that is: written with Him in the Mother of the Book, and this is the level of '
      'the WRITING.</strong></em>'
      % (ar('أَنَّ اللَّهَ يَعْلَمُ مَا فِي السَّمَاءِ وَالْأَرْضِ'), ar('إِنَّ ذَلِكَ فِي كِتَابٍ'))) +
    p('<strong>%s</strong> — <em>that is: <strong>the encompassing of His knowledge of what is in '
      'the heaven and the earth, and His writing of it, is easy for Him.</strong></em> '
      '<strong>And that is the shāhid: it affirms Allah\'s knowledge of the things and His writing '
      'of them in al-Lawḥ al-Maḥfūẓ — which is exactly what the first degree '
      'comprises.</strong>' % ar('إِنَّ ذَلِكَ عَلَى اللَّهِ يَسِيرٌ')))
b += B.ayah(
    'مَا أَصَابَ مِنْ مُصِيبَةٍ فِي الْأَرْضِ وَلَا فِي أَنْفُسِكُمْ إِلَّا فِي كِتَابٍ '
    'مِنْ قَبْلِ أَنْ نَبْرَأَهَا إِنَّ ذَلِكَ عَلَى اللَّهِ يَسِيرٌ',
    '"No calamity befalls in the earth, nor in yourselves, but it is in a Book before We bring it '
    'into being. Indeed that is easy for Allah."',
    'Sūrat al-Ḥadīd 57:22 · سُورَةُ الحَدِيد')
b += B.sharh(
    p('al-Fawzān glosses the two kinds of calamity the āyah names, and the detail is worth having: '
      '<strong>%s</strong> — <em>of <strong>drought of rain, weakness of plants, and shortfall of '
      'fruits</strong></em>; <strong>%s</strong> — <em>of <strong>pains and sicknesses and '
      'straitness of living</strong></em>.'
      % (ar('مَا أَصَابَ مِنْ مُصِيبَةٍ فِي الْأَرْضِ'), ar('وَلَا فِي أَنْفُسِكُمْ'))) +
    p('<strong>%s</strong> — <em>that is: <strong>but that it is written in al-Lawḥ '
      'al-Maḥfūẓ</strong></em>; <strong>%s</strong> — <em>that is: '
      '<strong>before We create it and bring it into existence</strong></em>; '
      '<strong>%s</strong> — <em>that is: <strong>its recording in the Book, for all its '
      'multitude, is easy for Allah.</strong></em>'
      % (ar('إِلَّا فِي كِتَابٍ'), ar('مِنْ قَبْلِ أَنْ نَبْرَأَهَا'),
         ar('إِنَّ ذَلِكَ عَلَى اللَّهِ يَسِيرٌ'))) +
    p('<strong>And the shāhid: it is a proof for the writing of the events in al-Lawḥ al-Maḥfūẓ '
      '<em>before their occurrence</em>; and that comprises His knowledge of them before the '
      'writing — so it is a proof for the two levels of knowledge and writing together.</strong>'))

b += B.heading('التَّقْدِيرُ العَامُّ وَالخَاصّ', 'The General Decree and the Particular')
b += B.sharh(
    p('<em>Then after that the Shaykh رحمه الله pointed out that <strong>the decreeing is of two '
      'kinds</strong>:</em>') +
    p('<strong>%s</strong> — <em>comprehensive of every thing that comes to be; and it is the one '
      'whose discussion with its proofs has just come, and it is <strong>what is written in '
      'al-Lawḥ al-Maḥfūẓ.</strong></em>' % ar('تَقْدِيرٌ عَامٌّ')) +
    p('<strong>%s</strong> — <em>and it is <strong>a detailing of the general decree</strong>; '
      'and it is <strong>three kinds</strong>.</em> This is al-Fawzān\'s reading of the author\'s '
      'phrase <strong>%s</strong> — «in places, in summary and in detail».'
      % (ar('وَتَقْدِيرٌ خَاصّ'), ar('يَكُونُ فِي مَوَاضِعَ جُمْلَةً وَتَفْصِيلًا'))) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.89rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>١ عُمْرِيّ</strong><br>'
    '<span style="font-size:.8rem">lifetime</span></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">as in the '
    'ḥadīth of <strong>Ibn Masʿūd</strong> concerning what is written upon '
    'the foetus in its mother’s belly, of <strong>four words: his provision, his appointed '
    'term, his deed, and whether he is wretched or happy</strong></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>٢ حَوْلِيّ</strong><br>'
    '<span style="font-size:.8rem">yearly</span></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">what is decreed '
    '<strong>on Laylat al-Qadr of the events of the year</strong> — as in '
    '<span dir="rtl" lang="ar">فِيهَا يُفْرَقُ كُلُّ أَمْرٍ حَكِيمٍ</span> '
    '(al-Dukhān 44:4)</td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>٣ يَوْمِيّ</strong><br>'
    '<span style="font-size:.8rem">daily</span></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">what is decreed of '
    '<strong>the day’s events — of life and death, honour and humiliation</strong> and '
    'the like — as in <span dir="rtl" lang="ar">كُلَّ يَوْمٍ هُوَ فِي شَأْنٍ</span> '
    '(al-Raḥmān 55:29)</td></tr>'
    '</table></div>' +
    p('So the structure is one decree and three windows onto it. '
      '<strong>Nothing new is decided at any of the three</strong> — they are, in al-Fawzān\'s '
      'word, <em>a detailing</em> of what is already in the Preserved Tablet. '
      '<strong>Which is why Laylat al-Qadr is a night to be sought rather than a night on which '
      'the outcome is still open.</strong>'))
b += B.ayah(
    'فِيهَا يُفْرَقُ كُلُّ أَمْرٍ حَكِيمٍ',
    '"In it every decided affair is apportioned."',
    'Sūrat al-Dukhān 44:4 · سُورَةُ الدُّخَان')
b += B.ayah(
    'يَسْأَلُهُ مَنْ فِي السَّمَاوَاتِ وَالْأَرْضِ كُلَّ يَوْمٍ هُوَ فِي شَأْنٍ',
    '"All who are in the heavens and the earth ask of Him. Every day He is upon some affair."',
    'Sūrat al-Raḥmān 55:29 · سُورَةُ الرَّحْمَن')

b += B.heading('غُلَاةُ القَدَرِيَّة', 'The Extremists of the Qadariyyah')
b += B.sharh(
    p('<em>And his saying <strong>%s</strong> — that is, the one just set out in its two kinds, '
      'the general and the particular — <strong>%s</strong>, that is: '
      '<strong>those who went to excess in denying the decree</strong>.</em>'
      % (ar('فَهَذَا القَدَر'), ar('قَدْ كَانَ يُنْكِرُهُ غُلَاةُ القَدَرِيَّةِ'))) +
    p('<em>So <strong>they deny Allah\'s knowledge of things before their existence, and His '
      'writing of them in al-Lawḥ al-Maḥfūẓ and elsewhere</strong>; and they say: '
      '<strong>Allah commanded and forbade while not knowing who will obey Him and who will '
      'disobey Him</strong> — <strong>so the affair is %s</strong>, that is: '
      '<strong>newly begun, not having preceded in Allah\'s knowledge and His '
      'decree.</strong></em>' % ar('أُنُف')) +
    p('<strong>%s</strong> is the word they used, and it is worth knowing because it names the '
      'position exactly: <em>the affair is fresh</em> — made up as it goes, unknown in advance '
      'even to Allah. <strong>That is not a view about human freedom; it is a denial of an '
      'attribute.</strong>' % ar('أُنُف')) +
    p('<em>And <strong>these the imāms declared disbelievers</strong>; '
      '<strong>but they have died out</strong> — and this is why the Shaykh said '
      '<strong>%s</strong>.</em>' % ar('وَمُنْكِرُوهُ اليَوْمَ قَلِيل')) +
    p('And then al-Fawzān names who is left, which is the bridge to the next lesson: '
      '<em>and <strong>there has remained the sect which acknowledges the knowledge, but denies '
      'that the deeds of the servants enter into the decree</strong>, and claims '
      '<strong>that they are created by them independently — that Allah did not create them and '
      'did not will them</strong>, as its explanation is to come.</em>') +
    p('<strong>So the dispute has moved.</strong> The old Qadariyyah denied the first degree — the '
      'knowledge and the writing. The later ones concede it and deny the second — '
      '<em>the volition and the creating</em>. Which is exactly what Lesson 43 takes up.'))

b += B.vocab([
    ('القَدَر', 'al-qadar', 'the decree',
     'From قَدَرْتَ الشَّيْءَ, to encompass its measure'),
    ('أَزَلًا وَأَبَدًا', 'azalan wa-abadan', 'in eternity and perpetually',
     'Al-azal: pre-eternity with no beginning; al-abad: the future with no end'),
    ('اللَّوْحُ المَحْفُوظ', 'al-lawḥ al-maḥfūẓ',
     'the Preserved Tablet',
     'It is أُمُّ الكِتَاب — guarded from any addition or subtraction'),
    ('المَوْجُودَاتُ وَالمَعْدُومَات', 'al-mawjūdāt wa-l-maʿdūmāt',
     'the existent and the non-existent',
     'The reach of His knowledge — including what never happened'),
    ('أُمُّ الكِتَاب', 'umm al-kitāb', 'the Mother of the Book',
     'Another name for the Preserved Tablet'),
    ('تَقْدِيرٌ عُمْرِيّ', 'taqdīr ʿumrī', 'the lifetime decree',
     'The four words written upon the foetus'),
    ('تَقْدِيرٌ حَوْلِيّ', 'taqdīr ḥawlī', 'the yearly decree',
     'On Laylat al-Qadr — فِيهَا يُفْرَقُ كُلُّ أَمْرٍ حَكِيمٍ'),
    ('أُنُف', 'unuf', 'newly begun, fresh',
     'The ghulāt al-qadariyyah’s word — unknown in advance even to Allah'),
])
b += B.mcq('ws-l42', [
    ('What does the author’s wording imply about one who denies al-qadar?',
     ['That he is sinful but still of Ahl al-Sunnah',
      'That he is not of Ahl al-Sunnah wa-l-Jamāʿah — and per the ḥadīth of Jibrīl, which made '
      'it the sixth pillar, he is not a believer',
      'That his case is left to Allah',
      'That he must be taught before being judged'], 1),
    ('Why does the author treat the knowledge and the writing as one degree?',
     ['Because the texts always mention them together',
      'Because the first pair is about what Allah knew and recorded, and neither of them makes '
      'anything happen — the second pair is what He willed and brought about',
      'Because the writing is a kind of knowledge',
      'To make the count come to two'], 1),
    ('What does %s establish about the reach of His knowledge?'
     % ar('المَوْجُودَاتِ وَالمَعْدُومَاتِ'),
     ['That He knows only what will occur',
      'That it includes what never happened — so the knowledge is complete independently of '
      'whether events occur',
      'That He knows the present but not the future',
      'That His knowledge increases with events'], 1),
    ('What are the two readings of %s?' % ar('أَوَّلُ مَا خَلَقَ اللهُ القَلَمَ'),
     ['One is authentic and the other weak',
      'In the accusative it is one sentence — when He first created the Pen He commanded it; in '
      'the nominative it is two — the Pen is the first created thing of this world',
      'They differ over whether the Pen or the Throne was first',
      'They differ over who narrated it'], 1),
    ('Whose words are %s?' % ar('فَمَا أَصَابَ الإِنْسَانَ لَمْ يَكُنْ لِيُخْطِئَهُ'),
     ['The Prophet’s ﷺ, in the same ḥadīth',
      'ʿUbādah ibn al-Ṣāmit’s, the narrator of the ḥadīth',
      'Ibn ʿAbbās’s', 'Ibn Taymiyyah’s own'], 1),
    ('How does al-Ḥajj 22:70 contain both levels of the first degree?',
     ['By mentioning the Pen and the Tablet',
      '"Allah knows what is in the heaven and the earth" is the level of knowledge; "indeed that '
      'is in a Book" is the level of writing',
      'By mentioning the heaven and the earth',
      'By affirming that it is easy for Allah'], 1),
    ('What are the three kinds of particular decree?',
     ['Of the angels, of men and of the jinn',
      'ʿUmrī — the four words on the foetus; ḥawlī — on Laylat al-Qadr; and yawmī — the day’s '
      'events',
      'Of provision, of lifespan and of deeds',
      'Of the heavens, the earth and what is between'], 1),
    ('What did the ghulāt al-qadariyyah mean by saying the affair is %s?' % ar('أُنُف'),
     ['That it is decided by the servant alone',
      'That it is newly begun — not having preceded in Allah’s knowledge or decree, so He '
      'commanded without knowing who would obey',
      'That it changes each year on Laylat al-Qadr',
      'That it is written but may be altered'], 1),
])
b += B.tf('ws-l42-tf', [
    ('الإِيمَانُ بِالقَدَرِ سَادِسُ أَرْكَانِ الإِيمَانِ.',
     'Belief in al-qadar is the sixth pillar of faith.', True),
    ('اللَّوْحُ المَحْفُوظُ مَحْفُوظٌ مِنَ الزِّيَادَةِ وَالنُّقْصَانِ.',
     'The Preserved Tablet is guarded from addition and subtraction.', True),
    ('التَّقْدِيرُ الخَاصُّ يُنْشِئُ مَا لَيْسَ فِي اللَّوْحِ المَحْفُوظِ.',
     'The particular decree originates what is not in the Preserved Tablet.', False),
    ('غُلَاةُ القَدَرِيَّةِ كَفَّرَهُمُ الأَئِمَّةُ.',
     'The imāms declared the extremists of the Qadariyyah disbelievers.', True),
])
b += B.memorize(
    'اكْتُبْ مَقَادِيرَ كُلِّ شَيْءٍ حَتَّى تَقُومَ السَّاعَةُ',
    'The second level of the decree in one command. And keep ʿUbādah\'s own comment beside it, '
    'which the sharḥ is careful to attribute to him rather than to the Prophet ﷺ: what reaches a '
    'man was never going to miss him, and what missed him was never going to reach him.')
b += B.aiquiz('Belief in al-qadar in al-Aqidah al-Wasitiyyah: its definition and the four maratib '
              'grouped into two degrees, why the knowledge and the writing are one degree, the '
              'reach of His knowledge over the existent AND the non-existent, the two readings of '
              'awwalu ma khalaqa Llahu al-qalam, that fama asaba al-insan is Ubadahs own words, '
              'how al-Hajj 22:70 contains both levels, the general decree with its three '
              'particular windows umri hawli and yawmi, and the ghulat al-qadariyyah who said '
              'the affair is unuf')
b += B.further()
b += B.nav('was-l41-ikhraj-bi-la-shafaah.html', 'Release from the Fire with No Intercession',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l42')

io.open(os.path.join(B.AQ, 'was-l42-qadar-ilm-kitabah.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'الإِيمَانُ بِالقَدَرِ · العِلْمُ وَالكِتَابَة',
    'Belief in the Decree — the Knowledge and the Writing',
    'Lesson 42 of al-ʿAqīdah al-Wāsiṭiyyah, opening Part 5: the '
    'four levels of the decree and why the first two are counted as one; the ḥadīth of '
    'the Pen with both its readings; the general decree and its three particular windows; and the '
    'extremists who said the affair was “newly begun”.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الثَّانِي وَالأَرْبَعُون', '5',
           'الإِيمَانُ بِالقَدَرِ · العِلْمُ وَالكِتَابَة',
           'Belief in the Decree — the Knowledge and the Writing', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l42-qadar-ilm-kitabah.html')
