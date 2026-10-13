# -*- coding: utf-8 -*-
"""Wasitiyyah L14 -- sections 13-17: hearing and sight again, al-makr wa-l-kayd,
pardon and might, affirming the Name and negating the like, negating the
partner. Sharh pp.58-65."""
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
    'Shaykh <strong>مُحَمَّدُ بْنُ صَالِحٍ العُثَيْمِين</strong>, '
    '<em>شَرْحُ العَقِيدَةِ الوَاسِطِيَّة</em> — a second, fuller sharḥ.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Give the argument from Arabic that %s cannot be an empty name.' % ar('سَمِيعٌ بَصِيرٌ'),
    'Define %s as it is ascribed to Allah, and distinguish the two kinds of %s.'
    % (ar('المَكْر'), ar('الكَيْد')),
    'State the rule that %s, and give al-Fawzān’s examples.'
    % ar('الفِعْلُ أَوْسَعُ مِنَ الاسْمِ'),
    'State the general rule for what is negated of Allah in the Book and the Sunnah.',
])

b += B.heading('١٣ · إِثْبَاتُ السَّمْعِ وَالبَصَرِ — تَمَامُ الحُجَّة',
               'Section 13 — Hearing and Sight: the Argument Completed')
b += B.sharh(
    p('The author brings the āyāt of hearing and sight again, and here al-Fawzān completes the '
      'argument he began in Lesson 10. He notes first <em>how</em> the Qurʾān affirms it — '
      'hearing is ascribed to Allah in <strong>three grammatical forms</strong>: the past verb '
      '%s, the present verb %s, and the active participle %s.'
      % (ar('سَمِعَ'), ar('يَسْمَعُ'), ar('سَمِيعٌ'))) +
    p('And then the argument itself, which needs no technical apparatus at all:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.93rem">— <strong>It is not valid in the speech of the '
    'Arabs to say of anything that it is “hearing, seeing” unless that thing actually hears and '
    'sees.</strong> This is the default. <em>So one does not say: a hearing, seeing '
    '<strong>mountain</strong></em> — because that is impossible except for something that '
    'hears and sees.</p></div>' +
    p('That single sentence disposes of the Jahmī position met in Lesson 5 — that the names are '
      'bare words carrying no attribute, so that %s indicates no hearing. If that were how '
      'language worked, you could call a mountain <em>samīʿ baṣīr</em> and mean nothing by it. '
      'Nobody does, because nobody can.' % ar('السَّمِيع')))

b += B.heading('١٤ · إِثْبَاتُ المَكْرِ وَالكَيْدِ عَلَى مَا يَلِيقُ بِه',
               'Section 14 — Stratagem and Plan, as Befits Him')
b += B.matn(
    'وَقَوْلُهُ: ﴿وَهُوَ شَدِيدُ الْمِحَالِ﴾، وَقَوْلُهُ: ﴿وَمَكَرُوا وَمَكَرَ اللَّهُ '
    'وَاللَّهُ خَيْرُ الْمَاكِرِينَ﴾، وَقَوْلُهُ: ﴿وَمَكَرُوا مَكْرًا وَمَكَرْنَا مَكْرًا '
    'وَهُمْ لَا يَشْعُرُونَ﴾، وَقَوْلُهُ: ﴿إِنَّهُمْ يَكِيدُونَ كَيْدًا ۝ وَأَكِيدُ '
    'كَيْدًا﴾.')
b += B.ayah(
    'وَمَكَرُوا وَمَكَرَ اللَّهُ وَاللَّهُ خَيْرُ الْمَاكِرِينَ',
    '"And they schemed, and Allah countered their scheme — and Allah is the best of those who '
    'counter schemes."',
    'Sūrat Āl ʿImrān 3:54 · سورة آل عمران')
b += B.sharh(
    p('<strong>%s</strong> in the language is <em>severity</em> — so: severe in His countering. '
      'al-Zajjāj: <em>one says “I contended with him in miḥāl” when you pit yourself against him '
      'until it becomes clear which of you is stronger.</em> And Ibn al-Aʿrābī says plainly: '
      '%s <em>is</em> %s.' % (ar('المِحَال'), ar('المِحَال'), ar('المَكْر'))) +
    p('And here is the definition that keeps the attribute clean, which al-Fawzān states '
      'outright: <strong>%s</strong> — <em>bringing what is disliked to the one who deserves it, '
      'from where he does not perceive it.</em>'
      % ar('المَكْرُ مِنَ اللهِ: إِيصَالُ المَكْرُوهِ إِلَى مَنْ يَسْتَحِقُّهُ مِنْ حَيْثُ لَا يَشْعُرُ')) +
    p('The context of the Āl ʿImrān āyah is the Children of Israel who plotted to kill ʿĪsā and '
      'crucify him. And %s means <em>He drew them on and repaid them for their scheming</em>.'
      % ar('وَمَكَرَ اللَّهُ')))
b += B.sharh(
    p('al-Fawzān then makes the division that answers the obvious objection — <em>how can '
      'scheming be an attribute of perfection?</em> <strong>%s is of two kinds:</strong>'
      % ar('الكَيْد')) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.55rem .7rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>قَبِيح</strong> — ugly</td>'
    '<td style="padding:.55rem .7rem;border:1px solid var(--line)">bringing it upon one who '
    '<em>does not</em> deserve it — and this is <strong>blameworthy</strong></td></tr>'
    '<tr><td style="padding:.55rem .7rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong>حَسَن</strong> — good</td>'
    '<td style="padding:.55rem .7rem;border:1px solid var(--line)">bringing it upon one who '
    '<em>does</em> deserve it, as a punishment — and this is <strong>praiseworthy</strong></td></tr>'
    '</table></div>' +
    p('<strong>And the Lord does of this only what He is praised for</strong> — out of justice '
      'from Him and wisdom. He seizes the wrongdoer and the transgressor <em>from where he does '
      'not reckon</em> — <strong>not as the oppressors do with the servants of Allah.</strong>') +
    p('al-Fawzān adds the controlling restriction: <strong>Allah did not describe Himself with '
      'plan, stratagem or outwitting except by way of recompense to one who did that '
      'wrongfully.</strong> And then the clinching comparison: <em>it is known that requiting is '
      'good even from a creature — so what of the Creator?</em>'))
b += B.sharh(
    p('<strong>%s</strong> — and this one is a rule you will use far beyond this section. '
      'Ascribing plan and stratagem to Allah is from <strong>%s</strong>, the unrestricted use of '
      'the <em>verb</em> — and <strong>the verb is broader than the name</strong>.'
      % (ar('تَنْبِيه'), ar('إِطْلَاقِ الفِعْلِ'))) +
    p('His proof is elegant: Allah ascribed to Himself <em>verbs</em> from which no name of the '
      'doer was taken. He said %s and %s — yet He is not named %s or %s. Likewise %s and %s — and '
      'one does not name Him by the participle from it.'
      % (ar('أَرَادَ'), ar('شَاءَ'), ar('المُرِيد'), ar('الشَّائِي'),
         ar('مَكَرَ'), ar('يَمْكُرُ'))) +
    p('So the discipline is exact. <strong>What Allah said of Himself as a verb, we say as a '
      'verb. We do not manufacture a name out of it.</strong> This is why the names of Allah are '
      'not open to invention — and it is a direct application of the %s principle from Lesson 4: '
      'this subject is received, not reasoned out.' % ar('تَوْقِيفِيَّة')))

b += B.heading('١٥ · العَفْوُ وَالمَغْفِرَةُ وَالرَّحْمَةُ وَالعِزَّةُ وَالقُدْرَة',
               'Section 15 — Pardon, Forgiveness, Mercy, Might and Power')
b += B.matn(
    'وَقَوْلُهُ تَعَالَى: ﴿إِنْ تُبْدُوا خَيْرًا أَوْ تُخْفُوهُ أَوْ تَعْفُوا عَنْ سُوءٍ '
    'فَإِنَّ اللَّهَ كَانَ عَفُوًّا قَدِيرًا﴾، وَقَوْلُهُ: ﴿وَلِلَّهِ الْعِزَّةُ '
    'وَلِرَسُولِهِ﴾، وَقَوْلُهُ عَنْ إِبْلِيسَ: ﴿قَالَ فَبِعِزَّتِكَ لَأُغْوِيَنَّهُمْ '
    'أَجْمَعِينَ﴾.')
b += B.ayah(
    'إِنْ تُبْدُوا خَيْرًا أَوْ تُخْفُوهُ أَوْ تَعْفُوا عَنْ سُوءٍ فَإِنَّ اللَّهَ كَانَ '
    'عَفُوًّا قَدِيرًا',
    '"If you disclose a good or conceal it, or pardon an offence — then indeed Allah is ever '
    'Pardoning, Able."',
    'Sūrat al-Nisāʾ 4:149 · سورة النساء')
b += B.sharh(
    p('%s — pass over the one who wronged you. And then the two names arrive '
      '<strong>together</strong>, which is the whole lesson of the āyah: Allah is '
      '<strong>%s</strong> toward His servants, passing over them <em>while able to take '
      'retribution from them</em> for what their hands earned.'
      % (ar('أَوْ تَعْفُوا عَنْ سُوءٍ'), ar('عَفُوًّا قَدِيرًا'))) +
    p('al-Fawzān draws the instruction out: <strong>so take Him as your example — for He pardons '
      '<em>while having the power</em>.</strong> Pardon from the powerless is not pardon; it is '
      'inability wearing pardon\'s clothes. The two names are placed side by side so that the '
      'servant knows which kind he is being asked for.'))
b += B.ayah(
    'قَالَ فَبِعِزَّتِكَ لَأُغْوِيَنَّهُمْ أَجْمَعِينَ إِلَّا عِبَادَكَ مِنْهُمُ الْمُخْلَصِينَ',
    '"He said: then by Your might, I will surely mislead them all — except Your servants among '
    'them who are sincere."',
    'Sūrat Ṣād 38:82–83 · سورة ص')
b += B.prose(
    'Note who is speaking, and note where he stops. Iblīs swears <em>by Allah\'s own might</em> '
    'that he will misguide every one of them — and then <strong>makes an exception he was not '
    'asked to make</strong>: the sincere. Even the enemy knows where the wall is. '
    '<em>Ikhlāṣ</em> is named by Iblīs himself as the thing he cannot get past.')

b += B.heading('١٦ · إِثْبَاتُ الاسْمِ لِلَّهِ وَنَفْيُ المِثْلِ عَنْه',
               'Section 16 — Affirming the Name, Negating the Like')
b += B.matn(
    'وَقَوْلُهُ: ﴿تَبَارَكَ اسْمُ رَبِّكَ ذِي الْجَلَالِ وَالْإِكْرَامِ﴾، وَقَوْلُهُ: '
    '﴿فَاعْبُدْهُ وَاصْطَبِرْ لِعِبَادَتِهِ هَلْ تَعْلَمُ لَهُ سَمِيًّا﴾، ﴿وَلَمْ يَكُنْ لَهُ '
    'كُفُوًا أَحَدٌ﴾، ﴿فَلَا تَجْعَلُوا لِلَّهِ أَنْدَادًا وَأَنْتُمْ تَعْلَمُونَ﴾.')
b += B.ayah(
    'تَبَارَكَ اسْمُ رَبِّكَ ذِي الْجَلَالِ وَالْإِكْرَامِ',
    '"Blessed is the name of your Lord, Owner of Majesty and Honour."',
    'Sūrat al-Raḥmān 55:78 · سورة الرحمن')
b += B.sharh(
    p('<strong>%s</strong> in the language is growth and increase; <strong>%s</strong> is '
      'supplicating for blessing. And the meaning of <strong>%s</strong> is <em>He has become '
      'immense, or His affair has risen and become exalted</em> — and al-Fawzān notes that '
      '<strong>this word is not applied to anyone but Allah.</strong>'
      % (ar('البَرَكَة'), ar('التَّبْرِيك'), ar('تَبَارَكَ'))) +
    p('And <strong>%s</strong>: single Him out in worship, and worship no other alongside Him. '
      '%s in the language is <em>lowliness and submission</em>; in the Sharīʿah it is <em>a '
      'comprehensive name for what Allah loves and is pleased with, of deeds and of statements</em> '
      '— the definition you met on the Islam 101 track from Ibn Taymiyyah, arriving here from the '
      'other direction.' % (ar('فَاعْبُدْهُ'), ar('العِبَادَة'))))
b += B.ayah(
    'وَمِنَ النَّاسِ مَنْ يَتَّخِذُ مِنْ دُونِ اللَّهِ أَنْدَادًا يُحِبُّونَهُمْ كَحُبِّ اللَّهِ',
    '"And among mankind are those who take, besides Allah, rivals — loving them as they love '
    'Allah."',
    'Sūrat al-Baqarah 2:165 · سورة البقرة')
b += B.sharh(
    p('al-Fawzān reads it against the āyah before it, which had established Allah\'s oneness by a '
      'plain proof of His immense dominion and His being alone in creating. <em>And even with '
      'that proof standing</em>, He informs us that there are still found among people those who '
      'take a rival beside Him and worship it — <strong>powerless idols</strong>.') +
    p('And then the precise point: %s means these disbelievers <em>did not stop at merely '
      'worshipping those rivals; they loved them with an immense love and went to excess in '
      'loving them, as they love Allah.</em> So — and this is the sentence to keep — '
      '<strong>%s</strong>: they equated them with Allah <em>in love</em>, not in creating, '
      'providing and governing.'
      % (ar('يُحِبُّونَهُمْ كَحُبِّ اللَّهِ'),
         ar('فَقَدْ سَوَّوْهُمْ بِاللهِ فِي المَحَبَّةِ لَا فِي الخَلْقِ وَالرِّزْقِ وَالتَّدْبِيرِ'))) +
    p('If that rings a bell, it should. It is exactly the explanation Ibn Taymiyyah and Ibn '
      'al-Qayyim gave for the confession in the Fire — %s (al-Shuʿarāʾ 26:98) — which you studied '
      'as the capstone of <em>al-Qawāʿid al-Arbaʿ</em>. Two different books, two different '
      'authors, the same analysis of the same error.' % ar('إِذْ نُسَوِّيكُمْ بِرَبِّ الْعَالَمِينَ')))
b += B.sharh(
    p('<strong>The shāhid</strong> of the section, and with it a rule for the whole subject: the '
      'āyāt affirm the Name of Allah and His magnification, <em>and</em> negate the namesake, the '
      'equal and the rival — and that negation is <strong>%s</strong>, a <em>summary</em> '
      'negation.' % ar('نَفْيٌ مُجْمَلٌ')) +
    p('al-Fawzān then states the general principle: <strong>this is the way that comes in the '
      'Book and the Sunnah regarding what is negated of Allah — that there be negated of Him '
      '<em>everything which contradicts His necessary perfection</em>, of the kinds of defect '
      'and deficiency.</strong>') +
    p('Hold that beside Lesson 6. The <em>affirmation</em> in the Qurʾān is detailed and specific '
      '— the Face, the Hands, the hearing, the mercy, each named. The <em>negation</em> is '
      'summary — no like, no equal, no rival, no defect. <strong>Detailed in what it affirms, '
      'general in what it denies.</strong> The muʿaṭṭilah inverted exactly that: general about '
      'the affirmation, exhaustively detailed about the denial.'))

b += B.heading('١٧ · نَفْيُ الشَّرِيكِ عَنِ اللهِ تَعَالَى', 'Section 17 — Negating the Partner')
b += B.matn(
    'وَقَوْلُهُ: ﴿وَقُلِ الْحَمْدُ لِلَّهِ الَّذِي لَمْ يَتَّخِذْ وَلَدًا وَلَمْ يَكُنْ لَهُ '
    'شَرِيكٌ فِي الْمُلْكِ وَلَمْ يَكُنْ لَهُ وَلِيٌّ مِنَ الذُّلِّ وَكَبِّرْهُ تَكْبِيرًا﴾.')
b += B.ayah(
    'وَقُلِ الْحَمْدُ لِلَّهِ الَّذِي لَمْ يَتَّخِذْ وَلَدًا وَلَمْ يَكُنْ لَهُ شَرِيكٌ فِي '
    'الْمُلْكِ وَلَمْ يَكُنْ لَهُ وَلِيٌّ مِنَ الذُّلِّ وَكَبِّرْهُ تَكْبِيرًا',
    '"And say: all praise belongs to Allah, who has not taken a son, and who has no partner in '
    'dominion, and who has no helper out of weakness — and magnify Him greatly."',
    'Sūrat al-Isrāʾ 17:111 · سورة الإسراء')
b += B.sharh(
    p('%s is praise, and the article on it is <strong>%s</strong>, for totality: <em>all</em> '
      'praise belongs to Allah. Then three denials, and al-Fawzān names the party answered by '
      'each:' % (ar('الحَمْد'), ar('لِلاسْتِغْرَاق'))) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.88rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.55rem .7rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar">لَمْ يَتَّخِذْ وَلَدًا</td>'
    '<td style="padding:.55rem .7rem;border:1px solid var(--line)">He has no son — against '
    '<strong>the Jews, the Christians, and some of the mushrikūn of the Arabs</strong></td></tr>'
    '<tr><td style="padding:.55rem .7rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar">وَلَمْ يَكُنْ لَهُ شَرِيكٌ فِي المُلْكِ</td>'
    '<td style="padding:.55rem .7rem;border:1px solid var(--line)">no partner in His dominion and '
    'Lordship — against <strong>the dualists</strong> and whoever holds a plurality of '
    'gods</td></tr>'
    '<tr><td style="padding:.55rem .7rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar">وَلَمْ يَكُنْ لَهُ وَلِيٌّ مِنَ الذُّلِّ</td>'
    '<td style="padding:.55rem .7rem;border:1px solid var(--line)">no ally taken out of '
    'weakness — He needs no helper at all</td></tr>'
    '</table></div>' +
    p('And then the command that closes it: <strong>%s</strong>. The āyah does not end with the '
      'denials; it ends by telling you what to <em>do</em> once they are settled — magnify Him, '
      'and magnify Him greatly. Every section of this book has been building toward a '
      'disposition, not only a position.' % ar('وَكَبِّرْهُ تَكْبِيرًا')))

b += B.vocab([
    ('المِحَال', 'al-miḥāl', 'severity, countering',
     'Ibn al-Aʿrābī: it <em>is</em> al-makr'),
    ('المَكْر', 'al-makr', 'stratagem',
     'From Allah: bringing what is disliked to one who deserves it, unperceived'),
    ('الكَيْد', 'al-kayd', 'plan',
     'Two kinds: ugly, upon one undeserving; good, upon one deserving'),
    ('الفِعْلُ أَوْسَعُ مِنَ الاسْم', 'al-fiʿl awsaʿ min al-ism',
     'the verb is broader than the name',
     'He said أَرَادَ and شَاءَ, yet is not named المُرِيد or الشَّائِي'),
    ('تَبَارَكَ', 'tabāraka', 'blessed is',
     'He has become immense — a word applied to none but Allah'),
    ('نَفْيٌ مُجْمَل', 'nafy mujmal', 'summary negation',
     'Detailed in what it affirms, general in what it denies'),
    ('الثَّنَوِيَّة', 'al-thanawiyyah', 'the dualists',
     'Answered by: no partner in His dominion'),
])
b += B.mcq('ws-l14', [
    ('What is the argument from Arabic that %s cannot be an empty name?'
     % ar('سَمِيعٌ بَصِيرٌ'),
     ['That the Companions understood it so',
      'That one does not say "a hearing, seeing mountain" — the description is impossible except '
      'for what actually hears and sees',
      'That the word appears many times',
      'That the Qurʾān is in clear Arabic'], 1),
    ('How does al-Fawzān define %s as ascribed to Allah?' % ar('المَكْر'),
     ['Deceiving the innocent',
      'Bringing what is disliked to the one who deserves it, from where he does not perceive it',
      'Changing His decree', 'Concealing His knowledge'], 1),
    ('What are the two kinds of %s?' % ar('الكَيْد'),
     ['Open and hidden',
      'Ugly — upon one who does not deserve it; and good — upon one who does, as punishment',
      'Worldly and otherworldly', 'Permitted and forbidden'], 1),
    ('What does the rule %s establish?' % ar('الفِعْلُ أَوْسَعُ مِنَ الاسْمِ'),
     ['That verbs are more numerous than nouns in Arabic',
      'That what Allah said of Himself as a verb is said as a verb — a name is not manufactured '
      'from it; He said أَرَادَ yet is not named المُرِيد',
      'That the names may be derived freely',
      'That the attributes are figurative'], 1),
    ('Why are %s placed together in al-Nisāʾ 4:149?' % ar('عَفُوًّا قَدِيرًا'),
     ['For rhyme',
      'Because He pardons <em>while able</em> — so the servant knows which kind of pardon he is '
      'asked for',
      'Because power requires pardon', 'To warn of punishment'], 1),
    ('In what respect did those of al-Baqarah 2:165 equate the rivals with Allah?',
     ['In creating and providing',
      'In love — not in creating, providing or governing',
      'In knowledge of the unseen', 'In power over life and death'], 1),
    ('What is the general rule for what is negated of Allah?',
     ['That only what the Qurʾān names explicitly is negated',
      'That everything contradicting His necessary perfection is negated — the kinds of defect '
      'and deficiency, as a summary negation',
      'That nothing may be negated of Him',
      'That negation is left to the intellect'], 1),
])
b += B.tf('ws-l14-tf', [
    ('يُقَالُ فِي لُغَةِ العَرَبِ: جَبَلٌ سَمِيعٌ بَصِيرٌ.',
     'In Arabic one may say: a hearing, seeing mountain.', False),
    ('لَمْ يَصِفِ اللهُ نَفْسَهُ بِالمَكْرِ إِلَّا عَلَى وَجْهِ الجَزَاءِ.',
     'Allah described Himself with makr only by way of recompense.', True),
    ('لَفْظُ «تَبَارَكَ» لَا يُطْلَقُ إِلَّا عَلَى اللهِ.',
     'The word tabāraka is applied to none but Allah.', True),
    ('إِبْلِيسُ اسْتَثْنَى المُخْلَصِينَ مِنْ إِغْوَائِهِ.',
     'Iblīs excepted the sincere from those he would misguide.', True),
])
b += B.memorize(
    'فَإِنَّ اللَّهَ كَانَ عَفُوًّا قَدِيرًا',
    'Two names that must be read together. He pardons — and He was never unable to do otherwise. '
    'When you are wronged and have the upper hand, this is the āyah you are being measured '
    'against.')
b += B.aiquiz('Hearing and sight, al-makr wa-l-kayd, pardon and might, and the negating of a like '
              'and a partner in al-Aqidah al-Wasitiyyah: the hearing seeing mountain argument, '
              'the two kinds of kayd, the rule that the verb is broader than the name, and that '
              'the Quran is detailed in affirmation and summary in negation')
b += B.further()
b += B.nav('was-l13-wajh-yadayn-aynayn.html', 'The Face, the Hands, the Eyes',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l14')

io.open(os.path.join(B.AQ, 'was-l14-makr-izzah-nafy.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'المَكْرُ وَالعِزَّةُ وَنَفْيُ المِثْلِ وَالشَّرِيك',
    'Stratagem, Might, and the Negating of Like and Partner',
    'Lesson 14 of al-ʿAqīdah al-Wāsiṭiyyah: the argument that a mountain is '
    'never called “hearing and seeing,” the two kinds of kayd and why only the '
    'praiseworthy belongs to Allah, the rule that the verb is broader than the name, and that the '
    'Qurʾān is detailed in what it affirms and summary in what it denies.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الرَّابِعَ عَشَر', '3',
           'المَكْرُ وَالعِزَّةُ وَنَفْيُ المِثْلِ وَالشَّرِيك',
           'Stratagem, Might, and the Negating of Like and Partner', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l14-makr-izzah-nafy.html')
