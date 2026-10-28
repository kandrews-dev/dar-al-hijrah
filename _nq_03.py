# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 3 — النَّاقِضُ الثَّانِي: اتِّخَاذُ الوَسَائِط.

Printed folios 68-98 (PDF indices 65-95, offset +3). The clause the whole matn
was written against: intermediaries between a man and Allah, the reasoning the
mushrikūn actually used, and the objection of the later ones answered.
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
    'State the three acts the matn names, and who reported the %s on this clause.'
    % ar('إِجْمَاع'),
    'Give the reasoning the people of the Jāhiliyyah actually used — and name the '
    'two errors they combined.',
    'Answer the king-and-minister argument for intermediaries.',
    'State what the mushrikūn knew about their objects of worship, and why it did '
    'not excuse them.',
    'Answer the objection «we only intend their intercession with Allah» the way '
    'Ibn Bāz answers it.',
])

b += B.provenance(68, 98)

b += B.matn(
    'الثَّانِي: مَنْ جَعَلَ بَيْنَهُ وَبَيْنَ اللهِ وَسَائِطَ يَدْعُوهُمْ '
    'وَيَسْأَلُهُمُ الشَّفَاعَةَ وَيَتَوَكَّلُ عَلَيْهِمْ — كَفَرَ إِجْمَاعًا.',
    'Three acts, not one: calling upon them, asking them for intercession, and '
    'relying upon them.')
b += B.prose(
    '<strong>The author claims an %s here, and the sharḥ names who reported '
    'it.</strong> Ibn Taymiyyah, in <em>Majmūʿ al-Fatāwā</em>: '
    '<em>«whoever affirms intermediaries between Allah and His creation, like the '
    'intermediaries that exist between kings and the subjects, <strong>is a '
    'mushrik — rather this is the religion of the mushrikūn, the worshippers of '
    'idols.</strong>»</em> <em>A claim of consensus with a named reporter is worth '
    'more than one without</em>, and this track states it either way.'
    % ar('إِجْمَاع'))

# ---------------------------------------------------------------- their reasoning
b += B.heading('حُجَّةُ الجَاهِلِيَّة', 'The Reasoning They Actually Used')
b += B.sharh(
    p('The nullifier is unintelligible until you know what the mushrikūn thought '
      'they were doing. Ibn Bāz states it without caricature:') +
    box(
        '<p style="margin:0 0 .5rem;font-size:.94rem"><em>— <strong>«Their belief '
        'was that their faith that Allah is their Lord suffices, and that He is '
        'not worshipped except through an intermediary.»</strong></em></p>'
        '<p style="margin:0;font-size:.94rem"><em>— <strong>«And they say: they '
        'have, of bad deeds and blameworthy qualities, what makes them not fit to '
        'undertake the worship of Allah directly»</strong></em> — as one does not '
        'reach kings and chiefs except through a courtier.</p>') +
    p('<strong>Read that twice, because it is not arrogance. It is a kind of '
      'humility.</strong> The man reasons: <em>I am too soiled to approach Him '
      'myself; let someone cleaner carry it.</em> That is why the error has '
      'survived every century — it feels like modesty, and it recruits a true '
      'premise (he <em>is</em> unworthy) to reach a false conclusion.') +
    p('And Ibn Bāz names the two errors it joins: <em>«<strong>so they liken Allah '
      'to His creation, then they associate partners with Him</strong>… '
      '<strong>so they combined تَشْبِيه and شِرْك</strong>; and all of that is '
      'from <strong>little knowledge, dense ignorance, and imitating the fathers '
      'and the grandfathers.</strong>»</em>'))
b += table([
    row(ar('التَّشْبِيه'),
        '<em>likening Allah to a king who cannot be reached without a courtier '
        '— an error about <strong>Him</strong></em>'),
    row(ar('الشِّرْك'),
        '<em>then directing worship to the courtier — an error about '
        '<strong>what is owed to Him</strong></em>'),
])
b += B.prose(
    '<strong>The order matters: the tashbīh comes first and produces the '
    'shirk.</strong> A man does not usually set out to give worship away. He first '
    'pictures Allah wrongly — as remote, as standing on ceremony — and the shirk '
    'follows as the reasonable response to a God who is not like that. '
    '<em>Which is why the first half of every creed in this school is spent on who '
    'Allah is.</em>')

