# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 7 — النَّاقِضُ الرَّابِع, part 3: المُضْطَرّ, الرِّضَا, التَّشْرِيع.

Printed folios 132-135 (PDF indices 129-132, offset +3). This closes the
fourth nullifier, which ran 28 folios across three lessons. The book sets its
own headings here, and the lesson follows them:

  * «حُكْمُ المُضْطَرِّ لِلتَّحَاكُمِ إِلَى القَانُون» — a fatwa, and the only
    place in the whole clause where the answer is «لَا يَكُونُ كَافِرًا» about
    a man who does litigate before such a court. With three limits attached in
    the same breath: only at ضَرُورَة, only where he cannot reach his right
    otherwise, and he may not take what the Sharīʿah does not make lawful.
  * «حُكْمُ مَنْ لَمْ يَرْضَ بِحُكْمِ الرَّسُولِ ﷺ» — the story of ʿUmar
    killing the man who refused arbitration. Ibn Bāz does **not** authenticate
    it: «وَفِي القِصَّتَيْنِ نَظَر» — and then «فَالمَعْنَى صَحِيحٌ مِنْ حَيْثُ
    المَعْنَى», with Muḥammad 47:9 as the actual proof. The page keeps both
    halves, because taking the second without the first is how a weak story
    becomes a daleel.
  * The compiler's text-critical warning: one printed edition of Ibn Bāz's
    «شَرْحُ كِتَابِ التَّوْحِيد» (Dār al-Ḍiyāʾ, taḥqīq al-ʿAlāwī) carries a
    sentence not found in the recording the editors relied on, and that edition
    «فِيهَا نَقْصٌ وَتَحْرِيفٌ فِي الأَلْفَاظ» and should not be relied upon.
    That belongs on the page: it is the same discipline as a ḥadīth grading,
    applied to a modern print.
  * Two incidents he reads as munāfiq speech — the man who turned away angry
    («لَعَمْرِي إِنَّكَ لَتُعْطِي مَنْ شِئْت»), which Ibn Bāz explains as
    accusing the Prophet ﷺ of not being truthful; and the Ḥunayn remark «مَا
    أَرَادَ بِهَا وَجْهَ الله» — «هَذَا مِنَ المُنَافِقِين». And the تَعْزِيَة
    he draws out of the first for anyone who meets ingratitude.
  * تَوْحِيدُ الحُكْم with its verses, and then التَّشْرِيع: governments have
    no legislative authority; الشَّارِع is applied to Allah and, by His
    command, to His Messenger, **but is not among Allah's names**; «النَّاسُ
    لَا يُشَرِّعُون»; and no man is to be named مَلِكُ المُلُوك / حَاكِمُ
    الحُكَّام / سُلْطَانُ السَّلَاطِين.
  * The مُبَلِّغ principle, which is how the Messenger ﷺ can be called
    مُشَرِّع without the tawḥīd being touched — argued from three ḥadīth
    wordings: Ibrāhīm «حَرَّمَ» Makkah, «إِنَّ اللهَ وَرَسُولَهُ حَرَّمَ بَيْعَ
    الخَمْر» (singular verb), and Anas's «يَنْهَيَانِكُم».

Rule 8: the sharḥ gives «حَرَّمَهَا اللهُ... وَلَمْ يُحَرِّمْهَا النَّاس» as
رَوَاهُ الشَّيْخَان and Anas's ḥadīth as فِي الصَّحِيحَيْن — those are reported
as the sharḥ reports them. The «لَا أَجِدُ مَا أُعْطِيك» ḥadīth and the Ḥunayn
ḥadīth are quoted here with **no** grading at this place, so the page says so
and supplies none.
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


def qa(q, a):
    return ('<div style="margin:0 0 .6rem;padding-right:.8rem;'
            'border-right:2px solid var(--line)">'
            '<p style="margin:0 0 .25rem;font-size:.88rem;color:var(--ink-light)">'
            '<strong>Q —</strong> <em>%s</em></p>'
            '<p style="margin:0;font-size:.93rem"><strong>Ibn Bāz —</strong> %s</p>'
            '</div>' % (q, a))


b = B.objectives([
    'State the ruling on a man who <strong>cannot reach his right</strong> '
    'except by litigating before a court that judges by man-made codes — and '
    'the <strong>three limits</strong> attached to it in the same answer.',
    'Quote Ibn Bāz’s two sentences on the story of ʿUmar — %s and %s — and say '
    'what each one does.'
    % ('«' + ar('وَفِي القِصَّتَيْنِ نَظَر') + '»',
       '«' + ar('فَالمَعْنَى صَحِيحٌ مِنْ حَيْثُ المَعْنَى') + '»'),
    'Give the verse that actually carries the ruling on one who '
    '<strong>hates</strong> what Allah sent down.',
    'Say why the compiler warns against one printed edition of %s.'
    % ar('شَرْحُ كِتَابِ التَّوْحِيد'),
    'Explain what Ibn Bāz says the words %s amounted to, and why he reads them '
    'as the speech of the munāfiqūn.'
    % ('«' + ar('إِنَّكَ لَتُعْطِي مَنْ شِئْت') + '»'),
    'State what %s is and is not: who has it, and whether %s is a name of '
    'Allah.' % (ar('التَّشْرِيع'), ar('الشَّارِع')),
    'Use the principle %s to explain how the Messenger ﷺ can be called a '
    'legislator without the tawḥīd being touched.' % ar('الرَّسُولُ مُبَلِّغ'),
])

b += B.provenance(132, 135)

