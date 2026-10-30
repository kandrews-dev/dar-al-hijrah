# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 9 — النَّاقِضُ السَّادِس, part 1: الاسْتِهْزَاء.

Printed folios 146-151 (PDF indices 143-148, offset +3). The clause runs to
printed 158, so part 2 takes 152-158.

Part 1 is the establishing half: the verse, why mockery is disbelief at all,
the transmitted ijmāʿ, and then the one distinction that keeps the clause from
swallowing every careless Muslim.

  * The argument is not «mockery is rude». It is that الاسْتِهْزَاء **is**
    تَنَقُّص and اِحْتِقَار — belittling and contempt — and the objects here are
    Allah, whose attributes are perfection; His Book, which is His speech,
    which is of His attributes of perfection; and His Messenger ﷺ, «the most
    perfect of creation». So the act is not *punished as* contempt of Allah; it
    **is** contempt of Allah.
  * The ijmāʿ is quoted from four named transmitters, not asserted: Ibn
    al-Mundhir («أَجْمَعَ عَوَامُّ أَهْلِ العِلْم» — and Ibn Bāz glosses the word
    عَوَامّ, because it does NOT mean «the common people»), al-Qāḍī ʿIyāḍ,
    Muḥammad ibn Saḥnūn, and Ibn Taymiyyah in *al-Ṣārim al-Maslūl*, with
    Aḥmad's own words by way of Ḥanbal.
  * Five passages on mockery, and all five are about the mockers of the
    prophets and the believers — 83:29-30, 23:109-111, 11:38-39, 9:79 — which
    is the sharḥ's way of showing whose trait this is.
  * The muṣḥaf cases, and the **footnote that matters**: «اسْتِهَانَةً بِه» in
    his wording is **for clarification, not a qualifier** — Ibn Taymiyyah's
    rule from *Kitāb al-Īmān*, with al-Anfāl 8:24 as the parallel. Though the
    footnote itself allows the qualifier to exclude the unintending and the
    coerced.
  * «لَوْ وَحَّدَ اللهَ وَصَدَّقَ الرُّسُلَ ولكن استهزأ بالرسول في شيء… صار
    كافرًا» + the footnote: it is NOT required that he mock all the messengers
    or all the religion.
  * And the **counterweight**, which is the reason this is one lesson and not
    an excerpt: asked about the Ashʿarī position that committing a major sin
    مُسْتَخِفًّا بِهَا is kufr, Ibn Bāz does not follow them — «لَا أَعْلَمُ
    ذَلِك» — and says Ahl al-Sunnah hold him عَاصٍ نَاقِصُ الإِيمَان. And
    separately: «إِظْهَارُ المَعَاصِي لَيْسَ بِكُفْر، إِلَّا إِذَا اسْتَحَلَّ
    ذَلِك؛ لَكِنَّهُ يَكُونُ فِسْقًا». **Taking lightly a sin is not mocking the
    religion**, and the sharḥ draws that line itself.
  * Then the bridge to the next lesson, in his own words: «تَجُرُّهُ
    المَعْصِيَةُ إِلَى الاسْتِهْزَاءِ بِاللهِ» — the same «barīd al-kufr»
    structure as nullifier 5.

Rule 8: «مَنْ بَدَّلَ دِينَهُ فَاقْتُلُوه» is quoted here with neither an
attribution nor a grading, so the page says so and supplies none.
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
    'Quote the sixth nullifier and its daleel, and say what the mockers’ own '
    'excuse in that verse was.',
    'Give the <strong>argument</strong> for why mockery is disbelief — not that '
    'it is rude, but what the act <em>is</em>.',
    'Name <strong>four</strong> scholars from whom the ijmāʿ is transmitted '
    'here, and explain Ibn Bāz’s gloss on the word %s.' % ar('عَوَامّ'),
    'State the ruling where a man affirms tawḥīd and the messengers but mocks '
    '<strong>one</strong> thing — and whether mocking all of them is required.',
    'Explain the footnote’s rule about %s: when a qualifier in a text is for '
    'clarification rather than restriction.' % ('«' + ar('اسْتِهَانَةً بِه') + '»'),
    'State what Ibn Bāz answered about the <strong>Ashʿarī</strong> position on '
    'a major sin committed %s — and what Ahl al-Sunnah hold.'
    % ar('مُسْتَخِفًّا بِهَا'),
    'Distinguish <strong>mocking the religion</strong> from '
    '<strong>taking a sin lightly</strong>, and give his wording for each.',
])

b += B.provenance(146, 151)

b += B.matn(
    'السَّادِس: مَنِ اسْتَهْزَأَ بِشَيْءٍ مِنْ دِينِ الرَّسُولِ ﷺ '
    'أَوْ ثَوَابِهِ أَوْ عِقَابِه — كَفَر؛ وَالدَّلِيلُ قَوْلُهُ تَعَالَى: '
    '﴿وَلَئِنْ سَأَلْتَهُمْ لَيَقُولُنَّ إِنَّمَا كُنَّا نَخُوضُ '
    'وَنَلْعَبُ قُلْ أَبِاللهِ وَآيَاتِهِ وَرَسُولِهِ كُنْتُمْ '
    'تَسْتَهْزِئُونَ﴾.',
    'Some commentaries read «مِنْ دِينِ الله» in place of «مِنْ دِينِ '
    'الرَّسُولِ ﷺ» — the compiler notes the variant.')
b += B.ayah(
    'وَلَئِن سَأَلْتَهُمْ لَيَقُولُنَّ إِنَّمَا كُنَّا نَخُوضُ وَنَلْعَبُ '
    'قُلْ أَبِاللَّهِ وَآيَاتِهِ وَرَسُولِهِ كُنتُمْ تَسْتَهْزِئُونَ',
    'And if you asked them, they would surely say, “We were only jesting and '
    'playing.” Say: was it Allah, and His verses, and His Messenger that you '
    'were mocking?',
    'سُورَةُ التَّوْبَة · 9:65')
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><strong>Read the verse as '
        'an exchange, because that is what it is.</strong> '
        '<em>Their defence is already in it</em> — «we were only jesting and '
        'playing» — <strong>and it is not accepted.</strong> Then the next verse '
        'closes the door: <em>«Do not make excuses; you have disbelieved after '
        'your belief.»</em></p>'
        '<p style="margin:0;font-size:.93rem">So the first thing the daleel '
        'settles is not <em>whether</em> mockery is disbelief. It is '
        '<strong>that “I was only joking” is the mockers’ own plea, answered in '
        'the Qurʾān before anyone thought to offer it.</strong></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))
