# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 1 — النَّاقِضُ الأَوَّل: الشِّرْكُ فِي عِبَادَةِ اللهِ.

Covers the definitional core of the first nullifier: what ʿibādah is, what
shirk is, the difference between mushrik and kāfir, the three categories of
tawḥīd and why they are three, and the two kinds of shirk.

Printed folios 19-36 (PDF indices 16-33, offset +3). The first nullifier runs
to folio 67 in the book; the remainder — the examples of major shirk, the
question of the one who abandons the prayer, and the difference between the
eternity of the disbeliever and of the sinner — is lesson 2.
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


def table(rows, fs='.91rem'):
    return ('<div style="overflow-x:auto"><table style="width:100%%;'
            'border-collapse:collapse;font-size:%s;margin:0 0 .75rem">%s</table></div>'
            % (fs, ''.join(rows)))


b = B.objectives([
    'Give the linguistic sense of %s, with the two Arab usages Ibn Bāz cites.'
    % ar('العِبَادَة'),
    'State the definition Ibn Bāz calls the most comprehensive — and name its author.',
    'Say why love alone is not worship, and what two things must accompany it.',
    'Define %s, and say how much of worship must be diverted for it to occur.'
    % ar('الشِّرْك'),
    'Distinguish %s from %s as Ibn Bāz distinguishes them.'
    % (ar('المُشْرِك'), ar('الكَافِر')),
    'Name the three categories of %s and say on what basis the division rests.'
    % ar('التَّوْحِيد'),
    'Explain why %s is not a third kind of shirk.' % ar('الشِّرْكُ الخَفِيّ'),
])

b += B.provenance(19, 36)

b += B.matn(
    'الأَوَّلُ: الشِّرْكُ فِي عِبَادَةِ اللهِ وَحْدَهُ لَا شَرِيكَ لَهُ. قَالَ '
    'اللهُ تَعَالَى: ﴿إِنَّ اللَّهَ لَا يَغْفِرُ أَنْ يُشْرَكَ بِهِ وَيَغْفِرُ مَا '
    'دُونَ ذَلِكَ لِمَنْ يَشَاءُ﴾، وَقَالَ تَعَالَى: ﴿إِنَّهُ مَنْ يُشْرِكْ '
    'بِاللَّهِ فَقَدْ حَرَّمَ اللَّهُ عَلَيْهِ الْجَنَّةَ وَمَأْوَاهُ النَّارُ '
    'وَمَا لِلظَّالِمِينَ مِنْ أَنْصَارٍ﴾. وَمِنْهُ: الذَّبْحُ لِغَيْرِ اللهِ، '
    'كَمَنْ يَذْبَحُ لِلْجِنِّ أَوْ لِلْقَبْرِ.',
    'The author gives two āyāt and then one worked example — and the example is '
    'not of an idol in a temple but of a slaughter at a grave.')

b += B.ayah(
    'إِنَّ اللَّهَ لَا يَغْفِرُ أَنْ يُشْرَكَ بِهِ وَيَغْفِرُ مَا دُونَ ذَلِكَ '
    'لِمَنْ يَشَاءُ',
    '"Indeed Allah does not forgive that partners be associated with Him, but He '
    'forgives what is less than that for whom He wills."',
    'Sūrat al-Nisāʾ 4:48 and 4:116 · سُورَةُ النِّسَاء')
b += B.ayah(
    'إِنَّهُ مَنْ يُشْرِكْ بِاللَّهِ فَقَدْ حَرَّمَ اللَّهُ عَلَيْهِ الْجَنَّةَ '
    'وَمَأْوَاهُ النَّارُ وَمَا لِلظَّالِمِينَ مِنْ أَنْصَارٍ',
    '"Whoever associates partners with Allah — Allah has forbidden him the Garden, '
    'and his refuge is the Fire; and the wrongdoers have no helpers."',
    'Sūrat al-Māʾidah 5:72 · سُورَةُ المَائِدَة')
