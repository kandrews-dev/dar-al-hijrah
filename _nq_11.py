# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 11 — النَّاقِضُ السَّابِع, part 1: حَقِيقَةُ السِّحْر.

Printed folios 159-165 (PDF indices 156-162, offset +3). The seventh nullifier
runs printed **159-193 — thirty-five folios, the longest clause in the book**,
so it takes three lessons:

  * part 1 (this one, 159-165) — what siḥr is, that it is kufr by the naṣṣ,
    the two kinds, the qadar frame, and the shirk mechanism.
  * part 2 (166-175) — حُكْمُ السَّاحِر: the killing and the repentance, the
    athar of ʿUmar, and **the grading of «حَدُّ السَّاحِرِ ضَرْبُهُ
    بِالسَّيْف»**, plus قَلْبُ الأَعْيَان against al-Rāzī.
  * part 3 (176-193) — النُّشْرَة and the treatment, whether the Prophet ﷺ was
    bewitched, Hārūt and Mārūt, and the bewitched against the insane.

What part 1 actually establishes:

  * The lexical work first — Ibn Bāz derives سِحْر from **concealment**
    («يَتَعَاطَوْنَهُ بِطُرُقٍ خَفِيَّة»), and gives the two other uses of the
    root that prove it: سَحَر for the last of the night, and سَحْر for the lung
    inside the body. *The word itself says the thing is hidden.*
  * **Teaching it is kufr, by the wording of the verse** — «وَمَا يُعَلِّمَانِ
    مِنْ أَحَدٍ حَتَّى يَقُولَا إِنَّمَا نَحْنُ فِتْنَةٌ فَلَا تَكْفُرْ» — and
    learning it likewise. The matn's own daleel, read for what its grammar
    does.
  * The **qadar frame**, which is where the clause is theologically anchored:
    «إِلَّا بِإِذْنِ اللهِ» is the **kawnī** permission, not the sharʿī one —
    and Ibn Bāz spells out the difference at length, then grounds it in 54:49
    and 57:22. «رَبُّنَا لَا يُغْلَب، وَلَا يَقَعُ فِي مُلْكِهِ مَا لَا
    يُرِيد.» And his own corollary: that we must **treat Allah's decree with
    His decree** — «يَجِبُ أَنْ نُعَالِجَ قَدَرَ اللهِ بِقَدَرِه» — which is
    why the ḥudūd are established against it rather than the matter left alone.
  * **Why siḥr is shirk and not merely a grave sin**: it cannot be reached
    except by worship of the shayāṭīn — ذَبْح، نَذْر، سُجُود — so «الإِنْسُ
    تَخْدُمُ الجِنَّ» by worship and «الجِنُّ تَخْدُمُ الإِنْسَ» by news and
    by harm. That is the استمتاع of al-Anʿām.
  * The **two kinds**, with the footnote naming them: سِحْرُ التَّخْيِيل and
    سِحْرُ التَّأْثِير. «وَغَالِبُ السِّحْرِ هُوَ التَّخْيِيل» — and the
    footnote on 7:116 asks whether Mūsā عليه السلام was included in «سَحَرُوا
    أَعْيُنَ النَّاس», answering yes for الاسْتِرْهَاب on the proof of
    «فَأَوْجَسَ فِي نَفْسِهِ خِيفَة», and that the تخييل reached him by
    «يُخَيَّلُ إِلَيْه».
  * And the one place the clause turns: **denying that siḥr exists is itself
    kufr** — «مَنْ قَالَهُ فَهُوَ كَافِرٌ مُكَذِّبٌ لِلْقُرْآن» — with
    al-Qurṭubī's distinction between the one who denies it secretly (زِنْدِيق)
    and openly (مُرْتَدّ).

Rule 8: the seven mūbiqāt are given here as «أَخْبَرَ النَّبِيُّ ﷺ» with no
attribution and no grading at this place → the page says so and supplies none.
«مَنْ عَقَدَ عُقْدَةً ثُمَّ نَفَثَ فِيهَا فَقَدْ سَحَر» Ibn Bāz attributes to
al-Nasāʾī from Abū Hurayrah **without a grading** → the page reports the
attribution and supplies no grading.
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


def qa(q, a):
    return ('<div style="margin:0 0 .6rem;padding-right:.8rem;'
            'border-right:2px solid var(--line)">'
            '<p style="margin:0 0 .25rem;font-size:.88rem;color:var(--ink-light)">'
            '<strong>Q —</strong> <em>%s</em></p>'
            '<p style="margin:0;font-size:.93rem"><strong>Ibn Bāz —</strong> %s</p>'
            '</div>' % (q, a))


b = B.objectives([
    'Define %s from the root, and give the two other uses of that root Ibn Bāz '
    'brings as proof.' % ar('السِّحْر'),
    'Show from the wording of al-Baqarah 2:102 that <strong>teaching</strong> '
    'and <strong>learning</strong> it are disbelief.',
    'Distinguish the <strong>kawnī</strong> from the <strong>sharʿī</strong> '
    'permission in %s, and say which one the verse means.'
    % ('«' + ar('إِلَّا بِإِذْنِ اللهِ') + '»'),
    'State Ibn Bāz’s corollary — %s — and what it licenses.'
    % ('«' + ar('نُعَالِجَ قَدَرَ اللهِ بِقَدَرِه') + '»'),
    'Explain <strong>why</strong> siḥr is shirk and not merely a grave sin, and '
    'name the three acts of worship by which the magician reaches it.',
    'Name the <strong>two kinds</strong> of siḥr, say which is the more common, '
    'and give an example of each.',
    'State the ruling on one who says siḥr is a <strong>superstition with no '
    'reality</strong>, and al-Qurṭubī’s distinction within it.',
])

b += B.provenance(159, 165)

b += B.matn(
    'السَّابِع: السِّحْر، وَمِنْهُ الصَّرْفُ وَالعَطْف؛ '
    'فَمَنْ فَعَلَهُ أَوْ رَضِيَ بِهِ كَفَر؛ وَالدَّلِيلُ قَوْلُهُ تَعَالَى: '
    '﴿وَمَا يُعَلِّمَانِ مِنْ أَحَدٍ حَتَّى يَقُولَا إِنَّمَا نَحْنُ '
    'فِتْنَةٌ فَلَا تَكْفُرْ﴾.',
    'Note the matn’s two additions: it names الصَّرْف and العَطْف as kinds of '
    'it, and it makes the clause fall on «فَعَلَهُ <strong>أَوْ رَضِيَ '
    'بِهِ</strong>» — the one who does it, <em>or is pleased with it</em>.')
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><strong>This is the '
        'longest clause in the book — thirty-five folios, printed ١٥٩–١٩٣.</strong> '
        'It takes three lessons, and they divide where the material divides:</p>'
        '<p style="margin:0;font-size:.92rem"><strong>Part 1</strong> (here) — '
        'what siḥr <em>is</em>: the word, the proof that it is disbelief, the '
        'qadar that governs it, and why it is <em>shirk</em> rather than merely a '
        'grave sin.<br>'
        '<strong>Part 2</strong> — the ruling on the magician, the athar of '
        'ʿUmar, and the grading of the ḥadīth everybody quotes for it.<br>'
        '<strong>Part 3</strong> — the treatment, النُّشْرَة, whether the '
        'Prophet ﷺ was bewitched, and Hārūt and Mārūt.</p>',
        wash='var(--accent-wash)', edge='var(--accent)'))