b += B.prose(
    'Ibn Bāz begins from that: <em>«the Book of Allah has pronounced the '
    'disbelief of whoever mocked the Great Messenger, or anything of the clear '
    'Book of Allah and His wise law»</em> — and then calls the verse '
    '<strong>«a manifest text and a decisive proof»</strong> of the disbelief of '
    'one who mocks Allah, His verses, or His Messenger ﷺ.')
b += B.sharh(
    p('He then relays the consensus, and the wording is careful:') +
    box('<p style="margin:0;font-size:.94rem"><em>«And the scholars of Islām '
        '<strong>in all ages and all lands</strong> are agreed upon the '
        'disbelief of whoever mocked Allah, or His Messenger, or His Book, or '
        '<strong>anything of the religion</strong>; and they are agreed that '
        'whoever mocked anything of that <strong>while being a Muslim</strong>, '
        'he becomes by that a disbeliever, an apostate from Islām.»</em></p>') +
    p('<em>The sharḥ adds in another place that the text is explicit that one '
      'who mocks has disbelieved <strong>%s</strong> — unrestrictedly — '
      '«because it indicates his denial, his rancour and his contempt… so this '
      'shows us that mockery is disbelief and apostasy, and that whenever it '
      'occurs from one who outwardly professes Islām it indicates his hypocrisy '
      'and his disbelief, and he has the ruling of the apostates.»</em>'
      % ar('مُطْلَقًا')) +
    p('The killing is grounded on <em>«%s»</em>. <strong>The sharḥ gives that '
      'ḥadīth here with neither an attribution nor a grading, so this page '
      'supplies none.</strong>' % ar('مَنْ بَدَّلَ دِينَهُ فَاقْتُلُوه')))

# ---------------------------------------------------------------- the argument
b += B.heading('لِمَاذَا كَانَ الاسْتِهْزَاءُ كُفْرًا',
               'The Argument — What the Act Actually Is')
b += B.prose(
    '<strong>This is the part to understand, because without it the clause looks '
    'like a rule about manners.</strong> <em>Ibn Bāz does not argue that mockery '
    'is <strong>punished as</strong> contempt of Allah. He argues that it '
    '<strong>is</strong> contempt of Allah</em> — and he builds it in two steps.')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><em>«And of the decisive proofs of '
        'the disbelief of whoever mocked Allah, or His Messenger, or His Book, is '
        'that <strong>mockery is a belittling and a contempt of the one '
        'mocked</strong> — and Allah, glorified is He, has the attribute of '
        '<strong>perfection</strong>; and His Book is of His speech, and His '
        'speech is of His attributes of perfection; and His Messenger Muḥammad '
        'is <strong>the most perfect of creation</strong> and their master, and '
        'the seal of the messengers, and the intimate friend of the Lord of the '
        'worlds. So whoever mocked Allah, or His Messenger, or His Book, or '
        'anything of His religion — <strong>he has belittled it and held it in '
        'contempt</strong>; and contempt of anything of that, and belittling it, '
        'is <strong>manifest disbelief, and bare hypocrisy, and enmity toward '
        'the Lord of the worlds, and disbelief in His trustworthy '
        'Messenger</strong>.»</em></p>'))
b += B.sharh(table([
    thead3('step', 'the claim', 'what it rests on'),
    row3('١', 'Mockery <strong>is</strong> belittling and contempt — '
         'that is what the act consists of',
         'the meaning of the word itself; <em>no premise about the mocker’s '
         'intention is needed</em>'),
    row3('٢', 'The objects here are <strong>perfection itself</strong>',
         'Allah has the attribute of perfection; <strong>His Book is His '
         'speech, and His speech is of His attributes</strong>; the Messenger ﷺ '
         'is the most perfect of creation'),
    row3('∴', 'Therefore mockery of any of them is contempt <em>of what is '
         'perfect</em> — and that is not compatible with faith in it',
         '<em>which is why he later says the mockery is «a proof that his claim '
         'to faith is false»</em>'),
]))
b += B.prose(
    '<em>Note what step 1 does.</em> It means the clause does '
    '<strong>not</strong> require proving that the man <em>intended</em> to '
    'insult Allah. <strong>The intention to mock is itself the contempt</strong> '
    '— which is exactly why the «we were only jesting» plea in the daleel fails. '
    '<em>Keep that; it is the pivot of the whole clause, and part 2 returns to it '
    'in his words «even if he was joking».</em>')

# ---------------------------------------------------------------- the ijma
b += B.heading('نَقْلُ الإِجْمَاع', 'Four Named Transmitters, Not an Assertion')
b += B.prose(
    'The sharḥ does not leave the ijmāʿ as a claim. <strong>It names who '
    'transmitted it.</strong> <em>That is worth imitating: an ijmāʿ with no '
    'transmitter named is not evidence of anything.</em>')
