# -*- coding: utf-8 -*-
"""Wasitiyyah L47 -- Part 6: the ranks of the Companions, and the two separate
questions of khilafah and tafdil. Sharh pp.169-175."""
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
    'الإِمَامُ <strong>ابْنُ القَيِّم</strong>, <em>الفَوَائِد</em> — quoted here on the ḥadīth '
    'of the people of Badr.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Name the three sources from which the Companions’ excellence is taken.',
    'Say which “Fatḥ” is meant in al-Ḥadīd 57:10, and why the Muhājirūn are ranked first.',
    'Give Ibn al-Qayyim’s resolution of «do as you wish, I have forgiven you».',
    'Separate the question of %s from the question of %s, and say which one a man is declared '
    'astray for.' % (ar('الخِلَافَة'), ar('التَّفْضِيل')),
])

b += B.heading('فَضْلُ الصَّحَابَةِ وَتَفَاضُلُهُمْ وَمَرَاتِبُهُم',
               'The Excellence of the Companions, and Their Ranks')
b += B.matn(
    'وَيَقْبَلُونَ مَا جَاءَ بِهِ الكِتَابُ وَالسُّنَّةُ وَالإِجْمَاعُ مِنْ '
    'فَضَائِلِهِمْ وَمَرَاتِبِهِمْ. وَيُفَضِّلُونَ مَنْ أَنْفَقَ مِنْ قَبْلِ الفَتْحِ — '
    'وَهُوَ صُلْحُ الحُدَيْبِيَةِ — وَقَاتَلَ، عَلَى مَنْ أَنْفَقَ مِنْ بَعْدُ '
    'وَقَاتَلَ. وَيُقَدِّمُونَ المُهَاجِرِينَ عَلَى الأَنْصَارِ. وَيُؤْمِنُونَ بِأَنَّ '
    'اللهَ قَالَ لِأَهْلِ بَدْرٍ — وَكَانُوا ثَلَاثَمِائَةٍ وَبِضْعَةَ عَشَرَ: '
    '«اعْمَلُوا مَا شِئْتُمْ فَقَدْ غَفَرْتُ لَكُمْ». وَبِأَنَّهُ لَا يَدْخُلُ '
    'النَّارَ أَحَدٌ بَايَعَ تَحْتَ الشَّجَرَةِ كَمَا أَخْبَرَ بِهِ النَّبِيُّ ﷺ، '
    'بَلْ لَقَدْ رَضِيَ اللهُ عَنْهُمْ وَرَضُوا عَنْهُ، وَكَانُوا أَكْثَرَ مِنْ '
    'أَلْفٍ وَأَرْبَعِمِائَةٍ. وَيَشْهَدُونَ بِالجَنَّةِ لِمَنْ شَهِدَ لَهُ رَسُولُ '
    'اللهِ ﷺ، كَالعَشَرَةِ وَثَابِتِ بْنِ قَيْسِ بْنِ شَمَّاسٍ وَغَيْرِهِمْ مِنَ '
    'الصَّحَابَةِ.')
b += B.sharh(
    p('<strong>%s</strong> — <em>and these three sources suffice as witness to their '
      'excellence.</em> Note the third: <strong>%s</strong>. This is not a case built on reports '
      'alone; the Ummah\'s agreement is itself part of the evidence.'
      % (ar('الكِتَابُ وَالسُّنَّةُ وَالإِجْمَاع'), ar('الإِجْمَاع'))) +
    p('<em>Then they are <strong>not upon one degree in excellence</strong> — rather '
      '<strong>according to their precedence to Islam, and the jihād, and the hijrah</strong>, '
      'and according to what they undertook of deeds toward their Prophet and their religion.</em>') +
    p('That is the shape of this whole section, and it is worth noticing before the details. '
      '<strong>Honouring them all does not mean levelling them.</strong> Lesson 46 forbade '
      'disparaging any of them; this lesson ranks them — and both are the same creed.'))

