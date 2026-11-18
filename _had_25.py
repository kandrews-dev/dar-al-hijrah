# -*- coding: utf-8 -*-
"""Ḥadīth 25 — «ذَهَبَ أَهْلُ الدُّثُورِ بِالأُجُور…». Abū Dharr al-Ghifārī,
Ṣaḥīḥ Muslim. Sharḥ of Ibn ʿUthaymīn, printed folios 277–285 (markers 278–286,
offset −1).

The poor Companions fear the wealthy have outrun them in reward; the Prophet ﷺ
opens doors of ṣadaqah within reach of everyone — every tasbīḥ, takbīr,
taḥmīd and tahlīl, enjoining good, forbidding evil, and even a man’s intimacy
with his wife. The Shaykh turns the last into a lesson in qiyās al-ʿaks, and
unfolds the full fiqh of amr bi-l-maʿrūf and nahy ʿan al-munkar.

Rule 8: the ḥadīth is in Ṣaḥīḥ Muslim (Kitāb al-Zakāh), so ṣaḥīḥ; the
supporting «أَصَلَّيْتَ؟… قُمْ فَصَلِّ» is muttafaq ʿalayh, «إِنَّ لِنَفْسِكَ
عَلَيْكَ حَقًّا» is in al-Bukhārī — named attributions, no grading invented.
"""
import io, os, importlib.util

spec = importlib.util.spec_from_file_location('hb', os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '_hadbuild.py'))
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)


def p(x):
    return '<p style="font-size:.92rem;color:var(--ink-mid);line-height:1.9;' \
           'margin:0 0 .85rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


def box(inner, wash='var(--brand-wash)', edge='var(--brand)'):
    return ('<div style="background:%s;border-right:4px solid %s;'
            'border-radius:var(--radius-sm);padding:var(--space-lg);'
            'margin:0 0 var(--space-md)">%s</div>' % (wash, edge, inner))


def row(k, v):
    return ('<tr><td style="padding:.62rem .8rem;border:1px solid var(--line);'
            'white-space:nowrap;vertical-align:top"><strong>%s</strong></td>'
            '<td style="padding:.62rem .8rem;border:1px solid var(--line)">%s</td></tr>'
            % (k, v))


def table(rows, fs='.91rem'):
    return ('<div style="overflow-x:auto"><table style="width:100%%;'
            'border-collapse:collapse;font-size:%s;margin:0 0 var(--space-md)">%s'
            '</table></div>' % (fs, ''.join(rows)))


b = B.objectives([
    'Say who narrated this ḥadīth and where it is reported, and what the poor '
    'Companions meant by «%s».' % ar('ذَهَبَ أَهْلُ الدُّثُورِ بِالأُجُور'),
    'List the doors of ṣadaqah the Prophet ﷺ opened that cost no wealth.',
    'Distinguish ṣadaqah that is <strong>obligatory</strong> from what is not, '
    'and the <strong>qāṣir</strong> from the <strong>mutaʿaddin</strong>.',
    'State the conditions of <strong>amr bi-l-maʿrūf</strong> and <strong>nahy '
    'ʿan al-munkar</strong>, and the four outcomes of forbidding an evil.',
    'Explain «%s» by qiyās al-ʿaks — how a lawful desire earns reward.'
    % ar('وَفِي بُضْعِ أَحَدِكُمْ صَدَقَة'),
])

b += B.provenance(277, 285)

