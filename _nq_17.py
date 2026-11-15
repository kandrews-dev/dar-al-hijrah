# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 17 — النَّاقِضُ العَاشِر: الإِعْرَاض. The tenth and last.

Printed folios 228-235 (PDF indices 225-232, offset +3); index 233 opens the
capstone مَوَانِعُ تَكْفِيرِ المُعَيَّن, which fixes the end of the range.
Eight folios, one rich lesson — this closes the ten nullifiers.

The clause: «العَاشِر: الإِعْرَاضُ عَنْ دِينِ اللهِ تَعَالَى، لَا يَتَعَلَّمُهُ
وَلَا يَعْمَلُ بِه»، on al-Sajdah 32:22.

There is a quiet perfection in ending the book here, and the lesson is built
to let it land once, at the close: the tenth and final nullifier is turning
AWAY from learning the dīn — and the student who has reached it, and studied
it, has by that very act done the opposite of it. The antidote Ibn Bāz
prescribes — «الإِقْبَالُ عَلَى كِتَابِ اللهِ وَسُنَّةِ رَسُولِهِ» — is the act
of studying this matn.

Structure, following the sharḥ:
  1. The clause and its daleel (32:22).
  2. Ibn Bāz's reframe: the deficit today is not access to knowledge — that is
     easy — but ʿamal and will. The ḥadīth «مَنْ يُرِدِ اللهُ بِهِ خَيْرًا
     يُفَقِّهْهُ فِي الدِّين» as the sign; maḥrūm vs marḥūm.
  3. The scale of iʿrāḍ — partial (leaving before the sermon: «لَا يَكْفُرُ
     بِهِ المُعْرِض») vs total. The restraint that keeps the clause honest.
  4. Ibn al-Qayyim's definition of kufr al-iʿrāḍ, and his note that most
     mutakallimūn deny it is kufr in itself.
  5. Jins al-ʿamal — shahādah with belief but abandoning ALL deeds is not
     Islām; «العَمَلُ عِنْدَ الجَمِيعِ شَرْطُ صِحَّة»; al-Barrāk and Ibn
     Taymiyyah in the footnote.
  6. No excuse for iʿrāḍ — «لَا يُعْذَرُ أَحَدٌ بِالإِعْرَاض» — except ahl
     al-fatrah; and the diligent seeker who errs still has his reward.
  7. The seal: the direct address «يَا عَبْدَ اللهِ», and care for the Qurʾān
     as «أَصْلُ كُلِّ خَيْر».

