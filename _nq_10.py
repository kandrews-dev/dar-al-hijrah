# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 10 — النَّاقِضُ السَّادِس, part 2: المَسَائِل.

Printed folios 152-158 (PDF indices 149-155, offset +3). Nullifier 7 — السِّحْر
— begins at index 156 → printed 159.

Part 1 established the ruling and drew the line against الاسْتِخْفَاف. Part 2 is
the applications, and the reason it is a lesson of its own is that the answers
**are not uniform**, and the two that are most often quoted are also the two
most often quoted without their own qualifications.

  * «مِثْلُ كَلِمَةٍ يَذْكُرُهَا بِلِسَانِهِ دُونَ قَلْبِه» — the Imām's phrase
    from Kashf al-Shubuhāt, and Ibn Bāz's example is the hard one: «محمد كذاب»
    said while laughing, «وَلَوْ مَا اعْتَقَدَهَا»; or «الله ما هو في السماء»,
    «وَلَوْ يَلْعَب».
  * «أَمَّا الاسْتِهْزَاءُ فَهَذَا مَضْمُونُهُ التَّكْذِيب» — and when the
    questioner pushes back that making people laugh is not takdhīb, the answer
    is «**وَلَوْ** — it indicates making light of the religion». Then:
    «حَتَّى وَلَوْ كَانَ مَازِحًا أَوْ يَقْصِدُ مُضَايَقَةَ شَخْص». The
    footnote's proof is **Pharaoh and the ṭawāghīt of the Arabs**, who mocked
    their prophet **while inwardly believing him** — al-Naml 27:14.
  * **The takfīr/killing distinction, in his own words**: «مَنِ اسْتَهْزَأَ
    بِالدِّينِ يَكْفُرُ بِعَيْنِه… أَمَّا القَتْلُ فَشَيْءٌ آخَر، القَتْلُ
    يَحْتَاجُ إِلَى اسْتِتَابَة.» This is on the page because it is the one
    sentence that keeps the clause from being read as a licence.
  * **Reviling the Ṣaḥābah is given at least six times over these folios and
    the ruling is always two-tiered**: all of them / in general → كُفْر وَرِدَّة
    by the agreement of all the people of knowledge, «لِأَنَّهُمْ نَقَلَةُ
    الدِّين»; **one or two → فِسْق**, and he names Muʿāwiyah and ʿĀʾishah as the
    examples of that tier. Accusing ʿĀʾishah of zinā is كُفْرٌ أَكْبَر, because
    it is takdhīb of Allah who declared her innocent. On Abū Bakr and ʿUmar
    specifically he says «الأَقْرَبُ عِنْدِي كُفْرُه» — a weighed position, not
    a flat one, and the page keeps the wording.
  * **الاسْتِهْزَاءُ بِالعِلْمِ وَأَهْلِه — «وَالصَّوَابُ: التَّفْصِيل»**: at
    the ʿilm, or at the scholars **for it** → ridda. At their clothes, or some
    of them's eagerness for the dunyā, or their customs having no connection to
    the Sharīʿah → **not** ridda, «because it does not go back to the religion».
    With the Lajnah's «يَا ذَقَن» fatwā as the worked example.
  * The muṣḥaf **behind the rows**: «مَحَلُّ نَظَر، وَالأَقْرَب… أَنَّهُ لَا
    حَرَجَ عَلَيْه» — because no insult is intended. Read against part 1's
    muṣḥaf cases, this is the footnote's «unintending» exclusion in practice.
  * حَمْدُ اللهِ عِنْدَ المَعْصِيَة: «هَذَا يَحْتَاجُ إِلَى تَأَمُّل» — and
    then both cases distinguished.
  * الجُلُوسُ مَعَ المُسْتَهْزِئِين: «فَظَاهِرُهُ المُوَافَقَة»; either speak
    or get up; «ظَاهِرُ القُرْآنِ عَدَمُ العُذْر». He does not name the verse at
    this place; the page says so and names al-Nisāʾ 4:140 as the verse that
    carries it.
  * And the clause closes on the **rights of the kalimah**: some rights, if
    unmet, leave a man «as though he never said it»; others only weaken it —
    ضَعِيفُ الإِيمَان, deserving punishment, in danger. Which is the whole book
    in one paragraph.

Rule 8: «هُمْ خَيْرُ النَّاس» is quoted loosely by Ibn Bāz inside an argument,
with no attribution or grading at this place, so the page reports it as his
wording and supplies neither.
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
    'State what Ibn Bāz says the content of mockery is, and what he answers to '
    '«but making people laugh is not denial».',
    'Give his ruling where the mocker <strong>was joking</strong> or '
    '<strong>meant to needle someone</strong> — and the proof the footnote '
    'gives from Pharaoh.',
    'Distinguish, in his own words, <strong>ruling a man a disbeliever</strong> '
    'from <strong>killing him</strong>.',
    'Give the <strong>two tiers</strong> of the ruling on reviling the '
    'Ṣaḥābah, with his own examples of the lower tier, and the reason he gives '
    'for the upper.',
    'State the ruling on accusing ʿĀʾishah رَضِيَ اللهُ عَنْهَا, and why.',
    'Apply %s to mocking knowledge and its people: which case is ridda and '
    'which is not.' % ar('التَّفْصِيل'),
    'State the ruling on <strong>sitting</strong> with those who mock, the two '
    'things that discharge the duty, and which verse carries it.',
    'Explain the %s — and how a man may say it and still be ruined, or say it '
    'and be merely weak.' % ar('حُقُوقُ الكَلِمَة'),
])

b += B.provenance(152, 158)

b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><strong>Part 1 established '
        'the ruling; these seven folios apply it.</strong> And they are a lesson '
        'of their own for one reason: <em>the answers are not uniform.</em></p>'
        '<p style="margin:0;font-size:.93rem">Two of the rulings below are '
        'quoted constantly. <strong>Both of them are two-tiered in the source, '
        'and both are usually quoted without their lower tier.</strong> '
        '<em>Reviling the Ṣaḥābah is not one ruling — it is two. Mocking the '
        'scholars is not one ruling — Ibn Bāz says in so many words '
        '«the correct position is to make the distinction».</em> '
        'And the single sentence that governs all of it is his: '
        '<strong>ruling a man a disbeliever and killing him are two different '
        'things.</strong></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))

