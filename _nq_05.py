# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 5 — النَّاقِضُ الرَّابِع, part 1: تَفْضِيلُ غَيْرِ هُدَى النَّبِيِّ ﷺ.

Printed folios 108-119 (PDF indices 105-116, offset +3).

The fourth nullifier is the longest of the ten -- 28 folios, printed 108-135 --
and it splits where the book splits. Folios 108-119 establish the ruling: the
ijmāʿ, the man-made codes, تَوْحِيدُ الحُكْم, al-Nisāʾ 4:65, and the shumūl of
the dīn. Folios 120-135 are the **تَفْصِيل**: كُفْرٌ أَكْبَر against كُفْرٌ
أَصْغَر, Ibn ʿAbbās's «كُفْرٌ دُونَ كُفْر», the particular case decided for
kinship or a bribe, the rule «لَازِمُ الحُكْمِ لَيْسَ بِحُكْم», and الخُرُوج.
Part 2 (`_nq_06.py`) carries those.

**This page therefore says on its own face that the tafṣīl follows**, in a box
placed before any of the strong material, because publishing the first half of
this clause alone is the exact error the clause is most often made to serve.
Ibn Bāz's sharpest statements here are about systems and codes, not about named
persons, and nothing on this page licenses a ruling on a particular man or
state -- the sharḥ itself says what does, twelve folios later.

Rule 8 showcase: the ḥadīth of ʿAdī ibn Ḥātim «فَتِلْكَ عِبَادَتُهُمْ» carries
a full grading apparatus in the footnote -- Ibn Bāz twice, in two different
words; Ibn Taymiyyah; ʿAbd al-Raḥmān ibn Ḥasan; al-Shinqīṭī; and the ʿillah
named (Ghuṭayf ibn Aʿyan is weak, and the Ḥudhayfah shāhid is mawqūf with a
break). All of it is on the page, because that is what rule 8 is for.
And the غُرْبَة ḥadīth is quoted by Ibn Bāz here **with no attribution and no
grading**, so the page says exactly that and supplies none.
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
    'State the fourth nullifier’s two halves, and the %s Ibn Bāz reports on it.'
    % ar('إِجْمَاع'),
    'Say why man-made codes are not ranked against each other, from '
    '%s.' % ar('النِّسَاء ٤:٦٠–٦١'),
    'Show that %s is part of what %s requires — from '
    '%s and %s.' % (ar('تَوْحِيدُ الحُكْم'), ar('لَا إِلَهَ إِلَّا اللهُ'),
                    ar('النَّحْل ١٦:٣٦'), ar('الأَعْرَاف ٧:٥٤')),
    'Give the three things %s demands, and what the footnote says about the '
    '%s it negates.' % (ar('النِّسَاء ٤:٦٥'), ar('إِيمَان')),
    'State the precision Ibn Bāz adds about one who <em>believes Allah’s rulings '
    'are better</em> and still permits man-made systems to replace them.',
    'Grade the ḥadīth of ʿAdī ibn Ḥātim as the sharḥ grades it — and say what the '
    'sharḥ supplies for the ḥadīth of %s.' % ar('الغُرْبَة'),
])

b += B.provenance(108, 119)

b += B.matn(
    'الرَّابِع: مَنِ اعْتَقَدَ أَنَّ غَيْرَ هُدَى النَّبِيِّ ﷺ أَكْمَلُ مِنْ '
    'هُدَاهُ، أَوْ أَنَّ حُكْمَ غَيْرِهِ أَحْسَنُ مِنْ حُكْمِهِ — كَالَّذِينَ '
    'يُفَضِّلُونَ حُكْمَ الطَّوَاغِيتِ عَلَى حُكْمِهِ — فَهُوَ كَافِرٌ.',
    'Two halves: a belief about guidance, and a belief about judgement. Note the '
    'verb in both — اعْتَقَدَ, يُفَضِّلُونَ. The clause is written about a '
    'preference held, not only about an act done.')

b += B.prose(
    '<strong>This is the longest of the ten — twenty-eight folios — and it is '
    'also the one most often made to serve an argument its author did not '
    'make.</strong> So read the clause’s own verbs first: %s, %s. It is written '
    'about <em>a preference held in the heart</em>.'
    % (ar('اعْتَقَدَ'), ar('يُفَضِّلُونَ')))

b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><strong>This clause has a '
        '%s, and it is not on this page.</strong></p>'
        '<p style="margin:0 0 .5rem;font-size:.93rem">The sharḥ gives twelve '
        'folios to establishing the ruling (108–119, which this lesson covers) '
        'and then <strong>sixteen folios to the detail</strong> (120–135): '
        '%s against %s, Ibn ʿAbbās’s %s, the judge who decides one case for '
        'kinship or a bribe, the rule %s, and the ruling on %s.</p>'
        '<p style="margin:0;font-size:.93rem"><strong>Nothing on this page '
        'licenses a ruling about a particular man or a particular state.</strong> '
        'Ibn Bāz’s sharpest words here are about <em>codes and systems</em>. What '
        'follows for an individual is decided by the detail — <em>and the sharḥ '
        'itself decides it twelve folios later</em>, which is '
        '<strong>part 2</strong>.</p>'
        % (ar('تَفْصِيل'), ar('كُفْرٌ أَكْبَر'), ar('كُفْرٌ أَصْغَر'),
           '«' + ar('كُفْرٌ دُونَ كُفْر') + '»',
           '«' + ar('لَازِمُ الحُكْمِ لَيْسَ بِحُكْم') + '»', ar('الخُرُوج')),
        wash='var(--accent-wash)', edge='var(--accent)'))