b += B.heading('مَنْ أَنْفَقَ مِنْ قَبْلِ الفَتْح', 'Those Who Spent before the Fatḥ')
b += B.sharh(
    p('Which <em>fatḥ</em>? al-Fawzān: <em>it is <strong>the treaty of al-Ḥudaybiyah</strong>, '
      '<strong>because Allah named it a fatḥ</strong> in His saying %s; <strong>and that is the '
      'well-known view</strong>.</em>' % ar('إِنَّا فَتَحْنَا لَكَ فَتْحًا مُبِينًا')))
b += B.ayah(
    'إِنَّا فَتَحْنَا لَكَ فَتْحًا مُبِينًا',
    '"Indeed We have granted you a clear victory."',
    'Sūrat al-Fatḥ 48:1 · سُورَةُ الفَتْح')
b += B.sharh(
    p('<em>And <strong>%s</strong> is <strong>a well near Makkah</strong>, at which the pledge '
      'took place beneath a tree that was there, <strong>when the mushrikūn barred the Messenger '
      'of Allah &#65018; and his Companions from entering Makkah, so they pledged to him upon '
      'death</strong>. And <strong>this pledge was named a fatḥ, for the good and the victory for '
      'the Muslims that came about because of it.</strong></em>' % ar('الحُدَيْبِيَة')) +
    p('There is a lesson in the naming by itself. <strong>Al-Ḥudaybiyah looked, at the time, like '
      'a defeat</strong> — turned back from the Kaʿbah, terms that seemed one-sided. '
      '<strong>The Qurʾān calls it a clear victory.</strong>') +
    p('<em>And the proof for preferring these is His saying:</em>'))
b += B.ayah(
    'لَا يَسْتَوِي مِنْكُمْ مَنْ أَنْفَقَ مِنْ قَبْلِ الْفَتْحِ وَقَاتَلَ أُولَئِكَ '
    'أَعْظَمُ دَرَجَةً مِنَ الَّذِينَ أَنْفَقُوا مِنْ بَعْدُ وَقَاتَلُوا وَكُلًّا وَعَدَ '
    'اللَّهُ الْحُسْنَى',
    '"Not equal among you are those who spent before the victory and fought — they are greater in '
    'degree than those who spent afterwards and fought. Yet to each Allah has promised the '
    'best."',
    'Sūrat al-Ḥadīd 57:10 · سُورَةُ الحَدِيد')
b += B.prose(
    'Read the last clause before drawing conclusions: <strong>%s — and to each Allah has promised '
    'the best.</strong> The āyah ranks them and then, in the same breath, refuses to disparage '
    'the lower rank. <strong>That is the exact balance of this section</strong>: a difference in '
    'degree is not a difference in standing.' % ar('وَكُلًّا وَعَدَ اللَّهُ الْحُسْنَى'))
b += B.ayah(
    'وَالسَّابِقُونَ الْأَوَّلُونَ مِنَ الْمُهَاجِرِينَ وَالْأَنْصَارِ وَالَّذِينَ '
    'اتَّبَعُوهُمْ بِإِحْسَانٍ رَضِيَ اللَّهُ عَنْهُمْ وَرَضُوا عَنْهُ',
    '"And the first forerunners among the Muhājirūn and the Anṣār, and those who followed them in '
    'excellence — Allah is pleased with them and they are pleased with Him."',
    'Sūrat al-Tawbah 9:100 · سُورَةُ التَّوْبَة')

b += B.heading('تَقْدِيمُ المُهَاجِرِينَ عَلَى الأَنْصَار',
               'The Muhājirūn Ranked before the Anṣār')
b += B.sharh(
    p('<strong>%s</strong> — the plural of %s; <em>and what is meant by them is '
      '<strong>those who migrated from Makkah to Madīnah</strong>. And <strong>%s</strong> in the '
      'language is <strong>leaving</strong>; and in the Sharīʿah: '
      '<strong>the moving from a land of shirk to a land of Islam.</strong></em>'
      % (ar('المُهَاجِرُون'), ar('مُهَاجِر'), ar('الهِجْرَة'))) +
    p('<strong>%s</strong> — <em>that is: <strong>those who supported the Messenger &#65018;</strong>; '
      'and they are <strong>الأَوْس and الخَزْرَج</strong>; <strong>the Prophet &#65018; named '
      'them by this name.</strong></em>' % ar('الأَنْصَار')) +
    p('And the proof for the ranking is a point of method worth having, because it is an argument '
      'from <em>word order</em>: <em>the proof for preferring the Muhājirūn over the Anṣār is '
      '<strong>that Allah put them first in the mention</strong></em> — in al-Tawbah 9:100, in '
      '9:117, and in al-Ḥashr 59:8–9, where the Muhājirūn are named before the Anṣār each time.') +
    p('<em>And for what they undertook of <strong>leaving their lands and their wealth and their '
      'children, seeking the reward and supporting Allah and His Messenger — and their '
      'truthfulness in that.</strong></em>'))

