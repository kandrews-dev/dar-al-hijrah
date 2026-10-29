# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 4 — النَّاقِضُ الثَّالِث: عَدَمُ تَكْفِيرِ المُشْرِكِين.

Printed folios 98-107 (PDF indices 95-104, offset +3). The matn clause opens on
index 95, NOT 96 where the running header first changes -- the header lags the
section by a page here, which is why the range was taken from the matn quotation
and not from the header map.

This clause is the one most often quoted without its restraints, and the sharḥ
itself spends the majority of its ten folios on them: on إِقَامَةُ الحُجَّة, on
what the ʿāmmī may and may not say, on the difference between doubting what
Allah has settled and doubting what the scholars dispute (Ibn Bāz's own worked
example is the man who abandons the prayer without denying its obligation --
one who doubts about HIM is excused, مَعْذُورٌ فِي اجْتِهَادِه), and on the
ḥudūd belonging to the one in authority and not to the individual. A lesson
that carried the ruling and dropped that material would misteach the clause,
so the ضَوَابِط section is the longest on the page.

Rule 8 note: the sharḥ's footnote grades «مَنْ كَفَّرَ مُسْلِمًا فَقَدْ كَفَرَ»
as كَذِبٌ لَا أَصْلَ لَه -- a commonly circulated text with no basis -- and the
page carries that grading with it, since the whole point of rule 8 is that a
grading travels with an attribution.
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


b = B.objectives([
    'State the three acts this clause of the matn names, and in what order they rise.',
    'Explain why it is kufr in terms of %s — belying a report — and not in terms '
    'of severity.' % ar('تَكْذِيب'),
    'Show from Muslim’s ḥadīth of Ṭāriq ibn Ashyam that this is the %s half of '
    'the kalimah, not an addition to it.' % ar('نَفْي'),
    'Give Ibn Bāz’s argument from %s — the creed a Muslim asks for in every '
    'rakʿah.' % ar('سُورَةُ الفَاتِحَة'),
    'State precisely <strong>where doubt is kufr and where doubt is '
    '%s</strong>, using Ibn Bāz’s own worked example.' % ar('اجْتِهَاد'),
    'Say who may carry out a sentence, and what the ʿāmmī does with a matter that '
    'is obscure to him.',
])

b += B.provenance(98, 107)

b += B.matn(
    'الثَّالِث: مَنْ لَمْ يُكَفِّرِ المُشْرِكِينَ، أَوْ شَكَّ فِي كُفْرِهِمْ، '
    'أَوْ صَحَّحَ مَذْهَبَهُمْ — كَفَرَ إِجْمَاعًا.',
    'Three acts, and they rise in subtlety: withholding the ruling, then '
    'wavering over it, then declaring their way sound.')
b += B.prose(
    '<strong>Of the ten, this is the clause most often quoted with its restraints '
    'stripped off</strong> — and the sharḥ does the opposite. Of its ten folios, '
    'the greater part is spent on %s, on what a layman may and may not say, on '
    'the difference between doubting what Allah has settled and doubting what the '
    'scholars dispute, and on whose hand carries out a sentence. '
    '<em>This lesson is weighted the same way the source is.</em>'
    % ar('إِقَامَةُ الحُجَّة'))

# ---------------------------------------------------------------- the abode
b += B.heading('هَذِهِ الدَّارُ جَامِعَةٌ', 'Where Ibn Bāz Begins')
b += B.sharh(
    p('He does not open with a ruling. He opens with a fact about the world:') +
    box('<p style="margin:0;font-size:.94rem"><em>«<strong>This abode gathers the '
        'wholesome and the foul, the disbeliever and the Muslim</strong> — and '
        'most of its people are upon disbelief and misguidance.»</em></p>') +
    p('And he lays four proofs under it: %s — <em>and most of mankind, however '
      'much you should crave it, will not believe</em>; %s — <em>and if you obey '
      'most of those upon the earth they will lead you away from the path of '
      'Allah</em>; %s — <em>and few of My slaves are grateful</em>; and the '
      'refrain that closes story after story in %s — %s.'
      % (ar('يُوسُف ١٢:١٠٣'), ar('الأَنْعَام ٦:١١٦'), ar('سَبَأ ٣٤:١٣'),
         ar('سُورَةُ الشُّعَرَاء'),
         '<em>«' + ar('وَمَا كَانَ أَكْثَرُهُمْ مُؤْمِنِينَ') + '»</em>')) +
    p('<strong>Why open there?</strong> Because this nullifier only has teeth if '
      'the category it speaks about is populated. A man who has quietly concluded '
      'that there are no mushrikūn left in the world never has to break this '
      'clause — <em>he has dissolved it.</em> So the sharḥ settles first that the '
      'category is not empty, and is not even small.'))

b += B.ayah(
    'وَمَا أَكْثَرُ النَّاسِ وَلَوْ حَرَصْتَ بِمُؤْمِنِينَ',
    'And most of mankind, however much you crave it, will not believe.',
    'سُورَةُ يُوسُف · 12:103')

# ---------------------------------------------------------------- inside tawhid
b += B.heading('مَا يَدْخُلُ فِي التَّوْحِيد', 'The Clause Is Inside the Definition')
b += B.sharh(
    p('The objection that writes itself is: <em>why should my view of other '
      'people be a condition of my own tawḥīd?</em> Ibn Bāz answers it by '
      'defining tawḥīd, and the answer is in the definition:') +
    box('<p style="margin:0;font-size:.94rem"><em>«Tawḥīd of Allah is singling '
        'Him out for worship — <strong>out of belief, out of truthfulness, and '
        'out of action, not mere speech</strong> — together with holding that '
        '<strong>the worship of other than Him is false</strong>, and that '
        '<strong>the worshippers of other than Him are mushrikūn</strong>, and '
        'together with <strong>barāʾah from them</strong>.»</em></p>') +
    p('So it is not a sixth item bolted onto five. The ruling on %s and the ruling '
      'on %s are two faces of one belief, and a man who affirms the first while '
      'refusing the second has not finished a sentence.'
      % (ar('العِبَادَة'), ar('العَابِد'))))
b += B.prose(
    'His proof is Ibrāhīm, and the wording repays attention — <strong>the people '
    'come before the objects</strong>, in both verses.')