b += B.prose(
    'Ibn Bāz pauses on the last clause. <em>«%s» — meaning the mushrikūn. '
    '<strong>الظُّلْم, when stated unrestrictedly, is intended as disbelief</strong></em>, '
    'as in «%s». <em>So the wrongdoers are the mushrikūn: they have no intercessor '
    'and no relative who can benefit them on the Day of Standing, '
    '<strong>because their disbelief prevented that.</strong></em>'
    % (ar('وَمَا لِلظَّالِمِينَ مِنْ أَنْصَارٍ'),
       ar('وَالْكَافِرُونَ هُمُ الظَّالِمُونَ')))

# ---------------------------------------------------------------- 'ibadah
b += B.heading('تَعْرِيفُ العِبَادَة', 'Defining Worship')
b += B.sharh(
    p('Before the nullifier can mean anything, the thing it concerns has to be '
      'fixed. <em>Worship with the Arabs is: <strong>التَّذَلُّلُ وَالخُضُوعُ '
      'وَالانْكِسَار</strong> — abasement, submission and being brought low.</em> '
      'And Ibn Bāz proves it from ordinary speech, which is the best kind of '
      'proof for a word:') +
    table([
        row(ar('طَرِيقٌ مُعَبَّد'),
            '<em>that is: <strong>made low — the feet have trodden it '
            'down</strong></em>'),
        row(ar('بَعِيرٌ مُعَبَّد'),
            '<em>that is: <strong>it has been bound and saddled until it became '
            'lowly to being ridden</strong> and loaded</em>'),
    ]) +
    p('<em>So our acts of obedience to Allah were named <strong>worship</strong> '
      'because we perform them <strong>with lowliness and submission</strong> to '
      'Allah جَلَّ وَعَلَا. And <strong>the slave was called a slave because he is '
      'lowly before Allah</strong>, subdued, owned by the One who created and '
      'brought him into being.</em>') +
    p('<strong>The road and the camel are the same image in two places.</strong> '
      'Neither is destroyed; both are <em>made usable by being brought low</em>. '
      'That is the picture the Arabic carries into the word, and it is why '
      'worship is not primarily about ritual acts — it is about a posture that '
      'ritual acts express.'))
b += box(
    '<p style="margin:0;font-size:.96rem"><em>— <strong>«Worship is not known by '
    'the opinions of people. It is only by the ruling of Allah.»</strong></em></p>'
    '<p style="margin:.6rem 0 0;font-size:.92rem">One sentence, and it closes a '
    'door that a great deal walks through. <strong>If what counts as worship were '
    'settled by what people feel to be reverent, then every practice could defend '
    'itself by sincerity.</strong> Ibn Bāz puts the definition out of reach of '
    'taste — which is the only way the nullifier can be stated at all.</p>')
b += B.sharh(
    p('<em>The scholars رَحِمَهُمُ اللهُ explained worship with meanings close to '
      'one another; <strong>of the most comprehensive of them</strong> is what '
      'Shaykh al-Islām Ibn Taymiyyah mentioned</em> — and Ibn Bāz says elsewhere, '
      'plainly, that <em>what Abū al-ʿAbbās Ibn Taymiyyah said is '
      '<strong>the most comprehensive of the definitions</strong></em>:'))
b += box(
    '<p style="margin:0 0 .5rem;font-size:1.02rem;text-align:center" dir="rtl" '
    'lang="ar"><strong>العِبَادَةُ: اسْمٌ جَامِعٌ لِكُلِّ مَا يُحِبُّهُ اللهُ '
    'وَيَرْضَاهُ مِنَ الأَقْوَالِ وَالأَعْمَالِ الظَّاهِرَةِ '
    'وَالبَاطِنَة</strong></p>'
    '<p style="margin:0;font-size:.95rem;text-align:center"><em>"Worship is a '
    'comprehensive name for everything Allah loves and is pleased with, of '
    'sayings and of deeds, outward and inward."</em></p>')