b += B.heading('أَهْلُ بَدْر', 'The People of Badr')
b += B.sharh(
    p('<strong>%s</strong> — <em>a well-known village about <strong>four stages</strong> from '
      'Madīnah, at which occurred the battle <strong>by which Allah gave Islam its '
      'might</strong>; and the day of Badr was named <strong>%s — the Day of the '
      'Criterion.</strong></em>' % (ar('بَدْر'), ar('يَوْمُ الفُرْقَان'))) +
    p('<em>And <strong>%s</strong> — thus their number came in <strong>صَحِيحُ '
      'البُخَارِيّ</strong>.</em> And the ḥadīth itself comes <em>in the two Ṣaḥīḥs, in the story '
      'of <strong>حَاطِبِ بْنِ أَبِي بَلْتَعَةَ</strong></em> — the Companion of Badr who sent '
      'word to Quraysh, and whose pardon is the occasion of these words.'
      % ar('ثَلَاثَمِائَةٍ وَبِضْعَةَ عَشَرَ')))
b += B.hadith(
    'اعْمَلُوا مَا شِئْتُمْ فَقَدْ غَفَرْتُ لَكُمْ',
    '"Do as you wish, for I have already forgiven you."',
    'فِي الصَّحِيحَيْنِ — in the story of Ḥāṭib ibn Abī Baltaʿah رضي الله عنه')