b += B.ayah(
    'قَدْ كَانَتْ لَكُمْ أُسْوَةٌ حَسَنَةٌ فِي إِبْرَاهِيمَ وَالَّذِينَ مَعَهُ '
    'إِذْ قَالُوا لِقَوْمِهِمْ إِنَّا بُرَآءُ مِنكُمْ وَمِمَّا تَعْبُدُونَ مِن '
    'دُونِ اللَّهِ',
    'There has already been for you an excellent example in Ibrāhīm and those '
    'with him, when they said to their people: indeed we are free of you, and of '
    'whatever you worship besides Allah.',
    'سُورَةُ المُمْتَحَنَة · 60:4')
b += B.prose(
    '%s — <em>free of <strong>you</strong></em>, and only then <em>of what you '
    'worship</em>. The same order in Ibrāhīm’s words to his father and his '
    'people: %s — %s. <em>The disavowal that the Qurʾān holds up as the excellent '
    'example is addressed to persons first.</em>'
    % ('<strong>' + ar('إِنَّا بُرَآءُ مِنكُمْ') + '</strong>',
       ar('إِنَّنِي بَرَاءٌ مِّمَّا تَعْبُدُونَ * إِلَّا الَّذِي فَطَرَنِي'),
       ar('الزُّخْرُف ٤٣:٢٦–٢٧')))

# ---------------------------------------------------------------- why kufr
b += B.heading('لِمَاذَا كَانَ كُفْرًا', 'Because It Is Takdhīb, Not Harshness')
b += B.sharh(
    p('Here is the sentence the whole clause turns on:') +
    box('<p style="margin:0;font-size:.94rem"><em>«And the one who knows the '
        'disbeliever and the falsehood he is upon, and then <strong>does not '
        'declare him a disbeliever, or doubts his disbelief</strong> — the meaning '
        'of that is that he is <strong>belying Allah and His Messenger</strong>, '
        'not believing in what Allah has ruled upon them of disbelief… so they '
        'are disbelievers <strong>by the text of the Qurʾān and the text of the '
        'Sunnah</strong>. So it is obligatory upon the accountable from among the '
        'Muslims to <strong>hold as a belief</strong> their disbelief and their '
        'misguidance.»</em></p>', wash='var(--accent-wash)', edge='var(--accent)') +
    p('<strong>Read what that does to the question.</strong> The clause is not '
      'asking you to issue a ruling; the ruling has been issued, and it was not '
      'issued by you. What is asked of you is %s — to hold as true a report that '
      'has already come. <em>Refusing is therefore not mercy. It is disbelieving '
      'a report</em>, and the softness of the motive does not change what the act '
      'is.' % ar('الاعْتِقَاد')) +
    p('Which is also why this lesson is not about naming people. '
      '<strong>It is about believing Allah about a category He has already '
      'described.</strong> Everything in the restraints section below follows '
      'from keeping those two things apart.'))
b += table([
    thead3('the act', 'what it amounts to', 'why'),
    row3(ar('لَمْ يُكَفِّرْ'), 'withholding assent to a ruling already given',
         'the report came from Allah; he declines to affirm it'),
    row3(ar('شَكَّ'), 'neither affirming nor denying',
         'the Qurʾān makes doubt in the foundations itself disbelief'),
    row3(ar('صَحَّحَ مَذْهَبَهُمْ'), 'declaring their way sound',
         'he contradicts the report <em>and</em> validates its opposite'),
])

b += B.heading('حَقِيقَةُ الشَّكّ', 'What Doubt Is')
b += B.sharh(
    p('The sharḥ quotes the ʿallāmah <strong>سُلَيْمَانُ بْنُ سَحْمَان</strong> '
      'defining it, because the word is used loosely:') +
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><em>«The Qurʾān has '
        'indicated that <strong>doubt in the foundations of the religion is '
        'disbelief</strong>, and doubt is <strong>wavering between two '
        'things</strong> — like one who is decisive about neither the '
        'truthfulness of the Messenger nor his lying; who is decisive about '
        'neither the occurrence of the Resurrection nor its non-occurrence; who '
        'holds neither the obligation of the prayer nor its non-obligation; who '
        'holds neither the prohibition of zinā nor its non-prohibition.»</em></p>'
        '<p style="margin:0;font-size:.94rem"><em>«And know that <strong>not every '
        'error and ijtihād and ignorance is forgiven its possessor</strong> — for '
        'Allah has informed us of the ignorance of many of the disbelievers '
        '<strong>while expressly declaring them disbelievers</strong>, and '
        'described the Christians as ignorant, though no Muslim doubts their '
        'disbelief.»</em></p>') +
    p('So doubt here is not the ordinary uncertainty of a student who has not yet '
      'studied a question. <em>It is suspension where the texts have not left the '
      'matter open</em> — and he is making the point that ignorance, as such, is '
      'not automatically a covering.'))
b += B.prose(
    'Ibn Saḥmān also answers the category objection, and it is worth having: '
    '<strong>declaring the disbeliever a disbeliever is from the %s, not the '
    '%s</strong> which may be hidden from many of the creation — so ignorance of '
    'it is not accommodated. <em>And in the same place he explains why the matn '
    'lists ten:</em> some of the people of knowledge counted the nullifiers at '
    '<strong>close to four hundred</strong> — but these ten are <em>«of what the '
    'scholars have agreed upon»</em>.'
    % (ar('أُصُول'), ar('فُرُوع')))

# ---------------------------------------------------------------- the kalimah
b += B.heading('كَلِمَةُ الإِخْلَاص', 'This Is the لَا of لَا إِلَهَ')
b += B.sharh(
    p('Ibn Bāz grounds the clause in a ḥadīth that makes the point structurally, '
      'and he quotes the narration that <em>interprets the kalimah with it</em>:'))
b += B.hadith(
    'مَنْ قَالَ لَا إِلَهَ إِلَّا اللهُ وَكَفَرَ بِمَا يُعْبَدُ مِنْ دُونِ '
    'اللهِ، حَرُمَ مَالُهُ وَدَمُهُ، وَحِسَابُهُ عَلَى اللهِ',
    'Whoever says “there is no deity except Allah” <em>and disbelieves in what is '
    'worshipped besides Allah</em> — his property and his blood become '
    'inviolable, and his reckoning is with Allah.',
    'رَوَاهُ مُسْلِمٌ فِي صَحِيحِهِ · from طَارِقُ بْنُ أَشْيَمَ الأَشْجَعِيّ '
    '— and in another narration of Muslim: مَنْ وَحَّدَ اللهَ')