b += B.hadith_block(
    'عَنْ أَبِي ذَرٍّ رَضِيَ اللهُ عَنْهُ أَيْضًا أَنَّ أُنَاسًا مِنْ '
    'أَصْحَابِ رَسُولِ اللهِ ﷺ قَالُوا لِلنَّبِيِّ ﷺ: يَا رَسُولَ اللهِ، '
    'ذَهَبَ أَهْلُ الدُّثُورِ بِالأُجُورِ؛ يُصَلُّونَ كَمَا نُصَلِّي، '
    'وَيَصُومُونَ كَمَا نَصُومُ، وَيَتَصَدَّقُونَ بِفُضُولِ أَمْوَالِهِمْ. '
    'قَالَ: «أَوَلَيْسَ قَدْ جَعَلَ اللهُ لَكُمْ مَا تَصَّدَّقُونَ بِهِ؟ '
    'إِنَّ بِكُلِّ تَسْبِيحَةٍ صَدَقَةً، وَكُلِّ تَكْبِيرَةٍ صَدَقَةً، '
    'وَكُلِّ تَحْمِيدَةٍ صَدَقَةً، وَكُلِّ تَهْلِيلَةٍ صَدَقَةً، وَأَمْرٌ '
    'بِالمَعْرُوفِ صَدَقَةٌ، وَنَهْيٌ عَنْ مُنْكَرٍ صَدَقَةٌ، وَفِي بُضْعِ '
    'أَحَدِكُمْ صَدَقَةٌ». قَالُوا: يَا رَسُولَ اللهِ، أَيَأْتِي أَحَدُنَا '
    'شَهْوَتَهُ وَيَكُونُ لَهُ فِيهَا أَجْرٌ؟ قَالَ: «أَرَأَيْتُمْ لَوْ '
    'وَضَعَهَا فِي حَرَامٍ أَكَانَ عَلَيْهِ وِزْرٌ؟ فَكَذَلِكَ إِذَا '
    'وَضَعَهَا فِي الحَلَالِ كَانَ لَهُ أَجْرٌ». رَوَاهُ مُسْلِم.',
    'Abū Dharr (may Allah be pleased with him) also reported that some of the '
    'Companions of the Messenger of Allah ﷺ said to the Prophet ﷺ: "O '
    'Messenger of Allah, the people of wealth have gone off with the rewards: '
    'they pray as we pray, they fast as we fast, and they give charity from the '
    'surplus of their wealth." He said: "Has Allah not made for you what you '
    'can give as charity? In every tasbīḥah is a charity, every takbīrah a '
    'charity, every taḥmīdah a charity, every tahlīlah a charity; enjoining '
    'good is a charity, forbidding evil is a charity, and in the intimacy of '
    'one of you with his wife there is a charity." They said: "O Messenger of '
    'Allah, does one of us fulfil his desire and have a reward in it?" He said: '
    '"Do you not see that were he to place it in the forbidden there would be a '
    'sin upon him? So likewise, when he places it in the lawful, he has a '
    'reward." Narrated by Muslim.',
    'Narrated by Abū Dharr al-Ghifārī · رَوَاهُ مُسْلِم — Muslim, in his Ṣaḥīḥ '
    '(Kitāb al-Zakāh, bāb anna ism al-ṣadaqah yaqaʿu ʿalā kull maʿrūf), so the '
    'ḥadīth is ṣaḥīḥ.')

# ------------------------------------------------------------------ §1
b += B.heading('«ذَهَبَ أَهْلُ الدُّثُورِ بِالأُجُور»',
               'The Poor Companions’ Complaint')
b += p('<strong>“Ahl al-duthūr” are the people of abundant wealth</strong>; '
       '«bi-l-ujūr» — they carried off the rewards. <em>The poor Companions did '
       'not mean envy, nor an objection to Allah’s decree.</em> They prayed and '
       'fasted as the rich did, but had nothing to give in charity — so they '
       'came hoping the Prophet ﷺ would open them a door by which to catch the '
       'race.')

# ------------------------------------------------------------------ §2
b += B.heading('أَبْوَابٌ فَتَحَهَا لَهُم', 'The Doors He Opened')
b += p('<strong>“Has Allah not made for you what you can give as '
       'charity?”</strong> <em>He affirmed them with what they could not deny '
       '(taqrīr), then named the deeds — every one a ṣadaqah, and none of them '
       'costing a dirham:</em>')