# ---------------------------------------------------------------- the word
b += B.heading('مَا هُوَ السِّحْر', 'The Word, and What It Tells You')
b += B.prose(
    'He begins where the book’s habit is to begin — <strong>with the '
    'word</strong> — and the derivation is not an aside. <em>It is the first '
    'piece of evidence about the thing.</em>')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><em>«<strong>السِّحْر</strong> — '
        'with a kasrah on the sīn — is: what the magicians practise of '
        '<strong>knots</strong>, and of <strong>potions</strong>, and of '
        '<strong>blowing into the knots</strong>, and other than that of what '
        'the masters of this craft practise. <strong>And it was named '
        '<em>siḥr</em> because they practise it by hidden means</strong> — and '
        'for this it was called siḥr. And siḥr is: what bewitches people and '
        'alters their perceptions, by whatever kind — <strong>but in most cases '
        'they are hidden</strong>, and for this it was called siḥr.»</em></p>') +
    p('And then the two proofs from the language itself: <em>«and the last part '
      'of the night is called <strong>%s</strong>, because it occurs at the end '
      'of the night <strong>when people are asleep</strong>; and the lung is '
      'called <strong>%s</strong>, because it is <strong>inside the belly, '
      'within the cavity — hidden</strong>.»</em>'
      % (ar('سَحَر'), ar('سَحْر'))) +
    p('<em>Three words off one root, and all three mean </em>concealed<em>.</em> '
      '<strong>So the hiddenness is not incidental to magic; it is what the '
      'Arabs named it for.</strong> <em>Which also tells you why the subject '
      'attracts so much nonsense, in both directions — the thing is by '
      'definition not on display.</em>'))
b += B.sharh(
    p('He then gives the working description: <em>«so siḥr is '
      '<strong>knots and incantations</strong> which the magicians perform, and '
      'they <strong>blow into their knots</strong>; and things, some of them '
      '<strong>potions</strong> which they gather; and things they '
      '<strong>receive from the jinn and the devils</strong>, until he directs '
      'it into whomever they wish.»</em>') +
    p('<em>Hold the last clause. It is the one that makes this a nullifier and '
      'not a chapter of fiqh:</em> <strong>the operative part is received from '
      'the devils</strong>, and nothing is received from the devils for '
      'nothing.'))

# ---------------------------------------------------------------- kufr by nass
b += B.heading('كُفْرٌ صَرِيحٌ بِنَصِّ القُرْآن', 'Disbelief by the Text — Including Teaching It')
b += B.sharh(
    p('<em>«And it is <strong>plain disbelief by the text of the '
      'Qurʾān</strong>»</em> — and he proves it twice over from one passage. '
      'First from what the verse says of the two who taught it:') +
    box('<p style="margin:0;font-size:.94rem"><em>«…where He said: '
        '«<strong>وَيُعَلِّمُونَ النَّاسَ السِّحْرَ</strong>» — '
        '<strong>so He informed of their disbelief by their teaching people '
        'magic</strong>; <strong>so He made teaching magic one of the deeds of '
        'disbelief</strong>.»</em></p>'))
b += B.ayah(
    'وَمَا يُعَلِّمَانِ مِنْ أَحَدٍ حَتَّىٰ يَقُولَا إِنَّمَا نَحْنُ '
    'فِتْنَةٌ فَلَا تَكْفُرْ',
    'And they did not teach anyone until they had said, “We are only a trial, '
    'so do not disbelieve.”',
    'سُورَةُ البَقَرَة · 2:102')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><strong>Read the grammar of the '
        'daleel, because that is the argument.</strong> The two do not teach a '
        'man <em>until they warn him</em> — and what they warn him of is '
        '<strong>%s</strong>, “do not disbelieve.” <em>The warning names what '
        'the learning amounts to.</em> Ibn Bāz: <em>«so that indicates that '
        '<strong>learning it is disbelief</strong>.»</em></p>'
        '<p style="margin:.5rem 0 0;font-size:.92rem"><em>So the one verse the '
        'matn cites covers both ends of the transaction — the teacher by '
        '«وَيُعَلِّمُونَ النَّاسَ السِّحْر», and the student by «فَلَا '
        'تَكْفُر».</em></p>' % ar('فَلَا تَكْفُرْ')))
b += B.prose(
    'He then walks the rest of the passage, and each clause adds something. '
    '<em>«%s»</em> — <strong>they learn what harms them and does not benefit '
    'them</strong>: <em>«so the harm is immense.»</em> '
    '<em>«%s»</em> — <strong>and they certainly knew that whoever purchased it '
    'would have no share in the Hereafter</strong>: <em>«meaning — no portion '
    'and no share.»</em>'
    % (ar('وَيَتَعَلَّمُونَ مَا يَضُرُّهُمْ وَلَا يَنْفَعُهُمْ'),
       ar('وَلَقَدْ عَلِمُوا لَمَنِ اشْتَرَاهُ مَا لَهُ فِي الآخِرَةِ مِنْ '
          'خَلَاقٍ')))
b += B.ayah(
    'وَلَوْ أَنَّهُمْ آمَنُوا وَاتَّقَوْا لَمَثُوبَةٌ مِّنْ عِندِ اللَّهِ '
    'خَيْرٌ لَّوْ كَانُوا يَعْلَمُونَ',
    'And if they had believed and been mindful of Allah, a reward from Allah '
    'would have been better — if only they knew.',
    'سُورَةُ البَقَرَة · 2:103')
b += B.sharh(
    p('<strong>And that verse is the one he builds the structural point on:</strong> '
      '<em>«so it indicates that it is <strong>the opposite of faith and the '
      'opposite of taqwā</strong>.»</em>') +
    p('<em>Notice the form of the inference.</em> The verse sets '
      '«<strong>if they had believed and been mindful</strong>» against what '
      'they were in fact doing. <strong>A thing set in opposition to īmān in the '
      'Qurʾān’s own construction is not a lesser sin inside īmān.</strong> '
      '<em>That is a cleaner argument than any assertion, and it is the reason '
      'this clause sits among the ten.</em>'))

# ---------------------------------------------------------------- qadar
b += B.heading('إِلَّا بِإِذْنِ اللهِ', 'The Qadar Frame — Which Permission?')
b += B.prose(
    '<strong>This is the part of the clause that is actually ʿaqīdah, and the '
    'sharḥ gives it more room than anything else on these folios.</strong> '
    '<em>The verse says the magicians harm no one «except by Allah’s '
    'permission» — and the whole question is which permission that is.</em>')