# ---------------------------------------------------------------- the ijma'
b += B.heading('الإِجْمَاع', 'What Exactly the Consensus Is On')
b += B.sharh(
    p('Ibn Bāz states it in one sentence, and the wording is narrow on purpose:') +
    box('<p style="margin:0;font-size:.94rem"><em>«<strong>The scholars have '
        'agreed</strong> that whoever <strong>claims that the judgement of other '
        'than Allah is better than the judgement of Allah</strong>, or '
        '<strong>that the guidance of other than the Messenger ﷺ is better than '
        'the guidance of the Messenger ﷺ</strong> — <strong>he is a '
        'disbeliever</strong>.»</em></p>') +
    p('<strong>Read what the ijmāʿ is reported on.</strong> It is on the man who '
      '<em>claims a superiority</em> — %s. It is not reported, in this sentence, '
      'on every ruling given by other than Allah’s law. That distinction is the '
      'hinge the whole twenty-eight folios turn on, <em>and the sharḥ is careful '
      'with it from its first line.</em>' % ar('زَعَمَ')))

# ---------------------------------------------------------------- man-made codes
b += B.heading('القَوَانِينُ الوَضْعِيَّة', 'Why the Codes Are Not Ranked')
b += B.sharh(
    p('On laws laid down by men with no reliance on the Book and the Sunnah:') +
    box('<p style="margin:0;font-size:.94rem"><em>«They are all of them the '
        'laying-down of human beings, and it is not permitted for the people of '
        'Islam to seek judgement from them — <strong>and none of them is more '
        'worthy of being judged by than another</strong>, because they are all '
        'of them from the judgement of the Jāhiliyyah, and from the judgement of '
        'the ṭāghūt which Allah warned against, and <strong>attributed to the '
        'hypocrites the desire to seek judgement from it</strong>.»</em></p>') +
    p('<strong>«None of them is more worthy than another» is a refusal to enter '
      'the comparison at all.</strong> The question «which code is best?» is not '
      'answered on the merits and then decided for the sharīʿah; <em>it is '
      'declined, because the sharīʿah is not a competitor in that field.</em> And '
      'note where he locates the <em>desire</em> to arbitrate elsewhere — the '
      'Qurʾān attributes it to the munāfiqūn, and he is quoting the verse that '
      'does so.'))
b += B.ayah(
    'أَلَمْ تَرَ إِلَى الَّذِينَ يَزْعُمُونَ أَنَّهُمْ آمَنُوا بِمَا أُنزِلَ '
    'إِلَيْكَ وَمَا أُنزِلَ مِن قَبْلِكَ يُرِيدُونَ أَن يَتَحَاكَمُوا إِلَى '
    'الطَّاغُوتِ وَقَدْ أُمِرُوا أَن يَكْفُرُوا بِهِ وَيُرِيدُ الشَّيْطَانُ أَن '
    'يُضِلَّهُمْ ضَلَالًا بَعِيدًا',
    'Have you not seen those who claim to have believed in what was sent down to '
    'you and what was sent down before you — they wish to refer judgement to the '
    'ṭāghūt, while they were commanded to disbelieve in it; and Satan wishes to '
    'lead them far astray.',
    'سُورَةُ النِّسَاء · 4:60')
b += B.prose(
    '<strong>%s</strong> — <em>while they were commanded to disbelieve in '
    'it.</em> The verse does not merely forbid arbitrating to the ṭāghūt; it says '
    'disbelieving in it was <em>already</em> an order. <em>Which is why this '
    'clause sits in a treatise on tawḥīd and not in a chapter on politics.</em> '
    'And the next verse names what they do when called to Allah’s revelation: %s '
    '— <em>you see the hypocrites turning away in aversion.</em>'
    % (ar('وَقَدْ أُمِرُوا أَن يَكْفُرُوا بِهِ'), ar('النِّسَاء ٤:٦١')))
b += B.sharh(
    p('He then puts the Qurʾān’s own question beside it — <em>«and every ruling '
      'that contradicts the legislation of Allah is from the judgement of the '
      'Jāhiliyyah»</em>:'))
b += B.ayah(
    'أَفَحُكْمَ الجَاهِلِيَّةِ يَبْغُونَ وَمَنْ أَحْسَنُ مِنَ اللَّهِ حُكْمًا '
    'لِّقَوْمٍ يُوقِنُونَ',
    'Is it the judgement of the Jāhiliyyah that they seek? And who is better than '
    'Allah in judgement, for a people who are certain?',
    'سُورَةُ المَائِدَة · 5:50')
b += B.prose(
    'Note the last three words, which are easy to read past: %s — <em>for a '
    'people who are certain.</em> <strong>The verse ties the recognition to '
    'yaqīn.</strong> It is not arguing that Allah’s judgement will look best to '
    'anyone; <em>it is saying who it looks best to.</em> And Ibn Bāz adds that '
    'Allah <em>«informed us that judging by other than what Allah sent down is '
    '%s, %s and %s»</em> — the three words of %s — and that these verses '
    '<em>«oblige the Muslims to beware of it, to disown it, and to hasten to the '
    'judgement of Allah and His Messenger, with an expansion of the chest to it '
    'and submission to it.»</em>'
    % (ar('لِّقَوْمٍ يُوقِنُونَ'), ar('كُفْرٌ'), ar('ظُلْمٌ'), ar('فِسْقٌ'),
       ar('المَائِدَة ٥:٤٤، ٤٥، ٤٧')))

# ---------------------------------------------------------------- tawhid al-hukm
b += B.heading('تَوْحِيدُ الحُكْم', 'Judgement Belongs to the One Who Creates')
b += B.sharh(
    p('The argument that makes this a creedal matter rather than a legal one is '
      'built from two verses. First, the mission of <strong>every</strong> '
      'messenger:'))
b += B.ayah(
    'وَلَقَدْ بَعَثْنَا فِي كُلِّ أُمَّةٍ رَّسُولًا أَنِ اعْبُدُوا اللَّهَ '
    'وَاجْتَنِبُوا الطَّاغُوتَ',
    'And We certainly sent into every nation a messenger, [saying]: worship Allah '
    'and shun the ṭāghūt.',
    'سُورَةُ النَّحْل · 16:36')
