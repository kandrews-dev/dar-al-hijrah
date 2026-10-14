# -*- coding: utf-8 -*-
"""Wasitiyyah L36 -- Part 4 opens: what occurs in the grave. The trial of the
grave, the punishment and the bliss, the two kinds of punishment, and the
Mu'tazilah's objection answered. Sharh pp.126-128."""
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
    'The ḥadīth of <strong>البَرَاءِ بْنِ عَازِبٍ</strong> رضي الله عنه on this āyah is '
    'reported by <strong>البُخَارِيّ</strong> and <strong>مُسْلِم</strong>, with the addition '
    'cited from <strong>مُسْلِم</strong>.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Give the author’s comprehensive definition of belief in the Last Day.',
    'Name the two questions put to the dead, and what %s means in Ibrāhīm 14:27.'
    % ar('القَوْلُ الثَّابِت'),
    'Distinguish the two kinds of punishment of the grave.',
    'Answer the Muʿtazilah’s objection to the punishment of the grave.',
])

b += B.heading('القِسْمُ الرَّابِع · مَا يَدْخُلُ فِي الإِيمَانِ بِاليَوْمِ الآخِر',
               'Part Four — What Enters into Belief in the Last Day')
b += B.sharh(
    p('<strong>%s</strong> — <em>is <strong>the Day of Rising</strong>; and belief in it is '
      '<strong>one of the pillars of faith</strong>. <strong>Reason and the fiṭrah have indicated '
      'it</strong>, <strong>all the revealed Books stated it plainly</strong>, and '
      '<strong>all the prophets and messengers called to it</strong>. And it is named '
      '<em>the Last Day</em> <strong>because it comes after this world.</strong></em>'
      % ar('اليَوْمُ الآخِر')) +
    p('And then al-Fawzān points out something about the author\'s method here, which is worth '
      'noticing before the details begin: <em>the Shaykh رحمه الله mentioned here '
      '<strong>a comprehensive rule for the meaning of belief in the Last Day</strong></em> —') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.95rem"><em>that it is <strong>belief in everything the Prophet '
    '&#65018; informed of, of what occurs after death.</strong></em></p></div>' +
    p('<em>So there enters into it belief in everything the texts have indicated: '
      '<strong>the state of dying, the state of the dead man in the grave, the resurrection from '
      'the graves, and what occurs after it.</strong> Then the Shaykh رحمه الله pointed to some '
      'of those things.</em>') +
    p('That is a rule rather than a list, and it has a practical use. <strong>A student who '
      'memorises five events is left defenceless before a sixth he has not heard of.</strong> The '
      'author\'s formulation covers whatever the texts contain, including what this book does not '
      'have room to mention.'))

b += B.heading('١ · مَا يَكُونُ فِي القَبْر', 'First — What Occurs in the Grave')
b += B.matn(
    'وَمِنَ الإِيمَانِ بِاليَوْمِ الآخِرِ: الإِيمَانُ بِكُلِّ مَا أَخْبَرَ بِهِ النَّبِيُّ '
    'ﷺ مِمَّا يَكُونُ بَعْدَ المَوْتِ؛ فَيُؤْمِنُونَ بِفِتْنَةِ القَبْرِ، وَبِعَذَابِ '
    'القَبْرِ وَنَعِيمِهِ. فَأَمَّا الفِتْنَةُ فَإِنَّ النَّاسَ يُفْتَنُونَ فِي '
    'قُبُورِهِمْ، فَيُقَالُ لِلرَّجُلِ: مَنْ رَبُّكَ؟ وَمَا دِينُكَ؟ وَمَنْ نَبِيُّكَ؟ '
    'فَيُثَبِّتُ اللهُ الَّذِينَ آمَنُوا بِالقَوْلِ الثَّابِتِ فِي الحَيَاةِ الدُّنْيَا '
    'وَفِي الآخِرَةِ؛ فَيَقُولُ المُؤْمِنُ: رَبِّيَ اللهُ، وَالإِسْلَامُ دِينِي، '
    'وَمُحَمَّدٌ ﷺ نَبِيِّي. وَأَمَّا المُرْتَابُ فَيَقُولُ: هَاهْ هَاهْ، لَا أَدْرِي، '
    'سَمِعْتُ النَّاسَ يَقُولُونَ شَيْئًا فَقُلْتُهُ. فَيُضْرَبُ بِمِرْزَبَّةٍ مِنْ '
    'حَدِيدٍ، فَيَصِيحُ صَيْحَةً يَسْمَعُهَا كُلُّ شَيْءٍ إِلَّا الإِنْسَانَ. وَلَوْ '
    'سَمِعَهَا الإِنْسَانُ لَصَعِقَ. ثُمَّ بَعْدَ هَذِهِ الفِتْنَةِ إِمَّا نَعِيمٌ '
    'وَإِمَّا عَذَابٌ.')
