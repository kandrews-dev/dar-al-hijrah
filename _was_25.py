# -*- coding: utf-8 -*-
"""Wasitiyyah L25 -- Part 2, sections 4 and 5: the affirmation of the Foot, and
of calling out with a voice and of addressing every believer. Sharh pp.96-97."""
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
    'All three aḥādīth in this lesson are reported by <strong>البُخَارِيّ</strong> and '
    '<strong>مُسْلِم</strong>.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Explain al-Fawzān’s account of why the Fire is filled in this way.',
    'Give both refutations of the muʿaṭṭilah’s reading of %s and %s.'
    % (ar('رِجْلَه'), ar('قَدَمَه')),
    'Say why %s is added after %s, and what it parallels in the Qurʾān.'
    % (ar('بِصَوْتٍ'), ar('فَيُنَادِي')),
    'State what the ḥadīth of the %s establishes about every believer.' % ar('تُرْجُمَان'),
])

b += B.heading('٤ · إِثْبَاتُ الرِّجْلِ وَالقَدَمِ لِلَّهِ سُبْحَانَه',
               'Section 4 — The Affirmation of the Foot')
b += B.matn(
    'وَقَوْلُهُ ﷺ: «لَا تَزَالُ جَهَنَّمُ يُلْقَى فِيهَا وَهِيَ تَقُولُ: هَلْ مِنْ '
    'مَزِيدٍ؟ حَتَّى يَضَعَ رَبُّ العِزَّةِ فِيهَا رِجْلَهُ» وَفِي رِوَايَةٍ: «عَلَيْهَا '
    'قَدَمَهُ، فَيَنْزَوِي بَعْضُهَا إِلَى بَعْضٍ، فَتَقُولُ: قَطْ قَطْ» مُتَّفَقٌ '
    'عَلَيْهِ.')
b += B.hadith(
    'لَا تَزَالُ جَهَنَّمُ يُلْقَى فِيهَا وَهِيَ تَقُولُ: هَلْ مِنْ مَزِيدٍ؟ حَتَّى يَضَعَ '
    'رَبُّ العِزَّةِ فِيهَا رِجْلَهُ — فَيَنْزَوِي بَعْضُهَا إِلَى بَعْضٍ، فَتَقُولُ: قَطْ '
    'قَطْ',
    '"Hellfire will not cease — people being cast into it while it says: is there any more? — '
    'until the Lord of Might places His Foot in it. Then parts of it will draw together, and it '
    'will say: enough, enough."',
    'مُتَّفَقٌ عَلَيْهِ — al-Bukhārī and Muslim')
b += B.sharh(
    p('<strong>%s</strong> is <em>one of the names of the Fire</em>. On the name itself al-Fawzān '
      'reports two views: <em>it has been said it was named so <strong>because of the remoteness '
      'of its floor</strong>; and it has been said <strong>because of its darkness</strong>, from '
      '%s, which is darkness.</em>' % (ar('جَهَنَّم'), ar('الجُهُومَة'))) +
    p('<strong>%s</strong> — <em>that is: <strong>its people are cast into it</strong></em>. Keep '
      'that verb in mind; the refutation below turns on it.' % ar('يُلْقَى فِيهَا')) +
    p('<strong>%s</strong> — <em>it <strong>asks for more, because of its vastness</strong>; '
      '<strong>and Allah had promised it that He would fill it.</strong></em> The question is the '
      'one the Qurʾān records: %s — «is there any more?» (Qāf 50:30).'
      % (ar('وَهِيَ تَقُولُ: هَلْ مِنْ مَزِيدٍ'), ar('هَلْ مِنْ مَزِيدٍ'))))
b += B.ayah(
    'يَوْمَ نَقُولُ لِجَهَنَّمَ هَلِ امْتَلَأْتِ وَتَقُولُ هَلْ مِنْ مَزِيدٍ',
    '"On the Day We will say to Hell: are you filled? And it will say: is there any more?"',
    'Sūrat Qāf 50:30 · سورة ق')