b += table([
    row('«%s»' % ar('تَسْبِيحَة / تَكْبِيرَة'),
        '<em>To say سُبْحَانَ الله is a charity; to say اللهُ أَكْبَر is a '
        'charity.</em>'),
    row('«%s»' % ar('تَحْمِيدَة / تَهْلِيلَة'),
        '<em>To say الحَمْدُ لِله is a charity; to say لَا إِلَٰهَ إِلَّا الله '
        'is a charity.</em>'),
    row('«%s»' % ar('أَمْرٌ بِالمَعْرُوف'),
        '<em>To command one you see falling short in an act of obedience is a '
        'charity.</em>'),
    row('«%s»' % ar('نَهْيٌ عَنْ مُنْكَر'),
        '<em>To forbid one you see upon an evil is a charity.</em>'),
    row('«%s»' % ar('بُضْعِ أَحَدِكُم'),
        '<em>And in a man’s intimacy with his wife there is a charity.</em>'),
])
b += box(
    '<p style="margin:0;font-size:.92rem"><strong>Bodily worship is shared by '
    'rich and poor alike.</strong> <em>“They pray as we pray and fast as we '
    'fast” — and the poor man’s performance may be more complete than the rich '
    'man’s. The rich may not give charity every day, and when they do they do '
    'not fill the day with it; but you can fill every hour with tasbīḥ, takbīr, '
    'tahlīl and taḥmīd.</em></p>')

# ------------------------------------------------------------------ §3
b += B.heading('لَيْسَتِ الصَّدَقَاتُ سَوَاء', 'Not Every Charity Is Equal')
b += p('<strong>All he named is ṣadaqah — but it is of two sorts twice '
       'over.</strong>')
b += table([
    row('وَاجِب / غَيْر وَاجِب',
        '<em>Some is obligatory, some not.</em> The takbīr of the prayer is '
        'wājib; the dhikr after it is mustaḥabb — and so for the rest. Enjoining '
        'good and forbidding evil are of the obligatory.'),
    row('قَاصِر / مُتَعَدٍّ',
        '<em>Some is confined to the doer (قَاصِر) — like the dhikr; some '
        'reaches others (مُتَعَدٍّ) — like enjoining good and forbidding '
        'evil.</em> The mutaʿaddin benefits the one commanded as well as the '
        'commander.'),
])

# ------------------------------------------------------------------ §4
b += B.heading('شُرُوطُ الأَمْرِ وَالنَّهْي',
               'The Conditions of Commanding Good and Forbidding Evil')
b += B.ayah(
    'وَلْتَكُن مِّنكُمْ أُمَّةٌ يَدْعُونَ إِلَى الْخَيْرِ وَيَأْمُرُونَ '
    'بِالْمَعْرُوفِ وَيَنْهَوْنَ عَنِ الْمُنكَرِ',
    'And let there be among you a community calling to good, enjoining what is '
    'right and forbidding what is wrong.',
    'سُورَةُ آلِ عِمْرَان · 3:104')
b += p('<strong>Two conditions for commanding good:</strong> <em>(1) that the '
       'commander <strong>knows</strong> it is a maʿrūf — for if he commands out '
       'of ignorance he has spoken about Allah what he does not know; (2) that '
       'he knows the person has <strong>left</strong> that maʿrūf, or else he '
       'asks first.</em> So when a man entered during the Friday khuṭbah and sat '
       'down, the Prophet ﷺ asked, “Did you pray?” — “No.” — “Stand and pray '
       'two rakʿahs.” He did not command until he had asked.')