b += B.sharh(table([
    row('أَبُو بَكْرٍ ابْنُ المُنْذِر',
        '<em>«<strong>The generality of the people of knowledge</strong> are '
        'agreed that the ḥadd of one who reviles the Prophet ﷺ is '
        '<strong>death</strong>; and among those who said it are '
        '<strong>Mālik, al-Layth, Aḥmad and Isḥāq</strong> — and it is the '
        'madhhab of <strong>al-Shāfiʿī</strong>.»</em>'),
    row('the gloss',
        'Ibn Bāz stops to explain the word: <em>«his saying %s is the plural of '
        '%s, and %s here is in the sense of <strong>the group</strong> — so his '
        'intent is that <strong>the groups of scholars</strong> were agreed.»</em> '
        '<em>Not “the laymen”, which is how the word would be misread today.</em>'
        % (ar('عَوَامّ'), ar('عَامَّة'), ar('العَامَّة'))),
    row('القَاضِي عِيَاض',
        '<em>«The Ummah is agreed upon the killing of the one who belittles him '
        'from among the Muslims, and the one who reviles him.»</em>'),
    row('مُحَمَّدُ بْنُ سَحْنُون',
        'of the imāms of the Mālikīs: <em>«The scholars are agreed that the one '
        'who reviles the Prophet and belittles him is a disbeliever, and the '
        'threat has come upon him of Allah’s punishment; and his ruling with the '
        'Ummah is death — <strong>and whoever doubts about his disbelief and his '
        'punishment has disbelieved</strong>.»</em>'),
    row('ابْنُ تَيْمِيَّة',
        'in <em>al-Ṣārim al-Maslūl ʿalā Shātim al-Rasūl</em>, after relaying the '
        'scholars’ statements: <em>«and the precise statement on it is that the '
        'reviler, <strong>if he is a Muslim</strong>, disbelieves and is killed '
        '<strong>without disagreement</strong> — and it is the madhhab of the '
        '<strong>four imāms</strong> and others.»</em>'),
    row('أَحْمَد, via Ḥanbal',
        '<em>«I heard Abū ʿAbdillāh say: whoever reviles the Messenger ﷺ or '
        'belittles him — <strong>Muslim or disbeliever</strong> — upon him is '
        'death; and I hold that he be killed and <strong>not asked to '
        'repent</strong>.»</em>'),
]) + p('And Ibn Bāz closes the transmission with a sentence that is itself a '
       'method: <em>«the speech of the scholars in this chapter is '
       '<strong>much</strong>, and in what we have relayed from them there is '
       '<strong>sufficiency for the seeker of truth</strong>.»</em>'))
b += B.sharh(
    p('He also addresses the worst form directly, because it is the form the '
      'question usually comes in: <em>«and there is no doubt that reviling takes '
      'many kinds, and no doubt that <strong>mockery of him — upon him be peace '
      'and blessings — and belittling him, and likening him to a despicable '
      'animal, is of the ugliest reviling and the greatest belittlement</strong>; '
      'so the doer of that is a disbeliever, his blood and property '
      'forfeit.»</em>') +
    p('<em>Keep in mind through all of this what part 2 makes explicit in his '
      'own words:</em> <strong>the ruling of disbelief and the carrying out of a '
      'killing are two different things</strong>, and the second belongs to the '
      'authority — <em>«as for the killing, that is another matter; the killing '
      'requires a demand for repentance.»</em>'))

# ---------------------------------------------------------------- the verses
b += B.heading('سِمَةُ الكُفَّارِ وَالمُنَافِقِين', 'Whose Trait This Is')
b += B.prose(
    'Then four passages, and the sharḥ’s purpose in stacking them is stated at '
    'the end: <em>mockery of the messengers and the believers is '
    '<strong>a trait of the disbelievers, the hypocrites and the '
    'mushrikīn</strong>.</em> <strong>Not an incidental sin that anyone might '
    'fall into — a marker of a party.</strong>')
b += B.ayah(
    'إِنَّ الَّذِينَ أَجْرَمُوا كَانُوا مِنَ الَّذِينَ آمَنُوا يَضْحَكُونَ '
    'وَإِذَا مَرُّوا بِهِمْ يَتَغَامَزُونَ',
    'Indeed, those who committed crimes used to laugh at those who believed; '
    'and when they passed by them, they would exchange derisive glances.',
    'سُورَةُ المُطَفِّفِين · 83:29–30')
b += B.ayah(
    'فَاتَّخَذْتُمُوهُمْ سِخْرِيًّا حَتَّىٰ أَنسَوْكُمْ ذِكْرِي وَكُنتُم '
    'مِّنْهُم تَضْحَكُونَ',
    'But you took them for mockery, until they made you forget My remembrance, '
    'and you used to laugh at them.',
    'سُورَةُ المُؤْمِنُون · 23:110')
b += B.prose(
    'The sharḥ gives that one with the verse before it and the verse after it, '
    'and the three together are the whole scene: <em>«a party of My slaves used '
    'to say, our Lord, we have believed, so forgive us and have mercy on us, and '
    'You are the best of the merciful»</em> — then the mockery — then '
    '<strong>«indeed I have rewarded them this Day for their patience: it is '
    'they who are the triumphant.»</strong> <em>The mocked are named the winners '
    'in the same breath.</em>')
b += B.ayah(
    'قَالَ إِن تَسْخَرُوا مِنَّا فَإِنَّا نَسْخَرُ مِنكُمْ كَمَا تَسْخَرُونَ',
    '“If you mock us, then we will mock you just as you mock.”',
    'سُورَةُ هُود · 11:38 — the words of Nūḥ عَلَيْهِ السَّلَام')
b += B.ayah(
    'الَّذِينَ يَلْمِزُونَ الْمُطَّوِّعِينَ مِنَ الْمُؤْمِنِينَ فِي '
    'الصَّدَقَاتِ وَالَّذِينَ لَا يَجِدُونَ إِلَّا جُهْدَهُمْ فَيَسْخَرُونَ '
    'مِنْهُمْ سَخِرَ اللَّهُ مِنْهُمْ وَلَهُمْ عَذَابٌ أَلِيمٌ',
    'Those who criticise the believers who give charity voluntarily, and those '
    'who find nothing but their own effort, and ridicule them — Allah will '
    'ridicule them, and for them is a painful punishment.',
    'سُورَةُ التَّوْبَة · 9:79')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><strong>That last verse is the one '
        'to sit with</strong>, because it is the smallest case in the set. '
        '<em>No one in it mocked Allah or the Messenger ﷺ. They mocked a poor '
        'man’s small ṣadaqah</em> — a man «who finds nothing but his own '
        'effort». <strong>And Allah answered it Himself.</strong></p>'
        '<p style="margin:.5rem 0 0;font-size:.92rem"><em>The sharḥ does not '
        'draw a ruling of disbelief from this verse — it uses the four passages '
        'together to show whose trait mockery is. But the smallness of the '
        'occasion is the lesson: the religion of a man is visible in what he '
        'finds funny.</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))