b += B.sharh(
    p('<em>Ibn al-Qayyim said in <strong>«الفَوَائِد»</strong>: '
      '<strong>its meaning has been difficult for many people</strong></em> — and al-Fawzān '
      'quotes his resolution in full, because it is the one that neither empties the promise nor '
      'licenses anything:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.93rem">'
    '<p style="margin:0 0 .7rem"><em>— <strong>What we think concerning it, and Allah knows '
    'best, is that this is an address to a people whom Allah knew would not leave their religion, '
    'but would die upon Islam</strong>; and that <strong>they may commit what others commit of '
    'sins — but He will not leave them persisting upon them</strong>; rather '
    '<strong>He grants them success to a sincere repentance, and seeking forgiveness, and good '
    'deeds which erase the trace of that.</strong></em></p>'
    '<p style="margin:0 0 .7rem"><em>— <strong>And their being singled out by this rather '
    'than others is because that was realised in them</strong>, and that they are forgiven.</em></p>'
    '<p style="margin:0"><em>— <strong>And that does not prevent the forgiveness having come '
    'about by causes arising from them</strong>; just as <strong>it does not require that they '
    'abandon the obligations in reliance upon the forgiveness.</strong> '
    '<strong>For had it been obtained without their continuing to carry out the commands, they '
    'would not have needed, after that, a prayer, nor a ḥajj, nor a zakāh, nor a '
    'jihād — and this is impossible.</strong></em></p></div>' +
    p('The last step is the one that settles it, and it is an argument from fact rather than from '
      'theory. <strong>The people of Badr went on praying, fasting, giving and fighting for the '
      'rest of their lives.</strong> So whatever the words meant, they plainly did not mean what '
      'the licensing reading says they meant — <em>the men who heard them did not understand them '
      'that way.</em>'))

b += B.heading('بَيْعَةُ الرِّضْوَان', 'The Pledge of Riḍwān')
b += B.sharh(
    p('<em>This speech concerns <strong>the people of بَيْعَةِ الرِّضْوَان</strong>, the pledge '
      'that took place at al-Ḥudaybiyah.</em> And al-Fawzān says the Shaykh mentioned '
      '<strong>two distinctions</strong> for them:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.92rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>الأُولَى</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<strong>not one of them enters the Fire</strong> — <em>its proof being what is in '
    '<strong>Ṣaḥīḥ Muslim</strong> from the ḥadīth of '
    '<strong>Jābir</strong> رضي الله عنه: '
    '«<span dir="rtl" lang="ar">لَا يَدْخُلُ النَّارَ أَحَدٌ بَايَعَ تَحْتَ '
    'الشَّجَرَةِ</span>»</em></td></tr>'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>الثَّانِيَة</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<strong>that Allah was pleased with them</strong> — <em>and this is '
    '<strong>the explicit text of the Qurʾān</strong></em></td></tr>'
    '</table></div>')
b += B.ayah(
    'لَقَدْ رَضِيَ اللَّهُ عَنِ الْمُؤْمِنِينَ إِذْ يُبَايِعُونَكَ تَحْتَ الشَّجَرَةِ '
    'فَعَلِمَ مَا فِي قُلُوبِهِمْ فَأَنْزَلَ السَّكِينَةَ عَلَيْهِمْ',
    '"Allah was certainly pleased with the believers when they pledged allegiance to you beneath '
    'the tree. He knew what was in their hearts, so He sent down tranquillity upon them."',
    'Sūrat al-Fatḥ 48:18 · سُورَةُ الفَتْح')
b += B.prose(
    'Notice the clause between the pleasure and its reward: <strong>%s — He knew what was in '
    'their hearts.</strong> The pleasure is not announced over an outward act whose sincerity was '
    'unexamined. <strong>It is announced over men whose hearts had already been inspected.</strong> '
    'Which is why a text of this strength can be given about a particular group of named people '
    'without being a general rule about anyone who takes a pledge.'
    % ar('فَعَلِمَ مَا فِي قُلُوبِهِمْ'))

b += B.heading('الشَّهَادَةُ بِالجَنَّة', 'Testifying to Paradise')
b += B.sharh(
    p('<em>That is: Ahl al-Sunnah <strong>testify to Paradise for whomever the Messenger '
      '&#65018; testified to it</strong>. <strong>As for one whom the Messenger &#65018; did not '
      'testify to, they do not testify for him</strong> — <strong>because in that is speaking '
      'about Allah without knowledge</strong>; <strong>but they hope for the doers of good and '
      'fear for the doers of evil.</strong> <strong>And this is a foundation among the '
      'foundations of the creed.</strong></em>') +
    p('That is a restraint worth dwelling on, because the natural impulse runs the other way. '
      '<strong>It is not piety to pronounce a righteous man into Paradise.</strong> The ruling '
      'belongs to Allah, and announcing it on His behalf is the fault — however good the person '
      'and however warm the intention. <strong>Hope and fear are what the believer is left '
      'with</strong>, which is exactly the position Lesson 36 described at the grave.') +
    p('<strong>%s</strong> — al-Fawzān names them: <em>أَبُو بَكْرٍ · عُمَرُ · عُثْمَانُ · '
      'عَلِيٌّ · عَبْدُ الرَّحْمَنِ بْنُ عَوْفٍ · الزُّبَيْرُ بْنُ العَوَّامِ · سَعْدُ بْنُ '
      'أَبِي وَقَّاصٍ · سَعِيدُ بْنُ زَيْدٍ · أَبُو عُبَيْدَةَ بْنُ الجَرَّاحِ · طَلْحَةُ '
      'بْنُ عُبَيْدِ اللهِ</em> رضي الله عنهم — <em>and <strong>the aḥādīth are authentic in '
      'testifying to Paradise for these.</strong></em>' % ar('العَشَرَة')) +
    p('<strong>%s</strong> — <em>he was <strong>the orator of the Messenger of Allah '
      '&#65018;</strong>, and <strong>his glad tidings of Paradise is established in صَحِيحُ '
      'البُخَارِيّ</strong></em>. <strong>%s</strong> — <em>such as '
      '<strong>عُكَّاشَةُ بْنُ مِحْصَنٍ</strong> and <strong>عَبْدُ اللهِ بْنُ سَلَامٍ</strong> '
      'and others.</em>'
      % (ar('وَثَابِتُ بْنُ قَيْسِ بْنِ شَمَّاسٍ'), ar('وَغَيْرُهُمْ مِنَ الصَّحَابَةِ'))))

b += B.heading('مَسْأَلَتَانِ · الخِلَافَةُ وَالتَّفْضِيل',
               'Two Separate Questions — the Caliphate and the Ranking')
b += B.matn(
    'وَيُقِرُّونَ بِمَا تَوَاتَرَ بِهِ النَّقْلُ عَنْ أَمِيرِ المُؤْمِنِينَ عَلِيِّ بْنِ '
    'أَبِي طَالِبٍ رَضِيَ اللهُ عَنْهُ وَغَيْرِهِ: أَنَّ خَيْرَ هَذِهِ الأُمَّةِ بَعْدَ '
    'نَبِيِّهَا أَبُو بَكْرٍ ثُمَّ عُمَرُ، وَيُثَلِّثُونَ بِعُثْمَانَ وَيُرَبِّعُونَ '
    'بِعَلِيٍّ رَضِيَ اللهُ عَنْهُمْ… وَإِنْ كَانَتْ هَذِهِ المَسْأَلَةُ — مَسْأَلَةُ '
    'عُثْمَانَ وَعَلِيٍّ — لَيْسَتْ مِنَ الأُصُولِ الَّتِي يُضَلَّلُ المُخَالِفُ فِيهَا '
    'عِنْدَ جُمْهُورِ أَهْلِ السُّنَّةِ، لَكِنِ الَّتِي يُضَلَّلُ فِيهَا مَسْأَلَةُ '
    'الخِلَافَةِ. وَمَنْ طَعَنَ فِي خِلَافَةِ أَحَدٍ مِنْ هَؤُلَاءِ فَهُوَ أَضَلُّ مِنْ '
    'حِمَارِ أَهْلِهِ.')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is, what is established by the route of '
      '<strong>%s — and al-tawātur is the strongest of the chains.</strong></em> The student met '
      'its definition in Lesson 31: what a group transmitted whose collusion upon a lie is ruled '
      'out, at every link.' % (ar('مَا تَوَاتَرَ بِهِ النَّقْلُ'), ar('التَّوَاتُر'))) +
    p('And note <strong>whose</strong> transmission it is. The report that Abū Bakr and then ʿUmar '
      'are the best of this Ummah is mutawātir <strong>from ʿAlī ibn Abī Ṭālib himself</strong> '
      '— <em>and in this mutawātir narration from ʿAlī is <strong>a refutation of the Rāfiḍah, '
      'who prefer ʿAlī over Abū Bakr and ʿUmar and advance him over them in the caliphate, and so '
      'impugn the caliphate of the two Shaykhs.</strong></em>') +
    p('<strong>The man they claim to be defending is the man who narrated against them.</strong>'))
