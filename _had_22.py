# -*- coding: utf-8 -*-
"""Ḥadīth 22 — «أَرَأَيْتَ إِذَا صَلَّيْتُ المَكْتُوبَاتِ…». Abū ʿAbdillāh
Jābir ibn ʿAbdillāh al-Anṣārī, Ṣaḥīḥ Muslim. Sharḥ of Ibn ʿUthaymīn, printed
folios 238–243 (markers 239–244, offset −1).

A man lists the obligatory prayers, the fast of Ramaḍān, doing the lawful and
leaving the forbidden, adds nothing more, and asks: do I enter Paradise? "Yes."
The Shaykh reads the question word by word (the five prayers, the shar'ī
definition of ṣiyām, the two senses of «أَحْلَلْت»), answers the apparent
difficulty of the missing zakāh and ḥajj, makes «نَعَمْ» a reiteration of the
question with its fiqh, and draws out the lofty aims of the Companions.

Rule 8: the ḥadīth is in Ṣaḥīḥ Muslim (Kitāb al-Īmān), so ṣaḥīḥ; the supporting
«مَنْ صَامَ رَمَضَانَ إِيمَانًا وَاحْتِسَابًا…» is in al-Bukhārī, and the qudsī
«أَعْدَدْتُ لِعِبَادِيَ الصَّالِحِينَ…» is muttafaq ʿalayh — named attributions,
no grading invented.
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
    'Say who narrated this ḥadīth and where it is reported, and read the '
    'question word by word — «%s».'
    % ar('أَرَأَيْتَ إِذَا صَلَّيْتُ المَكْتُوبَات'),
    'Give the shar‘ī definition of ṣiyām and the force of the qayd «%s».'
    % ar('تَعَبُّدًا لِله'),
    'Give the two senses of «%s», and when leaving the forbidden becomes an '
    'act of worship.' % ar('أَحْلَلْتُ الحَلَال'),
    'Answer the difficulty of the missing <strong>zakāh and ḥajj</strong> — why '
    'the man was still promised Paradise.',
    'Explain «%s» as a reiteration of the question, and name the aims of the '
    'Companions it reveals.' % ar('نَعَم'),
])

b += B.provenance(238, 243)

b += B.hadith_block(
    'عَنْ أَبِي عَبْدِ اللهِ جَابِرِ بْنِ عَبْدِ اللهِ الأَنْصَارِيِّ رَضِيَ '
    'اللهُ عَنْهُ أَنَّ رَجُلاً سَأَلَ النَّبِيَّ ﷺ فَقَالَ: «أَرَأَيْتَ إِذَا '
    'صَلَّيْتُ المَكْتُوبَاتِ، وَصُمْتُ رَمَضَانَ، وَأَحْلَلْتُ الحَلَالَ، '
    'وَحَرَّمْتُ الحَرَامَ، وَلَمْ أَزِدْ عَلَى ذَلِكَ شَيْئًا، أَأَدْخُلُ '
    'الجَنَّةَ؟» قَالَ: «نَعَمْ». رَوَاهُ مُسْلِم. وَمَعْنَى «حَرَّمْتُ '
    'الحَرَامَ» اجْتَنَبْتُهُ، وَمَعْنَى «أَحْلَلْتُ الحَلَالَ» فَعَلْتُهُ.',
    'Abū ʿAbdillāh Jābir ibn ʿAbdillāh al-Anṣārī (may Allah be pleased with '
    'him) reported that a man asked the Prophet ﷺ, "Tell me: if I pray the '
    'prescribed prayers, fast Ramaḍān, treat the lawful as lawful, treat the '
    'forbidden as forbidden, and add nothing more to that — shall I enter '
    'Paradise?" He said, "Yes." Narrated by Muslim. The meaning of "I treated '
    'the forbidden as forbidden" is: I avoided it; and "I treated the lawful as '
    'lawful" is: I did it.',
    'Narrated by Jābir ibn ʿAbdillāh al-Anṣārī · رَوَاهُ مُسْلِم — Muslim, in '
    'his Ṣaḥīḥ (Kitāb al-Īmān, bāb bayān al-īmān), so the ḥadīth is ṣaḥīḥ.')

# ------------------------------------------------------------------ §1
b += B.heading('قِرَاءَةُ السُّؤَال', 'Reading the Question')
b += p('<strong>«%s» means “inform me” (أَخْبِرْنِي).</strong> The man is asking '
       'the Prophet ﷺ to tell him the outcome of a settled, limited practice.'
       % ar('أَرَأَيْتَ'))
b += p('<strong>«%s» — the prescribed prayers</strong> are the <em>five in the '
       'day and night</em>, as Allah said; and what is beyond the five is not '
       'obligatory except for a cause that calls for it.'
       % ar('إِذَا صَلَّيْتُ المَكْتُوبَات'))
b += B.ayah(
    'إِنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا',
    'Indeed, prayer has been decreed upon the believers a decree of specified '
    'times.',
    'سُورَةُ النِّسَاء · 4:103')
b += box(
    '<p style="margin:0 0 .5rem;font-size:.94rem"><strong>«%s» — the fast of '
    'Ramaḍān.</strong> <em>Ṣiyām in the language is <strong>imsāk</strong> — to '
    'hold back from anything.</em></p>'
    '<p style="margin:0;font-size:.92rem">In the sharī‘ah it is: <strong>to hold '
    'back from the things that break the fast, from the rising of dawn (طُلُوعِ '
    'الفَجْر) to the setting of the sun (غُرُوبِ الشَّمْس), as worship to Allah '
    '(تَعَبُّدًا لِله).</strong> <em>The qayd “as worship” excludes one who '
    'holds back from food for a diet or his health — that is not a shar‘ī '
    'fast.</em></p>'
    % ar('وَصُمْتُ رَمَضَان'))

# ------------------------------------------------------------------ §2
b += B.heading('«أَحْلَلْتُ الحَلَالَ وَحَرَّمْتُ الحَرَام»',
               'Doing the Lawful, Leaving the Forbidden')
b += p('<strong>“Aḥalla the thing” carries two senses</strong> — <em>to believe '
       'it lawful</em>, and <em>to act upon it</em>. So «%s» is: I did the '
       'lawful <strong>believing it lawful</strong>; and «%s» is: I avoided the '
       'forbidden <strong>believing it forbidden</strong>.'
       % (ar('أَحْلَلْتُ الحَلَال'), ar('حَرَّمْتُ الحَرَام')))
b += p('<strong>And here leaving the forbidden can rise to worship.</strong> '
       '<em>A man may avoid drinking khamr not because it is ḥarām, but only '
       'because his soul has no taste for it — no sin lies on him; yet if he '
       'leaves it <strong>believing it forbidden</strong>, leaving it for '
       'Allah, he is rewarded for it.</em> Belief turns a bare abstention into '
       'an act of obedience.')
b += box(
    '<p style="margin:0;font-size:.94rem"><strong>A point beyond al-Nawawī’s '
    'wording.</strong> <em>Al-Nawawī explained «حَرَّمْتُ الحَرَام» as “I '
    'avoided it” and «أَحْلَلْتُ الحَلَال» as “I did it,” without tying it to '
    'belief. But one <strong>must</strong> believe the forbidden is forbidden '
    'and the lawful is lawful</em> — for if you do not believe the ḥarām is '
    'ḥarām you have not believed the shar‘ī ruling, and likewise the ḥalāl. So '
    'al-Nawawī’s explanation carries <strong>a touch of shortfall</strong> '
    '(قُصُور). Wallāhu aʿlam.</p>',
    wash='var(--gold-pale)', edge='var(--gold-warm)')

# ------------------------------------------------------------------ §3
b += B.heading('إِشْكَالُ الزَّكَاةِ وَالحَجّ', 'The Difficulty: Zakāh and Ḥajj')
b += p('<strong>The man said he added nothing more — yet he named neither zakāh '
       'nor ḥajj, two pillars of Islam, and still he was promised '
       'Paradise.</strong> <em>Zakāh was obligated before fasting, so we cannot '
       'say the ḥadīth predates zakāh; ḥajj was obligated only in the ninth or '
       'tenth year, so it may predate ḥajj. How is this answered?</em>')
b += table([
    row('الزَّكَاة',
        '<em>Perhaps the Prophet ﷺ knew the man was not one of wealth</em> — '
        'and that, were he wealthy, he would pay it; for he said «حَرَّمْتُ '
        'الحَرَام», and <strong>withholding zakāh is of the ḥarām</strong>, so '
        'it falls under his words.'),
    row('الحَجّ',
        '<em>It is easy to say this ḥadīth was before ḥajj was made '
        'obligatory</em> (the ninth or tenth year). And «%s» obligates '
        '<strong>completing</strong> the ḥajj, not <strong>beginning</strong> '
        'it; leaving ḥajj, too, is of the ḥarām, so it may fall under «حَرَّمْتُ '
        'الحَرَام».' % ar('وَأَتِمُّوا الحَجَّ وَالعُمْرَةَ لِله')),
])
b += B.ayah(
    'وَأَتِمُّوا الْحَجَّ وَالْعُمْرَةَ لِلَّهِ',
    'And complete the Ḥajj and ʿUmrah for Allah.',
    'سُورَةُ البَقَرَة · 2:196')

# ------------------------------------------------------------------ §4
b += B.heading('«قَالَ: نَعَم»', '“Yes” — a Reiteration of the Question')
b += p('<strong>«%s» is a particle of answer that affirms the thing asked '
       'about.</strong> <em>Its force is to <strong>repeat the question</strong>: '
       '“shall I enter Paradise?” — “yes [you enter Paradise].”</em> This is a '
       'rule that runs through the fiqh of contracts and declarations: wherever '
       '«نَعَم» answers a question, read it as the question said back in the '
       'affirmative.' % ar('نَعَم'))
b += table([
    row('أَطَلَّقْتَ امْرَأَتَك؟ — نَعَم',
        '<em>“Did you divorce your wife?” — “Yes.”</em> She is divorced, for '
        '«نَعَم» means “I divorced her.”'),
    row('زَوَّجْتُكَ ابْنَتِي… أَقَبِلْت؟ — نَعَم',
        '<em>“I marry my daughter to you… do you accept?” — “Yes.”</em> It '
        'suffices as acceptance of the marriage.'),
    row('أَوَقَفْتَ بَيْتَك؟ — نَعَم',
        '<em>“Did you make your house a waqf?” — “Yes.”</em> The house becomes '
        'waqf.'),
    row('أَبِعْتَ سَيَّارَتَك؟ — نَعَم',
        '<em>“Did you sell your car?” — “Yes.”</em> He has affirmed the sale.'),
])

# ------------------------------------------------------------------ §5
b += B.heading('غَايَاتُ الصَّحَابَة', 'The Aims of the Companions')
b += p('<strong>First benefit: the loftiness of the Companions’ aims.</strong> '
       '<em>The end they sought was <strong>entering Paradise</strong> — not '
       'abundance of wealth, nor many children, nor ease in this world.</em> '
       'When one of them did the Prophet ﷺ a service and was told, “Ask what '
       'you wish,” he said: <em>your companionship in Paradise.</em> He was '
       'answered: «%s» — “then help me for yourself by abundant prostration,” '
       'that is, by much prayer. He asked for no coin, no herds, no palace, no '
       'field — he asked for Paradise.'
       % ar('أَعِنِّي عَلَى نَفْسِكَ بِكَثْرَةِ السُّجُود'))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.94rem"><strong>And Paradise is the '
    'reward of such deeds.</strong> It is the abode of bliss Allah prepared for '
    'the God-fearing — what no eye has seen, as in the qudsī ḥadīth: «%s» '
    '(muttafaq ʿalayh).</p>'
    '<p style="margin:0;font-size:.92rem"><strong>Second: restricting oneself '
    'to the obligatory prayer brings no blame</strong> and does not bar one '
    'from Paradise — «%s». <em>Imām Aḥmad said of one who leaves the witr that '
    'he is a bad man whose witness should not be accepted; but being a bad man '
    'does not bar him from Paradise — he is only faulted because the witr is as '
    'little as a single rak‘ah, and still he neglects it.</em> And fasting and '
    'prayer are among the <strong>causes</strong> of entering Paradise: whoever '
    'fasts Ramaḍān in faith and seeking reward, his past sins are forgiven '
    '(al-Bukhārī).</p>'
    % (ar('أَعْدَدْتُ لِعِبَادِيَ الصَّالِحِينَ مَا لَا عَيْنٌ رَأَتْ، وَلَا '
          'أُذُنٌ سَمِعَتْ، وَلَا خَطَرَ عَلَى قَلْبِ بَشَر'),
       ar('أَرَأَيْتَ إِذَا صَلَّيْتُ المَكْتُوبَات')))
b += B.ayah(
    'فَلَا تَعْلَمُ نَفْسٌ مَّا أُخْفِيَ لَهُم مِّن قُرَّةِ أَعْيُنٍ جَزَاءً '
    'بِمَا كَانُوا يَعْمَلُونَ',
    'No soul knows what has been hidden for them of comfort for the eyes as '
    'reward for what they used to do.',
    'سُورَةُ السَّجْدَة · 32:17')

# ------------------------------------------------------------------ vocab
b += B.vocab([
    ('أَرَأَيْت', 'araʾayta', 'tell me, inform me', 'ر-أ-ي',
     'The opening of the man’s question — it means “inform me” (أَخْبِرْنِي) of '
     'the outcome of what I name',
     'أَرَأَيْتَ إِذَا صَلَّيْتُ المَكْتُوبَات'),
    ('المَكْتُوبَات', 'al-maktūbāt', 'the prescribed prayers', 'ك-ت-ب',
     'The five obligatory prayers of the day and night; the Qurʾān calls the '
     'prayer «كِتَابًا مَوْقُوتًا» — a decree of specified times',
     'إِذَا صَلَّيْتُ المَكْتُوبَات'),
    ('الصِّيَام', 'al-ṣiyām', 'fasting', 'ص-و-م',
     'In the language, imsāk (holding back from anything); in the sharī‘ah, '
     'holding back from what breaks the fast, dawn to sunset, as worship',
     'الصِّيَامُ فِي اللُّغَةِ الإِمْسَاك'),
    ('تَعَبُّدًا لِله', 'taʿabbudan lillāh', 'as worship to Allah', 'ع-ب-د',
     'The qayd in the definition of fasting that excludes abstaining for a diet '
     'or one’s health — that is not a shar‘ī fast',
     'الإِمْسَاكُ عَنِ المُفْطِرَاتِ تَعَبُّدًا لِله'),
    ('أَحْلَلْتُ الحَلَال', 'aḥlaltu al-ḥalāl', 'I treated the lawful as lawful',
     'ح-ل-ل',
     '“Aḥalla” has two senses — to believe a thing lawful, and to act upon it; '
     'here: I did the lawful believing it lawful',
     'أَحْلَلْتُ الحَلَالَ أَيْ فَعَلْتُهُ مُعْتَقِدًا حِلَّه'),
    ('حَرَّمْتُ الحَرَام', 'ḥarramtu al-ḥarām', 'I treated the forbidden as forbidden',
     'ح-ر-م',
     'I avoided the ḥarām believing it forbidden; leaving it for Allah turns a '
     'bare abstention into worship',
     'حَرَّمْتُ الحَرَامَ أَيِ اجْتَنَبْتُهُ مُعْتَقِدًا تَحْرِيمَه'),
    ('نَعَم', 'naʿam', 'yes (a particle of answer)', 'ن-ع-م',
     'A particle affirming what was asked — read as a reiteration of the '
     'question; in divorce, nikāḥ, waqf and sale it settles the matter',
     'أَأَدْخُلُ الجَنَّةَ؟ قَالَ: نَعَم'),
    ('الوِتْر', 'al-witr', 'the witr prayer', 'و-ت-ر',
     'At least a single rak‘ah; Imām Aḥmad faulted the one who abandons it — '
     'yet that does not bar him from Paradise',
     'مَنْ تَرَكَ الوِتْرَ فَهُوَ رَجُلُ سَوْء'),
])

# ------------------------------------------------------------------ MCQ
b += B.mcq('hd-h22', [
    ('Who narrated this ḥadīth, and where is it reported?',
     ['Abū Hurayrah, in al-Bukhārī',
      'Jābir ibn ʿAbdillāh al-Anṣārī, in Muslim',
      'Abū Dharr, in al-Tirmidhī',
      'ʿUmar ibn al-Khaṭṭāb, in Abū Dāwūd'], 1),
    ('What does «أَرَأَيْتَ» mean in the man’s question?',
     ['Have you seen with your eyes?',
      'Inform me / tell me (أَخْبِرْنِي)',
      'Do you think so?',
      'Will you show me?'], 1),
    ('What are «المَكْتُوبَات»?',
     ['All the voluntary prayers',
      'The five obligatory prayers of the day and night',
      'The prayers written in letters',
      'The funeral and eclipse prayers'], 1),
    ('Which āyah is cited for the five being a fixed obligation?',
     ['al-Baqarah 2:196',
      'al-Nisāʾ 4:103 — «كِتَابًا مَوْقُوتًا»',
      'al-Sajdah 32:17',
      'al-Aḥqāf 46:13'], 1),
    ('What is the shar‘ī definition of ṣiyām?',
     ['Abstaining from food only, at any time',
      'Holding back from what breaks the fast, from dawn to sunset, as worship '
      'to Allah',
      'Abstaining from speech for a day',
      'Eating only once a day'], 1),
    ('What does the qayd «تَعَبُّدًا لِله» exclude?',
     ['The sick and the traveller',
      'One who abstains from food for a diet or his health — that is not a '
      'shar‘ī fast',
      'The one who fasts voluntarily',
      'The fast of ʿĀshūrāʾ'], 1),
    ('What are the two senses of “aḥalla the thing”?',
     ['To sell it and to buy it',
      'To believe it lawful, and to act upon it',
      'To praise it and to forbid it',
      'To taste it and to describe it'], 1),
    ('When does avoiding the forbidden become an act of worship?',
     ['When others can see him avoid it',
      'When he leaves it believing it forbidden, leaving it for Allah — not '
      'merely because his soul dislikes it',
      'Only during Ramaḍān',
      'When he announces that he left it'], 1),
    ('How is the difficulty of the unmentioned ZAKĀH answered?',
     ['The ḥadīth predates the obligation of zakāh',
      'Perhaps the man was not wealthy; and withholding zakāh is of the ḥarām, '
      'so it falls under «حَرَّمْتُ الحَرَام»',
      'Zakāh is not truly obligatory',
      'He paid it secretly'], 1),
    ('What does «وَأَتِمُّوا الحَجَّ وَالعُمْرَةَ لِله» (2:196) obligate?',
     ['Beginning the ḥajj every year',
      'Completing the ḥajj and ʿumrah once begun — not initiating them',
      'Performing ḥajj on behalf of others',
      'Fasting during ḥajj'], 1),
    ('How is «نَعَم» to be understood as an answer?',
     ['As a mere sound of acknowledgement with no legal weight',
      'As a reiteration of the question — “yes [you enter Paradise]”; likewise '
      'in divorce, nikāḥ, waqf and sale',
      'As a request for more time',
      'As a conditional reply'], 1),
    ('What do the Companions’ aims in this ḥadīth reveal?',
     ['A desire for wealth and standing',
      'That their highest aim was entering Paradise — one asked for the '
      'Prophet’s ﷺ companionship there, not coin or herds',
      'Indifference to the Hereafter',
      'A preference for long life in the world'], 1),
])

# ------------------------------------------------------------------ T/F
b += B.tf('hd-h22-tf', [
    ('«أَرَأَيْتَ» فِي الحَدِيثِ بِمَعْنَى أَخْبِرْنِي.',
     '«Araʾayta» in the ḥadīth means “inform me.”', True),
    ('المَكْتُوبَاتُ هِيَ الصَّلَوَاتُ الخَمْسُ فِي اليَوْمِ وَاللَّيْلَة.',
     'The maktūbāt are the five prayers of the day and night.', True),
    ('مَنْ أَمْسَكَ عَنِ الطَّعَامِ حِمْيَةً لِنَفْسِهِ فَصِيَامُهُ صِيَامٌ '
     'شَرْعِيّ.',
     'Whoever abstains from food for a diet, his fast is a shar‘ī fast.', False),
    ('تَرْكُ الحَرَامِ مَعَ اعْتِقَادِ تَحْرِيمِهِ لِلهِ يَصِيرُ عِبَادَةً '
     'يُثَابُ عَلَيْهَا.',
     'Leaving the forbidden while believing it forbidden, for Allah, becomes an '
     'act of worship one is rewarded for.', True),
    ('مَنْعُ الزَّكَاةِ مِنَ الحَرَام، فَيَدْخُلُ فِي قَوْلِهِ «حَرَّمْتُ '
     'الحَرَام».',
     'Withholding zakāh is of the forbidden, so it falls under his words “I '
     'treated the forbidden as forbidden.”', True),
    ('«نَعَم» فِي جَوَابِ السُّؤَالِ كَإِعَادَةِ السُّؤَالِ مُثْبَتًا.',
     '«Yes» in answer to a question is like the question repeated in the '
     'affirmative.', True),
    ('مَنِ اقْتَصَرَ عَلَى الصَّلَاةِ المَكْتُوبَةِ يُحْرَمُ مِنْ دُخُولِ '
     'الجَنَّة.',
     'Whoever restricts himself to the obligatory prayer is barred from '
     'entering Paradise.', False),
])

b += B.memorize(
    'أَرَأَيْتَ إِذَا صَلَّيْتُ المَكْتُوبَاتِ، وَصُمْتُ رَمَضَانَ، وَأَحْلَلْتُ '
    'الحَلَالَ، وَحَرَّمْتُ الحَرَامَ، وَلَمْ أَزِدْ عَلَى ذَلِكَ شَيْئًا، '
    'أَأَدْخُلُ الجَنَّةَ؟ قَالَ: نَعَمْ',
    'A man counts up the <strong>five prayers</strong>, the <strong>fast of '
    'Ramaḍān</strong>, doing the lawful and leaving the forbidden — adds '
    'nothing more — and asks whether that is enough for Paradise. The Prophet ﷺ '
    'says <strong>yes</strong>. Around it the Shaykh fixes the shar‘ī meaning of '
    'the fast (holding back, dawn to sunset, <em>for Allah</em>), answers how '
    'the unnamed <strong>zakāh and ḥajj</strong> are still accounted for, and '
    'makes «naʿam» a question said back in the affirmative. <em>Its heart is '
    'the Companions’ aim: not wealth, not ease — but to enter the '
    'Garden.</em>')

b += B.nav('h21-qul-amantu.html', 'Ḥadīth 21 · قُلْ آمَنْتُ بِالله',
           'index.html', 'Mark complete · أَتْمَمْتَ الدَّرْس · Hadeeth Hub',
           'hd-h22')

B.write('h22-araayta-idha-sallaytu.html',
        'أَرَأَيْتَ إِذَا صَلَّيْتُ المَكْتُوبَات',
        'If I Pray the Prescribed Prayers… Shall I Enter Paradise?',
        'Ḥadīth 22 of al-Nawawī’s Forty (Jābir ibn ʿAbdillāh al-Anṣārī, Muslim) '
        'with the sharḥ of Ibn ʿUthaymīn: a man lists the obligatory prayers, '
        'the fast of Ramaḍān, doing the lawful and leaving the forbidden, and '
        'asks if he enters Paradise — “Yes.” Reading the question (the five '
        'prayers, al-Nisāʾ 4:103; the shar‘ī definition of ṣiyām; the two '
        'senses of «aḥlaltu»); the difficulty of the unnamed zakāh and ḥajj and '
        'its answer (al-Baqarah 2:196); «naʿam» as a reiteration of the '
        'question and its fiqh; and the lofty aims of the Companions (al-Sajdah '
        '32:17).',
        22, 'Muslim', '2', b)
print('wrote h22-araayta-idha-sallaytu.html')