b += B.matn(
    'الرَّابِع: مَنِ اعْتَقَدَ أَنَّ غَيْرَ هُدَى النَّبِيِّ ﷺ أَكْمَلُ مِنْ '
    'هُدَاه، أَوْ أَنَّ حُكْمَ غَيْرِهِ أَحْسَنُ مِنْ حُكْمِه — '
    'كَالَّذِينَ يُفَضِّلُونَ حُكْمَ الطَّوَاغِيتِ عَلَى حُكْمِه — '
    'فَهُوَ كَافِرٌ.',
    'The clause itself, for the third and last time. Part 1 established the '
    'ruling, part 2 gave the تَفْصِيل that governs how it is applied, and these '
    'four folios close it with three narrower questions the book heads itself.')

b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><strong>Four folios, three '
        'headings, and the book sets them.</strong> This lesson follows the '
        'source’s own order rather than imposing one: '
        '<em>the man under compulsion</em>, <em>the man who is not pleased with '
        'the ruling of the Messenger ﷺ</em>, and <em>legislation</em>.</p>'
        '<p style="margin:0;font-size:.92rem">Read in that order they do '
        'something deliberate. The clause began at its most severe, spent twelve '
        'folios on restraint, and <strong>ends by naming the one man it does not '
        'reach at all</strong> — and then returns the whole subject to where it '
        'started, which is not politics but tawḥīd.</p>',
        wash='var(--accent-wash)', edge='var(--accent)'))

# ---------------------------------------------------------------- al-mudtarr
b += B.heading('حُكْمُ المُضْطَرِّ لِلتَّحَاكُمِ إِلَى القَانُون',
               'The Man Who Cannot Reach His Right Any Other Way')
b += B.prose(
    'The question put to him is specific, and it is the ordinary situation of '
    'most Muslims on earth: <em>a man has a right — a debt owed him, a property '
    'taken from him — and the only court that will hear him judges by a '
    'man-made code. He cannot reach his right unless he goes to it. Is he a '
    'disbeliever?</em>')
b += B.sharh(
    box('<p style="margin:0;font-size:.95rem"><em>«So I refer to your request '
        'for a fatwā… in which you ask about the ruling on one who refers his '
        'case to one who judges by man-made codes, <strong>and who cannot reach '
        'his right unless he refers it to them</strong> — is he a disbeliever? '
        'And I inform you that <strong>if he is compelled to that, he is not a '
        'disbeliever.</strong> But it is not for him to refer his case to them '
        '<strong>except at the point of necessity</strong>, when obtaining his '
        'right is not made possible for him except by that; and '
        '<strong>it is not for him to take other than what the purified '
        'Sharīʿah makes lawful</strong>. May Allah grant all of us '
        'success.»</em></p>'))
b += B.prose(
    '<strong>That is the whole answer, and notice how much of it is '
    'condition.</strong> One sentence relieves him; three qualify it. The relief '
    'is for the man who is <em>compelled</em> — not for the man who finds that '
    'court convenient, and not for the man who prefers it, who is the subject of '
    'the clause in the first place.')
b += B.sharh(table([
    row('the ruling', 'He is <strong>not</strong> a disbeliever — '
        '%s.' % ('«' + ar('لَا يَكُونُ كَافِرًا') + '»')),
    row('limit ١', 'Only <strong>at necessity</strong> — '
        '%s. Not as a first resort and not as a preference.'
        % ('«' + ar('إِلَّا عِنْدَ الضَّرُورَة') + '»')),
    row('limit ٢', 'Only where <strong>obtaining his right is not possible '
        'otherwise</strong> — if another route exists, the necessity does not.'),
    row('limit ٣', 'He may <strong>not take</strong> what the Sharīʿah does not '
        'make lawful for him. <em>The court’s permission is not a title.</em> '
        'If it awards him ribā, or a share the Sharīʿah does not give him, the '
        'necessity that let him enter does not let him collect.'),
]) + p('<strong>Limit ٣ is the one that is usually dropped</strong>, and it is '
       'the one that keeps the answer honest. A man may go in to recover what is '
       'his. He does not come out with more than his.'))

# ---------------------------------------------------------------- al-rida
b += B.heading('حُكْمُ مَنْ لَمْ يَرْضَ بِحُكْمِ الرَّسُولِ ﷺ',
               'Not Being Pleased With His Ruling')
b += B.prose(
    'The second heading is where this clause meets the heart. The sharḥ brings '
    'it through a story — <em>ʿUmar killing a man who refused arbitration before '
    'the Prophet ﷺ</em> — and what Ibn Bāz does with that story is the most '
    'instructive thing on these four folios.')
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><em>«And in the two '
        'stories <strong>there is something to be examined</strong> — but they '
        'are two witnesses to the deed of the munāfiqūn… and for this reason, in '
        'this narration from ʿUmar, he rebuked this man who sought arbitration '
        'before other than the Prophet ﷺ, and held that he had '
        '<strong>apostatised</strong> by that, and for this he killed him. '
        '<strong>So the meaning is sound from the standpoint of the '
        'meaning</strong> — for whoever is not pleased with the ruling of the '
        'Messenger of Allah ﷺ is a disbeliever. So what is obligatory is '
        '<strong>contentment</strong> with the law of Allah and contentment with '
        'the ruling of Allah. And whoever <strong>hates</strong> the ruling of '
        'Allah is a disbeliever.»</em></p>'
        '<p style="margin:0;font-size:.92rem">Then the verse.</p>'))
b += B.ayah(
    'ذَٰلِكَ بِأَنَّهُمْ كَرِهُوا مَا أَنزَلَ اللَّهُ فَأَحْبَطَ أَعْمَالَهُمْ',
    'That is because they hated what Allah sent down, so He rendered their '
    'deeds worthless.',
    'سُورَةُ مُحَمَّد · 47:9')