b += B.ayah(
    'وَمَا هُم بِضَارِّينَ بِهِ مِنْ أَحَدٍ إِلَّا بِإِذْنِ اللَّهِ',
    'And they could not harm anyone by it except by the permission of Allah.',
    'سُورَةُ البَقَرَة · 2:102')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><em>«<strong>Meaning: by His '
        'kawnī, decreed permission — not by His legislative '
        'permission.</strong> For the Sharīʿah <strong>forbids</strong> them '
        'that and <strong>makes it unlawful</strong> upon them. But by the '
        '<strong>decreed</strong> permission, by which Allah’s knowledge and His '
        'prior decree have passed — that magic occurs from so-and-so, and occurs '
        'from such a woman, and befalls so-and-so and such a woman; just as His '
        'decree passed that so-and-so is afflicted with a killing, or afflicted '
        'with such an illness, and dies in such a land, and is provided such, '
        'and becomes rich or becomes poor — <strong>and all of it is by the will '
        'of Allah and His decree</strong>.»</em></p>'))
b += B.sharh(table([
    thead3('', 'الإِذْنُ الكَوْنِيُّ القَدَرِيّ', 'الإِذْنُ الشَّرْعِيّ'),
    row3('<strong>what it is</strong>',
         'That Allah <strong>allowed it to occur</strong> — it fell within His '
         'knowledge and decree',
         'That Allah <strong>permitted it in His law</strong>'),
    row3('<strong>does siḥr have it?</strong>',
         '<strong>Yes</strong> — nothing occurs without it',
         '<strong>No</strong> — «the Sharīʿah forbids them that and makes it '
         'unlawful upon them»'),
    row3('<strong>what follows</strong>',
         'No harm reaches anyone outside Allah’s decree — <em>«so whoever Allah '
         'wills be harmed by that, the harm reaches him»</em>',
         'The magician is a criminal, and the ḥudūd are established against him'),
]) + p('<strong>Confusing those two is the single commonest error on this '
       'subject, in both directions.</strong> <em>One man reasons: if it only '
       'happens by Allah’s permission, who am I to resist it — and becomes '
       'passive. Another reasons: it is forbidden, so it cannot really touch me '
       '— and denies the decree. The distinction answers both at once.</em>'))
b += B.ayah(
    'إِنَّا كُلَّ شَيْءٍ خَلَقْنَاهُ بِقَدَرٍ',
    'Indeed, We have created everything by measure.',
    'سُورَةُ القَمَر · 54:49')
b += B.ayah(
    'مَا أَصَابَ مِن مُّصِيبَةٍ فِي الْأَرْضِ وَلَا فِي أَنفُسِكُمْ إِلَّا '
    'فِي كِتَابٍ مِّن قَبْلِ أَن نَّبْرَأَهَا إِنَّ ذَٰلِكَ عَلَى اللَّهِ '
    'يَسِيرٌ',
    'No affliction befalls in the earth or in yourselves but that it is in a '
    'Book before We bring it into being. Indeed, that is easy for Allah.',
    'سُورَةُ الحَدِيد · 57:22')
b += B.sharh(
    p('And the conclusion he draws from those two verses is aimed at the heart, '
      'not the intellect:') +
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><em>«So these evils that '
        'may occur from the magicians and from others <strong>do not occur out '
        'of ignorance on the part of our Lord</strong> — for He is the Knower of '
        'all things; <strong>nothing hidden is hidden from Him</strong>.»</em></p>'
        '<p style="margin:0;font-size:.95rem"><em>«<strong>For our Lord is not '
        'overcome, and there does not occur in His dominion what He does not '
        'will</strong> — rather nothing occurs in this world nor in the '
        'Hereafter except by a prior decree, for a far-reaching wisdom which He '
        'has willed. So these may be tried with magic, and these tried with '
        'illness, and these tried with killing, and other than that — '
        '<strong>and to Allah belongs the far-reaching wisdom in what He '
        'decrees and ordains</strong>.»</em></p>'))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><strong>And then the '
        'corollary, which is the practical half and which people drop.</strong></p>'
        '<p style="margin:0;font-size:.94rem"><em>«And even if these things '
        'occur by the will of Allah and His decree, '
        '<strong>it is obligatory that we treat Allah’s decree with His '
        'decree</strong>; and it is obligatory that we <strong>war against all '
        'shirk and all acts of disobedience</strong> — while knowing that none '
        'of it occurs except by His will. <strong>But He has legislated for us '
        'that we war against them, and that we refrain from them, and that the '
        'legislated ḥudūd be established concerning them.</strong>»</em></p>'
        '<p style="margin:.5rem 0 0;font-size:.92rem"><em>«نُعَالِجَ قَدَرَ '
        'اللهِ بِقَدَرِه» is a rule far beyond this clause — it is the answer '
        'to fatalism about illness, about poverty, about sin and about harm. '
        '<strong>The decree is not an argument against acting; acting is part of '
        'the decree.</strong></em></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))

# ---------------------------------------------------------------- shirk
b += B.heading('لِمَاذَا كَانَ السِّحْرُ شِرْكًا', 'Why It Is Shirk, Not Merely a Grave Sin')
b += B.prose(
    '<strong>Here is the hinge of the whole clause.</strong> <em>Magic is not '
    'ranked with the gravest sins because of the harm it does — plenty of sins '
    'do harm. It is ranked there because of what it is reached '
    '<strong>by</strong>.</em>')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><em>«And that is only because they '
        '<strong>attain their magic by worship of the devils</strong>, and '
        '<strong>drawing near to them</strong> by what they desire of '
        '<strong>slaughter and vows and prostration</strong> and other than '
        'that; so the magicians <strong>draw near to the devils by worshipping '
        'them besides Allah</strong>, and they assist them in what they want of '
        'harming people, for the gain of this world.»</em></p>') +
    p('<strong>So the shirk is not a by-product. It is the price.</strong> '
      '<em>The three acts he names — %s, %s, %s — are three acts of worship, '
      'and the first two are the subject of the second nullifier and the third '
      'of the first. This clause is built on top of those.</em>'
      % (ar('ذَبْح'), ar('نَذْر'), ar('سُجُود'))))
b += B.sharh(
    p('And he states the exchange in both directions, which is the clearest '
      'description of the trade on these folios:') +
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><em>«<strong>So the jinn '
        'serve mankind, and mankind serve the jinn.</strong>»</em></p>'
        '<p style="margin:0;font-size:.93rem"><em>«The jinn serve mankind by '
        '<strong>informing them of some events</strong> in near and far lands, '
        'and <strong>aiding them in wronging people</strong>. And mankind serve '
        'the jinn by <strong>worshipping them besides Allah</strong>, and '
        '<strong>supplicating them</strong>, and <strong>vowing to them</strong>, '
        'and <strong>slaughtering for them</strong>, and the like of that — '
        '<strong>and this is the mutual enjoyment of one another</strong>.»</em></p>') +
    p('<em>The last phrase is a Qurʾānic one, and he uses it deliberately.</em> '
      '<strong>Note what the human side of the bargain costs and what it '
      'buys:</strong> he gives away <em>worship</em> and receives '
      '<em>information and the power to wrong people</em>. <em>Which is the '
      'worst exchange described anywhere in the ten clauses.</em>'))
