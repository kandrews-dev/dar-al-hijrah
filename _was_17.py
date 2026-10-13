# -*- coding: utf-8 -*-
"""Wasitiyyah L17 -- section 20: the ma'iyyah of Allah with His creation. The
two kinds, general and particular, and how being WITH the creation does not
contradict being ABOVE it. Sharh pp.75-78."""
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
    'الإِمَامُ <strong>الشَّوْكَانِيّ</strong>, <em>فَتْحُ القَدِير</em> — quoted by al-Fawzān '
    'in this section on the maʿiyyah of the patient.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Distinguish %s from %s, and say what each one entails.'
    % (ar('المَعِيَّةُ العَامَّة'), ar('المَعِيَّةُ الخَاصَّة')),
    'Explain why %s is always glossed by al-Fawzān with %s in the general kind.'
    % (ar('مَعَكُمْ'), ar('بِعِلْمِهِ')),
    'Reconcile Allah’s being %s with His being %s, in the two ways al-Fawzān gives.'
    % (ar('مَعَ خَلْقِه'), ar('عَالِيًا عَلَيْهِم')),
    'Give the Arabs’ own example that shows %s does not require touching or being level with.'
    % ar('المَعِيَّة'),
])

b += B.heading('٢٠ · إِثْبَاتُ مَعِيَّةِ اللهِ لِخَلْقِه',
               'Section 20 — The Maʿiyyah of Allah with His Creation')
b += B.matn(
    'وَقَوْلُهُ: ﴿وَهُوَ مَعَكُمْ أَيْنَ مَا كُنْتُمْ وَاللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ﴾، '
    'وَقَوْلُهُ: ﴿مَا يَكُونُ مِنْ نَجْوَى ثَلَاثَةٍ إِلَّا هُوَ رَابِعُهُمْ وَلَا خَمْسَةٍ '
    'إِلَّا هُوَ سَادِسُهُمْ وَلَا أَدْنَى مِنْ ذَلِكَ وَلَا أَكْثَرَ إِلَّا هُوَ مَعَهُمْ '
    'أَيْنَ مَا كَانُوا﴾، وَقَوْلُهُ: ﴿لَا تَحْزَنْ إِنَّ اللَّهَ مَعَنَا﴾، ﴿إِنَّنِي '
    'مَعَكُمَا أَسْمَعُ وَأَرَى﴾، ﴿إِنَّ اللَّهَ مَعَ الَّذِينَ اتَّقَوْا وَالَّذِينَ هُمْ '
    'مُحْسِنُونَ﴾، ﴿وَاصْبِرُوا إِنَّ اللَّهَ مَعَ الصَّابِرِينَ﴾، ﴿كَمْ مِنْ فِئَةٍ '
    'قَلِيلَةٍ غَلَبَتْ فِئَةً كَثِيرَةً بِإِذْنِ اللَّهِ وَاللَّهُ مَعَ الصَّابِرِينَ﴾.')
b += B.prose(
    'The author places this section immediately after the Throne and the highness, and that '
    'placement is the argument. Having just established that Allah is <strong>above</strong> His '
    'creation, he now brings every text that says He is <strong>with</strong> them — because the '
    'muʿaṭṭilah had used these very āyāt to cancel the first set. al-Fawzān will show that the '
    'two are not in competition, but he does the work in the right order: first establish what '
    'each kind of maʿiyyah actually entails, and only then reconcile.')

b += B.heading('النَّوْعُ الأَوَّل · المَعِيَّةُ العَامَّة',
               'The First Kind — the General Maʿiyyah')
b += B.ayah(
    'يَعْلَمُ مَا يَلِجُ فِي الْأَرْضِ وَمَا يَخْرُجُ مِنْهَا وَمَا يَنْزِلُ مِنَ السَّمَاءِ '
    'وَمَا يَعْرُجُ فِيهَا وَهُوَ مَعَكُمْ أَيْنَ مَا كُنْتُمْ وَاللَّهُ بِمَا تَعْمَلُونَ '
    'بَصِيرٌ',
    '"He knows what penetrates into the earth and what comes out of it, and what descends from '
    'the heaven and what ascends into it; and He is with you wherever you are — and Allah is '
    'Seeing of what you do."',
    'Sūrat al-Ḥadīd 57:4 · سورة الحديد')
