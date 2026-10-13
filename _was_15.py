# -*- coding: utf-8 -*-
"""Wasitiyyah L15 -- the completion of section 17: the four further ayat of
nafy al-sharik, the proof of al-tamanu', and the prohibition of striking
likenesses for Allah. Sharh pp.65-68."""
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
    'الحَافِظُ <strong>ابْنُ كَثِير</strong>, <em>تَفْسِيرُ القُرْآنِ العَظِيم</em> — quoted by '
    'al-Fawzān in this section on al-Furqān 25:2.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'State the four attributes al-Fawzān draws out of al-Furqān 25:2 and which party each answers.',
    'Lay out the proof of %s from al-Muʾminūn 23:91 in your own words.' % ar('التَّمَانُع'),
    'Explain what %s means and why the mushrikūn fell into it.' % ar('ضَرْبُ الأَمْثَالِ لِلَّهِ'),
    'Give the shāhid al-Fawzān states for this whole group of āyāt.',
])

b += B.heading('تَمَامُ القَوْلِ فِي نَفْيِ الشَّرِيك', 'Completing the Negation of a Partner')
b += B.prose(
    'Lesson 14 closed on al-Isrāʾ 17:111 — no son, no partner in dominion, no ally taken out of '
    'weakness. The author does not leave it at one āyah. He brings four more, and al-Fawzān '
    'treats them as one connected argument: first the <strong>declaration</strong> that creation '
    'itself declares Him free of a partner, then the <strong>attributes</strong> that rule a '
    'partner out, then a <strong>rational proof</strong> that two gods is incoherent, and finally '
    'the <strong>prohibition</strong> of the very move that produced the error.')

b += B.matn(
    'وَقَوْلُهُ: ﴿يُسَبِّحُ لِلَّهِ مَا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ﴾، وَقَوْلُهُ: '
    '﴿تَبَارَكَ الَّذِي نَزَّلَ الْفُرْقَانَ عَلَى عَبْدِهِ لِيَكُونَ لِلْعَالَمِينَ نَذِيرًا ۝ '
    'الَّذِي لَهُ مُلْكُ السَّمَاوَاتِ وَالْأَرْضِ وَلَمْ يَتَّخِذْ وَلَدًا وَلَمْ يَكُنْ لَهُ '
    'شَرِيكٌ فِي الْمُلْكِ﴾، وَقَوْلُهُ: ﴿مَا اتَّخَذَ اللَّهُ مِنْ وَلَدٍ وَمَا كَانَ مَعَهُ '
    'مِنْ إِلَهٍ﴾، وَقَوْلُهُ: ﴿فَلَا تَضْرِبُوا لِلَّهِ الْأَمْثَالَ﴾، وَقَوْلُهُ: ﴿قُلْ '
    'إِنَّمَا حَرَّمَ رَبِّيَ الْفَوَاحِشَ﴾ الآيَة.')

b += B.heading('١ · تَسْبِيحُ الخَلْقِ كُلِّه', 'First — All of Creation Declares Him Free')
b += B.ayah(
    'يُسَبِّحُ لِلَّهِ مَا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ '
    'وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ',
    '"Whatever is in the heavens and whatever is in the earth declares Allah free of all '
    'imperfection. His is the dominion and His is the praise, and He is Able over everything."',
    'Sūrat al-Taghābun 64:1 · سورة التغابن')
b += B.sharh(
    p('<strong>%s</strong> — al-Fawzān: <em>all of His creation, in His heavens and His earth, '
      'declares Him free of every defect and fault.</em> The <em>tasbīḥ</em> is not a human '
      'opinion about Allah that He then confirms; it is the standing testimony of everything He '
      'made.' % ar('يُسَبِّحُ لِلَّهِ مَا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ')) +
    p('<strong>%s</strong> — <em>the two are His exclusively; nothing of either belongs to anyone '
      'else.</em> And then the qualification that answers the obvious question — <em>but people '
      'own things</em>: <strong>whatever ownership His servants have, it is from His '
      'giving.</strong> A creature\'s dominion is loaned, not held.'
      % ar('لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ')) +
    p('<strong>%s</strong> — <em>nothing renders Him unable.</em>'
      % ar('وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ')))

