# -*- coding: utf-8 -*-
"""Wasitiyyah L44 -- Part 5 closes: no contradiction between the decree and
ascribing the servants' acts to them in reality. The Jabriyyah and the
Qadariyyah nufah, each refuted by one of two consecutive ayat -- and al-Fawzan's
correction of the matn on "the Magians of this Ummah". Sharh pp.157-159."""
import io, os, importlib.util

spec = importlib.util.spec_from_file_location('qb', os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '_mutunbuild.py'))
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
B.set_source(os.path.join(B.AQ, 'was-l01-basmalah.html'))
B.FOOT = ('al-ʿAqīdah al-Wāsiṭiyyah of Shaykh al-Islām Ibn Taymiyyah '
          '· sharḥ of Shaykh Ṣāliḥ al-Fawzān · in our own words')
B.READING = [
    'Shaykh <strong>صَالِحٌ الفَوْزَان</strong>, <em>شَرْحُ العَقِيدَةِ الوَاسِطِيَّة</em> '
    '(Riyadh, Presidency of Scholarly Research &amp; Iftāʾ) — the sharḥ this track follows, '
    'including its correction of the matn noted on this page.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Name the two parties and say which way each one went to excess.',
    'Give the argument from the servant being <em>described</em> as a believer or a prayer-keeper.',
    'Say which of al-Takwīr 81:28–29 refutes which party, and why.',
    'State al-Fawzān’s correction of the matn regarding %s.' % ar('مَجُوسُ هَذِهِ الأُمَّة'),
])

b += B.heading('لَا تَنَافِي بَيْنَ القَدَرِ وَإِسْنَادِ أَفْعَالِ العِبَادِ إِلَيْهِمْ حَقِيقَة',
               'No Contradiction between the Decree and Ascribing the Servants’ Acts to Them in '
               'Reality')
b += B.matn(
    'وَالعِبَادُ فَاعِلُونَ حَقِيقَةً، وَاللهُ خَالِقُ أَفْعَالِهِمْ. وَالعَبْدُ هُوَ '
    'المُؤْمِنُ وَالكَافِرُ وَالبَرُّ وَالفَاجِرُ وَالمُصَلِّي وَالصَّائِمُ. '
    'وَلِلْعِبَادِ قُدْرَةٌ عَلَى أَعْمَالِهِمْ، وَلَهُمْ إِرَادَةٌ، وَاللهُ '
    'خَالِقُهُمْ وَخَالِقُ قُدْرَتِهِمْ وَإِرَادَتِهِمْ، كَمَا قَالَ تَعَالَى: '
    '﴿لِمَنْ شَاءَ مِنْكُمْ أَنْ يَسْتَقِيمَ ۝ وَمَا تَشَاءُونَ إِلَّا أَنْ يَشَاءَ '
    'اللَّهُ رَبُّ الْعَالَمِينَ﴾. وَهَذِهِ الدَّرَجَةُ مِنَ القَدَرِ يُكَذِّبُ بِهَا '
    'عَامَّةُ القَدَرِيَّةِ، الَّذِينَ سَمَّاهُمُ النَّبِيُّ ﷺ مَجُوسَ هَذِهِ '
    'الأُمَّةِ. وَيَغْلُو فِيهَا قَوْمٌ مِنْ أَهْلِ الإِثْبَاتِ حَتَّى سَلَبُوا '
    'العَبْدَ قُدْرَتَهُ وَاخْتِيَارَهُ، وَيُخْرِجُونَ عَنْ أَفْعَالِ اللهِ '
    'وَأَحْكَامِهِ حِكَمَهَا وَمَصَالِحَهَا.')
