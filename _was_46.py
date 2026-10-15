# -*- coding: utf-8 -*-
"""Wasitiyyah L46 -- Part 6: the obligation toward the Companions of the
Messenger of Allah, soundness of heart and tongue toward them.
Sharh pp.166-168, with a cross-reference to Imam Ahmad's Usul al-Sunnah."""
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
    'الإِمَامُ <strong>الشَّوْكَانِيّ</strong> — quoted at length here on al-Ḥashr 59:10.',
    'الإِمَامُ <strong>أَحْمَدُ بْنُ حَنْبَل</strong>, <em>أُصُولُ السُّنَّة</em> §42 — '
    'cross-referenced on this page; the same ruling in the words of an imām of the third century.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'State the two soundnesses the matn requires, and find each of them inside al-Ḥashr 59:10.',
    'Give al-Fawzān’s four reasons for the Companions’ precedence.',
    'Explain why the little a Companion spent outweighs a mountain of gold from anyone after them.',
    'Give the principle about deeds that the ḥadīth establishes in passing.',
])

b += B.heading('الوَاجِبُ نَحْوَ أَصْحَابِ رَسُولِ اللهِ ﷺ',
               'The Obligation toward the Companions of the Messenger of Allah ﷺ')
b += B.matn(
    'وَمِنْ أُصُولِ أَهْلِ السُّنَّةِ وَالجَمَاعَةِ: سَلَامَةُ قُلُوبِهِمْ '
    'وَأَلْسِنَتِهِمْ لِأَصْحَابِ رَسُولِ اللهِ ﷺ، كَمَا وَصَفَهُمُ اللهُ بِهِ فِي '
    'قَوْلِهِ تَعَالَى: ﴿وَالَّذِينَ جَاءُوا مِنْ بَعْدِهِمْ يَقُولُونَ رَبَّنَا '
    'اغْفِرْ لَنَا وَلِإِخْوَانِنَا الَّذِينَ سَبَقُونَا بِالْإِيمَانِ وَلَا تَجْعَلْ '
    'فِي قُلُوبِنَا غِلًّا لِلَّذِينَ آمَنُوا رَبَّنَا إِنَّكَ رَءُوفٌ رَحِيمٌ﴾، '
    'وَطَاعَةُ الرَّسُولِ ﷺ فِي قَوْلِهِ: «لَا تَسُبُّوا أَصْحَابِي، فَوَالَّذِي '
    'نَفْسِي بِيَدِهِ لَوْ أَنَّ أَحَدَكُمْ أَنْفَقَ مِثْلَ أُحُدٍ ذَهَبًا مَا بَلَغَ '
    'مُدَّ أَحَدِهِمْ وَلَا نَصِيفَهُ».')
b += B.sharh(
    p('al-Fawzān unpacks the two soundnesses the matn names: '
      '<strong>%s</strong> — <em>from <strong>rancour, spite and hatred</strong></em>; and '
      '<strong>%s</strong> — <em>from <strong>disparagement, cursing and reviling</strong></em>.'
      % (ar('سَلَامَةُ قُلُوبِهِمْ'), ar('وَأَلْسِنَتِهِمْ'))) +
    p('Note that the obligation is stated in two places — <strong>the heart and the '
      'tongue</strong> — and in that order. <strong>It is not enough to hold the tongue while the '
      'heart carries the grudge</strong>, which is why the matn names the heart first.') +
    p('And why them? al-Fawzān gives four grounds: <em>for <strong>their excellence</strong>, and '
      '<strong>their precedence</strong>, and <strong>their being singled out by the companionship '
      'of the Prophet &#65018;</strong>, and for what they have of excellence over the whole '
      'Ummah</em> —') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.94rem"><em>— <strong>because they are the ones who '
    'carried the Sharīʿah from him &#65018; and conveyed it to those after '
    'them</strong>; and for <strong>their jihād alongside the Messenger &#65018; and their '
    'supporting of him.</strong></em></p></div>' +
    p('The first of those is the one with teeth. <strong>Every ruling the student has learned on '
      'this track reached him through these men.</strong> To hold that they were unreliable is to '
      'hold that the religion did not arrive — which is why this is a chapter of creed and not of '
      'manners.') +
    p('<em>And the Shaykh\'s purpose in composing this section is <strong>the refutation of the '
      'Rāfiḍah and the Khawārij, who revile the Companions and hate them and deny their '
      'excellences</strong>; and the making clear of <strong>Ahl al-Sunnah\'s innocence of this '
      'foul madhhab</strong>, and that they are with the Companions of their Prophet.</em>'))