b += B.sharh(
    p('<em>And this discussion comprises <strong>two questions</strong>.</em> Keeping them apart '
      'is the whole point of the section:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.91rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>مَسْأَلَةُ الخِلَافَة</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<em><strong>Ahl al-Sunnah — including the Ṣaḥābah — reached '
    'CONSENSUS</strong> that the caliph after the Messenger of Allah &#65018; is '
    '<strong>Abū Bakr, then ʿUmar, then ʿUthmān, then '
    'ʿAlī</strong></em></td></tr>'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>مَسْأَلَةُ التَّفْضِيل</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<em>they reached consensus that <strong>the best after the Prophet &#65018; is Abū '
    'Bakr then ʿUmar</strong> — <strong>and DIFFERED over ʿUthmān and '
    'ʿAlī, which of them is more excellent</strong></em></td></tr>'
    '</table></div>' +
    p('<em>The Shaykh mentioned <strong>three statements</strong> on it: '
      '<strong>advancing ʿUthmān · advancing ʿAlī · withholding from advancing either over the '
      'other.</strong></em>') +
    p('<em>And the Shaykh indicated a preference for the first — advancing ʿUthmān — '
      '<strong>for three reasons</strong>:</em>') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.93rem">'
    '<p style="margin:0 0 .6rem"><strong>١</strong> — <em>what the narrations concerning the '
    'virtues of ʿUthmān indicate.</em></p>'
    '<p style="margin:0 0 .6rem"><strong>٢</strong> — <em>the consensus of the Companions on '
    'advancing ʿUthmān in the pledge — <strong>and that was only because he was '
    'more excellent; so their ordering in excellence is like their ordering in the '
    'caliphate.</strong></em></p>'
    '<p style="margin:0"><strong>٣</strong> — <em>that the affair of Ahl al-Sunnah '
    '<strong>settled</strong> upon advancing ʿUthmān then ʿAlī.</em></p></div>' +
    p('And two statements from the Companions themselves. <strong>عَبْدُ الرَّحْمَنِ بْنُ '
      'عَوْفٍ</strong> said to ʿAlī رضي الله عنه: <em>I looked into the affair of the people, and '
      'I did not find them holding anyone equal to ʿUthmān.</em> And <strong>أَبُو '
      'أَيُّوبَ</strong>: <em>whoever does not advance ʿUthmān over ʿAlī has belittled the '
      'Muhājirūn and the Anṣār.</em>') +
    p('<em>And <strong>ʿAlī رضي الله عنه was among those who pledged to him, and used to carry out '
      'the prescribed punishments before him.</strong></em> Which is a quiet and complete answer '
      'to anyone claiming ʿAlī\'s cause against ʿUthmān: <strong>ʿAlī served in his '
      'administration.</strong>'))

b += B.heading('أَيُّ المَسْأَلَتَيْنِ يُضَلَّلُ فِيهَا', 'Which of the Two a Man Is Declared Astray For')
b += B.sharh(
    p('<em>The Shaykh رحمه الله set out a weighing between the two questions — the question of '
      'advancing ʿAlī over ʿUthmān <strong>in excellence</strong>, and the question of advancing '
      'ʿAlī over the others <strong>in the caliphate</strong> — in terms of <strong>the gravity '
      'that follows from each.</strong></em>') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.91rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);vertical-align:top">'
    'preferring ʿAlī over ʿUthmān <strong>in excellence</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<strong>he is NOT declared astray</strong> — <em>given the existence of the difference '
    'over it among Ahl al-Sunnah, even though the preponderant view is ʿUthmān</em></td></tr>'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);vertical-align:top">'
    'preferring ʿAlī <strong>in the caliphate</strong>, or over Abū Bakr and '
    'ʿUmar <strong>in excellence</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<strong>he IS declared astray</strong></td></tr>'
    '</table></div>' +
    p('And al-Fawzān gives the ground on which each caliphate rests, which is why the second row '
      'is settled: <em><strong>Abū Bakr</strong> — for his excellence, his precedence, '
      '<strong>the Prophet\'s &#65018; advancing him over all the Companions</strong>, and the '
      'Companions\' consensus on pledging to him. Then <strong>ʿUmar</strong> — for his '
      'excellence, his precedence, <strong>Abū Bakr\'s covenant to him</strong>, and the Ummah\'s '
      'agreement upon him. Then <strong>ʿUthmān</strong> — for <strong>the people of the shūrā '
      'advancing him</strong> and the Ummah\'s agreement. Then <strong>ʿAlī</strong> — for his '
      'excellence and <strong>the consensus of the people of his age upon him.</strong></em>') +
    p('<em>And these are <strong>the four caliphs</strong> pointed to in the ḥadīth of '
      '<strong>العِرْبَاضِ بْنِ سَارِيَةَ</strong> رضي الله عنه, in his &#65018; saying: '
      '<strong>«عَلَيْكُمْ بِسُنَّتِي وَسُنَّةِ الخُلَفَاءِ الرَّاشِدِينَ المَهْدِيِّينَ مِنْ '
      'بَعْدِي»</strong></em> — <em>hold to my Sunnah and the Sunnah of the rightly-guided, '
      'rightly-directed caliphs after me.</em>') +
    p('<em>And this is why the Shaykh said: <strong>%s</strong> — <strong>because of his '
      'opposing the text and the consensus, with no proof and no evidence</strong>; and that is '
      'like <strong>the Rāfiḍah, who claim that the caliphate after the Prophet &#65018; belongs '
      'to ʿAlī ibn Abī Ṭālib.</strong></em>'
      % ar('وَمَنْ طَعَنَ فِي خِلَافَةِ أَحَدٍ مِنْ هَؤُلَاءِ فَهُوَ أَضَلُّ مِنْ حِمَارِ أَهْلِهِ')))
