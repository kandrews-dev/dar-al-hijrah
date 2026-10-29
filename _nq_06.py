# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 6 — النَّاقِضُ الرَّابِع, part 2: التَّفْصِيل.

Printed folios 120-131 (PDF indices 117-128, offset +3). This is the half of
the fourth nullifier that governs how part 1 is applied, and it is almost
entirely restraint. Part 3 takes folios 132-135.

What the sharḥ actually says here, in Ibn Bāz's own words:

  * التَّفْصِيل is the أَصْل -- «الأَصْلُ التَّفْصِيل، هَذَا هُوَ الأَصْل».
  * istiḥlāl → كُفْرٌ أَكْبَر, murtadd. Judging wrongly for a bribe, kinship or
    enmity **while knowing he is sinning** → ẓālim, fājir, ʿāṣī, and
    «كُفْرٌ دُونَ كُفْر» as Ibn ʿAbbās and Mujāhid said.
  * The divider is the man's **own** assessment of himself, and the footnote
    collects six separate wordings of it from six separate places.
  * «لَازِمُ الحُكْمِ لَيْسَ بِحُكْم» -- you do not rule a man by what you infer
    his position must entail.
  * «قَرَائِنُ الأَحْوَالِ تَقْتَضِي أَنَّهُمْ يَسْتَجِيزُونَه، لَكِنَّ الحُكْمَ
    بِالرِّدَّةِ أَمْرٌ وَرَاءَ ذَلِكَ.»
  * «إِذَا لَمْ يُصَرِّحُوا بِذَلِكَ وَجَبَ التَّوَقُّف.»
  * And on the risālah «تَحْكِيمُ القَوَانِين» of Shaykh Muḥammad ibn Ibrāhīm:
    **«لَكِنْ أَنَا عِنْدِي فِيهِ تَوَقُّف؛ لِأَنَّ الظَّاهِرَ مَا يَكْفِي»** --
    a recorded reservation by one imām of this school on another's position.
    The compiler's own footnote pushes the other way, carrying al-Fawzān's
    denial that Ibn Ibrāhīm retracted. **Both are named on the page**, because
    the disagreement is part of the record and flattening it would be a lie
    about the school.
  * Fighting is answered at the level of **a capable state**, never an
    individual: «مَنِ الَّذِي يُقَاتِلُه؟» → «الدَّوْلَةُ المُسْلِمَة»; and
    «وَإِذَا مَا هِيَ قَادِرَة؟» → «يَبْقَى عَلَى حَالِهِ بَيْنَهُ وَبَيْنَ
    اللهِ». Even the الخُرُوج question is redirected to a قُوَّةٌ قَادِرَة.
  * «مَسَائِلُ خَطِيرَة، هَذِهِ مَا هِيَ بِسَهْلَة.» -- his own words, and the
    page ends on them.

The questioner in the folio 130-131 exchange is named in the footnote as
Shaykh ʿAbd al-ʿAzīz al-Rājiḥī.

Deliberately NOT done: the ḥadīth «إِلَّا أَنْ تَرَوْا كُفْرًا» is quoted only
by the QUESTIONER here, loosely, and Ibn Bāz's answer does not turn on it. The
page reports the exchange as it stands and does not supply a fuller wording or
a grading the sharḥ did not give at this place.
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
    'State the two states of one who judges by other than what Allah sent down, '
    'and which of them is %s.' % ar('كُفْرٌ أَكْبَر'),
    'Quote Ibn ʿAbbās’s %s and say what it describes.'
    % ('«' + ar('كُفْرٌ دُونَ كُفْر') + '»'),
    'Identify <strong>the one thing</strong> that divides the two states — and '
    'name the exception the compiler adds to it.',
    'Apply the rule %s to the argument that a man who codifies «must» be '
    'deeming it lawful.' % ('«' + ar('لَازِمُ الحُكْمِ لَيْسَ بِحُكْم') + '»'),
    'Say what Ibn Bāz holds about %s, and what he says is obligatory where no '
    'declaration has been made.' % ar('قَرَائِنُ الأَحْوَال'),
    'State Ibn Bāz’s recorded %s on Shaykh Muḥammad ibn Ibrāhīm’s risālah, and '
    'why.' % ar('تَوَقُّف'),
    'Say <strong>who</strong> fights, on what condition, and what the ruling is '
    'where there is no capacity.',
])

b += B.provenance(120, 131)

b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><strong>This is the half of '
        'the fourth nullifier that decides how the first half is applied.</strong> '
        'Part 1 established the ruling on <em>preferring</em> other than Allah’s '
        'judgement. These twelve folios are almost entirely '
        '<strong>restraint</strong> — and that is not a reading imposed on them. '
        'It is Ibn Bāz’s own first word on the subject:</p>'
        '<p style="margin:0;font-size:1.02rem"><span dir="rtl" lang="ar">'
        '«الأَصْلُ التَّفْصِيل، هَذَا هُوَ الأَصْل.»</span><br>'
        '<em style="font-size:.92rem">“The default is <strong>making the '
        'distinction</strong>. This is the default.”</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))

b += B.prose(
    'Before the distinctions, the severity is not softened either. Ibn Bāz calls '
    'referring judgement to <em>«man-made codes and human systems and the customs '
    'of forefathers and the rulings of soothsayers, sorcerers and '
    'astrologers»</em> <strong>«among the ugliest of evil deeds and the greatest '
    'of abominations»</strong>, and <em>«of the greatest hypocrisy, and among the '
    'largest of the emblems of disbelief and oppression and corruption»</em>. '
    '<em>The تَفْصِيل that follows is not a softening of that. It is the answer '
    'to a different question: not «how bad is this?» but «what may be said about '
    'a particular man?»</em>')