b += B.sharh(
    p('<strong>Two conditions, not one.</strong> The Prophet ﷺ made a man’s blood '
      'and property inviolable upon an affirmation <em>and</em> a disbelief — and '
      'the second narration, %s, shows that the second clause is the Prophet’s '
      'own gloss on the first. Ibn Bāz draws it out: <em>«whoever singled Allah '
      'out, devoted worship to Him alone and disbelieved in the ṭāghūt — his '
      'property and blood are inviolable, because he is a Muslim in truth; but '
      'whoever did not disbelieve in the ṭāghūt and did not single Allah out, '
      'this one is not a Muslim.»</em>' % ar('مَنْ وَحَّدَ اللهَ')) +
    p('And Ibn Saḥmān notes the grammar of it: %s is <strong>%s</strong> — a '
      'reinforcement of the negation half of the kalimah. Which gives the '
      'sentence the whole lesson can be folded into:'
      % ('«' + ar('وَكَفَرَ بِمَا يُعْبَدُ مِنْ دُونِ اللهِ') + '»',
         ar('تَأْكِيدٌ لِلنَّفْي'))) +
    box('<p style="margin:0;font-size:.95rem">Declaring the mushrikīn to be '
        'disbelievers is <strong>not an addition to tawḥīd. It is the %s of '
        '%s.</strong> <em>«So its meaning is not completed except by declaring a '
        'disbeliever whoever made for Allah a partner in his worship.»</em></p>'
        % (ar('لَا'), ar('لَا إِلَهَ إِلَّا اللهُ'))))

# ---------------------------------------------------------------- al-Fatihah
b += B.heading('فِي كُلِّ رَكْعَة', 'The Creed You Ask For Seventeen Times a Day')
b += B.sharh(
    p('This is the most striking argument on the ten folios, and it is not a '
      'ruling at all — it is a reading of %s:' % ar('سُورَةُ الفَاتِحَة')) +
    box('<p style="margin:0;font-size:.94rem"><em>«Allah commanded the Muslim to '
        'ask Him <strong>every day, in every prayer, and in every rakʿah</strong>, '
        'that He guide him to the straight path — and that He keep him from the '
        'path of <strong>%s</strong>, and they are the Jews and those like them, '
        '<em>who know that they are upon falsehood and persist upon it</em>; and '
        'keep him from the path of <strong>%s</strong>, who worship without '
        'knowledge and claim that they are upon a guidance while they are upon a '
        'misguidance… <strong>and all of that so that the Muslim may know with '
        'certain knowledge that every religion other than Islam is '
        'false.</strong>»</em></p>'
        % (ar('المَغْضُوبِ عَلَيْهِمْ'), ar('الضَّالِّينَ'))))
b += B.ayah(
    'اهْدِنَا الصِّرَاطَ المُسْتَقِيمَ * صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ '
    'غَيْرِ المَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ',
    'Guide us to the straight path — the path of those upon whom You have '
    'bestowed favour, not of those who earned anger, nor of those who went '
    'astray.',
    'سُورَةُ الفَاتِحَة · 1:6–7')
b += B.prose(
    '<strong>Notice what that does to the argument that this clause is a hard '
    'extra.</strong> It is not an extra; it is in the opening sūrah, and a Muslim '
    'is made to ask for it before every single thing he asks for. <em>A man '
    'cannot recite al-Fātiḥah and hold at the same time that all paths arrive — '
    'in that very rakʿah he asks to be kept off two of them by name.</em> The '
    'two are distinguished, too, and the distinction is instructive: one earned '
    'anger because it <em>knew</em>; the other went astray because it worshipped '
    '<em>without knowledge</em>.')
b += B.sharh(
    p('Two consequences Ibn Bāz draws in the same place:') +
    p('<strong>One — the disbelief is not for want of monotheism alone.</strong> '
      '<em>«As for the Jews and the Christians, when they did not affirm the '
      'truthfulness of Muḥammad ﷺ they became by that disbelievers, astray — '
      '<strong>and if we were to suppose that some of them singled Allah out, '
      'they are still astray, disbelievers, by the consensus of the '
      'Muslims</strong>, for their not believing in Muḥammad ﷺ.»</em>') +
    p('<strong>Two — the taṣdīq is not divisible.</strong> His own example: a man '
      'who says <em>«I worship Allah alone, and I affirm the truthfulness of '
      'Muḥammad in every single thing — <strong>except</strong> in the '
      'prohibition of zinā»</em>, making it lawful — <em>«he becomes by this a '
      'disbeliever by the consensus of the Muslims»</em>; and likewise one who '
      'excepts the prohibition of %s. <em>One exception voids the affirmation, '
      'because the affirmation was of a messenger, not of a list.</em>'
      % ar('اللِّوَاط')))

# ---------------------------------------------------------------- the restraints
b += B.heading('الضَّوَابِط', 'The Restraints — the Longer Half of the Sharḥ')
b += B.prose(
    '<strong>Everything to this point establishes a belief about a category. '
    'None of it licenses a man to go about assigning people to it.</strong> The '
    'sharḥ draws that line in five places, and they are the reason the clause is '
    'safe to teach.')

b += B.sharh(
    p('<strong>١ — The clause concerns what Allah has settled, not what the '
      'scholars dispute.</strong> Ibn Bāz works this out on a live question: the '
      'man who <em>abandons the prayer without denying that it is '
      'obligatory</em>. He reports the ikhtilāf, states his own position, and '
      'then — this is the part that is always dropped — rules on the one who '
      'doubts:') +
    box('<p style="margin:0;font-size:.94rem"><em>«As for one who leaves the '
        'prayer and does not deny its obligation, in this there is '
        '<strong>disagreement among the scholars</strong>. Among them are those '
        'who declared him a disbeliever — <strong>and that is correct</strong>… '
        'and others of the people of knowledge said he does not disbelieve by '
        'that… <strong>And whoever doubts the disbelief of this one is not a '
        'disbeliever, because it is a place of ijtihād among the people of '
        'knowledge</strong>; so whoever saw by the legislated evidences that he is '
        'a disbeliever, it is obligatory upon him to declare him so; and whoever '
        'doubted in that, and the evidences did not become clear to him, and he '
        'held that he does not disbelieve with major disbelief but with lesser '
        'disbelief — <strong>this one is excused in his ijtihād, and does not '
        'become a disbeliever by that.</strong>»</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('And the contrast, immediately after: <em>«As for one who <strong>denies its '
      'obligation</strong> and says: the prayer is not obligatory — <strong>this '
      'one is a disbeliever in the view of all</strong>, and whoever doubts his '
      'disbelief is a disbeliever.»</em> Likewise one who denies the obligation of '
      'the zakāh, or of the fast of Ramaḍān: <em>«because he is belying Allah and '
      'His Messenger, and belying the consensus of the Muslims.»</em>'))