b += B.ayah(
    'وَالَّذِينَ جَاءُوا مِنْ بَعْدِهِمْ يَقُولُونَ رَبَّنَا اغْفِرْ لَنَا وَلِإِخْوَانِنَا '
    'الَّذِينَ سَبَقُونَا بِالْإِيمَانِ وَلَا تَجْعَلْ فِي قُلُوبِنَا غِلًّا لِلَّذِينَ '
    'آمَنُوا رَبَّنَا إِنَّكَ رَءُوفٌ رَحِيمٌ',
    '"And those who came after them say: our Lord, forgive us and our brothers who preceded us in '
    'faith, and put not in our hearts rancour toward those who believed. Our Lord, You are '
    'Kind, Merciful."',
    'Sūrat al-Ḥashr 59:10 · سُورَةُ الحَشْر')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>after the Muhājirūn and the Anṣār</strong>; and '
      'they are <strong>those who follow them in excellence, until the Day of Rising, from the '
      'generality of the Muslims.</strong></em>' % ar('وَالَّذِينَ جَاءُوا مِنْ بَعْدِهِمْ')) +
    p('<strong>%s</strong> — <em>what is meant by the brotherhood here is '
      '<strong>the brotherhood of religion</strong>; so <strong>they seek forgiveness for '
      'themselves and for those who went before them</strong> of the Muhājirūn and the Anṣār.</em>'
      % ar('وَلِإِخْوَانِنَا الَّذِينَ سَبَقُونَا بِالْإِيمَانِ')) +
    p('<strong>%s</strong> — <em>that is: <strong>deceit, hatred and envy</strong></em>; '
      '<strong>%s</strong> — <em>that is, the people of faith; <strong>and the Companions enter '
      'into that by the foremost entry</strong>, <strong>because they are the noblest of the '
      'believers, and because the passage is about them.</strong></em>'
      % (ar('وَلَا تَجْعَلْ فِي قُلُوبِنَا غِلًّا'), ar('لِلَّذِينَ آمَنُوا'))))
b += B.sharh(
    p('And now the observation that makes the author\'s choice of this āyah exact, rather than '
      'merely apt. <strong>The matn asks for soundness of hearts and tongues — and the āyah '
      'contains both halves, in order:</strong>') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.93rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>رَبَّنَا اغْفِرْ لَنَا وَلِإِخْوَانِنَا</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '→ <strong><span dir="rtl" lang="ar">سَلَامَةُ الأَلْسِنَة</span></strong> — '
    'the soundness of the tongues</td></tr>'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>وَلَا تَجْعَلْ فِي قُلُوبِنَا غِلًّا</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '→ <strong><span dir="rtl" lang="ar">سَلَامَةُ القُلُوب</span></strong> — '
    'the soundness of the hearts</td></tr>'
    '</table></div>' +
    p('<em>So the shāhid of the āyah is: <strong>the excellence of the Companions, for their '
      'precedence in faith</strong>; and <strong>the seeking of forgiveness for them and asking '
      'Allah\'s pleasure for them</strong>; and in it is <strong>the soundness of the hearts and '
      'the tongues of Ahl al-Sunnah toward the Companions of the Messenger of Allah '
      '&#65018;.</strong></em>') +
    p('And a point from the āyah\'s context that sharpens it. These verses are about '
      '<strong>the distribution of the %s</strong> — the three groups entitled to a share: the '
      'Muhājirūn (59:8), the Anṣār (59:9), and <em>those who came after them</em> (59:10), '
      'described by this very duʿāʾ. al-Fawzān notes that <strong>whoever is not of this '
      'description does not deserve anything of the fayʾ.</strong>' % ar('الفَيْء')) +
    p('<strong>Love of the Companions is written into the qualification for a share of the '
      'Muslims\' wealth.</strong> It is not a sentiment the later generations are encouraged '
      'toward; it is the description by which the Qurʾān identifies them at all.'))