b += B.hadith(
    'اجْتَنِبُوا السَّبْعَ المُوبِقَات. قُلْنَا: وَمَا هُنَّ يَا رَسُولَ '
    'اللهِ؟ قَال: الشِّرْكُ بِاللهِ، وَالسِّحْر، وَقَتْلُ النَّفْسِ '
    'الَّتِي حَرَّمَ اللهُ إِلَّا بِالحَقّ، وَأَكْلُ الرِّبَا، وَأَكْلُ '
    'مَالِ اليَتِيم، وَالتَّوَلِّي يَوْمَ الزَّحْف، وَقَذْفُ '
    'المُحْصَنَاتِ الغَافِلَاتِ المُؤْمِنَات.',
    '“Avoid the seven destructive sins.” We said: and what are they, Messenger '
    'of Allah? He said: associating partners with Allah; magic; killing the '
    'soul Allah has made inviolable, except by right; consuming ribā; consuming '
    'the property of the orphan; turning away on the day of battle; and slander '
    'of chaste, unsuspecting believing women.',
    'يُورِدُهُ الشَّيْخُ بِقَوْلِهِ «أَخْبَرَ النَّبِيُّ ﷺ» · the sharḥ gives '
    'neither an attribution nor a grading at this place, so none is supplied here')
b += B.sharh(
    p('<strong>And look at where siḥr sits in that list.</strong> Ibn Bāz says '
      'it himself: <em>«so the greatest of them is <strong>shirk with '
      'Allah</strong>, then <strong>magic</strong> — and magic is '
      '<strong>of</strong> shirk, because it is not attained except by worship '
      'of the devils and drawing near to them by whom they are pleased with and '
      'by what they desire of slaughter and vows and prostration and other than '
      'that.»</em>') +
    p('<em>Second in the list of seven, and immediately after shirk itself — and '
      'then he says the second is a species of the first.</em>') +
    p('The footnote adds a ḥadīth that states the equation outright: '
      '<em>«And al-Nasāʾī has from Abū Hurayrah رَضِيَ اللهُ عَنْه from the '
      'Prophet ﷺ that he said: <strong>«مَنْ عَقَدَ عُقْدَةً ثُمَّ نَفَثَ '
      'فِيهَا فَقَدْ سَحَر، وَمَنْ سَحَرَ فَقَدْ أَشْرَك»</strong> — whoever '
      'ties a knot and then blows into it has performed magic, and whoever has '
      'performed magic has committed shirk. And this indicates that magic is '
      'shirk with Allah; and that is because it is not attained except by '
      'worship of the jinn and drawing near to them.»</em> '
      '<strong>Ibn Bāz names al-Nasāʾī and Abū Hurayrah but gives no grading at '
      'this place, so this page reports the attribution and supplies no '
      'grading.</strong>'))

# ---------------------------------------------------------------- two kinds
b += B.heading('سِحْرُ التَّخْيِيلِ وَسِحْرُ التَّأْثِير', 'Two Kinds — and the Common One')
b += B.prose(
    'The footnote names them: <strong>%s</strong> and <strong>%s</strong>. '
    '<em>And Ibn Bāz is careful about the difference, because the first is an '
    'effect on the <strong>eye of the beholder</strong> and the second is a real '
    'effect in the world.</em>'
    % (ar('سِحْرُ التَّخْيِيل'), ar('سِحْرُ التَّأْثِير')))
b += B.sharh(table([
    thead3('', 'سِحْرُ التَّخْيِيل', 'سِحْرُ التَّأْثِير'),
    row3('<strong>what happens</strong>',
         'The thing is seen <strong>other than as it is</strong> — '
         '<em>«they alter the appearances in people’s eyes»</em>; the rope is '
         'seen as a snake, a man as a donkey or an ape, a dog as a goat and a '
         'goat as a dog',
         'A <strong>real effect</strong> — <em>«this is other than mere '
         'imagining; rather it is something that <strong>has an '
         'effect</strong>»</em>: «<em>فَيَحْصُلُ بِهِ تَأْثِيرٌ عَلَى '
         'الزَّوْجِ فِي المَحَبَّةِ وَالبَغْضَاء</em>»'),
    row3('<strong>its daleel</strong>',
         '«<em>%s</em>» — <strong>it is made to SEEM to him</strong>, Ṭā Hā '
         '20:66; and «<em>سَحَرُوا أَعْيُنَ النَّاس</em>», al-Aʿrāf 7:116'
         % ar('يُخَيَّلُ إِلَيْهِ مِنْ سِحْرِهِمْ أَنَّهَا تَسْعَى'),
         '«<em>%s</em>» — what they separate a man and his wife with, '
         'al-Baqarah 2:102'
         % ar('مَا يُفَرِّقُونَ بِهِ بَيْنَ المَرْءِ وَزَوْجِهِ')),
    row3('<strong>how common</strong>',
         '<strong>«وَغَالِبُ السِّحْرِ هُوَ التَّخْيِيل»</strong> — most of it',
         'Real, and he says plainly that among its kinds are '
         '«<em>أَنْوَاعٌ مِنَ السِّحْرِ لَهَا أَثَرٌ وَلَهَا وُجُود</em>»'),
]))
b += B.ayah(
    'فَإِذَا حِبَالُهُمْ وَعِصِيُّهُمْ يُخَيَّلُ إِلَيْهِ مِن سِحْرِهِمْ '
    'أَنَّهَا تَسْعَىٰ',
    'And at once their ropes and staffs were made to seem to him, by their '
    'magic, to be moving.',
    'سُورَةُ طَه · 20:66')
b += B.sharh(
    p('He gives the examples at length, and they are worth having because they '
      'are the shapes the thing actually takes: <em>a rope or a staff seen as a '
      'snake walking; birds or snakes or scorpions apparently brought out of the '
      'mouth or the belly — <strong>«وَلَيْسَ لَهُ حَقِيقَة، كُلُّهُ '
      'تَخْيِيل»</strong>; and a man shown his wife’s form as ugly until he '
      'hates her, or she shown his form as ugly when he comes to her until she '
      'hates him</em> — and he adds the detail that it is her husband seen '
      '<em>black after having been white</em>, or seen <em>ill</em>. '
      '<strong>«فَعِنْدَ ذَلِكَ تَقَعُ البَغْضَاءُ وَالعَدَاوَةُ '
      'وَالفُرْقَة.»</strong>') +
    p('<em>And he gives the mechanism of the second kind as the first kind’s '
      'consequence:</em> <strong>«وَلَعَلَّ أَسْبَابَ التَّأْثِيرِ أَنَّ '
      'السِّحْرَ يُخَيِّلُ إِلَى الرَّجُلِ قَبَاحَةَ الزَّوْجَة»</strong> — '
      '<em>perhaps</em> the causes of the effect are that the magic makes the '
      'wife’s ugliness seem to the man. <em>Note the «perhaps». He is explaining '
      'a mechanism, not asserting one, and he marks it as such.</em>'))