b += B.prose(
    '<strong>Read the two sentences in order, because the order is the '
    'lesson.</strong> He says the story has <em>something in it to be '
    'examined</em> — %s — and <em>then</em> he says the meaning is sound. '
    '<em>The ruling is not resting on the story. It is resting on the verse, '
    'and the story is brought as an illustration of what the munāfiqūn '
    'did.</em>'
    % ('«' + ar('وَفِي القِصَّتَيْنِ نَظَر') + '»'))
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><strong>This is worth taking as a '
        'habit, not just a datum.</strong> A weak or questioned report that '
        'illustrates a ruling established elsewhere is used as an illustration. '
        'It does not become the proof. <em>Quoting «the meaning is sound» while '
        'dropping «there is something to be examined in it» turns a shaykh’s '
        'careful sentence into a licence he did not give</em> — and this clause, '
        'of all the ten, is the one where that is done most often.</p>',
        wash='var(--accent-wash)', edge='var(--accent)'))
b += B.sharh(
    p('<strong>And the compiler attaches a warning here that belongs on this '
      'page.</strong> One printed edition of Ibn Bāz’s '
      '<em>%s</em> — the Dār al-Ḍiyāʾ print, with the taḥqīq of al-ʿAlāwī — '
      'carries at this place the sentence <em>«and the story of ʿUmar '
      'demonstrates that referring judgement to other than the law of Allah is '
      'disbelief and apostasy»</em>. The compiler says plainly: '
      '<em>«I did not find this quotation in the recorded lecture that they '
      'relied upon in printing the sharḥ; and in any case '
      '<strong>this edition has deficiency and distortion in the wordings</strong>, '
      'and perhaps in the meanings also, <strong>so it ought not to be relied '
      'upon</strong>.»</em>' % ar('شَرْحُ كِتَابِ التَّوْحِيد')) +
    p('<em>A sentence that strong, attributed to Ibn Bāz, on this clause of all '
      'clauses — and the book’s own compiler says the edition carrying it is '
      'unreliable and the recording does not have it.</em> '
      '<strong>This is the discipline of ḥadīth applied to a modern print,</strong> '
      'and it is why the pages of this site name their folios.'))

# ---------------------------------------------------------------- munafiq speech
b += B.heading('كَلَامُ المُنَافِقِينَ عِنْدَ القَسْم',
               'Two Remarks, and What They Really Said')
b += B.prose(
    'Having said the stories are <em>witnesses to the deed of the munāfiqūn</em>, '
    'the sharḥ gives two incidents of exactly that kind. Both are about '
    'distribution of wealth, and in both the words sound like complaint until '
    'Ibn Bāz unpacks what they assert.')
b += B.hadith(
    'فَوَجَدْتُ عِنْدَهُ رَجُلًا يَسْأَلُهُ وَرَسُولُ اللهِ ﷺ يَقُول: '
    '«لَا أَجِدُ مَا أُعْطِيك»، فَتَوَلَّى الرَّجُلُ عَنْهُ وَهُوَ مُغْضَبٌ '
    'وَهُوَ يَقُول: لَعَمْرِي إِنَّكَ لَتُعْطِي مَنْ شِئْت. '
    'فَقَالَ رَسُولُ اللهِ ﷺ: «يَغْضَبُ عَلَيَّ أَنْ لَا أَجِدَ مَا '
    'أُعْطِيَه!»',
    '“I found with him a man asking him, and the Messenger of Allah ﷺ was '
    'saying, ‘I do not have anything to give you.’ So the man turned away from '
    'him angry, saying: by my life, you give to whomever you wish! And the '
    'Messenger of Allah ﷺ said: ‘He is angry with me that I do not have '
    'anything to give him!’”',
    'يُفَسِّرُهُ الشَّيْخُ فِي شَرْحِ سُنَنِ أَبِي دَاوُد · '
    'the sharḥ gives no grading at this place, so none is supplied here')
b += B.sharh(
    p('Ibn Bāz’s reading of it: <em>«this shows that <strong>some</strong> '
      'people, in most cases, if they are not given what they want, will speak '
      '— even if the one withholding is the Messenger of Allah ﷺ.»</em> Then he '
      'takes the man’s actual sentence apart:') +
    box('<p style="margin:0;font-size:.94rem"><em>«Look at this man saying '
        '<strong>“you give to whomever you wish”</strong> — after the Prophet ﷺ '
        'had excused himself to him. Its meaning is: '
        '<strong>you are not truthful.</strong> You give to whom you wish — but '
        'not because of a lack of what to give; rather you give to whom you wish '
        'and leave whom you wish. Its meaning is '
        '<strong>accusing the Prophet ﷺ of not being truthful in his saying that '
        'he does not have what to give him</strong>; '
        '<strong>and nobody says this but a hypocrite</strong>, of the people of '
        'hypocrisy well known in Madīnah.»</em></p>') +
    p('<strong>That is the move worth learning.</strong> The surface of the '
      'sentence is a grievance about money. Its content is '
      '<em>a denial of the Prophet’s ﷺ truthfulness</em> — and that, not the '
      'anger, is what the ruling attaches to. <em>The same clause runs through '
      'the whole nullifier: what is being asserted, not how loudly.</em>'))
b += B.hadith(
    'لَمَّا قَسَمَ النَّبِيُّ ﷺ قِسْمَةَ حُنَيْنٍ قَالَ رَجُلٌ مِنَ '
    'الأَنْصَار: مَا أَرَادَ بِهَا وَجْهَ اللهِ.',
    '“When the Prophet ﷺ made the division of Ḥunayn, a man from the Anṣār '
    'said: he did not intend the Face of Allah by it.”',
    'حَدِيثُ أَبِي وَائِلٍ عَنْ عَبْدِ اللهِ · '
    'the sharḥ quotes it here without a grading, and none is supplied here')