b += B.sharh(
    p('al-Fawzān states the author\'s purpose: <em>his intent by this is '
      '<strong>the refutation of whoever claimed that affirming that</strong> — the decree with '
      'its levels, together with the servants acting by their own choice — '
      '<strong>entails a contradiction.</strong></em>') +
    p('<em>And from there <strong>one party went to excess in affirming the decree, until they '
      'stripped the servant of his power and his choice</strong>; and <strong>the second party '
      'went to excess in affirming the actions of the servants and their choice, until they made '
      'them the creators of them</strong> — <strong>having no connection to Allah\'s volition and '
      'not falling under His power.</strong></em>') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>الجَبْرِيَّة</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<em>because they say <strong>the servant is compelled</strong> in what issues from him, '
    '<strong>having no choice in it</strong></em></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>القَدَرِيَّةُ النُّفَاة</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<em><strong>because they negate the decree</strong></em></td></tr>'
    '</table></div>' +
    p('And then al-Fawzān does something worth watching: '
      '<strong>he takes the matn clause by clause and assigns each clause to the party it '
      'answers.</strong> The author did not write a paragraph against one error and a paragraph '
      'against the other; <strong>he wrote sentences that alternate.</strong>'))
b += B.sharh(
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.89rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);vertical-align:top"'
    ' dir="rtl" lang="ar"><strong>وَالعِبَادُ فَاعِلُونَ حَقِيقَةً</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '→ <strong>against the Jabriyyah</strong>, <em>because they say the servants are not '
    'doers in reality, and <strong>ascribing the actions to them is of the category of the '
    'figurative</strong></em></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);vertical-align:top"'
    ' dir="rtl" lang="ar"><strong>وَاللهُ خَالِقُ أَفْعَالِهِمْ</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '→ <strong>against the Qadariyyah nufāh</strong>, <em>because they say Allah did '
    'not create the actions of the servants, but <strong>they created them independently, without '
    'Allah’s volition and His decreeing of them</strong></em></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);vertical-align:top"'
    ' dir="rtl" lang="ar"><strong>وَالعَبْدُ هُوَ المُؤْمِنُ وَالكَافِرُ… '
    'وَلِلْعِبَادِ قُدْرَةٌ… وَلَهُمْ إِرَادَةٌ</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '→ <strong>against the Jabriyyah</strong> again</td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);vertical-align:top"'
    ' dir="rtl" lang="ar"><strong>وَاللهُ خَالِقُهُمْ وَخَالِقُ قُدْرَتِهِمْ</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '→ <strong>against the Qadariyyah nufāh</strong> again</td></tr>'
    '</table></div>' +
    p('And the argument behind the third row is the best thing in the lesson, because it needs no '
      'theology at all — only attention to how we speak. '
      '<em>That is: <strong>the servants are not compelled in those deeds; because had it been '
      'so, it would not be valid to describe them with them</strong> — '
      '<strong>for the act of one compelled is not ascribed to him, and he is not described by '
      'it, and he does not deserve reward or punishment for it.</strong></em>') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.94rem">Look at the author’s list: '
    '<strong>the believer · the disbeliever · the righteous · the corrupt · '
    'the one who prays · the one who fasts.</strong> Every one of those is a '
    '<em>description of a person</em> taken from <em>what he does</em>. '
    '<strong>And nobody is called a thief for being pushed into a shop.</strong> So if the '
    'Jabriyyah were right, the Qurʾān’s whole vocabulary for people would be a '
    'mistake.</p></div>' +
    p('Note also what else that argument reaches: <strong>and he does not deserve reward or '
      'punishment for it.</strong> Lesson 37 established the recompense by reason — that it does '
      'not befit His wisdom to make the good-doer like the evil-doer. '
      '<strong>The Jabriyyah position makes the recompense itself unjust</strong>, which is the '
      'charge al-Fawzān closes the lesson with.'))

b += B.heading('آيَتَانِ مُتَتَابِعَتَانِ · لِكُلِّ طَائِفَةٍ وَاحِدَة',
               'Two Consecutive Āyāt — One for Each Party')
b += B.ayah(
    'لِمَنْ شَاءَ مِنْكُمْ أَنْ يَسْتَقِيمَ وَمَا تَشَاءُونَ إِلَّا أَنْ يَشَاءَ اللَّهُ '
    'رَبُّ الْعَالَمِينَ',
    '"For whoever among you wills to go straight. And you do not will, except that Allah — Lord '
    'of the worlds — wills."',
    'Sūrat al-Takwīr 81:28–29 · سُورَةُ التَّكْوِير')