b += B.sharh(
    p('<strong>Read what that definition rules in.</strong> Not a list of rites — '
      '<em>sayings</em> and <em>deeds</em>, <em>outward</em> and <em>inward</em>. '
      'So a belief held in the heart is worship; so is a word on the tongue; so is '
      'an act of the limbs. <em>This indicates that worship requires '
      '<strong>complete submission to Allah</strong> — in command and prohibition, '
      'in belief, word and deed — and that a person\'s life be founded on the law '
      'of Allah: he permits what Allah permitted and forbids what Allah forbade.</em>') +
    p('<em>And so <strong>one who submits to his Lord in some sides of his life</strong> '
      'and turns to another\'s judgement in others <strong>is not a worshipper of '
      'Allah</strong>; whoever submits to other than Him and seeks judgement from '
      'other than His law <strong>has worshipped the ṭāghūt</strong>.</em>'))

# ---------------------------------------------------------------- the three
b += B.heading('لَا تَكُونُ عِبَادَةً بِالحُبِّ وَحْدَه',
               'Love Alone Is Not Worship')
b += B.sharh(
    p('Ibn Bāz reports a line from the salaf that sounds severe until the reason '
      'is given: <em>«<strong>Whoever worships Allah with love — supposing that he '
      'loves Allah only — is a zindīq.</strong> How does he not fear Allah and not '
      'hope in Him? And who is he, that he should not fear Allah and not hope in '
      'Him?»</em>') +
    p('The proof is what Allah says of the Prophets themselves:'))
b += B.ayah(
    'إِنَّهُمْ كَانُوا يُسَارِعُونَ فِي الْخَيْرَاتِ وَيَدْعُونَنَا رَغَبًا '
    'وَرَهَبًا وَكَانُوا لَنَا خَاشِعِينَ',
    '"Indeed they used to hasten to good deeds and to call upon Us in hope and in '
    'fear, and they were humbly submissive to Us."',
    'Sūrat al-Anbiyāʾ 21:90 · سُورَةُ الأَنْبِيَاء')
b += B.sharh(
    p('<em>He did not say: «they call upon Us in love» only. He said: '
      '<strong>رَغَبًا وَرَهَبًا</strong> — <strong>desiring the Garden and '
      'dreading the Fire</strong>. So the Messengers and the Prophets and the '
      'believers <strong>feared Allah\'s punishment, hoped for His reward, and '
      'loved Him a true love</strong> which carried them to obeying Him and '
      'leaving disobedience — <strong>it did not carry them to excess, or '
      'self-admiration, or arrogance.</strong></em>') +
    p('And Ibn al-Qayyim\'s line, which Ibn Bāz quotes for the same point:') +
    '<div style="background:var(--brand-wash);border-radius:var(--radius-sm);'
    'padding:var(--space-md);margin:0 0 .8rem;text-align:center">'
    '<p style="margin:0;font-family:var(--font-arabic);font-size:1.05rem;'
    'direction:rtl;color:var(--teal-deep);line-height:2.1">'
    'وَعِبَادَةُ الرَّحْمَنِ غَايَةُ حُبِّهِ &nbsp;&nbsp;·&nbsp;&nbsp; '
    'مَعَ ذُلِّ عَابِدِهِ هُمَا قُطْبَان</p>'
    '<p style="margin:.5rem 0 0;font-size:.88rem"><em>"Worship of the Most '
    'Merciful is the utmost of love for Him, together with the lowliness of the '
    'worshipper — the two are its poles."</em></p></div>' +
    p('<strong>Two poles, not one.</strong> Love without lowliness is not worship, '
      'and lowliness without love is not worship either. That is the test to put '
      'to any devotion that feels intense: <em>does it humble the man, or does it '
      'make him grand?</em>'))
b += B.prose(
    'And the same definition has a quieter consequence Ibn Bāz draws out: '
    '<em>«If a man sleeps <strong>in order to gain strength for seeking knowledge</strong>, '
    'or to perform the lesson as he should, or to gain strength for travelling in '
    'the pursuit of knowledge — <strong>then his sleep is worship, and his travel '
    'is worship</strong>.» And: «according to the servant\'s intention his deeds '
    'become worship of Allah… and if he does them without intention, they are of '
    'the permissible things.»</em> <strong>The same act is worship or is nothing, '
    'and the intention decides.</strong>')