b += B.sharh(
    p('He also explains the <strong>onlookers</strong>, which is where stage '
      'conjuring and real magic get confused: <em>«and the magician '
      '<strong>bewitches the onlookers</strong> who witness his work; and there '
      'may be there <strong>one who assists him whom the onlookers do not '
      'see</strong>, of the devils who help him — <strong>for they see us and we '
      'do not see them</strong>… and it may be the magic of the eye by what he '
      'has done of sleight, like one who brings out of his pocket or his mouth a '
      'bird or an egg or other than that <strong>in the eyes of people — and the '
      'matter is otherwise</strong>.»</em>') +
    p('<em>And the heavy loads dragged «by a hair or two» are explained the same '
      'way:</em> <strong>«مِمَّا سَاعَدَهُ فِيهِ الشَّيَاطِين، وَهُمْ لَا '
      'يُرَوْن»</strong> — <em>the devils are pulling, unseen.</em> '
      '<strong>Which is the point: what looks like a power in the man is a '
      'service rendered by something he has paid for in worship.</strong>'))
b += B.ayah(
    'فَلَمَّا أَلْقَوْا سَحَرُوا أَعْيُنَ النَّاسِ وَاسْتَرْهَبُوهُمْ '
    'وَجَاءُوا بِسِحْرٍ عَظِيمٍ',
    'And when they threw, they bewitched the eyes of the people and overawed '
    'them, and they produced a great magic.',
    'سُورَةُ الأَعْرَاف · 7:116')
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.93rem"><strong>The footnote asks '
        'a question worth the asking:</strong> does Allah’s prophet Mūsā عَلَيْهِ '
        'السَّلَام fall under the general «they bewitched the eyes of the '
        'people and overawed them»?</p>'
        '<p style="margin:0;font-size:.93rem"><em>«As for “and overawed them” — '
        '<strong>yes</strong>, by the proof of His saying '
        '«<strong>فَأَوْجَسَ فِي نَفْسِهِ خِيفَة</strong>» [he conceived fear '
        'within himself]. And as for “they bewitched the eyes of the people” — '
        '<strong>it was made to seem to Mūsā, by reason of their magic, that '
        'they were great snakes; and had it not been for that he would not have '
        'feared</strong>, and His saying «<strong>يُخَيَّلُ '
        'إِلَيْهِ</strong>» — i.e. to Mūsā — indicates it; and that is of the '
        'magic of the eye.»</em></p>'
        '<p style="margin:.5rem 0 0;font-size:.91rem;color:var(--ink-light)">'
        '<em>This is also the compiler’s proof for Ibn Bāz’s sentence '
        '«the magician bewitches the onlookers».</em></p>'))
b += B.prose(
    '<strong>And the sharḥ does not leave Pharaoh’s magicians where it found '
    'them.</strong> <em>It follows them to the end of the story, and the end of '
    'the story is the only place in this entire clause where magicians come out '
    'well.</em> When Mūsā threw his staff, <em>«it swallowed up these ropes and '
    'staffs; and when the magicians saw it they believed, and fell down '
    'prostrate, believing in what Mūsā brought — and when Pharaoh threatened '
    'them <strong>they paid him no heed</strong>.»</em>')
b += B.ayah(
    'قَالُوا لَن نُّؤْثِرَكَ عَلَىٰ مَا جَاءَنَا مِنَ الْبَيِّنَاتِ '
    'وَالَّذِي فَطَرَنَا فَاقْضِ مَا أَنتَ قَاضٍ',
    'They said: we will never prefer you over what has come to us of clear '
    'proofs, and over Him who created us — so decree whatever you will decree.',
    'سُورَةُ طَه · 20:72')
b += B.ayah(
    'إِنَّا آمَنَّا بِرَبِّنَا لِيَغْفِرَ لَنَا خَطَايَانَا وَمَا '
    'أَكْرَهْتَنَا عَلَيْهِ مِنَ السِّحْرِ وَاللَّهُ خَيْرٌ وَأَبْقَىٰ',
    'Indeed, we have believed in our Lord, that He may forgive us our sins and '
    'the magic to which you compelled us. And Allah is better and more '
    'enduring.',
    'سُورَةُ طَه · 20:73')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><strong>They were magicians in the '
        'morning and martyrs by the evening.</strong> <em>And the thing they ask '
        'forgiveness for by name is «<strong>the magic to which you compelled '
        'us</strong>» — so the clause that makes magic a nullifier of Islām also '
        'preserves, in the Qurʾān’s own words, the case of magicians who '
        'repented and were accepted.</em></p>'
        '<p style="margin:.5rem 0 0;font-size:.92rem"><strong>Keep that for part '
        '2</strong>, where the question of the magician’s repentance is answered '
        'at length — and where the answer turns out to depend entirely on '
        '<em>whether he came of his own accord or was seized</em>.</p>',
        wash='var(--accent-wash)', edge='var(--accent)'))

# ---------------------------------------------------------------- al-sarf
b += B.heading('الصَّرْفُ وَالعَطْف', 'What the Matn Named Alongside It')
b += B.sharh(
    p('The matn singled out two kinds, and the sharḥ places them among the '
      'magician’s trade:') +
    box('<p style="margin:0;font-size:.94rem"><em>«And of their wicked deeds: '
        '<strong>الصَّرْف</strong> [turning a man away from what he desires — '
        'as from his wife], and <strong>العَطْف</strong> [bending him toward '
        'what he does not], and <strong>separating between the two spouses and '
        'between relatives</strong> by what they do of the deeds of magic and '
        'its kinds, which harms everyone; and it makes this one hateful to that '
        'one and that one to this — <strong>from what they receive from the jinn '
        'and the devils and serve them by</strong>.»</em></p>') +
    p('<em>Which is why the matn named them: they are the forms of the thing '
      'that reach ordinary households.</em> <strong>And both are instances of '
      '«مَا يُفَرِّقُونَ بِهِ بَيْنَ المَرْءِ وَزَوْجِهِ» — the verse’s own '
      'example.</strong>'))