# ---------------------------------------------------------------- the analogy
b += B.heading('حُجَّةُ المَلِكِ وَالوَزِير', 'The King-and-Minister Argument')
b += B.sharh(
    p('The sharḥ does something unusual in a footnote here: it quotes the argument '
      '<em>for</em> intermediaries at its most persuasive, from a man who wrote a '
      'book defending it, and then answers it. The argument runs:') +
    box(
        '<p style="margin:0;font-size:.93rem"><em>«Suppose the sultan said to you: '
        '<strong>I have ordered my minister so-and-so to raise your needs to me</strong>, '
        'and I will grant what I wish of them and refuse what I wish — so submit '
        'your needs and he will raise them to me. Would you consider it good '
        'manners and obedience to comply — or to refuse, and say: <strong>I will '
        'not have an intermediary between me and you, because I hold that it is '
        'association with your sovereignty?</strong> I think you see the ugliness '
        'in such a refusal — for you would have opposed the command, rebelled '
        'against obedience, belittled the minister\'s station, and claimed to know '
        'better than the sultan what counts as association in his '
        'sovereignty.»</em></p>',
        wash='#fff8e6', edge='#d4a017') +
    p('<strong>It is a good argument, and it is worth seeing why it is '
      'fatal.</strong> The answer is one sentence: '
      '<em>«<strong>look how he likened Allah to His creation and equated Allah '
      'with His creation — and this is the belief of the mushrikūn</strong>»</em>, '
      'as Allah reports of them:'))
b += B.ayah(
    'تَاللَّهِ إِنْ كُنَّا لَفِي ضَلَالٍ مُبِينٍ إِذْ نُسَوِّيكُمْ بِرَبِّ '
    'الْعَالَمِينَ',
    '"By Allah, we were surely in clear error when we equated you with the Lord of '
    'the worlds."',
    'Sūrat al-Shuʿarāʾ 26:97–98 · سُورَةُ الشُّعَرَاء')
b += B.sharh(
    p('<strong>The whole argument is an analogy — and the analogy is the shirk.</strong> '
      'It does not go wrong at the end; it goes wrong at the word «suppose». '
      'Everything after that is sound reasoning <em>about a sultan</em>. The '
      'question was never whether the reasoning holds, but whether Allah is the '
      'sort of thing it applies to.') +
    p('And then the sharp edge, which is the best line in the section: '
      '<em>«And this is from <strong>the completeness of their ignorance</strong>, '
      'when they likened Allah <strong>to the TYRANTS among His servants — those '
      'who shut their doors against the needs of the subjects and did not care for '
      'them</strong>.»</em>'))
b += box(
    '<p style="margin:0;font-size:.95rem">Follow what that observation does to the '
    'analogy. <strong>The king who needs a minister to reach him is a king with a '
    'defect</strong> — he is busy, or distant, or indifferent, or does not know '
    'his people\'s needs. <em>A ruler who could hear every subject directly and '
    'chose to would be the better ruler, not the worse one.</em></p>'
    '<p style="margin:.6rem 0 0;font-size:.93rem"><strong>So the argument does not '
    'merely liken Allah to a creature. It likens Him to a bad creature</strong> — '
    'and offers that as reverence. Which is why the Qurʾān answers this whole '
    'family of reasoning not with a rule but with a description: <em>He is nearer '
    'to him than his jugular vein</em>, and <em>when My servants ask you about Me, '
    'I am near.</em></p>')

# ---------------------------------------------------------------- what they knew
b += B.heading('مَاذَا كَانُوا يَعْلَمُون؟', 'What They Knew Perfectly Well')
b += B.sharh(
    p('<em>«So <strong>Abū Jahl and his like believed that Allah was their Creator '
      'and their Provider</strong>, and the Creator of the heavens and the earth — '
      '<strong>but this belief did not benefit them</strong>, because they '
      'associated partners by worshipping idols.»</em>') +
    p('<em>«And the mushrikūn <strong>knew that the things they worshipped do not '
      'create and do not provide, and that they are poor and owned</strong> — '
      '<strong>yet Allah did not excuse them by that, and declared them '
      'disbelievers for seeking intercession from other than Allah.</strong>»</em>'))