Rule 8: «مَنْ يُرِدِ اللهُ بِهِ خَيْرًا يُفَقِّهْهُ فِي الدِّين» the sharḥ
itself grades «مُتَّفَقٌ عَلَيْه» and places «فِي الصَّحِيحَيْنِ عَنْ
مُعَاوِيَة», so the page names exactly that. The «فَأَعْرَضَ اللهُ عَنْه»
report the footnote grades «مُتَّفَقٌ عَلَيْه» with a reference, and adds the
compiler's own ruling that it is partial iʿrāḍ — both are carried.
"""
from _nq_15_lib import B, p, ar, box, row, row3, thead3, table, qa
from _nq_17_q import QS

b = B.objectives([
    'State the tenth nullifier in the matn’s words, and the verse it rests on.',
    'Give Ibn Bāz’s <strong>reframe</strong> — where the real deficiency lies '
    'today, and what «%s» he makes the sign of good being willed for a '
    'person.' % ar('الحَدِيث'),
    'Distinguish <strong>الإِعْرَاضُ الجُزْئِيّ</strong> from total iʿrāḍ, '
    'with the sharḥ’s own example of the kind that does <em>not</em> entail '
    'disbelief.',
    'Give Ibn al-Qayyim’s definition of <strong>كُفْرُ الإِعْرَاض</strong>, '
    'and his note on how most of the mutakallimūn treat it.',
    'Explain <strong>جِنْسُ العَمَل</strong> as «%s» — why the one who '
    'abandons all deeds is not a Muslim even if he believes.'
    % ar('شَرْطُ صِحَّة'),
    'State who is <strong>not</strong> excused by iʿrāḍ, the one exception, '
    'and the standing of the diligent seeker who errs.',
    'Give the seal of the whole matn — the direct address «%s» — and why it '
    'is fitting that this is the last nullifier.' % ar('يَا عَبْدَ الله'),
])

b += B.provenance(228, 235)

b += B.matn(
    'العَاشِر: الإِعْرَاضُ عَنْ دِينِ اللهِ تَعَالَى، لَا يَتَعَلَّمُهُ '
    'وَلَا يَعْمَلُ بِه؛ وَالدَّلِيلُ قَوْلُهُ تَعَالَى: ﴿وَمَنْ أَظْلَمُ '
    'مِمَّنْ ذُكِّرَ بِآيَاتِ رَبِّهِ ثُمَّ أَعْرَضَ عَنْهَا إِنَّا مِنَ '
    'المُجْرِمِينَ مُنْتَقِمُونَ﴾.',
    'The clause names two things together — «لَا يَتَعَلَّمُهُ وَلَا يَعْمَلُ '
    'بِه», neither learns it nor acts on it — and its daleel is a '
    'rhetorical question: who does greater wrong than a man <em>reminded</em> '
    'of his Lord’s signs who then turns from them?')
b += B.ayah(
    'وَمَنْ أَظْلَمُ مِمَّن ذُكِّرَ بِآيَاتِ رَبِّهِ ثُمَّ أَعْرَضَ عَنْهَا '
    'إِنَّا مِنَ الْمُجْرِمِينَ مُنتَقِمُونَ',
    'And who does greater wrong than one reminded of the signs of his Lord, '
    'then turns away from them? Indeed, We will take retribution from the '
    'criminals.',
    'سُورَةُ السَّجْدَة · 32:22')
b += B.sharh(
    box('<p style="margin:0;font-size:.95rem"><strong>Read the daleel '
        'closely, because the whole clause is in it.</strong> The one '
        'condemned is not someone who never heard — he is «مَنْ ذُكِّرَ», '
        '<em>one who was reminded</em>. The sin is not absence of the '
        'message; it is <strong>presence of the message and a turning of the '
        'back</strong>.</p>',
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('<em>That is why this nullifier can stand beside shirk and '
      'istihzāʾ in a book of the gravest matters.</em> A man may utter no '
      'word of disbelief and deny nothing — he simply will not turn toward '
      'the religion to learn it or live it. «الإِعْرَاضُ عَنْ دِينِ اللهِ، '
      'لَا يَعْلَمُهُ وَلَا يَتَعَلَّمُهُ وَلَا يَعْمَلُ بِه — هَذَا مِنْ '
      'نَوَاقِضِ الإِسْلَام.»'))

# ----------------------------------------------- the reframe
b += B.heading('أَيْنَ النَّقْصُ اليَوْم؟', 'Where the Deficiency Really Lies')
b += B.prose(
    '<strong>Here Ibn Bāz turns the clause on his own age, and the turn is '
    'bracing.</strong> A person might expect the excuse of our time to be '
    'that knowledge is hard to reach. He says the opposite.')
b += B.sharh(
    p('<em>«النَّقْصُ اليَوْمَ أَشَدُّهُ وَأَعْظَمُهُ <strong>فِي '
      'العَمَل</strong>؛ أَمَّا العِلْمُ فَمُتَيَسِّر؛ يَسْتَطِيعُ طَالِبُ '
      'العِلْمِ أَنْ يُرَاجِعَ كَلَامَ اللهِ وَرَسُولِهِ وَكَلَامَ أَهْلِ '
      'العِلْم، وَيَسْتَطِيعُ العَامِّيُّ أَنْ يَسْأَلَ إِذَا رَغِبَ فِي '
      'الخَيْر... اليَوْمَ تَسَهَّلَ كُلُّ شَيْء.»</em>') +
    p('<strong>So the excuse is removed before it is offered.</strong> '
      '<em>The books are open, the scholars are reachable, the journey that '
      'once took months takes hours. What is left, when access is no longer '
      'the barrier, is the will — and that is exactly where he locates the '
      'disease:</em> «إِنَّمَا المُصِيبَةُ <strong>ضَعْفُ الطَّالِبِ '
      'وَقِلَّةُ نَشَاطِهِ وَإِعْرَاضُهُ وَغَفْلَتُه</strong>؛ هَذِهِ هِيَ '
      'المُصِيبَةُ العُظْمَى.»'))
b += B.hadith(
    'مَنْ يُرِدِ اللهُ بِهِ خَيْرًا يُفَقِّهْهُ فِي الدِّين',
    'Whoever Allah wants good for, He gives him understanding of the religion.',
    'مُتَّفَقٌ عَلَيْهِ — فِي الصَّحِيحَيْنِ عَنْ مُعَاوِيَةَ ؓ؛ '
    'the sharḥ names it «الحَدِيث الصَّحِيح» and «مُتَّفَقٌ عَلَى صِحَّتِه», '
    'so the grading here is its own.')
b += B.sharh(
    p('<strong>He reads the ḥadīth as a diagnosis, not a consolation.</strong> '
      '<em>«هَذَا دَلِيلٌ عَلَى أَنَّ مَنْ أَرَادَ اللهُ بِهِ خَيْرًا '
      'تَفَقَّهَ وَتَعَلَّمَ وَتَبَصَّرَ حَتَّى يَعْمَل، وَمَنْ لَمْ يُرِدِ '
      'اللهُ بِهِ خَيْرًا أَعْرَضَ وَغَفَل.»</em> So turning toward knowledge '
      'is itself a sign of mercy, and turning away a sign withheld — '
      '«فَالنَّاسُ مَا بَيْنَ <strong>مَحْرُومٍ وَمَرْحُوم</strong>».') +
    p('<em>And the greatest of all the means to this fiqh, he says, is not a '
      'shaykh or a matn but the Qurʾān itself:</em> «أَعْظَمُ ذَلِكَ '
      'العِنَايَةُ بِالقُرْآن؛ هُوَ أَصْلُ كُلِّ خَيْر... <strong>أَصْلُ '
      'العِلْمِ وَيَنْبُوعُه</strong>.»'))

# ----------------------------------------------- the scale
b += B.heading('إِعْرَاضٌ جُزْئِيٌّ وَإِعْرَاضٌ كُلِّيّ', 'Partial Turning-Away, and Total')
b += B.prose(
    '<strong>This is the restraint that keeps the clause from swallowing '
    'ordinary sinners, and it is the same discipline the whole book has '
    'shown.</strong> Not every turning-away is the nullifier. The sharḥ gives '
    'a small, concrete example of the kind that is <em>not</em> — and names it '
    'as such.')
b += B.sharh(
    p('<em>Ibn Bāz: the worshippers «لَا يَخْرُجُوا مِنَ المَسْجِدِ إِذَا '
      'وَعَظَ الوَاعِظ», and it is feared of one who leaves without '
      'necessity before hearing the admonition that he be of those the '
      'Prophet ﷺ said «(فَأَعْرَضَ اللهُ عَنْه)».</em>') +
    box('<p style="margin:0;font-size:.93rem"><strong>And the compiler, in the '
        'footnote, draws the exact line:</strong> that report is «مُتَّفَقٌ '
        'عَلَيْه» — <em>«وَهَذَا مِنَ <strong>الإِعْرَاضِ الجُزْئِيّ</strong> '
        'الَّذِي <strong>لَا يَكْفُرُ بِهِ المُعْرِض</strong>»</em>. A man who '
        'turns from <em>one</em> gathering of good has not left the '
        'religion.</p>') +
    p('<strong>So the nullifier is the total turning, not the partial '
      'lapse.</strong> <em>Hold this beside every clause before it: the book '
      'that is most often misquoted toward takfīr is, folio after folio, the '
      'book that keeps drawing the line short of it.</em>'))
b += B.heading('حَدُّ كُفْرِ الإِعْرَاض', 'What Kufr al-Iʿrāḍ Actually Is')
b += B.sharh(
    p('<strong>Ibn al-Qayyim’s definition, which the footnote carries from '
      '<em>Madārij al-Sālikīn</em> and <em>Miftāḥ Dār al-Saʿādah</em>, is the '
      'measure of the total kind:</strong>') +
    box('<p style="margin:0;font-size:.95rem"><span dir="rtl" lang="ar">'
        '«وَأَمَّا كُفْرُ الإِعْرَاضِ فَأَنْ يُعْرِضَ <strong>بِسَمْعِهِ '
        'وَقَلْبِهِ</strong> عَنِ الرَّسُول: لَا يُصَدِّقُهُ وَلَا '
        'يُكَذِّبُه، وَلَا يُحِبُّهُ وَلَا يُبْغِضُه، وَلَا يُوَالِيهِ وَلَا '
        'يُعَادِيه، <strong>وَلَا يُصْغِي إِلَى مَا جَاءَ بِهِ '
        'البَتَّة</strong>.»</span></p>') +
    p('<strong>Notice how complete the turning has to be.</strong> <em>Not a '
      'denial — he does not deny. Not a mockery — he does not mock. He simply '
      'closes ear and heart to the Messenger ﷺ altogether and will not so '
      'much as lean toward what he brought. That whole-person shutting-out is '
      'the kufr; a man who still argues, or sins, or asks, is not yet '
      'here.</em>') +
    p('<em>And Ibn al-Qayyim adds a precision the footnote keeps:</em> that '
      'most of the mutakallimūn «يُنْكِرُونَ كُفْرَ الإِعْرَاض» as a category '
      'in itself, and make it kufr only «لِدَلَالَتِهِ عَلَى كُفْرِ '
      'الجَهْل، لَا لِكَوْنِهِ كُفْرًا لِذَاتِه» — kufr for what it points to, '
      'not for what it is. <strong>The disagreement is named, not '
      'hidden.</strong>'))

# ----------------------------------------------- jins al-ʿamal
b += B.heading('جِنْسُ العَمَلِ شَرْطُ صِحَّة', 'The Genus of Action Is a Condition of Validity')
b += B.prose(
    '<strong>Underneath the clause sits a question of ʿaqīdah the sharḥ does '
    'not dodge: can faith be real with no deeds at all?</strong>')
b += B.sharh(
    qa('مَنْ شَهِدَ أَنْ لَا إِلَهَ إِلَّا اللهُ وَاعْتَقَدَ بِقَلْبِهِ، '
       'وَلَكِنْ تَرَكَ جَمِيعَ الأَعْمَال — هَلْ يَكُونُ مُسْلِمًا؟',
       '«<strong>لَا يَكُونُ مُسْلِمًا</strong>، حَتَّى يُوَحِّدَ اللهَ '
       'بِعَمَلِه... وَلَا يُتَصَوَّرُ إِنْسَانٌ مُسْلِمٌ يُؤْمِنُ بِاللهِ '
       'وَيَتْرُكُ جَمِيعَ الأَعْمَال؛ هَذَا تَقْدِيرٌ لَا أَسَاسَ لَه؛ '
       '<strong>لِأَنَّ الإِيمَانَ الصَّادِقَ يَحْفِزُهُ إِلَى '
       'العَمَل</strong>.»') +
    qa('مَنْ لَمْ يُكَفِّرْ تَارِكَ الصَّلَاةِ مِنَ السَّلَف — أَيَكُونُ '
       'العَمَلُ عِنْدَهُ شَرْطَ كَمَالٍ أَوْ شَرْطَ صِحَّة؟',
       '«لَا، بَلِ <strong>العَمَلُ عِنْدَ الجَمِيعِ شَرْطُ صِحَّة</strong>؛ '
       'إِلَّا أَنَّهُمُ اخْتَلَفُوا فِيمَا يَصِحُّ الإِيمَانُ بِه... '
       '<strong>إِلَّا أَنَّ جِنْسَ العَمَلِ لَا بُدَّ مِنْهُ لِصِحَّةِ '
       'الإِيمَانِ عِنْدَ السَّلَفِ جَمِيعًا</strong>؛ فَالإِيمَانُ '
       'عِنْدَهُم: قَوْلٌ وَعَمَلٌ وَاعْتِقَاد، لَا يَصِحُّ إِلَّا بِهَا '
       'مُجْتَمِعَة.»') +
    p('<strong>Read what he has and has not said, because it is precise.</strong> '
      '<em>The scholars differed over the <em>particular</em> deed whose '
      'absence breaks faith — some named the prayer, by the ijmāʿ of the '
      'Companions reported by ʿAbdullāh ibn Shaqīq; others named otherwise. '
      'But on</em> جِنْسُ العَمَل <em>— the genus of action, that there be '
      '</em>some<em> acting at all — there is no disagreement among the '
      'salaf.</em> <strong>Faith with literally no deed is not a weak faith; '
      'it is not faith.</strong>'))
b += B.sharh(
    p('<em>And al-Barrāk’s footnote turns that into the practical test, which '
      'is the answer to «how is iʿrāḍ escaped?»:</em> «يَتَحَقَّقُ '
      'عَدَمُ هَذَا الإِعْرَاضِ بِفِعْلِ شَيْءٍ مِنَ الوَاجِبَاتِ '
      '<strong>الَّتِي تَخْتَصُّ بِهَا شَرِيعَةُ الإِسْلَام</strong> — '
      'كَالصَّلَاةِ وَالزَّكَاةِ وَالصِّيَامِ وَالحَجّ — إِذَا فَعَلَ '
      'شَيْئًا مِنْ ذَلِكَ إِيمَانًا وَاحْتِسَابًا.» <em>Ibn Taymiyyah, in '
      'the same place:</em> «فَلَا يَكُونُ الرَّجُلُ مُؤْمِنًا بِاللهِ '
      'وَرَسُولِهِ مَعَ عَدَمِ فِعْلِ شَيْءٍ مِنَ الوَاجِبَاتِ الَّتِي '
      'يَخْتَصُّ بِإِيجَابِهَا مُحَمَّدٌ ﷺ.»'))

# ----------------------------------------------- no excuse
b += B.heading('لَا يُعْذَرُ أَحَدٌ بِالإِعْرَاض', 'No One Is Excused by Turning Away')
b += B.sharh(
    box('<p style="margin:0;font-size:.95rem"><span dir="rtl" lang="ar">'
        '«أَمَّا الإِعْرَاض: <strong>فَلَا يُعْذَرُ أَحَدٌ بِالإِعْرَاضِ '
        'وَالغَفْلَة</strong>... لَا بُدَّ مِنْ طَلَبِ العِلْم، لَا بُدَّ '
        'مِنَ التَّفَقُّهِ وَالسُّؤَالِ وَالعِنَايَة — <strong>إِلَّا أَهْلَ '
        'الفَتْرَةِ</strong> الَّذِينَ مَا جَاءَهُمْ رَسُولٌ وَلَا جَاءَهُمْ '
        'كِتَاب.»</span></p>',
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('<em>The one exception is the one the texts already name: those whom no '
      'messenger and no book reached. «أَمْرُهُمْ إِلَى اللهِ يَوْمَ '
      'القِيَامَة؛ يُمْتَحَنُونَ يَوْمَ القِيَامَة؛ فَمَنْ أَطَاعَ... نَجَا، '
      'وَمَنْ أَبَى صَارَ إِلَى النَّار.» But the one the Messenger ﷺ and the '
      'Book reached — «فَلَا يُعْذَر؛ يَتَعَلَّمُ وَيَتَفَقَّه».</em>') +
    p('<strong>And here the clause protects the honest student by name.</strong> '
      '<em>«فَإِذَا خَفِيَتْ عَلَيْهِ بَعْضُ الأُمُورِ لِخَفَائِهَا وَهُوَ '
      '<strong>مُجْتَهِدٌ حَرِيص، طَالِبُ عِلْمٍ يَسْأَلُ أَهْلَ العِلْم</strong> '
      '— فَهَذَا لَهُ أَجْرَانِ إِنْ أَصَاب، وَلَهُ أَجْرٌ إِنْ أَخْطَأ.» The '
      'turning-away that condemns is a refusal, not a gap in a seeker’s '
      'knowledge:</em> «أَمَّا أَنْ يُعْرِضَ وَيَغْفُلَ وَيُتَابِعَ الهَوَى '
      'وَيَقُول: أَنَا مَعْذُورٌ جَاهِل — لَا، لَا يُعْذَر.»'))
b += B.prose(
    '<strong>And the footnote closes the door with one line of reasoning:</strong> '
    '«%s» — <em>if the one who turns away were excused by his turning away, '
    'the disbelievers would be excused in their disbelief.</em> The excuse of '
    '«I did not know» cannot be granted to the man who <em>chose</em> not to '
    'know.' % ar('فَلَوْ كَانَ المُعْرِضُ مَعْذُورًا لَعُذِرَ الكَفَرَةُ فِي '
                 'كُفْرِهِم'))
b += B.ayah(
    'وَالَّذِينَ كَفَرُوا عَمَّا أُنذِرُوا مُعْرِضُونَ',
    'And those who disbelieve are turning away from that of which they are '
    'warned.',
    'سُورَةُ الأَحْقَاف · 46:3')
b += B.ayah(
    'وَمَنْ أَظْلَمُ مِمَّن ذُكِّرَ بِآيَاتِ رَبِّهِ فَأَعْرَضَ عَنْهَا '
    'وَنَسِيَ مَا قَدَّمَتْ يَدَاهُ',
    'And who does greater wrong than one reminded of the signs of his Lord, '
    'then turns away from them and forgets what his hands have sent forth?',
    'سُورَةُ الكَهْف · 18:57')
b += B.ayah(
    'وَمَن يَعْشُ عَن ذِكْرِ الرَّحْمَٰنِ نُقَيِّضْ لَهُ شَيْطَانًا فَهُوَ '
    'لَهُ قَرِينٌ',
    'And whoever turns blind to the remembrance of the Most Merciful — We '
    'appoint for him a devil, and he is to him a companion.',
    'سُورَةُ الزُّخْرُف · 43:36')
b += B.ayah(
    'وَمَن يُعْرِضْ عَن ذِكْرِ رَبِّهِ يَسْلُكْهُ عَذَابًا صَعَدًا',
    'And whoever turns away from the remembrance of his Lord — He will drive '
    'him into a mounting punishment.',
    'سُورَةُ الجِنّ · 72:17')
b += B.ayah(
    'وَلَا تَكُونُوا كَالَّذِينَ نَسُوا اللَّهَ فَأَنسَاهُمْ أَنفُسَهُمْ '
    'أُولَٰئِكَ هُمُ الْفَاسِقُونَ',
    'And do not be like those who forgot Allah, so He made them forget '
    'themselves. Those are the defiantly disobedient.',
    'سُورَةُ الحَشْر · 59:19')
b += B.sharh(
    p('<em>He reads 59:19 as the inner mechanism of the whole clause:</em> '
      '«نَسُوا اللهَ <strong>بِإِعْرَاضِهِمْ وَغَفْلَتِهِم</strong> '
      'وَعَدَمِ قِيَامِهِمْ بِالحَقّ، فَأَنْسَاهُمُ اللهُ أَنْفُسَهُم — '
      '<strong>أَنْسَاهُمْ أَسْبَابَ نَجَاتِهَا وَسَعَادَتِهَا</strong> '
      'حَتَّى صَارَتْ أَعْمَالُهُمْ كُلُّهَا فِي سَبَبِ هَلَاكِهِمْ. '
      'فَالجَزَاءُ مِنْ جِنْسِ العَمَل.»'))

# ----------------------------------------------- the seal
b += B.heading('خِتَامُ النَّوَاقِض', 'The Seal of the Nullifiers')
b += B.prose(
    '<strong>Ibn Bāz ends not on a verdict but on an address — he turns from '
    'describing the turning-away to calling his reader out of it, by '
    'name.</strong>')
b += B.sharh(
    box('<p style="margin:0;font-size:1rem"><span dir="rtl" lang="ar">'
        '«فَيَنْبَغِي لَكَ <strong>يَا عَبْدَ اللهِ</strong> الانْتِبَاهُ '
        'لِهَذَا الأَمْر، وَالإِقْبَالُ عَلَى كِتَابِ اللهِ وَسُنَّةِ '
        'رَسُولِهِ ﷺ دِرَاسَةً وَتَدَبُّرًا وَتَعَقُّلًا؛ <strong>حَتَّى '
        'تَعْرِفَ تَوْحِيدَ اللهِ وَالإِيمَانَ بِه، وَحَتَّى تَعْرِفَ مَا '
        'هُوَ الشِّرْكُ بِالله، وَحَتَّى تَكُونَ بَصِيرًا '
        'بِدِينِك</strong>.»</span></p>',
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('<em>And a warning that credentials are not fiqh:</em> «رُبَّمَا '
      'حَمَلَ <strong>الدُّكْتُورَاه</strong> جَاهِل، وَحَمَلَ الشَّهَادَةَ '
      'الابْتِدَائِيَّةَ مَنْ هُوَ أَعْلَمُ وَأَكْمَلُ شَأْنًا فِي دِينِ '
      'الله» — a man may carry a doctorate and be «أَجْهَلَ مِنْ أَبْنَاءِ '
      'المَدَارِسِ الابْتِدَائِيَّةِ فِي أَمْرِ دِينِه، وَهَذِهِ '
      'مُصِيبَة». And the summons: «فَجَدِيرٌ بِأَهْلِ الإِسْلَامِ ذُكُورًا '
      'وَإِنَاثًا أَنْ يَعْنُوا بِالعِلْمِ <strong>قَبْلَ '
      'قَبْضِه</strong>.»'))
b += B.prose(
    '<strong>There is a quiet fitness in ending the ten nullifiers '
    'here.</strong> The first was shirk — the gravest thing a heart can do. '
    'The last is <em>iʿrāḍ</em> — the simplest: not to turn toward the '
    'religion at all. And its cure, in Ibn Bāz’s own closing words, is «%s» — '
    '<em>turning to the Book of Allah and the Sunnah of His Messenger ﷺ, '
    'studying, pondering, until you know tawḥīd and know what shirk is.</em> '
    '<strong>Which is to say: the student who has reached this final clause, '
    'and sat with it, and understood it, has — by that very act — already done '
    'the opposite of the nullifier it describes.</strong> <em>You came toward '
    'the dīn to learn it. That is the whole answer to the tenth.</em>'
    % ar('الإِقْبَالُ عَلَى كِتَابِ اللهِ وَسُنَّةِ رَسُولِه'))

# ----------------------------------------------- vocab, quiz, memorize
b += B.vocab([
    ('الإِعْرَاض', 'al-iʿrāḍ', 'turning away',
     'The tenth nullifier: turning from the dīn, «لَا يَتَعَلَّمُهُ وَلَا '
     'يَعْمَلُ بِه». The sin of the back turned, not the tongue.'),
    ('كُفْرُ الإِعْرَاض', 'kufr al-iʿrāḍ', 'the disbelief of turning away',
     'Ibn al-Qayyim: closing ear and heart to the Messenger ﷺ entirely, «لَا '
     'يُصْغِي إِلَى مَا جَاءَ بِهِ البَتَّة». The total kind.'),
    ('الإِعْرَاضُ الجُزْئِيّ', 'al-iʿrāḍ al-juzʾī', 'partial turning-away',
     'Leaving before the sermon and the like — «لَا يَكْفُرُ بِهِ '
     'المُعْرِض». The clause’s own restraint against over-reach.'),
    ('جِنْسُ العَمَل', 'jins al-ʿamal', 'the genus of action',
     'That there be <em>some</em> acting at all. «شَرْطُ صِحَّة» for faith by '
     'the consensus of the salaf — īmān is qawl, ʿamal and iʿtiqād.'),
    ('شَرْطُ صِحَّة', 'sharṭ ṣiḥḥah', 'condition of validity',
     'Against «شَرْطُ كَمَال» (condition of perfection). Deeds, in their '
     'genus, are the first, not the second — faith is not valid without '
     'them.'),
    ('أَهْلُ الفَتْرَة', 'ahl al-fatrah', 'those a message never reached',
     'The one exception to «لَا يُعْذَرُ أَحَدٌ بِالإِعْرَاض». Their affair '
     'is to Allah; they are tested on the Day of Resurrection.'),
    ('الغَفْلَة', 'al-ghaflah', 'heedlessness',
     'Paired with iʿrāḍ throughout. «لَا يُعْذَرُ أَحَدٌ بِالإِعْرَاضِ '
     'وَالغَفْلَة».'),
    ('البَصِيرَة', 'al-baṣīrah', 'clear-sighted insight',
     'The goal of the seal: «حَتَّى تَكُونَ بَصِيرًا بِدِينِك» — not mere '
     'information, but seeing your religion clearly.'),
    ('مَحْرُومٌ وَمَرْحُوم', 'maḥrūm wa-marḥūm', 'deprived and shown-mercy',
     'The footnote’s two kinds of people: the one turned from fiqh, and the '
     'one granted it — «مَنْ يُرِدِ اللهُ بِهِ خَيْرًا يُفَقِّهْهُ فِي '
     'الدِّين».'),
])

b += B.mcq('nq-l17-mcq', QS)

b += B.tf('nq-l17-tf', [
    ('الإِعْرَاضُ عَنْ دِينِ اللهِ — لَا يَتَعَلَّمُهُ وَلَا يَعْمَلُ بِهِ — '
     'مِنْ نَوَاقِضِ الإِسْلَام.',
     'Turning away from the religion of Allah — neither learning nor acting '
     'on it — is of the nullifiers of Islām.', True),
    ('قَالَ ابْنُ بَاز: النَّقْصُ اليَوْمَ أَشَدُّهُ فِي العِلْمِ لَا فِي '
     'العَمَل.',
     'Ibn Bāz said the deficiency today is worst in knowledge, not in '
     'action.', False),
    ('الخُرُوجُ مِنَ المَسْجِدِ قَبْلَ المَوْعِظَةِ كُفْرٌ يُخْرِجُ مِنَ '
     'المِلَّة.',
     'Leaving the masjid before the sermon is a disbelief that exits the '
     'religion.', False),
    ('جِنْسُ العَمَلِ شَرْطُ صِحَّةٍ لِلْإِيمَانِ عِنْدَ السَّلَفِ جَمِيعًا.',
     'The genus of action is a condition of the validity of faith by the '
     'consensus of the salaf.', True),
    ('يُعْذَرُ بِالإِعْرَاضِ مَنْ قَال: أَنَا جَاهِلٌ مَعْذُور.',
     'The one who says “I am an excused ignorant one” is excused by his '
     'turning away.', False),
    ('أَهْلُ الفَتْرَةِ — الَّذِينَ لَمْ يَأْتِهِمْ رَسُولٌ وَلَا كِتَابٌ — '
     'أَمْرُهُمْ إِلَى اللهِ يُمْتَحَنُونَ يَوْمَ القِيَامَة.',
     'Ahl al-fatrah — whom no messenger and no book reached — their affair is '
     'to Allah, tested on the Day of Resurrection.', True),
    ('طَالِبُ العِلْمِ المُجْتَهِدُ إِذَا خَفِيَ عَلَيْهِ أَمْرٌ فَأَخْطَأَ '
     'فَلَهُ أَجْر.',
     'The diligent seeker of knowledge, if a matter is hidden from him and he '
     'errs, still has a reward.', True),
])

b += B.memorize(
    'فَيَنْبَغِي لَكَ يَا عَبْدَ اللهِ الانْتِبَاهُ لِهَذَا الأَمْر، '
    'وَالإِقْبَالُ عَلَى كِتَابِ اللهِ وَسُنَّةِ رَسُولِهِ ﷺ دِرَاسَةً '
    'وَتَدَبُّرًا؛ حَتَّى تَكُونَ بَصِيرًا بِدِينِك',
    'Ibn Bāz, in the closing words of the tenth and final nullifier. '
    '<strong>This is the seal of the whole book — and it is an address, not a '
    'verdict.</strong> <em>The last of the ten ways a person leaves Islām is '
    'simply not to turn toward it; and the cure Ibn Bāz names is to turn '
    'toward the Book and the Sunnah, studying and pondering, until you are '
    '</em>baṣīr<em> in your religion.</em> <strong>So the student who has '
    'reached this clause has, by reaching it, already begun doing the opposite '
    'of it.</strong> <em>You came to learn. «مَنْ يُرِدِ اللهُ بِهِ خَيْرًا '
    'يُفَقِّهْهُ فِي الدِّين» — and that turning-toward is itself the sign of '
    'the good that was willed for you.</em>')

b += B.nav('nq-l16-al-khuruj-an-al-shariah.html',
           'النَّاقِضُ التَّاسِع',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l17')

B.write('nq-l17-al-irad-an-al-din.html',
        'النَّاقِضُ العَاشِر · الإِعْرَاض',
        'The Tenth Nullifier — Turning Away from the Religion',
        'The tenth and final nullifier, from the words of Shaykh Ibn Bāz: '
        'turning away from the religion of Allah, neither learning it nor '
        'acting on it, on al-Sajdah 32:22; his reframe that the deficiency '
        'today lies in action and will, not in access to knowledge, with the '
        'ḥadīth «whoever Allah wills good for, He gives fiqh in the religion»; '
        'the distinction between partial iʿrāḍ, which does not entail '
        'disbelief, and the total kufr al-iʿrāḍ defined by Ibn al-Qayyim; that '
        'the genus of action is a condition of the validity of faith by the '
        'consensus of the salaf; that no one is excused by turning away save '
        'ahl al-fatrah, while the diligent seeker who errs is rewarded; and '
        'the seal of the matn — the direct address «yā ʿabd Allāh» to turn to '
        'the Book and the Sunnah until one is baṣīr in his religion.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ السَّابِعَ عَشَر', '6', b)
print('wrote nq-l17-al-irad-an-al-din.html')
