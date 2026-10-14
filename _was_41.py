# -*- coding: utf-8 -*-
"""Wasitiyyah L41 -- Part 4 closes: Allah brings people out of the Fire with no
intercession at all, by His mercy; the Garden has room left over; and the
author's referral of the rest to the Book and the Sunnah. Sharh pp.144-145."""
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
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Name the cause of release from the Fire that is <em>other than</em> intercession.',
    'Say who is brought out by it, and what the ḥadīth says about their deeds.',
    'State the asymmetry al-Fawzān draws between the Garden and the Fire.',
    'Explain what the author does with the remaining details, and why.',
])

b += B.heading('١٠ · إِخْرَاجُ أَقْوَامٍ مِنَ النَّارِ بِغَيْرِ شَفَاعَة',
               'Tenth — Bringing People Out of the Fire with No Intercession')
b += B.matn(
    'وَيُخْرِجُ اللهُ مِنَ النَّارِ أَقْوَامًا بِغَيْرِ شَفَاعَةٍ، بَلْ بِفَضْلِهِ '
    'وَرَحْمَتِهِ. وَيَبْقَى فِي الجَنَّةِ فَضْلٌ عَمَّنْ دَخَلَهَا مِنْ أَهْلِ '
    'الدُّنْيَا، فَيُنْشِئُ اللهُ أَقْوَامًا فَيُدْخِلُهُمُ الجَنَّةَ. وَأَصْنَافُ مَا '
    'تَضَمَّنَتْهُ الدَّارُ الآخِرَةُ مِنَ الحِسَابِ وَالثَّوَابِ وَالعِقَابِ '
    'وَالجَنَّةِ وَالنَّارِ، وَتَفَاصِيلُ ذَلِكَ، مَذْكُورَةٌ فِي الكُتُبِ '
    'المُنْزَلَةِ مِنَ السَّمَاءِ، وَالآثَارِ مِنَ العِلْمِ المَأْثُورِ عَنِ '
    'الأَنْبِيَاءِ؛ وَفِي العِلْمِ المَوْرُوثِ عَنْ مُحَمَّدٍ ﷺ مِنْ ذَلِكَ مَا '
    'يَشْفِي وَيَكْفِي، فَمَنِ ابْتَغَاهُ وَجَدَهُ.')
b += B.sharh(
    p('al-Fawzān marks why this comes after Lesson 40: <em>when the Shaykh رحمه الله had mentioned '
      'that among the kinds of intercession which occur by Allah\'s permission is '
      '<strong>the intercession for bringing some of those who entered the Fire out of it</strong> '
      '— <strong>he mentioned here that the coming out of the Fire has another cause besides the '
      'intercession</strong>, and it is: <strong>the mercy of Allah سبحانه, and His bounty and '
      'His beneficence.</strong></em>') +
    p('<em>So <strong>there comes out of the Fire, of the disobedient monotheists, '
      'whoever has in his heart the least weight of a grain of faith.</strong></em>') +
    p('Note what the previous lesson\'s two conditions have just been placed beside. '
      '<strong>An intercession requires His permission and His pleasure — and this requires '
      'neither, because there is no intercessor in it.</strong> The Fire is not emptied only as '
      'far as the intercessors can reach.'))
b += B.ayah(
    'إِنَّ اللَّهَ لَا يَغْفِرُ أَنْ يُشْرَكَ بِهِ وَيَغْفِرُ مَا دُونَ ذَلِكَ لِمَنْ '
    'يَشَاءُ',
    '"Indeed Allah does not forgive that He be associated with, and He forgives what is less than '
    'that for whom He wills."',
    'Sūrat al-Nisāʾ 4:48 · سُورَةُ النِّسَاء')
b += B.hadith(
    'يَقُولُ اللهُ: شَفَعَتِ المَلَائِكَةُ، وَشَفَعَ النَّبِيُّونَ، وَشَفَعَ '
    'المُؤْمِنُونَ، وَلَمْ يَبْقَ إِلَّا أَرْحَمُ الرَّاحِمِينَ. فَيَقْبِضُ قَبْضَةً '
    'مِنَ النَّارِ فَيُخْرِجُ مِنْهَا قَوْمًا لَمْ يَعْمَلُوا خَيْرًا قَطُّ',
    '"Allah will say: the angels have interceded, and the prophets have interceded, and the '
    'believers have interceded — and there remains none but the Most Merciful of those who show '
    'mercy. Then He will take a handful from the Fire and bring out from it a people who never '
    'did any good at all."',
    'الحَدِيثُ المُتَّفَقُ عَلَيْهِ — al-Bukhārī and Muslim')