b += B.prose(
    '<strong>That removes the excuse a student instinctively reaches for.</strong> '
    'One imagines the mushrik as a man who thinks his idol is a god — confused '
    'about metaphysics, and perhaps to be pitied for it. <em>He was not confused.</em> '
    'He knew the stone did not make the rain. He knew it owned nothing and was '
    'owned. <strong>He was condemned for what he did with that knowledge, not for '
    'lacking it</strong> — which is also why «but he knows Allah is the only '
    'Creator» establishes nothing about a man today.')

# ---------------------------------------------------------------- the objection
b += B.heading('شُبْهَةُ المُتَأَخِّرِين', 'The Objection of the Later Ones')
b += B.sharh(
    p('Ibn Bāz states the objection in the words its holders use, which is the only '
      'honest way to answer one:') +
    box(
        '<p style="margin:0;font-size:.94rem"><em>«If one of these later mushrikūn '
        'says: <strong>We do not intend that those ones benefit by themselves, or '
        'cure our sick, or help us by themselves, or harm an enemy by themselves. '
        'We only intend their intercession with Allah in that.</strong>»</em></p>') +
    p('<em>«<strong>The answer is to say to them: this is exactly the aim and the '
      'intent of the FIRST disbelievers.</strong> It was not their intent that '
      'their gods create, or provide, or benefit, or harm by themselves — '
      '<strong>for what Allah mentioned about them in the Qurʾān refutes that</strong> '
      '— <strong>they only wanted their intercession, their standing, and their '
      'bringing them near to Allah in rank.</strong>»</em>'))
b += B.ayah(
    'وَيَعْبُدُونَ مِنْ دُونِ اللَّهِ مَا لَا يَضُرُّهُمْ وَلَا يَنْفَعُهُمْ '
    'وَيَقُولُونَ هَؤُلَاءِ شُفَعَاؤُنَا عِنْدَ اللَّهِ قُلْ أَتُنَبِّئُونَ '
    'اللَّهَ بِمَا لَا يَعْلَمُ فِي السَّمَاوَاتِ وَلَا فِي الْأَرْضِ سُبْحَانَهُ '
    'وَتَعَالَى عَمَّا يُشْرِكُونَ',
    '"And they worship besides Allah that which neither harms them nor benefits '
    'them, and they say: these are our intercessors with Allah. Say: do you inform '
    'Allah of something He does not know in the heavens or in the earth? Exalted is '
    'He, and high above what they associate."',
    'Sūrat Yūnus 10:18 · سُورَةُ يُونُس')
b += B.sharh(
    p('<strong>The āyah states the objection and answers it in one verse</strong>, '
      'which is why it is the proof-text of this nullifier. The mushrikūn\'s own '
      'words are quoted — <em>«these are our intercessors with Allah»</em> — '
      'and they are not accused of thinking the idols independent. '
      '<strong>They are accused of informing Allah of an intercessor He does not '
      'know of.</strong>') +
    p('And notice the form of the refutation: <em>%s</em> — a question. '
      '<strong>An intercession that Allah has not appointed does not exist</strong>; '
      'to claim one is to tell Him of something in His own heavens and earth that '
      'He is unaware of. Put that way, the claim collapses without any need to '
      'discuss whether the intercessor is righteous.'
      % ar('أَتُنَبِّئُونَ اللَّهَ بِمَا لَا يَعْلَمُ')))
b += B.ayah(
    'أَلَا لِلَّهِ الدِّينُ الْخَالِصُ وَالَّذِينَ اتَّخَذُوا مِنْ دُونِهِ '
    'أَوْلِيَاءَ مَا نَعْبُدُهُمْ إِلَّا لِيُقَرِّبُونَا إِلَى اللَّهِ زُلْفَى',
    '"Unquestionably, to Allah belongs the pure religion. And those who take allies '
    'besides Him: we do not worship them except that they may bring us nearer to '
    'Allah in rank."',
    'Sūrat al-Zumar 39:3 · سُورَةُ الزُّمَر')