b += B.sharh(
    p('<em>«So whoever submitted to Allah, obeyed Him and referred judgement to '
      'His revelation — he is the one who worships Him; and whoever submitted to '
      'other than Him and referred judgement to other than His law — '
      '<strong>he has worshipped the ṭāghūt</strong> and yielded to it… And '
      'servitude to Allah alone, and barāʾah from the worship of the ṭāghūt and '
      'from referring judgement to it, is <strong>from what the testimony that '
      'there is no deity but Allah requires</strong>.»</em>') +
    p('Then the second verse, and it is the one that makes the whole argument '
      'short:'))
b += B.ayah(
    'أَلَا لَهُ الخَلْقُ وَالأَمْرُ',
    'Unquestionably, His is the creation and the command.',
    'سُورَةُ الأَعْرَاف · 7:54')
b += B.prose(
    '<em>«So just as He alone is the Creator, He alone is the One who commands — '
    'and what is obligatory is obedience to His command.»</em> '
    '<strong>%s and %s are placed in one sentence by the Qurʾān.</strong> A man '
    'who grants the first and withholds the second has divided a verse. <em>That '
    'is the whole of تَوْحِيدُ الحُكْم, and it is why the fourth nullifier is a '
    'nullifier at all and not merely a sin.</em>'
    % (ar('الخَلْق'), ar('الأَمْر')))

b += B.sharh(
    p('And Ibn Bāz shows that this was the actual mechanism of the ahl al-kitāb’s '
      'shirk — not statues, but <strong>obedience in making lawful and '
      'unlawful</strong>:') +
    p('<em>«And Allah has related of the Jews and the Christians that they took '
      'their rabbis and their monks as lords besides Allah — <strong>when they '
      'obeyed them in making the forbidden lawful and the lawful '
      'forbidden.</strong>»</em>'))
b += B.ayah(
    'اتَّخَذُوا أَحْبَارَهُمْ وَرُهْبَانَهُمْ أَرْبَابًا مِّن دُونِ اللَّهِ '
    'وَالمَسِيحَ ابْنَ مَرْيَمَ وَمَا أُمِرُوا إِلَّا لِيَعْبُدُوا إِلَهًا '
    'وَاحِدًا لَّا إِلَهَ إِلَّا هُوَ سُبْحَانَهُ عَمَّا يُشْرِكُونَ',
    'They took their rabbis and their monks as lords besides Allah, and the '
    'Messiah son of Maryam — while they were not commanded except to worship one '
    'God. There is no deity except Him; exalted is He above what they associate.',
    'سُورَةُ التَّوْبَة · 9:31')
b += B.sharh(
    p('<strong>ابْنُ كَثِير</strong>, whom the sharḥ quotes from his tafsīr on '
      'this verse, draws out the definition: the One God is '
      '<em>«the One who, when He forbids a thing, it is the forbidden; and what '
      'He makes lawful is the lawful; and what He legislates is followed; and '
      'what He rules by is carried out.»</em>') +
    p('<strong>And then the ḥadīth that stopped a Companion’s own objection.</strong> '
      '<strong>عَدِيُّ بْنُ حَاتِم</strong> had been a Christian before his '
      'Islam. He heard the Prophet ﷺ recite this verse and said: <em>O Messenger '
      'of Allah, we did not worship them</em> — understanding worship to mean '
      'slaughtering, vowing, prostration and bowing. The answer reframed the word '
      'for him:'))
b += B.hadith(
    'أَلَيْسَ يُحَرِّمُونَ مَا أَحَلَّ اللهُ فَتُحَرِّمُونَهُ، وَيُحِلُّونَ مَا '
    'حَرَّمَ فَتُحِلُّونَهُ؟ قَالَ: بَلَى. قَالَ: فَتِلْكَ عِبَادَتُهُمْ',
    '“Did they not forbid what Allah had made lawful, and you forbade it; and '
    'make lawful what He had forbidden, and you made it lawful?” He said: yes. '
    'He ﷺ said: <strong>“then that is your worship of them.”</strong>',
    'رَوَاهُ أَحْمَدُ وَالتِّرْمِذِيُّ — gradings below')
b += B.sharh(
    p('<strong>This ḥadīth is the reason the clause is about worship, so its '
      'grading matters, and the sharḥ gives it in full rather than in a word. '
      'Here is everything it says:</strong>') +
    table([
        row('ابْنُ بَاز', 'in <em>Sharḥ Fatḥ al-Majīd</em>: '
            '<em>«it is of the category of %s»</em>' % ar('الحَسَن')),
        row('ابْنُ بَاز (elsewhere)',
            '<em>«there is weakness in it, <strong>but it is well '
            'known</strong>»</em>'),
        row('ابْنُ بَاز (a third time)',
            '<em>«this ḥadīth, even though in its route is '
            '<strong>غُطَيْفُ بْنُ أَعْيَن, and he is weak</strong>, is '
            'supported by the athar of <strong>حُذَيْفَة</strong> and by what has '
            'come in that meaning from others than Ḥudhayfah among the righteous '
            'Salaf»</em>'),
        row('ابْنُ تَيْمِيَّة', 'graded it %s (<em>al-Fatāwā</em>, and '
            '<em>Minhāj al-Sunnah</em>)' % ar('حَسَن')),
        row('عَبْدُ الرَّحْمَنِ بْنُ حَسَن',
            'graded it %s, in <em>Fatḥ al-Majīd</em>' % ar('صَحِيح')),
        row('الشِّنْقِيطِيّ', 'graded it %s, in <em>al-ʿAdhb al-Namīr</em>'
            % ar('صَحِيح')),
        row('the %s named' % ar('عِلَّة'),
            'al-Tirmidhī and a group narrate it through '
            '<strong>Ghuṭayf ibn Aʿyan</strong> ← Muṣʿab ibn Saʿd ← ʿAdī, '
            '<em>and Ghuṭayf is weak</em>; its shāhid from Ḥudhayfah is '
            '<strong>mawqūf</strong>, through Ḥabīb ibn Abī Thābit ← Abū '
            'al-Bukhtarī ← Ḥudhayfah — <em>and Abū al-Bukhtarī did not hear from '
            'Ḥudhayfah</em>'),
    ]) +
    p('<strong>That is what an honest grading looks like.</strong> A weak '
      'narrator, named; a supporting athar, named, with <em>its own</em> defect '
      'named; four scholars raising it to ḥasan or ṣaḥīḥ on the strength of the '
      'support; and Ibn Bāz himself phrasing it three different ways in three '
      'places. <em>Nothing here is tidied.</em>'))