b += p('<strong>Three conditions for forbidding an evil:</strong>')
b += table([
    row('١ · أَنْ يَكُونَ مُنْكَرًا بِالدَّلِيل',
        '<em>That you know it is munkar by the sharī‘ah’s proof — not by taste, '
        'custom, jealousy, or emotion.</em>'),
    row('٢ · أَنْ يَكُونَ قَدْ وَقَعَ فِيه',
        '<em>That you know this person has actually fallen into it</em> — do '
        'not rebuke a man eating in Ramaḍān until you ask whether he is a '
        'traveller.'),
    row('٣ · أَلَّا يَؤُولَ إِلَى مَا هُوَ أَعْظَم',
        '<em>That forbidding it not lead to something worse.</em>'),
])
b += box(
    '<p style="margin:0 0 .5rem;font-size:.92rem"><strong>Four outcomes of '
    'forbidding an evil:</strong> <em>(1) it is removed entirely → forbidding '
    'is <strong>wājib</strong>; (2) it is lessened → <strong>wājib</strong>, '
    'for lessening evil is a duty; (3) it turns into a like evil → a place of '
    '<strong>consideration</strong> (naẓar); (4) it turns into a greater evil '
    '→ forbidding is <strong>ḥarām</strong>.</em></p>'
    '<p style="margin:0;font-size:.92rem">The proof of the last is «%s» — do '
    'not revile their false gods, lest they revile Allah in enmity and '
    'ignorance. Ibn Taymiyyah passed Tatars drinking wine and did not forbid '
    'them: had he done so they would have risen to plunder people’s homes and '
    'violate their honour — a greater evil. See the fiqh in the religion of '
    'Allah.</p>'
    % ar('وَلَا تَسُبُّوا الَّذِينَ يَدْعُونَ مِنْ دُونِ الله'))
b += B.ayah(
    'وَلَا تَسُبُّوا الَّذِينَ يَدْعُونَ مِن دُونِ اللَّهِ فَيَسُبُّوا اللَّهَ '
    'عَدْوًا بِغَيْرِ عِلْمٍ',
    'And do not revile those they invoke besides Allah, lest they revile Allah '
    'in enmity without knowledge.',
    'سُورَةُ الأَنْعَام · 6:108')

# ------------------------------------------------------------------ §5
b += B.heading('«وَفِي بُضْعِ أَحَدِكُمْ صَدَقَة»',
               'A Lawful Desire — and Qiyās al-ʿAks')
b += p('<strong>“Does one of us fulfil his desire and have a reward in '
       'it?”</strong> <em>They asked to understand, not to object.</em> The '
       'Prophet ﷺ answered by an <strong>analogy of opposites</strong> '
       '(قِيَاسُ العَكْس): were he to place that desire in the forbidden, there '
       'would be a <strong>sin</strong> upon him — <em>and all agree there '
       'would</em> — so, by the opposite, placing it in the lawful earns him a '
       '<strong>reward</strong>.')
b += box(
    '<p style="margin:0 0 .5rem;font-size:.92rem"><strong>And it is a charity '
    'even for mere desire</strong> — not only to fend off the ḥarām — for two '
    'reasons:</p>'
    '<p style="margin:0;font-size:.92rem">(1) A person is commanded not to deny '
    'his soul its lawful desire: «إِنَّ لِنَفْسِكَ عَلَيْكَ حَقًّا» '
    '(al-Bukhārī). (2) In coming to his wife he does good to her, for she has '
    'of desire what he has. <strong>Sufficing with the lawful in place of the '
    'forbidden makes the lawful itself a nearness and a charity.</strong></p>')

# ------------------------------------------------------------------ §6
b += B.heading('مَا لَمْ يَسْأَلْ عَنْهُ الصَّحَابَة', 'What the Companions Did Not Ask')
b += p('<strong>The Companions left no difficulty unasked</strong> — “does one '
       'of us fulfil his desire and have reward in it?” <em>By this we learn '
       'that a matter of religion the Companions did <strong>not</strong> ask '
       'about — asking about it now is an innovation</em>: had it been of the '
       'religion, Allah would have raised someone to ask. When the Prophet ﷺ '
       'spoke of the Dajjāl’s first day being like a year, and they asked '
       'whether one prayer would suffice that day, he said: «%s» — estimate its '
       'measure. What people need in their religion either came from him ﷺ at '
       'the start or in answer to a question; what did neither, and touches the '
       'religion, is a bidʿah to raise.'
       % ar('اقْدُرُوا لَهُ قَدْرَهُ'))
