# -*- coding: utf-8 -*-
"""Wasitiyyah L24 -- Part 2, sections 2 and 3: that Allah rejoices, laughs,
wonders and looks. Sharh pp.94-95."""
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
    'The first two aḥādīth are <strong>مُتَّفَقٌ عَلَيْهِمَا</strong> — al-Bukhārī and Muslim. '
    'For the third, see the تَنْبِيه on this page.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Say why %s for Allah is an attribute of perfection and not of need.' % ar('الفَرَح'),
    'Give the reason, from the ḥadīth itself, that Allah laughs at the two men.',
    'Distinguish the two kinds of %s and say which is meant of Allah.' % ar('العَجَب'),
    'Name the three attributes established in the ḥadīth of §3.',
])

b += B.heading('٢ · إِثْبَاتُ أَنَّ اللهَ يَفْرَحُ وَيَضْحَك',
               'Section 2 — That Allah Rejoices and Laughs')
b += B.matn(
    'وَقَوْلُهُ ﷺ: «لِلَّهِ أَشَدُّ فَرَحًا بِتَوْبَةِ عَبْدِهِ مِنْ أَحَدِكُمْ '
    'بِرَاحِلَتِهِ…» الحَدِيثَ، مُتَّفَقٌ عَلَيْهِ. وَقَوْلُهُ ﷺ: «يَضْحَكُ اللهُ إِلَى '
    'رَجُلَيْنِ يَقْتُلُ أَحَدُهُمَا الآخَرَ، كِلَاهُمَا يَدْخُلُ الجَنَّةَ» مُتَّفَقٌ '
    'عَلَيْهِ.')
b += B.hadith(
    'لِلَّهِ أَشَدُّ فَرَحًا بِتَوْبَةِ عَبْدِهِ مِنْ أَحَدِكُمْ بِرَاحِلَتِهِ',
    '"Allah is more intensely joyful at the repentance of His servant than any one of you is at '
    'his riding-camel…"',
    'مُتَّفَقٌ عَلَيْهِ — al-Bukhārī and Muslim')
b += B.sharh(
    p('The grammar first, as al-Fawzān always gives it. <strong>%s</strong> — '
      '<em>the lām is the <strong>lām of beginning</strong></em>; and <strong>%s</strong> is '
      '<em>manṣūb as <strong>%s</strong></em>, specifying in what respect the intensity holds.'
      % (ar('لِلَّهِ'), ar('فَرَحًا'), ar('التَّمْيِيز'))) +
    p('<strong>%s</strong> — <em>in the language it is <strong>gladness and the delight of the '
      'heart</strong>.</em> And <strong>%s</strong> — <em>and al-tawbah is '
      '<strong>the desisting from the sin and the returning</strong></em> to Allah.'
      % (ar('الفَرَح'), ar('بِتَوْبَةِ عَبْدِهِ'))) +
    p('Note the author\'s citation: he writes <strong>%s</strong>, and al-Fawzān explains that '
      'this is <em>an implied word</em> — <em>that is: <strong>complete the ḥadīth</strong>, '
      'because the author restricted himself to <strong>the point of evidence</strong> from '
      'it.</em> The full ḥadīth is the famous parable of the man who loses his mount in the '
      'desert with his food and drink on it, despairs of life, and then finds it standing '
      'there — <strong>and the author quotes only as much as makes his point.</strong>'
      % ar('الحَدِيثَ')))
b += B.sharh(
    p('<strong>And the shāhid: the affirming of joy for Allah سبحانه, in the manner that befits '
      'His majesty; and it is <em>an attribute of perfection</em> — the joy of no one of His '
      'creation resembles it.</strong>') +
    p('And then al-Fawzān heads off the obvious misunderstanding before it forms. The servant\'s '
      'repentance is not something Allah <em>gains</em> by: <strong>%s</strong> — '
      '<em>for He سبحانه <strong>is not benefited by the obedience of the obedient, nor harmed by '
      'the disobedience of the disobedient.</strong></em>'
      % ar('لَا تَنْفَعُهُ طَاعَةُ المُطِيعِ وَلَا تَضُرُّهُ مَعْصِيَةُ العَاصِي')) +
    p('Which makes the ḥadīth stranger and better, not weaker. A joy that gains nothing is a joy '
      'that is <strong>entirely for the sake of the one repenting</strong>. The man in the parable '
      'rejoices because he was going to die and now will live; Allah rejoices at the return of '
      'someone whose return adds nothing to Him. <strong>That is the whole doctrine of mercy in '
      'one comparison.</strong>'))
