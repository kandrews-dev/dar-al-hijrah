# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 2 — the first nullifier, second part.

Printed folios 37-67 (PDF indices 34-64, offset +3): slaughtering for other
than Allah with its proofs and a worked fatwā, the istighāthah that is allowed
against the one that is shirk, whether the one who abandons the prayer is a
mushrik, and the difference between the eternity of the disbeliever and that
of the sinner.
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
    'Give the two āyāt and the ḥadīth that make slaughtering an act of worship.',
    'Apply the sharḥ’s تَفْصِيل to the slaughter at a new house — and say what '
    'turns it from permitted to shirk.',
    'Distinguish the %s that is allowed from the kind that is shirk.'
    % ar('اسْتِغَاثَة'),
    'State Ibn Bāz’s ruling on %s, and give the grammatical argument it rests on.'
    % ar('تَارِكُ الصَّلَاة'),
    'Give the standard (%s) by which a sin is a major sin.' % ar('ضَابِط'),
    'Distinguish the two kinds of %s, and say which sins fall under the second.'
    % ar('خُلُود'),
])

b += B.provenance(37, 67)

# ---------------------------------------------------------------- dhabh
b += B.heading('الذَّبْحُ لِغَيْرِ اللهِ', 'Slaughtering for Other Than Allah')
b += B.sharh(
    p('The matn\'s own example, now with its proofs. The argument has one step: '
      '<em><strong>because slaughtering for Allah is an act of worship of Him — '
      'so directing it to another is shirk with Him.</strong></em> Everything else '
      'follows from establishing that first clause, and the Qurʾān establishes it '
      'twice.'))
b += B.ayah(
    'قُلْ إِنَّ صَلَاتِي وَنُسُكِي وَمَحْيَايَ وَمَمَاتِي لِلَّهِ رَبِّ '
    'الْعَالَمِينَ لَا شَرِيكَ لَهُ وَبِذَلِكَ أُمِرْتُ وَأَنَا أَوَّلُ '
    'الْمُسْلِمِينَ',
    '"Say: my prayer, my sacrifice, my living and my dying are for Allah, Lord of '
    'the worlds. He has no partner; with that I was commanded, and I am the first '
    'of those who submit."',
    'Sūrat al-Anʿām 6:162–163 · سُورَةُ الأَنْعَام')
b += B.ayah(
    'إِنَّا أَعْطَيْنَاكَ الْكَوْثَرَ فَصَلِّ لِرَبِّكَ وَانْحَرْ',
    '"Indeed We have given you al-Kawthar, so pray to your Lord and sacrifice."',
    'Sūrat al-Kawthar 108:1–2 · سُورَةُ الكَوْثَر')
b += B.prose(
    '<strong>Both āyāt put the sacrifice beside the prayer</strong> — '
    '«my prayer and my sacrifice», «pray to your Lord and sacrifice». '
    '<em>Nobody argues that prayer may be offered to a saint.</em> The pairing is '
    'the argument: whatever the prayer is, the slaughter is, and the two are '
    'commanded in one breath to one recipient.')
b += B.hadith(
    'لَعَنَ اللهُ مَنْ ذَبَحَ لِغَيْرِ اللهِ',
    '"Allah has cursed whoever slaughters for other than Allah."',
    'أَخْرَجَهُ مُسْلِمٌ فِي صَحِيحِهِ مِنْ حَدِيثِ عَلِيٍّ رَضِيَ اللهُ عَنْهُ')
b += B.sharh(
    p('<em>So <strong>it is not permissible to slaughter for al-Khiḍr, nor for '
      'al-Badawī, nor for al-Ḥusayn</strong>, nor for anyone else of mankind, nor '
      'for idols, nor for the jinn. Rather <strong>the slaughter is for Allah '
      'alone</strong>, and drawing near by sacrifices is for Him alone — as with '
      'the sacrificial animals and the offerings.</em>') +
    p('<strong>Notice who is named.</strong> Not foreign gods — <em>al-Ḥusayn</em> '
      'رَضِيَ اللهُ عَنْهُ, the grandson of the Prophet ﷺ, and figures revered as '
      'saints. The nullifier is written for people who love these names, which is '
      'exactly why it is a nullifier and not a warning about idolaters elsewhere.') +
    p('<em>And <strong>drawing near to them with sacrifices so that they may '
      'intercede for you, or cure your child — all of this is of the major '
      'shirk</strong>, and we seek refuge in Allah.</em> '
      '<strong>Read the two motives named.</strong> Neither is contempt for Allah; '
      'both are a man in need, reaching for help. That is the shape the first '
      'nullifier actually takes.'))