b += B.sharh(
    p('al-Fawzān glosses it exactly: <strong>%s</strong> — <em>He is with you '
      '<strong>by His knowledge</strong>; watching over you, witnessing your deeds — wherever '
      'you were and wherever you are, on land or at sea, by night or by day.</em> And He hears '
      'your speech and sees your place.' % ar('وَهُوَ مَعَكُمْ أَيْنَ مَا كُنْتُمْ')) +
    p('<strong>And this is the place of the shāhid from the noble āyah: in it is the affirming of '
      'the general maʿiyyah.</strong> Then <strong>%s</strong> — <em>nothing of your deeds is '
      'hidden from Him.</em>' % ar('وَاللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ')) +
    p('Notice that the āyah itself supplies the gloss. It opens with %s and closes with %s. '
      '<strong>The maʿiyyah sits between two statements of knowing and seeing</strong> — the '
      'context tells you what kind of withness is meant before any theologian arrives to argue '
      'about it.' % (ar('يَعْلَمُ'), ar('بَصِيرٌ'))))
b += B.ayah(
    'مَا يَكُونُ مِنْ نَجْوَى ثَلَاثَةٍ إِلَّا هُوَ رَابِعُهُمْ وَلَا خَمْسَةٍ إِلَّا هُوَ '
    'سَادِسُهُمْ وَلَا أَدْنَى مِنْ ذَلِكَ وَلَا أَكْثَرَ إِلَّا هُوَ مَعَهُمْ أَيْنَ مَا '
    'كَانُوا ثُمَّ يُنَبِّئُهُمْ بِمَا عَمِلُوا يَوْمَ الْقِيَامَةِ إِنَّ اللَّهَ بِكُلِّ '
    'شَيْءٍ عَلِيمٌ',
    '"There is no secret counsel of three but He is the fourth of them, nor of five but He is the '
    'sixth of them, nor fewer than that nor more, but He is with them wherever they are. Then He '
    'will inform them of what they did on the Day of Rising. Indeed Allah is Knowing of '
    'everything."',
    'Sūrat al-Mujādilah 58:7 · سورة المجادلة')
b += B.sharh(
    p('<strong>%s</strong> is <em>the secret</em>, so the meaning is: <em>no private conferring '
      'of three comes to be…</em> And <strong>%s</strong> means <em>making Himself their fourth '
      'and their sixth — in the sense that He shares with them in being informed of that private '
      'counsel</em>; He knows what they confer about and nothing of it is hidden from Him.'
      % (ar('النَّجْوَى'), ar('إِلَّا هُوَ رَابِعُهُمْ وَلَا خَمْسَةٍ إِلَّا هُوَ سَادِسُهُمْ'))) +
    p('And why three and five in particular? al-Fawzān gives the two explanations: either <em>the '
      'wording came out in terms of what is customary</em>, or <em>the cause of revelation was '
      'the private conferring of three in one incident and five in another</em>. '
      '<strong>Otherwise He سبحانه is with every number, few or many</strong> — and the āyah says '
      'so itself: <strong>%s</strong>, <em>neither fewer than the number mentioned, such as one '
      'or two, nor more than it, such as six or seven.</em>'
      % ar('وَلَا أَدْنَى مِنْ ذَلِكَ وَلَا أَكْثَرَ')))
b += B.prose(
    'The cause of revelation, as al-Fawzān reports it: the Jews used to confer privately among '
    'themselves, and the believers thought they were conferring about what would harm them, and '
    'grieved over it. When it went on and increased, they complained to the Messenger of Allah '
    '&#65018;, and he ordered the Jews not to confer privately apart from the Muslims. '
    '<strong>They did not stop, and went back to their private conferring — so Allah revealed '
    'these āyāt.</strong> The answer given to the believers\' anxiety was not surveillance; it '
    'was: <em>He is already the fourth of every three.</em>')
b += B.sharh(
    p('<strong>%s</strong> — the meaning is <em>the encompassing of His knowledge, سبحانه, of '
      'every private counsel that occurs from them in any place</em>. Then <strong>%s</strong> — '
      '<em>He will inform them</em>, and <em>recompense them for it; and in this is a threat to '
      'them and a rebuke.</em>'
      % (ar('أَيْنَ مَا كَانُوا'), ar('ثُمَّ يُنَبِّئُهُمْ بِمَا عَمِلُوا'))) +
    p('And now the structural observation that settles the meaning of the whole āyah — '
      '<strong>%s</strong>: this general maʿiyyah, <em>whose entailment is '
      '<strong>knowledge</strong></em>. al-Fawzān points out that Allah '
      '<strong>opened the āyah with knowledge</strong> — %s — <strong>and sealed it with '
      'knowledge</strong> — %s. The maʿiyyah is enclosed on both sides by ʿilm. '
      '<strong>The verse interprets itself.</strong>'
      % (ar('مُقْتَضَاهَا العِلْم'), ar('أَلَمْ تَرَ أَنَّ اللَّهَ يَعْلَمُ'),
         ar('إِنَّ اللَّهَ بِكُلِّ شَيْءٍ عَلِيمٌ'))))