# ---------------------------------------------------------------- the mushaf
b += B.heading('الاسْتِهَانَةُ بِالمُصْحَف', 'Degrading the Muṣḥaf, and a Rule About Qualifiers')
b += B.sharh(
    p('He extends the clause to the physical book, by the same argument:') +
    box('<p style="margin:0;font-size:.94rem"><em>«And likewise if he '
        '<strong>degraded</strong> something of what Allah has magnified, out of '
        'contempt for it and scorn — as if he were to degrade the muṣḥaf, or '
        'urinate on it, or tread on it, or sit on it, or the like of that, '
        '<strong>degrading it</strong> — he disbelieves by consensus; because by '
        'that he becomes one who belittles Allah and holds Him in contempt, '
        '<strong>since the Qurʾān is His speech</strong> — so whoever degraded '
        'it has degraded Allah.»</em></p>') +
    p('And elsewhere, flatly: <em>«if he degraded the muṣḥaf, or smeared it with '
      'filth, or trod on it, or sat on it — <strong>he is a disbeliever, even if '
      'he claims to be a Muslim</strong>; a disbeliever by consensus.»</em> '
      '<em>And: «likewise the one who degrades the muṣḥaf… <strong>while he '
      'knows it is the Book of Allah</strong> — this is a proof that this man has '
      'no faith; he merely claims faith, for had he sound faith it would have barred '
      'him from this deed.»</em>'))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><strong>Now the footnote, '
        'which teaches a rule of reading worth more than the case it '
        'settles.</strong> His words «<strong>%s</strong>» — <em>degrading it</em> '
        '— might be read as a <strong>condition</strong>: that only a '
        'degradation done <em>in order to</em> degrade counts.</p>'
        '<p style="margin:0;font-size:.93rem">The compiler says: <em>«this '
        'description is for <strong>statement and clarification</strong>, and it '
        'is <strong>not a restriction in the ruling</strong> — unless what is '
        'intended by it is to exclude the <strong>unintending</strong> and the '
        '<strong>coerced</strong> and their like.»</em></p>'
        % ar('اسْتِهَانَةً بِه')) +
    p('And he grounds it in Ibn Taymiyyah, from <em>Kitāb al-Īmān</em>: '
      '<em>«and the counterpart of this is His saying — exalted is He — '
      '«<strong>%s</strong>» — and <strong>He does not call except to '
      'that</strong>; so the qualification here has no contrary implication.»</em> '
      'Ibn Taymiyyah gives further examples and concludes: '
      '<em>«so the qualification in all of this is for statement and '
      'clarification, <strong>not to exclude another description</strong>; and '
      'for this reason some of the grammarians say: adjectives on '
      '<strong>definite</strong> nouns are for <strong>clarification</strong>, '
      'not for restriction — and on indefinite nouns, for restriction.»</em>'
      % ar('اسْتَجِيبُوا لِلَّهِ وَلِلرَّسُولِ إِذَا دَعَاكُمْ لِمَا '
           'يُحْيِيكُم')) +
    p('<strong>So: a man does not escape by saying “I trod on it but I did not '
      'mean it as degradation.”</strong> <em>The qualifier describes the act, it '
      'does not add a test. But the footnote keeps the one exclusion that is '
      'real — the man who did not intend the act at all, and the man under '
      'coercion.</em>'))

# ---------------------------------------------------------------- one thing
b += B.heading('وَلَوْ فِي شَيْءٍ وَاحِد', 'One Thing Is Enough — and Why')
b += B.sharh(
    box('<p style="margin:0;font-size:.95rem"><em>«<strong>Even if he affirmed '
        'the oneness of Allah and believed the messengers</strong> — but mocked '
        'the Messenger in <strong>something</strong>, or belittled him in '
        'something, or [mocked] some of the messengers — <strong>he becomes a '
        'disbeliever by that</strong>.»</em></p>') +
    p('<strong>And the footnote states the generalisation outright:</strong> '
      '<em>«so it is not a condition in the disbelief of the mocker that he mock '
      '<strong>all</strong> the messengers, or <strong>all</strong> the religion '
      '— if he mocked <strong>one</strong> messenger, or <strong>one '
      'thing</strong> of what the Messenger brought, he has disbelieved.»</em>') +
    p('<em>That is the same argument you met in the fifth nullifier against '
      '«only if he hates all of it» — and here it is made for mockery.</em> '
      '<strong>And it follows from the argument, not merely from a text:</strong> '
      'if the act <em>is</em> contempt of what is perfect, then contempt of one '
      'thing is contempt of what is perfect. <em>There is no quantity at which '
      'contempt becomes compatible with faith.</em>'))
b += B.sharh(
    p('He then puts it as an analogy that the matn’s own title invites:') +
    box('<p style="margin:0;font-size:.93rem"><em>«So the one who said “there is '
        'no god but Allah”, and brought the two testimonies, or the pillars of '
        'Islām, and then reviled the religion, or reviled Allah, or reviled His '
        'Messenger, or denied what Allah has obliged, or denied some of what '
        'Allah has forbidden — <strong>that testimony is nullified, and he '
        'becomes like one who has broken his purity by one of the '
        'nullifiers</strong>, by the consensus of the people of knowledge. And '
        'for this they mentioned, in the chapter on the ruling of the apostate, '
        '<strong>the many nullifiers</strong>: if he brings one of them, his '
        'Islām is nullified and he comes under the ruling of the '
        'apostates.»</em></p>') +
    p('<em>That is where the book’s own title comes from</em> — %s, the things '
      'that <strong>break</strong> it, the way an act of impurity breaks a '
      'wuḍūʾ. <strong>And the comparison is exact in one respect:</strong> '
      '<em>one is enough, and the state before it does not survive it.</em>'
      % ar('نَوَاقِضُ الإِسْلَام')))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><strong>And then, in the '
        'same breath, he warns about a habit of argument.</strong></p>'
        '<p style="margin:0;font-size:.93rem"><em>«But it is the custom of the '
        '<strong>weak of insight</strong>, or of one whose aim is not sound, to '
        '<strong>cling to the ambiguous, the unrestricted and the general</strong> '
        '— and this is not the way of the people of faith; for Allah has '
        'described the people of faith as <strong>believing in the ambiguous and '
        'returning it to the clear</strong>, while the people of deviation '
        '<strong>follow what is ambiguous of it, seeking discord</strong>.»</em></p>'
        '<p style="margin:.5rem 0 0;font-size:.91rem;color:var(--ink-light)">'
        '<em>The compiler’s footnote says the Shaykh means here to answer those '
        'who argue from the ḥadīth of the man with the slip of paper that one '
        'who leaves the prayer is saved from remaining forever in the Fire.</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))

