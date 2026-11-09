# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 13 — النَّاقِضُ السَّابِع, part 3: العِلَاجُ وَالنُّشْرَة.

Printed folios 179-193 (PDF indices 176-190, offset +3). This closes the
seventh nullifier — 35 folios, the longest clause in the book. Nullifier 8
(مظاهرة المشركين) begins at index 191 → printed 194.

Three things make these folios the most useful in the clause:

  * **The six شُبُهَات against the ḥadīth of the Prophet ﷺ being bewitched,
    answered one by one.** This is the best sustained apologetics in the book:
    the false claim that Hishām ibn ʿUrwah was mukhtaliṭ (al-Dhahabī: «لَمْ
    يَخْتَلِطْ أَبَدًا، وَلَا عِبْرَةَ بِمَا قَالَهُ أَبُو الحَسَنِ بْنُ
    القَطَّان»), the «khabar āḥād is not taken in ʿaqīdah» claim (itself named a
    bidʿah — and anyway this is of the **فروع** of belief, not the أصول), the
    «he only attempted it» claim, the objection from «وَاللهُ يَعْصِمُكَ مِنَ
    النَّاس», the objection from «رَجُلًا مَسْحُورًا», and the objection that
    it would destroy trust in the message.
  * **The ضَرُورَة argument demolished.** «العِلَاجُ مَا هُوَ بِضَرُورَة،
    العِلَاجُ سُنَّة» — with Ibn Taymiyyah's five reasons that treatment is not
    a necessity at all, the Lajnah on the condition inside «الضَّرُورَاتُ
    تُبِيحُ المَحْظُورَات», and Muḥammad ibn Ibrāhīm's «أَفَيُعْمَلُ الكُفْرُ
    لِتَحْيَا نُفُوسٌ مَرِيضَة؟»
  * **And the pastoral half, which is why this page is not only polemic**:
    recitation does not guarantee healing; «وَلَوْ كَانَ كُلُّ مَرِيضٍ يُشْفَى
    بِالرُّقْيَةِ أَوِ الدَّوَاءِ لَمْ يَمُتْ أَحَد» — and the proof is the
    Prophet ﷺ himself, over whose hands ʿĀʾishah recited the three sūrahs in
    his final illness, and he died of it, «لِأَنَّ اللهَ سُبْحَانَهُ لَمْ
    يُرِدْ شِفَاءَهُ مِنْ ذَلِكَ المَرَض». Plus Ibn Bāz's observation that much
    of what people call magic is «وَسَاوِسُ وَأَشْيَاءُ تَخَيَّلَهَا مَا هِيَ
    بِصَحِيحَة».

Also: compelling the magician to undo it before he is executed, with Ḥafṣah's
athar and the **governance** detail that ʿUthmān was angered by her acting
without his command; the ʿĀʾishah «أَفَلَا تَنَشَّرْت» objection and the
finding that the word is **مُدْرَجَة from Ibn ʿUyaynah**; the bewitched against
the insane; that no one is burned with fire; and Hārūt and Mārūt, where Ibn Bāz
refuses the whole corpus of al-Zuhrah stories — «فَلَا يُعَوَّلُ عَلَيْهَا،
وَإِنَّمَا يُعَوَّلُ عَلَى نَصِّ الكِتَابِ العَزِيز» — and then says what the
story would teach **if** it were sound.

Rule 8 inventory:
  * «لَيْسَ مِنَّا مَنْ سَحَرَ أَوْ سُحِرَ لَه» — **Ibn Bāz: «الحَدِيثُ
    صَحِيحٌ رَوَاهُ الإِمَامُ أَحْمَدُ وَأَبُو دَاوُدَ بِإِسْنَادٍ جَيِّد.»**
  * أَثَرُ حَفْصَة — the compiler: «وَسَنَدُهُ صَحِيح»; Ibn Kathīr: «صَحَّ».
    The third route (al-Ṭabarānī) al-Haythamī weakens via Ismāʿīl ibn ʿAyyāsh.
  * The ḥadīth of the Prophet ﷺ being bewitched — Ibn al-Qayyim: «ثَابِتٌ
    عِنْدَ أَهْلِ العِلْمِ بِالحَدِيث، لَا يَخْتَلِفُونَ فِي صِحَّتِه»; the
    Ṣaḥīḥayn agreed on it.
  * الزُّهَرَة reports — **«وَلَا يَصِحُّ فِي البَابِ شَيْءٌ مَرْفُوع»**; Abū
    Ḥātim: «مُنْكَر»; Ibn Bāz on the marfūʿ: «حَدِيثٌ ضَعِيف», and on Ibn
    ʿUmar's reported cursing of al-Zuhrah: «لَيْسَ بِصَحِيح».
  * «هِيَ مِنْ عَمَلِ الشَّيْطَان» (al-nushrah), «عِبَادَ اللهِ تَدَاوَوْا
    وَلَا تَدَاوَوْا بِحَرَام», «إِنَّ اللهَ لَمْ يَجْعَلْ شِفَاءَكُمْ فِيمَا
    حَرَّمَ عَلَيْكُم», «مَا تَعَوَّذَ المُتَعَوِّذُونَ بِمِثْلِهِمَا», «إِنَّ
    النَّارَ لَا يُعَذِّبُ بِهَا إِلَّا الله» — quoted here without gradings,
    so the page says so and supplies none.
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


def shub(n, claim, answer):
    return ('<div style="margin:0 0 .9rem;padding:.75rem .85rem;'
            'border:1px solid var(--line);border-radius:var(--radius-sm)">'
            '<p style="margin:0 0 .4rem;font-size:.9rem;color:var(--ink-light)">'
            '<strong>الشُّبْهَةُ %s —</strong> <em>%s</em></p>'
            '<p style="margin:0;font-size:.93rem"><strong>الجَوَاب —</strong> '
            '%s</p></div>' % (n, claim, answer))


b = B.objectives([
    'State exactly <strong>what</strong> the magic affected in the Prophet ﷺ '
    'and what it did <strong>not</strong>.',
    'Answer the objection from %s — and say what %s actually guarantees.'
    % ('«' + ar('وَاللهُ يَعْصِمُكَ مِنَ النَّاس') + '»', ar('العِصْمَة')),
    'Give the answer to <em>«a khabar āḥād is not taken in ʿaqīdah»</em>, '
    'including the point about %s and %s.'
    % (ar('الأُصُول'), ar('الفُرُوع')),
    'Define %s and give its ruling, with the reason stated as a principle.'
    % ar('النُّشْرَة'),
    'Demolish the <strong>necessity</strong> argument for treating magic with '
    'magic — Ibn Bāz’s sentence, Ibn Taymiyyah’s reasons, and the condition '
    'inside the qāʿidah.',
    'Explain why <strong>a recitation that does not heal</strong> is no '
    'argument for going to a magician — and the proof from the Prophet’s ﷺ own '
    'final illness.',
    'Say what the sharḥ concludes about <strong>Hārūt and Mārūt</strong>, and '
    'what it does with the stories of <strong>al-Zuhrah</strong>.',
])

b += B.provenance(179, 193)

b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><strong>This closes the '
        'longest clause in the book.</strong> Part 1 was what magic is, part 2 '
        'the ruling on the magician — <em>and these fifteen folios are the ones '
        'an ordinary Muslim will actually need</em>, because they are about '
        '<strong>being harmed</strong> and <strong>what may be done about '
        'it</strong>.</p>'
        '<p style="margin:0;font-size:.92rem">They also contain the best '
        'sustained piece of apologetics in the book: <strong>six objections to '
        'the ḥadīth that the Prophet ﷺ was bewitched, answered one at a '
        'time.</strong></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))

# ---------------------------------------------------------------- the incident
b += B.heading('سِحْرُ لَبِيدِ بْنِ الأَعْصَم', 'What Happened, and What It Did Not Touch')
b += B.prose(
    'The question put to him is the whole difficulty in one breath: '
    '<em>how can the Messenger ﷺ be bewitched when Allah says «وَاللهُ '
    'يَعْصِمُكَ مِنَ النَّاس»? And how, when he receives revelation and conveys '
    'it — how does he convey it while bewitched? And what of the disbelievers’ '
    'saying «you follow none but a bewitched man»?</em>')
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><em>«This is established '
        'in the authentic ḥadīth. And <strong>when the revelation had settled '
        'and the message had settled, and the proofs of prophethood and the '
        'truthfulness of the message had been established, and Allah had given '
        'His Prophet victory over the mushrikīn and humbled them</strong> — a '
        'person of the Jews called <strong>Labīd ibn al-Aʿṣam</strong> went '
        'against him and worked magic for him in a comb and combings and the '
        'sheath of a male date-palm spathe. So it came to be '
        '<strong>imagined</strong> to him that he had done a certain thing with '
        'his wife when he had not done it.»</em></p>'
        '<p style="margin:0;font-size:.95rem"><em>«<strong>But there did not '
        'depart from him — and praise be to Allah — his intellect, nor his '
        'awareness, nor his discernment</strong>, in what he spoke to the people '
        'of; <strong>and he spoke to the people with the truth which Allah had '
        'revealed to him</strong>; but he sensed something that affected him in '
        'some measure with his wives.»</em></p>'))
b += B.prose(
    '<strong>Read the timing first, because the sharḥ puts it first and it is '
    'not decoration.</strong> <em>This happened after the message was '
    'established and its proofs had been given. Whatever it was, it was not an '
    'event that could have put the mission in doubt — the mission was already '
    'proved.</em>')