b += B.sharh(
    p('Ibn Bāz on it, in four words: <em>«%s»</em> — '
      '<strong>“this is from the munāfiqūn.”</strong>'
      % ar('هَذَا مِنَ المُنَافِقِين')) +
    p('<em>And the reason is the same as the first.</em> To say of the '
      'Prophet ﷺ <strong>«he did not intend the Face of Allah by it»</strong> is '
      'not a complaint about a share. It is a verdict passed on his intention — '
      'which is the one thing no created person may pass a verdict on, and the '
      'thing the munāfiqūn of Madīnah were marked by.'))
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><strong>And he draws something out '
        'of the first incident that has nothing to do with takfīr at all.</strong> '
        '<em>«The intent is that in this there is a '
        '<strong>consolation</strong> for one who sees in the state of people '
        'what he sees — of their agitation, and their greed, and their failure '
        'to excuse the one who excuses himself to them.»</em></p>'
        '<p style="margin:.5rem 0 0;font-size:.92rem">A man was ungrateful to '
        'the Messenger of Allah ﷺ <em>to his face, over nothing</em>. '
        'So if you are treated that way, you are not seeing something new under '
        'the sun. <em>That is a ʿaqīdah book handing you something to live '
        'with.</em></p>'))

# ---------------------------------------------------------------- tawhid al-hukm
b += B.heading('تَوْحِيدُ الحُكْم', 'Ruling Belongs to Him As Worship Does')
b += B.prose(
    'Then the sharḥ returns the whole subject to where the matn put it. Not to '
    'constitutions — to tawḥīd. And it does so with a sentence that puts worship '
    'and ruling in one breath.')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><em>«So the intent is: '
        'there is no avoiding the tawḥīd of Allah, by singling Him out for '
        'worship and disowning the worship of other than Him and those who '
        'worship other than Him; and there is no avoiding the belief that shirk '
        'is false, and that it is obligatory upon all the slaves, of jinn and '
        'men, <strong>to devote worship to Allah alone, and to discharge the '
        'right of this tawḥīd by referring judgement to the law of '
        'Allah</strong> — for Allah is the Ruler; and of His tawḥīd is faith and '
        'affirmation of that. <strong>He is the Ruler in this world by His '
        'Sharīʿah, and in the Hereafter by Himself.</strong>»</em></p>') +
    p('And the explicit parallel: <em>«just as worship is for Allah alone, '
      '<strong>likewise ruling is His alone</strong>.»</em>'))
b += B.prose(
    'The verses he cites, in his order. The first is the clause he repeats most '
    '— %s, from al-Anʿām 6:57 and from Yūsuf 12:40 and 12:67, which is why he '
    'gives three references for one sentence.'
    % ('«' + ar('إِنِ الْحُكْمُ إِلَّا لِلَّهِ') + '»'))
b += B.ayah(
    'فَالْحُكْمُ لِلَّهِ الْعَلِيِّ الْكَبِيرِ',
    'So judgement belongs to Allah, the Most High, the Most Great.',
    'سُورَةُ غَافِر · 40:12')
b += B.ayah(
    'وَمَا اخْتَلَفْتُمْ فِيهِ مِن شَيْءٍ فَحُكْمُهُ إِلَى اللَّهِ',
    'And in whatever you differ, its judgement is referred to Allah.',
    'سُورَةُ الشُّورَى · 42:10')
b += B.prose(
    '<em>Keep the shape of the argument.</em> The matn’s clause was about a man '
    '<strong>preferring</strong> another guidance. The sharḥ closes by showing '
    '<strong>why</strong> that preference is a nullifier and not merely a sin: '
    'because ruling is an attribute singled out for Allah in the same way '
    'worship is, so granting it elsewhere is of the same kind as granting '
    'worship elsewhere. <em>That is the thread back to nullifiers one, two and '
    'three.</em>')

# ---------------------------------------------------------------- al-tashri
b += B.heading('التَّشْرِيع', 'Legislating, and Who Does It')
b += B.sharh(
    p('On governments, one sentence:') +
    box('<p style="margin:0;font-size:.95rem"><em>«<strong>They have no '
        'authority of legislation.</strong> Legislation belongs to Allah alone, '
        'in His Mighty Book, or His revelation to His Messenger ﷺ.»</em></p>') +
    p('And on people in general: <em>«<strong>%s</strong> — people do not '
      'legislate. The Legislator is Allah, by the hand of His Messenger '
      'Muḥammad ﷺ.»</em>'
      % ar('النَّاسُ لَا يُشَرِّعُون، المُشَرِّعُ هُوَ اللهُ عَلَى يَدِ '
           'رَسُولِهِ مُحَمَّدٍ ﷺ')))
b += B.sharh(
    p('<strong>Then a precision about the words themselves</strong>, which is '
      'the kind of thing this book is good at:') +
    box('<p style="margin:0;font-size:.94rem"><em>«%s and %s are applied to '
        'Allah — exalted is He — and to His Messenger ﷺ by the command of '
        'Allah; <strong>but the name %s is not among the names of Allah — '
        'exalted is He.</strong>»</em></p>'
        % (ar('الشَّارِع'), ar('المُشَرِّع'), ar('الشَّارِع'))) +
    p('<em>Two separate claims, and both matter.</em> The word may be '
      '<strong>used of</strong> Allah — we say «the Lawgiver» and mean Him. '
      'It is <strong>not one of His names</strong>, because His names are taken '
      'from revelation and not coined from His acts. <em>And the same word is '
      'used of the Messenger ﷺ — by Allah’s command, not in his own right, which '
      'is the point the next section settles.</em>'))