b += B.ayah(
    'وَتَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَىٰ',
    'And cooperate in righteousness and piety.',
    'سُورَةُ المَائِدَة · 5:2')

# ------------------------------------------------------------------ vocab
b += B.vocab([
    ('الدُّثُور', 'al-duthūr', 'abundant wealth', 'د-ث-ر',
     'The property of the rich; the poor Companions feared “ahl al-duthūr” had '
     'carried off the rewards with their charity',
     'ذَهَبَ أَهْلُ الدُّثُورِ بِالأُجُور'),
    ('تَسْبِيحَة', 'tasbīḥah', 'one utterance of subḥānallāh', 'س-ب-ح',
     'A single saying of سُبْحَانَ الله — and it is a charity that costs no '
     'wealth',
     'إِنَّ بِكُلِّ تَسْبِيحَةٍ صَدَقَة'),
    ('تَهْلِيلَة', 'tahlīlah', 'one utterance of lā ilāha illā Allāh', 'ه-ل-ل',
     'A single saying of لَا إِلَٰهَ إِلَّا الله — likewise a charity within '
     'everyone’s reach',
     'وَكُلِّ تَهْلِيلَةٍ صَدَقَة'),
    ('المَعْرُوف', 'al-maʿrūf', 'the good, the right', 'ع-ر-ف',
     'Enjoining it is a charity; but the one who commands must know it is a '
     'maʿrūf and that the person has left it',
     'وَأَمْرٌ بِالمَعْرُوفِ صَدَقَة'),
    ('المُنْكَر', 'al-munkar', 'the wrong, the evil', 'ن-ك-ر',
     'Forbidding it is a charity — on condition it is munkar by proof, the '
     'person fell into it, and forbidding leads to no greater evil',
     'وَنَهْيٌ عَنْ مُنْكَرٍ صَدَقَة'),
    ('بُضْع', 'buḍʿ', 'marital intimacy', 'ب-ض-ع',
     'In a man’s coming to his wife there is a charity — sometimes obligatory '
     '(if he fears zinā), otherwise recommended',
     'وَفِي بُضْعِ أَحَدِكُمْ صَدَقَة'),
    ('قِيَاسُ العَكْس', 'qiyās al-ʿaks', 'analogy of opposites', 'ع-ك-س',
     'The Prophet’s ﷺ proof: if desire placed in the ḥarām is a sin, then '
     'desire placed in the ḥalāl is a reward',
     'إِذَا وَضَعَهَا فِي الحَلَالِ كَانَ لَهُ أَجْر'),
    ('الوِزْر', 'al-wizr', 'sin, burden of guilt', 'و-ز-ر',
     'What would fall on a man who placed his desire in the ḥarām — the near '
     'side of the analogy from which the reward of the lawful is drawn',
     'لَوْ وَضَعَهَا فِي حَرَامٍ أَكَانَ عَلَيْهِ وِزْر'),
])