b += B.sharh(
    p('Then what was done about it: <em>«so the revelation came to him from his '
      'Lord by means of Jibrīl عَلَيْهِ السَّلَام, and informed him of what had '
      'occurred; so he sent one who extracted that thing from a well belonging '
      'to one of the Anṣār, and he destroyed it; and that effect '
      '<strong>departed from him</strong> — and praise be to Allah; and He sent '
      'down upon him the two sūrahs of refuge, and he recited them, '
      '<strong>and every affliction departed from him</strong>.»</em>') +
    p('And the Prophet’s ﷺ words <em>«%s»</em> — <strong>given here with no '
      'grading, so none is supplied.</strong>'
      % ar('مَا تَعَوَّذَ المُتَعَوِّذُونَ بِمِثْلِهِمَا')) +
    p('<strong>And the conclusion, stated flatly:</strong> <em>«and there did '
      'not follow from that <strong>anything of what harms people, or impairs '
      'the message or the revelation</strong>; and Allah — glorified and exalted '
      '— protected him from the people <strong>from what prevents the arrival of '
      'the message and its conveyance</strong>.»</em>'))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><strong>That last clause '
        'is the key to the whole section, and it is a definition of '
        'العِصْمَة.</strong> He does not say Allah protected him from harm. He '
        'says Allah protected him <em>«from what prevents the arrival of the '
        'message and its conveyance»</em>.</p>'
        '<p style="margin:0;font-size:.93rem">And then the list, so that nobody '
        'can pretend otherwise: <em>«as for what befalls the messengers of kinds '
        'of affliction — <strong>he was not protected from it; rather something '
        'of that befell him</strong>: he was <strong>wounded on the day of '
        'Uḥud</strong>, and the <strong>helmet was broken on his head</strong>, '
        'and some of the rings of the mail <strong>entered into his '
        'cheeks</strong>, and he <strong>fell into one of the pits</strong> that '
        'were there; and they constrained him in Makkah '
        '<strong>severely</strong>… and Allah raised his ranks by it, and '
        'elevated his station, and multiplied his good deeds by it — '
        '<strong>but Allah protected him from them, so they were not able to '
        'kill him, nor to prevent him from conveying the message</strong>… and '
        'he conveyed the message and discharged the trust.»</em></p>'))
b += B.prose(
    '<em>So the ʿiṣmah is specific, and the specificity is the answer.</em> '
    '<strong>«وَلَيْسَ مِنَ العِصْمَةِ عَدَمُ ابْتِلَائِهِم، بَلْ هُمْ '
    'أَشَدُّ النَّاسِ بَلَاءً.»</strong> <em>A man who holds that prophets are '
    'shielded from pain has to explain Uḥud, and cannot.</em>')

# ---------------------------------------------------------------- six shubuhat
b += B.heading('الشُّبُهَاتُ السِّتّ', 'Six Objections, Answered in Order')
b += B.sharh(
    shub('الأُولَى',
         'The ḥadīth is not sound, <strong>because Hishām ibn ʿUrwah who '
         'narrated it was mukhtaliṭ</strong> — his memory confused — as Ibn '
         'al-Qaṭṭān mentioned.',
         '<strong>al-Dhahabī</strong> in <em>al-Mīzān</em>: '
         '<em>«<strong>لَمْ يَخْتَلِطْ أَبَدًا</strong> — he was never '
         'confused — <strong>and no weight is given to what Abū al-Ḥasan ibn '
         'al-Qaṭṭān said</strong>»</em>; and <strong>Ibn Ḥajar</strong> in '
         '<em>al-Tahdhīb</em>: <em>«and we have not seen anyone preceding him in '
         'that»</em>. <strong>And then, granting it for argument:</strong> '
         '<em>«what is the proof that he narrated it <strong>after</strong> the '
         'confusion and not before — and a great multitude narrated it from '
         'him?»</em> — Egyptians, Meccans, Baṣrans and Madīnans, '
         '<em>«and the generality of them are of the trustworthy and firm»</em>. '
         'And <strong>Ibn Bāz’s own principle</strong>, said of Abū Isḥāq '
         'al-Sabīʿī: <em>«<strong>الأَصْلُ عَدَمُ الغَلَطِ بِسَبَبِ '
         'الاخْتِلَاط</strong> — the default is the absence of error on account '
         'of confusion; because the imāms narrated from him and paid no heed to '
         'his confusion.»</em> <strong>Plus:</strong> the ḥadīth has corroborating '
         'witnesses; the people of ḥadīth were agreed on its authenticity and '
         'received it with acceptance; <em>and neither al-Dāraquṭnī nor '
         'al-Jayyānī nor Abū Masʿūd al-Dimashqī criticised it — of those who did '
         'criticise some chains in the Ṣaḥīḥayn</em>. '
         '<strong>Ibn al-Qayyim:</strong> <em>«established with the people of '
         'knowledge of ḥadīth; <strong>they do not differ about its '
         'authenticity</strong>… and <strong>not one of the people of ḥadīth '
         'spoke about it with a single word</strong>; and the story is well '
         'known among the people of tafsīr and the sunan and ḥadīth and history '
         'and the jurists — <strong>and these know the states of the Messenger '
         'of Allah ﷺ and his days better than the theologians</strong>.»</em>'))
b += B.sharh(
    shub('الثَّانِيَة',
         'The ḥadīth of the magic is a <strong>khabar āḥād</strong>, and '
         'solitary reports <strong>are not taken in matters of belief</strong> '
         '— only the Qurʾān and the mutawātir.',
         '<strong>Three answers.</strong> <em>«The statement that a solitary '
         'report is not taken in ʿaqīdah is <strong>an innovation in the '
         'religion</strong>, and it is a false statement of the statements of '
         'the people of innovation, <strong>contrary to the Book and the Sunnah '
         'and the consensus of the Salaf</strong>.»</em> '
         '<strong>Second:</strong> <em>«this report <strong>yields '
         'knowledge</strong>, by the consensus of the imāms of criticism on its '
         'establishment.»</em> '
         '<strong>And third — the one worth keeping:</strong> <em>«believing in '
         'the possibility of magic affecting the Prophet ﷺ '
         '<strong>in what does not touch the Sharīʿah</strong> is of '
         '<strong>the branches of belief, not of its foundations</strong>.»</em> '
         '<em>Which is to say the objection does not even reach its target: '
         'nobody is founding a doctrine on this. It is a report about an event '
         'in a life.</em>'))
b += B.sharh(
    shub('الثَّالِثَة',
         'Labīd <strong>did not bewitch him</strong>; he only '
         '<strong>attempted</strong> it, and Allah informed him of it, and the '
         'magic had no effect on him — just as the magic of Pharaoh’s magicians '
         'had no effect on Mūsā.',
         '<strong>False on both halves.</strong> As to the first: the wording of '
         'ʿĀʾishah’s ḥadīth is <em>«<strong>سُحِرَ رَسُولُ اللهِ ﷺ</strong>»</em> '
         '— <em>he WAS bewitched</em> — <em>«so it indicates the '
         '<strong>occurrence</strong> of the magic, not merely the '
         'attempt»</em>; and the word <strong>«%s»</strong> means '
         '<em>bewitched</em>; and her words <em>«until it would be imagined to '
         'him»</em>. As to the second: <em>«the verses speak plainly that they '
         'bewitched the eyes of the people, and awe came over them from the '
         'staffs and ropes <strong>which they saw moving</strong> and which were '
         'not so in reality; <strong>and what occurred to the eyes of the people '
         'occurred to Mūsā likewise</strong> — when he conceived fear within '
         'himself; and this is of the effect of the magic '
         '<strong>upon his eyes</strong>, for otherwise why did he see the ropes '
         'and staffs moving?»</em>' % ar('مَطْبُوب')))
b += B.ayah(
    'فَأَوْجَسَ فِي نَفْسِهِ خِيفَةً مُّوسَىٰ',
    'And Mūsā conceived fear within himself.',
    'سُورَةُ طَه · 20:67')
b += B.sharh(
    shub('الرَّابِعَة',
         'The ḥadīth <strong>contradicts</strong> Allah’s saying '
         '«<strong>%s</strong>».' % ar('وَاللهُ يَعْصِمُكَ مِنَ النَّاس'),
         '<em>«That verse is <strong>among the last to be revealed</strong>, as '
         'Ibn Kathīr mentioned; <strong>and the Prophet ﷺ had been bewitched, '
         'and his tooth broken, and his head wounded, BEFORE its '
         'revelation</strong>.»</em> '
         '<strong>And on the meaning:</strong> <em>«and it is said: '
         'He protects you <strong>from killing, and captivity, and '
         'destruction</strong>. And the protection is established for the '
         'prophets of Allah — <strong>but it is not of the protection that they '
         'not be tried; rather they are the most severely tried of '
         'people</strong>; so what is intended by the protection is '
         '<strong>not</strong> their not being exposed to bodily harms.»</em> '
         'And Ibn Bāz, as above: <em>«Allah protected him from the people '
         '<strong>in what prevents the conveying of the message</strong>»</em> — '
         '<strong>not from illness and injury.</strong>'))
b += B.ayah(
    'وَاللَّهُ يَعْصِمُكَ مِنَ النَّاسِ',
    'And Allah will protect you from the people.',
    'سُورَةُ المَائِدَة · 5:67')