# ---------------------------------------------------------------- counterweight
b += B.heading('الاسْتِخْفَافُ بِالمَعْصِيَةِ لَيْسَ اسْتِهْزَاءً بِالدِّين',
               'The Line the Sharḥ Draws Itself')
b += B.prose(
    '<strong>Here is why this is a lesson and not an excerpt.</strong> Everything '
    'above would let a reader conclude that a careless Muslim who laughs while '
    'sinning has left Islām. <em>The sharḥ is asked exactly that, twice, and '
    'answers it the other way both times.</em>')
b += B.sharh(
    qa('Some of the <strong>Ashʿarīs</strong> mentioned in their books that one '
       'who commits a major sin <strong>%s</strong> — taking it lightly — '
       '<strong>disbelieves</strong>. Has anyone of Ahl al-Sunnah agreed with '
       'them in that?' % ar('مُسْتَخِفًّا بِهَا'),
       '<em>«<strong>I do not know of that.</strong>… He only commits it '
       'taking it lightly — were it not for his making light of it he would not '
       'have committed it; were it not for his making light of fornication and '
       'disobedience to parents he would not have done it. '
       '<strong>So what Ahl al-Sunnah wa-l-Jamāʿah hold is that he is a sinner, '
       'deficient in faith</strong> — even if he was lax; the reckless make '
       'light.»</em>') +
    p('<strong>Read his reasoning, because it is the decisive point.</strong> '
      '<em>Every</em> deliberate sin involves some making-light of the matter — '
      'that is <em>why</em> a man commits it. <strong>So if making light were '
      'itself disbelief, no sinner would remain a Muslim</strong>, and the whole '
      'category of %s would be empty. <em>The Ashʿarī position is answered not '
      'by a counter-text but by what it would entail.</em>' % ar('عَاصٍ')))
b += B.sharh(
    qa('Is the one who makes light of disobedience — <strong>of the major sins '
       'specifically</strong> — a disbeliever, an apostate? And what is the '
       'standard of this making-light?',
       '<em>«<strong>Making the sins open is not disbelief</strong> — '
       '<strong>unless he deems that lawful</strong>; but he becomes a '
       '<strong>fāsiq</strong>, and severely so, we seek refuge with Allah, and '
       'reckless… And his making light of the sins <strong>indicates the '
       'weakness of his faith</strong>, and that he is <strong>in danger of '
       'leaving Islām</strong>. But if he <strong>permits</strong> them — he '
       'says: fornication is permitted, or wine is permitted — '
       '<strong>then this is disbelief and apostasy from Islām</strong>, we seek '
       'refuge with Allah.»</em>'))
b += B.sharh(table([
    thead3('the act', 'the ruling', 'his word for it'),
    row3('Mocking the religion, or something of it',
         '<strong>كُفْر</strong> — by the consensus relayed above',
         'contempt of what is perfect'),
    row3('Sinning openly, <strong>making light</strong> of the sin',
         '<strong>NOT</strong> disbelief — <em>«إِظْهَارُ المَعَاصِي لَيْسَ '
         'بِكُفْر»</em>',
         '<strong>فِسْق</strong>, and severe; عَاصٍ نَاقِصُ الإِيمَان; '
         '«in danger»'),
    row3('<strong>Permitting</strong> the sin — «fornication is lawful», '
         '«wine is lawful»',
         '<strong>كُفْرٌ وَرِدَّة</strong>',
         '<em>اسْتِحْلَال</em> — the same divider as the fourth nullifier'),
]) + p('<strong>Three rows, and the middle one is the one that gets lost.</strong> '
       '<em>A man laughing while he sins is not, on these folios, a man mocking '
       'the religion — he is a fāsiq in danger. The difference is not a matter of '
       'degree: it is the difference between making light of a '
       '<strong>command one still acknowledges</strong> and holding the '
       '<strong>Legislator</strong> in contempt.</em>'))

# ---------------------------------------------------------------- bridge
b += B.heading('خَطَرُ المَعَاصِي', 'But Not Comfortable Either')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><em>«The danger of the sins is '
        'great, because they are a <strong>making-light of the command of '
        'Allah</strong>, and a laxity with His right, and a boldness against His '
        'sanctities… <strong>Then they drag one to disbelief in Allah.</strong> '
        'How many a sinner whose disobedience dragged him to disbelief in Allah '
        '— while he is among the sinners, suddenly he is among the disbelievers! '
        'The sin drags him to <strong>mockery of Allah</strong>, and to '
        '<strong>mockery of His religion</strong>, and to <strong>deriding what '
        'His prophets brought</strong> — so he joins the disbelievers, we seek '
        'refuge with Allah from that… <strong>his laxity with the prayer at home '
        'drags him until he abandons it</strong>; and when he abandons it, he '
        'falls into disbelief in Allah.»</em></p>') +
    p('<strong>This is the same structure as %s in the fifth '
      'nullifier, and it resolves the same way.</strong> <em>Making light of a '
      'sin is not mockery of the religion — and it is the road by which mockery '
      'of the religion arrives.</em> The first is a rule for judging a man; the '
      'second is a warning about yourself. <em>Holding both is the whole '
      'skill.</em>' % ('«' + ar('المَعَاصِي بَرِيدُ الكُفْر') + '»')))