b += B.sharh(
    p('<em>Then the Shaykh adduced, in refutation of the two parties, His saying تعالى…</em> — and '
      'al-Fawzān divides the two āyāt between them:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);vertical-align:top"'
    ' dir="rtl" lang="ar"><strong>لِمَنْ شَاءَ مِنْكُمْ أَنْ يَسْتَقِيمَ</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '→ <em>in it is <strong>the refutation of the Jabriyyah</strong>, '
    '<strong>because He affirmed a volition FOR THE SERVANTS — and they say they have no '
    'volition.</strong></em></td></tr>'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);vertical-align:top"'
    ' dir="rtl" lang="ar"><strong>وَمَا تَشَاءُونَ إِلَّا أَنْ يَشَاءَ اللَّهُ</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '→ <em>in it is <strong>the refutation of the Qadariyyah</strong>, who hold that '
    '<strong>the servant’s volition is independent in bringing the act into being, without '
    'depending on Allah’s volition.</strong> <strong>And this is false, because Allah '
    'attached the volition of the servants to His own volition, and tied it to '
    'it.</strong></em></td></tr>'
    '</table></div>' +
    p('<strong>Two āyāt, side by side, each one dismantling one of the two errors.</strong> And '
      'the order is not incidental: the first grants the servant a real will, '
      'and the second — <em>immediately</em>, in the next breath — makes it dependent. '
      '<strong>Anyone who stops at either āyah has one of the two heresies.</strong>') +
    p('This is the same passage the student met in Lesson 30, where it established that the '
      'servant\'s will is <em>real, and downstream</em>. '
      '<strong>Here it is doing the work twice over</strong> — and it is worth noticing that the '
      'author needed no third text to balance the two: '
      '<em>one āyah and its neighbour were enough.</em>'))

b += B.heading('«مَجُوسُ هَذِهِ الأُمَّة» · تَصْحِيحٌ مِنَ الشَّارِح',
               '"The Magians of This Ummah" — a Correction by the Commentator')
b += B.sharh(
    p('The author writes that the Qadariyyah are <strong>%s</strong> — '
      '<em>those whom the Prophet &#65018; named the Magians of this Ummah</em>. al-Fawzān first '
      'explains the comparison, and then corrects the attribution.'
      % ar('الَّذِينَ سَمَّاهُمُ النَّبِيُّ ﷺ مَجُوسَ هَذِهِ الأُمَّةِ')) +
    p('<em>The likeness is <strong>for their resembling the Magians, who affirm two creators: '
      'the light and the darkness</strong> — <strong>so they say the good is from the act of the '
      'light and the evil from the act of the darkness, and so they became dualists.</strong> '
      '<strong>And likewise these Qadariyyah made a creator alongside Allah</strong>, in that '
      'they claimed <strong>the servants create their actions without Allah\'s will and volition; '
      'rather they are independent in creating them.</strong></em>') +
    p('<strong>That is the point of the name</strong>, and it is exact: the charge is not merely '
      'error but <em>a second creator</em>. The Magian put the evil down to a rival principle; '
      '<strong>the Qadarī puts it down to man — and in both cases something besides Allah '
      'creates.</strong>') +
    '<div style="background:#fff8e6;border-right:4px solid #d4a017;'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .9rem">'
    '<p style="margin:0 0 .6rem;font-size:.9rem"><strong dir="rtl" lang="ar">تَنْبِيهٌ</strong> '
    '— and then al-Fawzān corrects the matn itself, in his own words:</p>'
    '<p style="margin:0;font-size:.95rem" dir="rtl" lang="ar"><strong>وَلَمْ يَثْبُتْ أَنَّ '
    'النَّبِيَّ ﷺ سَمَّاهُمْ مَجُوسَ هَذِهِ الأُمَّةِ، لِتَأَخُّرِ ظُهُورِهِمْ عَنْ '
    'وَقْتِ النَّبِيِّ ﷺ؛ فَأَكْثَرُ مَا يَجِيءُ مِنْ ذَمِّهِمْ إِنَّمَا هُوَ '
    'مَوْقُوفٌ عَلَى الصَّحَابَةِ.</strong></p>'
    '<p style="margin:.55rem 0 0;font-size:.9rem">— <em><strong>it is not established that '
    'the Prophet &#65018; named them the Magians of this Ummah</strong>, '
    '<strong>because of the lateness of their appearance after the Prophet’s '
    '&#65018; time</strong>; <strong>so most of what comes censuring them is only '
    '<span dir="rtl" lang="ar">مَوْقُوفٌ</span> upon the Ṣaḥābah.</strong></em></p></div>' +
    p('This is worth stopping on, because it is the standard of this whole subject applied to the '
      'author himself. <strong>al-Fawzān does not pass over a phrase in the matn he is '
      'commenting on.</strong> He explains what it means, and then says plainly that '
      '<em>the attribution to the Prophet &#65018; is not established</em> — and gives the '
      'reason, which is a reason of history rather than of chains: '
      '<strong>the sect arose after his lifetime.</strong>') +
    p('And he does not leave the censure unsupported either. The word <strong>%s</strong> is the '
      'muṣṭalaḥ term from the Hadeeth track: <em>a report that stops at a Companion</em> rather '
      'than reaching the Prophet &#65018;. <strong>So the censure of the Qadariyyah stands as the '
      'words of the Companions, and is reported as theirs.</strong>' % ar('مَوْقُوف')) +
    p('<strong>That is the discipline this track works to, demonstrated by the scholar we are '
      'following.</strong> A matn is not scripture; a named grading belongs to every report; and '
      'where the grading will not support the attribution, the honest course is to say so and keep '
      'the content at the level the evidence carries it.'))