b += B.sharh(
    p('Now al-Fawzān explains <em>why it happens this way</em>, and the reasoning is the finest '
      'thing in the section. Three facts stand together:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.93rem">'
    '<p style="margin:0">— <em>Since the Fire was at <strong>the utmost of largeness and '
    'vastness</strong>, and <strong>Allah had promised it its filling</strong>, '
    'and <strong>the requirement of His mercy was that He would not punish anyone without a '
    'crime</strong> — <strong>He fulfilled His promise and placed His Foot upon '
    'it.</strong></em></p></div>' +
    p('Read that again, because it answers a question most people never think to ask. '
      '<strong>Why is the Fire not simply filled with people?</strong> Because filling a vastness '
      'that keeps asking for more would mean condemning beyond the measure of justice — and His '
      'mercy will not punish anyone <em>without a crime</em>. So there is a promise to be kept and '
      'a mercy that will not be crossed, and <strong>the Foot is how both hold at once.</strong> '
      'The ḥadīth is a text of mercy as much as of attributes.') +
    p('<strong>%s</strong> — <em>parts of it draw in to each other, and its two edges meet, and '
      '<strong>no surplus remains in it beyond its people</strong></em>. '
      '<strong>%s</strong> — <em>that is: <strong>enough for me, it suffices me.</strong></em>'
      % (ar('فَيَنْزَوِي بَعْضُهَا إِلَى بَعْضٍ'), ar('فَتَقُولُ: قَطْ قَطْ'))) +
    p('<strong>And the shāhid: the affirming of %s and %s for Allah تعالى in the manner befitting '
      'Him سبحانه — and it is <em>of the attributes of the Essence</em>, like the Face and the '
      'Hand.</strong> So it belongs with Lesson 13, not with the descent and the laughter.'
      % (ar('الرِّجْل'), ar('القَدَم'))))
b += B.heading('غَلَطُ المُعَطِّلَةِ فِي هَذَا الحَدِيث',
               'The Muʿaṭṭilah’s Error in This Ḥadīth')
b += B.sharh(
    p('<em>And <strong>the muʿaṭṭilah erred</strong> in the explanation of this ḥadīth</em>, and '
      'al-Fawzān states their two readings exactly:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>قَدَمَهُ</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">they said: '
    '<em>a kind of created thing</em> — i.e. a group He sends ahead into it</td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>رِجْلَهُ</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">they said: '
    '<em>a crowd of people</em> — as one says '
    '<span dir="rtl" lang="ar">رِجْلُ جَرَادٍ</span>, a swarm of locusts</td></tr>'
    '</table></div>' +
    p('<strong>The reply is to say:</strong>') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.93rem">'
    '<p style="margin:0 0 .7rem"><strong>الأَوَّل ·</strong> <em>that the Prophet &#65018; '
    'said <strong><span dir="rtl" lang="ar">يَضَعَ</span></strong> — He '
    '<strong>places</strong> — <strong>and he did not say '
    '<span dir="rtl" lang="ar">يُلْقِي</span></strong>, He <strong>casts</strong>, '
    '<strong>as he did say at the beginning of the ḥadīth</strong>: '
    '<span dir="rtl" lang="ar">يُلْقَى فِيهَا</span>.</em></p>'
    '<p style="margin:0"><strong>الثَّانِي ·</strong> <em>and also, '
    '<span dir="rtl" lang="ar">القَدَم</span> <strong>cannot validly be explained as '
    '“a people” — neither really nor figuratively.</strong></em></p></div>' +
    p('The first reply is the kind of argument that only comes from reading the whole text. '
      '<strong>The ḥadīth uses both verbs, a few words apart.</strong> People are '
      '<em>cast</em> into the Fire — %s — and this is <em>placed</em> — %s. Had the Foot meant '
      'another batch of people, the Prophet &#65018; had the verb for that already in his mouth '
      'and would have used it again. <strong>The change of verb is deliberate, and it is the '
      'muʿaṭṭilah who must explain it away.</strong>' % (ar('يُلْقَى'), ar('يَضَعَ'))) +
    p('And the second reply simply tests their lexicography. They had an argument of a sort for '
      '%s, since %s is a known idiom for a swarm. <strong>But the other narration says %s</strong> '
      '— and there is no usage in Arabic, literal or figurative, in which <em>a foot</em> means '
      '<em>a crowd</em>. <strong>A taʾwīl that works for one narration and collapses on the '
      'other has not explained the ḥadīth.</strong>'
      % (ar('رِجْل'), ar('رِجْلُ جَرَادٍ'), ar('قَدَمَه'))))

b += B.heading('٥ · إِثْبَاتُ النِّدَاءِ وَالصَّوْتِ وَالكَلَامِ لِلَّهِ تَعَالَى',
               'Section 5 — Calling Out, the Voice, and Speech')
b += B.matn(
    'وَقَوْلُهُ ﷺ: «يَقُولُ اللهُ تَعَالَى: يَا آدَمُ! فَيَقُولُ: لَبَّيْكَ '
    'وَسَعْدَيْكَ. فَيُنَادِي بِصَوْتٍ: إِنَّ اللهَ يَأْمُرُكَ أَنْ تُخْرِجَ مِنْ '
    'ذُرِّيَّتِكَ بَعْثًا إِلَى النَّارِ» مُتَّفَقٌ عَلَيْهِ. وَقَوْلُهُ ﷺ: «مَا '
    'مِنْكُمْ مِنْ أَحَدٍ إِلَّا سَيُكَلِّمُهُ رَبُّهُ، لَيْسَ بَيْنَهُ وَبَيْنَهُ '
    'تُرْجُمَانٌ».')
b += B.hadith(
    'يَقُولُ اللهُ تَعَالَى: يَا آدَمُ! فَيَقُولُ: لَبَّيْكَ وَسَعْدَيْكَ. فَيُنَادِي '
    'بِصَوْتٍ: إِنَّ اللهَ يَأْمُرُكَ أَنْ تُخْرِجَ مِنْ ذُرِّيَّتِكَ بَعْثًا إِلَى النَّارِ',
    '"Allah will say: O Ādam! And he will say: at Your service, and in Your pleasure. Then He '
    'will call out with a voice: Allah commands you to bring out from your offspring a contingent '
    'for the Fire."',
    'مُتَّفَقٌ عَلَيْهِ — al-Bukhārī and Muslim')
b += B.sharh(
    p('Ādam\'s answer is two words, and both are built the same way. <strong>%s</strong> — '
      'the sense is <em>standing firm upon obedience</em>, <em>and it is manṣūb as a maṣdar, '
      '<strong>and it was put in the dual for emphasis</strong></em> — that is, '
      '<em>an answering after an answering</em>. And <strong>%s</strong> — <em>from %s, which is '
      '<strong>compliance</strong>: that is, <strong>a helping in Your obedience after a '
      'helping.</strong></em>' % (ar('لَبَّيْكَ'), ar('وَسَعْدَيْكَ'), ar('المُسَاعَدَة'))) +
    p('The dual is not a quirk of idiom. Both words are doubled to say <em>again and again, '
      'without end</em> — which is how the first man answers when he is called by name.') +
    p('<strong>%s</strong> — <em>with a kasrah on the دال; <strong>and the One calling out is '
      'Allah تعالى.</strong></em>' % ar('فَيُنَادِي')))
b += B.sharh(
    p('And then the word the section is named for. <strong>%s</strong> — <em>is '
      '<strong>an emphasis of his saying %s</strong>, because <strong>a calling-out does not '
      'occur except with a voice</strong>.</em>' % (ar('بِصَوْتٍ'), ar('يُنَادِي'))) +
    p('al-Fawzān then gives the parallel, and it is exactly the construction from Lesson 18: '
      '<em>and <strong>this is like His saying تعالى</strong></em> %s — «and Allah spoke to Mūsā '
      'with a direct speaking» (al-Nisāʾ 4:164).'
      % ar('وَكَلَّمَ اللَّهُ مُوسَى تَكْلِيمًا')) +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.93rem">The logic is the same in both places. '
    '<span dir="rtl" lang="ar">تَكْلِيمًا</span> after '
    '<span dir="rtl" lang="ar">كَلَّمَ</span> forecloses reading the speaking loosely; '
    '<span dir="rtl" lang="ar">بِصَوْتٍ</span> after '
    '<span dir="rtl" lang="ar">يُنَادِي</span> forecloses reading the calling as a mere '
    'conveying of meaning. <strong>In each case a word is added that a figurative reading cannot '
    'absorb.</strong></p></div>' +
    p('<strong>%s</strong> — <em>al-baʿth here carries the meaning of '
      '<strong>the contingent dispatched</strong> to it; and the meaning of that is: '
      '<strong>separate out</strong> the people</em> of the Fire.' % ar('بَعْثًا إِلَى النَّارِ')) +
    p('<strong>And the shāhid: the affirming of saying from Allah, and of '
      '<em>calling out with a voice that is heard</em>; and that this will occur on the Day of '
      'Rising — so in it is that Allah says and calls out <strong>whenever He wills and however '
      'He wills.</strong></strong>'))
b += B.hadith(
    'مَا مِنْكُمْ مِنْ أَحَدٍ إِلَّا سَيُكَلِّمُهُ رَبُّهُ، لَيْسَ بَيْنَهُ وَبَيْنَهُ '
    'تُرْجُمَانٌ',
    '"There is not one of you but his Lord will speak to him, with no interpreter between him and '
    'Him."',
    'رَوَاهُ البُخَارِيُّ وَمُسْلِمٌ')
b += B.sharh(
    p('<strong>%s</strong> — <em>the address is to the Ṣaḥābah, <strong>and it is general to all '
      'of the believers</strong></em>. <strong>%s</strong> — <em>that is: '
      '<strong>without an intermediary</strong></em>. And <strong>%s</strong> — '
      '<em>al-turjumān is <strong>one who renders into another language</strong>.</em>'
      % (ar('مَا مِنْكُمْ مِنْ أَحَدٍ'), ar('إِلَّا سَيُكَلِّمُهُ رَبُّهُ'),
         ar('لَيْسَ بَيْنَهُ وَبَيْنَهُ تُرْجُمَانٌ'))) +
    p('<strong>And the shāhid: the affirming of Allah\'s سبحانه addressing of His servants; and '
      'that He speaks when He wills — <em>so His speech is of His attributes of the '
      'Actions</em> — and <strong>that He will speak to every believer on the Day of '
      'Rising.</strong></strong>') +
    p('Set this beside Lesson 18, where %s was the honour that earned Mūsā the title %s, and the '
      'messengers spoken to without an intermediary were counted on the fingers of one hand. '
      '<strong>Here the same thing is promised to every believer in the room.</strong> The '
      'attribute that the deniers worked hardest to explain away turns out to be the one each of '
      'them is personally promised.' % (ar('التَّكْلِيم'), ar('الكَلِيم'))))

b += B.vocab([
    ('جَهَنَّم', 'jahannam', 'Hellfire',
     'Named for the remoteness of its floor, or from الجُهُومَة — darkness'),
    ('يَنْزَوِي', 'yanzawī', 'draws together',
     'Its two edges meet, and no surplus remains beyond its people'),
    ('قَطْ قَطْ', 'qaṭ qaṭ', 'enough, enough',
     'That is: حَسْبِي وَيَكْفِينِي'),
    ('رِجْلُ جَرَاد', 'rijl jarād', 'a swarm of locusts',
     'The idiom the muʺṭṭilah leaned on — which fails on قَدَمَهُ'),
    ('لَبَّيْكَ', 'labbayk', 'at Your service',
     'Manṣūb as a maṣdar, in the dual for emphasis: answering after answering'),
    ('سَعْدَيْكَ', 'saʿdayk', 'in Your pleasure',
     'From المُسَاعَدَة, compliance — a helping in Your obedience after a helping'),
    ('بِصَوْت', 'bi-ṣawt', 'with a voice',
     'An emphasis of يُنَادِي — as تَكْلِيمًا emphasises كَلَّمَ'),
    ('التُّرْجُمَان', 'al-turjumān', 'the interpreter',
     'One who renders into another language — and there will be none'),
])
b += B.mcq('ws-l25', [
    ('Why, according to al-Fawzān, is the Fire filled by the placing of the Foot?',
     ['Because its people are too few',
      'Because Allah promised to fill it, yet the requirement of His mercy is that He punish no '
      'one without a crime — so the promise is kept without crossing the mercy',
      'Because the Fire asked for it',
      'Because the angels could not fill it'], 1),
    ('What is the first reply to the muʿaṭṭilah here?',
     ['That no scholar held their view',
      'That the Prophet ﷺ said %s — He <em>places</em> — and did not say %s, <em>casts</em>, '
      'which he had already used in the same ḥadīth' % (ar('يَضَعَ'), ar('يُلْقِي')),
      'That the ḥadīth is only in Muslim', 'That جهنم is a proper name'], 1),
    ('What is the second reply?',
     ['That رِجْل never means a swarm in Arabic',
      'That %s cannot validly be explained as "a people" — neither really nor figuratively, so '
      'the taʾwīl collapses on the other narration' % ar('القَدَم'),
      'That the narration is contradicted by the Qurʾān',
      'That the Fire does not speak'], 1),
    ('To which class of attributes does the Foot belong?',
     ['The attributes of the Actions, like the descent',
      'The attributes of the Essence, like the Face and the Hand',
      'Neither; its meaning is unknown', 'The attributes of negation'], 1),
    ('Why are %s and %s in the dual?' % (ar('لَبَّيْكَ'), ar('سَعْدَيْكَ')),
     ['Because Ādam addressed two angels',
      'For emphasis — an answering after an answering, a helping after a helping',
      'Because they are vocatives', 'Because the verbs are dual'], 1),
    ('What work does %s do, and what does it parallel?' % ar('بِصَوْتٍ'),
     ['It identifies which angel called out',
      'It emphasises %s, since a calling-out occurs only with a voice — as %s emphasises %s'
      % (ar('يُنَادِي'), ar('تَكْلِيمًا'), ar('كَلَّمَ')),
      'It specifies the volume of the call',
      'It restricts the call to the Day of Rising'], 1),
    ('What does the ḥadīth of the %s establish?' % ar('تُرْجُمَان'),
     ['That Arabic will be the language of the Hereafter',
      'That Allah will speak to every believer on the Day of Rising, with no intermediary between '
      'them',
      'That the prophets will intercede as interpreters',
      'That only the messengers are addressed directly'], 1),
])
b += B.tf('ws-l25-tf', [
    ('الرِّجْلُ وَالقَدَمُ مِنْ صِفَاتِ الذَّاتِ.',
     'The Foot is of the attributes of the Essence.', True),
    ('قَالَ النَّبِيُّ ﷺ: «حَتَّى يُلْقِيَ رَبُّ العِزَّةِ فِيهَا رِجْلَهُ».',
     'The Prophet ﷺ said the Lord of Might would <em>cast</em> His Foot into it.', False),
    ('النِّدَاءُ لَا يَكُونُ إِلَّا بِصَوْتٍ.',
     'A calling-out does not occur except with a voice.', True),
    ('يُكَلِّمُ اللهُ كُلَّ مُؤْمِنٍ يَوْمَ القِيَامَةِ بِلَا وَاسِطَةٍ.',
     'Allah will speak to every believer on the Day of Rising without an intermediary.', True),
])
b += B.memorize(
    'مَا مِنْكُمْ مِنْ أَحَدٍ إِلَّا سَيُكَلِّمُهُ رَبُّهُ، لَيْسَ بَيْنَهُ وَبَيْنَهُ '
    'تُرْجُمَانٌ',
    'In Lesson 18, being spoken to without an intermediary was the distinction of two or three '
    'messengers. Here it is promised to you. Learn it as a creed and let it work on you as a '
    'warning: the conversation is coming, and nobody will be translating.')
b += B.aiquiz('The Foot and the calling out with a voice in al-Aqidah al-Wasitiyyah: why '
              'al-Fawzan says the Fire is filled by the placing of the Foot given the promise and '
              'the mercy, the two refutations of the muattilah including the deliberate change '
              'from yulqa to yada and that qadam cannot mean a people even figuratively, labbayk '
              'and sadayk in the dual for emphasis, bi-sawt paralleling takliman, and the hadith '
              'that Allah will speak to every believer with no interpreter')
b += B.further()
b += B.nav('was-l24-farah-dahik-ajab.html', 'That Allah Rejoices, Laughs and Wonders',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l25')

io.open(os.path.join(B.AQ, 'was-l25-qadam-nida-sawt.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'الرِّجْلُ وَالقَدَمُ · وَالنِّدَاءُ بِصَوْت',
    'The Foot, and the Calling Out with a Voice',
    'Lesson 25 of al-ʿAqīdah al-Wāsiṭiyyah: why the Fire is filled '
    'by the placing of the Foot — a promise kept without crossing the mercy — the two '
    'refutations of the muʿaṭṭilah, and the calling out with a voice that no '
    'figurative reading can absorb, ending on the ḥadīth that every believer will be '
    'spoken to with no interpreter.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الخَامِسُ وَالعِشْرُون', '3',
           'الرِّجْلُ وَالقَدَمُ · وَالنِّدَاءُ بِصَوْت',
           'The Foot, and the Calling Out with a Voice', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l25-qadam-nida-sawt.html')