b += B.sharh(
    shub('الخَامِسَة',
         'If the harm of magic reached the Messenger ﷺ, then '
         '<strong>the disbelievers would have been right</strong> in their '
         'saying «%s» — “you follow none but a bewitched man”.'
         % ar('إِنْ تَتَّبِعُونَ إِلَّا رَجُلًا مَسْحُورًا'),
         '<em>«The disbelievers intended by that only that he was '
         '<strong>insane</strong>, his mind gone by means of magic, and that for '
         'this he abandoned their religion; and it is said: <strong>مَسْحُورًا '
         'meaning a magician</strong>, bewitching people; and it is said: you '
         'follow none but a man who <strong>has a lung</strong>» — i.e. a mere '
         'mortal, «<em>eating food and drinking drink, not an angel of the '
         'angels</em>»; «and it is said: <strong>مَخْدُوعًا — deceived</strong>. '
         'So the disbelievers’ intent goes back to the disorder of his mind by '
         'magic, or to deception, or that he is a human being, or that he is a '
         'magician — <strong>and the ḥadīth indicates none of these corrupt '
         'meanings</strong>; and there is in the verse no indication of the '
         'impossibility of magic befalling him <strong>which does not affect his '
         'heart, nor his belief, nor his mind, but affects his body '
         'only</strong>.»</em>'))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><strong>And then a '
        'precision about the effect itself which settles the objection '
        'completely.</strong></p>'
        '<p style="margin:0 0 .5rem;font-size:.93rem"><em>«And the kind of '
        'effect has been specified: that he would imagine coming to his wives '
        'when he did not come to them — <strong>and he, along with that, was '
        'certain that the act had not occurred</strong>; so the matter was not '
        'confused for him such that he would believe the non-occurrence to be an '
        'occurrence. <strong>Rather that was a passing thought</strong>; and '
        'were it supposed that it reached the level of supposition, '
        '<strong>it was in one of the affairs of the world, and did not pass '
        'beyond it to the rest of the affairs of the world — let alone to the '
        'affairs of the religion</strong>.»</em></p>'
        '<p style="margin:0;font-size:.94rem"><strong>And the evidential '
        'clincher is an absence:</strong> <em>«it has not been reported that he '
        '<strong>deputed anyone to lead the people in prayer</strong>, nor '
        '<strong>to manage their affairs</strong>; so the ḥadīth does not '
        'indicate that he ﷺ was disordered in his mind, such that it could be '
        'said it contradicts the verse.»</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))
b += B.sharh(
    shub('السَّادِسَة',
         'Magic affecting the Messenger ﷺ <strong>leads to the absence of trust '
         'in everything he brought</strong> from Allah.',
         '<em>«A man is doubted only when <strong>his affair is hidden</strong>, '
         'or when he is <strong>known to have erred and denied it</strong>; '
         'as for one for whom there is <strong>decisive proof of his '
         'truthfulness</strong> — <strong>the possibility of doubt does not '
         'arise upon any matter of the matters the ḥadīth brings</strong>; '
         'because what befell him ﷺ was <strong>in his noble body</strong>, and '
         'in <strong>a particular matter</strong> also — not in his discernment '
         'nor his belief; so it did not prevent him from conveying the message '
         'and discharging it; <strong>and it has not been reported that he said '
         'a statement and then retracted it</strong>.»</em>'))

# ---------------------------------------------------------------- undo it
b += B.heading('إِلْزَامُ السَّاحِرِ بِإِزَالَةِ مَا فَعَل', 'Made to Undo It First')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><em>«<strong>The magician, when he '
        'is known, is compelled to remove what he has done</strong>; so it is '
        'said to him: <strong>either you remove what you did, or your neck is '
        'struck.</strong> Then, when he has removed that thing, '
        '<strong>the one in authority kills him</strong> — because the magician '
        'is killed, upon the correct view, without being asked to repent, as '
        'ʿUmar رَضِيَ اللهُ عَنْه did.»</em></p>') +
    p('<em>Note the order, which is a mercy toward the victim rather than toward '
      'the magician:</em> <strong>the harm is undone first.</strong> <em>The '
      'sentence does not take precedence over the Muslim who is still '
      'suffering.</em>'))
b += B.sharh(
    p('He grounds it in <strong>Ḥafṣah</strong>’s deed — <em>«and when Ḥafṣah '
      'the Mother of the Believers knew that a slave girl of hers had bewitched '
      'her… <strong>she killed her</strong>»</em> — <strong>and the compiler’s '
      'footnote on it is doing two jobs at once.</strong>') +
    table([
        row('the chain',
            'ʿAbdullāh ibn Aḥmad in <em>al-Masāʾil</em> and al-Bayhaqī, from '
            'ʿUbaydullāh ibn ʿUmar from Nāfiʿ from Ibn ʿUmar from Ḥafṣah: '
            '<em>a slave girl of hers bewitched her, <strong>and she confessed '
            'to the magic and brought it out</strong>, so she killed her</em>. '
            '<strong>«وَسَنَدُهُ صَحِيح»</strong>; and <strong>Ibn Kathīr:</strong> '
            '<em>«it is authentic that Ḥafṣah…»</em>; and Mālik has it in '
            '<em>al-Muwaṭṭaʾ</em> as a balāgh. <em>A third route, al-Ṭabarānī’s, '
            'al-Haythamī weakens through Ismāʿīl ibn ʿAyyāsh’s narrations from '
            'the Madīnans, «and the rest of its men are trustworthy».</em>'),
        row('<strong>the governance</strong>',
            'The same chain carries what happened next: <em>«that reached '
            '<strong>ʿUthmān</strong> رَضِيَ اللهُ عَنْه <strong>and he became '
            'angry</strong>; so Ibn ʿUmar came to him and said: her slave girl '
            'bewitched her, she confessed to the magic and brought it out — and '
            'ʿUthmān desisted.»</em> And the narrator’s own reading of it: '
            '<em>«<strong>and it is as though his anger was only at her killing '
            'her without his command</strong>»</em>'),
    ]) +
    p('<strong>Read that second row twice.</strong> <em>A Mother of the '
      'Believers, with a confession and the magic physically produced, acted — '
      'and the Caliph was angry, and the anger is reported to have been about '
      '<strong>acting without the authority</strong>.</em> '
      '<strong>That is the fourth nullifier’s rule showing up as a fact of the '
      'first generation’s history</strong>, and it is on this page for that '
      'reason.') +
    p('<em>Note also the sequence in her case:</em> the slave girl '
      '<strong>confessed and produced the magic</strong> — i.e. the harm was '
      'undone — <em>and only then was she killed</em>, which is exactly the rule '
      'Ibn Bāz stated above.'))

# ---------------------------------------------------------------- al-nushrah
b += B.heading('حُكْمُ النُّشْرَة', 'Undoing Magic With Magic')
b += B.prose(
    '<strong>This is the practical heart of the lesson</strong>, and the sharḥ '
    'gives it its own heading. <em>A Muslim has been harmed. May he go to a '
    'magician to have it undone?</em>')
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><em>«And whoever is '
        'afflicted with magic, <strong>it is not for him to treat himself with '
        'magic</strong> — for <strong>evil is not removed by evil, and disbelief '
        'is not removed by disbelief; rather evil is removed by good.</strong> '
        'And for this, when he — upon him be peace and blessings — was asked '
        'about <strong>النُّشْرَة</strong>, he said: '
        '<strong>«هِيَ مِنْ عَمَلِ الشَّيْطَان»</strong> — it is of the work of '
        'the devil.»</em></p>'
        '<p style="margin:0;font-size:.93rem"><em>«And the nushrah mentioned in '
        'the ḥadīth is: <strong>the undoing of magic from the bewitched '
        'person BY MAGIC.</strong>»</em> — <strong>the ḥadīth is given here '
        'without a grading, so none is supplied.</strong></p>'))
b += B.sharh(
    p('<strong>«الشَّرُّ لَا يُزَالُ بِالشَّرّ» is the principle, and he gives '
      'three separate reasons under it:</strong>') +
    table([
        row('it is <strong>shirk</strong>',
            '<em>«as for treating it <strong>by the work of the magicians</strong> '
            'and their like, of what they draw near to the jinn by, '
            '<strong>by slaughter or other acts of devotion</strong> — this is '
            'not permitted, because it is of the work of the devil; '
            '<strong>rather it is of the GREATER SHIRK</strong>»</em>'),
        row('the <strong>mechanism</strong>',
            '<em>«the undoing of magic at the hand of the magician is of the '
            'work of the devil, <strong>because he undoes it by supplication to '
            'other than Allah, and seeking rescue from other than Allah, and '
            'doing what Allah has forbidden</strong>»</em>'),
        row('what it <strong>leads to</strong>',
            '<em>«and it <strong>leads to being pleased with what the magician '
            'said and with what he does of magic</strong>»</em> — '
            '<em>which is the matn’s own «أَوْ رَضِيَ بِهِ»</em>'),
    ]) +
    p('And likewise forbidden is <em>«treating it by asking the '
      '<strong>soothsayers and fortune-tellers and charlatans</strong>, and '
      'using what they say; because <strong>they are not believed</strong>, and '
      'because they are <strong>lying reprobates who claim knowledge of the '
      'unseen</strong> and confuse people»</em> — which is part 2’s material '
      'arriving where it bites.'))
b += B.hadith(
    'لَيْسَ مِنَّا مَنْ سَحَرَ أَوْ سُحِرَ لَه',
    '“He is not of us who performs magic, or has magic performed for him.”',
    'قَالَ ابْنُ بَاز: «الحَدِيثُ صَحِيحٌ، رَوَاهُ الإِمَامُ أَحْمَدُ '
    'وَأَبُو دَاوُدَ بِإِسْنَادٍ جَيِّد» · a named grading')
b += B.sharh(
    p('<strong>And look at what that ḥadīth rules out by its second clause.</strong> '
      '<em>«أَوْ سُحِرَ لَه» — or had magic performed <strong>for</strong> him.</em> '
      'The man commissioning it is in the ḥadīth, not only the man performing '
      'it. <strong>Which is precisely the case of the person who goes to a '
      'magician to have his own magic undone.</strong>') +
    p('Ibn Bāz uses it exactly so, and adds an <em>a fortiori</em>: '
      '<strong>«وَإِذَا كَانَ الكَاهِنُ فَالسَّاحِرُ مِنْ بَابِ '
      'أَوْلَى»</strong> — <em>if the soothsayer carries the forty-day threat, '
      'then the magician all the more</em> — <strong>«فَكَيْفَ بِالسَّاحِرِ '
      'الَّذِي يَعْبُدُ الشَّيَاطِينَ وَيَعْبُدُ الجِنّ؟»</strong>'))

# ---------------------------------------------------------------- darurah
b += B.heading('العِلَاجُ مَا هُوَ بِضَرُورَة', 'The Necessity Argument, Taken Apart')
b += B.prose(
    '<strong>This is the argument everyone reaches for, and the sharḥ spends '
    'two folios on it.</strong> <em>«They argue by necessity» — the questioner '
    'says it outright.</em>')