b += B.sharh(
    p('Read the sequence, because the whole doctrine of the section is in its order. '
      '<strong>Every intercessor goes first.</strong> The angels, then the prophets, then the '
      'believers — each one permitted, each one pleased-with, each one reaching as far as he is '
      'allowed to reach. <strong>And then they are finished, and the sentence turns.</strong>') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.97rem;text-align:center" dir="rtl" lang="ar">'
    '<strong>وَلَمْ يَبْقَ إِلَّا أَرْحَمُ الرَّاحِمِينَ</strong></p>'
    '<p style="margin:.55rem 0 0;font-size:.92rem;text-align:center"><em>— '
    '<strong>and there remains none but the Most Merciful of those who show mercy.</strong></em></p></div>' +
    p('And the last clause is the one to be careful with, because it is easy to soften and should '
      'not be: <strong>%s — a people who never did any good at all.</strong> Not people whose '
      'good was outweighed; not people whose scales were close. '
      '<strong>The last ones out are the ones with nothing to their name.</strong>'
      % ar('قَوْمًا لَمْ يَعْمَلُوا خَيْرًا قَطُّ')) +
    p('Which is why the author was careful to say <strong>%s</strong> — <em>rather, by His bounty '
      'and His mercy</em>. <strong>There is nothing in these people for an intercession to '
      'appeal to</strong>, and no deed in the record to weigh. '
      'The grain of faith in the heart is the whole of their case, and '
      '<em>He forgives what is less than that for whom He wills.</em>'
      % ar('بَلْ بِفَضْلِهِ وَرَحْمَتِهِ')))

b += B.heading('وَيَبْقَى فِي الجَنَّةِ فَضْل', 'And There Remains Room in the Garden')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>a spaciousness</strong></em> — '
      '<strong>%s</strong>; <em>because <strong>Allah described it with spaciousness</strong></em>:'
      % (ar('وَيَبْقَى فِي الجَنَّةِ فَضْلٌ'), ar('عَمَّنْ دَخَلَهَا مِنْ أَهْلِ الدُّنْيَا'))))
b += B.ayah(
    'وَسَارِعُوا إِلَى مَغْفِرَةٍ مِنْ رَبِّكُمْ وَجَنَّةٍ عَرْضُهَا السَّمَاوَاتُ '
    'وَالْأَرْضُ أُعِدَّتْ لِلْمُتَّقِينَ',
    '"And hasten to a forgiveness from your Lord, and a Garden whose breadth is the heavens and '
    'the earth — prepared for those of taqwā."',
    'Sūrat Āl ʿImrān 3:133 · سُورَةُ آلُ عِمْرَان')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>He creates and brings into being</strong></em> '
      '— <strong>%s</strong>, <em>that is: <strong>groups</strong></em> — '
      '<strong>%s</strong>, <em>by His bounty and His mercy</em>.'
      % (ar('فَيُنْشِئُ اللهُ'), ar('أَقْوَامًا'), ar('فَيُدْخِلُهُمُ الجَنَّةَ'))) +
    p('So the Garden is not filled by the people of this world. '
      '<strong>Room is left, and Allah creates people for it.</strong> Which is a strange and '
      'generous thing to be told: <em>the capacity was never set by how many would earn it.</em>') +
    p('And then al-Fawzān states the asymmetry, which is the finest sentence in the section and '
      'the natural close of Part 4:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.95rem"><em>— <strong>because the Garden is His mercy: He '
    'has mercy by it upon whom He wills.</strong> <strong>As for the Fire — He does not '
    'punish in it except one against whom His proof has been established and who belied His '
    'messengers.</strong></em></p></div>' +
    p('<strong>The two are not symmetrical, and the asymmetry runs one way only.</strong> Entry '
      'into the Garden can be by sheer bounty, to people created for it and to people who never '
      'did a good deed. <strong>Entry into the Fire requires that a case was made and '
      'refused.</strong> Nobody is in it who was not shown the proof.') +
    p('That is the same shape the student met on the Islam 101 track in the asymmetry of the '
      'scale, and in <em>al-Qawāʿid al-Arbaʿ</em> where the ḥujjah must be established before '
      'anyone is condemned. <strong>It is the governing principle of the whole of Part 4, stated '
      'at the end rather than the beginning.</strong>'))

b += B.heading('وَفِيمَا وَرِثْنَا مَا يَشْفِي وَيَكْفِي',
               'And in What We Inherited There Is What Heals and Suffices')