b += B.heading('النَّوْعُ الثَّانِي · المَعِيَّةُ الخَاصَّة',
               'The Second Kind — the Particular Maʿiyyah')
b += B.ayah(
    'إِذْ يَقُولُ لِصَاحِبِهِ لَا تَحْزَنْ إِنَّ اللَّهَ مَعَنَا',
    '"When he said to his companion: do not grieve — indeed Allah is with us."',
    'Sūrat al-Tawbah 9:40 · سورة التوبة')
b += B.sharh(
    p('<em>This is an address from the Prophet &#65018; to his companion Abū Bakr '
      '&#1585;&#1590;&#1610; &#1575;&#1604;&#1604;&#1607; &#1593;&#1606;&#1607; when the two of '
      'them were in the cave at the time of the Hijrah and the mushrikūn had caught up with them. '
      'So Abū Bakr grieved, out of fear for the Prophet &#65018; from the harm of the '
      'disbelievers.</em>') +
    p('Note what he grieved <em>about</em>: not himself. And the answer: <strong>%s</strong> — '
      '<em>leave off the grieving</em> — <strong>%s</strong> — <em>with His aid, His help and His '
      'support.</em>' % (ar('لَا تَحْزَنْ'), ar('إِنَّ اللَّهَ مَعَنَا'))) +
    p('And then al-Fawzān\'s two-step conclusion, which is as much consolation as it is '
      'doctrine: <strong>%s</strong> — <em>and whoever has Allah with him will never be '
      'overcome; and whoever is not overcome, it is not fitting for him to grieve.</em>'
      % ar('وَمَنْ كَانَ اللهُ مَعَهُ فَلَنْ يُغْلَبَ، وَمَنْ لَا يُغْلَبُ لَا يَحِقُّ لَهُ أَنْ يَحْزَنَ')) +
    p('<strong>And the shāhid from the āyah: in it is the affirming of the particular maʿiyyah, '
      'belonging to the believers, whose entailment is victory and support.</strong>'))
b += B.ayah(
    'قَالَ لَا تَخَافَا إِنَّنِي مَعَكُمَا أَسْمَعُ وَأَرَى',
    '"He said: do not fear, I am with the two of you — I hear and I see."',
    'Sūrat Ṭā-Hā 20:46 · سورة طه')
b += B.sharh(
    p('Spoken to Mūsā and Hārūn &#1593;&#1604;&#1610;&#1607;&#1605;&#1575; '
      '&#1575;&#1604;&#1587;&#1604;&#1575;&#1605;: <em>do not fear Pharaoh.</em> And '
      '<strong>%s is a reason given for the prohibition</strong> — <em>that is: with you both, '
      'by granting the two of you victory and by help against Pharaoh.</em> Grammatically the '
      'āyah does not merely reassure; <strong>it explains the reassurance.</strong>'
      % ar('إِنَّنِي مَعَكُمَا')) +
    p('<strong>%s</strong> — <em>your speech and his speech</em>; <strong>%s</strong> — <em>your '
      'place and his place; nothing of your affair is hidden from Me.</em>'
      % (ar('أَسْمَعُ'), ar('وَأَرَى'))) +
    p('<strong>And the shāhid: the affirming of the particular maʿiyyah on Allah\'s part for His '
      'allies, by victory and support — as there is in it also the affirming of hearing and sight '
      'for Him سبحانه وتعالى.</strong> One āyah, carrying two sections of this book at once.'))
b += B.ayah(
    'إِنَّ اللَّهَ مَعَ الَّذِينَ اتَّقَوْا وَالَّذِينَ هُمْ مُحْسِنُونَ',
    '"Indeed Allah is with those who have taqwā, and those who are doers of good."',
    'Sūrat al-Naḥl 16:128 · سورة النحل')