b += table([
    thead3('the case', 'the ruling', 'one who doubts <em>this</em> case'),
    row3('denies the obligation of %s, %s or %s'
         % (ar('الصَّلَاة'), ar('الزَّكَاة'), ar('الصَّوْم')),
         'a disbeliever <strong>in the view of all</strong> — it is %s of Allah, '
         'His Messenger and the ijmāʿ' % ar('تَكْذِيب'),
         '<strong>himself a disbeliever</strong>, after the evidence is made '
         'clear to him'),
    row3('abandons the prayer <em>without</em> denying its obligation',
         'a place of <strong>ijtihād</strong> — Ibn Bāz: a disbeliever, and that '
         'is correct; others: %s' % ar('كُفْرٌ دُونَ كُفْر'),
         '<strong>not a disbeliever</strong> — he is %s'
         % ar('مَعْذُورٌ فِي اجْتِهَادِه')),
])
b += B.prose(
    '<strong>That one table is the whole difference between this nullifier and '
    'recklessness.</strong> «Doubt is disbelief» was never said of doubt as such; '
    'it was said of doubt about <em>what Allah has already settled</em>. Where '
    'the scholars still differ, the man who suspends is not breaking the clause '
    '— <em>he is doing what a student is supposed to do.</em>')

b += B.sharh(
    p('<strong>٢ — %s means establishing the evidence, each according to his '
      'state.</strong> He was asked about those who stipulate that the proof be '
      'established only by a scholar, so that when a layman falls into something '
      'he is told <em>«no, you are not a scholar»</em>:' % ar('إِقَامَةُ الحُجَّة')) +
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><em>«Establishing the '
        'ḥujjah means: <strong>establishing the evidence</strong>. This is '
        'establishing the ḥujjah — <strong>each according to his state.</strong>»'
        '</em></p>'
        '<p style="margin:0;font-size:.94rem"><em>«It suffices that the ḥujjah be '
        'established by clarifying the truth with its evidences… by the people of '
        'knowledge <strong>even if they are not mujtahids</strong>; rather it '
        'suffices that they know the legislated evidences from the Book of Allah '
        'and the Sunnah of His Messenger ﷺ in what they are calling him to.»'
        '</em></p>') +
    p('So the bar is not a credential. <em>It is that the evidence actually '
      'reached the man, in a form he could receive</em> — and that it reached '
      '<strong>him</strong>, which is what «each according to his state» is '
      'protecting.'))

b += B.sharh(
    p('<strong>٣ — What the ʿāmmī may say, and what he does with the rest.</strong> '
      'Asked whether the layman is kept from this altogether, the answer divides '
      'the ground in two:') +
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><em>«<strong>The ʿāmmī does '
        'not declare anyone a disbeliever except by evidence.</strong> The ʿāmmī '
        'has no knowledge — <strong>poor fellow</strong>.»</em></p>'
        '<p style="margin:0 0 .5rem;font-size:.94rem"><em>«But if he has '
        'knowledge of a specific thing — like one who denies the prohibition of '
        'zinā — <strong>then this one disbelieves in the view of the layman and '
        'the specialist alike; there is no ambiguity in it.</strong> If someone '
        'said: zinā is lawful — he disbelieves in the view of everyone. This is '
        'something that does not need evidences… or he said: shirk is permitted, '
        'it is allowed for people to worship other than Allah — does anyone doubt '
        'the disbelief of this one?… or he says: the prayer is not obligatory, '
        'whoever wishes prays and whoever wishes does not pray.»</em></p>'
        '<p style="margin:0;font-size:.94rem"><em>«<strong>%s</strong> — '
        'suspending judgement — is in the problematic matters, which may be '
        'hidden from the layman.»</em></p>' % ar('التَّوَقُّف')) +
    p('Note the tone of %s. <em>The restraint is not contempt for the layman; it '
      'is protection of him.</em> And note that the division is not by rank but '
      'by <strong>clarity</strong> — the matters named are ones where no '
      'evidence-gathering is required, because the denial is of something the '
      'religion is known by.' % ('«' + ar('مِسْكِين') + '»')) +
    p('He also names the cases we do affirm, and the list is pointed: '
      '<strong>أَبُو جَهْل</strong>, <strong>أَبُو طَالِب</strong>, '
      '<strong>عُتْبَةُ بْنُ رَبِيعَة</strong> and '
      '<strong>شَيْبَةُ بْنُ رَبِيعَة</strong> — <em>«with us is the evidence '
      'that they died upon disbelief.»</em> Abū Ṭālib is in that list, and he is '
      'the Prophet’s own uncle who sheltered him. <em>The ruling does not bend '
      'for kinship, and it does not bend for gratitude either.</em>'))

b += B.sharh(
    p('<strong>٤ — The ḥadīth people reach for, and a forgery people quote.</strong> '
      'The objection is usually made with a ṣaḥīḥ text:') +
    box('<p style="margin:0 0 .5rem;font-size:.94rem">'
        '<span dir="rtl" lang="ar" style="font-size:1.05rem;line-height:2.2">'
        'مَنْ قَالَ لِأَخِيهِ المُسْلِمِ: يَا كَافِرُ، فَقَدْ بَاءَ بِهَا '
        'أَحَدُهُمَا</span></p>'
        '<p style="margin:0;font-size:.94rem"><em>Whoever says to his Muslim '
        'brother “O disbeliever” — it returns upon one of the two of them.</em>'
        '</p>') +
    p('Ibn Bāz’s answer turns on a condition already inside the wording: '
      '<em>«the meaning is: if he said to him “O disbeliever” <strong>and he was '
      'not deserving of it</strong>. But if he <strong>was</strong> deserving of '
      'it, then it returns upon <strong>him</strong> — the one it was said '
      'to.»</em> The ḥadīth is a warning against a <em>false</em> accusation, not '
      'a prohibition of a true description.') +
    p('<strong>And the sharḥ’s footnote stops a forgery that circulates on this '
      'exact subject:</strong> the wording %s — <em>«whoever declares a Muslim a '
      'disbeliever has himself disbelieved»</em> — is graded there as '
      '<strong>%s</strong>, <em>a lie with no basis for it.</em> It is quoted '
      'constantly, and it is not a ḥadīth.'
      % ('«' + ar('مَنْ كَفَّرَ مُسْلِمًا فَقَدْ كَفَرَ') + '»',
         ar('كَذِبٌ لَا أَصْلَ لَه'))))