# ---------------------------------------------------------------- the division
b += B.heading('طَاغُوتٌ أَكْبَرُ وَطَاغُوتٌ أَصْغَر', 'The Division, in His Own Words')
b += B.sharh(
    p('He opens the detail with a sentence about the word %s itself: '
      '<em>«the ṭāghūt is sometimes a <strong>lesser</strong> ṭāghūt and '
      'sometimes a <strong>greater</strong> ṭāghūt.»</em> Then the division:'
      % ar('الطَّاغُوت')) +
    box('<p style="margin:0;font-size:.94rem"><em>«Whoever judges by other than '
        'what Allah sent down is a ṭāghūt. <strong>If it is along with his '
        'acknowledging and confessing that he is disobeying</strong> — then he is '
        'a ṭāghūt with a <strong>lesser</strong> tyranny. And if he '
        '<strong>deems it lawful and deems it permissible</strong> — he becomes a '
        '<strong>greater</strong> ṭāghūt, and a disbeliever, astray. And if he '
        'judged by other than what Allah sent down <strong>for a bribe, or for '
        'kinship, or for enmity</strong>, or for other causes, <strong>and he '
        'knows that he is disobeying</strong> — he becomes a lesser ṭāghūt, and '
        'becomes an oppressor, a transgressor, a sinner — '
        '<strong>but he does not become a disbeliever with that greater '
        'disbelief.</strong>»</em></p>'))
b += table([
    thead3('his state', 'the ruling', 'what he is'),
    row3('he <strong>deems it lawful</strong> / deems it permissible',
         '<strong>%s</strong> — «a disbeliever, apostate»' % ar('كُفْرٌ أَكْبَر'),
         'a <strong>greater</strong> ṭāghūt'),
    row3('he judges wrongly for a bribe, kinship or enmity, '
         '<strong>knowing he is disobeying</strong>',
         '%s — «as Ibn ʿAbbās and Mujāhid said»'
         % ('<strong>' + ar('كُفْرٌ دُونَ كُفْر') + '</strong>'),
         'a <strong>lesser</strong> ṭāghūt: %s, %s, %s'
         % (ar('ظَالِم'), ar('فَاجِر'), ar('عَاصٍ'))),
])
b += B.sharh(
    p('And he states the same division a second time in different words, which is '
      'worth having because it names the motive: '
      '<em>«the one who contravenes the ruling of Allah is upon two states: if he '
      'contravened the ruling of Allah <strong>deeming that lawful</strong>, he '
      'is a <strong>disbeliever, an apostate</strong>; and if he contravened it '
      '<strong>out of covetousness and desire</strong>, and he '
      '<strong>knows that he is wrong and that he is disobeying</strong>, but he '
      'contravened it for a bribe or for kinship or the like of that — he becomes '
      'by that an oppressor, a sinner, a disbeliever with '
      '<strong>a disbelief short of disbelief, as Ibn ʿAbbās and Mujāhid '
      'said</strong>.»</em>'))
b += B.ayah(
    'وَمَن لَّمْ يَحْكُم بِمَا أَنزَلَ اللَّهُ فَأُولَئِكَ هُمُ الكَافِرُونَ',
    'And whoever does not judge by what Allah has sent down — those are the '
    'disbelievers.',
    'سُورَةُ المَائِدَة · 5:44')
b += B.prose(
    '<strong>This is the verse Ibn ʿAbbās was asked about, and %s is his own '
    'tafsīr of it.</strong> So the qualification is not a later concession made '
    'under pressure; <em>it is as old as the verse’s earliest explanation, from a '
    'Companion, and Mujāhid with him.</em> The sharḥ cites it from a lesson of '
    'Ibn Bāz’s and from his tafsīr of Sūrat al-Māʾidah.'
    % ('«' + ar('كُفْرٌ دُونَ كُفْر') + '»'))

# ---------------------------------------------------------------- the divider
b += B.heading('مَا هُوَ الفَارِق', 'The Divider Is the Man’s Own Verdict on Himself')
b += B.prose(
    'Read the two states again and notice that <strong>the act can be '
    'identical</strong>. What differs is <em>what the man holds about what he is '
    'doing</em>. The sharḥ’s footnote is unusually thorough here: it collects '
    '<strong>six separate wordings of that condition from six separate '
    'places</strong>, and they are worth seeing together, because the repetition '
    'is the argument.')
b += B.sharh(
    table([
        row('wording ١', '<em>«he knows that he is disobeying, and that he has '
            'done a <strong>grave abomination</strong>»</em>'),
        row('wording ٢', '<em>«he knows that he is <strong>an '
            'oppressor</strong>, and that he is <strong>wrong</strong>, and that '
            'it is <strong>a means to disbelief</strong>… but '
            '<strong>so long as he knows that he is wrong and that he is an '
            'oppressor, he does not become a disbeliever</strong> — he is a '
            'sinner, and in it is a kind of disbelief, but it does not become a '
            'greater disbelief, <strong>because he believes that he is wrong, an '
            'oppressor, a sinner, and that the ruling of Allah is what must be '
            'followed</strong>»</em>'),
        row('wording ٣', '<em>«he knows that he is disobeying and that he has '
            '<strong>contravened the truth</strong>»</em>'),
        row('wording ٤', '<em>«he believes that he is… <strong>mistaken and at '
            'fault</strong> in that, and that he is <strong>disobedient to his '
            'Lord</strong>»</em>'),
        row('wording ٥', '<em>«and he knows that he is <strong>disobeying by '
            'it</strong>, and that he is <strong>a criminal by it</strong>»</em>'),
        row('wording ٦', '<em>«he knows that he is disobeying»</em> — the bare '
            'form, in the main text'),
    ]) +
    p('<strong>Every one of the six is a verdict the man passes on '
      'himself.</strong> Not a verdict we pass on him. <em>The nullifier turns on '
      'whether he still holds that Allah’s ruling is the one that must be '
      'followed and that he himself is in the wrong</em> — and nobody but he has '
      'direct access to that.'))
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><strong>And the compiler adds one '
        'precise exception, which closes the obvious hole.</strong> On the word '
        '%s in wording ٢ he says: <em>«his saying “<strong>an oppressor</strong>” '
        '<strong>excludes the one who declares openly that he is just, and that '
        'his ṭāghūtī rulings are justice and equity.</strong>»</em></p>'
        % ('«' + ar('ظَالِم') + '»')) +
    p('<em>That is exactly right, and it is the hinge.</em> The excuse is '
      'available to a man who concedes he is in the wrong. '
      '<strong>It is not available to a man who argues that what he has done is '
      'the better justice</strong> — because that is no longer a sin he admits; '
      'it is the preference the matn named in the first place.'))