b += B.sharh(
    qa('They argue by <strong>necessity</strong>.',
       '<em>«<strong>The medicine is not a necessity. Treatment is not a '
       'necessity. Treatment is a sunnah — it is recommended that one treat '
       'himself.</strong> It is not a necessity.»</em>') +
    qa('The statement of some of the jurists that it is permitted to undo magic '
       'with magic like it — and Imām Aḥmad and Saʿīd ibn al-Musayyib are said '
       'to have allowed it?',
       '<em>«<strong>غَلَط</strong> — a mistake.»</em> and: '
       '<em>«<strong>هِيَ مِنْ عَمَلِ الشَّيْطَان.</strong>»</em>') +
    p('<em>That answer is short because the work is done underneath it, and the '
      'compiler supplies the work.</em>'))
b += B.sharh(
    p('<strong>Ibn Taymiyyah, on why medical treatment is not a necessity at '
      'all — five reasons:</strong>') +
    table([
        row('١', '<em>«<strong>Many of the sick, or most of the sick, are healed '
            'without treatment</strong>»</em> — especially country people and '
            'those in the far reaches of the earth, «<em>Allah heals them by '
            'what He created in them of the natural powers in their bodies… and '
            'by what He makes easy for them of a kind of movement and work, or '
            '<strong>an answered supplication</strong>, or '
            '<strong>a beneficial recitation</strong>, or '
            '<strong>a strength of heart and good reliance</strong></em>». '
            '<strong>Whereas eating is necessary</strong> — «<em>were he not to '
            'eat he would die</em>»'),
        row('٢', 'Eating at necessity is <strong>obligatory</strong>; Masrūq: '
            '<em>«whoever is compelled to the carrion and does not eat, and '
            'dies, enters the Fire»</em>. <strong>But treatment is not '
            'obligatory</strong> — and the proof is '
            '<strong>the black woman whom the Prophet ﷺ gave the choice</strong> '
            'between <em>patience upon the affliction and entering the '
            'Garden</em>, and <em>supplication for health</em> — '
            '<strong>«فَاخْتَارَتِ البَلَاءَ وَالجَنَّة»</strong>; '
            '<em>«and had the removal of illness been obligatory, there would '
            'have been no place for the choice… and I do not know of any '
            'predecessor who made treatment obligatory»</em>'),
        row('٣', '<strong>The medicine is not certain</strong> — «<em>in many '
            'illnesses it is not even supposed that it will repel the illness; '
            'for were that consistent, no one would die</em>» — '
            '<strong>unlike food against hunger, which is certain</strong>'),
        row('٤', '<strong>An illness has many medicines</strong> — «<em>so if it '
            'is not repelled by the forbidden one, he moves to the lawful one; '
            'and it is impossible that there be no cure or medicine for it among '
            'the lawful; and He who sent down the disease sent down for every '
            'disease a cure, except death</em>» — and it is not permissible that '
            'the cures be in the forbidden category, «<em>and He is the Kind, '
            'the Merciful</em>»'),
        row('٥', '<em>«and in it is the fiqh of the chapter»</em> — hunger has '
            '<strong>one remover</strong>; illness is removed '
            '<strong>by many kinds of causes</strong>, outward and inward, '
            'spiritual and bodily — «<em>so the medicine is not determined as '
            'the remover</em>», and even the specific remedy «<em>is hidden from '
            'most people</em>», so that a specialist may spend much of his life '
            'learning it and still the kind of the illness and its cure be '
            'hidden from him. <em>«So the causes removing illness part from the '
            'causes removing hunger in these plain realities — and so their '
            'rulings parted.»</em>'),
    ]))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.93rem"><strong>And the Permanent '
        'Committee names the condition inside the qāʿidah itself</strong>, which '
        'is what the argument from necessity always skips:</p>'
        '<p style="margin:0 0 .5rem;font-size:.94rem"><em>«The rule '
        '<strong>«الضَّرُورَاتُ تُبِيحُ المَحْظُورَات»</strong>… '
        '<strong>it is a condition of this rule that the forbidden thing be '
        "LESS than the necessity</strong>, as the scholars of uṣūl have "
        'established. And since <strong>magic is disbelief and shirk, it is a '
        'greater harm</strong>… and magic <strong>can be treated by the '
        'legislated causes</strong>, so there is no compulsion to treat it by '
        'what is disbelief and shirk.»</em></p>'
        '<p style="margin:0;font-size:.94rem"><strong>And ʿAllāmah Muḥammad ibn '
        'Ibrāhīm, on those who permitted the nushrah for necessity, in one '
        'sentence:</strong> <em>«And magic is forbidden, and disbelief. '
        '<strong>So is disbelief to be committed so that sick or afflicted souls '
        'may live?</strong> — along with the fact that in most cases the '
        'bewitched person <strong>dies or his mind is disordered</strong>. '
        '<strong>So the Messenger ﷺ forbade and shut the door, and did not make '
        'a distinction</strong> — not in the work of the devil, and not in the '
        'bewitched person.»</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))
b += B.sharh(
    p('And the two prophetic wordings he cites for the general rule: '
      '<em>«%s»</em> — O slaves of Allah, treat yourselves, and do not treat '
      'yourselves with what is forbidden — and <em>«%s»</em> — Allah has not '
      'placed your cure in what He has forbidden you. '
      '<strong>The sharḥ gives the first as «قَالَ النَّبِيُّ ﷺ» and the second '
      'as «رُوِيَ عَنْه», with no gradings at this place, so none are '
      'supplied.</strong>'
      % (ar('عِبَادَ اللهِ تَدَاوَوْا، وَلَا تَدَاوَوْا بِحَرَام'),
         ar('إِنَّ اللهَ لَمْ يَجْعَلْ شِفَاءَكُمْ فِيمَا حَرَّمَ '
            'عَلَيْكُم'))))

# ---------------------------------------------------------------- when it fails
b += B.heading('وَإِذَا لَمْ يُشْفَ بِالقِرَاءَة', 'And When the Recitation Does Not Heal')
b += B.prose(
    '<strong>This is the pastoral half, and it is the reason the page is not '
    'merely polemic.</strong> <em>The real situation is not a man choosing '
    'between two treatments. It is a man who has tried the lawful one, and '
    'nothing happened, and is now desperate.</em>')
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><em>«And if the sick '
        'person was not healed by the recitation — <strong>medicine likewise '
        'does not necessarily entail healing</strong>; because '
        '<strong>not every treatment benefits</strong> and achieves the '
        'intended end. <strong>Allah may defer the healing to a long '
        'term</strong>, and a person may <strong>die of this illness</strong>; '
        'and <strong>it is not a condition of treatment that the person be '
        'healed</strong>.»</em></p>'
        '<p style="margin:0;font-size:.95rem"><em>«<strong>And that is not an '
        'excuse</strong> — if he was treated by someone with recitation and no '
        'healing appeared to him — <strong>to turn to the magicians</strong>; '
        'because the one under obligation is <strong>commanded to take up the '
        'legislated and permitted causes</strong>, and '
        '<strong>forbidden from taking up the forbidden causes</strong>.»</em></p>'))
b += B.sharh(
    p('And then the sentence that reframes the whole expectation: '
      '<em>«and <strong>many people are not benefited by the causes, nor by the '
      'recitation with the Qurʾān nor anything else</strong>, for want of the '
      'conditions being met and the impediments being absent. '
      '<strong>And were every sick person to be healed by the recitation or the '
      'medicine, no one would die</strong>; but Allah — glorified is He — is the '
      'One in whose hand is the healing: if He wills it, He makes its causes '
      'easy; and if He does not will it, <strong>the causes do not benefit '
      'him</strong>.»</em>') +
    box('<p style="margin:0;font-size:.94rem"><strong>And then he proves it from '
        'the one case nobody can answer.</strong> <em>«And in his final illness '
        'ﷺ, ʿĀʾishah رَضِيَ اللهُ عَنْهَا used to recite these three sūrahs</em> '
        '[al-Ikhlāṣ, al-Falaq and al-Nās] <em>into his hands ﷺ, then wipe with '
        'them his head and his face and his chest, hoping for their blessing and '
        'what had occurred in them of recitation — '
        '<strong>and he ﷺ passed away in that illness of his; because Allah — '
        'glorified is He — did not will his healing from that illness.</strong>»</em></p>'
        '<p style="margin:.5rem 0 0;font-size:.93rem"><em>The best recitation '
        'there has ever been, over the best man there has ever been, by the hand '
        'of his wife — <strong>and he died of it.</strong> If that is not a '
        'failure of the ruqyah, then nothing in your house is either.</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))
b += B.sharh(
    qa('A matter by which the trial has become general and whose affair has '
       'grown grave — <strong>going to the magicians to undo magic</strong>.',
       '<em>«<strong>هَذَا مُنْكَر.</strong>»</em>') +
    qa('Many of them go to the magicians <strong>and come out with no '
       'result</strong>, so they bear the sin [for nothing].',
       'He <strong>affirmed it</strong>, and said: <em>«Yes. '
       '<strong>And some of them — whisperings, and things he imagined that are '
       'not real</strong>; and this one is being tried with '
       '<strong>the devil’s play and the devil’s whisperings</strong>.»</em>') +
    p('<strong>That is a remarkable thing to find in this chapter and it is '
      'kindly meant.</strong> <em>Much of what a frightened person is certain is '
      'magic is not magic at all — it is waswasah and imagination. '
      'The man who said magic is real and that denying it is kufr is the same '
      'man saying most of what you are afraid of is not it.</em>'))

# ---------------------------------------------------------------- aisha
b += B.heading('أَفَلَا تَنَشَّرْت', 'The One Report Used Against All of This')
b += B.prose(
    'The objection is from <strong>al-Bukhārī</strong>, in the Book of Medicine '
    'and the Book of Adab, in the story of the magic: the thing was extracted at '
    'the Prophet’s ﷺ command, and ʿĀʾishah said — <em>«O Messenger of Allah, so '
    'why did you not…?»</em> <strong>and the wording that follows is the whole '
    'dispute.</strong>')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem">The Prophet ﷺ answered: '
        '<em>«<strong>أَمَّا اللهُ فَقَدْ شَفَانِي، وَأَمَّا أَنَا فَأَكْرَهُ '
        'أَنْ أُثِيرَ عَلَى النَّاسِ شَرًّا</strong>»</em> — '
        '<strong>“As for Allah, He has healed me; and as for me, I dislike to '
        'stir up evil against the people.”</strong> And of the well: '
        '<em>«this is the well I was shown — and it was as though its water were '
        'the steeping of henna, and as though its palms were the heads of '
        'devils.»</em></p>'))