b += B.sharh(
    p('<strong>٥ — Holding a ruling is not carrying out a sentence.</strong> This '
      'is the restraint that closes the gap everything else leaves open, and the '
      'sharḥ puts it in a footnote:') +
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><em>«But the killing of '
        'apostates and the like of them is <strong>particular to the guardians of '
        'the affairs of the Muslims</strong>.»</em></p>'
        '<p style="margin:0;font-size:.94rem">And '
        '<strong>ابْنُ تَيْمِيَّة</strong>: <em>«<strong>%s</strong> — the one '
        'who enjoins the right — <strong>has no right to killing or '
        'amputation.</strong>»</em></p>' % ar('المُحْتَسِب')) +
    p('So the two things this clause is forever confused with are formally '
      'separated: <em>a sharʿī description, which a student may be obliged to '
      'hold</em>, and <em>the execution of a ḥadd, which belongs to the one in '
      'authority and to nobody else</em>. Not even the muḥtasib — a man whose '
      'office <em>is</em> correcting wrongs — may take it upon himself.'))

b += B.prose(
    'The sharḥ also records the objection raised against the clause — <em>«this '
    'is a matter that chains endlessly; if we carried it through we would declare '
    'the Muslims disbelievers»</em> — and Ibn Saḥmān’s answer is two facts rather '
    'than a counter-argument: the objector <strong>brought no legislated evidence '
    'at all</strong>, only his own reasoning; and <strong>he did not name a '
    'single scholar who holds that the disbeliever is not declared a '
    'disbeliever.</strong> <em>The sharḥ’s own reply to it is considerably '
    'sharper than that, and the substance is what is reproduced here.</em>')

# ---------------------------------------------------------------- the misused verse
b += B.heading('فَمَن شَاءَ فَلْيُؤْمِن', 'A Verse Read Backwards')
b += B.sharh(
    p('Ibn Bāz names a confusion that arrives from the opposite direction — '
      '<em>«and among what some of the ignorant fall into is that he says: '
      '<strong>man is given a choice — if he wishes he disbelieves and if he '
      'wishes he submits</strong>, because Allah says %s»</em>. His answer:'
      % ('«' + ar('فَمَن شَاءَ فَلْيُؤْمِن وَمَن شَاءَ فَلْيَكْفُرْ') + '»')) +
    box('<p style="margin:0;font-size:.94rem"><em>«And this is from the great '
        'affliction — we ask Allah for safety — because this matter is '
        '<strong>a threat, not a giving of choice</strong>; and for this reason '
        'He said after it: <strong>%s</strong>.»</em></p>'
        % ar('إِنَّا أَعْتَدْنَا لِلظَّالِمِينَ نَارًا أَحَاطَ بِهِمْ سُرَادِقُهَا')) +
    p('<em>«Meaning: if he wishes let him believe, and he has the Garden; and if '
      'he wishes let him disbelieve, and he has the Fire.»</em> '
      '<strong>The sentence does not end where the quotation ends</strong> — and '
      'the half that is cut off is the half that tells you which of the two it '
      'was.'))
b += B.ayah(
    'وَقُلِ الحَقُّ مِن رَّبِّكُمْ فَمَن شَاءَ فَلْيُؤْمِن وَمَن شَاءَ '
    'فَلْيَكْفُرْ إِنَّا أَعْتَدْنَا لِلظَّالِمِينَ نَارًا أَحَاطَ بِهِمْ '
    'سُرَادِقُهَا',
    'And say: the truth is from your Lord. So whoever wills — let him believe; '
    'and whoever wills — let him disbelieve. Indeed We have prepared for the '
    'wrongdoers a Fire whose canopy encloses them.',
    'سُورَةُ الكَهْف · 18:29')
b += B.sharh(
    p('He treats %s the same way, and gives <strong>both</strong> scholarly '
      'positions rather than the one that suits him:'
      % ('«' + ar('لَا إِكْرَاهَ فِي الدِّينِ') + '»')) +
    table([
        row('the first view',
            'it was <strong>before the legislating of jihād</strong>; and the '
            'person is still obliged to enter Islam'),
        row('the second view',
            'it concerns <strong>%s and the Majūs</strong> — they are not '
            'compelled once they render the jizyah — and it is therefore '
            '<strong>not abrogated</strong>' % ar('أَهْلُ الكِتَاب')),
    ]) +
    p('<em>«And the intent in every case is that what is meant by it is '
      '<strong>not</strong> the giving of a choice, and it is not meant that there '
      'is no harm in his remaining upon his disbelief — <strong>this is not said '
      'by one who knows what he is saying</strong>»</em> — he is still obliged to '
      'enter Islam, <em>«so that he may rescue himself from the Fire.»</em>') +
    p('<strong>And there is something in that verse the objection never '
      'notices.</strong> Read the rest of it: %s — <em>disbelieve in the ṭāghūt '
      'first, then believe in Allah.</em> The verse produced against this clause '
      'carries <strong>the same two halves, in the same order, as Muslim’s '
      'ḥadīth.</strong>'
      % ('«' + ar('فَمَن يَكْفُرْ بِالطَّاغُوتِ وَيُؤْمِن بِاللَّهِ فَقَدِ '
                  'اسْتَمْسَكَ بِالعُرْوَةِ الوُثْقَى') + '» ' + ar('البَقَرَة ٢:٢٥٦'))))

# ---------------------------------------------------------------- two questions
b += B.heading('مَسْأَلَتَانِ', 'Two Questions He Was Asked')
b += B.sharh(
    p('<strong>The munāfiq.</strong> Asked whether it may be said to the hypocrite '
      '<em>you are a disbeliever</em>: <em>«<strong>If you know that he is a '
      'disbeliever, then he is a disbeliever</strong> — the hypocrites are '
      'disbelievers»</em>, and he cites %s. <em>«So if you know that he belies '
      'Allah and His Messenger, and that he reviles Allah and His Messenger — if '
      'you know this of him, you say to him: you are a disbeliever by this, and '
      'you denounce it upon him.»</em> <strong>The condition is repeated three '
      'times in four lines: %s.</strong> Knowledge of the man, not suspicion of '
      'him.' % (ar('المُنَافِقُون ٦٣:٣'), '«' + ar('إِذَا عَرَفْتَ') + '»')))