b += B.heading('مَسْأَلَةٌ: ذَبِيحَةُ البِنَاء', 'A Case: the Slaughter at a New House')
b += B.sharh(
    p('Ibn Bāz was asked about a custom: <em>a man, when he begins building a house '
      'for himself, slaughters an animal when the building reaches halfway — or '
      'the slaughter is delayed until the building is finished and he intends to '
      'live in it — and the relatives and neighbours are invited to it.</em>') +
    p('<em>He answered: <strong>«This practice has a detail in it»</strong></em> — '
      'and the detail is the whole lesson:') +
    table([
        row('<span dir="rtl" lang="ar">لِاتِّقَاءِ الجِنّ</span><br>'
            '<span style="font-size:.8rem;font-weight:400">to ward off the jinn</span>',
            '<em><strong>شِرْكٌ أَكْبَر</strong> — «if it is for the jinn then it is '
            'major shirk, <strong>because it is worship of other than '
            'Allah</strong>»</em>'),
        row('<span dir="rtl" lang="ar">لِتَحْصِيلِ السَّلَامَة</span><br>'
            '<span style="font-size:.8rem;font-weight:400">so that the slaughter '
            'itself secures the house and its people</span>',
            '<em><strong>لَا يَجُوز — «فَهُوَ مِنَ البِدَع»</strong>, it is of the '
            'innovations</em>'),
        row('<span dir="rtl" lang="ar">شُكْرًا لِلَّه</span><br>'
            '<span style="font-size:.8rem;font-weight:400">thanking Allah for the '
            'blessing of reaching the roof</span>',
            '<em>permitted — <strong>it is from the door of gratitude for what He '
            'has favoured him with</strong></em>'),
    ], fs='.9rem'))
b += box(
    '<p style="margin:0;font-size:.95rem"><strong>One animal, one knife, one day — '
    'and three different rulings.</strong> Nothing outward distinguishes them. '
    '<em>What moves the act between permitted, innovated and major shirk is '
    'entirely what the man intends by it</em> — which is the practical form of the '
    'definition in Lesson 1: worship is a posture, and the same outward act is '
    'worship or is not depending on where that posture is directed.</p>'
    '<p style="margin:.6rem 0 0;font-size:.92rem">And note the middle row, because '
    'students skip it. <strong>A thing can be forbidden as a bidʿah without being '
    'shirk at all.</strong> Believing the slaughter itself secures the house is not '
    'directing worship to a creature; it is inventing a cause Allah did not make. '
    'The categories are not a single slope.</p>')

# ---------------------------------------------------------------- istighathah
b += B.heading('أَيُّ اسْتِغَاثَةٍ تَجُوز؟', 'Which Seeking of Aid Is Allowed?')
b += B.sharh(
    p('Before the heavier question, a distinction that prevents a real error in the '
      'other direction. Ibn Bāz cites the story of Mūsā عَلَيْهِ السَّلَام:'))
b += B.ayah(
    'فَاسْتَغَاثَهُ الَّذِي مِنْ شِيعَتِهِ عَلَى الَّذِي مِنْ عَدُوِّهِ',
    '"And the one from his own party cried out to him for help against the one from '
    'his enemy."',
    'Sūrat al-Qaṣaṣ 28:15 · سُورَةُ القَصَص')
b += B.sharh(
    p('<em>And of that is <strong>a person seeking the aid of his companions in '
      'jihād and in war</strong>, and the like.</em>') +
    p('<strong>So the word %s is not itself the problem.</strong> A man calling to '
      'another man, present and able, for something a man can do, is ordinary — the '
      'Qurʾān reports it without censure. <em>What makes it shirk is asking of one '
      'who cannot be asked: the absent, the dead, or for what only Allah '
      'gives.</em> The nullifier is about <strong>who is being asked and for '
      'what</strong>, never about the asking.' % ar('اسْتِغَاثَة')))

# ---------------------------------------------------------------- tarik salah
b += B.heading('مَسْأَلَةٌ: تَارِكُ الصَّلَاة',
               'A Case: the One Who Abandons the Prayer')