# ---------------------------------------------------------------- khurafah
b += B.heading('مَنْ قَالَ إِنَّ السِّحْرَ خُرَافَة', 'Denying It Is Itself Disbelief')
b += B.sharh(
    qa('A man says: <strong>magic is a superstition and has no '
       'reality.</strong>',
       '<em>«<strong>Whoever says it is a disbeliever</strong> — because Allah '
       'mentioned magic in the Qurʾān and the Messenger ﷺ explained it. '
       '<strong>So magic exists, and it has a reality</strong>: some of it '
       'exists in reality — <strong>it sickens and it kills</strong> — and some '
       'of it is imagining; <strong>and all of it occurs. Whoever denies it is a '
       'disbeliever, denying the Qurʾān.</strong>»</em>') +
    p('<strong>So the clause cuts in two directions at once, and that is '
      'unusual.</strong> <em>The magician is a disbeliever for practising it. '
      'The modern man is a disbeliever for saying it is not real.</em> '
      '<strong>Both rulings rest on the same thing — the text of the Qurʾān — '
      'and that is why both are in this clause.</strong>'))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.93rem"><strong>And the compiler '
        'adds al-Qurṭubī, who draws a distinction inside the denial:</strong></p>'
        '<p style="margin:0;font-size:.93rem"><em>«The Qurʾān has indicated, in '
        'more than one verse, and the Sunnah in more than one ḥadīth, that magic '
        '<strong>exists and has an effect on the one bewitched</strong>; so '
        'whoever denies that is a <strong>disbeliever, denying Allah and His '
        'Messenger ﷺ</strong>, and a denier of what is known by direct '
        'observation. Then: the denier of magic — <strong>if he denies it '
        'secretly, he is a zindīq</strong>; <strong>and if he denies it openly, '
        'he is an apostate</strong>.»</em></p>'
        '<p style="margin:.5rem 0 0;font-size:.91rem;color:var(--ink-light)">'
        '<em>Reported by the compiler by way of al-Ubbī’s commentary on Ṣaḥīḥ '
        'Muslim.</em></p>'))
b += B.prose(
    '<strong>Part 2 takes printed folios ١٦٦–١٧٥</strong> — the ruling on the '
    'magician himself: the killing and who carries it out, whether his '
    'repentance is accepted and when, the athar of ʿUmar and of Ḥafṣah and of '
    'Jundub, <strong>and the grading of the one ḥadīth everyone quotes for the '
    'ḥadd</strong> — which the compiler works through at length and does not '
    'leave standing. With it, Ibn Bāz’s refutation of al-Rāzī on whether a '
    'magician can turn a man into a donkey.')

b += B.vocab([
    ('السِّحْر', 'al-siḥr', 'magic',
     'Knots, incantations, potions, and what is received from the jinn. Named '
     'for CONCEALMENT — «لِأَنَّهُمْ يَتَعَاطَوْنَهُ بِطُرُقٍ خَفِيَّة»; and '
     'the root’s other uses prove it (سَحَر for the last of the night, سَحْر '
     'for the lung).'),
    ('الصَّرْف', 'al-ṣarf', 'turning away',
     'Named in the matn. Turning a man from what he desires — as from his wife '
     '— by magic.'),
    ('العَطْف', 'al-ʿaṭf', 'bending toward',
     'Named in the matn beside الصَّرْف: bending a person toward what he would '
     'not otherwise incline to. Both are instances of «مَا يُفَرِّقُونَ بِهِ '
     'بَيْنَ المَرْءِ وَزَوْجِهِ».'),
    ('الإِذْنُ الكَوْنِيّ', 'al-idhn al-kawnī', 'the decreed permission',
     'What «إِلَّا بِإِذْنِ اللهِ» means in 2:102 — that Allah allowed it to '
     'OCCUR. NOT the sharʿī permission: «فَالشَّرْعُ يَمْنَعُهُمْ مِنْ ذَلِكَ '
     'وَيُحَرِّمُهُ عَلَيْهِم».'),
    ('نُعَالِجُ قَدَرَ اللهِ بِقَدَرِه', 'nuʿāliju qadar Allāh bi-qadarih',
     'we treat Allah’s decree with His decree',
     'Ibn Bāz’s corollary, and far bigger than this clause: the decree is no '
     'argument against acting — «وَلَكِنَّهُ شَرَعَ لَنَا أَنْ '
     'نُحَارِبَهَا».'),
    ('سِحْرُ التَّخْيِيل', 'siḥr al-takhyīl', 'the magic of seeming',
     'An effect on the eye of the beholder — the rope seen as a snake. '
     '«وَغَالِبُ السِّحْرِ هُوَ التَّخْيِيل.»'),
    ('سِحْرُ التَّأْثِير', 'siḥr al-taʾthīr', 'the magic of effect',
     'A real effect, not mere seeming — love and hatred between spouses. '
     '«بَلْ شَيْءٌ يُؤَثِّر.»'),
    ('المُوبِقَات', 'al-mūbiqāt', 'the destructive sins',
     'The seven. Siḥr is the SECOND, right after shirk — and Ibn Bāz then says '
     'the second is a species of the first: «وَالسِّحْرُ مِنَ الشِّرْك».'),
    ('خُرَافَة', 'khurāfah', 'a superstition',
     'What the modern denier calls it. Ibn Bāz: «مَنْ قَالَهُ فَهُوَ كَافِرٌ '
     'مُكَذِّبٌ لِلْقُرْآن» — and al-Qurṭubī: secretly a zindīq, openly an '
     'apostate.'),
])