b += B.sharh(
    p('al-Fawzān reads the two descriptions as the two halves of the religion. '
      '<strong>%s</strong> — <em>they abandoned the forbidden things and the acts of '
      'disobedience, in their differing kinds</em> — and <strong>%s</strong> — <em>by discharging '
      'the acts of obedience and undertaking what they were commanded with.</em> '
      '<strong>Leaving and doing.</strong>'
      % (ar('الَّذِينَ اتَّقَوْا'), ar('وَالَّذِينَ هُمْ مُحْسِنُونَ'))) +
    p('<em>So He سبحانه is with these, by His support and His aid and His help; '
      '<strong>and this is a particular maʿiyyah</strong>, and it is the place of the shāhid from '
      'the noble āyah.</em>') +
    p('Which is the practical point of the whole section. The general maʿiyyah is not earned and '
      'cannot be escaped — He is the fourth of every three, including the three plotting against '
      'you. <strong>The particular maʿiyyah is conditional</strong>, and the āyah names the two '
      'conditions.'))
b += B.ayah(
    'وَاصْبِرُوا إِنَّ اللَّهَ مَعَ الصَّابِرِينَ',
    '"And be patient — indeed Allah is with the patient."',
    'Sūrat al-Anfāl 8:46 · سورة الأنفال')
b += B.sharh(
    p('<strong>%s — this is a command to patience, and it is the restraining of the self.</strong> '
      'What is intended by it here is <em>patience upon the hardships of the war that is between '
      'the Muslims and the disbelievers</em>. <em>Then He gave the reason for this command with '
      'His saying %s — so He سبحانه is with the patient <strong>in every affair in which patience '
      'is called for</strong>.</em>' % (ar('وَاصْبِرُوا'), ar('إِنَّ اللَّهَ مَعَ الصَّابِرِينَ'))) +
    p('And al-Fawzān closes it with al-Shawkānī, whose words are worth keeping as they stand: '
      '<em>and how excellent is this maʿiyyah — <strong>the one granted it is not overcome by any '
      'overcomer, and its possessor is not got at from any direction, however many the directions '
      'be.</strong></em>'))
b += B.ayah(
    'كَمْ مِنْ فِئَةٍ قَلِيلَةٍ غَلَبَتْ فِئَةً كَثِيرَةً بِإِذْنِ اللَّهِ وَاللَّهُ مَعَ '
    'الصَّابِرِينَ',
    '"How many a small company has overcome a large company, by the permission of Allah — and '
    'Allah is with the patient."',
    'Sūrat al-Baqarah 2:249 · سورة البقرة')
b += B.sharh(
    p('<strong>%s</strong> — <em>by His will, His decree and His volition.</em> The small company '
      'does not win by being brave; it wins by permission. Take the %s out of the āyah and it '
      'becomes a slogan; leave it in and it is tawḥīd.'
      % (ar('بِإِذْنِ اللَّهِ'), ar('بِإِذْنِ اللَّهِ'))) +
    p('<strong>%s — this is the place of the shāhid from the noble āyah: the affirming of the '
      'maʿiyyah of Allah سبحانه for those patient upon jihād in His path; and it is a particular '
      'maʿiyyah whose entailment is victory and support.</strong>'
      % ar('وَاللَّهُ مَعَ الصَّابِرِينَ')))

b += B.heading('مَا يُسْتَفَادُ مِنْ مَجْمُوعِ الآيَات', 'What the Āyāt Yield Together')
b += B.sharh(
    p('<strong>%s</strong> — <em>they conveyed the affirming of the maʿiyyah, and that it is of '
      'two kinds:</em>' % ar('المَعِيَّةُ نَوْعَان')) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>المَعِيَّةُ العَامَّة</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">as in the first two '
    'āyāt. Its entailment: <strong>His encompassing of His creation, and His knowledge '
    'of their deeds — the good of them and the evil — and His recompensing them for '
    'them.</strong></td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>المَعِيَّةُ الخَاصَّة</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">with His believing servants. '
    'Its entailment: <strong>victory, support and preservation.</strong> Indicated by the '
    '<strong>five remaining āyāt</strong> the author brought.</td></tr>'
    '</table></div>' +
    p('Two kinds, and only one of them is a privilege. Both are real, and neither is a figure of '
      'speech.'))

b += B.heading('لَا تَنَافِي بَيْنَ المَعِيَّةِ وَالعُلُوّ',
               'No Contradiction Between the Maʿiyyah and the Highness')