# ------------------------------------------------------------------ MCQ
b += B.mcq('hd-h25', [
    ('Who narrated this ḥadīth, and where is it reported?',
     ['Jābir ibn ʿAbdillāh, in al-Bukhārī',
      'Abū Dharr al-Ghifārī, in Muslim',
      'Abū Hurayrah, in al-Tirmidhī',
      'Anas ibn Mālik, in Abū Dāwūd'], 1),
    ('What did the poor Companions mean by «ذَهَبَ أَهْلُ الدُّثُورِ '
     'بِالأُجُور»?',
     ['They envied the rich and objected to the decree',
      'Not envy nor objection — they wanted a door by which to catch the '
      'wealthy in reward',
      'They wished the rich to be punished',
      'They complained that worship was too hard'], 1),
    ('How did the Prophet ﷺ first answer them?',
     ['By telling them to earn wealth first',
      'By affirming with what they could not deny: “Has Allah not made for you '
      'what you can give as charity?”',
      'By telling them charity is only in money',
      'By rebuking them for the question'], 1),
    ('Which of these did he name as a ṣadaqah that costs no wealth?',
     ['Only fasting extra days',
      'Every tasbīḥ, takbīr, taḥmīd and tahlīl; enjoining good; forbidding '
      'evil; and marital intimacy',
      'Only building mosques',
      'Only freeing slaves'], 1),
    ('What is the difference between a qāṣir and a mutaʿaddin charity?',
     ['Qāṣir is in secret, mutaʿaddin in public',
      'Qāṣir is confined to the doer (like dhikr); mutaʿaddin reaches others '
      '(like enjoining good and forbidding evil)',
      'Qāṣir is obligatory, mutaʿaddin recommended',
      'They mean the same thing'], 1),
    ('What are the two conditions for enjoining a maʿrūf?',
     ['That it be done loudly and in a group',
      'That the commander knows it is a maʿrūf, and knows the person has left '
      'it (or asks first)',
      'That the person is older than the commander',
      'That it be written down'], 1),
    ('From the man who entered during the khuṭbah, what do we learn about '
     'commanding good?',
     ['That one may never speak during the khuṭbah',
      'The Prophet ﷺ asked “Did you pray?” before commanding — so one inquires '
      'before commanding',
      'That the two rakʿahs are forbidden then',
      'That latecomers should be turned away'], 1),
    ('Which is a condition for forbidding an evil?',
     ['That you dislike it personally',
      'That you know it is munkar by the sharī‘ah’s proof — not by taste, '
      'custom, jealousy or emotion',
      'That the person is a stranger',
      'That it happened in public only'], 1),
    ('When is forbidding an evil itself ḥarām?',
     ['When the evil would be removed entirely',
      'When forbidding it would turn it into a greater evil — as in «وَلَا '
      'تَسُبُّوا الَّذِينَ يَدْعُونَ مِنْ دُونِ الله»',
      'When the evil would be lessened',
      'When done sincerely for Allah'], 1),
    ('How did the Prophet ﷺ prove reward in a lawful desire?',
     ['By a direct verse of the Qurʾān',
      'By qiyās al-ʿaks — if placing it in the ḥarām is a sin, then placing it '
      'in the ḥalāl is a reward',
      'By the consensus of the Companions',
      'By a dream he was shown'], 1),
    ('Why is intimacy a charity even when it is for mere desire?',
     ['Because it is done in private',
      'One is commanded not to deny the soul its lawful desire «إِنَّ '
      'لِنَفْسِكَ عَلَيْكَ حَقًّا», and he does good to his wife',
      'Because it is obligatory every day',
      'Because it replaces the prayer'], 1),
    ('What do we learn from what the Companions did NOT ask about?',
     ['That they were negligent',
      'That a religious matter they did not ask about — asking about it now as '
      'religion is a bidʿah; Allah would have raised someone to ask it',
      'That questions are always blameworthy',
      'That the religion is incomplete'], 1),
])