b += B.sharh(
    p('And one more, on titles:') +
    box('<p style="margin:0;font-size:.94rem"><em>«No one is to be named with '
        'anything that <strong>shares with the Lord in His greatness</strong> — '
        'such as %s, %s, %s and the like; because this is '
        '<strong>false and a lie</strong>, and because it is '
        '<strong>a defect in the tawḥīd and a defect in the īmān</strong>, and '
        'because that will lead to self-admiration, arrogance and '
        'self-aggrandisement.»</em></p>'
        % (ar('مَلِكُ المُلُوك'), ar('حَاكِمُ الحُكَّام'),
           ar('سُلْطَانُ السَّلَاطِين'))) +
    p('<em>Note the three reasons, because they are three different kinds of '
      'reason:</em> it is <strong>untrue</strong>; it <strong>damages the '
      'tawḥīd</strong>; and it <strong>harms the man himself</strong>. '
      'The clause that spent twenty-eight folios on the gravest political '
      'question in the book ends up objecting to a <em>business card</em> — and '
      'that is not a change of subject. It is the same tawḥīd, met at the scale '
      'where most people will actually meet it.'))
b += B.sharh(
    box('<p style="margin:0;font-size:.93rem"><strong>The compiler adds the '
        'consensus in his own words:</strong> <em>“The scholars are agreed that '
        'legislating for people is of the <strong>exclusive '
        'characteristics</strong> of Allah — exalted is He — and that Allah is '
        'the Legislator; and that whoever says ‘<strong>I</strong> am the '
        'legislator for people’, or ‘I contend with Allah in His legislation’, '
        'or legislates alongside Allah, or legislates what '
        '<strong>contradicts</strong> the law of Allah, '
        '<strong>has contended with Allah in an attribute He has singled '
        'Himself out by</strong>; and that what is obligatory is to single Him '
        'out in ruling and in legislation.”</em></p>'
        '<p style="margin:.5rem 0 0;font-size:.9rem;color:var(--ink-light)">'
        '<em>Read against part 2: this is the claim stated at its '
        'clearest — and part 2 is where you learn that establishing it of a '
        'particular man is «أَمْرٌ وَرَاءَ ذَلِك».</em></p>'))

# ---------------------------------------------------------------- muballigh
b += B.heading('وَالرَّسُولُ مُبَلِّغ', 'How the Messenger ﷺ Can Be Called a Legislator')
b += B.prose(
    'That precision leaves a question, and the sharḥ answers it with three '
    'ḥadīth wordings in a row. <em>If legislation is Allah’s alone, how does the '
    'Sharīʿah itself ascribe making-unlawful to the Messenger ﷺ?</em> The '
    'answer is one word: %s — <strong>he conveys</strong>.' % ar('مُبَلِّغ'))
b += B.sharh(
    qa('The ḥadīth «Ibrāhīm made Makkah inviolable, and I make Madīnah '
       'inviolable as Ibrāhīm made Makkah inviolable» — and here it is '
       '<strong>Allah</strong> who made it inviolable?',
       '<em>«Both of these came. <strong>Allah</strong> made it inviolable on '
       'the day He created the heavens and the earth; and <strong>Ibrāhīm</strong> '
       'made it inviolable when Allah sent him — meaning: he '
       '<strong>manifested</strong> its prohibition and <strong>clarified</strong> '
       'it. And conveying — it was manifested by the hand of the Prophet ﷺ, '
       'its prohibition; and he did not speak of his own accord: it is from the '
       'Lawgiver, and He made it inviolable by the knowledge of Allah and the '
       'law of Allah.»</em>'))
b += B.prose(
    'The questioner there had in mind the ḥadīth of Khuwaylid — '
    '<em>«Makkah: Allah made it inviolable… and the people did not make it '
    'inviolable»</em> — which the compiler attributes to '
    '<strong>al-Bukhārī and Muslim</strong>, and that attribution is given here '
    'as the sharḥ gives it.')
b += B.sharh(
    p('The second wording makes the grammar carry the doctrine:') +
    box('<p style="margin:0;font-size:.94rem">On the ḥadīth '
        '<em>«إِنَّ اللهَ وَرَسُولَهُ <strong>حَرَّمَ</strong> بَيْعَ '
        'الخَمْر»</em>: <em>«he used the verb in the '
        '<strong>singular</strong>, because the making-unlawful '
        '<strong>in reality</strong> belongs to Allah, and the Messenger is a '
        'conveyer. For this reason the singular verb <em>ḥarrama</em> came. And '
        'the commentator mentioned a narration with <strong>ḥarramā</strong> '
        '[dual] — and that is not to be denied either, because they are two: '
        'so <strong>Allah is the One who makes unlawful, and the Messenger is a '
        'conveyer</strong>.»</em></p>') +
    p('And the third, from the Ṣaḥīḥayn — <em>«Allah and His Messenger '
      '<strong>forbid you</strong> [dual] the flesh of domestic donkeys»</em>, '
      'the ḥadīth of Anas: <em>«so <strong>Allah</strong> is the One who '
      'forbids, and that is <strong>the foundation</strong>; and the Messenger '
      'is a conveyer.»</em> <em>The sharḥ places it %s, and that is how '
      'it is reported here.</em>' % ar('فِي الصَّحِيحَيْن')))
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><strong>So the dual and the '
        'singular are both correct, and they are correct for different '
        'reasons.</strong> The singular is correct because the origin of the '
        'ruling is one. The dual is correct because '
        '<em>«they are two»</em> — Allah ruling, and the Messenger ﷺ conveying '
        'that ruling, which is a real and obligatory role, not a nominal one. '
        '<em>Reject the dual and you have cut off obedience to the Messenger ﷺ; '
        'take the dual as partnership and you have cut into the tawḥīd. The '
        'word %s holds both.</em></p>' % ar('مُبَلِّغ'),
        wash='var(--accent-wash)', edge='var(--accent)'))