# ---------------------------------------------------------------- shirk
b += B.heading('تَعْرِيفُ الشِّرْك', 'Defining Shirk')
b += B.sharh(
    p('<em>«The reality of shirk is: <strong>making another a partner with Allah '
      'in worship</strong> — whether an ally, a prophet, a jinn, an angel, a stone, '
      'an idol, a tree or other than that. <strong>This is the major shirk.</strong>»</em>') +
    p('And then the definition that carries the whole nullifier: '
      '<em>«Shirk is: <strong>directing SOME of the worship to other than Allah</strong> '
      '— making part of it for Allah and part of it for another: of jinn, mankind, '
      'angels, idols, trees, planets, stones or anything of the creation; he seeks '
      'rescue from them, or vows to them, or slaughters for them, or asks support '
      'of them.»</em>'))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem"><strong>«Some» is doing the work '
    'in that sentence, and the sharḥ says so explicitly:</strong></p>'
    '<p style="margin:0;font-size:.95rem"><em>— <strong>«Part of the worship, not '
    'all of it. Diverting part is enough — if he diverts part of it, that suffices '
    'for shirk</strong>, we seek refuge in Allah. And if he diverts all of it, it '
    'is graver and uglier.»</em></p>'
    '<p style="margin:.6rem 0 0;font-size:.92rem">Which answers the objection a '
    'student reaches for first: <em>but he prays, and fasts, and believes in '
    'Allah.</em> So did the mushrikūn of Makkah. <strong>The nullifier is not «he '
    'worships something else instead»; it is «he gives something else a share».</strong></p>')
b += B.prose(
    'The footnote adds a second framing worth holding beside the first: '
    '<strong>shirk is %s</strong> — <em>equating another with Allah in something '
    'of Allah\'s exclusive attributes</em>. Ibn Taymiyyah, as cited there: '
    '<em>«whoever equates the Creator and the created in love of Him, fear of Him '
    'and hope in Him, is a mushrik.»</em> And the Qurʾān gives the mushrikūn\'s own '
    'words in the Fire, which name the act exactly:'
    % ar('تَسْوِيَةُ غَيْرِ اللهِ بِاللهِ فِي شَيْءٍ مِنْ خَصَائِصِه'))
b += B.ayah(
    'تَاللَّهِ إِنْ كُنَّا لَفِي ضَلَالٍ مُبِينٍ إِذْ نُسَوِّيكُمْ بِرَبِّ '
    'الْعَالَمِينَ',
    '"By Allah, we were surely in clear error when we equated you with the Lord of '
    'the worlds."',
    'Sūrat al-Shuʿarāʾ 26:97–98 · سُورَةُ الشُّعَرَاء')
b += B.prose(
    '<strong>Note the verb they use: %s — «we equated you».</strong> Not «we '
    'worshipped you instead of Him», and not «we denied Him». They had never '
    'denied Him. <em>The confession is of equating</em> — which is the definition '
    'the footnote gave, put in the mouths of the people who did it.'
    % ar('نُسَوِّيكُم'))

# ---------------------------------------------------------------- mushrik/kafir
b += B.heading('الفَرْقُ بَيْنَ المُشْرِكِ وَالكَافِر',
               'The Difference Between Mushrik and Kāfir')
b += B.sharh(
    p('<em>«<strong>Every shirk is disbelief, and every disbelief is shirk.</strong> '
      'The mushrik is a kāfir and the kāfir is a mushrik.»</em> So the two are not '
      'two populations. <strong>But the names are not used at random either</strong>, '
      'and Ibn Bāz gives the usage:') +
    table([
        row(ar('المُشْرِك'),
            '<em>Whoever\'s disbelief came about <strong>by directing worship to '
            'other than Allah</strong> — calling upon another, seeking rescue of '
            'another — <strong>the name «mushrik» clings to him more '
            'closely</strong></em>'),
        row(ar('الكَافِر'),
            '<em>Whoever\'s disbelief came about <strong>by denial</strong> — '
            'denying what Allah obligated or what He forbade — <strong>or by '
            'reviling, or by belittling — the name «kāfir» clings to him more '
            'closely</strong></em>'),
    ]) +
    p('<em>«Disbelief is applied in the main to <strong>denying the truth</strong>, '
      'and shirk to <strong>directing worship to other than Allah</strong>; and '
      'each of them is called by the other\'s name.»</em>') +
    p('<strong>So the distinction is about which name fits more snugly, not about '
      'which ruling applies.</strong> That is a precision worth having, because a '
      'student who thinks they name two different verdicts will misread half the '
      'texts in this subject.'))