# ------------------------------------------------------------------ T/F
b += B.tf('hd-h25-tf', [
    ('قَصْدُ الفُقَرَاءِ بِقَوْلِهِمْ «ذَهَبَ أَهْلُ الدُّثُورِ» الحَسَدُ '
     'وَالاِعْتِرَاضُ عَلَى القَدَر.',
     'The poor Companions’ aim in saying “the people of wealth have gone off…” '
     'was envy and objection to the decree.', False),
    ('مِنَ الصَّدَقَةِ قَوْلُ سُبْحَانَ اللهِ وَالحَمْدُ لِلهِ وَاللهُ '
     'أَكْبَر.',
     'Saying subḥānallāh, al-ḥamdu lillāh and Allāhu akbar is of the charity.',
     True),
    ('الأَمْرُ بِالمَعْرُوفِ وَالنَّهْيُ عَنِ المُنْكَرِ صَدَقَةٌ '
     'مُتَعَدِّيَةٌ تَنْفَعُ الغَيْر.',
     'Enjoining good and forbidding evil is a charity that reaches others.',
     True),
    ('يَجُوزُ أَنْ تَأْمُرَ بِمَعْرُوفٍ وَأَنْتَ جَاهِلٌ بِكَوْنِهِ '
     'مَعْرُوفًا.',
     'It is permitted to enjoin a maʿrūf while you are ignorant of its being a '
     'maʿrūf.', False),
    ('إِذَا كَانَ إِنْكَارُ المُنْكَرِ يَؤُولُ إِلَى مُنْكَرٍ أَعْظَمَ '
     'فَالإِنْكَارُ حَرَام.',
     'If forbidding an evil would lead to a greater evil, then forbidding it is '
     'ḥarām.', True),
    ('أَثْبَتَ النَّبِيُّ ﷺ الأَجْرَ فِي الشَّهْوَةِ الحَلَالِ بِقِيَاسِ '
     'العَكْس.',
     'The Prophet ﷺ established the reward in a lawful desire by the analogy of '
     'opposites.', True),
    ('كُلُّ مَا لَمْ يَسْأَلْ عَنْهُ الصَّحَابَةُ مِنْ أُمُورِ الدِّينِ '
     'فَالسُّؤَالُ عَنْهُ سُنَّةٌ مُسْتَحَبَّة.',
     'Everything of religion the Companions did not ask about — asking about it '
     'is a recommended sunnah.', False),
])

b += B.memorize(
    'أَوَلَيْسَ قَدْ جَعَلَ اللهُ لَكُمْ مَا تَصَّدَّقُونَ بِهِ؟ إِنَّ بِكُلِّ '
    'تَسْبِيحَةٍ صَدَقَةً… وَفِي بُضْعِ أَحَدِكُمْ صَدَقَة',
    'The poor Companions feared the rich had outrun them in reward through '
    'charity. So the Prophet ﷺ opened doors that cost nothing: every '
    '<strong>tasbīḥ, takbīr, taḥmīd and tahlīl</strong> a charity; '
    '<strong>enjoining good</strong> and <strong>forbidding evil</strong> a '
    'charity — each with its conditions; and even a man’s '
    '<strong>intimacy with his wife</strong> a charity. When they wondered how '
    'a desire could be rewarded, he answered by <em>qiyās al-ʿaks</em>: if it '
    'were a sin in the forbidden, it is a reward in the lawful. <em>Worship is '
    'not priced in wealth — the tongue, the hand, and the lawful life are all '
    'roads of ṣadaqah.</em>')

b += B.nav('h24-ya-ibadi-innii-harramtu-al-zulm.html',
           'Ḥadīth 24 · يَا عِبَادِي إِنِّي حَرَّمْتُ الظُّلْم',
           'index.html', 'Mark complete · أَتْمَمْتَ الدَّرْس · Hadeeth Hub',
           'hd-h25')

B.write('h25-dhahaba-ahl-al-duthur.html',
        'ذَهَبَ أَهْلُ الدُّثُورِ بِالأُجُور',
        'The People of Wealth Have Gone Off With the Rewards',
        'Ḥadīth 25 of al-Nawawī’s Forty (Abū Dharr al-Ghifārī, Muslim) with the '
        'sharḥ of Ibn ʿUthaymīn: the poor Companions and the doors of ṣadaqah '
        'within everyone’s reach. What they meant and did not mean; every '
        'tasbīḥ, takbīr, taḥmīd and tahlīl, and enjoining good and forbidding '
        'evil, as charity; obligatory vs non-obligatory and qāṣir vs mutaʿaddin '
        'charity; the full conditions of amr bi-l-maʿrūf and nahy ʿan '
        'al-munkar and the four outcomes of forbidding an evil (Āl ʿImrān '
        '3:104, al-Anʿām 6:108, al-Māʾidah 5:2); and reward in a lawful desire '
        'by qiyās al-ʿaks.',
        25, 'Muslim', '2', b)
print('wrote h25-dhahaba-ahl-al-duthur.html')