# ---------------------------------------------------------------- 4:65
b += B.heading('فَلَا وَرَبِّكَ', 'An Oath, and Three Conditions')
b += B.prose(
    'This is the verse Ibn Bāz returns to more than any other in the clause — '
    'he quotes it at least five separate times across these folios. '
    '<em>«Allah swore an oath in this noble verse that the slaves do not believe '
    'until they make the Messenger ﷺ the judge in what arises between them.»</em>')
b += B.ayah(
    'فَلَا وَرَبِّكَ لَا يُؤْمِنُونَ حَتَّى يُحَكِّمُوكَ فِيمَا شَجَرَ '
    'بَيْنَهُمْ ثُمَّ لَا يَجِدُوا فِي أَنفُسِهِمْ حَرَجًا مِّمَّا قَضَيْتَ '
    'وَيُسَلِّمُوا تَسْلِيمًا',
    'But no, by your Lord, they will not believe until they make you the judge in '
    'what arises between them, and then find within themselves no discomfort over '
    'what you have decided, and submit in full submission.',
    'سُورَةُ النِّسَاء · 4:65')
b += table([
    row(ar('حَتَّى يُحَكِّمُوكَ'),
        'that they <strong>bring it to him</strong> — in his lifetime to him '
        'himself, <em>and after his death to his Sunnah</em>'),
    row(ar('لَا يَجِدُوا فِي أَنفُسِهِمْ حَرَجًا'),
        'that <strong>no constriction remains in the chest</strong> at what he '
        'decided — <em>an inward condition, not an outward one</em>'),
    row(ar('وَيُسَلِّمُوا تَسْلِيمًا'),
        'that they <strong>submit a complete submission</strong> — '
        '<em>«contentment with the judgement of Allah and tranquillity in '
        'it»</em>'),
])
b += B.sharh(
    p('Three things, and the second two are of the heart. <em>«So referring '
      'judgement to his Sunnah is referring judgement to what was sent down of '
      'the Qurʾān and the Sunnah»</em> — and Ibn Bāz insists the verse is '
      '<strong>%s</strong>, general upon its apparent meaning: <em>«it is not '
      'permitted for the Muslims to depart from the legislation of Allah; rather '
      'it is obligatory upon them to judge by the law of Allah '
      '<strong>in everything</strong> — in what pertains to the acts of worship, '
      'and in what pertains to dealings, and in all affairs of religion and of '
      'the world.»</em>' % ar('عَامَّةٌ عَلَى ظَاهِرِهَا')) +
    p('And he reads %s widely too: <em>«meaning the people, from the Muslims and '
      'others»</em>; and %s as <em>«in what they disputed over»</em> — whether '
      'between a state and another, a group and another, or <strong>one Muslim '
      'and his brother</strong>: <em>«the ruling in all of that is the '
      'same.»</em>' % ('«' + ar('لَا يُؤْمِنُونَ') + '»',
                       '«' + ar('فِيمَا شَجَرَ بَيْنَهُمْ') + '»')) +
    box('<p style="margin:0;font-size:.94rem">And the sharḥ’s footnote closes the '
        'escape that is usually taken here: <strong>«the %s negated in this '
        'place is the <em>root</em> of īmān, not merely its '
        'completeness»</strong> — and it gives the reason from the verse itself: '
        '<em>by the evidence of what comes after it.</em></p>'
        % ar('إِيمَان')) +
    p('<em>That footnote is doing real work.</em> «They will not believe» is '
      'frequently softened into «their faith will not be complete». The sharḥ '
      'declines the softening <strong>and shows its working</strong> — the verse '
      'goes on to make submission itself the condition, which a man of deficient '
      'but real faith would already have.'))

# ---------------------------------------------------------------- the shahadah
b += B.heading('الشَّهَادَةُ الثَّانِيَة', 'What “Muḥammad Is the Messenger of Allah” Commits You To')
b += B.sharh(
    p('He turns the clause onto the second half of the kalimah — and this is the '
      'same move the third nullifier made with the first half:') +
    box('<p style="margin:0;font-size:.94rem"><em>«Likewise, “I bear witness that '
        'Muḥammad is the Messenger of Allah” <strong>does not benefit the one who '
        'says it</strong> if he does not make the Messenger ﷺ the judge, and does '
        'not yield to his judgement and his law, and does not magnify his command '
        'and his prohibition… <strong>the testimony benefits only the one who '
        'acts by it.</strong>»</em></p>') +
    p('And he gives the shape of the self-contradiction plainly: a man who says '
      '<em>«I bear witness that there is no deity but Allah and that Muḥammad is '
      'the Messenger of Allah, and judging by the law of Allah is obligatory, and '
      'obligatory, and obligatory» — and then breaks this and does not do it — '
      '<strong>this testimony will not avail him</strong></em>; just as it will '
      'not avail the one who says it and then reviles Allah.'))