b += B.prose(
    '<strong>«We do not worship them except…» — and the Qurʾān calls it worship '
    'anyway.</strong> That is the sentence to carry out of this lesson. The '
    'mushrikūn supplied their own disclaimer, in the same words used today, and '
    'Allah recorded the disclaimer <em>and the ruling together in one verse</em>. '
    '<em>Intending something as a means does not stop it being worship.</em>')

# ---------------------------------------------------------------- today
b += B.heading('وَفِي زَمَانِنَا', 'And In Our Own Time')
b += B.sharh(
    p('Ibn Bāz does not leave this in the seventh century. He names the graves '
      'people actually go to: <em>«<strong>the worshippers of al-Badawī, and the '
      'worshippers of Shaykh ʿAbd al-Qādir, and the worshippers of al-Ḥusayn</strong>, '
      'and the worshippers of others — the affliction reached them from this road. '
      '<strong>They were ignorant of the reality of tawḥīd, and ignorant of the '
      'call of the Messengers</strong>, and matters became confused for them.»</em>') +
    p('And then the clause that explains why the practice is so hard to shift: '
      '<em>«<strong>so they fell into shirk AND DEEMED IT GOOD, and made it a '
      'religion and a means of nearness — and they rejected whoever rejected it '
      'upon them.</strong>»</em>'))
b += box(
    '<p style="margin:0;font-size:.95rem"><strong>«They fell into it and deemed it '
    'good» is the whole difficulty in six words.</strong> A man doing something he '
    'knows is wrong can be called back by a reminder. <em>A man who has made the '
    'thing into an act of devotion will experience the reminder as an attack on '
    'his religion</em> — and will answer it with the zeal of someone defending '
    'piety, which is exactly what the last clause describes.</p>')
b += B.sharh(
    p('And a warning Ibn Bāz aims at the scholars rather than the common people: '
      '<em>«<strong>and rarely will you find, in most of the lands, the scholar who '
      'has insight into this great foundation</strong>; rather you find one who is '
      'pointed to with the fingers, and it is said: he is the scholar — '
      '<strong>and he is, along with that, of those who venerate the graves with a '
      'veneration Allah did not legislate, and calls upon their occupants, and '
      'seeks rescue of them, and vows to them.</strong>»</em>') +
    p('<strong>That is a hard thing to put in a book, and it is why this nullifier '
      'is placed second.</strong> If learning alone settled the matter, the first '
      'nullifier would be enough. <em>The point of the second is that a man can '
      'hold the title of scholar and still be standing on the wrong side of '
      'it.</em>'))

b += B.vocab([
    ('الوَسَائِط', 'al-wasāʾiṭ', 'intermediaries',
     'Plural of وَاسِطَة — taken between a man and Allah to carry his need; the '
     'subject of the second nullifier'),
    ('الشَّفَاعَة', 'al-shafāʿah', 'intercession',
     'Asked of the intermediary; the Qurʾān answers that an intercession Allah has '
     'not appointed does not exist'),
    ('التَّوَكُّل', 'al-tawakkul', 'reliance',
     'The third act the matn names — reliance placed upon the intermediary rather '
     'than upon Allah'),
    ('التَّشْبِيه', 'al-tashbīh', 'likening',
     'The first of the two errors — picturing Allah as a king unreachable without '
     'a courtier; it produces the shirk that follows'),
    ('زُلْفَى', 'zulfā', 'nearness in rank',
     'al-Zumar 39:3 — «that they may bring us nearer to Allah in rank»: the '
     'mushrikūn’s own stated motive'),
    ('أَتُنَبِّئُونَ اللَّهَ', 'a-tunabbiʾūna Allāh', 'do you inform Allah?',
     'The form of the refutation in Yūnus 10:18 — claiming an unappointed '
     'intercessor is telling Him of something He does not know'),
    ('جَلَاءُ الأَفْهَام', 'Jalāʾ al-Afhām', 'a book defending intermediaries',
     'By Mukhtār al-ʿAẓmī al-Dimashqī; the sharḥ quotes its king-and-minister '
     'argument in full before answering it'),
    ('اسْتَحْسَنُوه', 'istaḥsanūh', 'they deemed it good',
     '«They fell into shirk and deemed it good, and made it a religion» — why the '
     'practice resists correction'),
])