# ---------------------------------------------------------------- lawful qawanin
b += B.heading('القَوَانِينُ الَّتِي لَا تُخَالِفُ الشَّرْع', 'A Code Is Not the Problem')
b += B.sharh(
    p('Before anything else is concluded, Ibn Bāz removes a whole category from '
      'the discussion:') +
    box('<p style="margin:0;font-size:.94rem"><em>«The codes, if they do '
        '<strong>not</strong> contravene the Sharīʿah, there is no harm in them — '
        'they are called codes, and they are called regulations. '
        '<strong>So every code that benefits the Muslims and does not contravene '
        'the law of Allah, there is no harm in it</strong> — in '
        '<strong>traffic</strong>, or in the <strong>judiciary</strong>, or in '
        'the <strong>government departments</strong>, or in any place… because '
        'Allah made His law ordering everything, and <strong>it is from the law '
        'of Allah that affairs be regulated</strong>, and that they not be '
        'neglected… so that people proceed upon something clear.»</em></p>') +
    p('<strong>So the word %s settles nothing by itself.</strong> Traffic '
      'regulations, court procedure, the administration of a ministry — the sharḥ '
      'names these three — are not a rival to the Sharīʿah; <em>regulating '
      'affairs is itself something the Sharīʿah asks for.</em> The question is '
      'only ever whether a thing <em>contravenes</em> it.'
      % ar('قَانُون')))

# ---------------------------------------------------------------- lazim al-hukm
b += B.heading('لَازِمُ الحُكْمِ لَيْسَ بِحُكْم', 'The Rule That Answers the Hardest Objection')
b += B.prose(
    'Now the strongest argument on the other side, and the sharḥ puts it fully. '
    'The questioner relays the reasoning of those who do declare the people of '
    'the codes to be disbelievers:')
b += B.sharh(
    box('<p style="margin:0;font-size:.93rem"><em>«They see a difference between '
        'one who <strong>commits</strong> a disobedience — so we rule that he is '
        'a sinful Muslim, or deficient in faith — and one who '
        '<strong>makes the disobedience a binding code for people</strong>. '
        'Because they say: it cannot be conceived of one who set the Sharīʿah '
        'aside — at the furthest remove — and put in its place a binding code, '
        '<strong>even if he says he does not deem it lawful</strong>, '
        '<em>except</em> that he deems it lawful, or holds that it is better for '
        'the people, or the like. And that he differs from the one who judged '
        '<strong>a single particular case</strong> for kinship or for a '
        'bribe.»</em></p>') +
    p('<em>That is a serious objection and it is honestly stated.</em> '
      'Ibn Bāz’s answer is a single rule of uṣūl:') +
    box('<p style="margin:0 0 .5rem;font-size:1.05rem;line-height:2.1">'
        '<span dir="rtl" lang="ar">«بَسِ القَاعِدَة: '
        '<strong>لَازِمُ الحُكْمِ لَيْسَ بِحُكْم</strong>.»</span></p>'
        '<p style="margin:0;font-size:.93rem"><em>“Only the principle: '
        '<strong>the necessary implication of a ruling is not itself a '
        'ruling.</strong>”</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('And he shows it works both ways, which is what makes it an answer rather '
      'than an assertion: <em>«it may be said of the one who judged '
      '<strong>for his own desire or for his relative</strong> that '
      '<strong>he is deeming it lawful — it follows necessarily from him</strong>. '
      '<strong>This is not a ruling — this is between him and Allah.</strong>»</em>') +
    p('<strong>Read what that does to the objection.</strong> The objection says: '
      '<em>a man who does this on that scale cannot be conceived except as '
      'deeming it lawful.</em> The answer does not deny the inference is '
      'reasonable. <em>It denies that an inference is a ruling.</em> And it points '
      'out that the same inference could be pressed on the petty judge taking a '
      'bribe — who is, by consensus of the two positions, not an apostate. '
      '<em>A principle that would convict him too is not doing the work it '
      'claims.</em>'))

# ---------------------------------------------------------------- not by supposition
b += B.heading('وَالحُكْمُ بِغَيْرِ الظَّنّ', 'A Ruling Is Not Made on Supposition')
b += B.prose(
    'This is the most careful passage in the clause, and it is a series of '
    'questions put to him and answered one by one. <strong>Notice that he '
    'concedes the appearance every single time, and still declines the '
    'ruling.</strong>')