b += B.sharh(
    p('<em>«But is it said of one who abandons the prayer that he is a mushrik? '
      '<strong>Yes — he is called a mushrik, and he is called a kāfir, upon the '
      'sounder of the two statements of the scholars.</strong>»</em> And the proof '
      'is a ḥadīth of Jābir:'))
b += B.hadith(
    'بَيْنَ الرَّجُلِ وَبَيْنَ الشِّرْكِ وَالكُفْرِ تَرْكُ الصَّلَاة',
    '"Between a man and shirk and disbelief is the abandonment of the prayer."',
    'رَوَاهُ مُسْلِمٌ فِي الصَّحِيحِ مِنْ حَدِيثِ جَابِرٍ رَضِيَ اللهُ عَنْهُ')
b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem"><strong>Now the argument — and it '
    'is grammatical, which is why it is worth slowing down for:</strong></p>'
    '<p style="margin:0;font-size:.95rem"><em>«So he named it <strong>disbelief and '
    'shirk</strong>; and <strong>the disbelief and the shirk DEFINED by the article '
    '«الْ» is the major disbelief and the major shirk.</strong>»</em></p>'
    '<p style="margin:.6rem 0 0;font-size:.93rem">The ḥadīth says '
    '<strong>الشِّرْك</strong> and <strong>الكُفْر</strong>, with the definite '
    'article — <em>the</em> shirk, <em>the</em> disbelief. And a definite noun '
    'points to the full, known reality of the thing, not to some lesser instance of '
    'it. <strong>So the wording itself carries the weight of the ruling.</strong></p>')
b += B.sharh(
    p('And the same rule answers the texts pulled in the other direction. '
      '<em>The ḥadīths in which disbelief is applied to <strong>one who disowns his '
      'father</strong>, to <strong>the one who fights</strong> a Muslim, to '
      '<strong>the wailing woman</strong>, and to <strong>one who attacks '
      'lineages</strong> — <strong>this is كُفْرٌ دُونَ كُفْر</strong>, disbelief '
      'below disbelief, with the people of knowledge, without doubt in it.</em>') +
    p('<em>And the reason: <strong>because it is كُفْرٌ مُنَكَّر — an INDEFINITE '
      'disbelief — not كُفْرٌ مُعَرَّف, a definite one.</strong></em>') +
    table([
        row(ar('الكُفْر') + ' / ' + ar('الشِّرْك') + '<br>'
            '<span style="font-size:.8rem;font-weight:400">with «الْ»</span>',
            '<em>the major — as in the ḥadīth of abandoning the prayer</em>'),
        row(ar('كُفْرٌ') + '<br><span style="font-size:.8rem;font-weight:400">'
            'indefinite</span>',
            '<em>كُفْرٌ دُونَ كُفْر — a sin among sins, not an exit from the '
            'religion</em>'),
    ]) +
    p('<strong>One article decides between a sin and an apostasy.</strong> That is '
      'the kind of thing this track exists to teach: the ruling was always in the '
      'wording, and a reader who does not notice the article will read the two sets '
      'of texts as contradicting each other and have to explain one of them away.') +
    p('<em>So what some went to, of <strong>analogising the abandonment of the '
      'prayer to these things, is not apparent</strong></em> — because the texts it '
      'is being analogised to are the indefinite kind, and this one is not.'))

# ---------------------------------------------------------------- khulud
b += B.heading('الفَرْقُ بَيْنَ خُلُودِ الكَافِرِ وَخُلُودِ العَاصِي',
               'The Eternity of the Disbeliever and That of the Sinner')
b += B.sharh(
    p('A difficulty the student will meet as soon as he reads the Qurʾān on the '
      'major sins: eternity in the Fire is stated for the murderer and for the one '
      'who returns to ribā. Ibn Bāz first fixes what a major sin is:') +
    box(
        '<p style="margin:0;font-size:.94rem"><strong dir="rtl" lang="ar">'
        'ضَابِطُ الكَبِيرَة</strong> — <em>every sin in which there came a threat '
        'of <strong>the Fire</strong>, or of <strong>Allah\'s anger</strong>, or of '
        '<strong>the curse</strong>, or in which there is <strong>a prescribed '
        'punishment in this world</strong> — that is a major sin. And what has '
        'nothing of that coming in it is called a disobedience, and is not called a '
        'major sin.</em></p>') +
    p('<em>And of the major sins, eternity in the Fire has come in some</em> — as '
      'in the one who kills, and in the one who returns to ribā:'))