# ---------------------------------------------------------------- tongue
b += B.heading('كَلِمَةٌ بِلِسَانِهِ دُونَ قَلْبِه',
               'A Word on the Tongue, Not in the Heart')
b += B.prose(
    'The first question is about a phrase of the Imām Muḥammad ibn ʿAbd '
    'al-Wahhāb’s in <em>Kashf al-Shubuhāt</em>: <em>«like a word he utters with '
    'his tongue without his heart.»</em> <strong>Ibn Bāz is asked what it '
    'means, and his examples are deliberately the worst ones.</strong>')
b += B.sharh(
    box('<p style="margin:0;font-size:.95rem"><em>«An example of a word he '
        'utters with his tongue without his heart: meaning — he laughs, he says: '
        '<strong>“Muḥammad is a liar”</strong>, or <strong>“So-and-so”</strong>… '
        '<strong>and he disbelieves, even if he did not believe it</strong>. Or '
        'he says: <strong>“Allah is not above the heaven”</strong> — '
        '<strong>even if he is playing</strong>. We ask Allah for '
        'soundness.»</em></p>') +
    p('<em>Hold the structure of that.</em> The man <strong>does not hold the '
      'belief</strong>. He is <strong>laughing</strong>. And the ruling lands '
      'anyway — <em>which is exactly what part 1’s argument predicted</em>: if '
      'mockery <strong>is</strong> contempt, then the absence of the '
      'corresponding belief does not remove the contempt. <strong>It is the '
      'uttering of it in jest that is the act.</strong>'))

# ---------------------------------------------------------------- takdhib
b += B.heading('مَضْمُونُهُ التَّكْذِيب', 'Its Content Is Denial — Even in Jest')
b += B.sharh(
    p('Then the exchange that answers the one objection everybody raises:') +
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><strong>Ibn Bāz —</strong> '
        '<em>«As for mockery: <strong>this, its content is denial.</strong> The '
        'mocker is in all of it — because his mockery indicates '
        '<strong>a disease in his heart and a doubt in his heart</strong>.»</em></p>'
        '<p style="margin:0 0 .5rem;font-size:.94rem"><strong>The questioner —</strong> '
        '<em>“The one who mocks is not denying. Like making people laugh.”</em></p>'
        '<p style="margin:0;font-size:.94rem"><strong>Ibn Bāz —</strong> '
        '<em>«<strong>وَلَوْ</strong> — even so. It indicates '
        '<strong>making light of the religion</strong>, and he has no faith with '
        'him to restrain him. We ask Allah for soundness.»</em></p>') +
    p('And in the same place: <em>«<strong>حَتَّى وَلَوْ كَانَ مَازِحًا أَوْ '
      'يَقْصِدُ مُضَايَقَةَ شَخْص</strong>»</em> — '
      '<strong>“even if he was joking, or meant to needle someone.”</strong>'))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><strong>And the footnote’s '
        'proof for that is the thing worth taking away.</strong> Asked how a man '
        'can be ruled a denier when he believes the religion he is mocking, the '
        'footnote answers with the Qurʾān’s own cases: <em>Pharaoh, and the '
        'ṭawāghīt of the Arabs who mocked their prophet '
        '<strong>while inwardly believing him</strong>.</em></p>'
        '<p style="margin:0;font-size:.93rem"><em>«They rejected it '
        '<strong>while their own selves were convinced of it</strong>, out of '
        'injustice and arrogance.»</em> — al-Naml 27:14</p>',
        wash='var(--accent-wash)', edge='var(--accent)'))
b += B.ayah(
    'وَجَحَدُوا بِهَا وَاسْتَيْقَنَتْهَا أَنفُسُهُمْ ظُلْمًا وَعُلُوًّا',
    'And they rejected them, while their own selves were convinced of them — '
    'out of injustice and arrogance.',
    'سُورَةُ النَّمْل · 27:14')
b += B.prose(
    '<strong>So inward assent is not a defence, because the Qurʾān has already '
    'described disbelievers who had it.</strong> <em>That is a serious point and '
    'it cuts against a common sentiment — “he believes really, he just has a '
    'bad mouth.” The verse is about men who were convinced, and it calls what '
    'they did جُحُود.</em>')

# ---------------------------------------------------------------- takfir vs qatl
b += B.heading('التَّكْفِيرُ شَيْءٌ وَالقَتْلُ شَيْءٌ آخَر',
               'The Sentence That Governs the Whole Clause')
b += B.sharh(
    box('<p style="margin:0;font-size:1rem"><em>«Whoever mocks the religion '
        '<strong>is declared a disbeliever specifically</strong>; everyone from '
        'whom a nullifier is found is declared a disbeliever specifically. '
        '<strong>As for the killing — that is another matter. The killing '
        'requires a demand for repentance.</strong>»</em></p>'))
b += B.prose(
    '<strong>Keep that sentence. It is the one that stops this clause being read '
    'as a licence.</strong> <em>Part 1 relayed an ijmāʿ on the killing of one '
    'who reviles the Prophet ﷺ, and relayed Aḥmad’s view that he is not even '
    'asked to repent. Here Ibn Bāz, stating the clause in his own voice, '
    'separates the two: the <strong>ruling</strong> and the '
    '<strong>execution of a sentence</strong>.</em> And the fourth nullifier '
    'already told you who carries out a sentence — not an individual, and not a '
    'group.')

# ---------------------------------------------------------------- amali
b += B.heading('كُفْرٌ عَمَلِيٌّ أَكْبَر', 'Where It Sits in the Kinds of Kufr')
b += B.sharh(
    p('One more statement of principle before the cases, and it is useful '
      'because it places the clause:') +
    box('<p style="margin:0;font-size:.94rem"><em>«There is a '
        '<strong>practical disbelief</strong> that takes one out of the religion '
        '— such as <strong>prostrating to other than Allah</strong>, and '
        '<strong>slaughtering for other than Allah</strong>… likewise if he '
        'reviled the religion, or reviled the Messenger, or mocked Allah or the '
        'Messenger: <strong>a greater practical disbelief, with all of Ahl '
        'al-Sunnah wa-l-Jamāʿah</strong>.»</em></p>') +
    p('<em>Note what he lists it beside</em> — the two acts from the '
      '<strong>first and second nullifiers</strong>. <strong>This is the same '
      'category as prostrating to an idol and slaughtering for a grave:</strong> '
      'an <em>act</em> that nullifies, not merely a belief. <em>Which is why the '
      'mocker’s inward assent does not save him: nobody argues that a man who '
      'prostrates to an idol is excused by believing in his heart that Allah is '
      'one.</em>'))