b += B.sharh(
    p('<strong>الأَمْرُ الأَوَّل · %s.</strong> And the word first: <em>al-fitnah, in the '
      'language, is <strong>%s — testing and examination</strong>; and what is intended by it '
      'here is <strong>the questioning of the dead by the two angels.</strong></em>'
      % (ar('فِتْنَةُ القَبْر'), ar('الامْتِحَانُ وَالاخْتِبَار'))) +
    p('A useful correction of the English instinct. <em>Fitnah</em> here is not «tribulation» in '
      'the loose sense; <strong>it is an examination</strong> — a thing with questions and '
      'answers and a result.') +
    p('And a point of precision on the matn\'s wording: <strong>%s</strong> — <em>that is: '
      '<strong>the dead person, whether a man or a woman</strong>; and perhaps the mention of «the '
      'man» is <strong>%s — by way of the masculine standing for both</strong>.</em>'
      % (ar('فَيُقَالُ لِلرَّجُلِ'), ar('التَّغْلِيب'))))
b += B.sharh(
    p('And the obligation, with its basis: <em><strong>belief in the questioning of the two angels '
      'is obligatory</strong>, because of its being established from the Prophet &#65018; '
      '<strong>in aḥādīth whose total reaches the degree of %s</strong>.</em> That is the term '
      'defined in Lesson 31 — and note the form of the claim: '
      '<strong>not one mutawātir ḥadīth, but a body of reports whose <em>sum</em> reaches that '
      'degree.</strong>' % ar('التَّوَاتُر')) +
    p('<em>And <strong>the Noble Qurʾān indicates it</strong> in His saying:</em>'))
b += B.ayah(
    'يُثَبِّتُ اللَّهُ الَّذِينَ آمَنُوا بِالْقَوْلِ الثَّابِتِ فِي الْحَيَاةِ الدُّنْيَا '
    'وَفِي الْآخِرَةِ وَيُضِلُّ اللَّهُ الظَّالِمِينَ وَيَفْعَلُ اللَّهُ مَا يَشَاءُ',
    '"Allah makes firm those who believe with the firm word, in the life of this world and in the '
    'Hereafter; and Allah lets the wrongdoers go astray — and Allah does what He wills."',
    'Sūrat Ibrāhīm 14:27 · سُورَةُ إِبْرَاهِيم')