b += B.mcq('nq-l11-mcq', [
    ('The matn makes the clause fall on whom?',
     ['The one who does it only',
      'The one who does it OR is pleased with it — «فَمَنْ فَعَلَهُ أَوْ '
      'رَضِيَ بِهِ كَفَر»',
      'The one who teaches it only',
      'The one who seeks it out'], 1),
    ('Why, according to Ibn Bāz, was it named سِحْر?',
     ['Because it deceives the weak',
      'Because they practise it by HIDDEN means — «بِطُرُقٍ خَفِيَّة»',
      'Because it comes from the Chaldeans',
      'Because it is forbidden'], 1),
    ('Which two uses of the root does he give as proof of that?',
     ['سَاحِر and مَسْحُور',
      'سَحَر for the last of the night, because it comes when people are '
      'asleep; and سَحْر for the lung, because it is inside the body — hidden',
      'سُحُور and سَحَر',
      'سَاحِرَة and سِحْرِيَّة'], 1),
    ('What does the sharḥ say siḥr consists of?',
     ['Words alone',
      'Knots, incantations blown into the knots, potions they gather, and things '
      'they RECEIVE FROM the jinn and the devils',
      'Sleight of hand only',
      'Astrological calculation'], 1),
    ('From which words of al-Baqarah 2:102 does he argue that TEACHING it is '
     'disbelief?',
     ['«إِلَّا بِإِذْنِ اللهِ»',
      '«وَيُعَلِّمُونَ النَّاسَ السِّحْرَ» — «so He informed of their disbelief '
      'by their teaching people magic»',
      '«مَا يَضُرُّهُمْ وَلَا يَنْفَعُهُمْ»',
      '«مَا لَهُ فِي الآخِرَةِ مِنْ خَلَاقٍ»'], 1),
    ('And that LEARNING it is disbelief?',
     ['From the ḥadīth of the seven',
      'From the daleel itself — the two do not teach anyone until they say «we '
      'are only a trial, SO DO NOT DISBELIEVE»; the warning names what the '
      'learning amounts to',
      'From al-Baqarah 2:103',
      'From the athar of ʿUmar'], 1),
    ('What does Ibn Bāz infer from «وَلَوْ أَنَّهُمْ آمَنُوا وَاتَّقَوْا»?',
     ['That they may yet repent',
      'That magic is the OPPOSITE of faith and the opposite of taqwā — a thing '
      'the Qurʾān sets in opposition to īmān',
      'That their deeds are merely deficient',
      'That the reward is better than the gain'], 1),
    ('«إِلَّا بِإِذْنِ اللهِ» — which permission?',
     ['The legislative permission',
      'The KAWNĪ, decreed permission — «not by His legislative permission; for '
      'the Sharīʿah forbids them that and makes it unlawful upon them»',
      'Both equally',
      'The permission of the one in authority'], 1),
    ('What error does that distinction prevent?',
     ['Only the error of denying magic',
      'Two at once — the passivity of «it only happens by Allah’s permission, so '
      'who am I to resist», and the denial of «it is forbidden, so it cannot '
      'touch me»',
      'The error of seeking treatment',
      'The error of fearing the magician'], 1),
    ('Which two verses does he ground the qadar in?',
     ['al-Baqarah 2:102 and 2:103',
      'al-Qamar 54:49 «إِنَّا كُلَّ شَيْءٍ خَلَقْنَاهُ بِقَدَرٍ» and al-Ḥadīd '
      '57:22',
      'Ṭā Hā 20:66 and al-Aʿrāf 7:116',
      'al-Shūrā 42:25 and al-Anʿām 6:128'], 1),
    ('«فَرَبُّنَا — جَلَّ وَعَلَا — لَا يُغْلَب، وَلَا يَقَعُ فِي مُلْكِهِ…»',
     ['«…إِلَّا مَا يُرِيدُ الشَّيْطَان»',
      '«…مَا لَا يُرِيد»',
      '«…شَيْءٌ مِنَ السِّحْر»',
      '«…إِلَّا الخَيْر»'], 1),
    ('What is Ibn Bāz’s practical corollary to all of that?',
     ['That the matter is left to Allah',
      'That «it is obligatory that we TREAT ALLAH’S DECREE WITH HIS DECREE» — '
      'warring against shirk and sin, and establishing the legislated ḥudūd, '
      'while knowing none of it occurs but by His will',
      'That supplication alone suffices',
      'That the magician is to be left to his fate'], 1),
    ('Why is siḥr shirk rather than merely a grave sin?',
     ['Because of the harm it causes',
      'Because it is not attained except by WORSHIP of the devils and drawing '
      'near to them — by slaughter, vows and prostration',
      'Because it involves lying',
      'Because the scholars agreed to call it so'], 1),
    ('Which three acts of worship does he name as the magician’s price?',
     ['Prayer, fasting, charity',
      'ذَبْح, نَذْر, سُجُود — slaughter, vows and prostration',
      'Supplication, reliance, fear',
      'Oath, vow, sacrifice of hair'], 1),
    ('In the mutual exchange he describes, what do the jinn give and what do '
     'men give?',
     ['Men give wealth; jinn give knowledge',
      'The jinn inform men of events in near and far lands and aid them in '
      'wronging people; men worship the jinn besides Allah, supplicate them, vow '
      'to them and slaughter for them',
      'Men give obedience; jinn give protection',
      'Neither gives anything; it is coercion'], 1),
    ('Where does siḥr sit in the seven destructive sins?',
     ['Last',
      'Second — immediately after shirk with Allah; and he then says «magic is '
      'OF shirk»',
      'Fourth, after ribā',
      'It is not among them'], 1),
    ('What does this page supply for the ḥadīth of the seven mūbiqāt?',
     ['An attribution to al-Bukhārī and Muslim with a grading of ṣaḥīḥ',
      'Nothing — the sharḥ gives it here with neither an attribution nor a '
      'grading, so the page says so and supplies none',
      'A grading of ḥasan',
      'An attribution to al-Nasāʾī'], 1),
    ('«مَنْ عَقَدَ عُقْدَةً ثُمَّ نَفَثَ فِيهَا فَقَدْ سَحَر، وَمَنْ سَحَرَ '
     'فَقَدْ…»',
     ['«…ظَلَم»', '«…أَشْرَك»', '«…فَسَق»', '«…كَذَب»'], 1),
    ('And what does the page supply for THAT one?',
     ['A grading of ṣaḥīḥ',
      'The attribution Ibn Bāz gives — al-Nasāʾī, from Abū Hurayrah — and NO '
      'grading, because he gives none at this place',
      'Nothing at all',
      'A grading of ḍaʿīf'], 1),
    ('Name the two kinds of siḥr as the footnote names them.',
     ['Lesser and greater',
      'سِحْرُ التَّخْيِيل — the magic of seeming — and سِحْرُ التَّأْثِير — the '
      'magic of real effect',
      'Of the jinn and of men',
      'Of the eye and of the tongue'], 1),
    ('Which is the more common?',
     ['The magic of effect',
      'التَّخْيِيل — «وَغَالِبُ السِّحْرِ هُوَ التَّخْيِيل»',
      'They are equal',
      'He does not say'], 1),
    ('Which verse is the daleel for the magic of seeming?',
     ['al-Baqarah 2:102',
      'Ṭā Hā 20:66 — «يُخَيَّلُ إِلَيْهِ مِنْ سِحْرِهِمْ أَنَّهَا تَسْعَى» — '
      'and with it al-Aʿrāf 7:116 «سَحَرُوا أَعْيُنَ النَّاس»',
      'al-Qamar 54:49',
      'Ṭā Hā 20:73'], 1),
    ('And for the magic of real effect?',
     ['al-Aʿrāf 7:116',
      'al-Baqarah 2:102 — «مَا يُفَرِّقُونَ بِهِ بَيْنَ المَرْءِ وَزَوْجِهِ»; '
      '«فَيَحْصُلُ بِهِ تَأْثِيرٌ عَلَى الزَّوْجِ فِي المَحَبَّةِ '
      'وَالبَغْضَاء»',
      'Ṭā Hā 20:72',
      'al-Ḥadīd 57:22'], 1),
    ('When Ibn Bāz explains HOW the second kind takes effect, how does he mark '
     'the explanation?',
     ['As certain',
      'With «وَلَعَلَّ» — «and PERHAPS the causes of the effect are that the '
      'magic makes the wife’s ugliness seem to the man»',
      'As a consensus',
      'As a transmitted report'], 1),
    ('How does he explain the onlookers at a magician’s display?',
     ['They are hypnotised by his gaze',
      'The magician bewitches the onlookers; and there may be one assisting him '
      'whom they do not see, of the devils — «for they see us and we do not see '
      'them»',
      'They agree beforehand to pretend',
      'They are affected by the drink served'], 1),
    ('And the heavy loads dragged «by a hair or two»?',
     ['Real strength granted to the magician',
      'The devils are helping him pull, and they are not seen',
      'An illusion of the eye only',
      'A trick of leverage'], 1),
    ('The footnote asks whether Mūsā عَلَيْهِ السَّلَام was included in «they '
     'bewitched the eyes of the people and overawed them». The answer?',
     ['No, in neither respect',
      'Yes as to the overawing — by «فَأَوْجَسَ فِي نَفْسِهِ خِيفَة»; and the '
      'seeming reached him too, by «يُخَيَّلُ إِلَيْهِ», «and had it not been '
      'for that he would not have feared»',
      'Yes as to the bewitching only',
      'The footnote leaves it open'], 1),
    ('How does the sharḥ follow Pharaoh’s magicians to the end of their story?',
     ['It does not mention them further',
      'They believed and fell prostrate, and when Pharaoh threatened them they '
      'paid him no heed — «فَاقْضِ مَا أَنْتَ قَاضٍ»',
      'They were killed before believing',
      'They fled Egypt'], 1),
    ('And what do they ask forgiveness for by name in Ṭā Hā 20:73?',
     ['Their obedience to Pharaoh',
      'Their sins AND «the magic to which you compelled us»',
      'Their fear',
      'Their delay in believing'], 1),
    ('What are الصَّرْف and العَطْف, which the matn names?',
     ['Two names for the same thing',
      'Turning a man AWAY from what he desires — as from his wife — and bending '
      'him TOWARD what he does not; both instances of separating a man and his '
      'wife',
      'Two kinds of incantation',
      'Two schools of magicians'], 1),
    ('A man says magic is a superstition with no reality. Ibn Bāz:',
     ['He is mistaken but excused',
      '«Whoever says it is a disbeliever» — denying the Qurʾān; for magic exists '
      'and has a reality, «some of it sickens and kills, and some is imagining, '
      'and all of it occurs»',
      'He is a fāsiq',
      'The matter requires research'], 1),
    ('What distinction does al-Qurṭubī add inside the denial?',
     ['Between the ignorant and the learned',
      'If he denies it SECRETLY he is a zindīq; if he denies it OPENLY he is an '
      'apostate',
      'Between the layman and the scholar',
      'Between denying its existence and denying its effect'], 1),
    ('What is unusual about this clause, as part 1 leaves it?',
     ['That it has no daleel',
      'That it cuts in two directions on the same ground — the practitioner is a '
      'disbeliever for doing it, and the modern denier is a disbeliever for '
      'saying it is not real, both on the text of the Qurʾān',
      'That it concerns only the Jews of Babylon',
      'That it has no ruling attached'], 1),
])