b += B.prose(
    '<strong>Part 2 takes printed folios ١٥٢–١٥٨</strong>, where the clause '
    'turns from establishing the ruling to the cases: the word said '
    '<em>«with the tongue and not the heart»</em>; mockery <em>«even if he was '
    'joking, or means to annoy someone»</em>; reviling the Ṣaḥābah, where '
    '<strong>all</strong> and <strong>one or two</strong> are given different '
    'rulings; mocking <strong>knowledge and its people</strong>, where Ibn Bāz '
    'says <em>«the correct position is to make the distinction»</em>; and the '
    'ruling on <strong>sitting with</strong> those who mock.')

b += B.vocab([
    ('الاسْتِهْزَاء', 'al-istihzāʾ', 'mockery',
     'The sixth nullifier. Ibn Bāz’s argument: it IS تَنَقُّص and اِحْتِقَار '
     '— belittling and contempt — so of Allah, His Book or His Messenger ﷺ it '
     'is contempt of what is perfect.'),
    ('تَنَقُّص', 'tanaqquṣ', 'belittling',
     'Finding fault with, diminishing. Paired throughout with اِحْتِقَار. The '
     'ijmāʿ transmitted by al-Qāḍī ʿIyāḍ and Ibn Saḥnūn covers المُتَنَقِّص, '
     'not only the open reviler.'),
    ('اِحْتِقَار', 'iḥtiqār', 'contempt',
     'Holding in contempt. «وَاحْتِقَارُ شَيْءٍ مِنْ ذَلِكَ وَتَنَقُّصُهُ '
     'كُفْرٌ ظَاهِرٌ وَنِفَاقٌ سَافِر.»'),
    ('عَوَامّ', 'ʿawāmm', 'the generalities, the groups',
     'In Ibn al-Mundhir’s «أَجْمَعَ عَوَامُّ أَهْلِ العِلْم» — plural of '
     'عَامَّة, and Ibn Bāz glosses it: here it means THE GROUPS of scholars. '
     'NOT «the laymen».'),
    ('الاسْتِهَانَة', 'al-istihānah', 'degrading, treating as of no account',
     'The muṣḥaf cases. And the footnote’s rule: in «اسْتِهَانَةً بِه» the '
     'qualifier is for clarification, not restriction — though it does exclude '
     'the unintending and the coerced.'),
    ('الاسْتِخْفَاف', 'al-istikhfāf', 'making light of a thing',
     'What Ibn Bāz REFUSES to equate with mockery: «إِظْهَارُ المَعَاصِي '
     'لَيْسَ بِكُفْر، إِلَّا إِذَا اسْتَحَلَّ ذَلِك؛ لَكِنَّهُ يَكُونُ '
     'فِسْقًا» — a fāsiq in danger, not an apostate.'),
    ('عَاصٍ نَاقِصُ الإِيمَان', 'ʿāṣin nāqiṣ al-īmān',
     'a sinner, deficient in faith',
     'What Ahl al-Sunnah hold of the man who sins while making light of it — '
     'against the Ashʿarī position Ibn Bāz declines: «لَا أَعْلَمُ ذَلِك».'),
    ('المُتَشَابِه', 'al-mutashābih', 'the ambiguous',
     'What the people of faith return to المُحْكَم, and what the people of '
     'deviation follow «seeking discord». Ibn Bāz names clinging to «the '
     'ambiguous, the unrestricted and the general» as the habit of the weak of '
     'insight.'),
    ('نَوَاقِض', 'nawāqiḍ', 'nullifiers, breakers',
     'The book’s own title, and the analogy is deliberate: one of them nullifies '
     'the testimony «like one who has broken his purity by one of the '
     'nullifiers» — one is enough.'),
])