b += B.sharh(
    p('The author closes Part 4 not with another event but with a referral. '
      '<em>When he رحمه الله had mentioned what he mentioned of the states of the Last Day and '
      'what occurs in it, <strong>he referred to the Book and the Sunnah for knowledge of the '
      'details of the remainder, of what he did not mention</strong> — <strong>because that is of '
      'the knowledge of the unseen, which is not known except by way of revelation.</strong></em>') +
    p('And look at the three places he names, in order: <strong>%s</strong> — the Books sent down '
      'from heaven; <strong>%s</strong> — the reports of knowledge transmitted from the prophets; '
      'and <strong>%s</strong> — the knowledge inherited from Muḥammad &#65018;, '
      '<em>of which there is <strong>what heals and what suffices</strong></em>.'
      % (ar('الكُتُبِ المُنْزَلَةِ مِنَ السَّمَاءِ'),
         ar('الآثَارِ مِنَ العِلْمِ المَأْثُورِ عَنِ الأَنْبِيَاءِ'),
         ar('العِلْمِ المَوْرُوثِ عَنْ مُحَمَّدٍ ﷺ'))) +
    p('<strong>%s — a healing and a sufficiency.</strong> Two different claims, and both matter. '
      '<em>Healing</em> answers the unease of the one who wants to know and finds the subject '
      'frightening; <em>sufficiency</em> answers the one who suspects something essential has '
      'been withheld. <strong>Neither is a promise that everything has been told — only that '
      'nothing needed has been left out.</strong>' % ar('مَا يَشْفِي وَيَكْفِي')) +
    p('And then the condition, which is the last word of Part 4 and the same condition the author '
      'attached at the close of Part 1: <strong>%s — so whoever seeks it will find it.</strong> '
      'In Lesson 21 it was <em>whoever ponders the Qurʾān <strong>seeking guidance</strong></em>. '
      'Here it is whoever <em>seeks</em> the inherited knowledge. '
      '<strong>Twice now the author has made the promise conditional not on intelligence or '
      'access, but on wanting it.</strong>' % ar('فَمَنِ ابْتَغَاهُ وَجَدَهُ')))
b += B.prose(
    'With this Part 4 is complete. <strong>The grave and its examination; the Greater Resurrection '
    'and the Scales; the registers and the Reckoning; the Ḥawḍ, the Ṣirāṭ and the Qanṭarah; the '
    'intercessions and their conditions; and the release by mercy alone.</strong> And it ends '
    'where it began — on the author\'s rule from Lesson 36, that belief in the Last Day is belief '
    'in <em>everything the Prophet &#65018; informed of</em>: having set out the chief events, he '
    'hands the student back to the sources for the rest.')