b += B.prose(
    '<strong>And here is the precision that most changes how the clause is '
    'read.</strong> It is easy to assume the nullifier requires a man to think '
    'man-made law <em>superior</em>. Ibn Bāz closes that door:')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><em>«And there is no %s for one who '
        'believes that the rulings of people and their opinions are '
        '<strong>better</strong> than the ruling of Allah and His Messenger, '
        '<strong>or equal and similar to it</strong>, <strong>or who permits that '
        'man-made rulings and human systems take its place</strong> — '
        '<strong><em>even if he believes that the rulings of Allah are better, '
        'more complete and more just.</em></strong>»</em></p>'
        % ar('إِيمَان'),
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('<strong>Three separate things, then, and only the first is about '
      'superiority:</strong> holding the man-made better; holding it '
      '<em>equal</em>; or <em>permitting it to take the sharīʿah’s place</em> '
      'while privately granting that Allah’s law is better. <em>The third is the '
      'one a man is most likely to think safe, and it is named explicitly.</em>') +
    p('And in another place he adds a fourth wording and a further point: '
      '<em>«or that it is <strong>more suitable for society and more '
      'accommodating to society</strong> than the ruling of Allah, or that it is '
      'better than the ruling of Allah — <strong>all of this is apostasy from '
      'Islam, even if he did not act upon it</strong>»</em>; and in a third '
      'place, of one who preferred the codes over the law: '
      '<em>«this one’s disbelief is apparent.»</em> <strong>The belief alone, '
      'unacted upon, is what the clause names</strong> — which is consistent with '
      'its verb, %s.' % ar('اعْتَقَدَ')))

# ---------------------------------------------------------------- shumul
b += B.heading('شُمُولُ الدِّين', 'A Religion That Does Not Divide')
b += B.sharh(
    p('Why there is no portion of life left over, in his own words:') +
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><em>«The religion of Allah '
        'is a <strong>comprehensive</strong> religion — it takes in the interests '
        'of the slaves in this life and the next… <strong>so it is worship and '
        'leadership</strong>: the believer is a worshipper and is a commander of '
        'the army; <strong>worship and judgement</strong> — he is a worshipper '
        'praying and fasting, and a ruler judging by the law of Allah carrying '
        'out its rulings; <strong>worship and jihād</strong>… '
        '<strong>a muṣḥaf and a sword</strong>.»</em></p>') +
    p('And the consequence he draws from it is the sentence to keep: '
      '<em>«<strong>He is not a worshipper of Allah who submitted to his Lord in '
      'some sides of his life and submitted to created beings in other '
      'sides.</strong>»</em> <em>Which is simply al-Nisāʾ 4:65 again, read as a '
      'statement about a man rather than about a court.</em>') +
    p('He also gives the comparison that fixes the priority: '
      '<em>«the people’s need for the ruling of the Sharīʿah is '
      '<strong>greater and more severe than their need for food and '
      'drink</strong> — because the utmost of their affair, if food and drink '
      'fail them, is that they die, and death is inevitable; but whoever loses '
      'the Sharīʿah and turns away from it and follows other than it, his end is '
      'everlasting punishment.»</em>'))

b += B.heading('لِمَاذَا أُرْسِلَ', 'What the Messenger ﷺ Was Sent to Replace')
b += B.sharh(
    p('The positive statement of the clause, which is usually left out of it '
      'altogether — <em>what the law is for</em>:') +
    p('<em>«Allah sent Muḥammad ﷺ to <strong>put an end to the corrupt systems in '
      'human society</strong>, and the deviant morals, and the oppression and '
      'injustice, and <strong>to put in their place sound systems and just '
      'rulings</strong>… to remove what is in the earth of oppression and '
      'tyranny… and to displace the corrupt systems and the <strong>despotic '
      'ṭawāghīt who rule over people by falsehood, and wrong them, and transgress '
      'against their rights, and enslave them</strong>.»</em>') +
    box('<p style="margin:0;font-size:.94rem">And what replaces them: '
        '<em>«leaders who are reformers, and just, upright systems, and wise and '
        'just legislations, which <strong>stop people at their limit, and do not '
        'distinguish between white and black</strong>, nor between red and other, '
        '<strong>nor between rich and poor</strong>, nor between one noble in '
        'people’s eyes and one lowly in their eyes; rather He made His law '
        '<strong>not distinguish between people</strong> — rather it directs them '
        'all, and commands them all, and forbids them all.»</em></p>') +
    p('<strong>That is the argument of the clause stated as a claim about justice '
      'rather than as a threat</strong>, and it belongs on the page as much as '
      'the ruling does. The objection to man-made codes is not that they are '
      'foreign; <em>it is that a law written by men who are subject to it will '
      'bend for the rich and the well-born, and this one does not.</em>'))

# ---------------------------------------------------------------- ghurbah
b += B.heading('الغُرْبَة وَالشَّبَاب', 'Strangeness, and a Word About the Young')
b += B.sharh(
    p('Ibn Bāz quotes here a ḥadīth about the strangeness of Islam returning, and '
      'the «strangers» being <em>«those who set right when the people have become '
      'corrupt»</em>, and in the other wording <em>«who set right what the people '
      'have corrupted of my Sunnah»</em>. '
      '<strong>The sharḥ gives this one neither an attribution nor a grading at '
      'this place, so this page supplies none</strong> — it is recorded here as '
      'what he said, and no more than that.') +
    p('What he does with it is the point: <em>«the claim of Islam is not strange '
      '— the claims are many; but a strangeness in reality: '
      '<strong>in implementing the Sharīʿah, and carrying out the command of '
      'Allah, and truthfulness in that</strong>. This is the strange thing.»</em>') +
    box('<p style="margin:0;font-size:.94rem"><strong>And then, immediately, the '
        'restraint on the strangers themselves</strong> — those who rise to set '
        'things right must do so <em>«<strong>beginning with setting themselves '
        'right</strong>, by striving against their own souls, and that they be '
        'upon <strong>insight and knowledge and guidance — not upon ignorance '
        'and misguidance</strong>; and that they <strong>seek the help of their '
        'scholars and their elders and consult with them</strong>.»</em></p>') +
    p('<em>Insight before action, and the scholars consulted first.</em> That is '
      'inside the same paragraph as the strongest language on these folios, and '
      'it is the sharḥ putting its own fence up before part 2 arrives.'))