b += B.sharh(
    p('<strong>The compiler’s answer has four steps, and the third is the '
      'finding.</strong>') +
    table([
        row('١', '<em>«There is nothing in the ḥadīth indicating the '
            'permissibility of the nushrah which is of the work of the devil; '
            '<strong>and whoever says that ʿĀʾishah’s intent was this — i.e. '
            'why did you not go to a magician to have the magic undone — '
            'upon him is the proof.</strong>»</em>'),
        row('٢', '<strong>The word is an insertion.</strong> <em>«Then his '
            'saying “تَنَشَّرْت” is <strong>مُدْرَجَة, from the words of Ibn '
            'ʿUyaynah</strong>, as is clear from the context of the ḥadīth in '
            'al-Ḥumaydī’s narration.»</em> <strong>Ibn Ḥajar</strong> in '
            '<em>al-Fatḥ</em>: <em>«so the one who explained what was intended '
            'by her saying “أَفَلَا” — <strong>it is as though he did not recall '
            'the exact word, so he gave it by its meaning</strong>»</em>'),
        row('٣', '<strong>And it may not be from النُّشْرَة at all.</strong> Ibn '
            'Ḥajar: <em>«and it is possible that it is from '
            '<strong>النَّشْر meaning extraction</strong>, so it agrees with the '
            'narration of whoever narrated it with the wording '
            '<strong>“فَهَلَّا أَخْرَجْتَه”</strong> — why did you not bring it '
            'out»</em>; and he reconciles the two wordings: <em>«the extraction '
            'that occurred was of <strong>the root of the magic</strong>, and '
            'the extraction denied was of <strong>the parts of the '
            'magic</strong>»</em>'),
        row('٤', '<strong>And even granting the word, it carries three '
            'meanings:</strong> the <em>shayṭānī</em> nushrah; the '
            '<strong>legislated</strong> nushrah; or <em>النَّشْر</em> in the sense '
            'of making a thing public and bringing it out. '
            '<em>«<strong>وَلَيْسَ فِي الحَدِيثِ مَا يُرَجِّح</strong>»</em> — '
            'and there is nothing in the ḥadīth to make one of them '
            'preponderant, <strong>so there is no proof in it</strong>'),
    ]))
b += B.sharh(
    p('And Ibn Bāz was asked about ʿĀʾishah’s words directly, and answered with '
      'a distinction in three words: <em>«<strong>النَّشْرُ غَيْرُ '
      'السِّحْر</strong>»</em> — <strong>undoing is not the same as '
      'magic.</strong>') +
    p('A questioner then put it as a matter of propriety — <em>is it conceivable '
      'that ʿĀʾishah would propose to the Messenger of Allah ﷺ that he be '
      'treated by the work of a magician? I hold this to be impossible with '
      'respect to the Messenger ﷺ.</em> <strong>And the Shaykh affirmed him and '
      'said: «لَا يُمْكِن»</strong> — it is not possible — citing '
      '«لَيْسَ مِنَّا مَنْ سَحَرَ أَوْ سُحِرَ لَه».'))

# ---------------------------------------------------------------- misc
b += B.heading('مَسَائِلُ خَاتِمَة', 'Three Closing Questions')
b += B.sharh(
    qa('The difference between <strong>the one bewitched</strong> and '
       '<strong>the insane</strong>?',
       '<em>«<strong>The insane</strong> is the one whom a jinnī '
       '<strong>enters into</strong>, only, until his mind is altered. '
       '<strong>And the bewitched</strong> is the one to whom harm occurs — '
       'meaning: <strong>the magicians from among mankind harm him by what they '
       'have gained from the jinn</strong>, as happened with Labīd ibn al-Aʿṣam '
       'when he bewitched the Prophet ﷺ.»</em>') +
    p('<em>Two different things with two different agents.</em> '
      '<strong>In possession, the jinnī acts on the man directly. In magic, '
      '<em>a human being</em> acts, using what he has bought from the '
      'jinn.</strong> <em>Which is why one of them has a criminal and the other '
      'does not.</em>'))
b += B.sharh(
    qa('Is the magician <strong>burned with fire</strong>?',
       '<em>«<strong>No one is burned with fire</strong>, because the '
       'Messenger ﷺ forbade that, and said: <strong>«إِنَّ النَّارَ لَا '
       'يُعَذِّبُ بِهَا إِلَّا الله»</strong> — none punishes with fire but '
       'Allah. <strong>Rather he is killed with the sword.</strong>»</em>') +
    p('<em>The sharḥ gives that prophetic wording here without a grading, so '
      'none is supplied.</em> <strong>And notice the shape of the answer in a '
      'chapter this severe:</strong> the ruling is death, and even so the '
      '<em>manner</em> is restrained by a prohibition — <em>because a mode of '
      'punishment belongs to Allah.</em>'))
b += B.heading('هَارُوتُ وَمَارُوت', 'Two Angels, or Two Kings?')
b += B.ayah(
    'وَمَا أُنزِلَ عَلَى الْمَلَكَيْنِ بِبَابِلَ هَارُوتَ وَمَارُوتَ',
    '…and what was sent down upon the two angels at Bābil, Hārūt and Mārūt.',
    'سُورَةُ البَقَرَة · 2:102')
b += B.sharh(
    qa('Are Hārūt and Mārūt <strong>two angels or two human beings</strong>? We '
       'hope for a statement of the preponderant view.',
       '<em>«<strong>The scholars differed in this, and the more apparent is '
       'that they are two angels, sent down as a trial and a test</strong>, as '
       'Allah said… And <strong>some of the people of knowledge said: they are '
       'two kings from the children of Ādam</strong>, by whom the people were '
       'tried. <strong>And the first statement is the more apparent</strong>; '
       'and the recitation upon this — on the first statement — is with '
       '<strong>fatḥ of the lām</strong> [المَلَكَيْن, the two angels], and on '
       'the second with <strong>kasr</strong> [المَلِكَيْن, the two '
       'kings].»</em>') +
    p('<strong>That is a precise thing and worth seeing.</strong> <em>The '
      'difference of opinion is not merely about history — it is carried by a '
      'single vowel, and each reading belongs to one of the two views.</em>'))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><strong>And then the '
        'stories.</strong> A large body of reports circulates about Hārūt and '
        'Mārūt and <strong>al-Zuhrah</strong> — the woman they are said to have '
        'desired, who was turned into the planet. <strong>The compiler’s verdict: '
        '«وَلَا يَصِحُّ فِي البَابِ شَيْءٌ مَرْفُوع» — nothing in the chapter is '
        'authentic as a prophetic report.</strong></p>'
        '<p style="margin:0;font-size:.93rem"><strong>Ibn Kathīr</strong> traces '
        'it: the nearest it comes to is a report of <strong>Ibn ʿUmar from Kaʿb '
        'al-Aḥbār</strong> — <em>«so the ḥadīth revolved and returned to the '
        'transmission of Kaʿb al-Aḥbār <strong>from the books of the Children of '
        'Isrāʾīl</strong>»</em>. The marfūʿ routes: <strong>Abū Ḥātim</strong> — '
        '<em>«هَذَا حَدِيثٌ مُنْكَر»</em>; <strong>al-Bazzār</strong> on Zuhayr '
        '— <em>«he was not a ḥāfiẓ»</em>; and the later routes rest on narrators '
        'the compiler shows to be <em>مَسْتُورُ الحَال</em> or «very weak».</p>'))
b += B.sharh(
    p('<strong>And Ibn Bāz’s own verdict, which is a model of how to handle an '
      'isrāʾīlī report:</strong>') +
    box('<p style="margin:0 0 .5rem;font-size:.93rem"><em>«ʿAbd al-Razzāq’s '
        'chain here is <strong>good</strong> — and this is of what [Ibn ʿUmar] '
        'narrated <strong>from Kaʿb al-Aḥbār</strong>; and '
        '<strong>Kaʿb al-Aḥbār narrates from the Children of Isrāʾīl the lean '
        'and the fat, the false and the sound — so he is not relied upon and not '
        'depended upon.</strong> As for [its being] from the Prophet ﷺ — '
        '<strong>it is a weak ḥadīth</strong>.»</em></p>'
        '<p style="margin:0;font-size:.93rem"><em>«So the upshot is that it is '
        '<strong>not established from the Prophet ﷺ</strong>; rather it is of '
        'the reports of the Children of Isrāʾīl, in which is the lean and the '
        'fat and the false and the sound and the lie — <strong>so they are not '
        'depended upon</strong>.»</em> And of the whole business: '
        '<em>«and these reports of theirs are <strong>differing, various and '
        'mutually contradictory — so no reliance is placed on them; reliance is '
        'placed only on the text of the Mighty Book</strong>, and Allah knows '
        'best what He intended… <strong>and there is in them no text from the '
        'Messenger explaining that</strong>.»</em></p>'))