b += B.ayah(
    'ذَلِكَ بِأَنَّهُمْ آمَنُوا ثُمَّ كَفَرُوا فَطُبِعَ عَلَى قُلُوبِهِمْ فَهُمْ '
    'لَا يَفْقَهُونَ',
    'That is because they believed, then disbelieved; so their hearts were sealed, '
    'and so they do not understand.',
    'سُورَةُ المُنَافِقُون · 63:3')
b += B.sharh(
    p('<strong>Does the shahādah shield a man from a nullifier?</strong> He was '
      'asked about one who does not pray the obligatory prayers, or who mocks the '
      'Qurʾān, <em>while he testifies that there is no deity but Allah and that '
      'Muḥammad is the Messenger of Allah</em>:') +
    box('<p style="margin:0;font-size:.94rem"><em>«Yes. If one is found who '
        'testifies that there is no deity except Allah and that Muḥammad is the '
        'Messenger of Allah, and he comes with an act that necessitates '
        'disbelief, it is obligatory that he be declared a disbeliever — because '
        '<strong>the Muslim disbelieves if he comes with something from the '
        'nullifiers of Islam</strong>. So the one who testifies… is <strong>not '
        'protected from a nullifier occurring from him</strong>; rather whenever '
        'a nullifier is found from him, he disbelieves by it.»</em></p>') +
    p('<em>The shahādah is what makes a man a Muslim. It was never issued as an '
      'immunity</em> — which is, after all, the premise of the entire matn: a '
      'treatise about the ten things that <strong>nullify</strong> an Islam that '
      'was really there.'))

# ---------------------------------------------------------------- the balance
b += B.heading('وَالمَقْصُودُ بِكُلِّ حَال', 'Where the Sharḥ Chooses to End')
b += B.sharh(
    p('Having spent ten folios establishing that most of mankind is not upon '
      'guidance, the last thing he does is refuse the sweep:') +
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><em>«And there is no doubt '
        'that most of the creation are to the Fire, and the fewer of them to the '
        'Garden»</em> — %s, %s.' % (ar('يُوسُف ١٢:١٠٣'), ar('الأَنْعَام ٦:١١٦')) +
        '</p><p style="margin:0;font-size:.94rem"><em>«<strong>But as for the '
        'statement that all the people of the earth are in the Fire — this is '
        'false speech.</strong> Rather, whoever believed in Allah and the Last '
        'Day is from the people of the Garden; and only the one who disbelieved '
        'in Allah and opposed His command is from the people of the '
        'Fire.»</em></p>', wash='var(--accent-wash)', edge='var(--accent)') +
    p('<strong>So the clause closes where it opened — on proportion rather than a '
      'verdict about the world.</strong> The ruling is about a category Allah '
      'described, applied by evidence, with doubt in a disputed question left as '
      'ijtihād, with the layman suspending where the matter is obscure to him, '
      'and with the sword in nobody’s hand but the ruler’s. <em>Take any one of '
      'those away and you no longer have the clause the author wrote.</em>'))

# ---------------------------------------------------------------- vocab
b += B.vocab([
    ('تَكْذِيب', 'takdhīb', 'belying a report',
     'Declaring a report untrue. The sharḥ’s key move: withholding this ruling is '
     'not harshness towards people but takdhīb of Allah, because the ruling was '
     'already given in the Qurʾān and the Sunnah.'),
    ('الاعْتِقَاد', 'al-iʿtiqād', 'holding as belief',
     'What is actually obliged on the accountable here — to believe what Allah '
     'reported about a category. Distinguish it sharply from issuing rulings '
     'about named individuals.'),
    ('إِقَامَةُ الحُجَّة', 'iqāmat al-ḥujjah', 'establishing the proof',
     'Ibn Bāz: it means establishing the evidence, and it is «each according to '
     'his state»; it may be done by people of knowledge even if they are not '
     'mujtahids.'),
    ('التَّوَقُّف', 'al-tawaqquf', 'suspending judgement',
     'What the layman does in the problematic matters that may be hidden from '
     'him — as opposed to the clear-cut cases, where there is no ambiguity.'),
    ('مَعْذُورٌ فِي اجْتِهَادِه', 'maʿdhūr fī ijtihādihi', 'excused in his ijtihād',
     'Ibn Bāz’s own ruling on one who, examining the evidence, concluded that the '
     'abandoner of prayer commits lesser kufr: he is excused and does not '
     'disbelieve — because that question is a place of ijtihād.'),
    ('كُفْرٌ دُونَ كُفْر', 'kufr dūna kufr', 'a disbelief short of disbelief',
     'The position of a group of the people of knowledge on one who abandons the '
     'prayer without denying its obligation: sinful, and disbelieving with a '
     'lesser disbelief, not the major kufr.'),
    ('تَأْكِيدٌ لِلنَّفْي', 'taʾkīd li-l-nafy', 'reinforcement of the negation',
     'Ibn Saḥmān on «and disbelieves in what is worshipped besides Allah» in '
     'Muslim’s ḥadīth: it reinforces the لَا of لَا إِلَهَ, which is why this '
     'clause is not an addition to the kalimah.'),
    ('المُحْتَسِب', 'al-muḥtasib', 'the one who enjoins the right',
     'Ibn Taymiyyah: he «has no right to killing or amputation» — cited in the '
     'sharḥ to keep holding a ruling separate from carrying out a sentence, which '
     'belongs to the one in authority.'),
    ('المَغْضُوبِ عَلَيْهِمْ', 'al-maghḍūb ʿalayhim', 'those who earned anger',
     'In Ibn Bāz’s reading of al-Fātiḥah: those who know they are upon falsehood '
     'and persist upon it — paired against الضَّالِّينَ, who worship without '
     'knowledge while supposing they are guided.'),
])