b += B.heading('كَلَامُ الشَّوْكَانِيِّ عَلَى الآيَة', 'al-Shawkānī on This Āyah')
b += B.sharh(
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.93rem">'
    '<p style="margin:0 0 .7rem"><em>— <strong>So whoever does not seek forgiveness for the '
    'Companions in general, and ask Allah’s pleasure for them, has opposed what Allah '
    'commanded in this āyah.</strong></em></p>'
    '<p style="margin:0 0 .7rem"><em>— <strong>And if he finds in his heart rancour toward '
    'them, then a goading of Shayṭān has struck him</strong>, and there has befallen him '
    '<strong>an ample share of disobedience to Allah, by enmity toward His allies and toward the '
    'best nation of His Prophet</strong> &#65018; — <strong>and a door of abandonment has '
    'opened for him, by which he arrives at the Fire of Hell, if he does not rescue himself by '
    'taking refuge with Allah</strong> سبحانه and imploring Him '
    '<strong>to pull out of his heart what has entered it of rancour toward the best of '
    'generations and the noblest of this Ummah.</strong></em></p>'
    '<p style="margin:0"><em>— And such a man is <strong>only afflicted with it by being '
    'tried with a teacher from the Rāfiḍah</strong>, or <strong>a companion from the '
    'enemies of the best of the Ummah</strong> — <strong>those whom Shayṭān has '
    'toyed with, and for whom he has made attractive the assorted lies, the fabricated tales and '
    'the invented fictions; and has turned them away from the Book of Allah, which falsehood does '
    'not approach from before it or from behind it.</strong></em></p></div>' +
    p('Two things in that are worth keeping. First, the diagnosis is not of an argument but of a '
      '<em>route</em>: <strong>al-Shawkānī says nobody arrives at this on his own</strong> — it '
      'comes through a teacher or a companion. Second, the cure he prescribes is not a '
      'counter-argument either. <strong>It is duʿāʾ</strong> — asking Allah to pull the rancour '
      'out — which is exactly what the āyah itself was already teaching the reader to say.'))

b += B.heading('حَدِيثُ «لَا تَسُبُّوا أَصْحَابِي»', 'The Ḥadīth: "Do Not Revile My Companions"')
b += B.hadith(
    'لَا تَسُبُّوا أَصْحَابِي، فَوَالَّذِي نَفْسِي بِيَدِهِ لَوْ أَنَّ أَحَدَكُمْ أَنْفَقَ '
    'مِثْلَ أُحُدٍ ذَهَبًا مَا بَلَغَ مُدَّ أَحَدِهِمْ وَلَا نَصِيفَهُ',
    '"Do not revile my Companions. For by the One in whose Hand is my soul, were one of you to '
    'spend the like of Uḥud in gold, he would not reach the mudd of one of them, nor half of it."',
    'الحَدِيثُ مُتَّفَقٌ عَلَيْهِ — al-Bukhārī and Muslim')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>do not disparage and do not insult</strong></em>. '
      '<strong>%s</strong> is the plural of %s; <em>and one who kept company with the Prophet '
      '&#65018; is called a <strong>%s</strong> — and he is <strong>whoever met the Prophet '
      '&#65018; as a believer in him and died upon that.</strong></em>'
      % (ar('لَا تَسُبُّوا'), ar('أَصْحَابِي'), ar('صَاحِب'), ar('صَحَابِيّ'))) +
    p('<strong>%s</strong> — <em>this is <strong>an oath from the Prophet &#65018;</strong>, by '
      'which he intends <strong>to emphasise what follows it</strong></em>. '
      '<strong>%s</strong> — <em>the answer to the conditional</em>; and <strong>%s</strong> is '
      '<em>a well-known mountain in Madīnah, named so <strong>because it stands alone, apart from '
      'the mountains</strong></em>; and <strong>%s</strong> is <em>manṣūb as tamyīz</em>.'
      % (ar('فَوَالَّذِي نَفْسِي بِيَدِهِ'), ar('لَوْ أَنَّ أَحَدَكُمْ أَنْفَقَ'),
         ar('أُحُد'), ar('ذَهَبًا'))) +
    p('<strong>%s</strong> — <em>al-mudd is <strong>a measure, and it is a quarter of the '
      'Prophetic ṣāʿ</strong></em>; <strong>%s</strong> — <em>a variant form of %s</em>.'
      % (ar('مَا بَلَغَ مُدَّ أَحَدِهِمْ'), ar('وَلَا نَصِيفَهُ'), ar('النِّصْف'))) +
    p('So the comparison is deliberately extreme at both ends: <strong>a mountain of gold against '
      'a double handful of grain — and not even half of it.</strong>'))