# ---------------------------------------------------------------- close
b += B.heading('خُلَاصَةُ النَّاقِضِ الرَّابِع', 'The Fourth Nullifier, Closed')
b += B.sharh(table([
    row('part 1 · ص ١٠٨–١١٩',
        'The ruling. The ijmāʿ is reported on the man who <strong>claims</strong> '
        'a superiority; تَوْحِيدُ الحُكْم; al-Tawbah 9:31 and the mechanism of '
        'obedience in making lawful and unlawful; and the three states — holding '
        'it better, holding it equal, or permitting it to replace the Sharīʿah '
        '<em>while privately granting Allah’s law is better</em>.'),
    row('part 2 · ص ١٢٠–١٣١',
        '%s. Greater and lesser ṭāghūt; istiḥlāl against the bribe and the '
        'kinship; Ibn ʿAbbās’s %s on 5:44; the six wordings of the one condition; '
        '%s; and who fights, which is a state and never a man.'
        % (ar('التَّفْصِيل'), '«' + ar('كُفْرٌ دُونَ كُفْر') + '»',
           '«' + ar('لَازِمُ الحُكْمِ لَيْسَ بِحُكْم') + '»')),
    row('part 3 · ص ١٣٢–١٣٥',
        'The man under <strong>compulsion</strong>, with his three limits; '
        'contentment with his ruling ﷺ, on the verse and not on the story; the '
        'munāfiq’s two remarks and what they asserted; and %s, closing on '
        '%s.' % (ar('التَّشْرِيع'), ar('وَالرَّسُولُ مُبَلِّغ'))),
]) + p('<strong>Twenty-eight folios, and the longest of the ten.</strong> '
       '<em>Of those, twelve established the ruling and sixteen governed its '
       'application.</em> If you remember the clause by its proportions you will '
       'remember it correctly.'))

b += B.vocab([
    ('المُضْطَرّ', 'al-muḍṭarr', 'the one compelled',
     'The man acting under ضَرُورَة — necessity. Here: one who cannot obtain his '
     'right except through a court judging by a man-made code. Ibn Bāz: '
     'لَا يَكُونُ كَافِرًا — with three limits attached.'),
    ('الضَّرُورَة', 'al-ḍarūrah', 'necessity',
     'The threshold, not the excuse. The relief runs only «عِنْدَ الضَّرُورَة» '
     'and only where the right cannot be obtained otherwise.'),
    ('الرِّضَا', 'al-riḍā', 'contentment',
     'What is obligatory toward the law of Allah — الرِّضَا بِشَرْعِ اللهِ. '
     'Its opposite, كَرَاهَة of what Allah sent down, is what al-Māʾidah’s '
     'sister verse Muḥammad 47:9 attaches the nullifying of deeds to.'),
    ('نَظَر', 'naẓar', 'something to be examined',
     'A scholar’s reservation about a report. «وَفِي القِصَّتَيْنِ نَظَر» — said '
     'of the story of ʿUmar, immediately before «the meaning is sound». '
     'Dropping the first half misquotes him.'),
    ('التَّحْرِيف', 'al-taḥrīf', 'distortion of wording',
     'What the compiler says the Dār al-Ḍiyāʾ edition of شَرْحُ كِتَابِ '
     'التَّوْحِيد has — نَقْصٌ وَتَحْرِيفٌ فِي الأَلْفَاظ — so it «ought not to '
     'be relied upon».'),
    ('التَّشْرِيع', 'al-tashrīʿ', 'legislating',
     'Laying down law. Allah’s alone, in His Book or His revelation to His '
     'Messenger ﷺ. Governments have «no authority» of it.'),
    ('المُشَرِّع', 'al-musharriʿ', 'the Legislator',
     'Applied to Allah, and to His Messenger ﷺ by Allah’s command — '
     'but الشَّارِع is NOT among the names of Allah.'),
    ('مُبَلِّغ', 'muballigh', 'a conveyer',
     'The Messenger’s ﷺ role in a ruling: real, obligatory, and not '
     'partnership. It is why «حَرَّمَ» in the singular and «حَرَّمَا» in the '
     'dual are both correct.'),
    ('الحِصْنُ الحَصِين', 'al-ḥiṣn al-ḥaṣīn', 'the impregnable fortress',
     'Ibn Bāz on تَحْكِيمُ الشَّرِيعَة: «the impregnable fortress and the '
     'ample coat of mail — for protecting mankind, delivering rights, deterring '
     'oppression and putting an end to the corrupters».'),
])