b += B.hadith(
    'يَضْحَكُ اللهُ إِلَى رَجُلَيْنِ يَقْتُلُ أَحَدُهُمَا الآخَرَ، كِلَاهُمَا يَدْخُلُ '
    'الجَنَّةَ',
    '"Allah laughs at two men, one of whom kills the other — and both of them enter the '
    'Garden."',
    'مُتَّفَقٌ عَلَيْهِ — al-Bukhārī and Muslim')
b += B.sharh(
    p('Read on its own the ḥadīth is a riddle: a killer and his victim, both in Paradise. '
      '<em>And the ḥadīth states <strong>the reason for that</strong> in its own words:</em>') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.95rem" dir="rtl" lang="ar">يُقَاتِلُ هَذَا فِي سَبِيلِ '
    'اللهِ عَزَّ وَجَلَّ فَيُسْتَشْهَدُ، ثُمَّ يَتُوبُ اللهُ عَلَى القَاتِلِ فَيُسْلِمُ، '
    'فَيُقَاتِلُ فِي سَبِيلِ اللهِ عَزَّ وَجَلَّ فَيُسْتَشْهَدُ.</p>'
    '<p style="margin:.5rem 0 0;font-size:.9rem">— <em>this one fights in the path of Allah '
    'and is martyred; then Allah turns to the killer in acceptance and he becomes Muslim, and he '
    'fights in the path of Allah and is martyred.</em></p></div>' +
    p('<em>And this is from <strong>the perfection of Allah\'s beneficence and the breadth of His '
      'mercy</strong>: for the Muslim fights in the path of Allah and the disbeliever kills him, '
      'so Allah honours the Muslim with martyrdom; <strong>then Allah bestows a favour upon that '
      'very disbelieving killer and guides him to Islam</strong> — so the two of them enter the '
      'Garden together.</em>') +
    p('<em>So <strong>this is a wondrous affair</strong> — <strong>and laughter comes about from '
      'the things that cause wonder.</strong></em> That last clause is the key to reading the '
      'attribute correctly. The laughter is not amusement at the killing; it is the response to '
      'something astonishing. <strong>The man who took a believer\'s life ends beside him in '
      'Paradise, by the mercy of the One both of them now worship.</strong>') +
    p('<strong>And the shāhid: the affirming of laughter for Allah سبحانه — an attribute of His '
      'attributes of the Actions, which we affirm for Him in the manner befitting His majesty and '
      'His greatness; it is <em>not like the laughter of the created thing</em>.</strong>'))

b += B.heading('٣ · إِثْبَاتُ أَنَّ اللهَ يَعْجَبُ وَيَضْحَكُ وَيَنْظُر',
               'Section 3 — That Allah Wonders, Laughs and Looks')
b += B.matn(
    'وَقَوْلُهُ ﷺ: «عَجِبَ رَبُّنَا مِنْ قُنُوطِ عِبَادِهِ وَقُرْبِ غِيَرِهِ، يَنْظُرُ '
    'إِلَيْكُمْ أَزِلِينَ… فَيَظَلُّ يَضْحَكُ».')
b += B.hadith(
    'عَجِبَ رَبُّنَا مِنْ قُنُوطِ عِبَادِهِ وَقُرْبِ غِيَرِهِ، يَنْظُرُ إِلَيْكُمْ '
    'أَزِلِينَ… فَيَظَلُّ يَضْحَكُ',
    '"Our Lord wonders at the despair of His servants, and how near His change is. He looks at '
    'you straitened… and He keeps on laughing."',
    'al-Fawzān cites it as رَوَاهُ أَحْمَدُ وَغَيْرُهُ')