b += B.sharh(
    p('And he states the particular case of the prayer, and then the full list:') +
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><em>«<strong>Mockery of the '
        'prayer is an independent disbelief, by the consensus of the '
        'Muslims.</strong>»</em></p>'
        '<p style="margin:0;font-size:.93rem"><em>«Whoever mocks the religion — '
        'mocks what the Messenger ﷺ brought: derides <strong>the prayer</strong>, '
        'or <strong>the two testimonies</strong>, or <strong>the zakāh</strong>, '
        'or <strong>the fasting</strong>, or <strong>the ḥajj</strong>, or the '
        'commands of Allah regarding <strong>letting the beard grow</strong> and '
        'trimming the moustache, or the commands of Allah regarding '
        '<strong>goodness to parents</strong> and <strong>maintaining ties of '
        'kinship</strong>, or the commands of Allah regarding '
        '<strong>jihād</strong> in His path, or other than that — '
        '<strong>this one is a disbeliever in Allah, even if he fasts the day '
        'and stands the night, and even if he testifies that there is no god but '
        'Allah and that Muḥammad is the Messenger of Allah ﷺ every '
        'hour</strong>.»</em></p>') +
    p('<em>That closing clause is the same note the matn struck in the fifth '
      'nullifier with «وَلَوْ عَمِلَ بِهِ».</em> <strong>The deeds are not in '
      'dispute. They are simply not what is being weighed.</strong>'))

# ---------------------------------------------------------------- sahabah
b += B.heading('سَبُّ الصَّحَابَة', 'Reviling the Ṣaḥābah — Two Tiers, Never One')
b += B.prose(
    '<strong>This is given six separate times over these folios, and every '
    'single time it comes in two tiers.</strong> <em>It is the most quoted '
    'material in the clause and the most often truncated, so the table below is '
    'built from his wordings rather than summarised.</em>')
b += B.sharh(table([
    thead3('the case', 'his ruling', 'his reason'),
    row3('Reviling them <strong>in general</strong> / all of them',
         '<strong>كُفْر</strong> — «<em>disbelief with '
         '<strong>all</strong> the people of knowledge</em>»; '
         '«<em>disbelief and apostasy from Islām</em>»; and he calls it '
         '<em>«كُفْرٌ مُسْتَقِلّ»</em>, an independent disbelief',
         '«<em>because its meaning is <strong>faulting</strong> them, and that '
         'they are not fit for knowledge to be carried from them</em>»; '
         '«<em>because they are <strong>the transmitters of the '
         'religion</strong></em>»; «<em>because if he reviles them, its meaning '
         'is that they are <strong>not trustworthy</strong>, and that what they '
         'transmitted of Islām <strong>has no soundness</strong></em>»'),
    row3('Reviling <strong>one or two</strong> of them',
         '<strong>فِسْق</strong> — «<em>this has a <strong>tafṣīl</strong>: the '
         'one and the two are <strong>fisq</strong></em>»',
         'his own named examples: «<em>as they revile <strong>Muʿāwiyah</strong>, '
         'or some of them revile <strong>ʿAlī</strong> — فِسْق</em>»; and '
         'elsewhere «<em>like reviling Muʿāwiyah and <strong>ʿĀʾishah</strong> — '
         'this is fisq</em>»'),
    row3('<strong>Abū Bakr and ʿUmar</strong> specifically',
         '«<em><strong>الأَقْرَبُ عِنْدِي كُفْرُه</strong></em>» — '
         '<strong>“what is nearest, in my view, is his disbelief”</strong>',
         '«<em>because Allah was <strong>pleased with them</strong></em>»; and '
         '«<em>because <strong>no one in whose heart is a mustard-seed of '
         'faith</strong> reviles al-Ṣiddīq and ʿUmar and hates them — in what we '
         'believe</em>»'),
    row3('Accusing <strong>ʿĀʾishah</strong> رَضِيَ اللهُ عَنْهَا of zinā',
         '<strong>كُفْرٌ أَكْبَر</strong> — «<em>whoever accused her of zinā '
         '<strong>has disbelieved</strong></em>»',
         '«<em>because he is a <strong>denier of Allah</strong> — for Allah '
         'declared her innocent</em>». <em>And he says that if they hold her '
         'innocence to be unestablished and that she is suspect, it becomes '
         'greater disbelief «because it is takdhīb of Allah».</em>'),
    row3('Denying their <strong>companionship</strong>, or saying they were not '
         'Muslims, or that they <strong>apostatised</strong>',
         '«<em>the apparent ruling is <strong>their disbelief</strong></em>»',
         '«<em>because they have made the Companions of the Messenger ﷺ '
         'disbelievers, and made the bearers of Islām disbelievers — and the '
         'meaning of this is the <strong>nullification of Islām and the '
         'nullification of the religion entirely</strong>. If its bearers were '
         'apostate disbelievers, <strong>what is left for us?</strong>… and at '
         'their head al-Ṣiddīq, and ʿUmar, and ʿUthmān, and Ṭalḥah, and '
         'al-Zubayr, and Saʿīd ibn Zayd, and Saʿd ibn Abī Waqqāṣ and their like '
         '— <strong>so who remains?</strong></em>»'),
]))
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><strong>The reason he gives is '
        'more important than the ruling.</strong> <em>Notice that he never '
        'grounds the upper tier in the honour of the Ṣaḥābah as individuals.</em> '
        'He grounds it in <strong>transmission</strong>: they are '
        '%s — the carriers of the religion. <em>To impugn them as a body is to '
        'say the chain by which the religion reached us is unsound</em>, which '
        'is why he calls it «<strong>the nullification of the religion '
        'entirely</strong>» and asks «so who remains?»</p>'
        '<p style="margin:.5rem 0 0;font-size:.93rem"><strong>And that is '
        'precisely why the lower tier is a different ruling.</strong> <em>A man '
        'who reviles Muʿāwiyah has not said the chain is broken. He has wronged '
        'a Muslim, gravely — فِسْقٌ وَظُلْم — and that is a different '
        'charge.</em></p>' % ar('نَقَلَةُ الدِّين'),
        wash='var(--accent-wash)', edge='var(--accent)'))