b += B.sharh(
    p('Now the resolution, and al-Fawzān states it as a flat denial: <strong>%s</strong> — '
      '<em>and His maʿiyyah سبحانه <strong>does not contradict</strong> His highness above His '
      'creation and His istiwāʾ upon His Throne.</em> He then gives two grounds.'
      % ar('وَمَعِيَّتُهُ سُبْحَانَهُ لَا تُنَافِي عُلُوَّهُ عَلَى خَلْقِه')) +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.93rem">'
    '<p style="margin:0 0 .7rem"><strong>الأَوَّل · His nearness is not the creature’s '
    'nearness.</strong> <em>For His nearness سبحانه and His maʿiyyah are not like the '
    'nearness of the created thing and the maʿiyyah of a created thing with a created '
    'thing</em> — because <span dir="rtl" lang="ar">لَيْسَ كَمِثْلِهِ شَيْءٌ وَهُوَ '
    'السَّمِيعُ البَصِيرُ</span> (al-Shūrā 42:11). The same āyah that governed '
    'every attribute in Lesson 6 governs this one.</p>'
    '<p style="margin:0"><strong>الثَّانِي · Maʿiyyah in the language does not mean '
    'contact.</strong> <em>Because al-maʿiyyah is <strong>unrestricted accompaniment</strong> '
    '— it does not require touching, nor being on the same level.</em> '
    '<strong>The Arabs say: <span dir="rtl" lang="ar">مَا زِلْنَا نَمْشِي وَالقَمَرُ '
    'مَعَنَا</span></strong> — <em>we kept walking and the moon was with us</em> — '
    '<em>even though it is above them, and the distance between them and it is far.</em></p></div>' +
    p('That example is the whole answer, and it costs nothing to understand. No Arab who says '
      '<em>the moon was with us</em> is claiming the moon walked beside him, and no Arab hearing '
      'it imagines he is. <strong>%s is a word about accompaniment, not about position</strong> — '
      'so an āyah affirming it was never in competition with an āyah affirming height.'
      % ar('مَعَ')) +
    p('<em>So the highness of Allah جَلَّ جَلَالُهُ and His maʿiyyah with His creation — '
      '<strong>there is no contradiction between the two of them.</strong> And more clarification '
      'of this is to come, إِنْ شَاءَ اللهُ.</em>') +
    p('Keep that last promise in view: the author returns to this. What has been settled here is '
      'the <em>linguistic</em> point. The fuller treatment of how the attributes are affirmed '
      'without taʿṭīl or tamthīl comes later in the book.'))