b += B.sharh(
    p('<strong>And then two things which show what the discipline is actually '
      'for.</strong>') +
    p('<strong>First, he says what matters instead:</strong> <em>«and the '
      'important thing in this is that He made clear — glorified is He — '
      '<strong>that it is disbelief, and that the knowledge of magic and its '
      'teaching is disbelief</strong>… and it is <strong>a trial and a '
      'test</strong>.»</em> <em>Which returns the Hārūt and Mārūt verse to the '
      'one thing it is cited in the matn for.</em>') +
    p('<strong>Second — and this is the part worth imitating — he says what the '
      'story would teach <em>if</em> it were sound, without accepting it:</strong> '
      '<em>«then this, <strong>if it were authentic</strong>, in it is the '
      'indication of <strong>the foulness of wine</strong>, and that it is '
      'a means to every evil — we seek refuge with Allah: a means to killing, '
      'a means to shirk, a means to fornication, a means to every corruption. '
      '<strong>It is أُمُّ الخَبَائِث — the mother of all foulness.</strong>»</em>') +
    p('<em>And he refuses one more report in passing.</em> Asked about what is '
      'related from <strong>Ibn ʿUmar</strong>, that whenever he saw '
      'al-Zuhrah he cursed it: <strong>«لَيْسَ بِصَحِيح»</strong> — it is not '
      'authentic.'))

b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><strong>النَّاقِضُ '
        'السَّابِع is closed — thirty-five folios, printed ١٥٩–١٩٣, the longest '
        'clause in the book.</strong></p>'
        '<p style="margin:0;font-size:.93rem"><strong>Part 1</strong> — what '
        'magic is: named for concealment; teaching and learning both kufr by the '
        'daleel; the kawnī permission and «نُعَالِجَ قَدَرَ اللهِ بِقَدَرِه»; '
        'and why it is <em>shirk</em> — the slaughter, vows and prostration it '
        'is bought with.<br>'
        '<strong>Part 2</strong> — the ruling: two grounds, the تَفْصِيل he '
        'grants and the أَصْل he keeps, killed as a disbeliever and not as a '
        'ḥadd, the repentance that is refused in court and accepted by Allah, '
        'and the famous ḥadīth of the ḥadd graded weak by seven named '
        'scholars.<br>'
        '<strong>Part 3</strong> — the harm and the remedy: six objections '
        'answered, النُّشْرَة forbidden with its three reasons, the necessity '
        'argument dismantled, the recitation that does not heal, and the '
        'isrāʾīlī stories refused.</p>'
        '<p style="margin:.55rem 0 0;font-size:.92rem"><em>النَّاقِضُ الثَّامِن '
        '— مُظَاهَرَةُ المُشْرِكِينَ وَمُعَاوَنَتُهُمْ عَلَى المُسْلِمِين — '
        'begins at printed folio ١٩٤.</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))

b += B.vocab([
    ('النُّشْرَة', 'al-nushrah', 'undoing magic by magic',
     'Ibn Bāz’s definition, from the ḥadīth: «حَلُّ السِّحْرِ عَنِ '
     'المَسْحُورِ بِالسِّحْر». The Prophet ﷺ called it «مِنْ عَمَلِ '
     'الشَّيْطَان», and Ibn Bāz calls treating by the magicians’ work '
     'الشِّرْكُ الأَكْبَر.'),
    ('مَطْبُوب', 'maṭbūb', 'bewitched',
     'The word in the ḥadīth of the Prophet ﷺ, and one of the proofs that the '
     'magic OCCURRED rather than being merely attempted.'),
    ('العِصْمَة', 'al-ʿiṣmah', 'the divine protection',
     'And it is SPECIFIC: Ibn Bāz — «عَصَمَهُ مِنَ النَّاسِ مِمَّا يَمْنَعُ '
     'مِنْ تَبْلِيغِ الرِّسَالَة». «وَلَيْسَ مِنَ العِصْمَةِ عَدَمُ '
     'ابْتِلَائِهِم، بَلْ هُمْ أَشَدُّ النَّاسِ بَلَاءً.»'),
    ('مُخْتَلِط', 'mukhtaliṭ', 'a narrator whose memory became confused',
     'Claimed of Hishām ibn ʿUrwah to weaken the ḥadīth. al-Dhahabī: «لَمْ '
     'يَخْتَلِطْ أَبَدًا، وَلَا عِبْرَةَ بِمَا قَالَهُ… ابْنُ القَطَّان»; and '
     'Ibn Bāz’s rule: «الأَصْلُ عَدَمُ الغَلَطِ بِسَبَبِ الاخْتِلَاط».'),
    ('خَبَرُ الآحَاد', 'khabar al-āḥād', 'a solitary report',
     'The claim that it is not taken in ʿaqīdah is named here «بِدْعَةٌ فِي '
     'الدِّين» — and anyway this report concerns الفُرُوع of belief, not '
     'الأُصُول.'),
    ('مُدْرَجَة', 'mudrajah', 'an insertion into the text',
     'The finding on «تَنَشَّرْت» in ʿĀʾishah’s report — it is from the words '
     'of Ibn ʿUyaynah, clear from al-Ḥumaydī’s narration; Ibn Ḥajar: he gave it '
     'by its meaning, not recalling the word.'),
    ('الضَّرُورَاتُ تُبِيحُ المَحْظُورَات', 'al-ḍarūrāt tubīḥ al-maḥẓūrāt',
     'necessities permit the forbidden',
     'With the condition the argument always skips — the Lajnah: «أَنْ يَكُونَ '
     'المَحْظُورُ أَقَلَّ مِنَ الضَّرُورَة». Magic is kufr, so it is the '
     'greater harm.'),
    ('أُمُّ الخَبَائِث', 'umm al-khabāʾith', 'the mother of all foulness',
     'Ibn Bāz on wine — stated as what the Hārūt and Mārūt story would teach '
     '«لَوْ صَحَّ», while refusing the story itself.'),
    ('الغَثُّ وَالسَّمِين', 'al-ghathth wa-l-samīn', 'the lean and the fat',
     'Ibn Bāz on Kaʿb al-Aḥbār’s transmissions from the Children of Isrāʾīl — '
     'and therefore «فَلَا يُعْتَمَدُ عَلَيْهِ وَلَا يُعَوَّلُ عَلَيْه».'),
])