b += B.ayah(
    'وَمَنْ يَقْتُلْ مُؤْمِنًا مُتَعَمِّدًا فَجَزَاؤُهُ جَهَنَّمُ خَالِدًا فِيهَا '
    'وَغَضِبَ اللَّهُ عَلَيْهِ وَلَعَنَهُ',
    '"And whoever kills a believer deliberately, his recompense is Hell, abiding '
    'therein; and Allah is angry with him and has cursed him."',
    'Sūrat al-Nisāʾ 4:93 · سُورَةُ النِّسَاء')
b += B.sharh(
    p('<em><strong>«The eternity that has come in these sins is not the eternity '
      'Allah promised the disbelievers. For eternity is of two '
      'kinds…»</strong></em>'))
b += B.sharh(
    table([
        row('<strong>١</strong> ' + ar('خُلُودٌ مُؤَبَّد') + '<br>'
            '<span style="font-size:.8rem;font-weight:400">no end at all</span>',
            '<em><strong>Everlasting, with no end — rather for ever and ever. This '
            'is the eternity of the disbelievers.</strong></em>'),
        row('<strong>٢</strong> ' + ar('خُلُودٌ طَوِيل') + '<br>'
            '<span style="font-size:.8rem;font-weight:400">long, but it ends</span>',
            '<em><strong>Because it has a long duration — but it comes to an '
            'end.</strong> This is the eternity of the one who kills himself, and '
            'the one who kills people, and the one who dies upon ribā.</em>'),
    ]))
b += B.ayah(
    'يُرِيدُونَ أَنْ يَخْرُجُوا مِنَ النَّارِ وَمَا هُمْ بِخَارِجِينَ مِنْهَا '
    'وَلَهُمْ عَذَابٌ مُقِيمٌ',
    '"They will wish to come out of the Fire, but they will not come out of it; and '
    'theirs is an enduring punishment."',
    'Sūrat al-Māʾidah 5:37 · سُورَةُ المَائِدَة')
b += B.prose(
    '<strong>That āyah is cited for the first kind, and see what it adds.</strong> '
    'It does not merely say they remain — it says <em>they will want to leave and '
    'will not</em>. The wanting is part of the punishment, and it is what '
    '«%s», enduring, is doing at the end of the verse.' % ar('مُقِيم'))
b += B.sharh(
    p('<em>And as for the second: <strong>«this one abides the measure of a year, '
      'and this one the measure of a hundred years, and this one the measure of a '
      'thousand years»</strong> — and more or less; <strong>an eternity with an end '
      'that Allah knows</strong>, سُبْحَانَهُ وَتَعَالَى.</em>') +
    p('<strong>So the word %s does not carry one fixed length.</strong> In Arabic '
      'it names a long staying; the Qurʾān uses it of both, and what separates them '
      'is not the word but <em>who it is said of</em>. The disbeliever\'s is sealed '
      'by other texts — «they will not come out of it»; the sinner\'s is not.'
      % ar('خَالِدًا')) +
    p('And that is the point at which this nullifier connects to everything after '
      'it. <strong>A man who dies upon the major shirk is in the first column; a '
      'Muslim who dies upon a major sin is in the second.</strong> The whole reason '
      'for studying the ten is to know which column a thing puts you in — '
      '<em>and, as the overview says, to guard your own Islam rather than to throw '
      'takfīr at others.</em>'))