b += B.mcq('nq-l03', [
    ('What three acts does the second nullifier name?',
     ['Slaughtering, vowing and circumambulating',
      'Calling upon them, asking them for intercession, and relying upon them',
      'Believing, loving and obeying them',
      'Building over graves, praying at them and travelling to them'], 1),
    ('Who reported the ijmāʿ on this clause, and where?',
     ['al-Nawawī, in Sharḥ Muslim',
      'Ibn Taymiyyah, in Majmūʿ al-Fatāwā — that whoever affirms intermediaries '
      'like those between kings and subjects is a mushrik',
      'Ibn Rajab, in Jāmiʿ al-ʿUlūm',
      'al-Bukhārī, in his Ṣaḥīḥ'], 1),
    ('What reasoning did the people of the Jāhiliyyah actually use?',
     ['That their idols created and provided',
      'That faith in Allah as Lord suffices, and that He is not worshipped except '
      'through an intermediary — because their own bad deeds made them unfit to '
      'approach Him directly',
      'That the idols were older than the revelation',
      'That their fathers had never been warned'], 1),
    ('Why is that reasoning so persistent, as the lesson presents it?',
     ['Because it is supported by a weak ḥadīth',
      'Because it feels like humility — the man reasons that he is too soiled to '
      'approach Him, which recruits a true premise to reach a false conclusion',
      'Because it is easier than prayer',
      'Because it is cheaper than ḥajj'], 1),
    ('Which two errors did they combine, and in what order?',
     ['Shirk then kufr',
      'التَّشْبِيه first — picturing Allah as a king needing a courtier — which '
      'then PRODUCES the shirk of directing worship to the courtier',
      'Innovation then disbelief',
      'Ignorance then arrogance'], 1),
    ('What is the one-sentence answer to the king-and-minister argument?',
     ['That ministers can be bribed and angels cannot',
      'That it likens Allah to His creation and equates Him with it — which is the '
      'belief of the mushrikūn, who confessed «we equated you with the Lord of the '
      'worlds»',
      'That the sultan in the example is unjust',
      'That kings are mortal'], 1),
    ('What is the sharpest flaw in the king analogy, per the sharḥ?',
     ['That it assumes the minister is trustworthy',
      'That it likens Allah to the TYRANTS among His servants — those who shut '
      'their doors against the subjects’ needs; so it offers a defect as reverence',
      'That sultans do not exist any more',
      'That the minister is also a subject'], 1),
    ('What did the mushrikūn know about what they worshipped?',
     ['That they were gods equal to Allah',
      'That they do not create, do not provide, and are poor and owned — and Allah '
      'did not excuse them by that knowledge',
      'That they were made by human hands only',
      'That they would be destroyed on the Day of Judgement'], 1),
    ('What follows from that, for a man today?',
     ['That ignorance is always an excuse',
      'That "but he knows Allah is the only Creator" establishes nothing — the '
      'mushrik was condemned for what he did with that knowledge, not for lacking '
      'it',
      'That knowledge of tawḥīd is not required',
      'That only scholars are accountable'], 1),
    ('How does Ibn Bāz answer «we only intend their intercession with Allah»?',
     ['That intercession is permitted if the intercessor is righteous',
      'That this is exactly the aim and intent of the FIRST disbelievers — they '
      'too did not claim their gods acted independently',
      'That intention is not examined in rulings',
      'That it is permitted but disliked'], 1),
    ('What exactly does Yūnus 10:18 accuse them of?',
     ['Of thinking the idols independent of Allah',
      'Of informing Allah of an intercessor He does not know of in His own heavens '
      'and earth — so an unappointed intercession does not exist',
      'Of worshipping in the wrong direction',
      'Of denying the resurrection'], 1),
    ('What is notable about al-Zumar 39:3?',
     ['It abrogates an earlier ruling on intercession',
      'The mushrikūn supply their own disclaimer — «we do not worship them except '
      'to bring us nearer» — and Allah records the disclaimer and calls it worship '
      'in the same verse',
      'It was revealed about the Christians only',
      'It permits nearness through the righteous'], 1),
    ('Which graves does Ibn Bāz name by way of present-day example?',
     ['Those of the Companions in Baqīʿ',
      'al-Badawī, Shaykh ʿAbd al-Qādir, and al-Ḥusayn',
      'Those of the four imāms',
      'The graves of the martyrs of Uḥud'], 1),
    ('Why does "they fell into it and deemed it good" make the practice hard to '
     'correct?',
     ['Because the texts on it are ambiguous',
      'Because a man who has made the act into devotion experiences the correction '
      'as an attack on his religion — and rejects whoever rejects it upon him',
      'Because the scholars have not written about it',
      'Because it is done in private'], 1),
    ('What warning does Ibn Bāz aim at the scholars?',
     ['That they should not write on this subject without ijāzah',
      'That rarely in most lands will you find one with insight into this '
      'foundation — and one pointed to as "the scholar" may himself venerate '
      'graves and call upon their occupants',
      'That they must not debate the grave-venerators',
      'That they should teach only in the Ḥaramayn'], 1),
])