b += B.sharh(
    '<div style="background:#fff8e6;border-right:4px solid #d4a017;'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .9rem">'
    '<p style="margin:0;font-size:.9rem"><strong dir="rtl" lang="ar">تَنْبِيهٌ</strong> — '
    'al-Fawzān gives this ḥadīth’s attribution, <em>reported by Aḥmad '
    'and others</em>, <strong>without stating a grading for it</strong>. This track’s rule '
    'is that every ḥadīth carries a grading attributed to a named scholar — so the '
    'page reports what the sharḥ reports and <strong>does not supply a grading of its '
    'own</strong>. The two aḥādīth of §2 above are '
    '<span dir="rtl" lang="ar">مُتَّفَقٌ عَلَيْهِمَا</span>, and the attributes taught here '
    '— the wonder, the laughter and the looking — rest on more than this one '
    'text.</p></div>' +
    p('Now the attribute. <strong>%s is of two kinds</strong>, and the distinction decides how the '
      'ḥadīth is read:' % ar('العَجَب')) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>١</strong> what the doer <strong>praises</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">its meaning is '
    '<strong>finding it good</strong>, and <em>informing of his being pleased with it</em> '
    '(<span dir="rtl" lang="ar">الاسْتِحْسَانُ وَالإِخْبَارُ عَنْ رِضَاهُ بِهِ</span>)</td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>٢</strong> what he <strong>dislikes</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">its meaning is '
    '<strong>rejection and censure</strong> of it '
    '(<span dir="rtl" lang="ar">الإِنْكَارُ وَالذَّمُّ لَهُ</span>)</td></tr>'
    '</table></div>' +
    p('And the ḥadīth is plainly the second kind: the wonder is <em>at despair</em>. '
      '<strong>%s — al-qunūṭ is the <em>severity</em> of despair</strong>; and '
      '<strong>%s</strong> — vowelled with a kasrah on the غ and a fatḥah on the ي — '
      '<em>is <strong>His changing of the condition from hardship to ease</strong></em>.'
      % (ar('مِنْ قُنُوطِ عِبَادِهِ'), ar('وَقُرْبِ غِيَرِهِ'))) +
    p('Put the two halves of the clause together and you have the thing being wondered at: '
      '<strong>they are giving up precisely when the relief is nearly here.</strong> The wonder '
      'is not at suffering; it is at despairing <em>a moment before the change</em> — and the '
      'censure in it is a mercy, because the One wondering is the One who was about to change it.') +
    p('<strong>%s</strong> — <em>and <strong>%s</strong>, with a sukūn on the ز, is '
      '<strong>straitness</strong>; one says <strong>%s</strong> — the man became '
      '<strong>in straits and in drought</strong>.</em>'
      % (ar('يَنْظُرُ إِلَيْكُمْ أَزِلِينَ'), ar('الأَزْل'),
         ar('أَزِلَ الرَّجُلُ يَأْزِلُ أَزْلًا'))) +
    p('<strong>%s</strong> — <em>this is of His attributes of the Actions, in which '
      '<strong>nothing of His creation resembles Him</strong>.</em>' % ar('فَيَظَلُّ يَضْحَكُ')))
b += B.sharh(
    p('al-Fawzān counts the attributes in the ḥadīth: <em>in it is the affirming of '
      '<strong>two of Allah\'s attributes of the Actions</strong> — <strong>%s and %s</strong> — '
      'and they are two attributes befitting His majesty, <strong>not like the wonder of the '
      'created thing nor the laughter of the created thing</strong>. And in the ḥadīth is also '
      '<strong>the affirming of %s for Allah سبحانه</strong>, and it too is of His attributes of '
      'the Actions, <strong>for He looks at His servants, and nothing in the earth or in the '
      'heaven is hidden from Him.</strong></em>'
      % (ar('العَجَب'), ar('الضَّحِك'), ar('النَّظَر'))) +
    p('Three attributes, then — and notice what the sequence of the ḥadīth does with them. '
      'He <em>looks</em> at them in their straits, He <em>wonders</em> at their despair, and He '
      '<em>keeps on laughing</em>. <strong>Each one presupposes that He is attending to a '
      'particular person in a particular difficulty</strong>, which is the whole reason these '
      'texts were ever worth preserving. A God described only in negations does not look at '
      'anyone.'))