b += B.sharh(
    p('He adds an encouragement from Ibrāhīm عَلَيْهِ السَّلَام, which is worth '
      'keeping for its own sake: <em>«one man, there was none other than him on '
      'the earth</em> [upon tawḥīd]<em>… and the people were all upon disbelief '
      'and misguidance — and even so <strong>he did not stop</strong> from jihād '
      'and calling to Allah, until he went out against their idols and broke them '
      'and smashed them to pieces… <strong>this shows that strength and vigour '
      'and high resolve make a man undertake great works which a great multitude '
      'of weak resolve do not undertake.</strong>»</em>') +
    p('And on the young who ask for the Sharīʿah, a judgement that is his own and '
      'is often not quoted: <em>«many of the rulers fear the young, because the '
      'young’s offence is that <strong>they demand the law of Allah and call to '
      'the law of Allah</strong>… and <strong>this is a good demand from the '
      'righteous youth, for which they are to be thanked</strong>; so the leaders '
      'ought to <strong>help them upon good, and guide them to what is correct if '
      'they err</strong>, and cultivate in them Islamic zeal and the strength of '
      'faith… and if a foot slips, or an error is found from them, '
      '<strong>they are directed to good</strong>.»</em>') +
    p('<em>The demand is legitimate; the correction of those who overreach in it '
      'is by teaching them.</em> Hold that sentence, because it is the bridge '
      'into part 2.'))

b += B.prose(
    'The hardest words on these folios are in the same passage — that where '
    'leaders <em>«deviate and leave the truth and hold to falsehood»</em> there '
    'is then <em>«no recourse but to strive against them»</em>, and that states '
    'called Islamic are <em>«themselves in need of being taken by the hand until '
    'they judge by the law of Allah»</em>. <strong>What that does and does not '
    'license is decided by the sharḥ’s own تَفْصِيل, at folios 120–131 — the '
    'akbar/aṣghar distinction, Ibn ʿAbbās’s «kufr short of kufr», and the ruling '
    'on الخُرُوج.</strong> <em>They are part 2, and this clause is not finished '
    'without them.</em>')

# ---------------------------------------------------------------- vocab
b += B.vocab([
    ('تَوْحِيدُ الحُكْم', 'tawḥīd al-ḥukm', 'singling Allah out in judgement',
     'That judgement belongs to Allah as creation does — from «أَلَا لَهُ '
     'الخَلْقُ وَالأَمْرُ» (7:54). Granting Him the creation and withholding the '
     'command divides a single verse.'),
    ('الطَّاغُوت', 'al-ṭāghūt', 'that which is transgressively obeyed',
     'In this clause: a law or authority referred to for judgement in place of '
     'Allah’s. Every messenger was sent with «worship Allah and shun the '
     'ṭāghūt» (16:36).'),
    ('التَّحَاكُم', 'al-taḥākum', 'referring judgement to',
     'Seeking a verdict from a source. al-Nisāʾ 4:60 attributes the *desire* for '
     'it elsewhere to the munāfiqūn, and notes they had already been commanded to '
     'disbelieve in that source.'),
    ('القَوَانِينُ الوَضْعِيَّة', 'al-qawānīn al-waḍʿiyyah', 'man-made codes',
     'Laws laid down by men with no reliance on the Book and Sunnah. Ibn Bāz: '
     '«none of them is more worthy of being judged by than another» — the '
     'comparison is declined, not won.'),
    ('فِيمَا شَجَرَ بَيْنَهُمْ', 'fīmā shajara baynahum', 'in what arose between them',
     'From 4:65. Ibn Bāz reads it of every dispute — between states, between '
     'groups, and between one Muslim and his brother: «the ruling in all of that '
     'is the same».'),
    ('حَرَجٌ', 'ḥaraj', 'constriction of the chest',
     'The second condition of 4:65, and an inward one: that no discomfort remain '
     'at what he ﷺ decided. The third is تَسْلِيم, complete submission.'),
    ('عَامَّةٌ عَلَى ظَاهِرِهَا', 'ʿāmmah ʿalā ẓāhirihā', 'general upon its apparent meaning',
     'His ruling on 4:65 — it is not restricted to a class of disputes; it covers '
     'acts of worship, dealings, and all affairs of religion and world.'),
    ('شُمُولٌ', 'shumūl', 'comprehensiveness',
     'That the dīn takes in both lives: «worship and leadership, worship and '
     'judgement, worship and jihād — a muṣḥaf and a sword». So no portion of '
     'life is left to be governed by something else.'),
    ('غُطَيْفُ بْنُ أَعْيَن', 'Ghuṭayf ibn Aʿyan', 'a weak narrator, named',
     'The weakness in the chain of «فَتِلْكَ عِبَادَتُهُمْ». The sharḥ names him, '
     'names the mawqūf shāhid of Ḥudhayfah and its own break, and then gives four '
     'scholars’ gradings — an example of how a grading should be reported.'),
])

