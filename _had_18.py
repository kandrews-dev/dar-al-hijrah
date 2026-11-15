# -*- coding: utf-8 -*-
"""Ḥadīth 18 — «اتَّقِ اللهَ حَيْثُمَا كُنْتَ، وَأَتْبِعِ السَّيِّئَةَ
الحَسَنَةَ تَمْحُهَا، وَخَالِقِ النَّاسَ بِخُلُقٍ حَسَن». Abū Dharr and Muʿādh
ibn Jabal, al-Tirmidhī — ḥasan (and in some copies ḥasan ṣaḥīḥ). Sharḥ of Ibn
ʿUthaymīn, printed folios 219–223 (PDF indices 220–224, offset −1).

Three commands covering the three relations: between a man and his Lord (taqwā
everywhere), a man and his own slips (follow a sin with a good deed), and a man
and other people (good character).

Structure, following the sharḥ:
  1. «اتَّقِ اللهَ حَيْثُمَا كُنْت» — taqwā is a wiqāyah (a shield) by doing the
     commands and leaving the prohibitions; «wherever» = public and secret.
  2. «وَأَتْبِعِ السَّيِّئَةَ الحَسَنَةَ تَمْحُهَا» — the grammar (تَمْحُهَا is
     the jawāb of the amr, hence jazm); the differed point — is the «good deed»
     repentance or general? the ṣawāb is general, on Hūd 11:114 and the ḥadīth
     of the man who kissed a woman then prayed Fajr.
  3. «وَخَالِقِ النَّاسَ بِخُلُقٍ حَسَن» — khuluq (the inner) vs khalq (the
     outer); the definition (kaff al-adhā, badhl al-nadā, ṣabr ʿalā al-adhā,
     wajh ṭalq); its ḍābiṭ in al-Aʿrāf 7:199; innate vs acquired (al-Ashajj
     ʿAbd al-Qays).
  4. Fawāʾid: secret vs public taqwā (tafṣīl, not a flat rule); acts of worship
     in unfit places; and that firmness does not contradict good character —
     «لِكُلِّ مَقَامٍ مَقَال», with rifq preferred when the matter is even.

Rule 8: al-Tirmidhī's own grading «حَسَن / حَسَن صَحِيح» is carried on the matn
line; every supporting ḥadīth (the kisser — al-Bukhārī & Muslim; al-Ashajj —
Muslim; «الله رفيق» — al-Bukhārī & Muslim) is named by its collection as the
sharḥ names it, with no grading added of our own.
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
    'Define <strong>التَّقْوَى</strong> as the sharḥ does — a '
    '<em>wiqāyah</em> — and say what «%s» adds to the command.'
    % ar('حَيْثُمَا كُنْت'),
    'Give the grammar of «%s» and the meaning it yields.'
    % ar('أَتْبِعِ السَّيِّئَةَ الحَسَنَةَ تَمْحُهَا'),
    'State the scholars’ disagreement over «the good deed», which view is '
    'correct, and the two proofs for it.',
    'Distinguish <strong>الخُلُق</strong> from <strong>الخَلْق</strong>, and '
    'give the fourfold definition of good character.',
    'Say whether good character is innate or acquired, with the ḥadīth of '
    'al-Ashajj ʿAbd al-Qays.',
    'Answer which is better — secret or public taqwā — and whether firmness '
    'contradicts good character.',
])

b += B.provenance(219, 223)

b += B.hadith_block(
    'عَنْ أَبِي ذَرٍّ جُنْدُبِ بْنِ جُنَادَةَ، وَأَبِي عَبْدِ الرَّحْمَٰنِ '
    'مُعَاذِ بْنِ جَبَلٍ رَضِيَ اللهُ عَنْهُمَا، عَنْ رَسُولِ اللهِ ﷺ قَالَ: '
    '«اتَّقِ اللهَ حَيْثُمَا كُنْتَ، وَأَتْبِعِ السَّيِّئَةَ الحَسَنَةَ '
    'تَمْحُهَا، وَخَالِقِ النَّاسَ بِخُلُقٍ حَسَنٍ». رَوَاهُ التِّرْمِذِيُّ '
    'وَقَالَ: حَدِيثٌ حَسَنٌ، وَفِي بَعْضِ النُّسَخِ: حَسَنٌ صَحِيحٌ.',
    'Abū Dharr Jundub ibn Junādah and Abū ʿAbd al-Raḥmān Muʿādh ibn Jabal (may '
    'Allah be pleased with them both) reported that the Messenger of Allah ﷺ '
    'said: "Fear Allah wherever you are; follow a bad deed with a good one and '
    'it will erase it; and deal with people with good character."',
    'Narrated by Abū Dharr & Muʿādh · رَوَاهُ التِّرْمِذِيُّ — al-Tirmidhī, who '
    'said: a ḥasan ḥadīth (and in some copies: ḥasan ṣaḥīḥ). The grading named '
    'here is al-Tirmidhī’s own.')

# ------------------------------------------------------------------ §1
b += B.heading('«اتَّقِ اللهَ حَيْثُمَا كُنْت»', 'Fear Allah Wherever You Are')
b += p('<strong>Three commands, and they cover the three relationships a '
       'person lives inside:</strong> with his Lord, with his own sins, and '
       'with other people. The first is taqwā — and the sharḥ defines the word '
       'before the command.')
b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem"><strong>«%s»</strong> — <em>take '
    'a <strong>shield</strong> (wiqāyah) from the punishment of Allah; and '
    'that is by <strong>doing His commands and avoiding His '
    'prohibitions</strong>.</em></p>'
    '<p style="margin:0;font-size:.93rem"><strong>«%s»</strong> is a ẓarf of '
    'place — <em>in whatever place you are: in the open or in secret, at home '
    'or in the market, whether people are with you or not.</em></p>'
    % (ar('اتَّقِ الله'), ar('حَيْثُمَا كُنْت')))
b += p('<strong>Read what the «wherever» is doing.</strong> It is easy to be '
       'God-fearing where one is seen; the command reaches precisely to the '
       'place no one is watching. <em>Taqwā that switches off in private was '
       'never taqwā of Allah — it was taqwā of people.</em>')

# ------------------------------------------------------------------ §2
b += B.heading('«وَأَتْبِعِ السَّيِّئَةَ الحَسَنَةَ تَمْحُهَا»', 'Follow a Bad Deed with a Good One')
b += p('The second command is for the man who has already slipped — and the '
       'grammar carries the meaning. <em>«%s» is a verb of command; «%s» is '
       'its first object and «%s» its second; and «%s» is the <strong>jawāb of '
       'the command</strong>, which is why it is majzūm.</em> The sense: '
       '<strong>if you do a bad deed, follow it with a good one, and the good '
       'deed erases the bad.</strong>'
       % (ar('أَتْبِع'), ar('السَّيِّئَة'), ar('الحَسَنَة'), ar('تَمْحُهَا')))
b += p('<strong>Then a real disagreement, which changes how wide the mercy '
       'is.</strong> <em>Is the «good deed» that erases the sin '
       '<strong>repentance</strong> specifically — as though he said: if you '
       'sin, repent — or is it <strong>general</strong>? The correct view is '
       'the second: the good deed erases the sin even if it is not '
       'repentance.</em>')
b += B.ayah(
    'وَأَقِمِ الصَّلَاةَ طَرَفَيِ النَّهَارِ وَزُلَفًا مِّنَ اللَّيْلِ إِنَّ '
    'الْحَسَنَاتِ يُذْهِبْنَ السَّيِّئَاتِ',
    'And establish the prayer at the two ends of the day and in the early '
    'hours of the night. Indeed, good deeds drive away bad deeds.',
    'سُورَةُ هُود · 11:114')
b += box(
    '<p style="margin:0;font-size:.94rem"><strong>And the proof from the '
    'Sunnah settles it.</strong> <em>A man came to the Prophet ﷺ and said he '
    'had taken from a woman everything a man takes from his wife short of '
    'zinā — and he had prayed Fajr with them. The Prophet ﷺ asked: «Did you '
    'pray Fajr with us?» He said yes — and the Prophet ﷺ recited to him «%s»</em> '
    '<strong>(al-Bukhārī and Muslim)</strong>. The good deed here was the '
    'prayer, not a formal repentance — <em>which shows the good deed erases '
    'the sin even when it is not itself the repentance.</em></p>'
    % ar('إِنَّ الْحَسَنَاتِ يُذْهِبْنَ السَّيِّئَات'))

# ------------------------------------------------------------------ §3
b += B.heading('«وَخَالِقِ النَّاسَ بِخُلُقٍ حَسَن»', 'Deal with People with Good Character')
b += p('The third command turns outward. <em>«%s» — deal with people with good '
       'character.</em> And the Shaykh draws the fine line between two words '
       'that sound alike:'
       % ar('خَالِقِ النَّاسَ بِخُلُقٍ حَسَن'))
b += table([
    row('<span dir="rtl" lang="ar">الخُلُق</span><br>'
        '<span style="font-size:.82rem;font-weight:400">khuluq</span>',
        '<em>the <strong>inner</strong> trait in a person</em> — the '
        'disposition the character flows from.'),
    row('<span dir="rtl" lang="ar">الخَلْق</span><br>'
        '<span style="font-size:.82rem;font-weight:400">khalq</span>',
        '<em>the <strong>outer</strong> form</em> — the body and appearance. '
        'The command is about the first, shown through word and deed.'),
])
b += p('<strong>What is good character, concretely?</strong> <em>Some of them '
       'said it is four things:</em> <strong>%s</strong> — withholding harm '
       'from people; <strong>%s</strong> — the giving of kindness; '
       '<strong>%s</strong> — patience over the harm others do, since no one '
       'is free of being harmed by people; and <strong>%s</strong> — a '
       'cheerful, open face.'
       % (ar('كَفُّ الأَذَى'), ar('بَذْلُ النَّدَى'),
          ar('الصَّبْرُ عَلَى الأَذَى'), ar('الوَجْهُ الطَّلْق')))
b += B.ayah(
    'خُذِ الْعَفْوَ وَأْمُرْ بِالْعُرْفِ وَأَعْرِضْ عَنِ الْجَاهِلِينَ',
    'Take what is easily given, enjoin what is good, and turn away from the '
    'ignorant.',
    'سُورَةُ الأَعْرَاف · 7:199')
b += p('<em>Its ḍābiṭ is what Allah named in «%s» — take what people give '
       'easily, and do not demand that they come to you as you would wish, for '
       'that is impossible; take what comes readily.</em> <strong>Good '
       'character is not requiring of people a perfection they cannot '
       'give.</strong>'
       % ar('خُذِ الْعَفْوَ'))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.94rem"><strong>Is good character '
    'innate or acquired?</strong> <em>Both: part of it is inborn, and part is '
    'won by effort.</em> The Prophet ﷺ said to al-Ashajj ʿAbd al-Qays: «%s» — '
    '<em>in you are two traits Allah loves: forbearance and deliberateness.</em> '
    'He asked: did I acquire them, or did Allah fashion me upon them? He said: '
    '<em>«Allah fashioned you upon them»</em> <strong>(Muslim)</strong>.</p>'
    '<p style="margin:0;font-size:.92rem">So one may be given a fine character '
    'from the outset — and another may <strong>train himself</strong> to it '
    'until it becomes his. <em>And the wonder, the Shaykh notes, is that good '
    'character earns the one who has it rest and peace of mind, because he is '
    'at ease with himself in dealing with others.</em></p>'
    % ar('إِنَّ فِيكَ لَخُلُقَيْنِ يُحِبُّهُمَا الله: الحِلْمُ وَالأَنَاة'))

# ------------------------------------------------------------------ §4
b += B.heading('مِنْ فَوَائِدِ الحَدِيث', 'From the Benefits')
b += p('<strong>١ · Which is better — taqwā in secret or in the open?</strong> '
       '<em>There is a detail here, not a flat rule.</em> If showing it brings '
       'about <strong>emulation and following</strong> — people taking after '
       'you in the good — then making it public is better, which is why Allah '
       'praised those who spend «%s», and why the Prophet ﷺ said «%s». But '
       'where showing it brings no benefit, <strong>secrecy is better</strong> '
       '— as in the man whom Allah shades, who gave charity so secretly «%s».'
       % (ar('سِرًّا وَعَلَانِيَة'),
          ar('مَنْ سَنَّ فِي الإِسْلَامِ سُنَّةً حَسَنَةً'),
          ar('حَتَّى لَا تَعْلَمَ شِمَالُهُ مَا تُنْفِقُ يَمِينُه')))
b += p('<strong>٢ · Does «wherever you are» mean performing acts of worship '
       'even in unfit places</strong> — a washroom and the like? <em>No: do '
       'not perform the acts there; but intend in your heart that you are '
       'obedient to Allah, complying with His command and avoiding His '
       'prohibition.</em> The command reaches the heart in every place, not '
       'the ritual act in every place.')
b += p('<strong>٣ · Does dealing firmly with people contradict «good '
       'character»?</strong> <em>It does not — «%s», to every situation its '
       'own speech.</em> Where the benefit lies in firmness, be firm; where it '
       'lies the other way, be gentle; and <strong>when the two are even, '
       'incline to gentleness</strong>, for the Prophet ﷺ said «%s».'
       % (ar('لِكُلِّ مَقَامٍ مَقَال'),
          ar('إِنَّ اللهَ رَفِيقٌ يُحِبُّ الرِّفْقَ فِي الأَمْرِ كُلِّه')))
b += box(
    '<p style="margin:0;font-size:.93rem"><strong>The sharḥ’s own '
    'illustration:</strong> <em>a Jew passed the Prophet ﷺ and said «al-sām '
    'ʿalayk» — death be upon you. ʿĀʾishah رَضِيَ اللهُ عَنْهَا answered him '
    'back with worse. The Prophet ﷺ restrained her and said: «Allah is gentle '
    'and loves gentleness in all things» — and «when the People of the Book '
    'greet you, say: </em>wa-ʿalaykum<em>»</em> <strong>(al-Bukhārī and '
    'Muslim)</strong>. <em>Even provoked, the answer measured to the moment '
    'was the gentle one.</em></p>')

# ------------------------------------------------------------------ vocab
b += B.vocab([
    ('التَّقْوَى', 'al-taqwā', 'God-consciousness, mindful fear', 'و-ق-ي',
     'A <em>wiqāyah</em>, a shield taken from the punishment of Allah by doing '
     'His commands and leaving His prohibitions',
     'اتَّقِ اللهَ حَيْثُمَا كُنْت'),
    ('حَيْثُمَا', 'ḥaythumā', 'wherever', 'ح-ي-ث',
     'A ẓarf of place: in the open or in secret, with people or alone — the '
     'command reaches the unwatched place',
     'حَيْثُمَا كُنْت... فِي العَلَانِيَةِ أَوْ فِي السِّرّ'),
    ('أَتْبِعْ', 'atbiʿ', 'make follow, follow up', 'ت-ب-ع',
     'A command: make a good deed follow a bad one; «تَمْحُهَا» is its jawāb, '
     'majzūm — the good deed erases the bad',
     'وَأَتْبِعِ السَّيِّئَةَ الحَسَنَةَ تَمْحُهَا'),
    ('الحَسَنَة', 'al-ḥasanah', 'the good deed', 'ح-س-ن',
     'The deed that erases the sin — general, not repentance alone, on Hūd '
     '11:114 and the ḥadīth of the man who prayed Fajr',
     'إِنَّ الحَسَنَاتِ يُذْهِبْنَ السَّيِّئَات'),
    ('الخُلُق', 'al-khuluq', 'character, inner disposition', 'خ-ل-ق',
     'The inner trait — against الخَلْق, the outer form; the command is to '
     'deal with people out of a beautiful one',
     'الخُلُقُ هُوَ الصِّفَةُ البَاطِنَةُ فِي الإِنْسَان'),
    ('كَفُّ الأَذَى', 'kaff al-adhā', 'withholding harm', 'ك-ف-ف',
     'The first of the four parts of good character — holding back your harm '
     'from people',
     'الخُلُقُ الحَسَن: كَفُّ الأَذَى، وَبَذْلُ النَّدَى'),
    ('بَذْلُ النَّدَى', 'badhl al-nadā', 'giving of kindness', 'ن-د-ي',
     'The second part — open-handed generosity and kindness toward people',
     'بَذْلُ النَّدَى أَيِ العَطَاء'),
    ('لِكُلِّ مَقَامٍ مَقَال', 'li-kulli maqāmin maqāl',
     'to every situation its own speech', 'ق-و-ل',
     'Why firmness does not contradict good character — firmness where it '
     'benefits, gentleness where it does, and gentleness when the two are even',
     'لِكُلِّ مَقَامٍ مَقَال؛ فَإِذَا كَانَتِ المَصْلَحَةُ فِي الشِّدَّةِ فَعَلَيْكَ بِهَا'),
])

# ------------------------------------------------------------------ MCQ
b += B.mcq('hd-h18', [
    ('How does the sharḥ define التَّقْوَى?',
     ['Fear that keeps a man from the mosque',
      'Taking a shield (wiqāyah) from the punishment of Allah — by doing His '
      'commands and avoiding His prohibitions',
      'Loving Allah only',
      'Abstaining from all food and drink'], 1),
    ('What does «حَيْثُمَا كُنْتَ» add to the command of taqwā?',
     ['That it applies only in the mosque',
      'That it applies in every place — the open and the secret, with people '
      'or alone; it reaches the unwatched place',
      'That it applies only among Muslims',
      'That it applies only during Ramaḍān'], 1),
    ('In «وَأَتْبِعِ السَّيِّئَةَ الحَسَنَةَ تَمْحُهَا», what is تَمْحُهَا '
     'grammatically, and what does the clause mean?',
     ['A separate command; it means erase your own record',
      'The jawāb of the command (hence majzūm) — meaning: if you do a bad '
      'deed, follow it with a good one, and the good deed erases it',
      'A past-tense verb; it means the sin was erased long ago',
      'A noun; it means the eraser'], 1),
    ('The scholars differed over «the good deed» that erases the sin. What is '
     'the correct view, and why does it matter?',
     ['That it is repentance alone — so only repentance erases sins',
      'That it is GENERAL — the good deed erases the sin even if it is not '
      'repentance; this widens the mercy, on Hūd 11:114 and the ḥadīth of the '
      'man who prayed Fajr',
      'That it erases nothing without a vow',
      'That only charity erases sins'], 1),
    ('Which ḥadīth proves the good deed erases the sin even when it is not '
     'itself repentance?',
     ['The ḥadīth of the man who freed a slave',
      'The man who took from a woman all but zinā, had prayed Fajr, and to '
      'whom the Prophet ﷺ recited «the good deeds drive away the bad» — '
      'al-Bukhārī & Muslim',
      'The ḥadīth of the three who were trapped in the cave',
      'The ḥadīth of Jibrīl'], 1),
    ('What is the difference between الخُلُق and الخَلْق?',
     ['They are the same word',
      'الخُلُق is the inner trait (character); الخَلْق is the outer form (the '
      'body) — the command concerns the first',
      'الخُلُق is the body; الخَلْق is the soul',
      'الخُلُق is for Arabs, الخَلْق for non-Arabs'], 1),
    ('What is the fourfold definition of good character given here?',
     ['Prayer, fasting, charity, and ḥajj',
      'Withholding harm (كَفُّ الأَذَى), giving kindness (بَذْلُ النَّدَى), '
      'patience over harm (الصَّبْرُ عَلَى الأَذَى), and a cheerful face '
      '(الوَجْهُ الطَّلْق)',
      'Knowledge, action, sincerity, and patience',
      'Honesty, courage, generosity, and justice'], 1),
    ('What is the ḍābiṭ of good character, per al-Aʿrāf 7:199?',
     ['To demand people come to you as you wish',
      'To take what people give easily and not require of them a perfection '
      'they cannot give — «خُذِ الْعَفْوَ»',
      'To avoid people entirely',
      'To correct every fault you see in them'], 1),
    ('Is good character innate or acquired?',
     ['Purely innate — it cannot be learned',
      'Both — part inborn and part won by effort; the Prophet ﷺ told '
      'al-Ashajj ʿAbd al-Qays that Allah fashioned him upon forbearance and '
      'deliberateness (Muslim), and one may also train himself to it',
      'Purely acquired — no one is born with it',
      'It is fixed at forty and cannot change'], 1),
    ('Which is better, taqwā in secret or in the open?',
     ['Always in secret',
      'There is a detail: public is better where it brings emulation and '
      'following in the good; secret is better where showing it brings no '
      'benefit',
      'Always in the open',
      'They are exactly equal in every case'], 1),
    ('Does «fear Allah wherever you are» mean performing acts of worship even '
     'in unfit places like a washroom?',
     ['Yes — one prays everywhere without exception',
      'No — do not perform the acts there, but intend in your heart that you '
      'are obedient to Allah; the command reaches the heart in every place, '
      'not the ritual act',
      'Yes — but silently',
      'It does not address places at all'], 1),
    ('Does dealing firmly with people contradict good character?',
     ['Yes — one must always be soft',
      'No — «لِكُلِّ مَقَامٍ مَقَال»: firmness where it benefits, gentleness '
      'where it does, and gentleness when the two are even, for «Allah is '
      'gentle and loves gentleness in all things»',
      'Yes — firmness is always forbidden',
      'Firmness is always better than gentleness'], 1),
])

# ------------------------------------------------------------------ T/F
b += B.tf('hd-h18-tf', [
    ('التَّقْوَى هِيَ اتِّخَاذُ وِقَايَةٍ مِنْ عَذَابِ اللهِ بِفِعْلِ '
     'الأَوَامِرِ وَاجْتِنَابِ النَّوَاهِي.',
     'Taqwā is taking a shield from Allah’s punishment by doing the commands '
     'and avoiding the prohibitions.', True),
    ('الحَسَنَةُ لَا تَمْحُو السَّيِّئَةَ إِلَّا إِذَا كَانَتْ تَوْبَةً.',
     'The good deed does not erase the sin unless it is repentance.', False),
    ('الخُلُقُ هُوَ الصِّفَةُ البَاطِنَة، وَالخَلْقُ هُوَ الصِّفَةُ '
     'الظَّاهِرَة.',
     'Al-khuluq is the inner trait and al-khalq is the outer form.', True),
    ('الخُلُقُ الحَسَنُ جِبِلِّيٌّ فَقَط، لَا يُكْتَسَب.',
     'Good character is purely innate and cannot be acquired.', False),
    ('إِظْهَارُ التَّقْوَى أَفْضَلُ إِذَا حَصَلَ بِهِ التَّأَسِّي '
     'وَالاتِّبَاع.',
     'Showing taqwā openly is better when emulation and following result from '
     'it.', True),
    ('إِذَا دَارَ الأَمْرُ بَيْنَ اللِّينِ وَالشِّدَّةِ عَلَى حَدٍّ سَوَاءٍ '
     'فَالأَفْضَلُ اللِّينُ وَالرِّفْق.',
     'When the matter is even between gentleness and firmness, the better '
     'course is gentleness and kindness.', True),
])

b += B.memorize(
    'اتَّقِ اللهَ حَيْثُمَا كُنْتَ، وَأَتْبِعِ السَّيِّئَةَ الحَسَنَةَ '
    'تَمْحُهَا، وَخَالِقِ النَّاسَ بِخُلُقٍ حَسَنٍ',
    'Three commands for the three relationships of a life. <strong>With your '
    'Lord</strong> — fear Him in the place no one sees, for taqwā that stops '
    'in private was taqwā of people. <strong>With your own sins</strong> — do '
    'not despair; follow the slip with a good deed and it wipes it, even when '
    'it is not a formal repentance. <strong>With other people</strong> — a '
    'beautiful character, which is to withhold harm, give kindness, bear what '
    'they do, and meet them with an open face. <em>Between a man and his Lord, '
    'his record, and his neighbour — the ḥadīth leaves no relation '
    'untended.</em>')

b += B.nav('h17-ihsan.html', 'Ḥadīth 17 · الإِحْسَانُ عَلَى كُلِّ شَيْء',
           'index.html', 'Mark complete · أَتْمَمْتَ الدَّرْس · Hadeeth Hub',
           'hd-h18')

B.write('h18-ittaqi-allah.html',
        'اتَّقِ اللهَ حَيْثُمَا كُنْت',
        'Fear Allah Wherever You Are',
        'Ḥadīth 18 of al-Nawawī’s Forty (Abū Dharr & Muʿādh, al-Tirmidhī — '
        'ḥasan) with the sharḥ of Ibn ʿUthaymīn: three commands covering a '
        'man’s three relationships — with his Lord, taqwā as a shield taken '
        'everywhere, open and secret; with his own slips, following a bad deed '
        'with a good one that erases it (general, not repentance alone, on Hūd '
        '11:114 and the ḥadīth of the man who prayed Fajr); and with people, '
        'good character — the inner khuluq versus the outer khalq, its fourfold '
        'definition, its ḍābiṭ in al-Aʿrāf 7:199, and whether it is innate or '
        'acquired. With the benefits: secret versus public taqwā, worship in '
        'unfit places, and that firmness does not contradict good character.',
        18, 'al-Tirmidhī (ḥasan)', '2', b)
print('wrote h18-ittaqi-allah.html')