b += B.mcq('nq-l13-mcq', [
    ('When did the magic of Labīd ibn al-Aʿṣam occur, and why does the sharḥ '
     'say so first?',
     ['Early in Makkah, before the message was proved',
      'AFTER the revelation and the message had settled and the proofs of '
      'prophethood were established — so it could not have put the mission in '
      'doubt',
      'During the final illness',
      'The sharḥ does not say'], 1),
    ('What did the magic affect?',
     ['His intellect and his memory',
      'That it was imagined to him that he had done something with his wife when '
      'he had not — and he sensed something affecting him in some measure with '
      'his wives',
      'His recitation of the Qurʾān',
      'His judgement in disputes'], 1),
    ('And what did it NOT touch?',
     ['Nothing; it touched everything',
      'His intellect, his awareness and his discernment — «and he spoke to the '
      'people with the truth which Allah had revealed to him»',
      'Only his body',
      'His family life'], 1),
    ('How was it removed?',
     ['By a physician',
      'The revelation informed him; he sent one who extracted it from a well of '
      'the Anṣār and destroyed it; and the two sūrahs of refuge were sent down, '
      'and he recited them',
      'By the recitation of ʿĀʾishah',
      'It was never removed'], 1),
    ('What does the sharḥ say Allah protected him from?',
     ['All bodily harm',
      'From what PREVENTS the arrival of the message and its conveyance',
      'From the Jews specifically',
      'From magic in particular'], 1),
    ('Which afflictions does it list as having actually befallen him?',
     ['None',
      'Wounded at Uḥud; the helmet broken on his head; rings of the mail '
      'entering his cheeks; falling into a pit; and severe constriction in '
      'Makkah',
      'Only hunger and poverty',
      'Only the loss of his children'], 1),
    ('«وَلَيْسَ مِنَ العِصْمَةِ عَدَمُ ابْتِلَائِهِم، بَلْ هُمْ…»',
     ['«…أَبْعَدُ النَّاسِ مِنَ البَلَاء»',
      '«…أَشَدُّ النَّاسِ بَلَاءً»',
      '«…أَقَلُّ النَّاسِ بَلَاءً»',
      '«…مَعْصُومُونَ مِنْ كُلِّ أَذًى»'], 1),
    ('The first objection claims Hishām ibn ʿUrwah was mukhtaliṭ. What did '
     'al-Dhahabī say?',
     ['That he was, late in life',
      '«He was NEVER confused — and no weight is given to what Abū al-Ḥasan ibn '
      'al-Qaṭṭān said»',
      'That the matter is unknown',
      'That it does not affect this ḥadīth'], 1),
    ('And what is the answer even if the confusion were granted?',
     ['That the ḥadīth would fall',
      'That there is no proof he narrated it AFTER the confusion rather than '
      'before, and a great multitude narrated it from him — Egyptians, Meccans, '
      'Baṣrans and Madīnans, mostly trustworthy and firm',
      'That another chain exists',
      'That the Ṣaḥīḥayn are exempt from criticism'], 1),
    ('What is Ibn Bāz’s stated principle on narrators said to be mukhtaliṭ?',
     ['Their reports are rejected outright',
      '«The default is the absence of error on account of confusion; because the '
      'imāms narrated from him and paid no heed to his confusion»',
      'Their reports are accepted only with corroboration',
      'The matter is referred to al-Dhahabī'], 1),
    ('What did Ibn al-Qayyim say about this ḥadīth?',
     ['That it is disputed',
      'That it is established with the people of knowledge of ḥadīth, «they do '
      'not differ about its authenticity», and «not one of the people of ḥadīth '
      'spoke about it with a single word»',
      'That it is weak but acted upon',
      'That its meaning is sound though its chain is not'], 1),
    ('And whom does he contrast with the people of ḥadīth, tafsīr, sunan, '
     'history and fiqh?',
     ['The grammarians',
      'The theologians — «these know the states of the Messenger of Allah ﷺ and '
      'his days better than the theologians»',
      'The physicians',
      'The historians of Persia'], 1),
    ('The second objection is that a khabar āḥād is not taken in ʿaqīdah. What '
     'is the first answer?',
     ['That this report is mutawātir',
      'That the claim is itself «an innovation in the religion», a false '
      'statement of the people of innovation, contrary to the Book, the Sunnah '
      'and the consensus of the Salaf',
      'That ʿaqīdah may rest on weak reports',
      'That the Qurʾān confirms it'], 1),
    ('And the third answer — the one worth keeping?',
     ['That the report is mutawātir in meaning',
      'That believing in the possibility of magic affecting the Prophet ﷺ IN '
      'WHAT DOES NOT TOUCH THE SHARĪʿAH is of the BRANCHES of belief, not its '
      'foundations — so the objection does not reach its target',
      'That the Ṣaḥīḥayn settle all disputes',
      'That the Salaf did not discuss it'], 1),
    ('The third objection says Labīd only ATTEMPTED the magic. How is it '
     'answered?',
     ['By rejecting the report',
      'By the wording: «سُحِرَ رَسُولُ اللهِ ﷺ» — he WAS bewitched — and '
      '«مَطْبُوب» meaning bewitched, and ʿĀʾishah’s «until it would be imagined '
      'to him»',
      'By the consensus',
      'By analogy with Mūsā'], 1),
    ('And the claim that Pharaoh’s magic had no effect on Mūsā?',
     ['It is accepted',
      'It is false — what occurred to the eyes of the people occurred to Mūsā '
      'likewise, «when he conceived fear within himself»; «for otherwise why did '
      'he see the ropes and staffs moving?»',
      'It is left undecided',
      'It applies only to the onlookers'], 1),
    ('The fourth objection is from «وَاللهُ يَعْصِمُكَ مِنَ النَّاس». What is '
     'the chronological answer?',
     ['The verse is abrogated',
      'That verse is among the LAST revealed, as Ibn Kathīr mentioned — and he '
      'had been bewitched, his tooth broken and his head wounded BEFORE its '
      'revelation',
      'The verse concerns Makkah only',
      'The verse concerns killing by poison only'], 1),
    ('And what is said about its meaning?',
     ['That it guarantees freedom from all harm',
      'That He protects him from killing, captivity and destruction — and it is '
      'not of the protection that prophets not be tried',
      'That it concerns the hypocrites only',
      'That it is general with no specification'], 1),
    ('The fifth objection is from «رَجُلًا مَسْحُورًا». What did the '
     'disbelievers mean by it?',
     ['Exactly what the ḥadīth describes',
      'Several things, all of them corrupt — that he was INSANE, his mind gone '
      'by magic; or a magician; or a man who «has a lung», i.e. a mere mortal, '
      'not an angel; or deceived',
      'That he was ill',
      'That he was truthful but mistaken'], 1),
    ('What is the precision given about the effect itself?',
     ['That it lasted years',
      'That he was CERTAIN the act had not occurred — «rather that was a passing '
      'thought»; and were it supposed to reach supposition, it was in one '
      'worldly matter, not passing beyond it, «let alone to the affairs of the '
      'religion»',
      'That it affected his judgement in one case',
      'That it was never specified'], 1),
    ('What absence does the sharḥ use as evidence?',
     ['That no Companion mentioned it',
      'That it was never reported that he deputed anyone to lead the prayer or '
      'to manage people’s affairs',
      'That the Qurʾān does not mention it',
      'That no treatment was sought'], 1),
    ('The sixth objection is that it destroys trust in the message. The answer?',
     ['That trust rests on the Qurʾān alone',
      'A man is doubted when his affair is hidden, or he is known to have erred '
      'and denied it; but where there is decisive proof of truthfulness, doubt '
      'does not arise — and what befell him was in his body and in a particular '
      'matter, not in his discernment or belief',
      'That the ḥadīth is weak after all',
      'That the objection cannot be answered'], 1),
    ('What is the magician made to do before he is executed?',
     ['Name his teachers',
      'Remove what he has done — «either you remove what you did, or your neck '
      'is struck»; then, when he has removed it, the one in authority kills him',
      'Repent publicly',
      'Pay compensation'], 1),
    ('Why is that order significant?',
     ['It gives the magician a chance to escape',
      'It is a mercy toward the VICTIM — the sentence does not take precedence '
      'over the Muslim who is still suffering',
      'It establishes his guilt',
      'It satisfies the ḥadd requirements'], 1),
    ('In Ḥafṣah’s case, what had the slave girl done before she was killed?',
     ['Fled',
      'Confessed to the magic AND brought it out',
      'Denied everything',
      'Repented'], 1),
    ('What happened when news of it reached ʿUthmān رَضِيَ اللهُ عَنْه?',
     ['He approved it',
      'He became ANGRY — and desisted when Ibn ʿUmar explained; and the '
      'narrator’s reading is «as though his anger was only at her killing her '
      'WITHOUT HIS COMMAND»',
      'He ordered an investigation',
      'He said nothing'], 1),
    ('Why is that detail on this page?',
     ['To weaken the athar',
      'Because it is the fourth nullifier’s rule — that a sentence belongs to '
      'the authority — appearing as a fact of the first generation’s history',
      'To show ʿUthmān’s severity',
      'To establish the chain'], 1),
    ('What is النُّشْرَة, in Ibn Bāz’s definition?',
     ['Reciting over the bewitched',
      'The undoing of magic from the bewitched person BY MAGIC',
      'Extracting the magic from where it is hidden',
      'Seeking refuge with the two sūrahs'], 1),
    ('And the principle under its prohibition?',
     ['Necessity permits the forbidden',
      '«Evil is not removed by evil, and disbelief is not removed by disbelief; '
      'rather evil is removed by good»',
      'The ends justify the means in medicine',
      'What is unknown is excused'], 1),
    ('What does Ibn Bāz call treating magic by the magicians’ work — their '
     'slaughter and acts of devotion to the jinn?',
     ['A forbidden means',
      'Of the GREATER SHIRK',
      'A disputed matter',
      'Lesser disbelief'], 1),
    ('And what does he say the undoing at a magician’s hand actually consists '
     'of?',
     ['Herbs and incantations',
      'Supplication to other than Allah, seeking rescue from other than Allah, '
      'and doing what Allah has forbidden',
      'Deception only',
      'A lawful transaction'], 1),
    ('Which clause of «لَيْسَ مِنَّا مَنْ سَحَرَ أَوْ سُحِرَ لَه» catches the '
     'person seeking a cure?',
     ['The first',
      '«أَوْ سُحِرَ لَه» — or had magic performed FOR him',
      'Neither',
      'Both equally'], 1),
    ('What grading does this page give that ḥadīth, and on whose authority?',
     ['None',
      'Ibn Bāz: «the ḥadīth is authentic, narrated by Imām Aḥmad and Abū Dāwūd '
      'with a good chain»',
      'al-Dhahabī: ṣaḥīḥ gharīb',
      'The compiler: ḥasan'], 1),
    ('They argue by necessity. Ibn Bāz’s answer?',
     ['«Necessity is established here»',
      '«The medicine is not a necessity. Treatment is not a necessity. Treatment '
      'is a sunnah — it is recommended that one treat himself»',
      '«Then it is permitted»',
      '«The matter is one of ijtihād»'], 1),
    ('And on the claim that some jurists — and Aḥmad and Saʿīd ibn al-Musayyib '
     '— permitted undoing magic with magic?',
     ['He accepted it',
      '«غَلَط» — a mistake — and «it is of the work of the devil»',
      'He left it undecided',
      'He restricted it to necessity'], 1),
    ('Which of Ibn Taymiyyah’s five reasons rests on the black woman given a '
     'choice by the Prophet ﷺ?',
     ['The first',
      'The second — that eating at necessity is obligatory while treatment is '
      'not: she was given the choice between patience and the Garden, and '
      'supplication for health, and «she chose the affliction and the Garden»',
      'The third',
      'The fifth'], 1),
    ('And which rests on an illness having many remedies?',
     ['The second',
      'The fourth — «so if it is not repelled by the forbidden one, he moves to '
      'the lawful one; and it is impossible that there be no cure for it among '
      'the lawful»',
      'The first',
      'The fifth'], 1),
    ('What condition inside «الضَّرُورَاتُ تُبِيحُ المَحْظُورَات» does the '
     'Lajnah name?',
     ['That the necessity be established by two witnesses',
      'That the FORBIDDEN THING BE LESS than the necessity — and since magic is '
      'disbelief and shirk, it is the greater harm',
      'That no scholar object',
      'That the harm be bodily'], 1),
    ('Muḥammad ibn Ibrāhīm’s sentence against the nushrah for necessity?',
     ['«The matter requires research»',
      '«So is disbelief to be committed so that sick or afflicted souls may '
      'live?» — adding that in most cases the bewitched person dies or his mind '
      'is disordered, and «the Messenger ﷺ forbade and shut the door, and did '
      'not make a distinction»',
      '«Necessity has its own ruling»',
      '«This is a place of ijtihād»'], 1),
    ('A man is treated with recitation and is not healed. Is that an excuse to '
     'go to the magicians?',
     ['Yes, once the lawful means fail',
      'No — medicine likewise does not guarantee healing; «it is not a condition '
      'of treatment that the person be healed»; and the obligated person is '
      'commanded to the legislated causes and forbidden the forbidden ones',
      'Yes, if a scholar permits it',
      'Only for a life-threatening case'], 1),
    ('«وَلَوْ كَانَ كُلُّ مَرِيضٍ يُشْفَى بِالرُّقْيَةِ أَوِ الدَّوَاءِ…»',
     ['«…لَكَانَ ذَلِكَ مِنَ المُعْجِزَات»',
      '«…لَمْ يَمُتْ أَحَد»',
      '«…لَمَا احْتَجْنَا إِلَى الطِّبّ»',
      '«…بَطَلَ القَدَر»'], 1),
    ('What case does Ibn Bāz use to prove it?',
     ['The illness of Abū Bakr',
      'The Prophet’s ﷺ own final illness — ʿĀʾishah recited the three sūrahs '
      'into his hands and wiped his head, face and chest, «and he ﷺ passed away '
      'in that illness of his; because Allah did not will his healing from it»',
      'The plague of ʿAmwās',
      'The wound of Uḥud'], 1),
    ('What does Ibn Bāz observe about much of what people believe to be magic?',
     ['That it is always real',
      'That some of it is «whisperings, and things he imagined that are not '
      'real» — and such a one is being tried with the devil’s play and '
      'whisperings',
      'That it is always the jinn',
      'That it cannot be known'], 1),
    ('ʿĀʾishah’s «أَفَلَا تَنَشَّرْت» is used to permit the nushrah. What is '
     'the compiler’s central finding about the word?',
     ['That it is in every narration',
      'That it is MUDRAJAH — an insertion from the words of Ibn ʿUyaynah, clear '
      'from al-Ḥumaydī’s narration; Ibn Ḥajar: he gave it by its meaning, not '
      'recalling the word',
      'That ʿĀʾishah retracted it',
      'That it is a copyist’s error'], 1),
    ('What other reading does Ibn Ḥajar allow for it?',
     ['From النُّشُور, resurrection',
      'From النَّشْر meaning EXTRACTION — agreeing with the narration «فَهَلَّا '
      'أَخْرَجْتَه»; and the extraction that occurred was of the root of the '
      'magic, the one denied of its parts',
      'From النُّشْرَة الشَّرْعِيَّة only',
      'From النَّشْر meaning publication only'], 1),
    ('And even granting the word, why is there no proof in it?',
     ['Because ʿĀʾishah was young',
      'Because it carries three possible meanings — the shayṭānī nushrah, the '
      'legislated nushrah, or making a thing public — «and there is nothing in '
      'the ḥadīth to make one preponderant»',
      'Because the Prophet ﷺ did not answer',
      'Because al-Bukhārī did not comment'], 1),
    ('What did the Prophet ﷺ answer her?',
     ['«It is permitted»',
      '«As for Allah, He has healed me; and as for me, I dislike to stir up evil '
      'against the people»',
      '«Ask the people of knowledge»',
      '«The matter is finished»'], 1),
    ('Ibn Bāz’s three-word distinction on her words?',
     ['«السِّحْرُ حَرَام»',
      '«النَّشْرُ غَيْرُ السِّحْر» — undoing is not the same as magic',
      '«الأَمْرُ وَاسِع»',
      '«هَذَا مُحْتَمَل»'], 1),
    ('The difference between the insane and the bewitched?',
     ['A difference of degree only',
      'The insane is one whom a JINNĪ enters into until his mind is altered; the '
      'bewitched is harmed by MAGICIANS FROM MANKIND using what they gained from '
      'the jinn',
      'The insane is incurable',
      'The bewitched is not responsible for his acts'], 1),
    ('Is the magician burned with fire?',
     ['Yes, as a deterrent',
      'No — «no one is burned with fire, because the Messenger ﷺ forbade that» '
      'and «none punishes with fire but Allah»; rather he is killed with the '
      'sword',
      'Only if he refuses to undo his magic',
      'The sharḥ does not say'], 1),
    ('Hārūt and Mārūt — what is the more apparent view?',
     ['Two kings of the children of Ādam',
      'Two ANGELS, sent down as a trial and a test',
      'Two devils',
      'Two prophets'], 1),
    ('How is the difference of opinion carried in the recitation?',
     ['By a difference in the consonants',
      'By the vowel on the lām — fatḥ for المَلَكَيْن, the two angels; kasr for '
      'المَلِكَيْن, the two kings',
      'By the case ending',
      'It is not reflected in the recitation'], 1),
    ('What is the verdict on the stories of Hārūt, Mārūt and al-Zuhrah?',
     ['They are authentic',
      '«Nothing in the chapter is authentic as a prophetic report» — the '
      'soundest route goes back to Kaʿb al-Aḥbār from the books of the Children '
      'of Isrāʾīl; Abū Ḥātim called the marfūʿ «munkar»',
      'They are ḥasan by corroboration',
      'They are left undecided'], 1),
    ('What does Ibn Bāz say about Kaʿb al-Aḥbār as a source?',
     ['That he is trustworthy throughout',
      'That he narrates from the Children of Isrāʾīl «the lean and the fat, the '
      'false and the sound — so he is not relied upon and not depended upon»',
      'That he is to be rejected entirely as a person',
      'That his reports are mutawātir'], 1),
    ('What does Ibn Bāz say matters instead, about the Hārūt and Mārūt verse?',
     ['The identification of the two',
      'That Allah made clear that it IS DISBELIEF, and that the knowledge of '
      'magic and its teaching is disbelief — «and it is a trial and a test»',
      'The location of Bābil',
      'The names themselves'], 1),
    ('And what does he say the story would teach IF it were sound?',
     ['The power of the angels',
      'The foulness of WINE — a means to killing, to shirk, to fornication, to '
      'every corruption: «it is the mother of all foulness»',
      'The danger of magic',
      'The weakness of human nature'], 1),
    ('What did he say of the report that Ibn ʿUmar cursed al-Zuhrah whenever he '
     'saw it?',
     ['That it is authentic',
      '«لَيْسَ بِصَحِيح» — it is not authentic',
      'That its chain is good',
      'That it is from Kaʿb'], 1),
])