# ---------------------------------------------------------------- tawhid 3
b += B.heading('أَنْوَاعُ التَّوْحِيدِ ثَلَاثَة',
               'The Three Categories of Tawḥīd')
b += B.sharh(
    table([
        row(ar('تَوْحِيدُ الرُّبُوبِيَّة'),
            '<em><strong>Acknowledging the Lord\'s actions</strong> — His '
            'governing of the world and His disposal within it; <strong>that He is '
            'the Creator, the Provider, the Manager of affairs</strong></em>'),
        row(ar('تَوْحِيدُ الأُلُوهِيَّة'),
            '<em>Singling Him out <strong>with the worship</strong> itself</em>'),
        row(ar('تَوْحِيدُ الأَسْمَاءِ وَالصِّفَات'),
            '<em>That He has <strong>the most beautiful names and the highest '
            'attributes</strong></em>'),
    ]) +
    p('And then the point on which the entire daʿwah of the Prophets turns: '
      '<em>«<strong>Tawḥīd al-rubūbiyyah — the mushrikūn affirmed it and did not '
      'deny it</strong>, but they did not enter Islam by it, because they did not '
      'make their worship purely for Allah. They affirmed that their Lord is the '
      'Creator and the Provider — <strong>but they did not single Him out with the '
      'worship — so the Prophet ﷺ fought them until they made the worship purely '
      'for Allah alone.</strong>»</em>'))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem"><strong dir="rtl" lang="ar">'
    'سُؤَالٌ وَجَوَاب</strong> — Ibn Bāz was asked whether dividing tawḥīd into '
    'three has any evidence for it. The answer is a lesson in method:</p>'
    '<p style="margin:0;font-size:.94rem"><em>«<strong>This is taken by '
    'اسْتِقْرَاء — induction.</strong> Because when the scholars surveyed what the '
    'texts of the Book and the Sunnah came with, this became apparent to them… '
    'whoever ponders the Noble Qurʾān finds in it āyāt commanding that worship be '
    'made purely for Allah alone — <strong>and this is tawḥīd al-ulūhiyyah</strong>; '
    'and he finds āyāt indicating that Allah is the Creator, the Provider, the '
    'Manager — <strong>and this is tawḥīd al-rubūbiyyah</strong>; and he finds '
    'others indicating that He has the most beautiful names and highest attributes '
    '— <strong>and this is tawḥīd al-asmāʾ wa-l-ṣifāt</strong>. So this division is '
    'known by induction, by tracing the āyāt and studying the Sunnah.»</em></p>'
    '<p style="margin:.6rem 0 0;font-size:.92rem"><strong>The division is a '
    'finding, not a framework imposed on the texts</strong> — which is the honest '
    'answer to anyone who calls it an innovation. Nobody claims the Qurʾān lists '
    'three headings; the claim is that these three are what the āyāt sort '
    'themselves into when you read them all.</p>')