b += B.sharh(
    qa('Is that the supposition about them?',
       '<em>«There is no doubt — that is the supposition about them. '
       '<strong>But the ruling is not by supposition</strong>… the supposition '
       'about them is evil and disbelief, <strong>but a person restrains himself '
       'from saying “disbeliever” unless he knows that he deemed it '
       'lawful.</strong>»</em>') +
    qa('Are they like the merely sinful rulers, or is this apparent disbelief?',
       '<em>«<strong>This there is no doubt about: corruption, and the lesser '
       'disbelief — this there is no doubt about.</strong> The discussion is only: '
       'did they disbelieve with a greater disbelief? Are they apostates or not? '
       '<strong>This is a place of consideration.</strong> If they have not '
       'declared openly that it is permitted… <strong>the default is binding: '
       'that they not be declared disbelievers until it is known that they deemed '
       'it permissible and lawful.</strong>»</em>') +
    qa('Do the circumstantial indications not suffice?',
       '<em>«<strong>The circumstantial indications do entail that they deem it '
       'permissible — but the ruling of apostasy is a matter beyond '
       'that.</strong>»</em>') +
    p('And in his own statement, not in answer to a question: '
      '<em>«the <strong>apparent</strong> state of the countries today, but few, '
      'their apparent state is disbelief in Allah and deeming lawful the ruling '
      'by other than what Allah sent down — <strong>but being decisive about that '
      'is a place of consideration</strong> if he claims that he does not permit '
      'it, and that he holds judging by the Sharīʿah to be binding and the '
      'implementing of the codes to be false, but such-and-such drove him to it. '
      '<strong>This is a place of consideration, and Allah knows best.</strong>»</em>') +
    p('<em>«And if they do not declare it openly, <strong>التَّوَقُّف is '
      'obligatory</strong> — it may be desire, and regard for their own '
      'interests…»</em>'))
b += B.prose(
    '<strong>Three times he grants that the outward appearance points one way, '
    'and three times he refuses to convert the appearance into a '
    'verdict.</strong> That is not evasion; it is a distinction between two '
    'different questions. <em>«What does this look like?» is answered: it looks '
    'like istiḥlāl. «What may be ruled?» is answered: not that, until he says '
    'it.</em> And he says plainly what is <em>not</em> in doubt — the fisq and '
    'the lesser kufr are established; only the greater is withheld.')
b += B.sharh(
    p('He also declines to shut the question on anyone else, which is itself '
      'instructive: <em>«this discussion does not prevent the other discussion. '
      'I say: <strong>each one exerts himself in the research and may find what '
      'sets his heart at rest</strong> — because these are '
      '<strong>dangerous matters; these are not easy; they are weighty '
      'matters.</strong>»</em>') +
    p('And the limiting case, which disposes of the simplest version of the '
      'argument: <em>«otherwise, <strong>merely that he judged by other than what '
      'Allah sent down, or ordered that — he does not disbelieve by '
      'that</strong>, like the one who ordered judgement against so-and-so, or '
      'the killing of so-and-so — he does not disbelieve by that '
      '<strong>until he deems it lawful</strong>.»</em>'))

# ---------------------------------------------------------------- the disagreement
b += B.heading('مَوْضِعُ الخِلَاف', 'Where Two Imāms of This School Differed')
b += B.prose(
    'The sharḥ does not hide that the matter was disputed <em>inside</em> this '
    'school, and the student is better served knowing it than not. '
    '<strong>Shaykh مُحَمَّدُ بْنُ إِبْرَاهِيم</strong>, in his risālah '
    '<em>%s</em>, drew the line in a different place:' % ar('تَحْكِيمُ القَوَانِين'))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.93rem"><em>«As for the one of whom '
        'it was said <strong>“a disbelief short of disbelief”</strong>: if he '
        'referred judgement to other than Allah while believing that he is '
        'disobeying and that the ruling of Allah is the truth — '
        '<strong>this is the one from whom the single instance and the like of it '
        'issues</strong>. But <strong>the one who made codes, arranged and '
        'instituted — that is disbelief</strong>, even if they said: we erred, '
        'and the ruling of the Sharīʿah is more just. '
        '<strong>So there is a difference between the one who affirms and '
        'establishes</strong> [Allah’s law, and disobeys it in an instance] '
        '<strong>and the one who made other than the law of Allah the '
        'REFERENCE</strong> — they made it the reference, and this is a disbelief '
        'that removes from the religion.»</em></p>') +
    p('<strong>That is a real distinction and not a careless one:</strong> a '
      'single ruling given wrongly, against a law one still acknowledges, is not '
      'the same act as installing a different law <em>as the authority</em>. '
      '<em>His case is that the second is a change of reference, not an instance '
      'of disobedience</em> — and he held it so even where the men concede the '
      'Sharīʿah is more just.'))
b += B.prose(
    '<strong>And Ibn Bāz, asked about that very risālah, recorded a '
    'reservation.</strong> He confirms he read it and states its position '
    'accurately — <em>«he holds their outward state to be disbelief; meaning, the '
    'one who judges by the codes, that indicates contentment and '
    'istiḥlāl»</em> — and then:')
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:1.03rem;line-height:2.1">'
        '<span dir="rtl" lang="ar">«قَرَأْتُ رِسَالَتَه… '
        '<strong>لَكِنْ أَنَا عِنْدِي فِيهِ تَوَقُّف؛ لِأَنَّ الظَّاهِرَ مَا '
        'يَكْفِي</strong>، مَا يَكْفِي حَتَّى يُعْرَفَ أَنَّهُ '
        '[يَسْتَحِلُّهُ].»</span></p>'
        '<p style="margin:0;font-size:.93rem"><em>“I read his risālah… '
        '<strong>but I have a reservation about it, because the outward is not '
        'enough</strong> — it is not enough until it is known that he deems it '
        'lawful.”</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('<strong>«The outward is not enough» is the whole of Ibn Bāz’s position in '
      'four words</strong>, and it is said here against a named scholar he '
      'otherwise honours — note he says it while asking Allah to forgive him, '
      '%s. <em>This is what disagreement among the imāms of this school actually '
      'looks like: the position stated accurately, the reservation stated '
      'plainly, and the man’s honour intact.</em>'
      % ('«' + ar('اللهُ يَغْفِرُ لَهُ') + '»')) +
    p('<strong>For completeness: the compiler’s own footnote pushes the other '
      'way.</strong> It carries Shaykh <strong>صَالِحٌ الفَوْزَان</strong> '
      'rejecting a claim that Ibn Ibrāhīm had <em>retracted</em> his takfīr — '
      '<em>«this is from lying and fabrication… the Shaykh did not retract, and '
      'what he said is the truth… he was not a hasty man; he used to deliberate '
      'and would not issue a fatwā until he had verified»</em>. '
      '<em>Note what that footnote does and does not establish: it answers a claim '
      'of retraction. It does not answer Ibn Bāz’s تَوَقُّف, which was never a '
      'claim that Ibn Ibrāhīm changed his mind.</em>'))