b += B.sharh(
    p('And the link from the āyah to the grave is not an inference; it is the Prophet\'s &#65018; '
      'own: <em><strong>the two Shaykhs reported</strong>, from the ḥadīth of '
      '<strong>البَرَاءِ بْنِ عَازِبٍ</strong> رضي الله عنهما, that the Prophet &#65018; said '
      'concerning His saying %s: <strong>«it was sent down concerning the punishment of the '
      'grave».</strong></em>' % ar('يُثَبِّتُ اللَّهُ الَّذِينَ آمَنُوا بِالْقَوْلِ الثَّابِتِ')) +
    p('<em>And <strong>Muslim added</strong>: <strong>«so it is said to him: who is your Lord? '
      'And he says: my Lord is Allah, and my prophet is Muḥammad &#65018;» — and that is His '
      'saying عز وجل: %s.»</strong></em>'
      % ar('يُثَبِّتُ اللَّهُ الَّذِينَ آمَنُوا بِالْقَوْلِ الثَّابِتِ')) +
    p('<strong>%s</strong> — <em>is <strong>the word of tawḥīd, which became firm in the heart of '
      'the believer by proof and evidence.</strong></em> And then al-Fawzān divides the āyah\'s '
      'two places, which is the finest thing in the section:'
      % ar('القَوْلُ الثَّابِت')) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.91rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>فِي الحَيَاةِ الدُّنْيَا</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)"><em>that '
    '<strong>they hold fast to it, even if there reaches them in its path what reaches them of '
    'harm and torture</strong></em></td></tr>'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>وَفِي الآخِرَةِ</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)"><em>that '
    '<strong>they are granted success in the answer at the questioning of the two '
    'angels</strong></em></td></tr>'
    '</table></div>' +
    p('<strong>One āyah, two makings-firm, and the second is earned by the first.</strong> The man '
      'who held the word fast under pressure in this life is the man who finds it on his tongue '
      'in the grave. Which is why the answer cannot be rehearsed: '
      '<strong>it is not a password but a report of what a life was actually built on.</strong>'))
b += B.sharh(
    p('<em>And <strong>%s</strong> — that is: <strong>the doubter</strong>; <strong>%s</strong>, '
      'when asked — <strong>%s</strong>, <em>a word of hesitation and of pain</em> — '
      '<strong>%s</strong>; <strong>because he is not a believer in what the Prophet '
      '&#65018; came with</strong>.</em> And of such Allah said %s — «and Allah lets the '
      'wrongdoers go astray».'
      % (ar('وَأَمَّا المُرْتَاب'), ar('فَيَقُولُ'), ar('هَاهْ هَاهْ'),
         ar('لَا أَدْرِي، سَمِعْتُ النَّاسَ يَقُولُونَ شَيْئًا فَقُلْتُهُ'),
         ar('وَيُضِلُّ اللَّهُ الظَّالِمِينَ'))) +
    p('Read what he actually confesses, because it is the most chilling line in the matn and it is '
      'not a denial. <strong>«I heard the people saying something, so I said it.»</strong> He had '
      'the right words. He simply never had them as his own — and the examination is of the '
      'second thing, not the first.') +
    p('<strong>%s</strong> — <em>and it is <strong>the great hammer</strong></em> — '
      '<strong>%s</strong>. <em>Then he explained the wisdom in man\'s not hearing it, with his '
      'saying <strong>%s</strong> — that is: <strong>he would fall down dead, or lose '
      'consciousness.</strong></em>'
      % (ar('فَيُضْرَبُ بِمِرْزَبَّةٍ مِنْ حَدِيدٍ'),
         ar('فَيَصِيحُ صَيْحَةً يَسْمَعُهَا كُلُّ شَيْءٍ إِلَّا الإِنْسَانَ'),
         ar('وَلَوْ سَمِعَهَا الإِنْسَانُ لَصَعِقَ'))) +
    p('And al-Fawzān adds a second wisdom of his own, which answers a question a bereaved person '
      'asks: <em>and of the wisdom of Allah also is that <strong>what happens to the dead in his '
      'grave is not perceived by those who loved him</strong> — because Allah تعالى '
      '<strong>made it of the unseen</strong>; and <strong>had He made it apparent, the intended '
      'wisdom would have been lost, which is belief in the unseen.</strong></em>'))

b += B.heading('الأَمْرُ الثَّانِي · النَّعِيمُ أَوِ العَذَاب',
               'Second — the Bliss, or the Punishment')