b += B.vocab([
    ('المَعِيَّة', 'al-maʿiyyah', 'withness, accompaniment',
     'Unrestricted accompaniment — it requires no touching and no being level'),
    ('المَعِيَّةُ العَامَّة', 'al-maʿiyyah al-ʿāmmah', 'the general withness',
     'With all creation; entails encompassing, knowledge and recompense'),
    ('المَعِيَّةُ الخَاصَّة', 'al-maʿiyyah al-khāṣṣah',
     'the particular withness',
     'With the believers; entails victory, support and preservation'),
    ('النَّجْوَى', 'al-najwā', 'secret counsel',
     'He is the fourth of every three, whatever the number'),
    ('مُقْتَضَى', 'muqtaḍā', 'entailment, what it requires',
     'The key question for each kind: knowledge, or victory?'),
    ('الصَّبْر', 'al-ṣabr', 'patience',
     'The restraining of the self — here, upon the hardships of war'),
    ('التَّنَافِي', 'al-tanāfī', 'mutual contradiction',
     'What does NOT exist between the maʿiyyah and the ʿuluww'),
])
b += B.mcq('ws-l17', [
    ('What does al-Fawzān say the general maʿiyyah entails?',
     ['His presence in every place',
      'His encompassing of His creation, His knowledge of their deeds, and His recompensing them',
      'His victory and support for them', 'His touching of the creation'], 1),
    ('How does al-Mujādilah 58:7 interpret its own maʿiyyah?',
     ['By mentioning the Throne',
      'By opening with knowledge and sealing with knowledge, so the maʿiyyah sits enclosed '
      'between them',
      'By naming the Jews explicitly', 'By mentioning the Day of Rising'], 1),
    ('Why does the āyah mention three and five in particular?',
     ['Because those numbers are blessed',
      'Either because the wording came out in terms of what is customary, or because the cause of '
      'revelation involved three in one incident and five in another',
      'Because the plotters were exactly eight',
      'To exclude larger numbers'], 1),
    ('What did Abū Bakr رضي الله عنه grieve about in the cave?',
     ['For himself, fearing capture',
      'Out of fear for the Prophet ﷺ from the harm of the disbelievers',
      'For the believers left in Makkah', 'For the loss of his wealth'], 1),
    ('What are the two conditions of the particular maʿiyyah in al-Naḥl 16:128?',
     ['Knowledge and action',
      'Taqwā — abandoning the forbidden — and iḥsān: discharging the obedience commanded',
      'Hijrah and jihād', 'Patience and gratitude'], 1),
    ('Which āyah does al-Fawzān cite to show His nearness is unlike the creature’s?',
     ['%s (al-Ikhlāṣ 112:4)' % ar('وَلَمْ يَكُنْ لَهُ كُفُوًا أَحَدٌ'),
      '%s (al-Shūrā 42:11)' % ar('لَيْسَ كَمِثْلِهِ شَيْءٌ وَهُوَ السَّمِيعُ الْبَصِيرُ'),
      '%s (al-Baqarah 2:255)' % ar('اللَّهُ لَا إِلَهَ إِلَّا هُوَ'),
      '%s (Ṭā-Hā 20:5)' % ar('الرَّحْمَنُ عَلَى الْعَرْشِ اسْتَوَى')], 1),
    ('What is the Arabs’ own example that maʿiyyah requires no contact?',
     ['"The sea is with the sailor"',
      '"We kept walking and the moon was with us" — though it is above them and far off',
      '"The shadow is with the man"', '"The wind is with the traveller"'], 1),
])
b += B.tf('ws-l17-tf', [
    ('المَعِيَّةُ تَقْتَضِي المُمَاسَّةَ وَالمُحَاذَاةَ.',
     'Maʿiyyah requires touching and being on the same level.', False),
    ('المَعِيَّةُ الخَاصَّةُ مُقْتَضَاهَا النَّصْرُ وَالتَّأْيِيدُ.',
     'The particular maʿiyyah entails victory and support.', True),
    ('مَعِيَّةُ اللهِ تُنَافِي عُلُوَّهُ عَلَى خَلْقِهِ.',
     'Allah’s maʿiyyah contradicts His highness above His creation.', False),
    ('مَنْ كَانَ اللهُ مَعَهُ فَلَنْ يُغْلَبَ.',
     'Whoever has Allah with him will never be overcome.', True),
])
b += B.memorize(
    'لَا تَحْزَنْ إِنَّ اللَّهَ مَعَنَا',
    'Two men in a cave, the search party at the mouth of it, and the whole of the answer is a '
    'statement about Allah rather than about the odds. al-Fawzān\'s chain is worth carrying: '
    'whoever has Allah with him will never be overcome — and whoever is not overcome has no right '
    'to grieve.')
b += B.aiquiz('The maiyyah of Allah with His creation in al-Aqidah al-Wasitiyyah: the general '
              'maiyyah whose entailment is knowledge and the particular maiyyah whose entailment '
              'is victory and support, how al-Mujadilah 58:7 interprets itself by opening and '
              'sealing with knowledge, the two conditions in al-Nahl 16:128, and the two grounds '
              'on which maiyyah does not contradict uluww including the Arabs saying that the '
              'moon was with us')
b += B.further()
b += B.nav('was-l16-istiwa-uluww.html', 'The Istiwāʾ and the Highness',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l17')

io.open(os.path.join(B.AQ, 'was-l17-maiyyah.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'المَعِيَّةُ العَامَّةُ وَالخَاصَّة',
    'The Maʿiyyah of Allah: General and Particular',
    'Lesson 17 of al-ʿAqīdah al-Wāsiṭiyyah: the two kinds of '
    'maʿiyyah and what each one entails, how Sūrat al-Mujādilah interprets its own '
    'maʿiyyah by enclosing it in knowledge, the two conditions of the particular '
    'maʿiyyah, and why being WITH the creation never competed with being ABOVE it.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ السَّابِعَ عَشَر', '3',
           'المَعِيَّةُ العَامَّةُ وَالخَاصَّة',
           'The Maʿiyyah of Allah: General and Particular', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l17-maiyyah.html')