# ---------------------------------------------------------------- who fights
b += B.heading('مَنِ الَّذِي يُقَاتِل', 'And the Question Everyone Arrives Here to Ask')
b += B.prose(
    'The questioner finally asks it directly, and the answers are short. '
    '<strong>Read who the subject of every verb is.</strong>')
b += B.sharh(
    qa('One who is asked to judge by the law of Allah and refuses?',
       '<em>«<strong>He is fought.</strong>»</em>') +
    qa('He is fought?',
       '<em>«Yes — <strong>so if he fights, he has disbelieved; and if he does '
       'not fight, he has not disbelieved — his ruling is the ruling of the '
       'sinners.</strong>»</em>') +
    qa('Who is it that fights him?',
       '<em>«<strong>The Muslim state.</strong>»</em>') +
    qa('And if it is not able, O Shaykh?',
       '<em>«<strong>He remains as he is, between him and Allah.</strong> Allah '
       'is the One whose help is sought, Allah is the One whose help is '
       'sought.»</em>') +
    p('<strong>Four answers, and three of them are restraints.</strong> The '
      'actor is <em>a state</em>, not a group and not a man. The trigger is '
      '<em>armed defence</em> of the refusal — <strong>«if he fights, he has '
      'disbelieved; and if he does not fight, he has not»</strong>. And where '
      'there is no capacity, the answer is not a lesser action; '
      '<em>it is no action, and a supplication.</em>'))
b += B.sharh(
    p('He grounds the precedent in Abū Bakr’s war on those who withheld the '
      'zakāh, as <strong>ابْنُ تَيْمِيَّة</strong> framed it — cited in the '
      'sharḥ from <em>Fatḥ al-Majīd</em>, on the fighting of the Tatars: '
      '<em>«fighting them is the fighting of apostates, not the fighting of '
      'sinners, <strong>when they defend their falsehood</strong>»</em>. And Ibn '
      'Bāz’s own wording on the parallel: <em>«every group that refuses and '
      'persists and says: we will not pay zakāh, or will not fast Ramaḍān — then '
      'upon <strong>the one in authority</strong> is that he strive against them '
      'until they adhere to the law of Allah, <strong>because their fighting over '
      'this is a kind of denial</strong>.»</em>') +
    p('And elsewhere he makes the sign explicit: <em>«they are not declared '
      'disbelievers for the withholding <strong>unless they fight in defence of '
      'it</strong> — so their fighting in defence of it is '
      '<strong>a sign of their denial</strong>.»</em> <em>The fighting is not the '
      'crime; it is the evidence of the belief that is.</em>'))

b += B.prose(
    '<strong>Finally the question is put in its sharpest form — and the answer is '
    'the one that matters most on this page.</strong> The questioner asks: if we '
    'do not rule them disbelievers, may we not still treat this as the kufr '
    'referred to in %s, and does that not warrant %s against him?'
    % ('«' + ar('إِلَّا أَنْ تَرَوْا كُفْرًا') + '»', ar('الخُرُوج')))
b += B.sharh(
    box('<p style="margin:0;font-size:.93rem"><em>«The apparent meaning of the '
        'speech of many of the people of knowledge is that the like of this, '
        '<strong>if there is a capable force or a capable state</strong> able to '
        'compel him and to fight him, <strong>they have that</strong>, until he '
        'adheres… and Shaykh Taqī al-Dīn Ibn Taymiyyah mentioned the consensus of '
        'the people of knowledge on this: if a state is found that does not '
        'implement the Sharīʿah, or does not prevent wine, or does not prevent '
        'ribā — <strong>it is obligatory upon the Muslim state</strong> to compel '
        'it to this thing, and to fight it if it persists and refuses.»</em></p>') +
    p('<strong>Notice that the answer does not grant what the question '
      'asked.</strong> The question was about %s — rising against a ruler. '
      '<em>The answer is given entirely at the level of a capable force or a '
      'state compelling another state</em>, with Ibn Taymiyyah’s reported '
      'consensus cited for <strong>that</strong>, and with the examples being '
      'wine and ribā as much as the Sharīʿah. <em>Taken with the previous answer '
      '— «who fights him?» «the Muslim state»; «and if it is not able?» «he '
      'remains as he is between him and Allah» — the sharḥ gives no door at all '
      'to an individual or a faction.</em>' % ar('الخُرُوج')))

b += B.prose(
    'And the sentence to leave this page with is his, not mine: '
    '<strong>%s</strong> — <em>«these are dangerous matters; these are not '
    'easy.»</em> A man who has read these twelve folios and come away more '
    'confident of his verdicts has read them backwards.'
    % ar('مَسَائِلُ خَطِيرَة، هَذِهِ مَا هِيَ بِسَهْلَة'))