# ---------------------------------------------------------------- 2 kinds
b += B.heading('الشِّرْكُ نَوْعَان', 'Shirk Is of Two Kinds')
b += B.sharh(
    table([
        row(ar('شِرْكٌ أَكْبَر'),
            '<em>What <strong>comprises directing worship — or part of it — to '
            'other than Allah</strong>. It takes its doer out of the religion</em>'),
        row(ar('شِرْكٌ أَصْغَر'),
            '<em>What <strong>the texts established the naming of as shirk, but '
            'which did not reach the degree of the major</strong> — such as '
            '<strong>الرِّيَاء</strong> and <strong>السُّمْعَة</strong>; and of it '
            'is the servant\'s saying <strong>«مَا شَاءَ اللهُ وَشَاءَ '
            'فُلَان»</strong>, or «were it not for Allah and so-and-so», or «this '
            'is from Allah and from so-and-so»</em>'),
    ]) +
    p('Then a question the Shaykh settles rather than leaves open: '
      '<em>and there is a shirk called <strong>الشِّرْكُ الخَفِيّ</strong>, the '
      'hidden shirk, which some of the people of knowledge mentioned as '
      '<strong>a third category</strong>…</em>'))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem"><em>— <strong>«And the correct '
    'view is that this is not a third category; rather it is of the minor '
    'shirk»</strong> — and it may be hidden because it subsists in the hearts, as '
    'one who recites showing off.</em></p>'
    '<p style="margin:0 0 .5rem;font-size:.94rem"><em>— <strong>«And it may be '
    'hidden AND be of the major shirk, as the belief of the hypocrites»</strong>: '
    'for they show off with their outward deeds, and their disbelief is hidden; '
    'they did not make it apparent.</em></p>'
    '<p style="margin:0;font-size:.93rem"><strong>So «hidden» is not a third '
    'rank — it is a description that can attach to either of the two.</strong> '
    'Which is why the reasoning matters more than the label: the question is never '
    '«is this hidden?» but «is this directing worship to another, or not?»</p>')
b += B.sharh(
    table([
        row(ar('جَلِيّ') + '<br><span style="font-size:.8rem;font-weight:400">'
            'open</span>',
            '<em><strong>Calling upon the dead, seeking rescue of the dead, '
            'vowing to them</strong> and the like</em>'),
        row(ar('خَفِيّ') + '<br><span style="font-size:.8rem;font-weight:400">'
            'hidden</span>',
            '<em>What is <strong>in the hearts of the hypocrites</strong> — they '
            'pray with the people and fast…</em>'),
    ]))
b += B.prose(
    'And now look back at the matn\'s own example with this in hand. The author '
    'did not illustrate the first nullifier with an idol. He wrote: '
    '<strong>«%s» — and of it: slaughtering for other than Allah, like one who '
    'slaughters for the jinn or for the grave.</strong> <em>A slaughter is an act '
    'of worship</em>; performing it for a grave is giving a share of worship to '
    'other than Allah. <strong>The example is chosen because it is the one a '
    'Muslim might actually do while believing himself a Muslim</strong> — which is '
    'precisely what a nullifier is for.'
    % ar('وَمِنْهُ: الذَّبْحُ لِغَيْرِ اللهِ'))

b += B.vocab([
    ('العِبَادَة', 'al-ʿibādah', 'worship',
     'لُغَةً التَّذَلُّلُ وَالخُضُوعُ وَالانْكِسَار; and in the most comprehensive '
     'definition, اسْمٌ جَامِعٌ لِكُلِّ مَا يُحِبُّهُ اللهُ وَيَرْضَاه'),
    ('طَرِيقٌ مُعَبَّد', 'ṭarīq muʿabbad', 'a trodden road',
     'A road made low by feet — the Arab usage that shows the root means being '
     'brought low, not ritual'),
    ('الشِّرْك', 'al-shirk', 'associating partners',
     'صَرْفُ بَعْضِ العِبَادَةِ لِغَيْرِ اللهِ — diverting SOME of the worship; '
     'and تَسْوِيَةُ غَيْرِ اللهِ بِاللهِ in His exclusive attributes'),
    ('رَغَبًا وَرَهَبًا', 'raghaban wa-rahaban', 'in hope and in fear',
     'The two that must accompany love — al-Anbiyāʾ 21:90, said of the Prophets '
     'themselves'),
    ('الزِّنْدِيق', 'al-zindīq', 'a heretic',
     'What the salaf called one who claims to worship Allah by love alone, with '
     'neither fear nor hope'),
    ('تَوْحِيدُ الرُّبُوبِيَّة', 'tawḥīd al-rubūbiyyah', 'oneness of lordship',
     'Acknowledging He is Creator, Provider, Manager — the mushrikūn affirmed it '
     'and were not Muslims by it'),
    ('الاسْتِقْرَاء', 'al-istiqrāʾ', 'induction',
     'The basis of the three-fold division of tawḥīd — a finding drawn from '
     'surveying the texts, not a framework imposed on them'),
    ('الشِّرْكُ الأَصْغَر', 'al-shirk al-aṣghar', 'minor shirk',
     'What the texts name shirk without it reaching the major — الرِّيَاء, '
     'السُّمْعَة, «مَا شَاءَ اللهُ وَشَاءَ فُلَان»'),
    ('الشِّرْكُ الخَفِيّ', 'al-shirk al-khafī', 'hidden shirk',
     'Not a third category — a description that may attach to either kind; '
     'the hypocrites’ belief is hidden AND major'),
])