b += B.mcq('nq-l07-mcq', [
    ('A man cannot obtain his right except by litigating before a court that '
     'judges by a man-made code. What did Ibn Bāz answer?',
     ['He is a disbeliever',
      'If he is compelled to that, he is not a disbeliever — but only at the '
      'point of necessity, only where he cannot obtain his right otherwise, and '
      'he may not take what the Sharīʿah does not make lawful for him',
      'He must abandon the right entirely',
      'The question is one of ijtihād with no answer'], 1),
    ('Which of the three limits is most often dropped when this fatwā is quoted?',
     ['That it applies only to debts',
      'That he may not take other than what the purified Sharīʿah makes lawful — '
      'the court’s permission is not a title',
      'That he must inform the scholars first',
      'That it applies only to a Muslim land'], 1),
    ('What did Ibn Bāz say about the story of ʿUmar killing the man who refused '
     'arbitration?',
     ['That it is authentic without question',
      '«وَفِي القِصَّتَيْنِ نَظَر» — there is something in the two stories to be '
      'examined — and then that the meaning is sound from the standpoint of the '
      'meaning',
      'That it is a fabrication with no basis',
      'That it is the primary proof of the clause'], 1),
    ('So what is the ruling actually resting on?',
     ['The story',
      'The verse — «ذَلِكَ بِأَنَّهُمْ كَرِهُوا مَا أَنْزَلَ اللهُ فَأَحْبَطَ '
      'أَعْمَالَهُمْ», Muḥammad 47:9 — with the story brought as an illustration '
      'of the deed of the munāfiqūn',
      'The consensus of the people of Madīnah',
      'ʿUmar’s ijtihād alone'], 1),
    ('Which verse does the sharḥ give for one who HATES what Allah sent down?',
     ['al-Māʾidah 5:44', 'Muḥammad 47:9', 'al-Nisāʾ 4:65', 'al-Shūrā 42:10'], 1),
    ('Why does the compiler warn against the Dār al-Ḍiyāʾ edition of Ibn Bāz’s '
     '«شَرْحُ كِتَابِ التَّوْحِيد»?',
     ['Because its attribution to Ibn Bāz is denied',
      'Because it carries at this place a sentence he did not find in the '
      'recorded lecture the editors relied upon, and the edition has deficiency '
      'and distortion in the wordings — «so it ought not to be relied upon»',
      'Because it is incomplete',
      'Because its taḥqīq is anonymous'], 1),
    ('What is the discipline being applied in that warning?',
     ['Fiqh of transactions',
      'The discipline of ḥadīth criticism applied to a modern printed edition — '
      'a strong sentence is not accepted merely because a print carries it',
      'Grammatical analysis',
      'Legal codification'], 1),
    ('The man said «by my life, you give to whomever you wish». What did Ibn '
     'Bāz say its meaning was?',
     ['A request for more',
      '«Its meaning is: you are not truthful» — accusing the Prophet ﷺ of not '
      'being truthful in saying he had nothing to give; and nobody says this but '
      'a hypocrite',
      'A complaint about the Anṣār',
      'An expression of poverty'], 1),
    ('Which part of that incident does the ruling attach to?',
     ['The man’s anger',
      'What his words ASSERTED — a denial of the Prophet’s ﷺ truthfulness',
      'His turning away',
      'His oath «by my life»'], 1),
    ('What did Ibn Bāz draw out of that incident that has nothing to do with '
     'takfīr?',
     ['A ruling on charity',
      'A consolation — «for one who sees in the state of people… their '
      'agitation, their greed, and their failure to excuse the one who excuses '
      'himself to them»',
      'A rule about asking',
      'A grading of the report'], 1),
    ('Of the Anṣārī’s remark at the division of Ḥunayn — «he did not intend the '
     'Face of Allah by it» — Ibn Bāz said:',
     ['«This is ijtihād»',
      '«This is from the munāfiqūn»',
      '«This is a slip of the tongue»',
      '«This requires investigation»'], 1),
    ('Why is that remark of a different order from a complaint about a share?',
     ['Because it was said publicly',
      'Because it passes a verdict on the Prophet’s ﷺ INTENTION — which no '
      'created person may do',
      'Because it concerned war spoils',
      'Because it was said by an Anṣārī'], 1),
    ('What does Ibn Bāz call تَحْكِيمُ الشَّرِيعَة?',
     ['A political preference',
      '«The impregnable fortress and the ample coat of mail — for protecting '
      'mankind, delivering rights, deterring oppression and putting an end to '
      'the corrupters»',
      'A matter of ijtihād',
      'A later development'], 1),
    ('How does the sharḥ tie ruling to worship?',
     ['By analogy with prayer times',
      '«Just as worship is for Allah alone, likewise ruling is His alone» — and '
      'discharging the right of tawḥīd includes referring judgement to the law '
      'of Allah',
      'By the rules of inheritance',
      'By the obligation of obedience to rulers'], 1),
    ('«He is the Ruler in this world by His Sharīʿah, and in the Hereafter…»',
     ['by His angels', 'by Himself', 'by His prophets', 'by the scales'], 1),
    ('Which clause does the sharḥ cite from three places — al-Anʿām 6:57 and '
     'Yūsuf 12:40 and 12:67?',
     ['«وَمَا اخْتَلَفْتُمْ فِيهِ مِنْ شَيْءٍ»',
      '«إِنِ الْحُكْمُ إِلَّا لِلَّهِ»',
      '«فَالْحُكْمُ لِلَّهِ الْعَلِيِّ الْكَبِيرِ»',
      '«أَلَا لَهُ الْخَلْقُ وَالْأَمْرُ»'], 1),
    ('What did Ibn Bāz say about governments and legislation?',
     ['That they legislate within limits set by scholars',
      '«They have no authority of legislation» — legislation belongs to Allah '
      'alone, in His Book or His revelation to His Messenger ﷺ',
      'That they may legislate in worldly matters only',
      'That the question is new and unanswered'], 1),
    ('Is الشَّارِع a name of Allah?',
     ['Yes, it is among the ninety-nine',
      'No — the word is APPLIED to Allah, and to His Messenger ﷺ by Allah’s '
      'command, but it is not among the names of Allah',
      'Yes, by consensus',
      'Only in the language of the jurists'], 1),
    ('Why is a man not to be called مَلِكُ المُلُوك or حَاكِمُ الحُكَّام?',
     ['Because the titles are foreign',
      'Three reasons: it is false and a lie; it is a defect in the tawḥīd and in '
      'the īmān; and it leads to self-admiration, arrogance and '
      'self-aggrandisement',
      'Because they were used by the Persians',
      'Because they belong to the Prophet ﷺ alone'], 1),
    ('In the compiler’s statement of the consensus, what is the act described as?',
     ['A sin of the branches',
      'Contending with Allah in an attribute He has singled Himself out by',
      'An error of ijtihād',
      'A matter of disputed wording'], 1),
    ('How does the sharḥ reconcile «Ibrāhīm made Makkah inviolable» with Allah '
     'having made it inviolable?',
     ['One of the two reports is weak',
      'Both came: Allah made it inviolable the day He created the heavens and '
      'the earth; Ibrāhīm «made it inviolable» means he MANIFESTED and clarified '
      'its prohibition — conveying',
      'Ibrāhīm legislated it independently',
      'The prohibition was renewed twice'], 1),
    ('Why is the verb singular in «إِنَّ اللهَ وَرَسُولَهُ حَرَّمَ بَيْعَ '
     'الخَمْر»?',
     ['A copyist’s error',
      'Because the making-unlawful in reality belongs to Allah, and the '
      'Messenger is a conveyer',
      'Because wine is a single subject',
      'Because the dual is not used in ḥadīth'], 1),
    ('And the narration with the dual «حَرَّمَا»?',
     ['It is rejected',
      'It is «not to be denied either, because they are two» — Allah making '
      'unlawful, and the Messenger ﷺ conveying',
      'It is a weak narration',
      'It belongs to a different ḥadīth'], 1),
    ('What does the word مُبَلِّغ protect on both sides?',
     ['Only the tawḥīd',
      'Both: reject the dual and you cut off obedience to the Messenger ﷺ; take '
      'the dual as partnership and you cut into the tawḥīd',
      'Only obedience to the Messenger ﷺ',
      'Neither — it is a grammatical term only'], 1),
    ('Across the whole fourth nullifier, how are the twenty-eight folios '
     'divided?',
     ['Evenly between ruling and application',
      'Twelve establish the ruling; sixteen govern its application',
      'Twenty on the ruling; eight on application',
      'All twenty-eight on the ruling'], 1),
])