b += B.sharh(
    p('He also runs the argument through the Prophet’s ﷺ own testimony: '
      '<em>«the scholars are agreed that whoever <strong>faults</strong> them is '
      'a disbeliever… because its meaning is <strong>denying the '
      'Prophet</strong> — the Prophet says they are <strong>%s</strong>, and '
      'this one faults them.»</em>' % ar('خَيْرُ النَّاس')) +
    p('<em>Ibn Bāz quotes those words of the Prophet ﷺ loosely here, inside the '
      'argument, and the sharḥ gives them at this place with no attribution and '
      'no grading — so this page reports them as his wording and supplies '
      'neither.</em>'))

# ---------------------------------------------------------------- ilm
b += B.heading('الاسْتِهْزَاءُ بِالعِلْمِ وَأَهْلِه',
               '«The Correct Position Is to Make the Distinction»')
b += B.prose(
    '<strong>This one he answers with the word %s in his own mouth</strong>, and '
    'it is the single most useful ruling on these folios, because the case is so '
    'common.' % ('«' + ar('التَّفْصِيل') + '»'))
b += B.sharh(
    box('<p style="margin:0;font-size:.95rem"><em>«And <strong>the correct '
        'position is to make the distinction.</strong> If the mockery is at the '
        '<strong>Sharʿī knowledge</strong>, or at the <strong>scholars on '
        'account of it</strong> — then <strong>there is no doubt that that is '
        'apostasy from Islām</strong>, because it is a belittling of what Allah '
        'has magnified, and a making-light of it, and within that is contempt '
        'for it and denial of it.</em></p>'
        '<p style="margin:.6rem 0 0;font-size:.95rem"><em>But if the mockery at '
        'the scholars <strong>goes back to another matter</strong> — such as '
        '<strong>their clothes</strong>, or <strong>the eagerness of some of '
        'them for the dunyā</strong>, or <strong>their being accustomed to other '
        'than what people are accustomed to</strong>, of customs having '
        '<strong>no connection to the Sharīʿah</strong>, or what resembles that '
        '— then <strong>this and its like is not apostasy from Islām, because it '
        'does not go back to the religion</strong>; rather it goes back to other '
        'matters. And Allah knows best.»</em></p>'))
b += B.sharh(table([
    thead3('what is mocked', 'the ruling', 'the test'),
    row3('Sharʿī knowledge itself',
         '<strong>رِدَّة</strong>',
         'it is belittling <em>what Allah has magnified</em>'),
    row3('A scholar <strong>on account of his knowledge</strong>',
         '<strong>رِدَّة</strong> — «no doubt»',
         'the knowledge is the real object; the man is the occasion'),
    row3('A scholar’s <strong>clothes</strong>, worldliness, or unusual habits '
         'with no Sharʿī connection',
         '<strong>NOT</strong> ridda',
         '«<em>because it does not go back to the religion</em>» — '
         '<em>and note he does not call it permissible either</em>'),
]) + p('<strong>The footnote gives the Lajnah’s worked example, and it is the '
       'whole distinction in two words.</strong> On a man who says '
       '<em>«%s»</em> — “hey, beard” — <em>«if the speaker intended by his '
       'saying it <strong>ridicule</strong>, then that is disbelief; and if he '
       'intended <strong>identification</strong>, then it is not '
       'disbelief.»</em> <em>Same syllables, two rulings, and the difference is '
       'what the words were aimed at.</em>' % ar('يَا ذَقَن')))

# ---------------------------------------------------------------- unintending
b += B.heading('مَحَلُّ نَظَر', 'Where He Declines to Rule')
b += B.sharh(
    qa('Placing the <strong>muṣḥaf behind the rows</strong> in the mosque — '
       'where people lean back against it.',
       '<em>«This is <strong>a place of consideration</strong>, and what is '
       'nearest — and Allah knows best — is that <strong>there is no harm upon '
       'him</strong>; because <strong>he does not intend to degrade them or hold '
       'them in contempt</strong>, and his need is only to lean back; and the one '
       'who placed them there intends to <strong>bring them near the '
       'people</strong> so that they may obtain copies when they wish to read. '
       'But if they were placed <strong>in front</strong>, that would be more '
       'prudent.»</em>') +
    p('<strong>Read that against part 1.</strong> <em>There, treading on a '
      'muṣḥaf is disbelief by consensus and the qualifier «degrading it» was '
      'said to be clarification rather than a condition. Here, leaning on one is '
      '«no harm».</em> <strong>The two are consistent, and the footnote in part '
      '1 told you how:</strong> the one exclusion it preserved was '
      '<em>the unintending</em>. <em>This is that exclusion in practice, from '
      'his own mouth, on a real case in a real mosque.</em>'))
b += B.sharh(
    qa('A man who <strong>praises Allah</strong> at the moment of committing '
       'something forbidden — smoking, drinking, fornication — '
       '<strong>as mockery</strong>. Does he disbelieve?',
       '<em>«<strong>This needs reflection.</strong> If his intent is '
       '<strong>mockery of the religion</strong>, and that there is '
       '<strong>no difference</strong> between praising at sins and praising at '
       'blessings, and that <strong>the religion has no value</strong> — then '
       'this is <strong>greater disbelief</strong>; mockery of the religion is '
       'disbelief: «<em>%s</em>». But if he says: it is an affliction, and '
       'praise be to Allah upon the affliction, and I repent to Allah and turn '
       'back to Him — but it is an affliction, and I praise Allah at '
       'afflictions as I praise Him at blessings, and I ask Him to pardon me and '
       'to accept my repentance — <strong>that is not mockery; there is nothing '
       'in it.</strong>»</em>'
       % ar('قُلْ أَبِاللهِ وَآيَاتِهِ وَرَسُولِهِ كُنْتُمْ تَسْتَهْزِئُون')) +
    p('<strong>«هَذَا يَحْتَاجُ إِلَى تَأَمُّل» is the answer to notice.</strong> '
      '<em>The same words — «al-ḥamdu lillāh» at the moment of a sin — are two '
      'completely different acts, and he will not rule on them until he knows '
      'which one happened.</em> And the second case he describes is not merely '
      'excused; it is a man repenting mid-sin. <em>Nothing on these folios is '
      'read off the surface of an utterance.</em>'))