b += B.heading('غُلُوُّ الجَبْرِيَّةِ وَمَا يَلْزَمُ مِنْه',
               'The Excess of the Jabriyyah, and What Follows from It')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is, in this degree of the decree; and %s is '
      '<strong>exceeding the required limit in a thing</strong></em>. '
      '<strong>%s</strong> — <em>and what is meant by them is '
      '<strong>the Jabriyyah, who said the servant is compelled in his act</strong></em> — '
      '<strong>%s</strong>.'
      % (ar('وَيَغْلُو فِيهَا'), ar('الغُلُوّ'), ar('قَوْمٌ مِنْ أَهْلِ الإِثْبَاتِ'),
         ar('حَتَّى سَلَبُوا العَبْدَ قُدْرَتَهُ وَاخْتِيَارَهُ'))) +
    p('And al-Fawzān sets the two excesses opposite each other in one sentence, which is the '
      'cleanest statement of the whole part: <em><strong>so the former went to excess in '
      'affirming the actions of the servants until they took them outside Allah\'s volition; and '
      'these went to excess in negating the actions of the servants until they stripped them of '
      'power and choice.</strong></em>') +
    p('<strong>%s</strong> — <em>the plurals of %s and %s; that is: '
      '<strong>that the Jabriyyah, in this madhhab of theirs, when they negated the actions of the '
      'servants and stripped them of power and choice, negated Allah\'s wisdom in His command and '
      'His prohibition and His reward and His punishment.</strong></em>'
      % (ar('وَيُخْرِجُونَ عَنْ أَفْعَالِ اللهِ وَأَحْكَامِهِ حِكَمَهَا وَمَصَالِحَهَا'),
         ar('حِكْمَة'), ar('مَصْلَحَة'))) +
    p('And then the consequence, which al-Fawzān states without softening: '
      '<em><strong>so they said: that He rewards or punishes the servants for what is not of their '
      'own doing, and commands them with what they are not able to do</strong> — '
      '<strong>so they accused Allah of injustice and of purposelessness</strong>; '
      'تَعَالَى اللهُ عَمَّا يَقُولُونَ عُلُوًّا كَبِيرًا.</em>') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.94rem">Which is where Part 5 ends, and it ends on an irony '
    'worth keeping. <strong>The Jabriyyah went to excess in affirming the decree in order to '
    'magnify Allah’s power</strong> — and arrived at a God who commands the incapable '
    'and punishes the innocent. <strong>So the party that tried hardest to protect His power '
    'ended by impugning His justice and His wisdom</strong>, which is the same shape as the '
    'Jahmiyyah of Lesson 30, who went to excess in <em>tanzīh</em> and ended by stripping Him '
    'of His names.</p></div>' +
    p('<strong>Excess in defending one attribute costs another.</strong> That is the lesson of the '
      'five pairs, and al-qadar is where it is most expensive — because here the attributes at '
      'stake are His power on one side and His justice and wisdom on the other, '
      '<strong>and Ahl al-Sunnah are the only party that does not have to trade one for the '
      'other.</strong>'))