b += B.sharh(
    p('The author\'s clause <strong>%s</strong> — <em>in this is '
      '<strong>the affirming of the punishment of the grave or its bliss</strong>.</em>'
      % ar('ثُمَّ بَعْدَ هَذِهِ الفِتْنَةِ إِمَّا نَعِيمٌ وَإِمَّا عَذَابٌ')) +
    p('<em>And <strong>the madhhab of Ahl al-Sunnah wa-l-Jamāʿah is that the dead, when he dies, '
      'is in bliss or in punishment; and that this occurs to his soul AND his body</strong>, as '
      'the aḥādīth from the Messenger of Allah &#65018; have come mutawātir. '
      '<strong>So belief in it is obligatory — and its manner and description are not spoken '
      'of</strong>, because <strong>that is not grasped by the intellects, being of the matters of '
      'the Hereafter; and the matters of the Hereafter none knows but Allah and those whom Allah '
      'has acquainted with something of them — and they are the messengers</strong> صلوات الله '
      'وسلامه عليهم.</em>') +
    p('<strong>Affirm, and do not ask how.</strong> The same discipline as the attributes, applied '
      'now to an event rather than to a description — and for the same reason: '
      '<strong>no one has the access that answering «how» would require.</strong>') +
    p('And the two kinds, which resolve the obvious question of whether a sinning believer is '
      'punished forever in the grave:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.91rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>النَّوْعُ الأَوَّل</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<strong>a lasting punishment</strong>, and it is <strong>the punishment of the '
    'disbeliever</strong> — as He said: '
    '<span dir="rtl" lang="ar">النَّارُ يُعْرَضُونَ عَلَيْهَا غُدُوًّا وَعَشِيًّا</span> '
    '(Ghāfir 40:46)</td></tr>'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top"><strong>النَّوْعُ الثَّانِي</strong></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<strong>for a term, then it is cut off</strong> — the punishment of '
    '<strong>some of the disobedient among the believers</strong>: <em>he is punished '
    '<strong>to the measure of his crime</strong>, then it is lightened for him. '
    '<strong>And the punishment may be cut off from him by reason of a supplication, or a '
    'charity, or a seeking of forgiveness</strong></em></td></tr>'
    '</table></div>' +
    p('That last clause is the one to sit with. <strong>A duʿāʾ made for a dead person can end a '
      'punishment that had begun.</strong> It is the strongest argument in the whole section for '
      'why this doctrine is not morbid: it tells the living that there is still something they can '
      'do.'))
b += B.ayah(
    'النَّارُ يُعْرَضُونَ عَلَيْهَا غُدُوًّا وَعَشِيًّا وَيَوْمَ تَقُومُ السَّاعَةُ '
    'أَدْخِلُوا آلَ فِرْعَوْنَ أَشَدَّ الْعَذَابِ',
    '"The Fire — they are exposed to it morning and evening; and on the Day the Hour comes: enter '
    'the family of Pharaoh into the severest punishment."',
    'Sūrat Ghāfir 40:46 · سُورَةُ غَافِر')

b += B.heading('شُبْهَةُ المُعْتَزِلَةِ وَالجَوَابُ عَنْهَا',
               'The Muʿtazilah’s Objection, and the Answer to It')
b += B.sharh(
    p('<em>And <strong>the Muʿtazilah denied the punishment of the grave</strong>; and their '
      'objection in that is: <strong>that they do not perceive it, and do not see the dead being '
      'punished or being questioned.</strong></em>') +
    p('<strong>The answer:</strong> <em>that <strong>our not perceiving a thing and not seeing it '
      'does not indicate its non-existence and its not occurring.</strong> '
      '<strong>How many things are there that we do not see, and they exist</strong> — and of '
      'that is the punishment of the grave, or its bliss.</em>') +
    p('<em>And that <strong>Allah تعالى made the matter of the Hereafter, and what is connected to '
      'it, unseen, and veiled it from the grasp of the intellects in this abode</strong> — '
      '<strong>so that those who believe in the unseen might be distinguished from '
      'others.</strong> <strong>And the matters of the Hereafter are not measured by the matters '
      'of this world.</strong> وَاللهُ أَعْلَم.</em>') +
    p('Notice that the answer has two layers, and the second is the stronger. The first is merely '
      'logical: <em>absence of perception is not evidence of absence</em>. '
      '<strong>The second says the concealment is deliberate and is the point</strong> — the '
      'unseen is hidden <em>in order</em> to sort those who will believe a report from those who '
      'will only believe their eyes. <strong>So the Muʿtazilī demand to see it before believing it '
      'is not an objection to the doctrine; it is the very test the doctrine '
      'describes.</strong>') +
    p('And note the family resemblance to Lesson 21. There, the deniers of the ruʾyah reasoned '
      'from what seeing is like <em>here</em>; here, the deniers of the punishment reason from '
      'what death looks like <em>here</em>. <strong>Both measure the Hereafter by this world, and '
      'both are answered by refusing the measurement.</strong>'))

b += B.vocab([
    ('اليَوْمُ الآخِر', 'al-yawm al-ākhir', 'the Last Day',
     'Named so because it comes after this world'),
    ('الفِتْنَة', 'al-fitnah', 'the examination',
     'In the language: testing and examination — here, the two angels’ questioning'),
    ('التَّغْلِيب', 'al-taghlīb', 'the prevailing form',
     'Why the matn says «the man» though it covers man and woman alike'),
    ('القَوْلُ الثَّابِت', 'al-qawl al-thābit', 'the firm word',
     'The word of tawḥīd, made firm in the heart by proof and evidence'),
    ('المُرْتَاب', 'al-murtāb', 'the doubter',
     'Who answers: I heard the people saying something, so I said it'),
    ('مِرْزَبَّة', 'mirzabbah', 'a great hammer',
     'Of iron — and the cry is heard by everything but man'),
    ('البَرْزَخ', 'al-barzakh', 'the intervening abode',
     'The second of the three abodes, between this world and the Hereafter'),
])
b += B.mcq('ws-l36', [
    ('What is the author’s comprehensive rule for belief in the Last Day?',
     ['Belief in the resurrection and the reckoning',
      'Belief in everything the Prophet ﷺ informed of, of what occurs after death',
      'Belief in the Garden and the Fire',
      'Belief in the signs of the Hour'], 1),
    ('Why is that a rule rather than a list?',
     ['Because the list is disputed',
      'Because a student who memorises a few events is defenceless before one he has not heard '
      'of — the rule covers whatever the texts contain',
      'Because the author ran out of space',
      'Because the events differ between narrations'], 1),
    ('What does %s mean in the language, and here?' % ar('الفِتْنَة'),
     ['Tribulation; and the hardship of dying',
      'Testing and examination; and here, the questioning of the dead by the two angels',
      'Discord; and here, the dispute over the grave',
      'Burning; and here, the punishment'], 1),
    ('How is Ibrāhīm 14:27 connected to the grave?',
     ['By the inference of the scholars',
      'By the Prophet’s ﷺ own statement in the ḥadīth of al-Barāʾ ibn ʿĀzib in the two '
      'Ṣaḥīḥs: "it was sent down concerning the punishment of the grave"',
      'By the context of the sūrah',
      'By the consensus of the mufassirūn only'], 1),
    ('What are the āyah’s two makings-firm?',
     ['Firmness in belief, and firmness in action',
      'In this life, that they hold fast to the word though harm and torture reach them; and in '
      'the Hereafter, success in the answer to the two angels',
      'Firmness at death, and firmness at the Reckoning',
      'Firmness of the heart, and firmness of the tongue'], 1),
    ('What does the doubter actually confess?',
     ['That he never heard of the Prophet ﷺ',
      '"I heard the people saying something, so I said it" — he had the right words but never as '
      'his own',
      'That he denied the resurrection',
      'That he followed his forefathers'], 1),
    ('What are the two kinds of punishment of the grave?',
     ['Of the body, and of the soul',
      'Lasting — the disbeliever’s; and for a term then cut off — some disobedient '
      'believers, to the measure of the crime, and it may be cut off by a duʿāʾ, a charity or a '
      'seeking of forgiveness',
      'Of the grave, and of the Fire',
      'Light and severe, both lasting'], 1),
    ('What is the stronger of the two layers answering the Muʿtazilah?',
     ['That the aḥādīth are mutawātir',
      'That the concealment is deliberate and is the point — the unseen is hidden in order to '
      'distinguish those who believe a report from those who believe only their eyes',
      'That the Companions affirmed it',
      'That reason cannot judge the Hereafter'], 1),
])
b += B.tf('ws-l36-tf', [
    ('الإِيمَانُ بِسُؤَالِ المَلَكَيْنِ وَاجِبٌ.',
     'Belief in the questioning of the two angels is obligatory.', True),
    ('نَعِيمُ القَبْرِ وَعَذَابُهُ يَحْصُلُ لِلرُّوحِ وَالبَدَنِ.',
     'The bliss and punishment of the grave occur to the soul and the body.', True),
    ('يُتَكَلَّمُ فِي كَيْفِيَّةِ عَذَابِ القَبْرِ وَصِفَتِهِ.',
     'The manner and description of the punishment of the grave are spoken of.', False),
    ('عَدَمُ إِدْرَاكِنَا لِلشَّيْءِ يَدُلُّ عَلَى عَدَمِ وُجُودِهِ.',
     'Our not perceiving a thing indicates its non-existence.', False),
])
b += B.memorize(
    'يُثَبِّتُ اللَّهُ الَّذِينَ آمَنُوا بِالْقَوْلِ الثَّابِتِ فِي الْحَيَاةِ الدُّنْيَا '
    'وَفِي الْآخِرَةِ',
    'The Prophet ﷺ said this āyah was sent down about the punishment of the grave. Learn it with '
    'al-Fawzān\'s two places attached: the firmness you are given <em>there</em> is the firmness '
    'you held to <em>here</em>. The answer in the grave is not recalled — it is reported.')
b += B.aiquiz('What occurs in the grave, in al-Aqidah al-Wasitiyyah: the author comprehensive '
              'rule that belief in the Last Day is belief in everything the Prophet informed of '
              'after death, fitnah as examination, the hadith of al-Bara ibn Azib tying Ibrahim '
              '14:27 to the punishment of the grave and the two makings-firm in this life and the '
              'next, what the doubter confesses, the two kinds of punishment including that a dua '
              'or charity may cut it off, and the two-layer answer to the Mutazilah')
b += B.further()
b += B.nav('was-l35-ruyah-mawadi.html', 'The Obligation of Believing in the Seeing',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l36')

io.open(os.path.join(B.AQ, 'was-l36-fitnat-al-qabr.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'فِتْنَةُ القَبْرِ وَعَذَابُهُ وَنَعِيمُه',
    'The Examination of the Grave, Its Punishment and Its Bliss',
    'Lesson 36 of al-ʿAqīdah al-Wāsiṭiyyah, opening Part 4: the '
    'author’s comprehensive rule for belief in the Last Day, the two angels’ '
    'examination and what the doubter confesses, the two makings-firm of Ibrāhīm 14:27, '
    'the two kinds of punishment — one of which a duʿāʾ may cut off — '
    'and why the Muʿtazilī demand to see it first is the very test the doctrine '
    'describes.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ السَّادِسُ وَالثَّلَاثُون', '4',
           'فِتْنَةُ القَبْرِ وَعَذَابُهُ وَنَعِيمُه',
           'The Examination of the Grave, Its Punishment and Its Bliss', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l36-fitnat-al-qabr.html')