b += B.heading('٢ · أَرْبَعُ صِفَاتٍ تَنْفِي الشَّرِيك', 'Second — Four Attributes That Rule a Partner Out')
b += B.ayah(
    'تَبَارَكَ الَّذِي نَزَّلَ الْفُرْقَانَ عَلَى عَبْدِهِ لِيَكُونَ لِلْعَالَمِينَ نَذِيرًا '
    'الَّذِي لَهُ مُلْكُ السَّمَاوَاتِ وَالْأَرْضِ وَلَمْ يَتَّخِذْ وَلَدًا وَلَمْ يَكُنْ لَهُ '
    'شَرِيكٌ فِي الْمُلْكِ وَخَلَقَ كُلَّ شَيْءٍ فَقَدَّرَهُ تَقْدِيرًا',
    '"Blessed is He who sent down the Criterion upon His servant, that he might be a warner to '
    'the worlds — He to whom belongs the dominion of the heavens and the earth, who has not taken '
    'a son, and who has no partner in dominion, and who created everything and measured it out '
    'with exact measure."',
    'Sūrat al-Furqān 25:1–2 · سورة الفرقان')
b += B.sharh(
    p('Before the four attributes, three notes on the opening. <strong>%s</strong> is a past-tense '
      'verb from <strong>%s</strong> — growth and increase, settled, firm, lasting; and '
      'al-Fawzān states two restrictions on it: <em>this word is not used of anyone but Allah, '
      'and it is not used except in the past-tense form.</em>'
      % (ar('تَبَارَكَ'), ar('البَرَكَة'))) +
    p('<strong>%s</strong> is the Qurʾān; it is called <em>the Criterion</em> because it '
      '<strong>separates truth from falsehood</strong>. And <strong>%s</strong> means Muḥammad '
      '&#65018; — <em>and this is a description of praise and commendation, because He ascribed '
      'him to Himself by an ascription of honour and ennobling</em>, in the very context of '
      'sending the Qurʾān down upon him. Being named <em>His servant</em> is the station, not a '
      'demotion from one.' % (ar('الفُرْقَان'), ar('عَلَى عَبْدِهِ'))) +
    p('<strong>%s</strong> — a warner to mankind and the jinn, <em>and this is from his '
      'particular distinctions</em> &#65018;: the general messengership. %s is from %s, which is '
      '<em>informing of the causes of fear</em>.'
      % (ar('لِيَكُونَ لِلْعَالَمِينَ نَذِيرًا'), ar('نَذِيرًا'), ar('الإِنْذَار'))))