b += B.tf('nq-l11-tf', [
    ('سُمِّيَ السِّحْرُ سِحْرًا لِخَفَاءِ طُرُقِه.',
     'Magic was named siḥr because its means are hidden.', True),
    ('تَعْلِيمُ السِّحْرِ لَيْسَ بِكُفْرٍ عِنْدَ ابْنِ بَاز.',
     'Teaching magic is not disbelief, for Ibn Bāz.', False),
    ('«إِلَّا بِإِذْنِ اللهِ» مَعْنَاهَا الإِذْنُ الشَّرْعِيّ.',
     '«Except by the permission of Allah» means the legislative permission.',
     False),
    ('القَدَرُ حُجَّةٌ فِي تَرْكِ مُحَارَبَةِ السِّحْرِ وَالشِّرْك.',
     'The decree is an argument for abandoning the war against magic and shirk.',
     False),
    ('السِّحْرُ مِنَ الشِّرْكِ لِأَنَّهُ لَا يُتَوَصَّلُ إِلَيْهِ إِلَّا '
     'بِعِبَادَةِ الشَّيَاطِين.',
     'Magic is of shirk because it is not attained except by worship of the '
     'devils.', True),
    ('غَالِبُ السِّحْرِ هُوَ سِحْرُ التَّأْثِيرِ لَا التَّخْيِيل.',
     'Most magic is the magic of real effect, not of seeming.', False),
    ('مَنْ أَنْكَرَ وُجُودَ السِّحْرِ فَهُوَ كَافِرٌ مُكَذِّبٌ '
     'لِلْقُرْآن.',
     'Whoever denies that magic exists is a disbeliever, denying the Qurʾān.',
     True),
])

b += B.memorize(
    'يَجِبُ أَنْ نُعَالِجَ قَدَرَ اللهِ بِقَدَرِه',
    'Ibn Bāz, in the middle of the qadar passage on this clause — and '
    '<strong>it is the biggest sentence on the page.</strong> <em>He has just '
    'said that nothing reaches anyone except by Allah’s decree, including the '
    'magician’s harm. The obvious wrong conclusion is passivity, and he closes '
    'it off in the same breath:</em> «<strong>وَلَكِنَّهُ — سُبْحَانَهُ — '
    'شَرَعَ لَنَا أَنْ نُحَارِبَهَا، وَأَنْ نَمْتَنِعَ مِنْهَا، وَأَنْ '
    'تُقَامَ فِيهَا الحُدُودُ الشَّرْعِيَّة.</strong>» <em>The decree is not an '
    'argument against acting — acting is part of the decree. Which answers '
    'fatalism about illness, poverty and sin, and not only about magic.</em> '
    '<strong>And keep beside it the sentence that makes the clause a nullifier '
    'at all: %s.</strong>'
    % ('«' + ar('وَالسِّحْرُ مِنَ الشِّرْك') + '»'))

b += B.nav('nq-l10-masail-al-istihza.html',
           'النَّاقِضُ السَّادِس · part 2',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l11')

B.write('nq-l11-haqiqat-al-sihr.html',
        'النَّاقِضُ السَّابِع · حَقِيقَةُ السِّحْر',
        'The Seventh Nullifier, Part 1 — What Magic Is',
        'The seventh nullifier, from the words of Shaykh Ibn Bāz: siḥr named '
        'from concealment, with the root’s other uses as proof; that teaching '
        'and learning it are both disbelief by the wording of al-Baqarah 2:102; '
        'the kawnī against the sharʿī permission in «except by the permission of '
        'Allah», and the corollary that we treat Allah’s decree with His decree; '
        'why magic is shirk and not merely a grave sin — the slaughter, vows and '
        'prostration by which it is reached, and the mutual service of jinn and '
        'men; the two kinds, the magic of seeming and the magic of effect, with '
        'Pharaoh’s magicians followed to their repentance; al-ṣarf and al-ʿaṭf; '
        'and that denying magic exists is itself disbelief.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ الحَادِي عَشَر', '6', b)
print('wrote nq-l11-haqiqat-al-sihr.html')