b += B.vocab([
    ('بِغَيْرِ شَفَاعَة', 'bi-ghayri shafāʿah', 'with no intercession',
     'A second cause of release — requiring neither of L40’s two conditions'),
    ('أَدْنَى مِثْقَالِ حَبَّة', 'adnā mithqāli ḥabbah',
     'the least weight of a grain',
     'Of faith in the heart — the whole of their case'),
    ('أَرْحَمُ الرَّاحِمِين', 'arḥam al-rāḥimīn',
     'the Most Merciful of those who show mercy',
     'Who remains when every intercessor is finished'),
    ('فَضْل', 'faḍl', 'room, spaciousness',
     'Left over in the Garden after the people of this world have entered'),
    ('فَيُنْشِئُ اللهُ', 'fa-yunshiʾu Allāh', 'then Allah brings into being',
     'He creates groups and admits them — the capacity was never set by who would earn it'),
    ('قِيَامُ الحُجَّة', 'qiyām al-ḥujjah', 'the establishing of the proof',
     'Required before anyone is punished in the Fire — the asymmetry'),
    ('مَا يَشْفِي وَيَكْفِي', 'mā yashfī wa-yakfī',
     'what heals and what suffices',
     'Not that everything was told — that nothing needed was left out'),
])
b += B.mcq('ws-l41', [
    ('What is the cause of release from the Fire that is other than intercession?',
     ['The weight of the good deeds',
      'The mercy of Allah, His bounty and His beneficence — requiring no intercessor at all',
      'The duʿāʾ of the living', 'The passage of a fixed term'], 1),
    ('Who is brought out by it?',
     ['Those whose good and evil were equal',
      'Of the disobedient monotheists, whoever has in his heart the least weight of a grain of '
      'faith',
      'The people of the Heights', 'Those who died before the message reached them'], 1),
    ('What does the ḥadīth say about the deeds of the last group brought out?',
     ['That their good was outweighed by a little',
      'That they never did any good at all',
      'That their deeds were accepted but insufficient',
      'That they had prayed but not fasted'], 1),
    ('Why does the order of the ḥadīth matter?',
     ['Because it shows the angels are the greatest intercessors',
      'Because every intercessor goes first and is finished — and only then does the mercy that '
      'needs no intercessor act',
      'Because it establishes the sequence of the Reckoning',
      'Because the believers intercede last among creatures'], 1),
    ('What does the author say happens to the room left in the Garden?',
     ['It remains empty as a sign',
      'Allah creates groups and admits them, by His bounty and mercy',
      'It is given to the children of the believers',
      'It is folded away'], 1),
    ('What is the asymmetry al-Fawzān states?',
     ['The Garden is larger than the Fire',
      'The Garden is His mercy, by which He has mercy on whom He wills; but He punishes in the '
      'Fire only one against whom His proof was established and who belied His messengers',
      'The Garden is eternal and the Fire is not',
      'The Garden is entered by deeds and the Fire by decree'], 1),
    ('What does the author do with the remaining details, and why?',
     ['He omits them as unimportant',
      'He refers them to the Book and the Sunnah, because they are of the unseen, known only by '
      'way of revelation',
      'He defers them to a later book',
      'He says the scholars differ over them'], 1),
    ('What do %s each answer?' % ar('مَا يَشْفِي وَيَكْفِي'),
     ['The doubts of the philosophers, and of the common people',
      'Healing answers the unease of one who finds the subject frightening; sufficiency answers '
      'one who suspects something essential was withheld',
      'The questions of the Jews, and of the Christians',
      'The needs of the scholar, and of the worshipper'], 1),
])
b += B.tf('ws-l41-tf', [
    ('يُخْرِجُ اللهُ مِنَ النَّارِ أَقْوَامًا بِغَيْرِ شَفَاعَةٍ.',
     'Allah brings people out of the Fire with no intercession.', True),
    ('الجَنَّةُ تَمْتَلِئُ بِأَهْلِ الدُّنْيَا فَلَا يَبْقَى فِيهَا فَضْلٌ.',
     'The Garden is filled by the people of this world, so no room remains.', False),
    ('لَا يُعَذِّبُ اللهُ فِي النَّارِ إِلَّا مَنْ قَامَتْ عَلَيْهِ حُجَّتُهُ.',
     'Allah punishes in the Fire only one against whom His proof has been established.', True),
    ('تَفَاصِيلُ اليَوْمِ الآخِرِ تُعْرَفُ بِالعَقْلِ.',
     'The details of the Last Day are known by the intellect.', False),
])
b += B.memorize(
    'وَلَمْ يَبْقَ إِلَّا أَرْحَمُ الرَّاحِمِينَ',
    'Keep the whole sequence with it: the angels have interceded, the prophets have interceded, '
    'the believers have interceded — and then this. Every permitted intercessor has reached as far '
    'as he was allowed, and the Fire is still not finished being emptied.')
b += B.aiquiz('Bringing people out of the Fire with no intercession in al-Aqidah al-Wasitiyyah: '
              'the mercy of Allah as a second cause requiring neither of the two conditions, the '
              'hadith order in which every intercessor is finished first and the last ones out '
              'never did any good at all, the room left in the Garden and the groups Allah '
              'creates for it, the asymmetry that the Garden is His mercy while the Fire requires '
              'that the proof was established, and the authors referral of the rest to the Book '
              'and the Sunnah with ma yashfi wa-yakfi')
b += B.further()
b += B.nav('was-l40-shafaat.html', 'The Intercessions and Their Two Conditions',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l41')

io.open(os.path.join(B.AQ, 'was-l41-ikhraj-bi-la-shafaah.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'الإِخْرَاجُ مِنَ النَّارِ بِغَيْرِ شَفَاعَة',
    'Release from the Fire with No Intercession',
    'Lesson 41 of al-ʿAqīdah al-Wāsiṭiyyah, closing Part 4: the '
    'ḥadīth in which every intercessor is finished before the mercy that needs no '
    'intercessor acts, and the last ones out never did any good at all; the room left in the '
    'Garden; and the asymmetry — the Garden is His mercy, while the Fire requires that a '
    'case was made and refused.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الحَادِي وَالأَرْبَعُون', '4',
           'الإِخْرَاجُ مِنَ النَّارِ بِغَيْرِ شَفَاعَة',
           'Release from the Fire with No Intercession', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l41-ikhraj-bi-la-shafaah.html')