b += B.prose(
    'With this Part 5 is complete: <strong>the four levels of the decree, grouped into two '
    'degrees; that there is no conflict between the decree and the Law; that His decreeing a sin '
    'is not His loving it; and that the servants are doers in reality while Allah is the Creator '
    'of their acts.</strong> And the whole of it rests on two words of Ibn Taymiyyah\'s from the '
    'previous lesson — <strong>%s</strong>, <em>they believe in this and in that.</em>'
    % ar('يُؤْمِنُونَ بِهَذَا وَهَذَا'))

b += B.vocab([
    ('فَاعِلُونَ حَقِيقَةً', 'fāʿilūna ḥaqīqatan',
     'doers in reality',
     'Against the Jabriyyah, who said ascribing acts to them is figurative'),
    ('الجَبْرِيَّة', 'al-jabriyyah', 'the compulsionists',
     'The servant is compelled, having no choice in what issues from him'),
    ('القَدَرِيَّةُ النُّفَاة', 'al-qadariyyah al-nufāh', 'the decree-denying Qadariyyah',
     'The servants create their acts independently of His volition'),
    ('الغُلُوّ', 'al-ghulūw', 'excess',
     'Exceeding the required limit in a thing — in BOTH directions here'),
    ('مَجُوسُ هَذِهِ الأُمَّة', 'majūs hādhihi al-ummah',
     'the Magians of this Ummah',
     'For resembling the dualists — but see the تَنْبِيه: not established as the '
     'Prophet’s ط words'),
    ('مَوْقُوف', 'mawqūf', 'stopping at a Companion',
     'The muṣṭalaḥ term — a report that does not reach the Prophet ط'),
    ('حِكَمٌ وَمَصَالِح', 'ḥikam wa-maṣāliḥ', 'wisdoms and benefits',
     'What the Jabriyyah stripped from His command, prohibition, reward and punishment'),
])
b += B.mcq('ws-l44', [
    ('Which way did each party go to excess?',
     ['Both denied the decree, in different degrees',
      'The Jabriyyah went to excess in affirming the decree until they stripped the servant of '
      'power and choice; the Qadariyyah nufāh in affirming the servants’ acts until they '
      'made them their creators',
      'The Jabriyyah denied the knowledge; the Qadariyyah denied the writing',
      'Both affirmed the decree and denied the Law'], 1),
    ('What is the argument from the servant being <em>described</em> as a believer or one who '
     'prays?',
     ['That the Qurʾān uses these words, so they must be true',
      'Had he been compelled it would not be valid to describe him with them — the act of one '
      'compelled is not ascribed to him, not described of him, and earns him no reward or '
      'punishment',
      'That descriptions follow intentions',
      'That the believer is named for his belief, not his deeds'], 1),
    ('Which part of al-Takwīr 81:28–29 refutes the Jabriyyah?',
     ['%s — because He attached their volition to His' % ar('وَمَا تَشَاءُونَ'),
      '%s — because He affirmed a volition for the servants, and they say they have none'
      % ar('لِمَنْ شَاءَ مِنْكُمْ أَنْ يَسْتَقِيمَ'),
      'Neither; the āyāt refute only the Qadariyyah',
      'Both equally'], 1),
    ('Why does the order of the two āyāt matter?',
     ['Because the first is abrogated by the second',
      'The first grants the servant a real will and the second immediately makes it dependent — '
      'so whoever stops at either āyah has one of the two heresies',
      'Because the second explains the first’s wording',
      'Because they were revealed at different times'], 1),
    ('Why were the Qadariyyah likened to the Magians?',
     ['Because they worshipped fire',
      'Because the Magians affirm two creators, light and darkness, attributing good to one and '
      'evil to the other — and these likewise made a creator alongside Allah',
      'Because they came from Persia',
      'Because they denied the resurrection'], 1),
    ('What is al-Fawzān’s correction of the matn on that phrase?',
     ['That the Prophet ﷺ said it of the Jabriyyah, not the Qadariyyah',
      'That it is not established that the Prophet ﷺ named them so, because they appeared after '
      'his time — most of what censures them is mawqūf upon the Ṣaḥābah',
      'That the ḥadīth is authentic but misapplied',
      'That the phrase is Ibn Taymiyyah’s own coinage'], 1),
    ('What does %s mean?' % ar('مَوْقُوف'),
     ['A report with a broken chain',
      'A report that stops at a Companion rather than reaching the Prophet ﷺ',
      'A report suspended pending verification',
      'A report rejected by the imāms'], 1),
    ('What did the Jabriyyah position cost them, in the end?',
     ['The affirmation of His knowledge',
      'His wisdom and justice — for they made Him reward and punish for what is not of the '
      'servants’ doing, and command what they cannot do',
      'The affirmation of His creating',
      'Belief in the Last Day'], 1),
])
b += B.tf('ws-l44-tf', [
    ('العِبَادُ فَاعِلُونَ حَقِيقَةً، وَاللهُ خَالِقُ أَفْعَالِهِمْ.',
     'The servants are doers in reality, and Allah is the Creator of their acts.', True),
    ('فِعْلُ المُجْبَرِ يُنْسَبُ إِلَيْهِ وَيَسْتَحِقُّ عَلَيْهِ الثَّوَابَ.',
     'The act of one compelled is ascribed to him and earns him reward.', False),
    ('ثَبَتَ أَنَّ النَّبِيَّ ﷺ سَمَّى القَدَرِيَّةَ مَجُوسَ هَذِهِ الأُمَّةِ.',
     'It is established that the Prophet ﷺ named the Qadariyyah the Magians of this Ummah.',
     False),
    ('الجَبْرِيَّةُ غَلَوْا فِي نَفْيِ أَفْعَالِ العِبَادِ.',
     'The Jabriyyah went to excess in negating the actions of the servants.', True),
])
b += B.memorize(
    'لِمَنْ شَاءَ مِنْكُمْ أَنْ يَسْتَقِيمَ · وَمَا تَشَاءُونَ إِلَّا أَنْ يَشَاءَ اللَّهُ '
    'رَبُّ الْعَالَمِينَ',
    'Memorize the two together and in order, because each one alone is a heresy. The first gives '
    'you a real will; the second, in the very next breath, gives it an owner. That is the whole of '
    'al-qadar in two āyāt that happen to be neighbours.')