# ---------------------------------------------------------------- mcq
b += B.mcq('nq-l05-mcq', [
    ('What two beliefs does the fourth nullifier name?',
     ['Ruling by other than Allah’s law, and taking a bribe for it',
      'That other than the Prophet’s ﷺ guidance is more complete than his, or '
      'that another’s judgement is better than his',
      'Abandoning the prayer, and denying its obligation',
      'Mocking the Sharīʿah, and praising the disbelievers'], 1),
    ('What is significant about the clause’s verbs, اعْتَقَدَ and يُفَضِّلُونَ?',
     ['They indicate a repeated action',
      'They make the clause about a preference held in the heart, not only about '
      'an act done',
      'They restrict the clause to rulers',
      'They show the clause is figurative'], 1),
    ('Exactly what does Ibn Bāz report the ijmāʿ upon?',
     ['Upon every ruling given by other than Allah’s law',
      'Upon the one who CLAIMS that the judgement of other than Allah is better, '
      'or that the guidance of other than the Messenger ﷺ is better',
      'Upon anyone who works for a state with man-made codes',
      'Upon those who doubt the Sharīʿah’s suitability'], 1),
    ('Why does Ibn Bāz say that no man-made code is more worthy of arbitration '
     'than another?',
     ['Because they are all equally well drafted',
      'Because they are all from the judgement of the Jāhiliyyah — so the '
      'comparison is declined rather than won on the merits',
      'Because none of them has been translated into Arabic',
      'Because the scholars have not examined them'], 1),
    ('What does al-Nisāʾ 4:60 say the people referring judgement to the ṭāghūt '
     'had ALREADY been commanded?',
     ['To consult the scholars first',
      'To disbelieve in it — «وَقَدْ أُمِرُوا أَن يَكْفُرُوا بِهِ»',
      'To seek a second opinion',
      'To emigrate'], 1),
    ('Whom does the Qurʾān attribute the desire to arbitrate to the ṭāghūt?',
     ['The idolaters of Quraysh',
      'The hypocrites — and the next verse shows them turning away when called to '
      'what Allah sent down',
      'The People of the Book',
      'The Bedouin'], 1),
    ('What do the last words of al-Māʾidah 5:50, «لِّقَوْمٍ يُوقِنُونَ», add?',
     ['That the verse applies only to the certain among the scholars',
      'That the verse ties recognising Allah’s judgement as best to yaqīn — it '
      'says who it looks best to',
      'That certainty is a condition for the ruling to be binding',
      'That the ruling is suspended in cases of doubt'], 1),
    ('How does «أَلَا لَهُ الخَلْقُ وَالأَمْرُ» (7:54) make this a creedal matter?',
     ['By proving Allah’s existence',
      'By placing creation and command in one sentence — so granting Him the '
      'first while withholding the second divides a single verse',
      'By mentioning the Throne',
      'By listing the sun and moon'], 1),
    ('What was the mechanism of the ahl al-kitāb’s shirk in al-Tawbah 9:31?',
     ['Worshipping statues of their rabbis',
      'Obeying their rabbis and monks in making the forbidden lawful and the '
      'lawful forbidden',
      'Praying towards their monasteries',
      'Swearing oaths by their monks'], 1),
    ('What had ʿAdī ibn Ḥātim assumed «worship» meant, before the Prophet ﷺ '
     'corrected him?',
     ['Love and loyalty',
      'Slaughtering, vowing, prostration and bowing only',
      'Prayer and fasting',
      'Pilgrimage to their churches'], 1),
    ('How does the sharḥ grade the ḥadīth «فَتِلْكَ عِبَادَتُهُمْ»?',
     ['Ṣaḥīḥ without any discussion',
      'Weak in its route through Ghuṭayf ibn Aʿyan but supported — Ibn Bāz calls '
      'it ḥasan and elsewhere says there is weakness in it though it is well '
      'known; Ibn Taymiyyah ḥasan; ʿAbd al-Raḥmān ibn Ḥasan and al-Shinqīṭī '
      'ṣaḥīḥ',
      'Fabricated',
      'The sharḥ gives no grading at all'], 1),
    ('What defect does the sharḥ name in the SUPPORTING report of Ḥudhayfah?',
     ['That Ḥudhayfah retracted it',
      'That it is mawqūf, and Abū al-Bukhtarī did not hear from Ḥudhayfah',
      'That its wording contradicts the Qurʾān',
      'That it is known only from one route in Ibn Mājah'], 1),
    ('What three things does al-Nisāʾ 4:65 require?',
     ['Belief, prayer and zakāh',
      'That they make him ﷺ the judge; that no constriction remain in their '
      'chests at what he decided; and that they submit a complete submission',
      'That they emigrate, fight and spend',
      'That they consult, agree and record'], 1),
    ('After the Prophet’s ﷺ death, what does «حَتَّى يُحَكِّمُوكَ» mean in '
     'practice?',
     ['That judgement passes to the consensus of the rulers',
      'Referring judgement to his Sunnah — which is referring judgement to what '
      'was sent down of the Qurʾān and the Sunnah',
      'That the verse no longer applies',
      'Referring judgement to the four imāms'], 1),
    ('What does the sharḥ’s footnote say about the īmān negated in 4:65?',
     ['That it is the completeness of faith only',
      'That it is the ROOT of faith, not merely its completeness — by the '
      'evidence of what comes after it in the verse',
      'That it refers to the faith of the hypocrites specifically',
      'That the negation is rhetorical'], 1),
    ('How widely does Ibn Bāz read «فِيمَا شَجَرَ بَيْنَهُمْ»?',
     ['Of disputes between states only',
      'Of every dispute — between a state and another, a group and another, or '
      'one Muslim and his brother: «the ruling in all of that is the same»',
      'Of disputes in acts of worship only',
      'Of disputes brought before a qāḍī only'], 1),
    ('Which THREE positions does Ibn Bāz say leave a man without īmān?',
     ['Only believing man-made law superior',
      'Believing it better; believing it EQUAL and similar; or permitting it to '
      'take the Sharīʿah’s place — even while believing Allah’s rulings are '
      'better, more complete and more just',
      'Believing it better, working under it, or paying its taxes',
      'Doubting it, studying it, or translating it'], 1),
    ('What does he say about one who holds man-made law «more suitable for '
     'society» than Allah’s ruling?',
     ['That it is a sin short of disbelief',
      'That all of this is apostasy from Islam — even if he did not act upon it',
      'That it depends on the society in question',
      'That it is permitted if he intends benefit'], 1),
    ('What does «أَشْهَدُ أَنَّ مُحَمَّدًا رَسُولُ اللهِ» commit a man to, per '
     'Ibn Bāz?',
     ['Reciting it in every prayer',
      'Making him ﷺ the judge, yielding to his judgement and law, and magnifying '
      'his command and prohibition — the testimony benefits only the one who acts '
      'by it',
      'Loving his family',
      'Visiting his grave'], 1),
    ('What does Ibn Bāz mean by «a muṣḥaf and a sword»?',
     ['That the Qurʾān was spread by conquest',
      'That the dīn is comprehensive — worship and leadership, worship and '
      'judgement, worship and jihād — so no side of life is governed by something '
      'else',
      'That two proofs are required for every ruling',
      'That the scholar must also be a soldier'], 1),
    ('What comparison does he use for the people’s need of the Sharīʿah?',
     ['That it is like their need for shelter',
      'That it is greater and more severe than their need for food and drink — '
      'since losing those ends in death, which is inevitable anyway',
      'That it is like a physician’s need for medicine',
      'That it is like the body’s need for sleep'], 1),
    ('What does the lesson identify as the positive argument of the clause?',
     ['That man-made codes are foreign impositions',
      'That a law written by men who are subject to it bends for the rich and the '
      'well-born — and the Sharīʿah «does not distinguish between people»',
      'That the Sharīʿah is older',
      'That the Sharīʿah is simpler to administer'], 1),
    ('What restraint does Ibn Bāz place on those who rise to «set things right»?',
     ['That they must obtain a licence from the ruler',
      'To begin by setting themselves right, to be upon insight and knowledge and '
      'guidance rather than ignorance, and to seek the help of their scholars and '
      'elders and consult them',
      'That they must act only in their own country',
      'That they must remain silent until unanimity is reached'], 1),
    ('What is his judgement on the young who demand the law of Allah?',
     ['That they should be restrained from speaking',
      'That it is a good demand for which they are to be thanked — and leaders '
      'ought to help them to good and guide them to what is correct if they err',
      'That they are to be declared innovators',
      'That their demand is premature until they are scholars'], 1),
    ('Why does this lesson state on its own page that the clause has a تَفْصِيل?',
     ['Because the sharḥ is incomplete',
      'Because the sharḥ gives sixteen further folios to the detail — akbar '
      'against aṣghar, «kufr short of kufr», and الخُرُوج — and the first half '
      'alone decides nothing about a particular man or state',
      'Because the scholars disagree about the matn’s wording',
      'Because the folios are out of order'], 1),
])