b += B.prose(
    'The distinction this section draws is one of the most practically useful in the whole book, '
    'and it is worth stating plainly: <strong>Ahl al-Sunnah differ among themselves on one of '
    'these questions and do not declare each other astray for it; and they do not differ at all '
    'on the other.</strong> A settled matter and an open matter sit side by side here, and the '
    'author is careful to tell you which is which — <em>which is itself a lesson in how to hold a '
    'position you believe is preponderant without making it a test of orthodoxy.</em>')

b += B.vocab([
    ('الفَتْح', 'al-fatḥ', 'the Victory',
     'Here: ṣulḥ al-Ḥudaybiyah — because Allah named it a fatḥ'),
    ('الحُدَيْبِيَة', 'al-Ḥudaybiyah', 'al-Ḥudaybiyah',
     'A well near Makkah, where they pledged to him upon death'),
    ('الهِجْرَة', 'al-hijrah', 'the migration',
     'Linguistically: leaving; in the Sharīʿah: moving from a land of shirk to a land '
     'of Islam'),
    ('الأَنْصَار', 'al-Anṣār', 'the Helpers',
     'Al-Aws and al-Khazraj — the Prophet ط named them so'),
    ('يَوْمُ الفُرْقَان', 'yawm al-furqān', 'the Day of the Criterion',
     'The name of the day of Badr'),
    ('بَيْعَةُ الرِّضْوَان', 'bayʿat al-riḍwān', 'the Pledge of Riḍwān',
     'Two distinctions: none of them enters the Fire; and Allah was pleased with them'),
    ('العَشَرَة', 'al-ʿasharah', 'the Ten',
     'Those for whom the aḥādīth authentically testify to Paradise'),
    ('التَّوَاتُر', 'al-tawātur', 'mass transmission',
     'The strongest of the chains — and this report comes through ʿAlī himself'),
    ('التَّفْضِيل', 'al-tafḍīl', 'the ranking',
     'An OPEN question between ʿUthmān and ʿAlī — unlike the caliphate'),
])
b += B.mcq('ws-l47', [
    ('From what three sources is the Companions’ excellence taken?',
     ['The Qurʾān, analogy and consensus',
      'The Book, the Sunnah, and the consensus',
      'The Sunnah, the āthār and the historians',
      'The Qurʾān and the Sunnah only'], 1),
    ('Which "Fatḥ" is meant in al-Ḥadīd 57:10, and why?',
     ['The conquest of Makkah, because it was the greatest victory',
      'The treaty of al-Ḥudaybiyah, because Allah named it a fatḥ in Sūrat al-Fatḥ 48:1',
      'The battle of Badr, because it was the Day of the Criterion',
      'The opening of Khaybar'], 1),
    ('What does the closing clause of al-Ḥadīd 57:10 add?',
     ['That the later group receives no reward',
      '%s — to each Allah has promised the best: it ranks them and refuses to disparage the lower '
      'rank in the same breath' % ar('وَكُلًّا وَعَدَ اللَّهُ الْحُسْنَى'),
      'That the ranking applies only in this world',
      'That spending outweighs fighting'], 1),
    ('What is the proof that the Muhājirūn are ranked before the Anṣār?',
     ['An explicit ḥadīth to that effect',
      'That Allah put them first in the mention — in al-Tawbah 9:100, 9:117 and al-Ḥashr 59:8–9',
      'That they were more numerous',
      'The consensus of the Tābiʿūn'], 1),
    ('How does Ibn al-Qayyim resolve «do as you wish, I have forgiven you»?',
     ['That it was abrogated',
      'It addresses people Allah knew would die upon Islam; they may sin but He will not leave '
      'them persisting — granting them repentance and good deeds that erase it',
      'That it applies only to sins committed before Badr',
      'That the wording is not established'], 1),
    ('What is Ibn al-Qayyim’s closing argument against the licensing reading?',
     ['That no scholar held it',
      'That had forgiveness come without continuing to obey, they would not have needed prayer, '
      'ḥajj, zakāh or jihād afterwards — which is impossible',
      'That the Companions were infallible',
      'That the ḥadīth is addressed to the Prophet ﷺ alone'], 1),
    ('Why do Ahl al-Sunnah not testify to Paradise for a righteous person generally?',
     ['Because deeds may be nullified later',
      'Because that is speaking about Allah without knowledge — rather they hope for the doers of '
      'good and fear for the doers of evil',
      'Because only the Companions may be testified for',
      'Because it would make people complacent'], 1),
    ('Which of the two questions is a man declared astray over?',
     ['Both equally',
      'The caliphate — and preferring ʿAlī over Abū Bakr and ʿUmar in excellence; but not '
      'preferring ʿAlī over ʿUthmān in excellence',
      'The ranking only',
      'Neither; both are open'], 1),
    ('What is notable about the chain of the report that Abū Bakr then ʿUmar are the best?',
     ['It is reported only by the Umayyads',
      'It is mutawātir from ʿAlī ibn Abī Ṭālib himself — the man the Rāfiḍah claim to defend',
      'It is a solitary report',
      'It is reported from Abū Bakr himself'], 1),
])
b += B.tf('ws-l47-tf', [
    ('الصَّحَابَةُ عَلَى دَرَجَةٍ وَاحِدَةٍ فِي الفَضْلِ.',
     'The Companions are upon one degree in excellence.', False),
    ('سُمِّيَ صُلْحُ الحُدَيْبِيَةِ فَتْحًا فِي القُرْآنِ.',
     'The treaty of al-Ḥudaybiyah is called a victory in the Qurʾān.', True),
    ('نَشْهَدُ بِالجَنَّةِ لِكُلِّ مَنْ ظَهَرَ صَلَاحُهُ.',
     'We testify to Paradise for everyone whose righteousness is apparent.', False),
    ('مَسْأَلَةُ الخِلَافَةِ مِمَّا يُضَلَّلُ فِيهَا المُخَالِفُ.',
     'The question of the caliphate is one in which the opponent is declared astray.', True),
])
b += B.memorize(
    'وَكُلًّا وَعَدَ اللَّهُ الْحُسْنَى',
    'The clause that closes al-Ḥadīd 57:10, immediately after ranking one group above another. '
    'Learn the ranking and this clause together, or you will have half the verse: a difference in '
    'degree is not a difference in standing.')