b += B.tf('nq-l03-tf', [
    ('كَانَ المُشْرِكُونَ يَعْتَقِدُونَ أَنَّ مَعْبُودَاتِهِمْ تَخْلُقُ '
     'وَتَرْزُقُ بِنَفْسِهَا.',
     'The mushrikūn believed their objects of worship create and provide by '
     'themselves.', False),
    ('قِيَاسُ اللهِ عَلَى المَلِكِ الَّذِي لَا يُوصَلُ إِلَيْهِ إِلَّا '
     'بِوَاسِطَةٍ تَشْبِيهٌ لَهُ بِخَلْقِهِ.',
     'Likening Allah to a king unreachable except through an intermediary is '
     'likening Him to His creation.', True),
    ('قَوْلُهُمْ «مَا نَعْبُدُهُمْ إِلَّا لِيُقَرِّبُونَا» يُخْرِجُ فِعْلَهُمْ '
     'عَنْ أَنْ يَكُونَ عِبَادَةً.',
     'Their saying "we only worship them to bring us nearer" stops their act being '
     'worship.', False),
    ('نَقَلَ ابْنُ تَيْمِيَّةَ الإِجْمَاعَ عَلَى كُفْرِ مَنْ أَثْبَتَ '
     'الوَسَائِطَ.',
     'Ibn Taymiyyah reported the consensus on the disbelief of whoever affirms '
     'intermediaries.', True),
    ('الاسْتِشْفَاعُ بِمَنْ لَمْ يَأْذَنِ اللهُ لَهُ شَفَاعَةٌ ثَابِتَةٌ.',
     'Seeking intercession through one whom Allah has not permitted is an '
     'established intercession.', False),
])

b += B.memorize(
    'مَا نَعْبُدُهُمْ إِلَّا لِيُقَرِّبُونَا إِلَى اللَّهِ زُلْفَى',
    'Their own words, quoted by Allah — <strong>and He calls it worship in the '
    'same verse that records their denial of it.</strong> The disclaimer people '
    'offer today is not a new answer to the objection; <em>it is the objection the '
    'Qurʾān was answering.</em> Intending a thing as a means does not stop it being '
    'worship.')

b += B.nav('nq-l02-dhabh-wa-tarik-al-salah.html',
           'النَّاقِضُ الأَوَّل · part 2',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l03')

B.write('nq-l03-al-wasait.html',
        'النَّاقِضُ الثَّانِي · اتِّخَاذُ الوَسَائِط',
        'The Second Nullifier — Taking Intermediaries',
        'The second of the ten nullifiers, from the words of Shaykh Ibn Bāz: the '
        'three acts the matn names and Ibn Taymiyyah’s report of the consensus; the '
        'reasoning the Jāhiliyyah actually used and the two errors it joined; the '
        'king-and-minister argument quoted in full and answered; what the mushrikūn '
        'knew and why it did not excuse them; and the objection «we only intend '
        'their intercession» answered from Yūnus 10:18 and al-Zumar 39:3.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ الثَّالِث', '3', b)
print('wrote nq-l03-al-wasait.html')