# ---------------------------------------------------------------- sitting
b += B.heading('الجُلُوسُ مَعَ المُسْتَهْزِئِين', 'Sitting With Them')
b += B.sharh(
    box('<p style="margin:0;font-size:.95rem"><em>«If he sits and '
        '<strong>does not forbid them and stays silent</strong>, then '
        '<strong>its apparent import is agreement</strong>. Otherwise — it is '
        '<strong>obligatory</strong> upon whoever sits with those who speak '
        'falsehood and reject the truth and mock the truth '
        '<strong>that he not sit</strong>; rather <strong>he should get up and '
        'depart</strong>, if he is unable to forbid with the tongue. Otherwise, '
        'let him <strong>forbid and make clear the error</strong> of the one who '
        'spoke falsehood. But if he sits and stays silent, then its meaning is '
        '<strong>agreement</strong>, and there is no power and no strength except '
        'by Allah… <strong>the apparent sense of the Qurʾān is that there is no '
        'excuse</strong> — rather either he speaks or he gets up. And if he '
        'forbade and made the falsehood clear, <strong>he has discharged what '
        'was upon him</strong>.»</em></p>'))
b += B.prose(
    '<em>He says «the apparent sense of the Qurʾān» without naming the verse at '
    'this place. The verse that carries it is al-Nisāʾ 4:140</em> — and it is '
    'worth having in front of you, because the ending is severe.')
b += B.ayah(
    'وَقَدْ نَزَّلَ عَلَيْكُمْ فِي الْكِتَابِ أَنْ إِذَا سَمِعْتُمْ آيَاتِ '
    'اللَّهِ يُكْفَرُ بِهَا وَيُسْتَهْزَأُ بِهَا فَلَا تَقْعُدُوا مَعَهُمْ '
    'حَتَّىٰ يَخُوضُوا فِي حَدِيثٍ غَيْرِهِ إِنَّكُمْ إِذًا مِّثْلُهُمْ',
    'And it has already been revealed to you in the Book that when you hear the '
    'verses of Allah being disbelieved in and mocked, do not sit with them '
    'until they turn to another subject — for then you would be like them.',
    'سُورَةُ النِّسَاء · 4:140')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><strong>Two ways out, and he names '
        'both: speak, or leave.</strong> <em>And he puts them in an order — the '
        'leaving is for the one who is <strong>unable</strong> to forbid with '
        'his tongue.</em> <strong>What there is not, is a third option of '
        'staying and saying nothing</strong>, and that is what «ظَاهِرُ '
        'القُرْآنِ عَدَمُ العُذْر» means.</p>'
        '<p style="margin:.5rem 0 0;font-size:.93rem"><em>This is also the one '
        'ruling on the page that most people will actually need, and it asks '
        'nothing of anyone that is beyond him. Standing up is available to '
        'everybody.</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))

# ---------------------------------------------------------------- the kalimah
b += B.heading('حُقُوقُ الكَلِمَة', 'The Rights of the Word — the Whole Book in a Paragraph')
b += B.prose(
    'The clause closes on something larger than itself, and it is the right place '
    'to end the Nawāqiḍ’s middle section. <em>The question underneath every one '
    'of these ten clauses is: a man said «lā ilāha illā Allāh» — what does that '
    'get him?</em>')
b += B.sharh(
    box('<p style="margin:0 0 .55rem;font-size:.94rem"><em>«And he may '
        '<strong>revile his religion</strong>, and he may '
        '<strong>mock his religion</strong>, while he is saying “there is no god '
        'but Allah” — <strong>and this word will not benefit him</strong>, '
        'because he has not discharged its right. For of its right is that you '
        '<strong>worship Allah alone</strong>, and that you '
        '<strong>magnify His sanctities</strong>, and that you '
        '<strong>hold to His right</strong>, and that you '
        '<strong>reject what is worshipped besides Him</strong>. So if you said '
        'it while you are <strong>not holding to its right</strong>, then '
        '<strong>its presence is like its absence</strong>.»</em></p>'
        '<p style="margin:0;font-size:.94rem"><em>«So the point is that '
        '<strong>this word has rights</strong>, and these rights must be '
        'discharged. <strong>Some rights, [failing them,] make their owner as '
        'though he never said it at all</strong> — he remains in his disbelief '
        'and misguidance. <strong>And some rights, [failing them,] diminish its '
        'meaning and weaken its meaning, but their owner does not become a '
        'disbeliever.</strong>»</em></p>'))
b += B.sharh(table([
    thead3('', 'the first case', 'the second case'),
    row3('<strong>what he did</strong>',
         'He said it, then <strong>reviled Allah and His Messenger</strong> — '
         '«<em>he has disbelieved by that</em>»',
         'He said it <strong>but does not hold to its completing '
         'rights</strong> — «<em>he did not discharge its right fully; rather he '
         'discharged it with deficiency</em>»'),
    row3('<strong>what it is worth</strong>',
         '«<em>Saying “lā ilāha illā Allāh” <strong>did not benefit him</strong>, '
         'nor his prayer, nor his fasting, nor his ḥajj, nor his zakāh… '
         '<strong>because he came with a nullifier from among the nullifiers of '
         'Islām</strong></em>»',
         '«<em>So he is <strong>weak in faith</strong>, and '
         '<strong>deserving of punishment</strong>, and <strong>in danger of '
         'entering the Fire</strong> on the Day of Resurrection if he dies upon '
         'that</em>»'),
    row3('<strong>the name for it</strong>',
         '<strong>نَاقِض</strong> — it breaks',
         '<strong>نَقْص</strong> — it diminishes'),
]) + p('<strong>That distinction — نَاقِض against نَقْص — is the entire book, '
       'and it is why the book exists.</strong> <em>Ten clauses that break, set '
       'apart from everything that merely damages. And the second column is '
       'nobody’s comfort: weak in faith, deserving punishment, in danger of the '
       'Fire. It is simply not the same ruling.</em>'))
