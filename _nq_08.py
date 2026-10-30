# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 8 — النَّاقِضُ الخَامِس: بُغْضُ شَيْءٍ مِمَّا جَاءَ بِهِ ﷺ.

Printed folios 136-145 (PDF indices 133-142, offset +3). Nullifier 6 begins at
index 143 → printed 146.

The clause is short and the sharḥ is long, because the whole weight of it sits
on **one distinction** that the matn makes in four words: «وَلَوْ عَمِلَ بِهِ».

  * The footnote takes those four words as the key: the بُغْض meant here is
    بُغْضُ التَّشْرِيع, not بُغْضُ العَمَل. Hence **two kinds**:
      - النَّوْعُ الأَوَّل: بُغْضٌ مُكَفِّر — hating that Allah legislated a
        thing, or that He sent Muḥammad ﷺ. Ibn Taymiyyah relays the ijmāʿ.
      - النَّوْعُ الثَّانِي: بُغْضٌ طَبِيعِيّ — the co-wife pleased with the
        Sharīʿah and pained by the decree; cold water for wuḍūʾ; the hardship
        of fighting. «فَهَذَا لَيْسَ مِنَ الكُفْرِ فِي شَيْء.»
  * Ibn Bāz applies the matn's four words directly: «مَنْ كَرِهَ الصَّلَاةَ —
    وَلَوْ صَلَّى — أَوْ كَرِهَ الحَجَّ — وَلَوْ حَجَّ — ... كَفَرَ.»
  * He also distinguishes كَرَاهَةٌ طَبِيعِيَّة from إِكْرَاه, and defines the
    latter.
  * Then eight masāʾil in his own words, and the spread across them is the
    lesson: the beard (كَفَر), the Ṣaḥābah (kufr in general, **fisq** for
    rancour toward some), polygyny (مُرْتَدّ), Waḥshī (غَلَط, تَوْبَة, not
    kufr), the Jumuʿah recitation (**«إِمَّا جَاهِلٌ وَإِمَّا ضَعِيفُ
    الإِيمَان»** — explicitly not kufr), songs as a cause that grows type 1 out
    of type 2, and the cure: «إِذَا رَوَّضَ نَفْسَهُ وَجَاهَدَهَا صَارَتْ
    هَذِهِ الأَعْمَالُ نَعِيمًا يَجِدُهُ فِي قَلْبِه».
  * And the compiler's long refutation of «تَسْهِيلُ العَقِيدَةِ
    الإِسْلَامِيَّة», which held that only hating **all** of the religion is
    kufr. Six arguments, each one answered. It is the best single piece of
    reasoning in the book so far and the page gives it properly — including the
    Ḥudaybiyah objection, «أَسْلِمْ وَإِنْ كُنْتَ كَارِهًا», and Thaqīf's
    conditions.
  * The close is the compiler's own, and it is two-sided: beware lest baghḍ of
    the religion enter the heart — and it is on the scholar to carry people on
    المَعْهُودُ الوَسَط, because **«طَرَفُ التَّشَدُّدِ مُهْلِكَةٌ تُبَغِّضُ
    لِلْعَامَّةِ الدِّين»**. A clause about hating the religion ends by naming
    harshness as something that *teaches* people to hate it.