b += B.sharh(
    p('Now the four attributes al-Fawzān numbers in the second āyah:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.88rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.5rem .7rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>الأُولَى</strong></td>'
    '<td style="padding:.5rem .7rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar">لَهُ مُلْكُ السَّمَاوَاتِ وَالْأَرْضِ</td>'
    '<td style="padding:.5rem .7rem;border:1px solid var(--line)">His, and no one else’s — '
    'so <strong>He alone disposes of them</strong></td></tr>'
    '<tr><td style="padding:.5rem .7rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>الثَّانِيَة</strong></td>'
    '<td style="padding:.5rem .7rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar">وَلَمْ يَتَّخِذْ وَلَدًا</td>'
    '<td style="padding:.5rem .7rem;border:1px solid var(--line)">against what the Christians and '
    'Jews allege — <strong>because of the perfection of His freedom from need, and every '
    'creature’s need of Him</strong></td></tr>'
    '<tr><td style="padding:.5rem .7rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>الثَّالِثَة</strong></td>'
    '<td style="padding:.5rem .7rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar">وَلَمْ يَكُنْ لَهُ شَرِيكٌ فِي الْمُلْكِ</td>'
    '<td style="padding:.5rem .7rem;border:1px solid var(--line)">a refutation of the parties of '
    'the mushrikūn — <strong>the idolaters, the dualists and others</strong></td></tr>'
    '<tr><td style="padding:.5rem .7rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>الرَّابِعَة</strong></td>'
    '<td style="padding:.5rem .7rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar">وَخَلَقَ كُلَّ شَيْءٍ</td>'
    '<td style="padding:.5rem .7rem;border:1px solid var(--line)">of the created things — '
    '<strong>and the deeds of the servants enter into this</strong>: they are Allah’s '
    'creating and the servant’s doing</td></tr>'
    '</table></div>' +
    p('That last line is small and load-bearing: it is the Sunnī position on the servant\'s acts, '
      'dropped in here in passing and taken up in full in the section on <em>al-qadar</em>. The '
      'act is <strong>created by Allah</strong> and <strong>done by the servant</strong> — not '
      'one to the exclusion of the other.') +
    p('<strong>%s</strong> — <em>He measured out everything He created: the appointed terms, the '
      'provisions, the happiness and the wretchedness; and He prepared each thing for what it is '
      'suited to.</em>' % ar('فَقَدَّرَهُ تَقْدِيرًا')))
b += B.prose(
    'al-Fawzān closes the āyah with Ibn Kathīr: <em>He declared Himself free of a son and of a '
    'partner; then He informed that He created everything and measured it out with exact measure '
    '— that is, everything besides Him is created and governed, and He is the Creator of '
    'everything, its Lord, its Owner and its God; and everything is beneath His overpowering, His '
    'governing, His subjecting and His measuring.</em>')

b += B.heading('٣ · بُرْهَانُ التَّمَانُع', 'Third — The Proof of Mutual Obstruction')
b += B.ayah(
    'مَا اتَّخَذَ اللَّهُ مِنْ وَلَدٍ وَمَا كَانَ مَعَهُ مِنْ إِلَهٍ إِذًا لَذَهَبَ كُلُّ '
    'إِلَهٍ بِمَا خَلَقَ وَلَعَلَا بَعْضُهُمْ عَلَى بَعْضٍ سُبْحَانَ اللَّهِ عَمَّا يَصِفُونَ',
    '"Allah has not taken any son, nor was there ever any god alongside Him. Had there been, each '
    'god would have gone off with what he created, and some of them would have risen over others. '
    'Glory be to Allah above what they describe."',
    'Sūrat al-Muʾminūn 23:91 · سورة المؤمنون')
b += B.sharh(
    p('al-Fawzān first notes the grammar: <strong>%s in both places is to emphasise the '
      'negation</strong> — not merely "He has no son," but the negation driven home. Then he '
      'identifies what the rest of the āyah is doing: <strong>%s is an evidentiary argument '
      '<em>for</em> what preceded it</strong> at the start of the āyah — the denial of a son and '
      'a partner in divinity. The Qurʾān states the claim, then reasons for it.'
      % (ar('مِنْ'), ar('إِذًا لَذَهَبَ كُلُّ إِلَهٍ بِمَا خَلَقَ'))) +
    p('The argument runs in two steps, and it is worth following exactly:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.93rem">'
    '<p style="margin:0 0 .6rem"><strong>1 · الانْقِسَام.</strong> Were a plurality of gods '
    'supposed, <em>each one of them would go off separately from the other with what he '
    'created</em> — and at that point <strong>the universe would not hold together</strong>, '
    'because of the existence of division. <em>And the observed reality is that the universe is '
    'ordered with the most complete order; no plurality and no division has occurred in it.</em></p>'
    '<p style="margin:0"><strong>2 · المُغَالَبَة.</strong> And were there another god with '
    'Him, <em>each of them would seek to overpower the other and to oppose him, so some of them '
    'would rise over others — as is the state of the kings of this world</em>. And then '
    '<strong>that defeated weak one does not deserve to be a god at all.</strong></p></div>' +
    p('Note what the second step does. It does not merely say a second god is unlikely; it says '
      'the <em>concept</em> collapses. Two gods must contend; contention produces a winner and a '
      'loser; and a loser is not a god. <strong>So the supposition destroys itself.</strong>') +
    p('And therefore: <em>when the invalidity of a co-sharer is established, it is necessarily '
      'the case that the God is one — He is Allah alone.</em> Which is why the āyah ends %s — free '
      'of the partner and the son.' % ar('سُبْحَانَ اللَّهِ عَمَّا يَصِفُونَ')))

b += B.heading('٤ · النَّهْيُ عَنْ ضَرْبِ الأَمْثَالِ لِلَّه', 'Fourth — The Prohibition of Striking Likenesses')
b += B.ayah(
    'فَلَا تَضْرِبُوا لِلَّهِ الْأَمْثَالَ إِنَّ اللَّهَ يَعْلَمُ وَأَنْتُمْ لَا تَعْلَمُونَ',
    '"So do not strike likenesses for Allah. Indeed Allah knows, and you do not know."',
    'Sūrat al-Naḥl 16:74 · سورة النحل')
b += B.sharh(
    p('<strong>%s is comparing one state to another state</strong> — and here al-Fawzān explains '
      'precisely how the mushrikūn reasoned themselves into their shirk, which is the most '
      'useful paragraph in the section:' % ar('ضَرْبُ المَثَلِ')) +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.93rem">The mushrikūn used to say: <em>Allah is too '
    'exalted for one of us to worship Him directly, so there must be the taking of an '
    'intermediary between us and Him.</em> So they would seek nearness to Him through the idols '
    'and other things — <strong>likening Him to the kings of this world</strong>. And Allah '
    'forbade that, because He has no like, so He is not likened to His creation nor compared with '
    'them.</p></div>' +
    p('That is the whole mechanism: a <em>courtly analogy</em>. You cannot approach a king without '
      'a chamberlain, so — they reasoned — you cannot approach the King of kings without one '
      'either. The reasoning is not stupid; it is simply an analogy applied where no likeness '
      'exists. Hence: <strong>%s</strong> — He informs that He has no like. And '
      '<strong>%s</strong>: <em>this act of yours issued from a corrupt supposition and a false '
      'notion; and you also do not know what evil outcome lies in the worship of the idols.</em>'
      % (ar('إِنَّ اللَّهَ يَعْلَمُ'), ar('وَأَنْتُمْ لَا تَعْلَمُونَ'))) +
    p('This is the same disease met in <em>al-Qawāʿid al-Arbaʿ</em> and in Lesson 4 of this track, '
      'now traced to its root. <strong>Shirk is built on ignorance and imagination</strong> — not '
      'on a proof that came out wrong, but on no proof at all.'))

b += B.ayah(
    'قُلْ إِنَّمَا حَرَّمَ رَبِّيَ الْفَوَاحِشَ مَا ظَهَرَ مِنْهَا وَمَا بَطَنَ وَالْإِثْمَ '
    'وَالْبَغْيَ بِغَيْرِ الْحَقِّ وَأَنْ تُشْرِكُوا بِاللَّهِ مَا لَمْ يُنَزِّلْ بِهِ '
    'سُلْطَانًا وَأَنْ تَقُولُوا عَلَى اللَّهِ مَا لَا تَعْلَمُونَ',
    '"Say: my Lord has only forbidden the gross indecencies — what is open of them and what is '
    'hidden — and sin, and aggression without right, and that you associate with Allah that for '
    'which He has sent down no authority, and that you say about Allah what you do not know."',
    'Sūrat al-Aʿrāf 7:33 · سورة الأعراف')
b += B.sharh(
    p('<strong>%s</strong> — the address is to the Prophet &#65018;, <em>and in that is a proof '
      'that the Qurʾān is the speech of Allah, and that the Prophet &#65018; is a conveyer from '
      'Allah.</em> A single imperative carries both: the words are not his, and his office is to '
      'deliver them.' % ar('قُلْ')) +
    p('<strong>%s is a particle of restriction</strong> — <em>only</em> these. %s is the plural of '
      '%s: <em>whatever has reached the furthest point of ugliness among the acts of '
      'disobedience</em>; %s — what is made public of them and what is kept secret. %s is '
      '<em>every act of disobedience that occasions sin</em>, and it has been said it is wine '
      'specifically. %s is <em>wrongdoing that crosses the limit, and transgression against '
      'people</em>.' % (ar('مَا'), ar('الفَوَاحِش'), ar('فَاحِشَة'),
                        ar('مَا ظَهَرَ مِنْهَا وَمَا بَطَنَ'), ar('الإِثْم'),
                        ar('البَغْيُ بِغَيْرِ الحَقِّ'))) +
    p('And then <strong>%s</strong> — <em>that you make for Him a partner in worship</em> — '
      '<strong>and this is the place of the shāhid from the āyah</strong>. %s: a proof and an '
      'evidence. Shirk is forbidden <em>and</em> unsupported: no authority was ever sent down for '
      'it.' % (ar('وَأَنْ تُشْرِكُوا بِاللَّهِ'), ar('سُلْطَانًا'))) +
    p('The last clause, <strong>%s</strong>, covers <em>the fabricating and lying involved in '
      'claiming that He has a son, and the like of that of which you have no knowledge; and such '
      'as what they used to attribute to Him of permissions and prohibitions which He never '
      'authorised.</em> Speaking about Allah without knowledge is listed <strong>alongside</strong> '
      'the gross sins, not beneath them.' % ar('وَأَنْ تَقُولُوا عَلَى اللَّهِ مَا لَا تَعْلَمُونَ')))

b += B.heading('الشَّاهِدُ مِنْ هَذِهِ الآيَات', 'The Point of Evidence in These Āyāt')
b += B.sharh(
    p('al-Fawzān gathers the whole group into one statement, and it is the summary to memorise:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.93rem">In them is <strong>the negation of a partner to Allah</strong>, '
    'and <strong>the affirming of His being alone in perfection</strong>; and the negation of a son '
    'and of a like from Him; and that <strong>all His creation declares Him free and holy</strong> '
    'of that. As there is in them also <strong>the establishing of the proof for the invalidity of '
    'shirk</strong>, and that it is built on <em>ignorance and imagination</em>, and that He has no '
    'like and no resemblance. وَاللهُ أَعْلَم.</p></div>' +
    p('Four moves, in order: creation testifies · the attributes exclude a partner · reason shows '
      'two gods is incoherent · and the analogy that produced the error is forbidden by name. '
      '<strong>The negation is never left as a bare denial</strong> — each time it is attached to '
      'a perfection that makes the denial necessary.'))

b += B.vocab([
    ('التَّسْبِيح', 'al-tasbīḥ', 'declaring free of defect',
     'All His creation does it — of every defect and fault'),
    ('الفُرْقَان', 'al-furqān', 'the Criterion',
     'Named so because it separates truth from falsehood'),
    ('التَّمَانُع', 'al-tamānuʿ', 'mutual obstruction',
     'Two gods must contend; the loser is no god — so the supposition collapses'),
    ('الانْقِسَام', 'al-inqisām', 'division',
     'Each god would go off with what he created, and the universe would not hold'),
    ('ضَرْبُ المَثَل', 'ḍarb al-mathal', 'striking a likeness',
     'Comparing one state to another — forbidden with regard to Allah'),
    ('الفَوَاحِش', 'al-fawāḥish', 'gross indecencies',
     'What has reached the furthest point of ugliness among the sins'),
    ('سُلْطَان', 'sulṭān', 'authority, warrant',
     'A proof and an evidence — and none was ever sent down for shirk'),
])
b += B.mcq('ws-l15', [
    ('al-Fawzān says all of creation declares Allah free of what?',
     ['Of having created evil', 'Of every defect and fault',
      'Of speaking to His creation', 'Of being known by the intellect'], 1),
    ('How does al-Fawzān reconcile %s with the fact that people own things?'
     % ar('لَهُ الْمُلْكُ'),
     ['People own nothing in reality',
      'Whatever ownership His servants have is from His giving',
      'Ownership is only metaphorical in Arabic',
      'The āyah concerns the Hereafter only'], 1),
    ('Which party does the third attribute of al-Furqān 25:2 (%s) answer?'
     % ar('وَلَمْ يَكُنْ لَهُ شَرِيكٌ فِي الْمُلْكِ'),
     ['The Jews and Christians', 'The idolaters, the dualists and their like',
      'The Jahmiyyah', 'The philosophers'], 1),
    ('What does al-Fawzān say about the servants’ deeds under %s?'
     % ar('وَخَلَقَ كُلَّ شَيْءٍ'),
     ['They are outside the āyah, being the servant’s alone',
      'They enter into it: they are Allah’s creating and the servant’s doing',
      'They are created and not done',
      'The āyah concerns only bodies, not acts'], 1),
    ('What is the second step of the proof in al-Muʾminūn 23:91?',
     ['That the gods would agree and so be one',
      'That each would seek to overpower the other, some rising over others — and the defeated '
      'weak one does not deserve to be a god',
      'That creation would cease to exist',
      'That the messengers would contradict one another'], 1),
    ('By what reasoning did the mushrikūn arrive at taking intermediaries?',
     ['From a verse they misread',
      'By likening Allah to the kings of this world, who cannot be approached without an '
      'intermediary',
      'From the practice of earlier prophets',
      'From a disputed hadith'], 1),
    ('Where is the shāhid in al-Aʿrāf 7:33?',
     ['In the mention of the gross indecencies',
      'In %s — that you associate with Allah that for which no authority was sent down'
      % ar('وَأَنْ تُشْرِكُوا بِاللَّهِ'),
      'In the mention of aggression', 'In the address to the Prophet ﷺ'], 1),
])
b += B.tf('ws-l15-tf', [
    ('لَفْظُ «تَبَارَكَ» لَا يُسْتَعْمَلُ إِلَّا بِلَفْظِ المَاضِي.',
     'The word tabāraka is not used except in the past-tense form.', True),
    ('سُمِّيَ القُرْآنُ فُرْقَانًا لِأَنَّهُ يَفْرِقُ بَيْنَ الحَقِّ وَالبَاطِلِ.',
     'The Qurʾān is called al-Furqān because it separates truth from falsehood.', True),
    ('وَصْفُ النَّبِيِّ ﷺ بِأَنَّهُ «عَبْدُهُ» وَصْفُ نَقْصٍ.',
     'Describing the Prophet ﷺ as "His servant" is a description of deficiency.', False),
    ('الشِّرْكُ مَبْنِيٌّ عَلَى جَهْلٍ وَخَيَالٍ.',
     'Shirk is built on ignorance and imagination.', True),
])
b += B.memorize(
    'إِذًا لَذَهَبَ كُلُّ إِلَهٍ بِمَا خَلَقَ وَلَعَلَا بَعْضُهُمْ عَلَى بَعْضٍ',
    'The whole proof of al-tamānuʿ is in one line. Two gods means division, and division means '
    'contention, and contention means a loser — and a loser is not a god. Look at the order of '
    'the universe and ask whether it looks like the work of rivals.')
b += B.aiquiz('The completion of nafy al-sharik in al-Aqidah al-Wasitiyyah: the tasbih of all '
              'creation, the four attributes of al-Furqan 25:2 and the party each answers, the '
              'proof of al-tamanu from al-Muminun 23:91 in its two steps, and the prohibition of '
              'striking likenesses for Allah with the courtly analogy that produced the shirk of '
              'the mushrikun')
b += B.further()
b += B.nav('was-l14-makr-izzah-nafy.html', 'Stratagem, Might, and the Negations',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l15')

io.open(os.path.join(B.AQ, 'was-l15-nafy-sharik-tamanu.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'تَمَامُ نَفْيِ الشَّرِيكِ وَبُرْهَانُ التَّمَانُع',
    'Completing the Negation of a Partner, and the Proof of al-Tamānuʿ',
    'Lesson 15 of al-ʿAqīdah al-Wāsiṭiyyah: the tasbīḥ of all '
    'creation, the four attributes of al-Furqān 25:2 and the party each one answers, the '
    'two-step proof that a plurality of gods is incoherent, and the courtly analogy the '
    'Qurʾān forbids by name.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الخَامِسَ عَشَر', '3',
           'تَمَامُ نَفْيِ الشَّرِيكِ وَبُرْهَانُ التَّمَانُع',
           'Completing the Negation of a Partner, and the Proof of al-Tamānuʿ', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l15-nafy-sharik-tamanu.html')