# ---------------------------------------------------------------- mcq
b += B.mcq('nq-l04-mcq', [
    ('Which three acts does this clause of the matn name?',
     ['Worshipping, vowing and slaughtering for other than Allah',
      'Not declaring the mushrikīn to be disbelievers, doubting their disbelief, '
      'or declaring their way sound',
      'Mocking the religion, denying a pillar and abandoning the prayer',
      'Calling upon them, asking their intercession and relying upon them'], 1),
    ('Why does Ibn Bāz open the clause by establishing that most of mankind is '
     'upon disbelief?',
     ['To justify severity in rulings',
      'Because the nullifier only has teeth if the category is populated — a man '
      'who decides there are no mushrikūn left never breaks the clause, he '
      'dissolves it',
      'Because the verses were revealed in that order',
      'To prove that guidance is rare among the scholars'], 1),
    ('In Ibn Bāz’s definition, what does tawḥīd itself include?',
     ['Only singling Allah out in supplication',
      'Singling Him out for worship out of belief, truthfulness and action — '
      'together with holding the worship of other than Him false, the worshippers '
      'of other than Him mushrikūn, and barāʾah from them',
      'The five pillars and belief in the six articles',
      'Affirming His lordship and His names without His worship'], 1),
    ('What is notable about the word order of al-Mumtaḥanah 60:4 and al-Zukhruf '
     '43:26?',
     ['The objects of worship are disavowed before the people',
      'The people are disavowed before the objects — «free of you, and of what '
      'you worship»',
      'Neither is mentioned explicitly',
      'Only the fathers are named'], 1),
    ('In what terms does the sharḥ explain WHY this is disbelief?',
     ['That it is a grave sin which leads gradually to disbelief',
      'That it is takdhīb — belying Allah and His Messenger about a ruling they '
      'have already issued, so what is obliged is iʿtiqād, holding a report true',
      'That it entails loving the disbelievers',
      'That it is abandoning an obligation of the limbs'], 1),
    ('How does Ibn Saḥmān define the doubt that this clause makes disbelief?',
     ['Any uncertainty a student feels before studying a question',
      'Wavering between two things — decisive about neither the Messenger’s '
      'truthfulness nor his lying, neither the obligation of prayer nor its '
      'non-obligation',
      'Preferring one scholar’s view over another’s',
      'Asking a question about the foundations'], 1),
    ('What does Ibn Saḥmān say about ignorance as an excuse?',
     ['That it always excuses until the proof is established by a mujtahid',
      'That not every error, ijtihād and ignorance is forgiven — Allah informed '
      'us of the ignorance of many of the disbelievers while expressly declaring '
      'them disbelievers',
      'That it excuses only the layman',
      'That it is never relevant to any ruling'], 1),
    ('How does Muslim’s ḥadīth of Ṭāriq ibn Ashyam bear on this clause?',
     ['It shows that the shahādah alone makes blood and property inviolable',
      'It makes inviolability conditional on TWO things — saying lā ilāha illā '
      'Allāh and disbelieving in what is worshipped besides Allah — so this clause '
      'is the نَفْي half of the kalimah, not an addition to it',
      'It restricts the ruling to the time of the Prophet ﷺ',
      'It concerns only the people of the Book'], 1),
    ('What is Ibn Bāz’s argument from Sūrat al-Fātiḥah?',
     ['That the sūrah must be recited in Arabic',
      'That the Muslim is made to ask, in every rakʿah, to be kept from the path '
      'of those who earned anger and of those who went astray — so that he knows '
      'with certainty that every religion other than Islam is false',
      'That the sūrah contains the names of the prophets',
      'That it proves the obligation of the congregational prayer'], 1),
    ('How does he distinguish المَغْضُوبِ عَلَيْهِمْ from الضَّالِّينَ?',
     ['By era — the former preceded the latter',
      'The first know they are upon falsehood and persist upon it; the second '
      'worship without knowledge, supposing they are upon guidance',
      'By scripture — one had a book and the other did not',
      'By number — the first are the many and the second the few'], 1),
    ('What does the example of the man who affirms Muḥammad ﷺ «in everything '
     'except the prohibition of zinā» establish?',
     ['That major sins expel a man from the religion',
      'That the taṣdīq is not divisible — one exception voids it, because the '
      'affirmation was of a messenger and not of a list',
      'That zinā is the worst of the major sins',
      'That the ḥudūd are a condition of Islam'], 1),
    ('Ibn Bāz holds that one who abandons the prayer without denying its '
     'obligation disbelieves. What does he rule about someone who DOUBTS that?',
     ['That he too is a disbeliever, since doubt in the foundations is disbelief',
      'That he is NOT a disbeliever — because it is a place of ijtihād among the '
      'people of knowledge, and one who concluded it is lesser kufr is excused in '
      'his ijtihād',
      'That he must be silent and may not be asked about it',
      'That his prayer is invalid until he retracts'], 1),
    ('And what of one who denies that the prayer is obligatory at all?',
     ['The same disagreement applies to him',
      'A disbeliever in the view of all — and one who doubts HIS disbelief is a '
      'disbeliever, after the matter is made clear to him',
      'He is sinful but not a disbeliever',
      'The ruling is suspended until a ruler decides'], 1),
    ('What does إِقَامَةُ الحُجَّة require, according to Ibn Bāz?',
     ['That a recognised mujtahid deliver it in person',
      'Establishing the evidence — «each according to his state» — and it suffices '
      'that people of knowledge clarify the truth with its evidences even if they '
      'are not mujtahids',
      'That it be delivered in the Ḥaramayn',
      'That the person request it first'], 1),
    ('What may the ʿāmmī do, and what must he not?',
     ['He may never speak on any of it',
      'He does not declare anyone a disbeliever except by evidence — but where a '
      'man denies something the religion is known by, that is clear «to the layman '
      'and the specialist alike»; in the problematic matters he suspends',
      'He may rule freely, since the matters are from the foundations',
      'He may rule only on the dead'], 1),
    ('Whom does Ibn Bāz name as men we do affirm died upon disbelief?',
     ['Only those named in the Qurʾān by name',
      'Abū Jahl, Abū Ṭālib, ʿUtbah ibn Rabīʿah and Shaybah ibn Rabīʿah — «with us '
      'is the evidence that they died upon disbelief»',
      'The leaders of the Khawārij',
      'Nobody may be named at all'], 1),
    ('How is the ḥadīth «whoever says to his Muslim brother: O disbeliever» '
     'explained?',
     ['It forbids the description absolutely',
      'It concerns saying it to one NOT deserving of it; if he was deserving of '
      'it, it returns upon the one it was said to',
      'It applies only between relatives',
      'It was abrogated by the ḥadīth of Ṭāriq ibn Ashyam'], 1),
    ('What grading does the sharḥ give «whoever declares a Muslim a disbeliever '
     'has himself disbelieved»?',
     ['Ṣaḥīḥ, recorded by Muslim',
      'كَذِبٌ لَا أَصْلَ لَه — a lie with no basis for it; it is not a ḥadīth at '
      'all, though it is quoted constantly',
      'Ḥasan, with a supporting chain',
      'Ḍaʿīf but acted upon in this chapter'], 1),
    ('Who may carry out the sentence on an apostate?',
     ['Any Muslim who has established the proof',
      'The guardians of the affairs of the Muslims — and Ibn Taymiyyah adds that '
      'even the muḥtasib has no right to killing or amputation',
      'The scholars of the land',
      'The family of the one concerned'], 1),
    ('How does Ibn Bāz answer those who read «so whoever wills, let him believe, '
     'and whoever wills, let him disbelieve» as a choice?',
     ['That the verse is abrogated',
      'That it is a threat and not a giving of choice — proven by what '
      'immediately follows it: «indeed We have prepared for the wrongdoers a Fire '
      'whose canopy encloses them»',
      'That it addresses the People of the Book only',
      'That the wording is a question, not a command'], 1),
    ('What two scholarly positions does he report on «there is no compulsion in '
     'religion»?',
     ['That it is general, or that it is specific to women and children',
      'That it preceded the legislating of jihād; or that it concerns Ahl '
      'al-Kitāb and the Majūs who are not compelled once they render the jizyah, '
      'and so is not abrogated',
      'That it is muḥkam, or that its chain is weak',
      'That it is Makkan, or that it is Madinan'], 1),
    ('What does the lesson point out about the rest of al-Baqarah 2:256?',
     ['That it mentions the jizyah explicitly',
      'That it carries the same two halves in the same order as Muslim’s ḥadīth — '
      'disbelieve in the ṭāghūt, then believe in Allah',
      'That it names the Majūs',
      'That it ends with a command to fight'], 1),
    ('What condition does Ibn Bāz repeat when asked about the hypocrite?',
     ['That a ruler must authorise it',
      '«If you know» — knowledge of the man that he belies or reviles Allah and '
      'His Messenger, not suspicion of him',
      'That two witnesses are required',
      'That it may only be said in his absence'], 1),
    ('Does the shahādah protect a man from a nullifier?',
     ['Yes — whoever says it cannot be declared a disbeliever',
      'No — the one who testifies is not protected from a nullifier occurring '
      'from him; whenever one is found from him, he disbelieves by it',
      'Yes, unless he was born outside the lands of Islam',
      'Only if he prays the five prayers'], 1),
    ('How does the sharḥ end the clause?',
     ['By widening the ruling to all the people of the earth',
      'By refusing the sweep — most of the creation are to the Fire, BUT the claim '
      'that all the people of the earth are in the Fire is false speech; whoever '
      'believed in Allah and the Last Day is of the people of the Garden',
      'By listing the remaining nullifiers',
      'By naming the sects that fell into this clause'], 1),
])