# ---------------------------------------------------------------- vocab
b += B.vocab([
    ('التَّفْصِيل', 'al-tafṣīl', 'making the distinction',
     'Ibn Bāz: «الأَصْلُ التَّفْصِيل، هَذَا هُوَ الأَصْل» — the default is to '
     'distinguish the states, not to apply one ruling to all of them.'),
    ('الاسْتِحْلَال', 'al-istiḥlāl', 'deeming a thing lawful',
     'The dividing line of the whole clause. Judging by other than Allah’s law '
     'while deeming it lawful or permissible is كُفْرٌ أَكْبَر; without it, the '
     'ruling does not reach that — «until he deems it lawful».'),
    ('كُفْرٌ دُونَ كُفْر', 'kufr dūna kufr', 'a disbelief short of disbelief',
     'Ibn ʿAbbās’s own tafsīr of al-Māʾidah 5:44, and Mujāhid with him. It '
     'describes the man who judges wrongly for a bribe, kinship or desire while '
     'knowing he is disobeying: ẓālim, fājir, ʿāṣī — not an apostate.'),
    ('لَازِمُ الحُكْمِ لَيْسَ بِحُكْم', 'lāzim al-ḥukm laysa bi-ḥukm',
     'an implication is not a ruling',
     'His answer to the argument that a man who codifies «cannot be conceived '
     'except» as deeming it lawful. The inference is not denied — its standing as '
     'a ruling is. «This is between him and Allah.»'),
    ('قَرَائِنُ الأَحْوَال', 'qarāʾin al-aḥwāl', 'circumstantial indications',
     '«They do entail that they deem it permissible — but the ruling of apostasy '
     'is a matter beyond that.» He concedes the appearance and still declines the '
     'verdict.'),
    ('التَّوَقُّف', 'al-tawaqquf', 'suspending judgement',
     'What he says is obligatory where no open declaration has been made — and '
     'also the word he uses for his own reservation on Shaykh Muḥammad ibn '
     'Ibrāhīm’s risālah: «الظَّاهِرُ مَا يَكْفِي».'),
    ('مَحَلُّ نَظَر', 'maḥall naẓar', 'a place of consideration',
     'His recurring verdict on whether the greater kufr has occurred in a '
     'particular case. The fisq and the lesser kufr he calls «no doubt about it»; '
     'the greater he leaves here.'),
    ('المَرْجِع', 'al-marjiʿ', 'the reference, the authority',
     'Shaykh Muḥammad ibn Ibrāhīm’s dividing line: between one who affirms '
     'Allah’s law and disobeys it in an instance, and one who «made other than '
     'the law of Allah THE REFERENCE». Ibn Bāz recorded a tawaqquf on applying it.'),
    ('دِفَاعُ المُسْتَحِلّ', 'difāʿ al-mustaḥill', 'the defence of one who deems it lawful',
     'Armed defence of the refusal is treated as the sign — «if he fights, he has '
     'disbelieved; and if he does not fight, he has not». The parallel is Abū '
     'Bakr’s war on those who withheld the zakāh and fought over it.'),
])