b += B.tf('nq-l13-tf', [
    ('أَثَّرَ السِّحْرُ فِي عَقْلِ النَّبِيِّ ﷺ وَتَمْيِيزِه.',
     'The magic affected the Prophet’s ﷺ intellect and discernment.', False),
    ('العِصْمَةُ المَذْكُورَةُ فِي الآيَةِ تَعْنِي أَنَّهُ لَا يُصِيبُهُ '
     'أَذًى بَدَنِيّ.',
     'The protection in the verse means no bodily harm befalls him.', False),
    ('قَوْلُهُمْ: خَبَرُ الآحَادِ لَا يُؤْخَذُ بِهِ فِي العَقِيدَةِ '
     'بِدْعَة.',
     'The claim that a solitary report is not taken in ʿaqīdah is an innovation.',
     True),
    ('النُّشْرَةُ هِيَ حَلُّ السِّحْرِ عَنِ المَسْحُورِ بِالسِّحْر.',
     'Al-nushrah is the undoing of magic from the bewitched by magic.', True),
    ('العِلَاجُ ضَرُورَةٌ تُبِيحُ المَحْظُور.',
     'Treatment is a necessity that permits the forbidden.', False),
    ('إِذَا لَمْ تَنْفَعِ الرُّقْيَةُ جَازَ الذَّهَابُ إِلَى '
     'السَّحَرَة.',
     'If the recitation does not benefit, going to the magicians becomes '
     'permitted.', False),
    ('لَا يَصِحُّ فِي قِصَّةِ الزُّهَرَةِ شَيْءٌ مَرْفُوعٌ إِلَى '
     'النَّبِيِّ ﷺ.',
     'Nothing in the story of al-Zuhrah is authentic as a report traced to the '
     'Prophet ﷺ.', True),
])

b += B.memorize(
    'الشَّرُّ لَا يُزَالُ بِالشَّرّ، وَالكُفْرُ لَا يُزَالُ بِالكُفْر، '
    'وَإِنَّمَا يُزَالُ الشَّرُّ بِالخَيْر',
    'Ibn Bāz, on undoing magic by magic. <strong>It is the whole of these '
    'fifteen folios in one line</strong>, and it is the answer to the argument '
    'from desperation — <em>which these folios take seriously rather than '
    'brushing aside: «العِلَاجُ مَا هُوَ بِضَرُورَة، العِلَاجُ سُنَّة»</em>. '
    '<strong>And keep beside it the sentence that makes the whole page '
    'bearable, because it is about the Prophet ﷺ himself:</strong> ʿĀʾishah '
    'recited the three sūrahs over his hands in his final illness, '
    '<em>«وَتُوُفِّيَ ﷺ فِي مَرَضِهِ ذَلِك؛ لِأَنَّ اللهَ سُبْحَانَهُ لَمْ '
    'يُرِدْ شِفَاءَهُ مِنْ ذَلِكَ المَرَض.»</em> <strong>A ruqyah that does not '
    'heal is not a failed ruqyah. It is a decree.</strong>')

b += B.nav('nq-l12-hukm-al-sahir.html',
           'النَّاقِضُ السَّابِع · part 2',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l13')

B.write('nq-l13-al-nushrah-wa-al-ilaj.html',
        'النَّاقِضُ السَّابِع · العِلَاجُ وَالنُّشْرَة',
        'The Seventh Nullifier, Part 3 — The Harm and the Remedy',
        'The close of the seventh nullifier, from the words of Shaykh Ibn Bāz: '
        'the magic of Labīd ibn al-Aʿṣam and exactly what it did and did not '
        'touch; the six objections to the ḥadīth answered one by one, including '
        'the false claim that Hishām ibn ʿUrwah was mukhtaliṭ and the claim that '
        'solitary reports are not taken in belief; what «and Allah will protect '
        'you from the people» actually guarantees; compelling the magician to '
        'undo his magic before he is executed, and ʿUthmān’s anger at a sentence '
        'carried out without his command; al-nushrah and its three grounds of '
        'prohibition; the necessity argument dismantled with Ibn Taymiyyah’s '
        'five reasons and the condition inside the qāʿidah; why a recitation '
        'that does not heal is no excuse, proved from the Prophet’s ﷺ own final '
        'illness; the finding that «afalā tanashsharta» is an insertion; the '
        'bewitched against the insane; and Hārūt and Mārūt, with the stories of '
        'al-Zuhrah refused.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ الثَّالِثَ عَشَر', '6', b)
print('wrote nq-l13-al-nushrah-wa-al-ilaj.html')