b += B.vocab([
    ('النُّسُك', 'al-nusuk', 'sacrifice, rite',
     'Paired with the prayer in al-Anʿām 6:162 — which is the argument that a '
     'slaughter is worship'),
    ('ذَبِيحَةُ البِنَاء', 'dhabīḥat al-bināʾ', 'the slaughter at a building',
     'The worked case: shirk if for the jinn, bidʿah if the slaughter itself is '
     'thought to secure the house, permitted if thanks to Allah'),
    ('الاسْتِغَاثَة', 'al-istighāthah', 'seeking rescue',
     'Allowed of a living, present, able person — al-Qaṣaṣ 28:15; shirk when asked '
     'of the absent or the dead, or for what only Allah gives'),
    ('كُفْرٌ مُعَرَّف', 'kufr muʿarraf', 'definite disbelief',
     'الكُفْر with the article — the major; as in «بَيْنَ الرَّجُلِ وَبَيْنَ '
     'الشِّرْكِ وَالكُفْرِ تَرْكُ الصَّلَاة»'),
    ('كُفْرٌ مُنَكَّر', 'kufr munakkar', 'indefinite disbelief',
     'كُفْرٌ without the article — كُفْرٌ دُونَ كُفْر, a sin among sins; the '
     'wailing woman, disowning one’s father, attacking lineages'),
    ('ضَابِط', 'ḍābiṭ', 'a governing standard',
     'For a major sin: a threat of the Fire, or of Allah’s anger, or of the curse, '
     'or a prescribed punishment in this world'),
    ('خُلُودٌ مُؤَبَّد', 'khulūd muʾabbad', 'everlasting abiding',
     'With no end at all — the eternity of the disbelievers'),
    ('خُلُودٌ طَوِيل', 'khulūd ṭawīl', 'long abiding',
     'A long duration that comes to an end — a year, a hundred, a thousand; its '
     'term known to Allah'),
    ('مُقِيم', 'muqīm', 'enduring, resident',
     'Of the punishment in al-Māʾidah 5:37 — they will want to leave and will not'),
])

b += B.mcq('nq-l02', [
    ('What is the one-step argument that slaughtering elsewhere is shirk?',
     ['That it wastes wealth that belongs to Allah',
      'That slaughtering for Allah is an act of WORSHIP of Him — so directing it to '
      'another is shirk with Him',
      'That it imitates the practice of the Jāhiliyyah',
      'That the meat becomes unlawful'], 1),
    ('What do al-Anʿām 6:162 and al-Kawthar 108:2 have in common?',
     ['Both were revealed in Makkah',
      'Both put the SACRIFICE beside the PRAYER — and nobody argues the prayer may '
      'be offered to a saint',
      'Both mention the Day of Judgement',
      'Both address the People of the Book'], 1),
    ('Who does Ibn Bāz name among those one may not slaughter for?',
     ['Only idols and the jinn',
      'al-Khiḍr, al-Badawī and al-Ḥusayn — names the reader may revere, which is '
      'why it is a nullifier and not a warning about distant idolaters',
      'Only the kings of the past',
      'Only those buried in the Ḥijāz'], 1),
    ('In the case of the slaughter at a new house, what makes it MAJOR SHIRK?',
     ['That the neighbours are invited',
      'That it is done for the jinn — because that is worship of other than Allah',
      'That it is done before the house is finished',
      'That the meat is not distributed'], 1),
    ('What makes that same slaughter a bidʿah rather than shirk?',
     ['That it is done at the halfway point',
      'That the slaughter itself is believed to secure the house and its people — '
      'inventing a cause Allah did not make, without directing worship to a creature',
      'That it is done annually',
      'That it replaces the ʿaqīqah'], 1),
    ('When is that slaughter permitted?',
     ['Never, in any intention',
      'When it is from the door of gratitude to Allah for the blessing He favoured '
      'him with',
      'Only if a scholar is present',
      'Only if it is a sheep'], 1),
    ('What does the case of the three rulings on one slaughter demonstrate?',
     ['That scholars differ on the question',
      'That nothing outward distinguishes them — what moves the act between '
      'permitted, innovated and major shirk is entirely what is intended by it',
      'That custom determines the ruling',
      'That the ruling depends on the animal'], 1),
    ('Which istighāthah does al-Qaṣaṣ 28:15 show to be allowed?',
     ['Calling upon a prophet after his death',
      'Calling to a living, present, able person for something a person can do — as '
      'the man of Mūsā’s party cried out to him',
      'Calling upon the angels in battle',
      'Calling upon Allah through an intermediary'], 1),
    ('What is Ibn Bāz’s ruling on the one who abandons the prayer?',
     ['He is sinful but remains a Muslim by consensus',
      'He is called a mushrik and a kāfir, upon the sounder of the two statements '
      'of the scholars',
      'The matter is suspended until he dies',
      'He is a hypocrite only'], 1),
    ('What grammatical argument carries that ruling?',
     ['That the ḥadīth uses the perfect tense',
      'That the ḥadīth says الشِّرْك and الكُفْر WITH the article — and the '
      'definite points to the full known reality, i.e. the major',
      'That «bayna» implies total separation',
      'That «tark» is a verbal noun'], 1),
    ('How are the texts calling the wailing woman a kāfir answered?',
     ['They are weak narrations',
      'They are كُفْرٌ مُنَكَّر — indefinite disbelief, i.e. كُفْرٌ دُونَ كُفْر, a '
      'sin among sins; so analogising the abandonment of prayer to them is not '
      'apparent',
      'They were abrogated',
      'They apply only to the Jāhiliyyah'], 1),
    ('What is the ḍābiṭ of a major sin?',
     ['Any sin repeated three times',
      'Any sin in which came a threat of the Fire, or of Allah’s anger, or of the '
      'curse, or which carries a prescribed punishment in this world',
      'Any sin the scholars have named so',
      'Any sin involving wealth or blood'], 1),
    ('What are the two kinds of khulūd?',
     ['Khulūd in the Garden and khulūd in the Fire',
      'مُؤَبَّد, everlasting with no end — the disbelievers’; and طَوِيل, a long '
      'duration that comes to an end — the murderer’s and the one who dies on ribā',
      'Khulūd of the body and of the soul',
      'Khulūd stated in the Qurʾān and in the Sunnah'], 1),
    ('What does al-Māʾidah 5:37 add beyond saying they remain?',
     ['That their punishment is lightened in stages',
      'That they will WANT to come out and will not — the wanting is part of the '
      'punishment, which is what «muqīm», enduring, carries',
      'That they are given no food or drink',
      'That their faces are blackened'], 1),
])