# ---------------------------------------------------------------- mcq
b += B.mcq('nq-l06-mcq', [
    ('What does Ibn Bāz say is the «default» in this clause?',
     ['Declaring the ruling and leaving the detail to the scholars',
      'التَّفْصِيل — making the distinction between the states: «this is the '
      'default»',
      'Suspending all discussion of the subject',
      'Applying the ruling of apostasy and then examining excuses'], 1),
    ('How does he divide the ṭāghūt?',
     ['Into a ruler and a judge',
      'Into a lesser ṭāghūt and a greater ṭāghūt',
      'Into the ancient and the modern',
      'Into one who legislates and one who enforces'], 1),
    ('One who judges by other than Allah’s law while acknowledging that he is '
     'disobeying is —',
     ['a disbeliever, an apostate',
      'a LESSER ṭāghūt: an oppressor, a transgressor, a sinner — «but he does not '
      'become a disbeliever with that greater disbelief»',
      'excused entirely',
      'a hypocrite in creed'], 1),
    ('And one who deems it lawful and deems it permissible?',
     ['He is a sinner only',
      'He becomes a GREATER ṭāghūt — «a disbeliever, astray» — and an apostate',
      'His case is a place of consideration',
      'He is judged by his intention alone'], 1),
    ('Whose tafsīr is «كُفْرٌ دُونَ كُفْر», and of which verse?',
     ['al-Ṭabarī, of al-Nisāʾ 4:65',
      'Ibn ʿAbbās — and Mujāhid with him — of al-Māʾidah 5:44',
      'Ibn Kathīr, of al-Tawbah 9:31',
      'Mujāhid alone, of al-Māʾidah 5:50'], 1),
    ('Why does the lesson point out how old that qualification is?',
     ['To show it is weaker than the main position',
      'Because it is not a later concession — it is as old as the verse’s '
      'earliest explanation, from a Companion',
      'Because Ibn ʿAbbās retracted it',
      'Because it applies only to the Companions’ era'], 1),
    ('What single thing divides the greater from the lesser state?',
     ['The scale of the wrong done',
      'What the man himself holds about what he is doing — whether he still holds '
      'that he is wrong and that Allah’s ruling is what must be followed',
      'Whether he holds public office',
      'Whether he was taught the Sharīʿah'], 1),
    ('What is notable about the footnote on that condition?',
     ['It cites a single wording from a single place',
      'It collects six separate wordings of it from six separate places — and '
      'every one of them is a verdict the man passes on HIMSELF',
      'It contradicts the main text',
      'It attributes the condition to Ibn Taymiyyah'], 1),
    ('What exception does the compiler add to the word «ẓālim» in that condition?',
     ['That it excludes rulers',
      'That it excludes the one who declares openly that he is JUST, and that his '
      'ṭāghūtī rulings are justice and equity',
      'That it excludes the ignorant',
      'That it excludes one who was coerced'], 1),
    ('Why is that exception the hinge?',
     ['Because it narrows the clause to judges',
      'Because the excuse is for a man who concedes he is in the wrong — it is '
      'not available to one who argues that what he did is the better justice, '
      'which is the very preference the matn named',
      'Because it transfers the ruling to the ruler',
      'Because it makes the condition impossible to meet'], 1),
    ('What does Ibn Bāz say about codes that do NOT contravene the Sharīʿah?',
     ['That they are disliked but permitted',
      'That there is no harm in them — in traffic, the judiciary, the government '
      'departments or anywhere; and that regulating affairs is itself from the '
      'law of Allah',
      'That they must be renamed regulations',
      'That they are permitted only in necessity'], 1),
    ('State the objection of those who declare the people of the codes '
     'disbelievers.',
     ['That the codes are of foreign origin',
      'That one who sets the Sharīʿah aside and puts a binding code in its place '
      'cannot be conceived EXCEPT as deeming it lawful or holding it better — and '
      'so differs from one who judged a single case for kinship or a bribe',
      'That codification is an innovation with no precedent',
      'That the codes cannot be reconciled with the ḥudūd'], 1),
    ('What is the rule Ibn Bāz answers it with?',
     ['الضَّرُورَاتُ تُبِيحُ المَحْظُورَات',
      'لَازِمُ الحُكْمِ لَيْسَ بِحُكْم — the necessary implication of a ruling is '
      'not itself a ruling',
      'الأَصْلُ بَرَاءَةُ الذِّمَّة',
      'لَا يُنْسَبُ لِسَاكِتٍ قَوْل'], 1),
    ('How does he show that rule is an answer and not merely an assertion?',
     ['By citing a consensus for it',
      'By showing it cuts both ways — the same inference could be pressed on the '
      'petty judge who ruled for his own relative, and a principle that would '
      'convict him too is not doing the work it claims',
      'By restricting it to matters of creed',
      'By deriving it from al-Māʾidah 5:44'], 1),
    ('What does he say about ruling on the basis of supposition?',
     ['That supposition suffices where the matter is grave',
      'That the supposition about them may be evil and disbelief — «but the ruling '
      'is not by supposition», and a person restrains himself from saying '
      '«disbeliever» unless he knows that he deemed it lawful',
      'That supposition is enough for the scholars but not the laymen',
      'That supposition must be supported by two witnesses'], 1),
    ('Asked whether the قَرَائِنُ الأَحْوَال suffice, what did he answer?',
     ['That they suffice when numerous',
      'That they do entail that they deem it permissible — «but the ruling of '
      'apostasy is a matter BEYOND that»',
      'That they never indicate anything',
      'That they suffice only against a state'], 1),
    ('What does he say is NOT in doubt, and what does he leave as a «place of '
     'consideration»?',
     ['Everything is a place of consideration',
      'The fisq and the LESSER kufr are «no doubt about it»; whether the GREATER '
      'kufr has occurred — whether they are apostates — is the place of '
      'consideration',
      'The greater kufr is certain; the lesser is disputed',
      'Neither can be spoken about at all'], 1),
    ('What is obligatory where no open declaration has been made?',
     ['Applying the ruling of apostasy',
      'التَّوَقُّف — suspending judgement; «it may be desire, and regard for '
      'their own interests»',
      'Emigration from that land',
      'Referring the question to the ruler'], 1),
    ('What does he say of merely judging by other than what Allah sent down, or '
     'ordering it?',
     ['That it is apostasy in every case',
      'That he does not disbelieve by that — like one who ordered judgement '
      'against so-and-so — «until he deems it lawful»',
      'That it is forgiven if done once',
      'That it depends on the scale of the case'], 1),
    ('Where did Shaykh Muḥammad ibn Ibrāhīm draw the line differently?',
     ['He denied the kufr dūna kufr altogether',
      'He applied «kufr dūna kufr» to the single instance, and held that making '
      'codes «the REFERENCE» is a different act — a disbelief removing from the '
      'religion — even if they say they erred and the Sharīʿah is more just',
      'He restricted the clause to the Tatars',
      'He held the whole question to be one of ijtihād'], 1),
    ('What did Ibn Bāz record about that risālah?',
     ['That he endorsed it fully',
      'That he read it and has a تَوَقُّف about it — «because the outward is not '
      'enough; it is not enough until it is known that he deems it lawful»',
      'That he had never seen it',
      'That its attribution is doubtful'], 1),
    ('What does the compiler’s footnote carrying al-Fawzān’s words actually '
     'answer?',
     ['Ibn Bāz’s tawaqquf',
      'A claim that Ibn Ibrāhīm had RETRACTED his position — which is not what Ibn '
      'Bāz’s tawaqquf asserted',
      'The authenticity of the risālah',
      'The grading of Ibn ʿAbbās’s tafsīr'], 1),
    ('Asked «who is it that fights him?», what did Ibn Bāz answer?',
     ['Whoever has the strength among the Muslims',
      'The Muslim STATE',
      'The scholars of the land',
      'The people of the city in which he rules'], 1),
    ('And asked «if it is not able?»',
     ['Then the duty passes to groups within it',
      '«He remains as he is, between him and Allah» — and a supplication, not a '
      'lesser action',
      'Then emigration becomes obligatory on everyone',
      'Then the matter is referred to another state’s scholars'], 1),
    ('What is the trigger, in his wording, for the ruling of disbelief in that '
     'exchange?',
     ['The refusal itself',
      'Armed defence of the refusal — «if he fights, he has disbelieved; and if he '
      'does not fight, he has not disbelieved; his ruling is the ruling of the '
      'sinners»',
      'The passage of a year',
      'The judgement of a council'], 1),
    ('In the zakāh parallel, what is the significance of fighting in defence of '
     'the withholding?',
     ['It is an additional crime only',
      'It is a SIGN of denial — «they are not declared disbelievers for the '
      'withholding unless they fight in defence of it»',
      'It abrogates the obligation',
      'It transfers the ruling to the one in authority'], 1),
    ('The questioner asked whether this warrants الخُرُوج against a ruler. How '
     'was it answered?',
     ['That it does, once the kufr is seen',
      'It was not granted — the answer is given entirely at the level of a capable '
      'force or STATE compelling another state, with Ibn Taymiyyah’s reported '
      'consensus cited for that, and wine and ribā given as parallel examples',
      'That the question may not be asked',
      'That it warrants it only after the scholars agree'], 1),
    ('How does Ibn Bāz characterise this whole subject?',
     ['As a settled matter requiring no research',
      'As «dangerous matters; these are not easy; weighty matters» — and he leaves '
      'each person to exert himself in the research',
      'As a matter of the branches, not the foundations',
      'As a question for rulers alone to consider'], 1),
])