b += B.aiquiz('That the decree does not conflict with ascribing the servants acts to them in '
              'al-Aqidah al-Wasitiyyah: the Jabriyyah and the Qadariyyah nufah and which way '
              'each went to excess, how al-Fawzan assigns each clause of the matn to the party it '
              'answers, the argument that the act of one compelled is not ascribed to him or '
              'described of him or rewarded, how al-Takwir 81:28 refutes the Jabriyyah and 81:29 '
              'the Qadariyyah, the Magian comparison, and al-Fawzan correction that attributing '
              'that phrase to the Prophet is not established since they appeared after his time '
              'so the censure is mawquf upon the Sahabah')
b += B.further()
b += B.nav('was-l43-mashiah-khalq.html', 'The Volition and the Creating',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l44')

io.open(os.path.join(B.AQ, 'was-l44-afal-al-ibad.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'أَفْعَالُ العِبَادِ بَيْنَ الجَبْرِيَّةِ وَالقَدَرِيَّة',
    'The Acts of the Servants, between the Jabriyyah and the Qadariyyah',
    'Lesson 44 of al-ʿAqīdah al-Wāsiṭiyyah, closing Part 5: how each '
    'clause of the matn answers one of two opposite parties; why describing a man as a believer '
    'or one who prays already refutes compulsion; the two neighbouring '
    'āyāt of al-Takwīr, each dismantling one error — and al-Fawzān’s '
    'correction of the matn on “the Magians of this Ummah”.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الرَّابِعُ وَالأَرْبَعُون', '5',
           'أَفْعَالُ العِبَادِ بَيْنَ الجَبْرِيَّةِ وَالقَدَرِيَّة',
           'The Acts of the Servants, between the Jabriyyah and the Qadariyyah', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l44-afal-al-ibad.html')