b += B.aiquiz('The ranks of the Companions in al-Aqidah al-Wasitiyyah: the three sources of their '
              'excellence, al-Hudaybiyah as the Fath of al-Hadid 57:10 and the clause wa-kullan '
              'waada Llahu al-husna, the Muhajirun ranked first by word order, Ibn al-Qayyims '
              'resolution of "do as you wish" with the argument that they went on praying and '
              'fasting afterwards, the two distinctions of Bayat al-Ridwan, why Ahl al-Sunnah do '
              'not testify to Paradise without a text, and the separation of the question of the '
              'caliphate from the question of ranking')
b += B.further()
b += B.nav('was-l46-wajib-nahw-al-sahabah.html', 'The Obligation toward the Companions',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l47')

io.open(os.path.join(B.AQ, 'was-l47-maratib-al-sahabah.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'مَرَاتِبُ الصَّحَابَةِ · الخِلَافَةُ وَالتَّفْضِيل',
    'The Ranks of the Companions — the Caliphate and the Ranking',
    'Lesson 47 of al-ʿAqīdah al-Wāsiṭiyyah: why honouring them all '
    'does not mean levelling them; al-Ḥudaybiyah as the Fatḥ, and the clause that '
    'refuses to disparage the lower rank; Ibn al-Qayyim on “do as you wish”; and the '
    'careful separation of a settled question from an open one.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ السَّابِعُ وَالأَرْبَعُون', '6',
           'مَرَاتِبُ الصَّحَابَةِ · الخِلَافَةُ وَالتَّفْضِيل',
           'The Ranks of the Companions — the Caliphate and the Ranking', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l47-maratib-al-sahabah.html')