b += B.tf('nq-l06-tf', [
    ('مَنْ حَكَمَ بِغَيْرِ مَا أَنْزَلَ اللهُ لِرَشْوَةٍ وَهُوَ يَعْلَمُ '
     'أَنَّهُ عَاصٍ فَهُوَ كَافِرٌ كُفْرًا أَكْبَر.',
     'One who judges by other than what Allah sent down for a bribe, knowing he '
     'is disobeying, is a disbeliever with the greater disbelief.', False),
    ('«كُفْرٌ دُونَ كُفْرٍ» تَفْسِيرُ ابْنِ عَبَّاسٍ لِآيَةِ المَائِدَة.',
     '«A disbelief short of disbelief» is Ibn ʿAbbās’s tafsīr of the verse of '
     'al-Māʾidah.', True),
    ('القَوَانِينُ الَّتِي لَا تُخَالِفُ الشَّرْعَ لَا بَأْسَ بِهَا عِنْدَ '
     'ابْنِ بَاز.',
     'Codes that do not contravene the Sharīʿah are, for Ibn Bāz, unobjectionable.',
     True),
    ('قَرَائِنُ الأَحْوَالِ تَكْفِي لِلْحُكْمِ بِالرِّدَّة.',
     'Circumstantial indications suffice for a ruling of apostasy.', False),
    ('أَقَرَّ ابْنُ بَازٍ رِسَالَةَ الشَّيْخِ مُحَمَّدِ بْنِ إِبْرَاهِيمَ '
     'بِلَا تَوَقُّف.',
     'Ibn Bāz endorsed Shaykh Muḥammad ibn Ibrāhīm’s risālah without reservation.',
     False),
    ('الَّذِي يُقَاتِلُ مَنِ امْتَنَعَ عَنِ الحُكْمِ بِشَرْعِ اللهِ هُوَ '
     'الدَّوْلَةُ المُسْلِمَة.',
     'The one who fights whoever refuses to judge by the law of Allah is the '
     'Muslim state.', True),
    ('إِذَا لَمْ تَكُنِ الدَّوْلَةُ قَادِرَةً انْتَقَلَ الأَمْرُ إِلَى '
     'الأَفْرَادِ وَالجَمَاعَات.',
     'If the state is not able, the matter passes to individuals and groups.',
     False),
])

b += B.memorize(
    'قَرَائِنُ الأَحْوَالِ تَقْتَضِي أَنَّهُمْ يَسْتَجِيزُونَهُ، لَكِنَّ '
    'الحُكْمَ بِالرِّدَّةِ أَمْرٌ وَرَاءَ ذَلِكَ',
    'Ibn Bāz, asked whether circumstantial evidence was enough. '
    '<strong>He grants the appearance and refuses the verdict in the same '
    'breath</strong> — and that is the shape of the entire تَفْصِيل. Two '
    'different questions: <em>what does this look like?</em> and <em>what may be '
    'ruled?</em> He answers the first honestly — it looks like istiḥlāl — and '
    'answers the second with %s. <em>Beside it keep his other sentence: '
    '«مَسَائِلُ خَطِيرَة، هَذِهِ مَا هِيَ بِسَهْلَة.»</em>'
    % ('«' + ar('الظَّاهِرُ مَا يَكْفِي') + '»'))

b += B.nav('nq-l05-tafdil-ghayr-huda-al-nabi.html',
           'النَّاقِضُ الرَّابِع · part 1',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l06')

B.write('nq-l06-tafsil-al-hukm.html',
        'النَّاقِضُ الرَّابِع · التَّفْصِيل',
        'The Fourth Nullifier, Part 2 — The Distinction',
        'The fourth nullifier’s تَفْصِيل, from the words of Shaykh Ibn Bāz: the '
        'greater and lesser ṭāghūt; Ibn ʿAbbās’s «kufr dūna kufr» on al-Māʾidah '
        '5:44; the six wordings of the one condition that divides them; codes that '
        'do not contravene the Sharīʿah; «lāzim al-ḥukm laysa bi-ḥukm» against the '
        'argument from necessary implication; «the ruling is not by supposition» '
        'and «circumstantial indications… but the ruling of apostasy is a matter '
        'beyond that»; his recorded tawaqquf on Shaykh Muḥammad ibn Ibrāhīm’s '
        'risālah because «the outward is not enough»; and who fights, on what '
        'condition, and what holds where there is no capacity.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ السَّادِس', '6', b)
print('wrote nq-l06-tafsil-al-hukm.html')