b += B.prose(
    '<strong>Six of the ten nullifiers are now done.</strong> '
    '<em>The seventh is %s — and the matn names with it %s and %s — beginning at '
    'printed folio ١٥٩.</em>'
    % (ar('السِّحْر'), ar('الصَّرْف'), ar('العَطْف')))

b += B.vocab([
    ('مَضْمُونُهُ التَّكْذِيب', 'maḍmūnuhū al-takdhīb',
     'its content is denial',
     'Ibn Bāz on mockery. Pressed that making people laugh is not denial, he '
     'answered «وَلَوْ» — even so; it indicates making light of the religion.'),
    ('مَازِحًا', 'māziḥan', 'joking',
     '«حَتَّى وَلَوْ كَانَ مَازِحًا أَوْ يَقْصِدُ مُضَايَقَةَ شَخْص» — the '
     'footnote’s proof is Pharaoh and the ṭawāghīt of the Arabs, who mocked '
     'while inwardly convinced: al-Naml 27:14.'),
    ('يَكْفُرُ بِعَيْنِه', 'yakfuru bi-ʿaynihī',
     'he is declared a disbeliever specifically',
     'And immediately: «أَمَّا القَتْلُ فَشَيْءٌ آخَر، القَتْلُ يَحْتَاجُ '
     'إِلَى اسْتِتَابَة.» The ruling and the sentence are two things.'),
    ('كُفْرٌ عَمَلِيٌّ أَكْبَر', 'kufr ʿamalī akbar',
     'a greater practical disbelief',
     'Where he places mockery — beside prostrating to other than Allah and '
     'slaughtering for other than Allah. An ACT that nullifies, which is why '
     'inward assent does not save it.'),
    ('نَقَلَةُ الدِّين', 'naqalat al-dīn',
     'the transmitters of the religion',
     'His reason for the upper tier on the Ṣaḥābah — not their honour as '
     'individuals. Impugning them as a body says the chain is unsound: «إِيش '
     'بَقِيَ لَنَا؟»'),
    ('الأَقْرَبُ عِنْدِي', 'al-aqrab ʿindī',
     'what is nearest, in my view',
     'His wording on reviling Abū Bakr and ʿUmar — «الأَقْرَبُ عِنْدِي '
     'كُفْرُه». A weighed position, and the page keeps it as he said it.'),
    ('فِسْقٌ وَظُلْم', 'fisq wa-ẓulm', 'depravity and wrongdoing',
     'The lower tier: reviling one or two — he names Muʿāwiyah, ʿAlī and '
     'ʿĀʾishah as the examples. Grave, and a different charge.'),
    ('التَّفْصِيل', 'al-tafṣīl', 'making the distinction',
     'His own word on mocking knowledge and its people: «وَالصَّوَابُ: '
     'التَّفْصِيل». At the ʿilm or at a scholar FOR it → ridda; at clothes, '
     'worldliness or customs with no Sharʿī connection → not ridda.'),
    ('حُقُوقُ الكَلِمَة', 'ḥuqūq al-kalimah',
     'the rights of the word',
     'The clause’s close, and the book’s logic: some rights, failing them, '
     'leave a man «as though he never said it»; others only weaken it — '
     'ضَعِيفُ الإِيمَان, deserving punishment, in danger. نَاقِض against '
     'نَقْص.'),
])