b += B.tf('nq-l07-tf', [
    ('المُضْطَرُّ الَّذِي لَا يَصِلُ إِلَى حَقِّهِ إِلَّا بِالتَّحَاكُمِ '
     'إِلَى القَانُونِ كَافِرٌ عِنْدَ ابْنِ بَاز.',
     'For Ibn Bāz, one compelled to litigate under a man-made code to reach his '
     'right is a disbeliever.', False),
    ('لَيْسَ لِلْمُضْطَرِّ أَنْ يَأْخُذَ خِلَافَ مَا يُحِلُّهُ الشَّرْع.',
     'The one compelled may not take other than what the Sharīʿah makes lawful.',
     True),
    ('قَالَ ابْنُ بَازٍ فِي قِصَّةِ عُمَرَ: «وَفِي القِصَّتَيْنِ نَظَر».',
     'Ibn Bāz said of the story of ʿUmar: «in the two stories there is something '
     'to be examined».', True),
    ('اعْتَمَدَ المُؤَلِّفُ طَبْعَةَ دَارِ الضِّيَاءِ لِشَرْحِ كِتَابِ '
     'التَّوْحِيد.',
     'The compiler relies on the Dār al-Ḍiyāʾ edition of Sharḥ Kitāb al-Tawḥīd.',
     False),
    ('الشَّارِعُ مِنْ أَسْمَاءِ اللهِ تَعَالَى.',
     '«al-Shāriʿ» is among the names of Allah.', False),
    ('الحُكْمُ لِلَّهِ وَحْدَهُ كَمَا أَنَّ العِبَادَةَ لَهُ وَحْدَه.',
     'Ruling is His alone, just as worship is His alone.', True),
    ('إِفْرَادُ الفِعْلِ فِي «حَرَّمَ» دَلِيلٌ عَلَى أَنَّ الرَّسُولَ ﷺ '
     'لَيْسَ لَهُ فِي التَّبْلِيغِ شَأْن.',
     'The singular verb in «ḥarrama» shows the Messenger ﷺ has no role in '
     'conveying.', False),
])

b += B.memorize(
    'النَّاسُ لَا يُشَرِّعُون، المُشَرِّعُ هُوَ اللهُ عَلَى يَدِ رَسُولِهِ '
    'مُحَمَّدٍ ﷺ',
    'Ibn Bāz. <strong>The whole fourth nullifier in one sentence</strong>, and '
    'both of its halves are in it. <em>«People do not legislate»</em> is the '
    'ruling that part 1 established. <em>«by the hand of His Messenger '
    'Muḥammad ﷺ»</em> is %s — the reason the Messenger’s ﷺ share in it takes '
    'nothing from Allah. <em>And beside it keep the sentence that governs how '
    'any of this is applied to a particular man, from part 2: '
    '«لَكِنَّ الحُكْمَ بِالرِّدَّةِ أَمْرٌ وَرَاءَ ذَلِكَ.»</em>'
    % ar('مُبَلِّغ'))

b += B.nav('nq-l06-tafsil-al-hukm.html',
           'النَّاقِضُ الرَّابِع · part 2',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l07')

B.write('nq-l07-mudtarr-wa-tashri.html',
        'النَّاقِضُ الرَّابِع · المُضْطَرُّ وَالتَّشْرِيع',
        'The Fourth Nullifier, Part 3 — Necessity, Contentment, Legislation',
        'The close of the fourth nullifier, from the words of Shaykh Ibn Bāz: the '
        'man who cannot reach his right except through a court judging by '
        'man-made codes, and the three limits on the relief given him; '
        'contentment with the ruling of the Messenger ﷺ, resting on Muḥammad 47:9 '
        'and not on the questioned story of ʿUmar; the compiler’s warning against '
        'a printed edition carrying a sentence absent from the recording; what '
        'the munāfiq’s two remarks actually asserted; tawḥīd al-ḥukm with its '
        'verses; al-tashrīʿ, and that al-Shāriʿ is not among the names of Allah; '
        'and «the Messenger is a conveyer» as the reconciliation.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ السَّابِع', '6', b)
print('wrote nq-l07-mudtarr-wa-tashri.html')