b += B.sharh(
    p('<em>And the meaning is: <strong>that abundant spending in the path of Allah from other '
      'than the Companions does not equal the little spending of the Companions.</strong></em> '
      'And al-Fawzān gives the reason, which is the finest reasoning in the lesson because it '
      'explains rather than merely asserts the precedence:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.94rem"><em>— <strong>And that is because the '
    'īmān which was in their hearts at the time of the spending</strong> — '
    '<strong>at the beginning of Islam, and the fewness of its people, and the abundance of what '
    'turned people away from it, and the weakness of the motives toward it</strong> — '
    '<strong>it is not possible that the like of it should be attained by anyone who came after '
    'them.</strong></em></p></div>' +
    p('Four circumstances, and every one of them a <em>disincentive</em>. '
      '<strong>The religion was new, its people were few, the pressures against it were many, and '
      'there was nothing in the world to be gained by joining it.</strong> A dirham given under '
      'those conditions is not the same act as a dirham given now, and the ḥadīth is not '
      'exaggerating — it is weighing the faith that produced the gift, not the gift.') +
    p('<em>And the shāhid from the ḥadīth: <strong>the forbiddance of reviling the Companions, and '
      'the making clear of their excellence over others — and that the deed admits of degrees '
      'according to the intention of its doer, and according to the TIME in which it was '
      'discharged.</strong></em>') +
    p('That last clause is a principle worth carrying well beyond this chapter. '
      '<strong>The same act is not the same deed in every age.</strong> Which cuts both ways, and '
      'the second way is the encouraging one: a small obedience held onto in a time when almost '
      'nobody is holding onto it is weighed by the conditions it was done in.') +
    p('<em>And in the ḥadīth: <strong>that whoever loves the Companions and praises them has '
      'obeyed the Messenger &#65018;; and whoever reviles them and hates them has disobeyed the '
      'Messenger &#65018;.</strong></em>'))

b += B.heading('مُوَافَقَةُ الإِمَامِ أَحْمَدَ فِي أُصُولِ السُّنَّة',
               'Imām Aḥmad, in Uṣūl al-Sunnah, on the Same Point')
b += B.prose(
    'It is worth setting the author\'s formulation beside one written some four centuries earlier. '
    '<strong>الإِمَامُ أَحْمَدُ بْنُ حَنْبَل</strong> ruled on this in '
    '<em>أُصُولُ السُّنَّة</em>, and he reaches for <strong>the same two words the matn '
    'uses</strong> — the heart, and its soundness:')
b += B.sharh(
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.96rem" dir="rtl" lang="ar"><strong>وَمَنِ انْتَقَصَ '
    'أَحَدًا مِنْ أَصْحَابِ رَسُولِ اللهِ ﷺ، أَوْ أَبْغَضَهُ بِحَدَثٍ كَانَ مِنْهُ، '
    'أَوْ ذَكَرَ مَسَاوِئَهُ — كَانَ مُبْتَدِعًا، حَتَّى يَتَرَحَّمَ عَلَيْهِمْ '
    'جَمِيعًا، وَيَكُونَ قَلْبُهُ لَهُمْ سَلِيمًا</strong></p>'
    '<p style="margin:.55rem 0 0;font-size:.9rem">— <em>and whoever disparages one of the '
    'Companions of the Messenger of Allah &#65018;, or hates him for something that occurred from '
    'him, or mentions his faults — <strong>he is an innovator, until he asks mercy for all '
    'of them and his heart is sound toward them.</strong></em></p>'
    '<p style="margin:.5rem 0 0;font-size:.85rem;color:var(--ink-light)">'
    'أُصُولُ السُّنَّ'
    'ة §٤٢</p></div>' +
    p('Three details reward a second look. <strong>First: %s — «his heart is sound toward '
      'them».</strong> That is the matn\'s own %s, in the words of an imām of the third century. '
      'The author did not coin the expression; he inherited it.'
      % (ar('وَيَكُونَ قَلْبُهُ لَهُمْ سَلِيمًا'), ar('سَلَامَةُ القُلُوب'))) +
    p('<strong>Second: %s — «for something that occurred from him».</strong> Imām Aḥmad is not '
      'ruling on someone who hates a Companion out of pure malice; he is ruling on the man who '
      'has <em>a reason</em> — some incident he has heard of. <strong>Having a grievance is '
      'precisely the case being addressed, and it is not accepted as an excuse.</strong>'
      % ar('أَوْ أَبْغَضَهُ بِحَدَثٍ كَانَ مِنْهُ')) +
    p('<strong>Third, the remedy is stated as a condition, not a punishment: %s — <em>until</em> '
      'he asks mercy for them all and his heart is sound.</strong> The door is left open, and the '
      'way back through it is the same duʿāʾ of al-Ḥashr 59:10 that this lesson began with — '
      'which is the whole argument closing on itself.' % ar('حَتَّى يَتَرَحَّمَ عَلَيْهِمْ جَمِيعًا')))

b += B.vocab([
    ('سَلَامَةُ القُلُوب', 'salāmat al-qulūb', 'soundness of the hearts',
     'From rancour, spite and hatred — named FIRST in the matn'),
    ('سَلَامَةُ الأَلْسِنَة', 'salāmat al-alsinah', 'soundness of the tongues',
     'From disparagement, cursing and reviling'),
    ('الغِلّ', 'al-ghill', 'rancour',
     'Glossed as deceit, hatred and envy'),
    ('الفَيْء', 'al-fayʾ', 'the fayʾ',
     'The context of al-Ḥashr 59:8–10 — and this description is the '
     'qualification for a share'),
    ('صَحَابِيّ', 'ṣaḥābī', 'a Companion',
     'Whoever met the Prophet ط believing in him and died upon that'),
    ('أُحُد', 'Uḥud', 'Mount Uḥud',
     'Named so because it stands alone, apart from the mountains'),
    ('المُدّ', 'al-mudd', 'a mudd',
     'A measure — a quarter of the Prophetic ṣāʿ'),
    ('نَصِيف', 'naṣīf', 'a half',
     'A variant form of النّصف'),
])
b += B.mcq('ws-l46', [
    ('What are the two soundnesses the matn requires, and why is the heart named first?',
     ['Of speech and of action; because speech precedes action',
      'Of the hearts (from rancour, spite and hatred) and of the tongues (from disparagement, '
      'cursing and reviling) — the heart first, because holding the tongue while the heart '
      'carries the grudge is not enough',
      'Of belief and of intention; because belief precedes intention',
      'Of the tongue and of the pen'], 1),
    ('Which of al-Fawzān’s reasons for their precedence bears most on creed?',
     ['Their numbers at Badr',
      'That they carried the Sharīʿah from him ﷺ and conveyed it to those after them — so to hold '
      'them unreliable is to hold that the religion did not arrive',
      'Their relationship to him by blood',
      'Their wealth spent in his cause'], 1),
    ('How does al-Ḥashr 59:10 contain both halves of the matn’s requirement?',
     ['By mentioning the Muhājirūn and the Anṣār',
      '"Our Lord, forgive us and our brothers" is the soundness of the tongues; "and put not in '
      'our hearts rancour" is the soundness of the hearts',
      'By naming faith and precedence',
      'By ending with "Kind, Merciful"'], 1),
    ('What does the āyah’s context add?',
     ['That it was revealed at Badr',
      'It concerns the distribution of the fayʾ — so this description is the qualification for a '
      'share of it',
      'That it abrogates an earlier ruling',
      'That it addresses the hypocrites'], 1),
    ('How does al-Shawkānī say a man arrives at rancour toward the Companions?',
     ['By reading the historical reports himself',
      'Not on his own — through being tried with a teacher from the Rāfiḍah, or a companion from '
      'the enemies of the best of the Ummah',
      'By excessive love of ʿAlī alone',
      'By ignorance of Arabic'], 1),
    ('Why does a Companion’s small spending outweigh a mountain of gold from anyone after them?',
     ['Because wealth was scarcer then',
      'Because of the īmān in their hearts at that time — Islam’s beginning, the fewness of '
      'its people, the abundance of what turned people away, and the weakness of the motives '
      'toward it',
      'Because they spent it directly to the Prophet ﷺ',
      'Because their wealth was lawful beyond doubt'], 1),
    ('What principle about deeds does the ḥadīth establish in passing?',
     ['That deeds are judged only by their outcome',
      'That a deed admits of degrees according to the intention of its doer AND according to the '
      'time in which it was discharged',
      'That spending is the best of deeds',
      'That deeds are equal before Allah'], 1),
    ('What does Imām Aḥmad make the condition for the one who disparaged a Companion?',
     ['That he be punished by the authority',
      'Until he asks mercy for all of them and his heart is sound toward them',
      'That he never be forgiven',
      'That he make public repentance'], 1),
])
b += B.tf('ws-l46-tf', [
    ('سَلَامَةُ اللِّسَانِ وَحْدَهَا تَكْفِي فِي حَقِّ الصَّحَابَةِ.',
     'Soundness of the tongue alone suffices regarding the Companions.', False),
    ('الصَّحَابَةُ يَدْخُلُونَ فِي ﴿لِلَّذِينَ آمَنُوا﴾ دُخُولًا أَوَّلِيًّا.',
     'The Companions enter into "those who believed" by the foremost entry.', True),
    ('العَمَلُ يَتَفَاضَلُ بِحَسَبِ الوَقْتِ الَّذِي أُدِّيَ فِيهِ.',
     'A deed admits of degrees according to the time in which it was discharged.', True),
    ('مَنْ أَبْغَضَ صَحَابِيًّا بِحَدَثٍ كَانَ مِنْهُ فَهُوَ مَعْذُورٌ.',
     'Whoever hates a Companion for something that occurred from him is excused.', False),
])
b += B.memorize(
    'وَلَا تَجْعَلْ فِي قُلُوبِنَا غِلًّا لِلَّذِينَ آمَنُوا',
    'The Qurʾān does not merely forbid the rancour — it teaches you the duʿāʾ against it, which '
    'is an admission that it can enter a heart uninvited. Imām Aḥmad makes the same duʿāʾ the way '
    'back: <em>until he asks mercy for all of them and his heart is sound toward them.</em>')
b += B.aiquiz('The obligation toward the Companions in al-Aqidah al-Wasitiyyah: the soundness of '
              'hearts and tongues and why the heart is named first, al-Fawzan four grounds '
              'including that they carried the Shariah and conveyed it, how al-Hashr 59:10 '
              'contains both halves of the requirement and its context in the distribution of the '
              'fay, al-Shawkani on how a man arrives at rancour through a teacher or companion, '
              'why a Companions mudd outweighs a mountain of gold given the four disincentives of '
              'that time, and Imam Ahmad in Usul al-Sunnah making soundness of heart the '
              'condition')
b += B.further()
b += B.nav('was-l45-haqiqat-al-iman.html', 'The Reality of Īmān',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l46')

io.open(os.path.join(B.AQ, 'was-l46-wajib-nahw-al-sahabah.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'الوَاجِبُ نَحْوَ أَصْحَابِ رَسُولِ اللهِ ﷺ',
    'The Obligation toward the Companions of the Messenger of Allah ﷺ',
    'Lesson 46 of al-ʿAqīdah al-Wāsiṭiyyah: the two soundnesses '
    'and how al-Ḥashr 59:10 contains both; al-Shawkānī on the route by which '
    'rancour reaches a heart and the duʿāʾ that removes it; why a Companion’s '
    'handful outweighs a mountain of gold; and Imām Aḥmad’s ruling in '
    'Uṣūl al-Sunnah, in the matn’s own words four centuries earlier.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ السَّادِسُ وَالأَرْبَعُون', '6',
           'الوَاجِبُ نَحْوَ أَصْحَابِ رَسُولِ اللهِ ﷺ',
           'The Obligation toward the Companions of the Messenger of Allah ﷺ', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l46-wajib-nahw-al-sahabah.html')