b += B.tf('nq-l05-tf', [
    ('نَقَلَ ابْنُ بَازٍ الإِجْمَاعَ عَلَى كُفْرِ مَنْ زَعَمَ أَنَّ حُكْمَ '
     'غَيْرِ اللهِ أَحْسَنُ مِنْ حُكْمِ اللهِ.',
     'Ibn Bāz reports the consensus on the disbelief of whoever claims that the '
     'judgement of other than Allah is better than Allah’s judgement.', True),
    ('بَعْضُ القَوَانِينِ الوَضْعِيَّةِ أَوْلَى بِالتَّحَاكُمِ إِلَيْهِ مِنْ '
     'بَعْضٍ.',
     'Some man-made codes are more worthy of being judged by than others.',
     False),
    ('الإِيمَانُ المَنْفِيُّ فِي «فَلَا وَرَبِّكَ لَا يُؤْمِنُونَ» هُوَ '
     'كَمَالُ الإِيمَانِ لَا أَصْلُهُ.',
     'The faith negated in «but no, by your Lord, they will not believe» is the '
     'completeness of faith, not its root.', False),
    ('مَنْ أَجَازَ أَنْ تَحِلَّ الأَنْظِمَةُ البَشَرِيَّةُ مَحَلَّ الشَّرِيعَةِ '
     'فَلَا إِيمَانَ لَهُ، وَلَوِ اعْتَقَدَ أَنَّ حُكْمَ اللهِ أَحْسَنُ.',
     'One who permits human systems to take the Sharīʿah’s place has no faith, '
     'even if he believes Allah’s ruling is better.', True),
    ('حَدِيثُ «فَتِلْكَ عِبَادَتُهُمْ» صَحِيحٌ بِلَا كَلَامٍ فِي إِسْنَادِهِ.',
     'The ḥadīth «then that is your worship of them» is ṣaḥīḥ with no discussion '
     'of its chain.', False),
    ('مُطَالَبَةُ الشَّبَابِ بِتَحْكِيمِ الشَّرِيعَةِ مَطْلَبٌ طَيِّبٌ '
     'يُشْكَرُونَ عَلَيْهِ عِنْدَ ابْنِ بَاز.',
     'The young’s demand that the Sharīʿah be implemented is, for Ibn Bāz, a good '
     'demand for which they are to be thanked.', True),
])

b += B.memorize(
    'فَلَا وَرَبِّكَ لَا يُؤْمِنُونَ حَتَّى يُحَكِّمُوكَ فِيمَا شَجَرَ '
    'بَيْنَهُمْ ثُمَّ لَا يَجِدُوا فِي أَنفُسِهِمْ حَرَجًا مِّمَّا قَضَيْتَ '
    'وَيُسَلِّمُوا تَسْلِيمًا',
    'The verse Ibn Bāz returns to five times in these folios. '
    '<strong>Three conditions, and two of them are of the heart</strong> — bring '
    'it to him; find no constriction at what he decided; submit completely. '
    '<em>And the sharḥ’s footnote refuses the usual softening: the إِيمَان '
    'negated here is the root, not merely the completeness</em> — by the evidence '
    'of what comes after it in the verse itself.')

b += B.nav('nq-l04-takfir-al-mushrikin.html',
           'النَّاقِضُ الثَّالِث · عَدَمُ تَكْفِيرِ المُشْرِكِين',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l05')

B.write('nq-l05-tafdil-ghayr-huda-al-nabi.html',
        'النَّاقِضُ الرَّابِع · تَفْضِيلُ غَيْرِ هُدَى النَّبِيِّ ﷺ',
        'The Fourth Nullifier, Part 1 — Preferring Other Than His Guidance',
        'The fourth of the ten nullifiers, part 1, from the words of Shaykh Ibn '
        'Bāz: exactly what the ijmāʿ is reported upon; why man-made codes are not '
        'ranked against one another; tawḥīd al-ḥukm from al-Naḥl 16:36 and '
        'al-Aʿrāf 7:54; the ḥadīth of ʿAdī ibn Ḥātim with its full grading '
        'apparatus; the three conditions of al-Nisāʾ 4:65 and the footnote on the '
        'īmān it negates; and the precision that permitting human systems to '
        'replace the Sharīʿah is named even where a man believes Allah’s rulings '
        'better. The tafṣīl — akbar against aṣghar, and al-khurūj — is part 2.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ الخَامِس', '5', b)
print('wrote nq-l05-tafdil-ghayr-huda-al-nabi.html')