b += B.mcq('nq-l09-mcq', [
    ('What excuse do the mockers themselves give in the daleel of this clause?',
     ['That they were ignorant',
      '«إِنَّمَا كُنَّا نَخُوضُ وَنَلْعَبُ» — we were only jesting and playing '
      '— and the verse does not accept it',
      'That they were coerced',
      'That they had repented'], 1),
    ('And what does the following verse say?',
     ['That they are forgiven on repentance',
      '«Do not make excuses; you have disbelieved after your belief»',
      'That the matter is left to Allah',
      'That they are hypocrites of the lesser kind'], 1),
    ('What is Ibn Bāz’s ARGUMENT for why mockery is disbelief?',
     ['That it is bad manners and leads to worse',
      'That mockery IS belittling and contempt — and the objects here are '
      'perfection: Allah has the attribute of perfection, His Book is His speech '
      'which is of His attributes, and His Messenger ﷺ is the most perfect of '
      'creation',
      'That the scholars have agreed, without further reason',
      'That it resembles the deeds of the hypocrites'], 1),
    ('What follows from the first step of that argument?',
     ['That intention must be proved',
      'That no premise about intending to insult Allah is needed — the intention '
      'to mock IS the contempt, which is why «we were only joking» fails',
      'That only public mockery counts',
      'That the ruling is probabilistic'], 1),
    ('From whom does the sharḥ transmit the ijmāʿ?',
     ['It asserts it without attribution',
      'Four named transmitters — Ibn al-Mundhir, al-Qāḍī ʿIyāḍ, Muḥammad ibn '
      'Saḥnūn and Ibn Taymiyyah in al-Ṣārim al-Maslūl — plus Aḥmad’s own words '
      'by way of Ḥanbal',
      'From Ibn Taymiyyah alone',
      'From the Four Imāms without naming a book'], 1),
    ('Ibn al-Mundhir said «أَجْمَعَ عَوَامُّ أَهْلِ العِلْم». How does Ibn Bāz '
     'gloss «عَوَامّ»?',
     ['As the common people, as against the scholars',
      'As the plural of عَامَّة, here meaning THE GROUPS — so his intent is that '
      'the groups of scholars were agreed',
      'As the majority against a minority',
      'As the people of the two sanctuaries'], 1),
    ('Which four madhhab-imāms does Ibn al-Mundhir name as holding it?',
     ['Abū Ḥanīfah, Mālik, al-Shāfiʿī, Aḥmad',
      'Mālik, al-Layth, Aḥmad and Isḥāq — and he adds that it is the madhhab of '
      'al-Shāfiʿī',
      'al-Awzāʿī, al-Thawrī, Mālik, Aḥmad',
      'al-Bukhārī, Muslim, Abū Dāwūd, al-Nasāʾī'], 1),
    ('What did Muḥammad ibn Saḥnūn add to the ruling?',
     ['That repentance is accepted',
      'That whoever DOUBTS about his disbelief and his punishment has '
      'disbelieved',
      'That it applies in the Ḥaram only',
      'That the ruling is one of ijtihād'], 1),
    ('Ibn Taymiyyah’s «precise statement» in al-Ṣārim al-Maslūl:',
     ['That the matter is disputed among the four imāms',
      'That the reviler, IF HE IS A MUSLIM, disbelieves and is killed without '
      'disagreement — the madhhab of the four imāms and others',
      'That he is asked to repent three times',
      'That the ruling belongs to the scholars of his land'], 1),
    ('Why does the sharḥ stack 83:29–30, 23:109–111, 11:38–39 and 9:79?',
     ['To establish the number of witnesses required',
      'To show that mockery of the messengers and the believers is a TRAIT of '
      'the disbelievers, the hypocrites and the mushrikīn',
      'To derive the ḥadd',
      'To establish the abrogation of earlier rulings'], 1),
    ('What is remarkable about al-Tawbah 9:79 within that set?',
     ['It names the mockers',
      'It is the smallest case — no one in it mocked Allah or the Messenger ﷺ; '
      'they mocked a poor man’s small ṣadaqah, and Allah answered it Himself',
      'It abrogates the others',
      'It concerns the Ṣaḥābah alone'], 1),
    ('And in al-Muʾminūn, what is said of the mocked?',
     ['That they are avenged in this world',
      '«Indeed I have rewarded them this Day for their patience: it is they who '
      'are the triumphant»',
      'That they are told to retaliate',
      'That their patience is not mentioned'], 1),
    ('On what ground does the ruling extend to degrading the muṣḥaf?',
     ['The sanctity of paper',
      'Because the Qurʾān is HIS SPEECH — «so whoever degraded it has degraded '
      'Allah»',
      'Analogy with the Kaʿbah',
      'The consensus of the Mālikīs alone'], 1),
    ('In «اسْتِهَانَةً بِه», what does the compiler say the qualifier is doing?',
     ['Restricting the ruling to deliberate degradation',
      'Serving for statement and CLARIFICATION, not as a restriction in the '
      'ruling — unless it is meant to exclude the unintending and the coerced',
      'Narrowing it to the muṣḥaf only',
      'Transferring the ruling to the judge'], 1),
    ('Which verse does Ibn Taymiyyah give as the parallel for that rule?',
     ['«وَمَا أَرْسَلْنَاكَ إِلَّا رَحْمَةً لِلْعَالَمِينَ»',
      '«اسْتَجِيبُوا لِلَّهِ وَلِلرَّسُولِ إِذَا دَعَاكُمْ لِمَا يُحْيِيكُمْ» — '
      'and He does not call except to that, so the qualification has no contrary '
      'implication',
      '«فَلَا تَقْعُدُوا مَعَهُمْ»',
      '«إِنَّ الْحُكْمَ إِلَّا لِلَّهِ»'], 1),
    ('And the grammarians’ formulation he cites?',
     ['Adjectives always restrict',
      'Adjectives on DEFINITE nouns are for clarification, not restriction; on '
      'indefinite nouns, for restriction',
      'Adjectives follow the case of the noun only',
      'Qualifiers in reports differ from qualifiers in commands'], 1),
    ('A man affirms the oneness of Allah and believes the messengers, but mocks '
     'the Messenger ﷺ in one thing. The ruling?',
     ['He is a sinner only',
      'He becomes a disbeliever by that',
      'The matter is referred to the scholars',
      'It depends on whether he repeats it'], 1),
    ('Must he mock all the messengers, or all the religion?',
     ['Yes, by the footnote',
      'No — «if he mocked ONE messenger, or ONE thing of what the Messenger '
      'brought, he has disbelieved»',
      'He must mock the essentials of the religion',
      'He must mock in public'], 1),
    ('Why does that follow from the argument and not only from a text?',
     ['Because the scholars agreed on it',
      'Because if the act IS contempt of what is perfect, there is no quantity at '
      'which contempt becomes compatible with faith',
      'Because mockery is always repeated',
      'Because the verse is general in wording'], 1),
    ('What analogy does Ibn Bāz use for the nullifiers?',
     ['Illness and medicine',
      'Breaking one’s purity — one who brings a nullifier «becomes like one who '
      'has broken his purity by one of the nullifiers», by consensus',
      'A debt and its payment',
      'A tree and its branches'], 1),
    ('Whose habit is it, in his words, to cling to «the ambiguous, the '
     'unrestricted and the general»?',
     ['The scholars of kalām',
      'The weak of insight, or one whose aim is not sound — whereas the people '
      'of faith return the ambiguous to the clear',
      'The judges',
      'The common people'], 1),
    ('The Ashʿarīs held that committing a major sin مُسْتَخِفًّا بِهَا is '
     'disbelief. What did Ibn Bāz answer?',
     ['That he agrees with them',
      '«I do not know of that» — and that Ahl al-Sunnah hold such a man to be a '
      'sinner, deficient in faith',
      'That the question is one of ijtihād',
      'That the Ashʿarīs did not say it'], 1),
    ('What is the reasoning that defeats that position?',
     ['A ḥadīth of al-Bukhārī',
      'That EVERY deliberate sin involves some making-light — that is why a man '
      'commits it — so if making light were disbelief, no sinner would remain a '
      'Muslim',
      'The consensus of the Mālikīs',
      'The ḥadīth of the man with the slip of paper'], 1),
    ('«إِظْهَارُ المَعَاصِي لَيْسَ بِكُفْر» — with what exception?',
     ['Unless it is done in the mosque',
      'Unless he DEEMS IT LAWFUL — «he says: fornication is permitted, or wine '
      'is permitted; then this is disbelief and apostasy»',
      'Unless he repeats it',
      'Unless he teaches it to others'], 1),
    ('So what IS the ruling on the man who sins openly and makes light of it?',
     ['Disbelief',
      'Fisq — and severe — a sinner deficient in faith, who «is in danger of '
      'leaving Islām»',
      'Nothing at all',
      'Hypocrisy of belief'], 1),
    ('What is the difference in kind between making light of a sin and mocking '
     'the religion?',
     ['Only a difference of degree',
      'Making light of a COMMAND one still acknowledges, versus holding the '
      'LEGISLATOR in contempt',
      'Private versus public',
      'Once versus repeatedly'], 1),
    ('Ibn Bāz on the danger of sins — what does he say they drag a man to?',
     ['Poverty and humiliation',
      'To disbelief in Allah — «the sin drags him to mockery of Allah, and to '
      'mockery of His religion, and to deriding what His prophets brought»',
      'To the company of the hypocrites only',
      'To doubt about the Hereafter'], 1),
    ('How are those two teachings — fisq not kufr, and sins dragging to kufr — '
     'to be held together?',
     ['The second overrides the first',
      'The first is a rule for JUDGING a man; the second is a warning about '
      'ONESELF',
      'They concern different eras',
      'The first is for scholars and the second for laymen'], 1),
    ('Which earlier nullifier has the same structure in its closing warning?',
     ['The first',
      'The fifth — «المَعَاصِي بَرِيدُ الكُفْر»',
      'The second',
      'The third'], 1),
    ('What does this page supply for «مَنْ بَدَّلَ دِينَهُ فَاقْتُلُوه»?',
     ['A grading of ṣaḥīḥ and attribution to al-Bukhārī',
      'Nothing — the sharḥ gives it here with neither an attribution nor a '
      'grading, so the page says so and supplies none',
      'A grading of ḥasan',
      'An attribution to Mālik'], 1),
])