b += B.mcq('nq-l10-mcq', [
    ('Ibn Bāz’s example of «a word uttered with the tongue without the heart»:',
     ['A slip in recitation',
      'A man laughing and saying «Muḥammad is a liar» — «and he disbelieves, '
      'even if he did not believe it»; or «Allah is not above the heaven» — '
      '«even if he is playing»',
      'A vow not intended',
      'An oath taken in anger'], 1),
    ('Why does the ruling land although the man holds no such belief?',
     ['Because the words are blasphemous in form',
      'Because mockery IS contempt — so the absence of the corresponding belief '
      'does not remove the contempt; the uttering of it in jest is the act',
      'Because he may come to believe it later',
      'Because the listeners may be misled'], 1),
    ('What does Ibn Bāz say the content of mockery is?',
     ['Ignorance', 'Denial — التَّكْذِيب', 'Anger', 'Weakness of faith'], 1),
    ('The questioner objected: «the one who mocks is not denying — like making '
     'people laugh.» The answer?',
     ['That the objection is correct in that case',
      '«وَلَوْ» — even so; it indicates making light of the religion, and he has '
      'no faith to restrain him',
      'That it depends on the audience',
      'That it is fisq only'], 1),
    ('And where the mocker was joking, or meant to needle someone?',
     ['He is excused',
      '«حَتَّى وَلَوْ كَانَ مَازِحًا أَوْ يَقْصِدُ مُضَايَقَةَ شَخْص» — the '
      'ruling stands',
      'He owes expiation only',
      'The matter is referred to a judge'], 1),
    ('What proof does the footnote give that inward assent is no defence?',
     ['The ḥadīth of intentions',
      'Pharaoh and the ṭawāghīt of the Arabs, who mocked their prophet while '
      'inwardly believing him — «وَجَحَدُوا بِهَا وَاسْتَيْقَنَتْهَا '
      'أَنْفُسُهُمْ», al-Naml 27:14',
      'The consensus of the Mālikīs',
      'The verse of al-Nisāʾ 4:140'], 1),
    ('Ibn Bāz on the mocker and the killing:',
     ['Both follow automatically',
      'He is declared a disbeliever specifically — «as for the killing, that is '
      'another matter; the killing requires a demand for repentance»',
      'Neither may be stated',
      'The killing is immediate without demand for repentance'], 1),
    ('Why does that sentence matter for the whole clause?',
     ['It softens the ruling',
      'It separates the RULING from the EXECUTION of a sentence — and the fourth '
      'nullifier already settled who carries out a sentence',
      'It transfers the ruling to the scholars',
      'It restricts the clause to public mockery'], 1),
    ('Beside which two acts does he place mockery, as كُفْرٌ عَمَلِيٌّ أَكْبَر?',
     ['Abandoning prayer and abandoning zakāh',
      'Prostrating to other than Allah, and slaughtering for other than Allah',
      'Magic and soothsaying',
      'Hypocrisy and doubt'], 1),
    ('What does that placement explain?',
     ['Why the ruling is disputed',
      'Why inward assent does not save the mocker — nobody argues that one who '
      'prostrates to an idol is excused by believing in his heart that Allah is '
      'one',
      'Why the killing is obligatory',
      'Why the clause follows the fifth'], 1),
    ('«Mockery of the prayer is…»',
     ['a major sin',
      'an independent disbelief, by the consensus of the Muslims',
      'fisq',
      'a matter of ijtihād'], 1),
    ('In his long list of what mocking makes a man a disbeliever for, how does '
     'he close it?',
     ['«unless he repents at once»',
      '«even if he fasts the day and stands the night, and even if he testifies '
      'that there is no god but Allah and that Muḥammad is the Messenger of '
      'Allah every hour»',
      '«unless he is ignorant»',
      '«and the scholars differ in this»'], 1),
    ('Reviling the Ṣaḥābah in general — the ruling?',
     ['Fisq',
      'Disbelief and apostasy from Islām, «with all the people of knowledge» — '
      'he calls it an independent disbelief',
      'A matter of ijtihād',
      'Prohibited but not sinful'], 1),
    ('And reviling one or two of them?',
     ['The same ruling',
      'فِسْق — «this has a tafṣīl: the one and the two are fisq» — and he names '
      'Muʿāwiyah, ʿAlī and ʿĀʾishah as the examples',
      'Disbelief if repeated',
      'No ruling is given'], 1),
    ('What reason does he give for the UPPER tier?',
     ['Their precedence in Islām',
      'That they are نَقَلَةُ الدِّين — the transmitters; so reviling them as a '
      'body means they are not trustworthy and what they transmitted «has no '
      'soundness»',
      'Their participation at Badr',
      'The verse of al-Fatḥ'], 1),
    ('How does he press that point rhetorically?',
     ['By citing the consensus',
      '«If its bearers were apostate disbelievers, what is left for us?… and at '
      'their head al-Ṣiddīq, ʿUmar, ʿUthmān, Ṭalḥah, al-Zubayr, Saʿīd ibn Zayd, '
      'Saʿd ibn Abī Waqqāṣ — so who remains?»',
      'By quoting Ibn Taymiyyah',
      'By listing the ten promised Paradise'], 1),
    ('On reviling Abū Bakr and ʿUmar specifically, what is his wording?',
     ['«He has disbelieved by consensus»',
      '«الأَقْرَبُ عِنْدِي كُفْرُه» — what is nearest, in my view, is his '
      'disbelief — «because Allah was pleased with them»',
      '«This is fisq»',
      '«The matter requires research»'], 1),
    ('And he adds about such a person:',
     ['That he must be exiled',
      'That «no one in whose heart is a mustard-seed of faith» reviles al-Ṣiddīq '
      'and ʿUmar and hates them — «in what we believe»',
      'That he is to be asked to repent three times',
      'That his testimony is rejected only'], 1),
    ('Accusing ʿĀʾishah رَضِيَ اللهُ عَنْهَا of zinā:',
     ['Fisq, like reviling Muʿāwiyah',
      'He has disbelieved — «because he is a denier of Allah, for Allah declared '
      'her innocent»; and holding her innocence unestablished is greater '
      'disbelief, «because it is takdhīb of Allah»',
      'A major sin requiring the ḥadd of slander only',
      'A matter of ijtihād'], 1),
    ('On mocking knowledge and its people, what does Ibn Bāz say the correct '
     'position is?',
     ['Takfīr in every case',
      'التَّفْصِيل — making the distinction',
      'Withholding judgement entirely',
      'Fisq in every case'], 1),
    ('Mockery at Sharʿī knowledge, or at a scholar ON ACCOUNT OF it:',
     ['Fisq',
      'Apostasy from Islām, «no doubt» — because it belittles what Allah has '
      'magnified, and within it is contempt and denial',
      'Prohibited but not apostasy',
      'A matter for the ruler'], 1),
    ('And mockery at a scholar’s clothes, his worldliness, or customs with no '
     'Sharʿī connection?',
     ['Also apostasy',
      'NOT apostasy from Islām — «because it does not go back to the religion»; '
      'and note he does not thereby call it permissible',
      'Permissible',
      'Fisq only if public'], 1),
    ('The Lajnah’s worked example on «يَا ذَقَن»:',
     ['It is disbelief in every case',
      'If the speaker intended RIDICULE, that is disbelief; if he intended '
      'IDENTIFICATION, it is not',
      'It is permitted among friends',
      'It requires the ḥadd of slander'], 1),
    ('On placing the muṣḥaf behind the rows in the mosque, Ibn Bāz said:',
     ['It is disbelief by consensus',
      'It is a place of consideration, and «what is nearest… is that there is no '
      'harm upon him» — because he does not intend to degrade them; though '
      'placing them in front would be more prudent',
      'It is forbidden outright',
      'It is obligatory to remove them'], 1),
    ('How is that consistent with part 1, where treading on a muṣḥaf is '
     'disbelief by consensus?',
     ['It is not consistent',
      'Part 1’s footnote preserved exactly one exclusion — the UNINTENDING — and '
      'this is that exclusion applied to a real case',
      'The two concern different copies',
      'The earlier ruling was retracted'], 1),
    ('A man praises Allah at the moment of a forbidden act, as mockery. What '
     'did Ibn Bāz answer?',
     ['That he disbelieves outright',
      '«This needs reflection» — then he distinguishes: if he intends mockery of '
      'the religion and that it has no value, greater disbelief; if he means «it '
      'is an affliction, and I praise Allah at afflictions and repent to Him», '
      '«there is nothing in it»',
      'That it is fisq in both cases',
      'That the question may not be answered'], 1),
    ('What does that answer show about reading utterances?',
     ['That the surface wording decides',
      'That nothing on these folios is read off the surface of an utterance — '
      'the same words can be two completely different acts',
      'That intention is never relevant',
      'That only scholars may speak'], 1),
    ('A man sits with people mocking the religion and stays silent. Ibn Bāz:',
     ['He is excused if he dislikes it inwardly',
      '«Its apparent import is agreement» — it is obligatory that he not sit; '
      'rather he should get up and depart if unable to forbid with the tongue',
      'He must report them to the authority',
      'He may remain if he is a scholar'], 1),
    ('What are the two things that discharge the duty?',
     ['Dislike in the heart, or supplication',
      'Forbidding and making the falsehood clear — or getting up and leaving',
      'Leaving, or informing the ruler',
      'Silence, or changing the subject'], 1),
    ('What does «ظَاهِرُ القُرْآنِ عَدَمُ العُذْر» rule out?',
     ['Forbidding with the tongue',
      'A third option of staying and saying nothing',
      'Leaving the gathering',
      'Rebuking in private afterwards'], 1),
    ('Which verse carries that ruling?',
     ['al-Tawbah 9:65',
      'al-Nisāʾ 4:140 — «do not sit with them until they turn to another '
      'subject; for then you would be like them». The sharḥ says «the apparent '
      'sense of the Qurʾān» without naming it at this place',
      'al-Anʿām 6:68',
      'al-Naml 27:14'], 1),
    ('What does Ibn Bāz say of a man who says «lā ilāha illā Allāh» while '
     'reviling or mocking his religion?',
     ['That the word intercedes for him',
      'That the word «will not benefit him», because he has not discharged its '
      'right — «its presence is like its absence»',
      'That he is weak in faith only',
      'That he must be asked to renew it'], 1),
    ('What are the two kinds of failure in the rights of the kalimah?',
     ['Public and private',
      'Some, failing them, make their owner «as though he never said it» — he '
      'remains in disbelief; others diminish and weaken its meaning, «but their '
      'owner does not become a disbeliever»',
      'Those of the heart and those of the limbs',
      'Those before Islām and those after'], 1),
    ('What does he say of the second kind of man?',
     ['That he is safe',
      'That he is weak in faith, deserving of punishment, and in danger of '
      'entering the Fire on the Day of Resurrection if he dies upon that',
      'That he is a hypocrite',
      'That nothing is upon him'], 1),
    ('And what is that distinction, in the book’s own terms?',
     ['Kufr and īmān',
      'نَاقِض against نَقْص — what breaks, against what merely diminishes',
      'Major and minor shirk',
      'Obligation and recommendation'], 1),
])