b += B.mcq('nq-l01', [
    ('What does العِبَادَة mean in the language, and what proves it?',
     ['Ritual acts specifically, proven by the five pillars',
      'التَّذَلُّلُ وَالخُضُوعُ وَالانْكِسَار — proven from Arab usage: a '
      'road مُعَبَّد is one trodden low, and a camel مُعَبَّد is one bound until '
      'lowly to being ridden',
      'Obedience, proven by the āyah of obedience to those in authority',
      'Love, proven by the āyah «yuḥibbuhum wa yuḥibbūnah»'], 1),
    ('Which definition does Ibn Bāz call the most comprehensive, and whose is it?',
     ['Ibn al-Qayyim’s: worship is love and lowliness',
      'Ibn Taymiyyah’s: a comprehensive name for everything Allah loves and is '
      'pleased with, of sayings and deeds, outward and inward',
      'Ibn Kathīr’s: obedience with humility',
      'al-Ṭabarī’s: submission to the command'], 1),
    ('What does "worship is not known by the opinions of people" rule out?',
     ['That scholars may differ over details of worship',
      'That a practice can justify itself by how reverent it feels — what counts '
      'as worship is set by the ruling of Allah, not by taste',
      'That laypeople may ask about worship',
      'That worship can be performed in any language'], 1),
    ('Why did the salaf call one who worships by love alone a zindīq?',
     ['Because love of Allah is not required',
      'Because worship requires hope and fear with the love — as Allah said of the '
      'Prophets themselves, «they call upon Us رَغَبًا وَرَهَبًا»',
      'Because love cannot be verified',
      'Because love is an inward act and worship must be outward'], 1),
    ('What are the two "poles" in Ibn al-Qayyim’s line?',
     ['Fear and hope',
      'The utmost of love for Him, together with the lowliness of the worshipper',
      'The outward and the inward deed',
      'Knowledge and action'], 1),
    ('How much of worship must be diverted for shirk to occur?',
     ['All of it — a man must abandon Allah entirely',
      'SOME of it — "diverting part is enough; and if he diverts all of it, it is '
      'graver and uglier"',
      'Only acts of the limbs, not of the heart',
      'Only what is done publicly'], 1),
    ('What verb do the mushrikūn use of themselves in al-Shuʿarāʾ 26:98?',
     ['«we denied You»', '«we equated you with the Lord of the worlds» — نُسَوِّيكُم',
      '«we forgot You»', '«we worshipped you instead of Him»'], 1),
    ('How does Ibn Bāz distinguish مُشْرِك from كَافِر?',
     ['They name two different rulings',
      'Every shirk is kufr and every kufr is shirk — but the name «mushrik» clings '
      'more closely to one whose disbelief came by directing worship elsewhere, and '
      '«kāfir» to one whose came by denial or reviling',
      'Mushrik is major and kāfir is minor',
      'Kāfir applies only to the People of the Book'], 1),
    ('What did the mushrikūn of Makkah affirm, and why did it not make them Muslims?',
     ['Tawḥīd al-ulūhiyyah, but they worshipped idols too',
      'Tawḥīd al-rubūbiyyah — that Allah is Creator, Provider and Manager — but '
      'they did not single Him out with the WORSHIP',
      'The names and attributes, but they denied the resurrection',
      'The prophethood of Ibrāhīm, but not of Muḥammad ﷺ'], 1),
    ('On what basis does the three-fold division of tawḥīd rest?',
     ['A ḥadīth listing the three',
      'الاسْتِقْرَاء — induction: it is what the āyāt sort themselves into when the '
      'scholars surveyed the Book and the Sunnah, a finding rather than a framework '
      'imposed',
      'The consensus of the four imāms',
      'The practice of the people of Madīnah'], 1),
    ('Which are examples of minor shirk?',
     ['Calling upon the dead and vowing to them',
      'الرِّيَاء and السُّمْعَة, and saying «مَا شَاءَ اللهُ وَشَاءَ فُلَان» or '
      '«were it not for Allah and so-and-so»',
      'Denying the obligation of the prayer',
      'Slaughtering at a grave'], 1),
    ('Why is الشِّرْكُ الخَفِيّ not a third category?',
     ['Because the texts never use the phrase',
      'Because "hidden" is a description that may attach to either kind — minor '
      'shirk may be hidden in the heart, and the hypocrites’ disbelief is hidden '
      'AND major',
      'Because it was invented by later scholars',
      'Because hidden deeds are not accountable'], 1),
    ('Why is slaughtering at a grave the matn’s chosen example?',
     ['Because it was the commonest practice in Najd',
      'Because a slaughter is an act of worship, so performing it for a grave gives '
      'a share of worship to other than Allah — and it is the kind of thing a man '
      'might do while believing himself a Muslim',
      'Because the jinn are mentioned alongside it',
      'Because it involves wealth as well as intention'], 1),
])