Rule 8: «أَسْلِمْ وَإِنْ كُنْتَ كَارِهًا» — the compiler grades the isnād
صَحِيح and names al-Dhahabī's صَحِيحٌ غَرِيب. Thaqīf's ḥadīth — Abū Dāwūd,
إِسْنَادٌ حَسَن, his grading. «وَإِسْبَاغُ الوُضُوءِ» — صَحِيحُ مُسْلِم.
«لَا تَلْعَنْهُ» — البُخَارِيّ. But «حُفَّتِ الجَنَّةُ بِالمَكَارِه» and
«بَايَعْنَا... فِي المَنْشَطِ وَالمَكْرَه» are quoted with **no** grading at
this place, so the page says so and supplies none.
"""
import io, os, importlib.util

spec = importlib.util.spec_from_file_location('nq', os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '_nqbuild.py'))
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


def box(inner, wash='var(--brand-wash)', edge='var(--brand)'):
    return ('<div style="background:%s;border-right:4px solid %s;'
            'border-radius:var(--radius-sm);padding:var(--space-md);'
            'margin:0 0 .8rem">%s</div>' % (wash, edge, inner))


def row(k, v):
    return ('<tr><td style="padding:.62rem .8rem;border:1px solid var(--line);'
            'white-space:nowrap;vertical-align:top"><strong>%s</strong></td>'
            '<td style="padding:.62rem .8rem;border:1px solid var(--line)">%s</td></tr>'
            % (k, v))


def row3(a, b_, c):
    return ('<tr><td style="padding:.62rem .8rem;border:1px solid var(--line);'
            'vertical-align:top">%s</td>'
            '<td style="padding:.62rem .8rem;border:1px solid var(--line);'
            'vertical-align:top">%s</td>'
            '<td style="padding:.62rem .8rem;border:1px solid var(--line);'
            'vertical-align:top">%s</td></tr>' % (a, b_, c))


def thead3(a, b_, c):
    cell = ('<th style="padding:.5rem .8rem;border:1px solid var(--line);'
            'text-align:left;font-size:.76rem;letter-spacing:.05em;'
            'text-transform:uppercase;color:var(--ink-light)">%s</th>')
    return '<tr>' + (cell % a) + (cell % b_) + (cell % c) + '</tr>'


def table(rows, fs='.91rem'):
    return ('<div style="overflow-x:auto"><table style="width:100%%;'
            'border-collapse:collapse;font-size:%s;margin:0 0 .75rem">%s</table></div>'
            % (fs, ''.join(rows)))


def obj(claim, answer):
    return ('<div style="margin:0 0 .85rem;padding:.7rem .85rem;'
            'border:1px solid var(--line);border-radius:var(--radius-sm)">'
            '<p style="margin:0 0 .4rem;font-size:.9rem;color:var(--ink-light)">'
            '<strong>The objection —</strong> <em>%s</em></p>'
            '<p style="margin:0;font-size:.93rem"><strong>The answer —</strong> '
            '%s</p></div>' % (claim, answer))


b = B.objectives([
    'Quote the fifth nullifier and say what the four words %s do to it.'
    % ('«' + ar('وَلَوْ عَمِلَ بِهِ') + '»'),
    'Name the <strong>two kinds</strong> of %s, give two examples of each, and '
    'state the ruling on each.' % ar('بُغْض'),
    'Give Ibn Bāz’s own application of the matn’s condition — the one about '
    'prayer and ḥajj.',
    'Distinguish %s from %s, and define the second.'
    % (ar('كَرَاهَةٌ طَبِيعِيَّة'), ar('إِكْرَاه')),
    'State the ruling on reviling the Ṣaḥābah <em>in general</em> and the '
    'ruling on rancour toward <em>some</em> of them — and why they differ.',
    'Refute the claim that only hating <strong>all</strong> of the religion is '
    'disbelief, from the wording of the verse and by reductio.',
    'Explain the Ṣaḥābah at al-Ḥudaybiyah without attributing to them hatred of '
    'anything the Prophet ﷺ brought.',
    'State the rule %s and the two-sided warning the compiler closes with.'
    % ('«' + ar('المَعَاصِي بَرِيدُ الكُفْر') + '»'),
])

b += B.provenance(136, 145)

b += B.matn(
    'الخَامِس: مَنْ أَبْغَضَ شَيْئًا مِمَّا جَاءَ بِهِ النَّبِيُّ ﷺ '
    'وَلَوْ عَمِلَ بِه — كَفَرَ إِجْمَاعًا؛ وَالدَّلِيلُ قَوْلُهُ تَعَالَى: '
    '﴿ذَلِكَ بِأَنَّهُمْ كَرِهُوا مَا أَنْزَلَ اللهُ فَأَحْبَطَ '
    'أَعْمَالَهُمْ﴾.',
    'Some copies of the matn read «مِنْ دِينِ الله» in place of «مِمَّا جَاءَ '
    'بِهِ النَّبِيُّ ﷺ» — the compiler notes the variant.')

b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><strong>The whole clause '
        'turns on four words, and they are easy to read past: %s — '
        '<em>“even if he acts upon it.”</em></strong></p>'
        '<p style="margin:0;font-size:.93rem">A man prays and hates that prayer '
        'was legislated. A man makes ḥajj and hates that ḥajj was imposed. '
        '<em>The deed is there and the nullifier is still there</em>, which '
        'tells you immediately that what is being judged is not the limbs. '
        'And it tells you something else, which the footnote makes explicit: '
        '<strong>if the بُغْض that nullifies were dislike of the act itself, '
        'these four words would be a contradiction.</strong> So it is not. '
        'It is <strong>%s</strong> — dislike of the <em>legislating</em>.</p>'
        % ('«' + ar('وَلَوْ عَمِلَ بِهِ') + '»', ar('بُغْضُ التَّشْرِيع')),
        wash='var(--accent-wash)', edge='var(--accent)'))
b += B.ayah(
    'ذَٰلِكَ بِأَنَّهُمْ كَرِهُوا مَا أَنزَلَ اللَّهُ فَأَحْبَطَ أَعْمَالَهُمْ',
    'That is because they hated what Allah sent down, so He rendered their '
    'deeds worthless.',
    'سُورَةُ مُحَمَّد · 47:9')
b += B.prose(
    '<em>This is the same verse that closed the fourth nullifier, and it is '
    'carrying a different load here.</em> There it answered the man who is not '
    '<strong>pleased</strong> with the ruling of the Messenger ﷺ. Here it is the '
    'daleel for the man who <strong>hates</strong> a thing of what he brought. '
    'And in both places the operative word is the heart’s, not the hand’s.')

# ---------------------------------------------------------------- two kinds
b += B.heading('نَوْعَانِ مِنَ البُغْض', 'Two Kinds, and Only One Is Disbelief')
b += B.prose(
    'This is the distinction to carry out of the lesson, and it is the '
    'compiler’s footnote on %s. <strong>Get it wrong in either direction and '
    'you have ruined the clause</strong> — collapse the two and you make a '
    'woman’s grief at her co-wife into apostasy; erase the first and you empty '
    'the nullifier out entirely.' % ('«' + ar('وَلَوْ عَمِلَ بِهِ') + '»'))
b += B.sharh(table([
    thead3('', 'النَّوْعُ الأَوَّل · بُغْضٌ مُكَفِّر',
           'النَّوْعُ الثَّانِي · بُغْضٌ طَبِيعِيّ'),
    row3('<strong>what is hated</strong>',
         'The <strong>legislating</strong>, or something of it — '
         '<em>«so he hates that Allah legislated marriage, or hates that Allah '
         'sent Muḥammad ﷺ»</em>',
         'The <strong>act</strong>, for its hardship or pain — while being '
         '<strong>pleased with the Sharīʿah</strong> of it'),
    row3('<strong>examples</strong>',
         'Hating that prayer, or zakāh, or tawḥīd, or fasting was legislated',
         'A woman whose husband marries a second wife — '
         '<em>«hating the particular decree, pleased with the '
         'Sharīʿah»</em>; one who dislikes wuḍūʾ with cold water; '
         'one who dislikes fighting for its hardship on him'),
    row3('<strong>the ruling</strong>',
         '<strong>كُفْر</strong> — and Ibn Taymiyyah relays the <strong>'
         'ijmāʿ</strong> that whoever hates what the Messenger ﷺ brought is a '
         'disbeliever',
         '<em>«<strong>فَهَذَا لَيْسَ مِنَ الكُفْرِ فِي شَيْء</strong>»</em> — '
         '“this is not of disbelief in anything at all”'),
]))
b += B.prose(
    'The verses given for the first kind are worth reading together, because '
    'each one names a different symptom of the same thing — <em>and all three '
    'are describing hearts, not deeds.</em>')
b += B.ayah(
    'بَلْ جَاءَهُم بِالْحَقِّ وَأَكْثَرُهُمْ لِلْحَقِّ كَارِهُونَ',
    'Rather, he brought them the truth, and most of them are averse to the '
    'truth.',
    'سُورَةُ المُؤْمِنُون · 23:70')
b += B.ayah(
    'وَمَن يُرِدْ أَن يُضِلَّهُ يَجْعَلْ صَدْرَهُ ضَيِّقًا حَرَجًا كَأَنَّمَا '
    'يَصَّعَّدُ فِي السَّمَاءِ',
    'And whomever He wills to leave astray, He makes his breast tight and '
    'constricted, as though he were climbing into the sky.',
    'سُورَةُ الأَنْعَام · 6:125')
b += B.ayah(
    'وَإِذَا ذُكِرَ اللَّهُ وَحْدَهُ اشْمَأَزَّتْ قُلُوبُ الَّذِينَ لَا '
    'يُؤْمِنُونَ بِالْآخِرَةِ',
    'And when Allah alone is mentioned, the hearts of those who do not believe '
    'in the Hereafter shrink with aversion.',
    'سُورَةُ الزُّمَر · 39:45')
b += B.prose(
    'And the verses given for the <strong>second</strong> kind are the ones that '
    'settle the matter beyond argument, because <em>Allah describes the believers '
    'themselves this way.</em>')
b += B.ayah(
    'كُتِبَ عَلَيْكُمُ الْقِتَالُ وَهُوَ كُرْهٌ لَّكُمْ',
    'Fighting has been enjoined upon you, while it is hateful to you.',
    'سُورَةُ البَقَرَة · 2:216')
b += B.ayah(
    'يُجَادِلُونَكَ فِي الْحَقِّ بَعْدَمَا تَبَيَّنَ كَأَنَّمَا يُسَاقُونَ '
    'إِلَى الْمَوْتِ وَهُمْ يَنظُرُونَ',
    'They dispute with you concerning the truth after it had become clear, as '
    'though they were being driven to death while they looked on.',
    'سُورَةُ الأَنْفَال · 8:6')
b += B.prose(
    'The sharḥ pairs that with al-Anfāl 8:5 — <em>«and indeed a party of the '
    '<strong>believers</strong> were averse»</em> — and with al-Tawbah 9:38: '
    '<em>«what is the matter with you that when you are told, “Go forth in the '
    'path of Allah,” you cling heavily to the earth?»</em> '
    '<strong>These are believers.</strong> <em>So a heaviness in the soul toward '
    'a hard command is not the nullifier; and anyone who tells you otherwise is '
    'reading past three verses and a ḥadīth of Muslim.</em>')
b += B.hadith(
    'وَإِسْبَاغُ الوُضُوءِ عَلَى المَكَارِه',
    '“…and performing wuḍūʾ thoroughly despite discomfort.”',
    'صَحِيحُ مُسْلِم · عَنْ أَبِي هُرَيْرَةَ رَضِيَ اللهُ عَنْه')
b += B.sharh(
    p('<em>Read that ḥadīth as a definition.</em> The Prophet ﷺ names '
      '<strong>doing the act while it is disliked</strong> as a thing to be '
      'praised and counted among the means of raised ranks. '
      '<strong>It is not merely excused — it is rewarded.</strong>') +
    p('The sharḥ also quotes <em>«%s»</em> — paradise is encircled with things '
      'disliked — attributed to the Prophet ﷺ. '
      '<em>No grading is given for it at this place, so none is supplied '
      'here.</em>' % ar('حُفَّتِ الجَنَّةُ بِالمَكَارِه')))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><strong>And Ibn Taymiyyah '
        'is quoted on how the two kinds relate</strong>, in a sentence that is '
        'really about the mechanics of the heart:</p>'
        '<p style="margin:0;font-size:.93rem"><em>«The one who is content — '
        'what carries him to bear the disliked things and the pains is '
        '<strong>what he finds of the pleasure of contentment and its '
        'sweetness</strong>. So when that sweetness and pleasure are lost, it '
        'becomes impossible for him to bear pain and bitterness. '
        'So <strong>how can he be imagined to be content when he has with him '
        'none of the sweetness of contentment by which he might carry the '
        'bitterness of what is disliked?</strong>»</em> — al-Istiqāmah</p>') +
    p('<strong>Which is to say: the second kind is survivable because the first '
      'is absent.</strong> The co-wife bears her grief <em>on</em> the '
      'contentment underneath it. Remove the contentment and there is nothing '
      'left to bear it with. <em>That is the clinical account of how type 2 '
      'turns into type 1 if it is fed instead of fought.</em>'))
b += B.sharh(
    p('And the Imām of the matn himself, in his tafsīr of '
      '<em>«وَاصْبِرْ نَفْسَكَ مَعَ الَّذِينَ يَدْعُونَ رَبَّهُم»</em>, draws '
      'exactly the conclusion a worried person needs: '
      '<em>«in it is: that <strong>the believer is not harmed by his own soul’s '
      'dislike of that, when he struggles against it</strong>.»</em>') +
    p('<strong>So the obligation in the second kind is مُجَاهَدَة, not '
      'panic.</strong> <em>And one sentence of Ibn Bāz’s later on these folios '
      'is the whole method:</em> <em>«if he trains his soul and struggles '
      'against it, these deeds become a <strong>bliss he finds in his '
      'heart</strong>, and his soul becomes a mount for him in this — it '
      'complies with him, because he has trained it and struggled against '
      'it.»</em>'))

# ---------------------------------------------------------------- ibn baz
b += B.heading('وَلَوْ صَلَّى، وَلَوْ حَجّ', 'Ibn Bāz Applies the Matn’s Condition')
b += B.sharh(
    p('He states the clause first in general:') +
    box('<p style="margin:0;font-size:.94rem"><em>«And likewise whoever hates '
        'the law of Allah, or <strong>something</strong> of the law of Allah — '
        'so whoever hates something of the law of Allah: hates the prayer, or '
        'the zakāh, or <strong>the tawḥīd</strong>, or the fasting, and is '
        'averse to that — <strong>he becomes a disbeliever</strong>… So what is '
        'obligatory upon the believer is that he <strong>love what Allah has '
        'legislated</strong>, and that he ally upon that; and that he '
        '<strong>be wary of what Allah has forbidden</strong>, and ally upon '
        'that; and that he <strong>submit to the law of Allah wherever it '
        'is</strong>.»</em></p>') +
    p('<em>Note «أَوْ شَيْئًا» — “or something of it.” That is the matn’s word, '
      'and it is the hinge of the long refutation further down these '
      'folios.</em>'))
b += B.sharh(
    p('Then he is asked the exact question the matn’s four words anticipate: '
      '<em>what if he dislikes the thing but does not deny it — he dislikes, '
      'say, the prohibition of drinking wine?</em>') +
    box('<p style="margin:0;font-size:.95rem"><em>«Whoever hates what Allah has '
        'legislated, <strong>his deed is nullified</strong>… '
        '<strong>Whoever hates the prayer — even if he prays</strong> — or '
        'hates the ḥajj — <strong>even if he makes ḥajj</strong> — or hates the '
        'prohibition of fornication, or of wine: <strong>he disbelieves, '
        'likewise.</strong>»</em></p>') +
    p('<strong>That is the matn’s %s, in his own voice, with the examples '
      'filled in.</strong> <em>And it is also the answer to anyone who imagines '
      'this nullifier is about weak feelings: the man in the example is praying. '
      'What is being judged is what he holds about the Legislator who imposed '
      'it.</em>' % ('«' + ar('وَلَوْ عَمِلَ بِهِ') + '»')))
b += B.sharh(
    p('And one more distinction, from a different question — this one between '
      'natural dislike and <strong>compulsion</strong>, which are constantly '
      'confused because the Arabic shares a root:') +
    box('<p style="margin:0;font-size:.93rem">On the pledge <em>«%s»</em>: '
        '<em>«its meaning is that they hear and obey <strong>even if this thing '
        'is something they dislike</strong> and it is hard upon them, because of '
        'their poverty or for other reasons — whenever the Messenger commands, '
        'they obey him, even if it is something that may harm them… '
        'So it is from the standpoint of <strong>natural dislike</strong>, from '
        'the standpoint of <strong>natural hardship</strong> — '
        '<strong>not</strong> from the standpoint of compulsion. '
        '<strong>Compulsion</strong> is his being forced to this thing, or '
        'threatened over a thing so that he does it, and it is '
        'not legislated — <em>that</em> is compulsion.»</em></p>'
        % ar('بَايَعْنَا رَسُولَ اللهِ ﷺ عَلَى السَّمْعِ وَالطَّاعَةِ فِي '
             'المَنْشَطِ وَالمَكْرَه')) +
    p('<em>The sharḥ quotes that ḥadīth here without a grading, so none is '
      'supplied.</em> <strong>And keep the three apart:</strong> '
      '%s is hating the legislating — the nullifier. '
      '%s is finding the act hard — rewarded. '
      '%s is being forced to an unlegislated act — a different chapter '
      'entirely, with its own rulings.'
      % (ar('بُغْضُ التَّشْرِيع'), ar('كَرَاهَةٌ طَبِيعِيَّة'),
         ar('إِكْرَاه'))))

# ---------------------------------------------------------------- masail
b += B.heading('مَسَائِل', 'Eight Questions, and the Spread Across Them')
b += B.prose(
    'What follows on these folios is a run of particular questions answered in '
    'Ibn Bāz’s own words. <strong>Read them as a set.</strong> <em>The point is '
    'not any single ruling — it is that the answers are not all the same, and '
    'the ones that are not takfīr are as instructive as the ones that are.</em>')
b += B.sharh(table([
    thead3('the question', 'his answer', 'what kind'),
    row3('Hating the Sharīʿah’s ruling on the <strong>beard</strong>',
         '<em>«Whoever hates the law of Allah in it <strong>has '
         'disbelieved</strong> — because the least of the states is that it is '
         'an emphasised sunnah.»</em>',
         'hating the <strong>legislating</strong> → type 1'),
    row3('Hating / reviling the <strong>Ṣaḥābah</strong> in general',
         'On %s: <em>«the one whom the Ṣaḥābah enrage, and who hates the '
         'Ṣaḥābah — <strong>there is no doubt about his disbelief and his '
         'misguidance</strong>. Those who hate the Ṣaḥābah in general and revile '
         'them in general <strong>are never Muslims</strong>.»</em>'
         % ('«' + ar('لِيَغِيظَ بِهِمُ الْكُفَّار') + '»'),
         'type 1'),
    row3('Reviling <strong>some</strong> of them, out of rancour toward some',
         '<em>«This is <strong>fisq and misguidance</strong> — '
         '<strong>but it is not greater disbelief.</strong>»</em>',
         '<strong>not</strong> type 1 — grave, and not this nullifier'),
    row3('Hating <strong>polygyny</strong> and claiming its absence is better',
         '<em>«He is a <strong>disbeliever, an apostate</strong> from Islām — '
         'because he is a denier of the ruling of Allah and averse to what Allah '
         'legislated… whoever holds that the Sharīʿah has wronged, or that the '
         'ruling of Allah in this is deficient or not good, or that what they do '
         'in the lands of the Christians — one wife — is better: '
         '<strong>all of this is apostasy.</strong>»</em>',
         'type 1 — and note it is the <em>claim about the ruling</em> that does '
         'it'),
    row3('«I hate <strong>Waḥshī ibn Ḥarb</strong>, because the Messenger ﷺ '
         'disliked him»',
         '<em>«<strong>This is a mistake.</strong> Upon him is repentance to '
         'Allah. It is not permissible — <strong>because he is of the Ṣaḥābah, '
         'and loving him is obligatory</strong>, even if there was some '
         'deficiency with him.»</em>',
         '<strong>not</strong> kufr — an error, with repentance due'),
    row3('Being <strong>irked</strong> by the recitation of al-Sajdah and '
         'al-Dahr at Jumuʿah fajr',
         '<em>«This is a sunnah the Prophet ﷺ performed and the authentic '
         'aḥādīth are established in it; and the one who is wearied by it is '
         '<strong>either ignorant or weak in faith</strong>.»</em>',
         '<strong>not</strong> kufr — and this is the answer to have ready'),
    row3('<strong>Songs</strong> and amusements',
         '<em>«They <strong>grow hypocrisy</strong>, and grow in the hearts '
         '<strong>aversion to the truth, and aversion to the Qurʾān</strong>, '
         'and aversion to the gatherings of remembrance and knowledge, and '
         'aversion to the acts of worship and the prayers, and contentment with '
         'every depravity and every affliction — so this is of their effects in '
         'the hearts, until the heart <strong>darkens and blackens</strong>.»</em>',
         'a <strong>cause</strong> that grows type 1'),
    row3('Finding the five prayers in congregation <strong>hard</strong>',
         '<em>«It is known that a person’s hastening to the five prayers in '
         'their time in congregation… and leaving his occupations at the time of '
         'the prayer, and leaving sleep at the time of the prayer, '
         '<strong>is hard upon some souls</strong>. But if he '
         '<strong>trains</strong> his soul and <strong>struggles</strong> '
         'against it, these deeds become a <strong>bliss he finds in his '
         'heart</strong>.»</em>',
         'type 2, named as such — and the <strong>cure</strong>'),
]))
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><strong>Three of those eight are '
        'not takfīr</strong>, and one of them is explicitly the opposite. '
        '<em>A man who is wearied by a long recitation is told he is ignorant or '
        'weak in faith — not that he has left the religion. A man who hates a '
        'Companion is told to repent, not that he has apostatised. Rancour '
        'toward some of the Ṣaḥābah is named fisq and misguidance, and then the '
        'door is explicitly closed: «but it is not greater disbelief.»</em></p>'
        '<p style="margin:.5rem 0 0;font-size:.93rem">Whoever quotes the beard '
        'answer and the polygyny answer from these folios while leaving out the '
        'other three has <strong>not quoted the folios</strong>. He has quoted '
        'the half he wanted.</p>',
        wash='var(--accent-wash)', edge='var(--accent)'))
b += B.sharh(
    p('The footnote on the beard answer is worth having, because '
      '<em>«the least of its states»</em> sounds like a hedge and is not one: '
      '<em>«his saying “the least of its states” is not intended to mean that it '
      'is [merely] a sunnah, or that there is a disagreement in it; rather he '
      'means: <strong>even if the non-obligation of letting it grow were '
      'supposed</strong>, there is no doubt that letting it grow is a prophetic '
      'sunnah — so whoever hates the legislation of Allah in it has disbelieved, '
      'because it is of what Allah sent down. '
      '<strong>So a disagreement, were it supposed to exist, does not affect the '
      'ruling of disbelief on the one who hates it.</strong>»</em>') +
    p('<em>That is a clean piece of reasoning and it generalises:</em> the '
      'nullifier attaches to <strong>hating that Allah legislated a thing</strong> '
      '— so the fiqh rank of the thing is beside the point. <em>Obligatory or '
      'recommended, the object of the hatred is the same.</em>'))

# ---------------------------------------------------------------- refutation
b += B.heading('هَلْ يُشْتَرَطُ بُغْضُ الدِّينِ كُلِّه؟',
               'The Long Refutation — “Only If He Hates All of It”')
b += B.prose(
    'Then the compiler takes up a position from a printed book, '
    '<em>تَسْهِيلُ العَقِيدَةِ الإِسْلَامِيَّة</em>, which held that hating what '
    'the Messenger ﷺ brought is only disbelief <strong>if he hates the whole '
    'religion of Allah</strong>; whoever hates <em>part</em> of it does not '
    'disbelieve. The argument offered was from this very verse: '
    '<em>«Allah mentioned in it the nullifying of the deeds of one who hated '
    '<strong>all</strong> of what Allah sent down, because «مَا» is '
    'general.»</em>')
b += B.sharh(
    p('<strong>The compiler’s reply is the best sustained reasoning in the book '
      'so far, and it is six answers to six claims.</strong> He opens flatly: '
      '<em>«%s»</em> — and then works.' % ar('وَهَذَا خَطَأ')) +
    obj('«مَا» in the verse means <strong>all</strong> of what Allah sent down.',
        'Allah said <em>«they hated <strong>what</strong> Allah sent '
        'down»</em> — <strong>He did not say “all of what Allah sent '
        'down”</strong>, and the difference between the two is plain. '
        '«مَا» here is a <strong>relative pronoun meaning “that which”</strong>, '
        'not a word meaning “all”, and it <strong>takes in the individual '
        'instances</strong> of what Allah sent down. So of one who hates the '
        'Qurʾān, or hates the Sunnah, or hates the prophethood of Muḥammad ﷺ and '
        'is angered by it, or hates the ḥajj — <em>it is sound to say: so-and-so '
        'hated what Allah sent down.</em>') +
    obj('A general «مَا» must mean the totality.',
        'Then test the same grammar on a sister verse. Of a man who eats '
        '<strong>one date</strong> it is sound to say <em>he ate what Allah made '
        'lawful</em> — and the verse is %s. So when we say <em>whoever eats what '
        'Allah made lawful enters Paradise</em>, or <em>whoever commits what '
        'Allah forbade of the destructive sins enters the Fire</em>, '
        '<strong>nobody understands that he must eat every lawful thing on earth '
        'first, or commit every forbidden thing.</strong>'
        % ('«' + ar('كُلُوا مِن طَيِّبَاتِ مَا رَزَقْنَاكُم') + '»')) +
    obj('And in any case the verse concerns only those who never entered Islām — '
        'and <strong>the disbeliever hates all of Allah’s religion</strong>.',
        '<strong>This is not correct</strong>, and the list he gives is the '
        'refutation: among the disbelievers are those who '
        '<strong>love</strong> many of the Sharʿī rulings — '
        '<em>maintaining ties of kinship, honouring the guest, the system of '
        'zakāh in Islām, chastity, aiding the wronged, truthfulness, '
        'trustworthiness</em> — indeed <strong>some of them love Islām, and were '
        'it not for people’s blame he would accept it</strong>. And the '
        'disbelievers of Quraysh <strong>performed ḥajj and ʿumrah</strong>, and '
        'among them were those who fasted voluntarily and made vows to Allah. '
        '<em>«So they are not all of them hating all of the religion of Allah '
        'and its rulings from first to last — and perhaps that is not even '
        'conceivable.»</em>') +
    obj('If part-hatred were disbelief, the <strong>reductio</strong> would be '
        'absurd.',
        'The compiler turns the reductio the other way and it lands: '
        '<strong>if the verse required hating the totality, we could not '
        'declare a disbeliever the man who hates Islām itself</strong> — not '
        'until he also hated <em>every</em> sound heavenly religion before its '
        'abrogation, and everything Allah sent down upon <em>all</em> of His '
        'prophets, <em>«because all of it is of what Allah sent down — and '
        'nobody says this.»</em>'))
b += B.sharh(
    obj('<strong>The Sunnah shows it is not disbelief:</strong> ʿUmar disliked '
        'the ruling of the Prophet ﷺ at the truce of al-Ḥudaybiyah — and the '
        'apparent state of the Ṣaḥābah that day is that they <em>hated</em> this '
        'truce, which is why they did not at first comply with his command ﷺ to '
        'shave.',
        '<strong>No doubt many of the Ṣaḥābah did not desire the truce and were '
        'averse to it, and they reviewed it with the Prophet ﷺ.</strong> '
        '<em>And that was <strong>before the ruling had settled with '
        'them</strong></em> — because they saw it as one of the '
        '<strong>political matters in which ijtihād is permitted</strong>, and '
        'they hoped only to change his ijtihād, since they supposed this was '
        'giving a humiliation in the religion, and held that the perfection of '
        'the religion lay in engaging the disbelievers of Makkah in battle, to '
        'humble them and make Islām manifest. '
        '<strong>So when they knew that this was of what the Prophet ﷺ brought, '
        'and the revelation settled it with the descent of Sūrat al-Fatḥ, they '
        'left off reviewing it with him and their souls were at peace with '
        'it.</strong> <em>«So it is not permissible then to say that the Ṣaḥābah '
        'hated and were averse to something of what the Prophet ﷺ brought — we '
        'seek refuge with Allah.»</em>'))
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><strong>That answer is worth more '
        'than the objection it answers.</strong> It gives you the whole method '
        'for reading the Ṣaḥābah’s reviewing of the Prophet ﷺ: '
        '<em>a matter they took to be open to ijtihād, reviewed before the '
        'ruling was settled, and accepted the moment the revelation came.</em> '
        '<strong>Not one of those three elements is dispensable.</strong> Take '
        'away the first and it is objection to a ruling; take away the third and '
        'it is persistence. <em>It is also the exact shape of what the sharḥ '
        'said about Ḥunayn back in part 1 of the fourth nullifier.</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))
b += B.sharh(
    p('He then answers the objection from the ḥadīth of the bedouin:') +
    box('<p style="margin:0;font-size:.95rem">The Prophet ﷺ said to a man: '
        '<em>«%s»</em> — <strong>“Accept Islām.”</strong> He said: '
        '<em>«%s»</em> — <strong>“I find myself averse.”</strong> '
        'He said: <em>«%s»</em> — <strong>“Accept Islām, even if you are '
        'averse.”</strong></p>'
        % (ar('أَسْلِمْ'), ar('أَجِدُنِي كَارِهًا'),
           ar('أَسْلِمْ وَإِنْ كُنْتَ كَارِهًا'))) +
    p('<strong>The grading is given, and named.</strong> The compiler cites it '
      'from Aḥmad’s <em>Musnad</em> by two chains from Ḥumayd from Anas and says '
      '<em>«%s»</em> — <strong>its chain is authentic</strong>; and he reports '
      'al-Dhahabī’s judgement in <em>Muʿjam Shuyūkhihi</em>: '
      '<em>«this is an authentic, singular ḥadīth»</em>.'
      % ar('وَسَنَدُهُ صَحِيح')) +
    p('<strong>And then the answer:</strong> <em>«there is not in this that if '
      'he accepted Islām while hating the religion his Islām would be valid. '
      'For this bedouin had <strong>made clear to the Prophet ﷺ</strong> that '
      'in his soul there was a <strong>remnant</strong> of dislike for the '
      'religion which had not yet expanded to it — so the Prophet ﷺ guided him '
      'and directed him to <strong>accepting the truth and compelling the soul '
      'to accept Islām even if his soul disliked it</strong>; '
      '<strong>because faith, when its pleasantness mixes with the hearts, no '
      'one is displeased with it.</strong>»</em>') +
    p('<em>So the ḥadīth is about a man being led out of the dislike, not a man '
      'being admitted with it.</em> <strong>And the last sentence is the '
      'promise:</strong> the aversion does not survive contact with the faith '
      'itself.'))
b += B.sharh(
    obj('<strong>And Thaqīf:</strong> the Prophet ﷺ accepted them although they '
        'stipulated that there be no <em>ṣadaqah</em> upon them and no '
        '<em>jihād</em> — <em>«and the apparent state of them is that they '
        'entered Islām while hating these two rulings.»</em> '
        '<em>(Abū Dāwūd; the compiler grades the chain <strong>ḥasan</strong>.)</em>',
        'This is <strong>borne on dislike of <em>acting</em> on the two, for '
        'their hardship on them at the outset</strong> — and there is '
        '<strong>no text in it</strong> that they hated their '
        '<em>legislation</em>; rather their apparent state is that they disliked '
        '<strong>performing</strong> them. So the Prophet ﷺ was gentle with '
        'them, <em>knowing that once they believed they would come to know the '
        'obligation of zakāh and jihād upon them and would comply</em>, and he '
        'did not press them, <strong>lest they be driven away from Islām</strong>; '
        'and knowing that <strong>this corrupt condition has no weight and no '
        'effect</strong> — as in the Ṣaḥīḥayn in the story of Barīrah, when he '
        'said <em>«and stipulate the right of inheritance for them»</em>, '
        'meaning: it has no effect. '
        '<strong>And the same ḥadīth itself says it:</strong> the Prophet ﷺ said '
        'afterwards, <em>«they will give charity and they will fight, once they '
        'accept Islām.»</em>'))
b += B.sharh(
    p('And the compiler seals that with a quotation from the ḥāfiẓ '
      '<strong>Abū Aḥmad al-Qaṣṣāb</strong> — <em>whom Ibn Taymiyyah calls «the '
      'well-known imām»</em> — in <em>Nukat al-Qurʾān</em>:') +
    box('<p style="margin:0;font-size:.93rem"><em>«And I do not know of any '
        'disagreement among the Ummah that the one coming out of disbelief into '
        'faith, were he to say: <strong>“I believe in Allah, and I believe that '
        'the prayer and the zakāh are a right — but I will not perform '
        'them,”</strong> and confine himself to pronouncing the testimony — '
        '<strong>that it is not accepted from him, and that he is a disbeliever '
        'as he was.</strong>»</em></p>'))
b += B.sharh(
    obj('<strong>The last objection, and the most tempting:</strong> the mere '
        'commission of sins carries the sinner — willing or not — into hating '
        'some acts of obedience. The man given to drink or to fornication hates '
        'that the law of Allah be applied in his town so he is not prevented, '
        'and hates the ones who enjoin good; yet Ahl al-Sunnah are agreed that '
        'committing them does not take him out of Islām. <em>So hating some acts '
        'of obedience is not disbelief.</em>',
        '<em>«<strong>وَهَذَا لَيْسَ بِشَيْء، وَالمُلَازَمَةُ '
        'مُنْتَفِيَة</strong>»</em> — the implication simply does not hold. '
        '<strong>Contradictory wills can sit together in one heart</strong> — '
        'the soul’s appetite for the sin and the heart’s hatred <em>of the '
        'sin</em>; <em>so all the more does committing a sin not entail hating '
        'the obedience.</em> And the claim is <strong>contradicted by the '
        'evidence</strong>: many of the people of major sins '
        '<strong>love</strong> the people of ḥisbah, and love that Islām be '
        'ruled by in their lands, and <strong>praise their rulers for '
        'establishing the ḥudūd</strong> — even while they want concealment for '
        'themselves; many of them love the people of obedience and uprightness '
        'and <em>wish Allah would help them against their own desires so they '
        'might repent</em>; and the drinkers and smokers '
        '<strong>are not angered to see the scholars of Islām warning against '
        'it — rather you find them warning their own children off it and '
        'striking them over it</strong>. And such-and-such of the Ṣaḥābah '
        '<strong>came to the Messenger of Allah ﷺ to have the ḥadd established '
        'upon them</strong>, and did not hate him ﷺ.'))
b += B.hadith(
    'لَا تَلْعَنْهُ، فَإِنَّهُ يُحِبُّ اللهَ وَرَسُولَه',
    '“Do not curse him — for he loves Allah and His Messenger.”',
    'رَوَاهُ البُخَارِيّ · said by the Prophet ﷺ of a man brought repeatedly '
    'for drink')
b += B.sharh(
    p('<em>That ḥadīth is the whole answer in one sentence,</em> and the '
      'compiler uses it as such. The man is a repeat offender, brought for the '
      'ḥadd again, and he is being <strong>cursed by others</strong> — and the '
      'Prophet ﷺ stops them with <strong>what is in the man’s heart.</strong>') +
    p('So, the compiler concludes: <em>«they love the legislation of Allah and '
      'love that the law of Allah be carried out on the criminals; and whoever’s '
      'faith among them is strong steps forward to the imām to have the ḥadd '
      'established on him; and of them is one who shelters under Allah’s '
      'concealment; and of them is one who hates that the ḥadd be established '
      'upon him — <strong>not because he hates the legislation</strong>, but '
      'for what is in it of pain to him, or his killing, or the tearing of his '
      'covering. <strong>So this is of the natural dislike.</strong>»</em>') +
    p('<em>Which returns the whole refutation to the distinction it started '
      'from.</em> <strong>Type 2, again — and now in the hardest case, the '
      'habitual sinner.</strong>'))

# ---------------------------------------------------------------- close
b += B.heading('المَعَاصِي بَرِيدُ الكُفْر', 'And Yet — the Two-Sided Warning')
b += B.sharh(
    p('Having refused the inference, the compiler refuses to leave the sinner '
      'comfortable either:') +
    box('<p style="margin:0;font-size:.94rem"><em>«<strong>Yes</strong> — '
        'immersion in the major sins and turning away from the obligations '
        '<strong>may lead its author in the future to aversion to the religion '
        'and hatred of it</strong>. And for this the scholars said: '
        '<strong>%s</strong> — the acts of disobedience are the '
        '<strong>courier of disbelief</strong>. So this divine punishment may '
        'descend on some of the disobedient who contravene His command; and for '
        'this Allah warned them lest a trial befall them — '
        'which shows the <strong>obligation of fearing sins</strong>, and that '
        'they are <strong>among the causes of falling into apostasy</strong>, we '
        'seek refuge with Allah from it.»</em></p>'
        % ar('المَعَاصِي بَرِيدُ الكُفْر')) +
    p('<strong>So both things are true at once, and the lesson is in holding '
      'them together.</strong> <em>Committing a sin does not entail hating the '
      'obedience — and living in sin is the road by which that hatred '
      'arrives.</em> The first is a rule of judgement; the second is a warning '
      'about oneself. <em>Apply the first to other people and the second to '
      'yourself, and you have read the folios correctly.</em>'))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><strong>And then the '
        'clause closes with something nobody would predict from its '
        'subject.</strong></p>'
        '<p style="margin:0;font-size:.94rem"><em>«When that is clear: it is '
        '<strong>obligatory upon every Muslim to beware lest there fall into his '
        'heart an aversion to the religion, and he be destroyed</strong>; and '
        '<strong>it is upon the scholar to carry the people upon the known '
        'middle way</strong> — so he does not take them the way of '
        '<strong>severity</strong>, nor incline them to the side of '
        '<strong>dissolution</strong>; for going out to the extremes is a '
        'departure from justice, and the welfare of the creation is not '
        'established by it. As for the side of dissolution — it is the likely '
        'place of walking with caprice and appetite, and Allah has forbidden us '
        'to follow them. And as for <strong>the side of harshness — it is a '
        'destroyer: it makes the religion hateful to the common '
        'people.</strong>»</em></p>') +
    p('<strong>Read that twice.</strong> <em>A clause whose subject is hating '
      'the religion ends by naming <strong>harshness in teaching it</strong> as '
      'one of the things that <em>produces</em> that hatred</em> — and it names '
      'it as a <strong>مُهْلِكَة</strong>, a destroyer, the same weight of word '
      'used for dissolution on the other side. <em>The man who takes the nine '
      'folios above and uses them to make the religion heavy on the common '
      'people is, by the compiler’s own closing sentence, doing the thing the '
      'clause warns against.</em>'))

b += B.vocab([
    ('بُغْضُ التَّشْرِيع', 'bughḍ al-tashrīʿ', 'hatred of the legislating',
     'النَّوْعُ الأَوَّل. Hating that Allah legislated a thing — or that He sent '
     'Muḥammad ﷺ. This is the nullifier, and Ibn Taymiyyah relays the ijmāʿ '
     'on it.'),
    ('بُغْضٌ طَبِيعِيّ', 'bughḍ ṭabīʿī', 'natural dislike',
     'النَّوْعُ الثَّانِي. Finding the act hard or painful while being pleased '
     'with its Sharīʿah — «فَهَذَا لَيْسَ مِنَ الكُفْرِ فِي شَيْء». Allah '
     'describes the believers this way: «وَهُوَ كُرْهٌ لَكُمْ».'),
    ('وَلَوْ عَمِلَ بِهِ', 'wa-law ʿamila bihī', 'even if he acts upon it',
     'The matn’s four words, and the whole key to the clause: the deed does not '
     'answer for the heart. Ibn Bāz: «مَنْ كَرِهَ الصَّلَاةَ — وَلَوْ صَلَّى — '
     '… كَفَر».'),
    ('إِكْرَاه', 'ikrāh', 'compulsion',
     'Not the same as كَرَاهَة. Ibn Bāz defines it: being forced to a thing, or '
     'threatened over a thing so that he does it, and it is not legislated. A '
     'different chapter with its own rulings.'),
    ('المَكَارِه', 'al-makārih', 'things disliked',
     'What the Prophet ﷺ named as praiseworthy to bear — «وَإِسْبَاغُ '
     'الوُضُوءِ عَلَى المَكَارِه», Ṣaḥīḥ Muslim. Type 2 is not merely excused; '
     'bearing it is rewarded.'),
    ('المُلَازَمَة', 'al-mulāzamah', 'the necessary implication',
     'The compiler on the claim that sinning entails hating the obedience: '
     '«وَالمُلَازَمَةُ مُنْتَفِيَة» — the implication does not hold. Contrary '
     'wills coexist in one heart.'),
    ('المَعَاصِي بَرِيدُ الكُفْر', 'al-maʿāṣī barīd al-kufr',
     'sins are the courier of disbelief',
     'The scholars’ rule, cited here as the other side of that answer: '
     'immersion in sin may be the road by which hatred of the religion '
     'eventually arrives.'),
    ('المَعْهُودُ الوَسَط', 'al-maʿhūd al-wasaṭ', 'the known middle way',
     'What it is upon the scholar to carry people on — neither the way of '
     'شِدَّة nor the side of اِنْحِلَال, «for going out to the extremes is a '
     'departure from justice».'),
    ('مُهْلِكَة', 'muhlikah', 'a destroyer',
     'The compiler’s word for the side of harshness: «فَإِنَّهَا مُهْلِكَةٌ '
     'تُبَغِّضُ لِلْعَامَّةِ الدِّين» — it makes the religion hateful to the '
     'common people.'),
])

b += B.mcq('nq-l08-mcq', [
    ('What do the matn’s words «وَلَوْ عَمِلَ بِهِ» establish?',
     ['That the deed excuses the heart',
      'That the بُغْض meant is hatred of the LEGISLATING, not of the act — since '
      'a man may pray and still fall under the clause',
      'That the clause applies only to one who abandons the act',
      'That the ijmāʿ is disputed'], 1),
    ('What are the two kinds of بُغْض in the footnote?',
     ['Open and hidden',
      'بُغْضٌ مُكَفِّر — hatred of the legislating; and بُغْضٌ طَبِيعِيّ — '
      'natural dislike of the act while being pleased with its Sharīʿah',
      'Major and minor in degree only',
      'Of the heart and of the tongue'], 1),
    ('Which examples does the footnote give for the SECOND kind?',
     ['Hating that marriage was legislated',
      'A woman whose husband marries a second wife — averse to the particular '
      'decree, pleased with the Sharīʿah; one who dislikes wuḍūʾ with cold '
      'water; one who dislikes fighting for its hardship',
      'Hating that Allah sent Muḥammad ﷺ',
      'Hating the prohibition of wine'], 1),
    ('And what is its ruling?',
     ['Lesser disbelief',
      '«فَهَذَا لَيْسَ مِنَ الكُفْرِ فِي شَيْء» — this is not of disbelief in '
      'anything at all',
      'Major sin',
      'It depends on the scholar'], 1),
    ('Which verse does the sharḥ use to settle that the second kind is not '
     'disbelief?',
     ['al-Māʾidah 5:44',
      '«كُتِبَ عَلَيْكُمُ الْقِتَالُ وَهُوَ كُرْهٌ لَكُمْ» — al-Baqarah 2:216, '
      'and with it al-Anfāl 8:5–6 on «a party of the BELIEVERS» being averse',
      'al-Tawbah 9:31',
      'al-Zumar 39:45'], 1),
    ('What does the ḥadīth «وَإِسْبَاغُ الوُضُوءِ عَلَى المَكَارِه» add?',
     ['That wuḍūʾ may be shortened in cold',
      'That bearing the act while it is disliked is PRAISED — type 2 is not '
      'merely excused but rewarded',
      'That cold water is forbidden',
      'That dislike invalidates the wuḍūʾ'], 1),
    ('The sharḥ quotes «حُفَّتِ الجَنَّةُ بِالمَكَارِه». What does this page '
     'supply for it?',
     ['A grading of ṣaḥīḥ',
      'No grading — because the sharḥ gives none at this place',
      'A grading of ḍaʿīf',
      'An attribution to Muslim'], 1),
    ('In Ibn Taymiyyah’s quoted explanation, what makes the believer able to '
     'bear what he dislikes?',
     ['Fear of punishment alone',
      'What he finds of the pleasure and sweetness of RIḌĀ — and when that is '
      'lost, bearing bitterness becomes impossible',
      'Habit',
      'The company of others'], 1),
    ('What did the Imām of the matn conclude in his tafsīr of «وَاصْبِرْ '
     'نَفْسَكَ مَعَ الَّذِينَ يَدْعُونَ رَبَّهُم»?',
     ['That dislike invalidates the deed',
      'That the believer is NOT harmed by his own soul’s dislike of that, when '
      'he struggles against it',
      'That he must abandon the gathering',
      'That the verse concerns the hypocrites'], 1),
    ('Give Ibn Bāz’s application of the matn’s condition.',
     ['Whoever abandons the prayer disbelieves',
      '«Whoever hates the prayer — even if he prays — or hates the ḥajj — even '
      'if he makes ḥajj — or hates the prohibition of fornication or of wine: he '
      'disbelieves, likewise»',
      'Whoever prays without khushūʿ disbelieves',
      'Whoever doubts the obligation disbelieves'], 1),
    ('Which four does Ibn Bāz name as examples of «something of the law of '
     'Allah»?',
     ['Marriage, trade, travel, inheritance',
      'The prayer, the zakāh, THE TAWḤĪD, and the fasting',
      'Ḥajj, ʿumrah, iʿtikāf, and fasting',
      'The ḥudūd, the jihād, the ḥisbah, and the bayʿah'], 1),
    ('How does Ibn Bāz define إِكْرَاه?',
     ['Any hardship in an act',
      'Being forced to a thing, or threatened over a thing so that he does it, '
      'and it is not legislated',
      'Dislike arising from poverty',
      'Obeying a command one finds heavy'], 1),
    ('On hating the Sharīʿah’s ruling regarding the beard, what did he say?',
     ['It is a disputed matter with no ruling',
      'Whoever hates the law of Allah in it has disbelieved — «because the least '
      'of the states is that it is an emphasised sunnah»',
      'It is fisq but not kufr',
      'It is permitted to dislike it'], 1),
    ('And what does the footnote clarify about «the least of the states»?',
     ['That it concedes the matter is only a sunnah',
      'That it does NOT mean it is merely a sunnah or disputed — rather: even if '
      'non-obligation were supposed, it is a prophetic sunnah, so a supposed '
      'disagreement does not affect the ruling on the one who hates Allah’s '
      'legislation in it',
      'That the ruling applies only in Najd',
      'That the beard is obligatory by ijmāʿ'], 1),
    ('Reviling the Ṣaḥābah in general, versus rancour toward some of them:',
     ['Both are greater disbelief',
      'Hating and reviling them in general — «they are never Muslims»; but '
      'reviling some, where there is some rancour toward some, is fisq and '
      'misguidance and «it is not greater disbelief»',
      'Both are fisq',
      'Neither is addressed on these folios'], 1),
    ('A man says: «I hate Waḥshī ibn Ḥarb, because the Messenger ﷺ disliked '
     'him.» Ibn Bāz answered:',
     ['That he has apostatised',
      '«This is a mistake; upon him is repentance to Allah; it is not permissible '
      '— because he is of the Ṣaḥābah and loving him is obligatory, even if '
      'there was some deficiency with him»',
      'That it is permitted',
      'That he must be asked to clarify'], 1),
    ('Of one who is wearied by the recitation of al-Sajdah and al-Dahr at '
     'Jumuʿah fajr, Ibn Bāz said he is:',
     ['A disbeliever',
      'Either ignorant or weak in faith',
      'A hypocrite',
      'An innovator'], 1),
    ('What did Ibn Bāz say songs and amusements do?',
     ['Waste time only',
      'They GROW hypocrisy, and grow in the hearts aversion to the truth, to the '
      'Qurʾān, to the gatherings of knowledge and to the acts of worship — until '
      'the heart darkens and blackens',
      'They are disputed among the scholars',
      'They are disliked but harmless'], 1),
    ('And what is his cure for the hardness of the five prayers upon the soul?',
     ['Reducing them in travel',
      'Training the soul and struggling against it — until «these deeds become a '
      'bliss he finds in his heart, and his soul becomes a mount for him»',
      'Praying alone',
      'Waiting for the heart to soften'], 1),
    ('«تَسْهِيلُ العَقِيدَةِ الإِسْلَامِيَّة» held that hating what the '
     'Messenger ﷺ brought is disbelief only if:',
     ['He announces it',
      'He hates the WHOLE religion of Allah — because «مَا» in the verse is '
      'general',
      'He abandons the act as well',
      'He is a scholar'], 1),
    ('What is the compiler’s grammatical answer?',
     ['That «مَا» is interrogative',
      'Allah said «they hated WHAT Allah sent down», not «all of what Allah sent '
      'down» — «مَا» is a relative pronoun meaning «that which», taking in the '
      'individual instances',
      'That the verse is abrogated',
      'That «مَا» is negating'], 1),
    ('Which verse does he test the same grammar on?',
     ['«وَمَا أَرْسَلْنَاكَ إِلَّا رَحْمَةً»',
      '«كُلُوا مِنْ طَيِّبَاتِ مَا رَزَقْنَاكُمْ» — of a man who eats one date '
      'it is sound to say he ate what Allah made lawful',
      '«وَأَنْزَلْنَا إِلَيْكَ الْكِتَابَ»',
      '«إِنَّ الْحُكْمَ إِلَّا لِلَّهِ»'], 1),
    ('Against the claim «the disbeliever hates all of Allah’s religion», what '
     'does the compiler point out?',
     ['That it is true but irrelevant',
      'That many disbelievers LOVE many Sharʿī rulings — kinship ties, honouring '
      'the guest, the zakāh system, chastity, aiding the wronged, truthfulness, '
      'trustworthiness — and the disbelievers of Quraysh performed ḥajj and '
      'ʿumrah, some fasting voluntarily and making vows',
      'That the disbelievers are of many kinds in law only',
      'That the claim contradicts the ijmāʿ'], 1),
    ('What is his reductio against requiring hatred of the totality?',
     ['That it would excuse the hypocrites',
      'That we could not then declare a disbeliever the man who hates Islām '
      'itself — not until he also hated every sound heavenly religion before its '
      'abrogation and everything sent down to all the prophets',
      'That it would abrogate the verse',
      'That it would contradict al-Māʾidah 5:44'], 1),
    ('How does he answer the objection from al-Ḥudaybiyah?',
     ['By denying that any of them disliked the truce',
      'They were averse and reviewed it with him BEFORE the ruling had settled — '
      'seeing it as a political matter open to ijtihād — and when the revelation '
      'settled it with Sūrat al-Fatḥ they left off reviewing and their souls '
      'were at peace with it',
      'By grading the reports weak',
      'By saying ʿUmar alone disliked it'], 1),
    ('Which three elements make that explanation work?',
     ['Sincerity, obedience, patience',
      'A matter they took to be open to ijtihād; reviewed BEFORE the ruling was '
      'settled; and accepted the moment the revelation came',
      'Consultation, consensus, delegation',
      'Fear, hope, love'], 1),
    ('The ḥadīth «أَسْلِمْ وَإِنْ كُنْتَ كَارِهًا» — what grading does the '
     'compiler give, and from whom?',
     ['He gives none',
      'He grades the chain ṣaḥīḥ from Aḥmad’s Musnad, and reports al-Dhahabī’s '
      '«this is an authentic, singular ḥadīth»',
      'He grades it ḥasan only',
      'He reports Ibn Taymiyyah grading it'], 1),
    ('And what is his answer to the objection from it?',
     ['That the ḥadīth is about a hypocrite',
      'The bedouin had made clear that in his soul was a REMNANT of dislike not '
      'yet expanded — so the Prophet ﷺ guided him to accept the truth and compel '
      'the soul, «because faith, when its pleasantness mixes with the hearts, no '
      'one is displeased with it»',
      'That the wording is «even if you are poor»',
      'That it is specific to that man'], 1),
    ('Thaqīf stipulated no ṣadaqah and no jihād. How is that answered?',
     ['Their Islām was invalid',
      'It is borne on disliking PERFORMING them for their hardship at the outset '
      '— no text says they hated their legislation; the corrupt condition has no '
      'effect, as with «and stipulate the right of inheritance for them» in '
      'Barīrah’s story; and the ḥadīth itself says «they will give charity and '
      'they will fight, once they accept Islām»',
      'The report is rejected',
      'The stipulation was accepted permanently'], 1),
    ('What does Abū Aḥmad al-Qaṣṣāb report no disagreement about?',
     ['The ruling on the beard',
      'That one coming out of disbelief who says «I believe, and that prayer and '
      'zakāh are a right — but I will not perform them» is not accepted from, '
      'and is a disbeliever as he was',
      'The grading of the Thaqīf ḥadīth',
      'The permissibility of conditions in Islām'], 1),
    ('To the claim that sinning NECESSARILY entails hating some obedience, the '
     'compiler answers:',
     ['That it is true of major sins only',
      '«وَالمُلَازَمَةُ مُنْتَفِيَة» — the implication does not hold; '
      'contradictory wills coexist in one heart, and the evidence contradicts '
      'the claim',
      'That it is a matter of ijtihād',
      'That it applies only to the ḥudūd'], 1),
    ('Which ḥadīth does he bring against it?',
     ['«إِنَّمَا الأَعْمَالُ بِالنِّيَّات»',
      '«لَا تَلْعَنْهُ، فَإِنَّهُ يُحِبُّ اللهَ وَرَسُولَه» — al-Bukhārī, said '
      'of a man brought repeatedly for drink',
      '«مَنْ بَدَّلَ دِينَهُ فَاقْتُلُوه»',
      '«الدِّينُ النَّصِيحَة»'], 1),
    ('Why does a sinner hate that the ḥadd be established upon him, in the '
     'compiler’s account?',
     ['Because he hates the legislation',
      'NOT because he hates the legislation — but for what is in it of pain, or '
      'his killing, or the tearing of his covering; «so this is of the natural '
      'dislike»',
      'Because he denies the ruling',
      'Because he prefers another judge'], 1),
    ('What is «المَعَاصِي بَرِيدُ الكُفْر» cited to establish?',
     ['That every sinner is a disbeliever',
      'That immersion in major sins and turning from obligations MAY lead its '
      'author in the future to hatred of the religion — so sins are to be feared '
      'as among the causes of falling into apostasy',
      'That sins nullify deeds immediately',
      'That the ḥudūd must be established'], 1),
    ('How are the two sides of that answer to be held together?',
     ['The second cancels the first',
      'The first is a rule of JUDGEMENT about others; the second is a WARNING '
      'about oneself',
      'They apply to different eras',
      'The first applies to scholars only'], 1),
    ('What does the compiler say it is upon the scholar to do?',
     ['To take the strictest of the positions',
      'To carry the people upon المَعْهُودُ الوَسَط — neither the way of '
      'severity nor inclining them to dissolution, «for going out to the '
      'extremes is a departure from justice»',
      'To withhold the rulings from the common people',
      'To refer every question to the ruler'], 1),
    ('And what does he say about the side of harshness specifically?',
     ['That it is safer',
      'That it is a DESTROYER — «فَإِنَّهَا مُهْلِكَةٌ تُبَغِّضُ لِلْعَامَّةِ '
      'الدِّين» — it makes the religion hateful to the common people',
      'That it is permitted for scholars',
      'That it is preferable to dissolution'], 1),
])

b += B.tf('nq-l08-tf', [
    ('البُغْضُ المُكَفِّرُ هُوَ بُغْضُ التَّشْرِيعِ لَا بُغْضُ العَمَل.',
     'The bughḍ that nullifies is hatred of the legislating, not dislike of the '
     'act.', True),
    ('مَنْ كَرِهَ الصَّلَاةَ وَهُوَ يُصَلِّي فَلَا شَيْءَ عَلَيْه.',
     'One who hates the prayer while praying has nothing against him.', False),
    ('الكَرَاهَةُ الطَّبِيعِيَّةُ لِلْعَمَلِ لَيْسَتْ مِنَ الكُفْرِ فِي '
     'شَيْء.',
     'Natural dislike of the act is not of disbelief in anything at all.', True),
    ('أَوْجَبَتِ الآيَةُ بُغْضَ جَمِيعِ مَا أَنْزَلَ اللهُ لِيَكُونَ '
     'كُفْرًا.',
     'The verse requires hatred of ALL that Allah sent down for it to be '
     'disbelief.', False),
    ('سَبُّ بَعْضِ الصَّحَابَةِ لِحِقْدٍ عَلَى بَعْضِهِمْ كُفْرٌ أَكْبَر.',
     'Reviling some of the Ṣaḥābah out of rancour toward some is greater '
     'disbelief.', False),
    ('مَنْ تَبَرَّمَ بِقِرَاءَةِ السَّجْدَةِ فِي فَجْرِ الجُمُعَةِ كَافِر.',
     'One wearied by the recitation of al-Sajdah at Jumuʿah fajr is a '
     'disbeliever.', False),
    ('قَالَ المُؤَلِّف: طَرَفُ التَّشَدُّدِ مُهْلِكَةٌ تُبَغِّضُ '
     'لِلْعَامَّةِ الدِّين.',
     'The compiler says the side of harshness is a destroyer that makes the '
     'religion hateful to the common people.', True),
])

b += B.memorize(
    'فَهَذَا لَيْسَ مِنَ الكُفْرِ فِي شَيْء',
    'The footnote, on <strong>natural dislike</strong>. <em>Keep it beside the '
    'matn’s own four words, %s, and you have both halves of the fifth '
    'nullifier in two short phrases.</em> One says: '
    '<strong>the deed does not answer for the heart.</strong> The other says: '
    '<strong>the heart’s heaviness under a hard command is not the thing being '
    'judged.</strong> <em>And beside both keep the compiler’s last sentence, '
    'because it is aimed at whoever teaches this clause: '
    '«فَإِنَّهَا مُهْلِكَةٌ تُبَغِّضُ لِلْعَامَّةِ الدِّين.»</em>'
    % ('«' + ar('وَلَوْ عَمِلَ بِهِ') + '»'))

b += B.nav('nq-l07-mudtarr-wa-tashri.html',
           'النَّاقِضُ الرَّابِع · part 3',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l08')

B.write('nq-l08-bughd-ma-jaa-bihi.html',
        'النَّاقِضُ الخَامِس · بُغْضُ شَيْءٍ مِمَّا جَاءَ بِهِ ﷺ',
        'The Fifth Nullifier — Hating Something of What He Brought',
        'The fifth nullifier, from the words of Shaykh Ibn Bāz: the matn’s '
        '«even if he acts upon it», and the two kinds of bughḍ it forces apart — '
        'hatred of the legislating, which is the nullifier, and natural dislike '
        'of the act, which «is not of disbelief in anything at all»; Ibn Bāz on '
        'one who hates the prayer even while praying; the difference between '
        'natural dislike and compulsion; eight particular questions and the '
        'spread across their answers, three of which are not takfīr; the long '
        'refutation of the claim that only hating the whole religion is '
        'disbelief, with al-Ḥudaybiyah, «accept Islām even if you are averse», '
        'and the conditions of Thaqīf; and the closing warning that harshness '
        'itself makes the religion hateful to people.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ الثَّامِن', '6', b)
print('wrote nq-l08-bughd-ma-jaa-bihi.html')