b += B.tf('nq-l02-tf', [
    ('الذَّبْحُ عِبَادَةٌ، فَصَرْفُهُ لِغَيْرِ اللهِ شِرْكٌ.',
     'Slaughtering is worship, so directing it to other than Allah is shirk.', True),
    ('ذَبِيحَةُ البِنَاءِ شُكْرًا لِلَّهِ شِرْكٌ أَكْبَرُ.',
     'A slaughter at a new house, out of gratitude to Allah, is major shirk.',
     False),
    ('الاسْتِغَاثَةُ بِالحَيِّ الحَاضِرِ فِيمَا يَقْدِرُ عَلَيْهِ جَائِزَةٌ.',
     'Seeking the aid of a living, present person in what he is able to do is '
     'permitted.', True),
    ('الكُفْرُ المُعَرَّفُ بِـ«الْ» هُوَ الكُفْرُ الأَصْغَرُ.',
     'Disbelief made definite by the article is the minor disbelief.', False),
    ('خُلُودُ العَاصِي فِي النَّارِ لَهُ نِهَايَةٌ يَعْلَمُهَا اللهُ.',
     'The sinner’s abiding in the Fire has an end that Allah knows.', True),
])

b += B.memorize(
    'بَيْنَ الرَّجُلِ وَبَيْنَ الشِّرْكِ وَالكُفْرِ تَرْكُ الصَّلَاة',
    'Keep the article in view when you recite it. <strong>الشِّرْك and الكُفْر, '
    'definite, are the major</strong> — and the texts that call a wailing woman or '
    'one who disowns his father a kāfir use the word <em>indefinite</em>, which is '
    'كُفْرٌ دُونَ كُفْر. <strong>One article separates a sin from an '
    'apostasy</strong>, and a reader who does not notice it will think the two sets '
    'of texts contradict.')

b += B.nav('nq-l01-shirk-al-ibadah.html', 'النَّاقِضُ الأَوَّل · part 1',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l02')

B.write('nq-l02-dhabh-wa-tarik-al-salah.html',
        'النَّاقِضُ الأَوَّل · الذَّبْحُ وَتَارِكُ الصَّلَاة',
        'The First Nullifier — Slaughter, and the One Who Leaves the Prayer',
        'The first nullifier completed, from the words of Shaykh Ibn Bāz: the two '
        'āyāt pairing sacrifice with prayer and the ḥadīth of Muslim; the worked '
        'case of the slaughter at a new house with three rulings on one act; which '
        'istighāthah is allowed; whether the one who abandons the prayer is a '
        'mushrik, on the argument from the definite article; and the two kinds of '
        'abiding in the Fire.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ الثَّانِي', '3', b)
print('wrote nq-l02-dhabh-wa-tarik-al-salah.html')