b += B.tf('nq-l01-tf', [
    ('العِبَادَةُ تُعْرَفُ بِآرَاءِ النَّاسِ وَمَا يَسْتَحْسِنُونَهُ.',
     'Worship is known by people’s opinions and what they deem good.', False),
    ('صَرْفُ بَعْضِ العِبَادَةِ لِغَيْرِ اللهِ يَكْفِي فِي الشِّرْكِ.',
     'Diverting some of the worship to other than Allah is enough for shirk.', True),
    ('أَقَرَّ المُشْرِكُونَ بِتَوْحِيدِ الرُّبُوبِيَّةِ وَلَمْ يَدْخُلُوا بِهِ فِي '
     'الإِسْلَامِ.',
     'The mushrikūn affirmed the oneness of lordship and did not enter Islam by it.',
     True),
    ('الشِّرْكُ الخَفِيُّ قِسْمٌ ثَالِثٌ مُسْتَقِلٌّ.',
     'Hidden shirk is an independent third category.', False),
    ('عِبَادَةُ اللهِ بِالحُبِّ وَحْدَهُ دُونَ خَوْفٍ وَلَا رَجَاءٍ كَافِيَةٌ.',
     'Worshipping Allah by love alone, without fear or hope, is sufficient.', False),
])

b += B.memorize(
    'العِبَادَةُ: اسْمٌ جَامِعٌ لِكُلِّ مَا يُحِبُّهُ اللهُ وَيَرْضَاهُ مِنَ '
    'الأَقْوَالِ وَالأَعْمَالِ الظَّاهِرَةِ وَالبَاطِنَة',
    'Memorize this one and the first nullifier becomes readable. '
    '<strong>If worship is everything Allah loves — sayings and deeds, outward and '
    'inward — then shirk is giving any of that to someone else</strong>, and it '
    'does not need to be all of it. Which is why the author illustrated the '
    'nullifier with a slaughter at a grave rather than an idol in a temple: '
    '<em>the danger is not that a man stops worshipping Allah, but that he lets '
    'something else take a share.</em>')

b += B.nav('u6-nawaqid.html', 'نَوَاقِضُ الإِسْلَام · the overview',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l01')

B.write('nq-l01-shirk-al-ibadah.html',
        'النَّاقِضُ الأَوَّل · الشِّرْكُ فِي العِبَادَة',
        'The First Nullifier — Shirk in Worship',
        'The first of the ten nullifiers, explained from the words of Shaykh Ibn '
        'Bāz: what worship is in the language and in the most comprehensive '
        'definition; why love alone is not worship; that diverting SOME of the '
        'worship suffices for shirk; the difference between mushrik and kāfir; the '
        'three categories of tawḥīd and the induction they rest on; and why hidden '
        'shirk is not a third kind.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ الأَوَّل', '3', b)
print('wrote nq-l01-shirk-al-ibadah.html')