b += B.vocab([
    ('الفَرَح', 'al-faraḥ', 'joy',
     'In the language: gladness and the delight of the heart — an attribute of perfection'),
    ('التَّوْبَة', 'al-tawbah', 'repentance',
     'Desisting from the sin and returning to Allah'),
    ('التَّمْيِيز', 'al-tamyīz', 'specification',
     'Why فَرَحًا is manṣūb in أَشَدُّ فَرَحًا'),
    ('الضَّحِك', 'al-ḍaḥik', 'laughter',
     'Of the attributes of the Actions — and it comes about from what causes wonder'),
    ('العَجَب', 'al-ʿajab', 'wonder',
     'Two kinds: finding good and being pleased, or rejecting and censuring'),
    ('القُنُوط', 'al-qunūṭ', 'despair',
     'The *severity* of despair — what the wonder is directed at'),
    ('الغِيَر', 'al-ghiyar', 'change of condition',
     'His changing the state from hardship to ease — and it is NEAR'),
    ('الأَزْل', 'al-azl', 'straitness',
     'أَزِلِينَ — in straits and in drought'),
])
b += B.mcq('ws-l24', [
    ('Why is Allah’s joy at the servant’s repentance not a joy of need?',
     ['Because joy is figurative when ascribed to Him',
      'Because He is not benefited by the obedience of the obedient nor harmed by the '
      'disobedience of the disobedient — so the joy is entirely for the repentant’s sake',
      'Because the ḥadīth concerns the angels’ joy',
      'Because the repentance was decreed anyway'], 1),
    ('What does al-Fawzān say the word %s indicates in the author’s citation?'
     % ar('الحَدِيثَ'),
     ['That the ḥadīth is weak in part',
      'That a word is implied — "complete the ḥadīth" — because the author quoted only the point '
      'of evidence',
      'That it was narrated in meaning only',
      'That there are two versions of it'], 1),
    ('What is the reason, in the ḥadīth itself, that both men enter the Garden?',
     ['They repented together before dying',
      'The first is martyred fighting; then Allah turns to his killer in acceptance, he becomes '
      'Muslim, fights in Allah’s path and is martyred too',
      'They were brothers and one was forgiven for the other',
      'The killing was accidental'], 1),
    ('How does al-Fawzān explain why laughter is the fitting response here?',
     ['Because the believers will laugh at the disbelievers',
      'Because laughter comes about from the things that cause wonder — and this is a wondrous '
      'affair',
      'Because the ḥadīth is a parable, not literal',
      'Because the killer was humiliated'], 1),
    ('Which of the two kinds of %s applies in the ḥadīth of §3?' % ar('العَجَب'),
     ['The kind meaning finding good and being pleased',
      'The kind meaning rejection and censure — the wonder is at <em>despair</em>',
      'Neither; it is a third kind', 'Both at once'], 1),
    ('What is %s, and why does it matter to the meaning?' % ar('وَقُرْبِ غِيَرِهِ'),
     ['The nearness of His punishment — so the despair is justified',
      'The nearness of His changing their condition from hardship to ease — so they are '
      'despairing a moment before the relief',
      'The nearness of the Hour',
      'The nearness of His servants to Him'], 1),
    ('Which three attributes does al-Fawzān find in the ḥadīth of §3?',
     ['Mercy, anger and coming', 'Wonder, laughter and looking',
      'Hearing, sight and knowledge', 'Descent, speech and forgiving'], 1),
])
b += B.tf('ws-l24-tf', [
    ('الفَرَحُ صِفَةُ كَمَالٍ لِلَّهِ تَعَالَى.',
     'Joy is an attribute of perfection for Allah.', True),
    ('تَنْفَعُ اللهَ طَاعَةُ المُطِيعِ وَتَضُرُّهُ مَعْصِيَةُ العَاصِي.',
     'Allah is benefited by the obedience of the obedient and harmed by the disobedience of the '
     'disobedient.', False),
    ('الضَّحِكُ يَكُونُ مِنَ الأُمُورِ المُعْجِبَةِ.',
     'Laughter comes about from the things that cause wonder.', True),
    ('النَّظَرُ مِنْ صِفَاتِ اللهِ الفِعْلِيَّةِ.',
     'The looking is of Allah’s attributes of the Actions.', True),
])
b += B.memorize(
    'عَجِبَ رَبُّنَا مِنْ قُنُوطِ عِبَادِهِ وَقُرْبِ غِيَرِهِ',
    'The two halves belong together or the sentence loses its point: they despair, and the change '
    'is already near. Whatever you are in the middle of, this is the clause that is about you.')
b += B.aiquiz('That Allah rejoices, laughs, wonders and looks in al-Aqidah al-Wasitiyyah: why '
              'the joy at repentance is an attribute of perfection and not of need since He is '
              'not benefited by obedience, the reason in the hadith that both the killer and his '
              'victim enter the Garden and why laughter is the fitting response to what causes '
              'wonder, and the two kinds of ajab with al-qunut and qurb ghiyarihi')
b += B.further()
b += B.nav('was-l23-nuzul.html', 'The Divine Descent',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l24')

io.open(os.path.join(B.AQ, 'was-l24-farah-dahik-ajab.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'الفَرَحُ وَالضَّحِكُ وَالعَجَبُ وَالنَّظَر',
    'That Allah Rejoices, Laughs, Wonders and Looks',
    'Lesson 24 of al-ʿAqīdah al-Wāsiṭiyyah: why the joy at a '
    'servant’s repentance is an attribute of perfection and not of need, the reason the '
    'ḥadīth itself gives that a killer and his victim both enter the Garden, and the two '
    'kinds of wonder — with al-qunūṭ and the nearness of the change.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الرَّابِعُ وَالعِشْرُون', '3',
           'الفَرَحُ وَالضَّحِكُ وَالعَجَبُ وَالنَّظَر',
           'That Allah Rejoices, Laughs, Wonders and Looks', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l24-farah-dahik-ajab.html')