b += B.tf('nq-l10-tf', [
    ('مَنْ قَالَ كَلِمَةَ الكُفْرِ مَازِحًا فَلَا شَيْءَ عَلَيْهِ عِنْدَ '
     'ابْنِ بَاز.',
     'For Ibn Bāz, one who utters a word of disbelief in jest has nothing '
     'against him.', False),
    ('التَّصْدِيقُ البَاطِنُ عُذْرٌ لِلْمُسْتَهْزِئ.',
     'Inward assent is an excuse for the mocker.', False),
    ('التَّكْفِيرُ وَالقَتْلُ شَيْءٌ وَاحِدٌ عِنْدَ ابْنِ بَاز.',
     'For Ibn Bāz, declaring a man a disbeliever and killing him are one thing.',
     False),
    ('سَبُّ الصَّحَابَةِ عُمُومًا كُفْرٌ لِأَنَّهُمْ نَقَلَةُ الدِّين.',
     'Reviling the Ṣaḥābah in general is disbelief because they are the '
     'transmitters of the religion.', True),
    ('سَبُّ الوَاحِدِ وَالاثْنَيْنِ مِنَ الصَّحَابَةِ كُفْرٌ أَكْبَر.',
     'Reviling one or two of the Ṣaḥābah is greater disbelief.', False),
    ('الاسْتِهْزَاءُ بِلِبَاسِ العَالِمِ رِدَّةٌ عَنِ الإِسْلَام.',
     'Mocking a scholar’s clothes is apostasy from Islām.', False),
    ('مَنْ جَلَسَ مَعَ المُسْتَهْزِئِينَ وَسَكَتَ فَظَاهِرُهُ المُوَافَقَة.',
     'Whoever sits with the mockers and stays silent — its apparent import is '
     'agreement.', True),
])

b += B.memorize(
    'أَمَّا القَتْلُ فَشَيْءٌ آخَر، القَتْلُ يَحْتَاجُ إِلَى اسْتِتَابَة',
    'Ibn Bāz, in the same breath as %s. <strong>Of everything on these two '
    'lessons, this is the sentence to carry.</strong> <em>It does not soften the '
    'ruling by one word — he has just said the mocker is declared a disbeliever '
    'specifically. It separates the <strong>ruling</strong> from the '
    '<strong>sentence</strong>, and the fourth nullifier already told you whose '
    'the sentence is.</em> <strong>And beside it keep the two he will not '
    'flatten: «وَالصَّوَابُ: التَّفْصِيل» on mocking the scholars, and '
    '«الفَرْدُ وَالفَرْدَانِ فِسْق» on reviling the Ṣaḥābah.</strong> '
    '<em>Three sentences, and together they are the difference between learning '
    'this clause and misusing it.</em>' % ('«' + ar('يَكْفُرُ بِعَيْنِه') + '»'))

b += B.nav('nq-l09-al-istihza.html',
           'النَّاقِضُ السَّادِس · part 1',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l10')

B.write('nq-l10-masail-al-istihza.html',
        'النَّاقِضُ السَّادِس · مَسَائِلُ الاسْتِهْزَاء',
        'The Sixth Nullifier, Part 2 — The Cases',
        'The sixth nullifier’s cases, from the words of Shaykh Ibn Bāz: a word '
        'said with the tongue and not the heart; that mockery’s content is '
        'denial «even if he was joking or meant to needle someone», with '
        'Pharaoh and al-Naml 27:14 as the footnote’s proof; the governing '
        'distinction that declaring a man a disbeliever and killing him are two '
        'things, the second requiring a demand for repentance; the two tiers on '
        'reviling the Ṣaḥābah and why the upper rests on their being the '
        'transmitters of the religion; «the correct position is to make the '
        'distinction» on mocking knowledge and its people, with the «yā dhaqan» '
        'fatwā; where he declines to rule — the muṣḥaf behind the rows, and '
        'praising Allah at a sin; the ruling on sitting with mockers, and '
        'al-Nisāʾ 4:140; and the rights of the kalimah — what breaks it against '
        'what merely diminishes it.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ العَاشِر', '6', b)
print('wrote nq-l10-masail-al-istihza.html')