b += B.tf('nq-l04-tf', [
    ('مَنْ شَكَّ فِي كُفْرِ تَارِكِ الصَّلَاةِ غَيْرِ الجَاحِدِ '
     'لِوُجُوبِهَا فَهُوَ كَافِرٌ عِنْدَ ابْنِ بَاز.',
     'One who doubts the disbelief of a man who abandons the prayer without '
     'denying its obligation is, according to Ibn Bāz, a disbeliever.', False),
    ('مَنْ جَحَدَ وُجُوبَ الصَّلَاةِ كَافِرٌ عِنْدَ الجَمِيعِ.',
     'One who denies the obligation of the prayer is a disbeliever in the view of '
     'all.', True),
    ('إِقَامَةُ الحُجَّةِ لَا تَكُونُ إِلَّا مِنْ مُجْتَهِدٍ.',
     'Establishing the proof can only be done by a mujtahid.', False),
    ('تَكْفِيرُ المُشْرِكِينَ دَاخِلٌ فِي مَعْنَى لَا إِلَهَ إِلَّا اللهُ، '
     'لَا زِيَادَةٌ عَلَيْهَا.',
     'Declaring the mushrikīn disbelievers is inside the meaning of lā ilāha illā '
     'Allāh, not an addition to it.', True),
    ('قَتْلُ المُرْتَدِّ لِمَنْ ثَبَتَ عِنْدَهُ الدَّلِيلُ مِنْ عَامَّةِ '
     'المُسْلِمِينَ.',
     'Carrying out the sentence on an apostate belongs to any Muslim for whom the '
     'evidence is established.', False),
    ('حَدِيثُ «مَنْ كَفَّرَ مُسْلِمًا فَقَدْ كَفَرَ» لَا أَصْلَ لَهُ.',
     'The ḥadīth «whoever declares a Muslim a disbeliever has himself '
     'disbelieved» has no basis.', True),
])

b += B.memorize(
    'مَنْ قَالَ لَا إِلَهَ إِلَّا اللهُ وَكَفَرَ بِمَا يُعْبَدُ مِنْ دُونِ اللهِ',
    'Hold the <strong>two halves</strong> and most of the confusion around this '
    'clause falls away. An affirmation <em>and</em> a disbelief — and the second '
    'is the Prophet’s own gloss on the first, in the narration '
    '«مَنْ وَحَّدَ اللهَ». <em>So this nullifier is not a severity added onto '
    'tawḥīd; it is the لَا that tawḥīd begins with.</em> And hold the restraint '
    'beside it: <strong>مَعْذُورٌ فِي اجْتِهَادِه</strong> — where the scholars '
    'differ, the one who suspends is not breaking the clause.')

b += B.nav('nq-l03-al-wasait.html',
           'النَّاقِضُ الثَّانِي · اتِّخَاذُ الوَسَائِط',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l04')

B.write('nq-l04-takfir-al-mushrikin.html',
        'النَّاقِضُ الثَّالِث · عَدَمُ تَكْفِيرِ المُشْرِكِين',
        'The Third Nullifier — Not Declaring the Mushrikīn Disbelievers',
        'The third of the ten nullifiers, from the words of Shaykh Ibn Bāz: why '
        'it is takdhīb rather than harshness; how Muslim’s ḥadīth of Ṭāriq ibn '
        'Ashyam makes it the نَفْي half of the kalimah; Ibn Bāz’s argument from '
        'Sūrat al-Fātiḥah; and the restraints the sharḥ spends most of its space '
        'on — iqāmat al-ḥujjah, what the layman may say, the difference between '
        'doubting what Allah settled and doubting what the scholars dispute, and '
        'the ḥudūd belonging to the one in authority.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ الرَّابِع', '4', b)
print('wrote nq-l04-takfir-al-mushrikin.html')
