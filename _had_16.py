# -*- coding: utf-8 -*-
"""Ḥadīth 16 — «لَا تَغْضَبْ». Sharḥ of Ibn ʿUthaymīn, printed folios 205-208.

Range note: the running-header map (_hadmap.py) gives H16 as 205-210, but
ḥadīth 17's matn actually begins on folio 209 — H17's header page OCR'd badly,
so the detector overshot. Read the pages, found the real boundary, and cite
205-208.
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
    'Say why the sharḥ declines to identify the man who asked — and what that '
    'tells you about reading ḥadīth.',
    'Define %s, and say what the Prophet ﷺ compared anger to.' % ar('الوَصِيَّة'),
    'Give the two readings of «%s» and say which one Ibn ʿUthaymīn calls '
    'plainly obligatory.' % ar('لَا تَغْضَبْ'),
    'State the rule %s, and use it to answer why he ﷺ did not advise this man '
    'with taqwā.' % ar('يُخَاطَبُ بِمَا تَقْتَضِيهِ حَالُه'),
    'List the verbal and the practical remedies for anger, with the reason given '
    'for each.',
])

b += B.provenance(205, 208)

b += B.hadith_block(
    'عَنْ أَبِي هُرَيْرَةَ رَضِيَ اللهُ عَنْهُ أَنَّ رَجُلًا قَالَ لِلنَّبِيِّ ﷺ: '
    'أَوْصِنِي، قَالَ: «لَا تَغْضَبْ»، فَرَدَّدَ مِرَارًا، قَالَ: «لَا تَغْضَبْ». '
    'رَوَاهُ البُخَارِيُّ.',
    'Abū Hurayrah (may Allah be pleased with him) narrated that a man said to the '
    'Prophet ﷺ: "Advise me." He said: "Do not become angry." The man repeated his '
    'request several times, and he said: "Do not become angry."',
    'Narrated by Abū Hurayrah · رَوَاهُ البُخَارِيُّ — al-Bukhārī, Kitāb al-Adab, '
    'bāb al-ḥadhar min al-ghaḍab')

# ------------------------------------------------------------------ §1
b += B.heading('الرَّجُلُ المُبْهَم', 'The Man Who Is Not Named')
b += p('The sharḥ opens on something easy to walk past: <em>this man is not '
       'identified, and this happens a great deal in the ḥadīth — the unnamed one '
       'is not named.</em> And Ibn ʿUthaymīn gives the reason, then a verdict:')
b += box(
    '<p style="margin:0 0 .5rem;font-size:.94rem"><em>— <strong>because knowing '
    'the man\'s name or his description is not needed</strong>.</em></p>'
    '<p style="margin:0;font-size:.94rem"><em>— <strong>And you find some of the '
    'scholars wearying themselves greatly in determining who this man was; and '
    'what I hold is that there is no need for the trouble, so long as the ruling '
    'does not change with this man or that one.</strong></em></p>')
b += p('<strong>That is a reading rule worth taking from the very first line.</strong> '
       'A ḥadīth is read for the ruling it carries. Where a detail cannot change '
       'the ruling, chasing it is effort spent away from the point — and the Shaykh '
       'is willing to say so of scholars who did chase it.')
b += p('<em>And <strong>%s</strong> is <strong>an undertaking laid upon a person '
       'concerning a weighty matter</strong></em> — as a man leaves a bequest over '
       'his third, or over his young child, or the like. So the man is not asking '
       'for a pleasantry. <strong>He is asking for the one thing worth entrusting '
       'to him</strong>, and that is what makes the brevity of the answer so '
       'striking.' % ar('الوَصِيَّة'))

# ------------------------------------------------------------------ §2
b += B.heading('مَا هُوَ الغَضَب؟', 'What Anger Is')
b += p('Before the ruling, the thing itself. <em>The Prophet ﷺ made clear that it '
       'is <strong>a coal which Shayṭān throws into the heart of the son of '
       'Ādam</strong></em> — <em>so the heart boils, and for that reason '
       '<strong>his face reddens, the veins of his neck swell, and sometimes his '
       'hair stands on end.</strong></em>')
b += p('<strong>Note that the description is physical throughout.</strong> The '
       'redness, the swelling, the hair — anger is being described as something '
       'that <em>happens to a body</em>, which is precisely why the question that '
       'follows is a real one: can a man be commanded not to have it at all?')

# ------------------------------------------------------------------ §3
b += B.heading('مَعْنَيَا «لَا تَغْضَبْ»', 'The Two Readings of "Do Not Become Angry"')
b += p('<em>So is the Messenger\'s ﷺ intent by «%s»: that anger should not occur '
       'from you — or is the meaning: do not carry out the anger?</em> Ibn '
       'ʿUthaymīn takes them in turn, and does not treat them as equal.'
       % ar('لَا تَغْضَبْ'))
b += table([
    row('<span dir="rtl" lang="ar">الأَوَّل</span><br>'
        '<span style="font-size:.82rem;font-weight:400">the natural anger</span>',
        '<em><strong>Controlling that is difficult, because people differ in it a '
        'great difference.</strong> But there is no objection to saying he meant '
        'the natural anger in this sense: <strong>that you settle yourself and '
        'cool the matter down upon yourself</strong> — and <strong>restrain '
        'yourself when the cause is present, so that you do not become '
        'angry.</strong></em>'),
    row('<span dir="rtl" lang="ar">الثَّانِي</span><br>'
        '<span style="font-size:.82rem;font-weight:400">acting on it</span>',
        '<em>that you <strong>do not carry out what the anger demands</strong> — '
        '<strong>and this is true, and it is forbidden</strong> to do.</em>'),
])
b += p('<strong>The asymmetry is the lesson.</strong> The first is a counsel about '
       'a disposition, and it is conceded to be hard and to vary from man to man. '
       '<strong>The second is a prohibition, flat and binding on everyone</strong> '
       '— because what a man <em>does</em> is within his power in a way that what '
       'rises in his chest is not.')
b += box(
    '<p style="margin:0;font-size:.94rem"><em>So if a man became angry and wanted '
    'to divorce his wife, <strong>we say to him: be patient, and take your '
    'time.</strong></em></p>'
    '<p style="margin:.6rem 0 0;font-size:.92rem">The example is not incidental. '
    '<strong>It names the thing anger most often destroys that cannot be put '
    'back</strong> — and the counsel against it is not «do not feel this», which '
    'he cannot obey on the spot, but «do not act yet», which he can.</p>')

# ------------------------------------------------------------------ §4
b += B.heading('مِنْ فَوَائِدِ الحَدِيث', 'From the Benefits of the Ḥadīth')
b += p('<strong>١ · «%s» — they asked in order to act.</strong> <em>The Companions '
       'رَضِيَ اللهُ عَنْهُمْ, when they came to know the truth, '
       '<strong>did not stop at mere knowledge — they acted</strong>. And many '
       'people today ask about the ruling and come to know it '
       '<strong>but do not act by it</strong>. As for the Companions, '
       '<strong>when they asked about the medicine, they took it.</strong></em>'
       % ar('أَوْصِنِي'))
b += p('<em>And notice <strong>he repeated the request several times</strong></em> '
       '— and received the same four letters back each time. <strong>The man wanted '
       'more and was given the same thing again</strong>, which is itself part of '
       'the answer: he had already been told what he needed.')
b += p('<strong>٢ · %s — the one addressed is addressed by what his condition '
       'calls for.</strong> <em>And this is an important rule.</em> Ibn ʿUthaymīn '
       'raises the objection against it before answering:'
       % ar('يُخَاطَبُ بِمَا تَقْتَضِيهِ حَالُه'))
b += B.ayah(
    'وَلَقَدْ وَصَّيْنَا الَّذِينَ أُوتُوا الْكِتَابَ مِنْ قَبْلِكُمْ وَإِيَّاكُمْ '
    'أَنِ اتَّقُوا اللَّهَ',
    '"And We have instructed those given the Scripture before you, and you, to fear '
    'Allah."',
    'Sūrat al-Nisāʾ 4:131 · سُورَةُ النِّسَاء')
b += p('<em>Why did he ﷺ not advise him with the taqwā of Allah عَزَّ وَجَلَّ, as '
       'Allah said?</em> <strong>The answer:</strong> <em>that every person is '
       'addressed by what his condition calls for — <strong>so it is as though the '
       'Prophet ﷺ knew of this man that he was given to anger, and so advised him '
       'with that.</strong></em>')
b += p('And the Shaykh makes the rule portable with two cases of his own: '
       '<em>a man comes to you and says «advise me», and you know he '
       '<strong>keeps bad company</strong> — it is right to say: I advise you not '
       'to keep company with the wicked. Another comes, and you know he '
       '<strong>treats his family badly</strong> — you say to him: be good in your '
       'dealings with your family.</em>')
b += box(
    '<p style="margin:0;font-size:.95rem"><em>— <strong>that a person is advised '
    'with what his condition calls for, not with the highest thing that can be '
    'advised</strong>; because the highest thing that can be advised is other than '
    'this.</em></p>'
    '<p style="margin:.6rem 0 0;font-size:.92rem">Which quietly answers a question '
    'the student will meet everywhere in the Sunnah: <strong>why the same question '
    'gets different answers from him ﷺ.</strong> It is not inconsistency. The '
    'answer is fitted to the man standing in front of him — and the most useful '
    'advice is rarely the grandest one available.</p>')
b += p('<strong>And the harm anger does, in the Shaykh\'s own tally:</strong> '
       '<em>how many a man became angry and <strong>divorced</strong>, then came '
       'asking; and how many a man became angry and said <strong>«by Allah I will '
       'not speak to so-and-so»</strong>, then regretted it and came asking.</em> '
       '<strong>Both examples are of a man undoing something in a moment that takes '
       'years to repair</strong> — and in both, what he came back with was a '
       'question, not a remedy.')

# ------------------------------------------------------------------ §5
b += B.heading('عِلَاجُ الغَضَب', 'The Treatment of Anger')
b += p('<em>If the cause of anger is present and a man becomes angry, what should '
       'he do?</em> The sharḥ answers in two kinds, and gives a reason for each '
       'rather than leaving them as bare instructions.')
b += table([
    row('<span dir="rtl" lang="ar">الدَّوَاءُ اللَّفْظِيّ</span><br>'
        '<span style="font-size:.82rem;font-weight:400">the verbal remedy</span>',
        '<em>When he feels the anger, <strong>let him say: '
        'أَعُوذُ بِاللهِ مِنَ الشَّيْطَانِ الرَّجِيم</strong></em> — on the ḥadīth '
        'that <em>«a word which, if he said it, what he finds would leave him — '
        'were he to say: I seek refuge with Allah from the accursed '
        'Shayṭān»</em> <strong>(al-Bukhārī and Muslim)</strong>.'),
    row('<span dir="rtl" lang="ar">الدَّوَاءُ الفِعْلِيّ</span><br>'
        '<span style="font-size:.82rem;font-weight:400">the practical remedy</span>',
        '<em><strong>If he is standing, let him sit; and if he is sitting, let him '
        'lie down</strong> — <strong>because changing his outward state brings '
        'about a change in his inward state</strong>. And if that does not help, '
        '<strong>let him make wuḍūʾ</strong>: because <strong>occupying himself '
        'with the wuḍūʾ makes him forget the anger</strong>, and because '
        '<strong>the wuḍūʾ extinguishes its heat</strong>.</em>'),
])
b += p('<strong>Read the two reasons given for wuḍūʾ, because they are different '
       'in kind.</strong> One is about attention — the act occupies him, and anger '
       'needs attention to sustain itself. The other is about the coal of the first '
       'section: if anger is a heat, water is its opposite. '
       '<em>The remedy is matched to the diagnosis.</em>')
b += p('<em>And is he limited to this? <strong>The answer: he is not obliged to '
       'stop at it.</strong> We may say: if you become angry, <strong>leave the '
       'place</strong> — and many people do this; if one of them becomes angry he '
       'goes out of the house <strong>so that nothing he dislikes afterwards should '
       'happen.</strong></em>')
b += box(
    '<p style="margin:0 0 .55rem;font-size:.95rem"><em>— <strong>And forbidding '
    'the evils of character entails commanding the excellences of character.</strong> '
    'So accustom yourself…</em></p>'
    '<p style="margin:0;font-size:.94rem"><strong>That one clause is the turn of '
    'the whole lesson.</strong> «Do not become angry» looks purely negative — a '
    'thing withheld. But a prohibition of a vice is a command of the virtue facing '
    'it, so <em>«do not become angry» is also «be forbearing»</em>, and the '
    'ḥadīth stops being a restraint and becomes a training.</p>'
    '<p style="margin:.6rem 0 0;font-size:.92rem"><em>So take to '
    '<strong>الحِلْم</strong>, forbearance, as far as you are able — '
    '<strong>until your heart is at rest</strong>, and you are kept from the '
    'illnesses that come on from anger, such as diabetes and blood pressure and '
    'the like. وَاللهُ المُسْتَعَان.</em></p>')
b += p('<strong>And the Shaykh ends on the body again</strong>, where he began. '
       'Anger entered as something that reddens a face and swells a vein; it leaves '
       'as something that damages a man over years. <em>The counsel is not only for '
       'his religion.</em>')

b += B.vocab([
    ('لَا تَغْضَبْ', 'lā taghḍab', 'do not become angry', 'غ-ض-ب',
     'Read two ways: restrain yourself when the cause arises; and — binding on '
     'everyone — do not carry out what the anger demands',
     'قَالَ: «لَا تَغْضَبْ»، فَرَدَّدَ مِرَارًا، قَالَ: «لَا تَغْضَبْ»'),
    ('الوَصِيَّة', 'al-waṣiyyah', 'a bequest, a charge', 'و-ص-ي',
     'العَهْدُ إِلَى الشَّخْصِ بِأَمْرٍ هَامّ — an undertaking laid on someone '
     'concerning a weighty matter, as over one’s third or one’s young child',
     'أَوْصِنِي — advise me, i.e. entrust me with something weighty'),
    ('المُبْهَم', 'al-mubham', 'the unnamed one', 'ب-ه-م',
     'The unidentified narrator or party in a ḥadīth; left unnamed where knowing '
     'the name cannot change the ruling',
     'لَمْ يُبَيِّنْ هَذَا الرَّجُلَ، وَهَذَا يَأْتِي كَثِيرًا فِي الأَحَادِيثِ'),
    ('جَمْرَة', 'jamrah', 'a live coal', 'ج-م-ر',
     'What Shayṭān throws into the heart of the son of Ādam — so the heart boils, '
     'the face reddens and the veins swell',
     'جَمْرَةٌ يُلْقِيهَا الشَّيْطَانُ فِي قَلْبِ ابْنِ آدَمَ'),
    ('أَوْدَاج', 'awdāj', 'the veins of the neck', 'و-د-ج',
     'Plural of وَدَج; their swelling is named among the bodily signs of anger',
     'يَحْمَرُّ وَجْهُهُ وَتَنْتَفِخُ أَوْدَاجُهُ'),
    ('مُقْتَضَى الغَضَب', 'muqtaḍā al-ghaḍab', 'what the anger demands', 'ق-ض-ي',
     'The action anger presses toward; carrying it out is the sense of the '
     'prohibition that binds everyone',
     'لَا تُنَفِّذْ مُقْتَضَى الغَضَبِ'),
    ('الحِلْم', 'al-ḥilm', 'forbearance', 'ح-ل-م',
     'The virtue facing anger — since forbidding an evil of character entails '
     'commanding the excellence opposite it',
     'فَعَلَيْكَ بِالحِلْمِ مَا أَمْكَنَكَ ذَلِكَ حَتَّى يَسْتَرِيحَ قَلْبُكَ'),
    ('يُخَاطَبُ بِمَا تَقْتَضِيهِ حَالُه', 'yukhāṭab bi-mā taqtaḍīhi ḥāluh',
     'addressed by what his condition calls for', 'ق-ض-ي',
     'The rule that answers why the same question receives different answers from '
     'the Prophet ﷺ — advice is fitted to the man, not to the grandest topic',
     'أَنْ يُوصَى الإِنْسَانُ بِمَا تَقْتَضِيهِ حَالُهُ لَا بِأَعْلَى مَا يُوصَى بِهِ'),
])

b += B.mcq('hd-h16', [
    ('Why does the sharḥ decline to identify the man who asked?',
     ['Because the chain does not preserve his name',
      'Because knowing his name or description is not needed — and the ruling does '
      'not change with one man or another, so the effort spent identifying him is '
      'spent away from the point',
      'Because he later apostatised',
      'Because he was a bedouin whose name was unknown to the Companions'], 1),
    ('What is الوَصِيَّة, as defined here?',
     ['Any piece of good advice',
      'An undertaking laid upon a person concerning a weighty matter — as one '
      'bequeaths over his third or his young child',
      'A written will only',
      'A command given to a group'], 1),
    ('What did the Prophet ﷺ compare anger to?',
     ['A flood that sweeps away',
      'A live coal that Shayṭān throws into the heart of the son of Ādam, so the '
      'heart boils — the face reddens, the neck-veins swell, the hair may stand',
      'A wind that passes',
      'A debt that must be repaid'], 1),
    ('What are the two readings of «لَا تَغْضَبْ», and how do they differ in force?',
     ['Both are equally binding commands',
      'That anger should not arise — conceded to be difficult and to vary between '
      'people; and that one should not CARRY OUT what anger demands — which is '
      'binding on everyone',
      'One is for the Companions and one for later Muslims',
      'One concerns worship and the other dealings'], 1),
    ('Which example does Ibn ʿUthaymīn give of acting on anger?',
     ['Striking a servant',
      'A man who becomes angry and wants to divorce his wife — to whom we say: be '
      'patient and take your time',
      'Cursing one’s parents',
      'Abandoning the prayer'], 1),
    ('What does the Companions’ asking «أَوْصِنِي» show, per the sharḥ?',
     ['That they had not been taught the basics',
      'That when they came to know the truth they did not stop at knowledge but '
      'acted — when they asked about the medicine, they took it',
      'That advice must be sought three times',
      'That they preferred brief answers'], 1),
    ('Why was this man not advised with taqwā, as in al-Nisāʾ 4:131?',
     ['Because taqwā had not yet been legislated',
      'Because each person is addressed by what his condition calls for — it is as '
      'though the Prophet ﷺ knew this man was given to anger',
      'Because he was not yet a believer',
      'Because the āyah addresses the People of the Book only'], 1),
    ('What follows from the rule «advised by what his condition calls for»?',
     ['That advice should always name the greatest obligation',
      'That a person is advised with what his condition calls for, NOT with the '
      'highest thing that could be advised — which is why the same question gets '
      'different answers from him ﷺ',
      'That only scholars may give advice',
      'That advice must be given privately'], 1),
    ('What is the verbal remedy, and on whose authority?',
     ['Saying «lā ḥawla wa-lā quwwata illā billāh», per al-Tirmidhī',
      'Saying «أَعُوذُ بِاللهِ مِنَ الشَّيْطَانِ الرَّجِيم» — on the ḥadīth that a '
      'word, if he said it, would remove what he finds; al-Bukhārī and Muslim',
      'Reciting Āyat al-Kursī, per Aḥmad',
      'Remaining silent, per Abū Dāwūd'], 1),
    ('Why is wuḍūʾ prescribed, and what are the TWO reasons given?',
     ['Because anger breaks the wuḍūʾ, and prayer follows it',
      'Because occupying himself with it makes him forget the anger, and because '
      'the water extinguishes its heat — one reason about attention, one matched to '
      'anger being a coal',
      'Because it is obligatory before any supplication',
      'Because it delays him until the cause passes'], 1),
    ('What does the practical remedy of sitting or lying down rest on?',
     ['That standing is disliked in the Sunnah',
      'That changing his outward state brings about a change in his inward state',
      'That it prevents him striking anyone',
      'That the angels record the change'], 1),
    ('How does "forbidding the evils of character" turn the ḥadīth positive?',
     ['It does not; the ḥadīth is purely a prohibition',
      'Because forbidding a vice entails commanding the virtue facing it — so «do '
      'not become angry» is also «be forbearing», and the ḥadīth becomes a training '
      'rather than only a restraint',
      'Because anger is permitted for Allah’s sake',
      'Because the prohibition lapses after repentance'], 1),
])

b += B.tf('hd-h16-tf', [
    ('تَعْيِينُ الرَّجُلِ المُبْهَمِ فِي هَذَا الحَدِيثِ لَازِمٌ لِفَهْمِ '
     'الحُكْمِ.',
     'Identifying the unnamed man in this ḥadīth is necessary to understand the '
     'ruling.', False),
    ('النَّهْيُ عَنْ تَنْفِيذِ مُقْتَضَى الغَضَبِ حَقٌّ يَشْمَلُ كُلَّ أَحَدٍ.',
     'The prohibition of carrying out what anger demands is binding upon everyone.',
     True),
    ('يُوصَى الإِنْسَانُ دَائِمًا بِأَعْلَى مَا يُوصَى بِهِ.',
     'A person is always advised with the highest thing that can be advised.',
     False),
    ('مِنْ عِلَاجِ الغَضَبِ أَنْ يَجْلِسَ القَائِمُ وَيَضْطَجِعَ الجَالِسُ.',
     'Among the remedies for anger is that the one standing should sit and the one '
     'sitting should lie down.', True),
    ('النَّهْيُ عَنْ مَسَاوِئِ الأَخْلَاقِ يَسْتَلْزِمُ الأَمْرَ بِمَحَاسِنِهَا.',
     'Forbidding the evils of character entails commanding its excellences.', True),
])

b += B.memorize(
    'لَا تَغْضَبْ',
    'Four letters, asked for three times and given back unchanged. '
    '<strong>He wanted more and was told the same thing</strong> — because he had '
    'already been given what his own condition called for. And read it the way the '
    'sharḥ ends it: a prohibition of a vice is a command of the virtue facing it, '
    'so <em>«do not become angry» is also «be forbearing»</em>.')

b += B.nav('h15-qul-khayran.html', 'Ḥadīth 15 · فَلْيَقُلْ خَيْرًا أَوْ لِيَصْمُتْ',
           'index.html', 'Mark complete · أَتْمَمْتَ الدَّرْس · Hadeeth Hub',
           'hd-h16')

B.write('h16-la-taghdab.html',
        'لَا تَغْضَبْ',
        'Do Not Become Angry',
        'Ḥadīth 16 of al-Nawawī’s Forty with the sharḥ of Ibn ʿUthaymīn: why the '
        'questioner is left unnamed; anger as a coal thrown into the heart; the two '
        'readings of «lā taghḍab» and which one binds everyone; the rule that a man '
        'is advised by what his condition calls for; and the verbal and practical '
        'remedies, each with its reason.',
        16, 'al-Bukhārī', '2', b)
print('wrote h16-la-taghdab.html')