b += B.tf('nq-l09-tf', [
    ('قَوْلُهُمْ «إِنَّمَا كُنَّا نَخُوضُ وَنَلْعَبُ» عُذْرٌ مَقْبُولٌ فِي '
     'الآيَة.',
     '«We were only jesting and playing» is an accepted excuse in the verse.',
     False),
    ('الاسْتِهْزَاءُ فِي نَفْسِهِ تَنَقُّصٌ وَاحْتِقَارٌ لِلْمُسْتَهْزَأِ '
     'بِه.',
     'Mockery is in itself a belittling and a contempt of the one mocked.',
     True),
    ('«عَوَامُّ أَهْلِ العِلْم» عِنْدَ ابْنِ بَازٍ مَعْنَاهَا عَامَّةُ '
     'النَّاس.',
     'For Ibn Bāz, «ʿawāmm ahl al-ʿilm» means the common people.', False),
    ('يُشْتَرَطُ فِي كُفْرِ المُسْتَهْزِئِ أَنْ يَسْتَهْزِئَ بِالدِّينِ '
     'كُلِّه.',
     'It is a condition in the mocker’s disbelief that he mock the whole '
     'religion.', False),
    ('إِظْهَارُ المَعَاصِي كُفْرٌ عِنْدَ ابْنِ بَاز.',
     'Making sins open is disbelief for Ibn Bāz.', False),
    ('مَنْ أَبَاحَ الزِّنَا أَوِ الخَمْرَ فَهُوَ كَافِرٌ مُرْتَدّ.',
     'Whoever declares fornication or wine permitted is a disbelieving apostate.',
     True),
    ('وَافَقَ ابْنُ بَازٍ الأَشَاعِرَةَ فِي تَكْفِيرِ المُسْتَخِفِّ '
     'بِالكَبِيرَة.',
     'Ibn Bāz agreed with the Ashʿarīs in declaring a disbeliever the one who '
     'makes light of a major sin.', False),
])

b += B.memorize(
    'فَمَنِ اسْتَهْزَأَ بِاللهِ أَوْ رَسُولِهِ أَوْ كِتَابِهِ أَوْ شَيْءٍ '
    'مِنْ دِينِهِ فَقَدْ تَنَقَّصَهُ وَاحْتَقَرَه',
    'Ibn Bāz. <strong>This is the clause’s whole argument in one line</strong>, '
    'and the word to hold is <em>فَقَدْ</em> — he has <em>already</em> '
    'belittled it. <em>The mockery is not evidence of contempt somewhere behind '
    'it; the mockery is the contempt.</em> <strong>And keep beside it the '
    'sentence that stops this clause from swallowing every careless Muslim: '
    '«إِظْهَارُ المَعَاصِي لَيْسَ بِكُفْر، إِلَّا إِذَا اسْتَحَلَّ ذَلِك؛ '
    'لَكِنَّهُ يَكُونُ فِسْقًا.»</strong> %s is contempt of the Legislator; '
    '%s is making light of a command still acknowledged.'
    % (ar('الاسْتِهْزَاء'), ar('الاسْتِخْفَاف')))

b += B.nav('nq-l08-bughd-ma-jaa-bihi.html',
           'النَّاقِضُ الخَامِس',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l09')

B.write('nq-l09-al-istihza.html',
        'النَّاقِضُ السَّادِس · الاسْتِهْزَاء',
        'The Sixth Nullifier, Part 1 — Mockery',
        'The sixth nullifier, from the words of Shaykh Ibn Bāz: the mockers’ own '
        'plea «we were only jesting», answered in the verse itself; the argument '
        'that mockery IS belittling and contempt, and that its objects here are '
        'perfection; the ijmāʿ transmitted from Ibn al-Mundhir, al-Qāḍī ʿIyāḍ, '
        'Ibn Saḥnūn and Ibn Taymiyyah, with Ibn Bāz’s gloss on «ʿawāmm ahl '
        'al-ʿilm»; four Qurʾānic passages on whose trait mockery is; degrading '
        'the muṣḥaf and the rule that a qualifier may be for clarification '
        'rather than restriction; that one thing suffices and why; and the line '
        'the sharḥ draws itself — making light of a sin is fisq and danger, not '
        'mockery of the religion, unless he deems it lawful.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ التَّاسِع', '6', b)
print('wrote nq-l09-al-istihza.html')
