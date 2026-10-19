# -*- coding: utf-8 -*-
"""Wasitiyyah L51 -- Part 7, the first closing fasl: the qualities of Ahl
al-Sunnah wa-l-Jama'ah, why they are named so, and the three usul.
Sharh pp.190-194."""
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


def box(inner, wash='var(--brand-wash)', edge='var(--brand)'):
    return ('<div style="background:%s;border-right:4px solid %s;'
            'border-radius:var(--radius-sm);padding:var(--space-md);'
            'margin:0 0 .8rem">%s</div>' % (wash, edge, inner))


def row(k, v):
    return ('<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);'
            'white-space:nowrap;vertical-align:top"><strong>%s</strong></td>'
            '<td style="padding:.6rem .78rem;border:1px solid var(--line)">%s</td></tr>'
            % (k, v))


def table(rows, fs='.91rem'):
    return ('<div style="overflow-x:auto"><table style="width:100%%;'
            'border-collapse:collapse;font-size:%s;margin:0 0 .75rem">%s</table></div>'
            % (fs, ''.join(rows)))


b = B.objectives([
    'Say what %s means here — and what it deliberately does NOT mean.'
    % ar('آثَارُ الرَّسُولِ ﷺ'),
    'Give the three grounds on which the Companions’ way is followed, and al-Fawzān’s '
    'answer to «the way of the salaf is safer, the way of the khalaf is more learned».',
    'Define %s and %s as a pair.' % (ar('الرَّاشِد'), ar('الغَاوِي')),
    'Define %s linguistically and in the Sharīʿah.' % ar('البِدْعَة'),
    'Explain why Ahl al-Sunnah carry BOTH names — %s and %s.'
    % (ar('أَهْلُ الكِتَابِ وَالسُّنَّة'), ar('أَهْلُ الجَمَاعَة')),
    'Say which ijmāʿ is the one that can be pinned down, and give the two reasons a '
    'later ijmāʿ cannot be.',
    'Say which fourth uṣūl the author left out, and why.',
])

# ------------------------------------------------------------------ framing
b += B.heading('فَصْلٌ · فِي صِفَاتِ أَهْلِ السُّنَّةِ وَالجَمَاعَةِ وَلِمَ سُمُّوا '
               'بِذَلِك',
               'A Section on the Qualities of Ahl al-Sunnah, and Why They Are So Named')
b += B.prose(
    '<em>When the Shaykh had set out the way of Ahl al-Sunnah in the matters of '
    '<strong>creed</strong>, he mentioned in this section and the one after it '
    '<strong>their way in the religion at large — its foundations and its branches — and '
    'the descriptions by which they are distinguished from the people of innovation and '
    'opposition.</strong></em> So the book turns, in its last two sections, from what '
    'this group <em>holds</em> to what this group <em>is like</em>; and L52 will close '
    'with their manners.')
b += B.matn(
    'ثُمَّ مِنْ طَرِيقَةِ أَهْلِ السُّنَّةِ وَالجَمَاعَةِ: اتِّبَاعُ آثَارِ رَسُولِ '
    'اللهِ ﷺ بَاطِنًا وَظَاهِرًا، وَاتِّبَاعُ سَبِيلِ السَّابِقِينَ الأَوَّلِينَ '
    'مِنَ المُهَاجِرِينَ وَالأَنْصَارِ، وَاتِّبَاعُ وَصِيَّةِ رَسُولِ اللهِ ﷺ حَيْثُ '
    'قَالَ: «عَلَيْكُمْ بِسُنَّتِي وَسُنَّةِ الخُلَفَاءِ الرَّاشِدِينَ '
    'المَهْدِيِّينَ مِنْ بَعْدِي، تَمَسَّكُوا بِهَا وَعَضُّوا عَلَيْهَا '
    'بِالنَّوَاجِذِ، وَإِيَّاكُمْ وَمُحْدَثَاتِ الأُمُورِ، فَإِنَّ كُلَّ بِدْعَةٍ '
    'ضَلَالَةٌ». وَيَعْلَمُونَ أَنَّ أَصْدَقَ الكَلَامِ كَلَامُ اللهِ، وَخَيْرَ '
    'الهَدْيِ هَدْيُ مُحَمَّدٍ ﷺ؛ وَيُؤْثِرُونَ كَلَامَ اللهِ عَلَى غَيْرِهِ مِنْ '
    'كَلَامِ أَصْنَافِ النَّاسِ، وَيُقَدِّمُونَ هَدْيَ مُحَمَّدٍ ﷺ عَلَى هَدْيِ كُلِّ '
    'أَحَدٍ. وَلِهَذَا سُمُّوا أَهْلَ الكِتَابِ وَالسُّنَّةِ، وَسُمُّوا أَهْلَ '
    'الجَمَاعَةِ؛ لِأَنَّ الجَمَاعَةَ هِيَ الاجْتِمَاعُ وَضِدُّهَا الفُرْقَةُ. '
    'وَالإِجْمَاعُ هُوَ الأَصْلُ الثَّالِثُ الَّذِي يُعْتَمَدُ عَلَيْهِ فِي العِلْمِ '
    'وَالدِّينِ؛ وَهُمْ يَزِنُونَ بِهَذِهِ الأُصُولِ الثَّلَاثَةِ جَمِيعَ مَا عَلَيْهِ '
    'النَّاسُ مِنْ أَقْوَالٍ وَأَعْمَالٍ بَاطِنَةٍ أَوْ ظَاهِرَةٍ مِمَّا لَهُ '
    'تَعَلُّقٌ بِالدِّينِ. وَالإِجْمَاعُ الَّذِي يَنْضَبِطُ هُوَ مَا كَانَ عَلَيْهِ '
    'السَّلَفُ الصَّالِحُ، فَإِنَّ بَعْدَهُمْ كَثُرَ الاخْتِلَافُ وَانْتَشَرَتِ '
    'الأُمَّةُ.')

# ------------------------------------------------------------------ 1. athar
b += B.heading('١ · اتِّبَاعُ آثَارِ النَّبِيِّ ﷺ بَاطِنًا وَظَاهِرًا',
               'Following His ﷺ Traces, Inwardly and Outwardly')
b += B.sharh(
    p('<em>That is: <strong>treading his road and travelling upon his method</strong> — '
      '<strong>%s</strong>, <strong>in contrast to the hypocrites, who follow him '
      'outwardly and not inwardly.</strong></em>'
      % ar('بَاطِنًا وَظَاهِرًا')) +
    p('Then the definition that does the real work in this clause:') +
    table([
        row('<span dir="rtl" lang="ar">آثَارُهُ ﷺ</span><br>'
            '<span style="font-size:.82rem;font-weight:400">what it IS</span>',
            '<em><strong>his Sunnah</strong> — and it is <strong>what is narrated from '
            'him and transmitted from him of a saying, a deed, or an '
            'approval.</strong></em>'),
        row('<span dir="rtl" lang="ar">لَا آثَارُهُ الحِسِّيَّة</span><br>'
            '<span style="font-size:.82rem;font-weight:400">what it is NOT</span>',
            '<em><strong>not his physical traces</strong>, such as the places where he '
            'sat and slept and the like — <strong>because pursuing that is a cause of '
            'falling into shirk, as happened in the nations before.</strong></em>'),
    ]))
b += box(
    '<p style="margin:0;font-size:.95rem">That second row is one of the sharpest things '
    'in the sharḥ, and it turns on a pun the Arabic makes available and English does '
    'not. <strong>%s</strong> can mean <em>a transmitted report</em> or <em>a physical '
    'relic</em> — and al-Fawzān insists the matn means the first and warns against the '
    'second <strong>in the same breath.</strong></p>'
    '<p style="margin:.6rem 0 0;font-size:.93rem">So <em>following his traces</em> means '
    'doing what he said, did and approved. <strong>It does not mean venerating the '
    'ground he stood on.</strong> And the reason given is not aesthetic distaste: it is '
    'that this exact practice is how the earlier nations arrived at shirk — which the '
    'whole first half of this creed was spent dismantling.</p>'
    % ar('أَثَر'))

# ------------------------------------------------------------------ 2. sabil
b += B.heading('٢ · اتِّبَاعُ سَبِيلِ السَّابِقِينَ الأَوَّلِين',
               'Following the Way of the First Forerunners')
b += B.sharh(
    p('<em>Because of what Allah singled them out with <strong>of knowledge and '
      'fiqh</strong></em> — and al-Fawzān gives three grounds, each of which is a '
      'structural advantage that cannot be reproduced later:') +
    table([
        row('<strong>١</strong>', '<em><strong>they witnessed the sending down</strong> '
            'of the revelation</em>'),
        row('<strong>٢</strong>', '<em><strong>they heard its interpretation</strong></em>'),
        row('<strong>٣</strong>', '<em><strong>and they received from the Messenger ﷺ '
            'without an intermediary</strong></em>'),
    ], fs='.92rem') +
    p('<em>So <strong>they are nearer to what is correct, and more deserving of being '
      'followed after the Messenger ﷺ. Their being followed comes in the second '
      'degree, after the following of the Messenger ﷺ.</strong></em>') +
    p('And then the ruling that follows from it: <em><strong>the sayings of the '
      'Companions are a proof that must be followed when no text from the Prophet ﷺ is '
      'found</strong> — because their way is <strong>%s</strong>.</em>'
      % ar('أَسْلَمُ وَأَعْلَمُ وَأَحْكَم')))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem"><strong>Those three words are chosen '
    'to answer a specific saying</strong>, and al-Fawzān quotes it in order to refuse '
    'it:</p>'
    '<p style="margin:0 0 .55rem;font-size:.94rem"><em>— <strong>not as some of the '
    'later ones say: that the way of the salaf is safer (أَسْلَم), while the way of the '
    'khalaf is more learned and more judicious (أَعْلَمُ وَأَحْكَم) — so they follow '
    'the way of the khalaf and abandon the way of the salaf.</strong></em></p>'
    '<p style="margin:0;font-size:.93rem">Notice the shape of the refusal. '
    '<strong>The saying concedes safety to the salaf and then takes knowledge away from '
    'them</strong> — which is a way of honouring them out of the argument. al-Fawzān '
    'does not meet it with indignation; he meets it by claiming all three words at '
    'once: <strong>أَسْلَمُ وَأَعْلَمُ وَأَحْكَم.</strong> The men who watched the '
    'revelation descend and asked the Messenger ﷺ what it meant were not merely more '
    '<em>cautious</em> than those who came later. They knew more. '
    '<strong>A safety that is bought by ignorance would be no safety at all</strong> — '
    'so if the salaf were safer, it is because they were better informed, not in spite '
    'of being less so.</p>')

# ------------------------------------------------------------------ 3. wasiyyah
b += B.heading('٣ · اتِّبَاعُ وَصِيَّةِ رَسُولِ اللهِ ﷺ',
               'Following the Bequest of the Messenger of Allah ﷺ')
b += B.hadith(
    'عَلَيْكُمْ بِسُنَّتِي وَسُنَّةِ الخُلَفَاءِ الرَّاشِدِينَ المَهْدِيِّينَ مِنْ '
    'بَعْدِي، تَمَسَّكُوا بِهَا وَعَضُّوا عَلَيْهَا بِالنَّوَاجِذِ، وَإِيَّاكُمْ '
    'وَمُحْدَثَاتِ الأُمُورِ، فَإِنَّ كُلَّ بِدْعَةٍ ضَلَالَةٌ',
    '"Hold to my Sunnah and the sunnah of the rightly-guided, guided Caliphs after me. '
    'Cling to it and bite upon it with the molars. And beware of newly-invented matters, '
    'for every innovation is a misguidance."',
    'رَوَاهُ الإِمَامُ أَحْمَدُ وَأَبُو دَاوُدَ وَالتِّرْمِذِيُّ وَابْنُ مَاجَهْ — '
    'وَقَالَ التِّرْمِذِيُّ: حَسَنٌ صَحِيحٌ')
b += B.sharh(
    p('<em>And the Shaykh’s purpose is to make clear that Ahl al-Sunnah follow '
      '<strong>the way of the rightly-guided Caliphs in particular</strong>, after their '
      'following of the first forerunners of the Muhājirūn and the Anṣār '
      '<strong>in general</strong> — because the Prophet ﷺ enjoined following the way of '
      'the rightly-guided Caliphs <strong>with a bequest specific to them</strong> in '
      'this ḥadīth.</em>') +
    p('<em>So in it <strong>he joined the sunnah of the rightly-guided Caliphs to his '
      'own sunnah</strong> — which indicates that <strong>what the rightly-guided '
      'Caliphs, or one of them, instituted, it is not permissible to turn away '
      'from.</strong></em>') +
    p('Then the wording, word by word:') +
    table([
        row(ar('الخُلَفَاءُ الرَّاشِدُون'),
            '<em>the four Caliphs: <strong>أَبُو بَكْرٍ · عُمَرُ · عُثْمَانُ · '
            'عَلِيٌّ</strong>. And they were described as <strong>الرَّاشِدِين because '
            'they knew the truth and followed it.</strong></em>'),
        row(ar('المَهْدِيِّين'),
            '<em>that is: <strong>those whom Allah guided to the truth</strong></em>'),
        row(ar('تَمَسَّكُوا بِهَا'), '<em>that is: <strong>cleave to it</strong></em>'),
        row(ar('وَعَضُّوا عَلَيْهَا بِالنَّوَاجِذ'),
            '<em>a figure for <strong>the intensity of clinging to it</strong>; and '
            '<strong>النَّوَاجِذ are the furthest back of the molars</strong></em>'),
        row(ar('مُحْدَثَاتُ الأُمُور'), '<em>they are <strong>the innovations</strong></em>'),
    ], fs='.9rem'))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem"><strong>الرَّاشِد and its opposite</strong> '
    '— al-Fawzān defines the word by giving its contrary, which is how he teaches a term '
    'whenever the contrast carries the meaning:</p>'
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.93rem">'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong dir="rtl" lang="ar">الرَّاشِد</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<em><strong>one who knew the truth AND acted by it</strong></em></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap">'
    '<strong dir="rtl" lang="ar">الغَاوِي</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">'
    '<em><strong>one who knew the truth and did NOT act by it</strong></em></td></tr>'
    '</table></div>'
    '<p style="margin:.6rem 0 0;font-size:.93rem">So the two differ by one thing only, '
    'and it is not knowledge. <strong>Both men know.</strong> The title of the four '
    'Caliphs is therefore a statement about their obedience and not about their '
    'learning — and the pair quietly warns the student that knowing the truth is the '
    'cheaper half of the matter.</p>')
b += B.sharh(
    p('And then <strong>%s</strong>, defined in the two registers al-Fawzān always '
      'gives:' % ar('البِدْعَة')) +
    table([
        row('<span dir="rtl" lang="ar">لُغَةً</span>',
            '<em><strong>what has no prior precedent</strong></em>'),
        row('<span dir="rtl" lang="ar">شَرْعًا</span>',
            '<em><strong>what no Sharīʿah evidence has indicated</strong></em>'),
    ], fs='.93rem') +
    p('<em>So <strong>everyone who introduces something and ascribes it to the religion '
      'while it has no evidence — it is an innovation and a misguidance</strong>, '
      '<strong>whether in creed, or in sayings, or in deeds.</strong></em>') +
    p('<strong>Mark the two conditions in that sentence, because together they are the '
      'whole definition.</strong> A thing is a bidʿah when it is <em>introduced</em> '
      '<strong>and</strong> <em>ascribed to the religion</em> without evidence. That is '
      'why the Sharīʿah definition is narrower than the linguistic one: a new tool, a '
      'new road, a new way of recording a text — these have no prior precedent and are '
      'not innovations in the religion, because nobody ascribes them to it. '
      '<strong>The ascription is what makes a novelty a bidʿah</strong>, and al-Fawzān '
      'returns to this on the next page.'))

# ------------------------------------------------------------------ 4. taqdim
b += B.heading('٤ · تَقْدِيمُ الكِتَابِ وَالسُّنَّةِ عَلَى كَلَامِ النَّاس',
               'Putting the Book and the Sunnah Before the Speech of Men')
b += B.sharh(
    p('<em>And of the qualities of Ahl al-Sunnah: <strong>that they magnify the Book of '
      'Allah and the Sunnah of His Messenger and hold them in awe, and put them first — '
      'in drawing evidence from them and in taking them as a pattern — over the sayings '
      'of men and their deeds.</strong></em> Because they know two things:'))
b += B.ayah(
    'اللَّهُ لَا إِلَهَ إِلَّا هُوَ لَيَجْمَعَنَّكُمْ إِلَى يَوْمِ الْقِيَامَةِ لَا '
    'رَيْبَ فِيهِ وَمَنْ أَصْدَقُ مِنَ اللَّهِ حَدِيثًا',
    '"Allah — there is no deity but Him. He will surely gather you to the Day of '
    'Standing, about which there is no doubt. And who is more truthful than Allah in '
    'speech?"',
    'Sūrat al-Nisāʾ 4:87 · سُورَةُ النِّسَاء')
b += B.ayah(
    'وَعْدَ اللَّهِ حَقًّا وَمَنْ أَصْدَقُ مِنَ اللَّهِ قِيلًا',
    '"The promise of Allah, in truth. And who is more truthful than Allah in word?"',
    'Sūrat al-Nisāʾ 4:122 · سُورَةُ النِّسَاء')
b += B.prose(
    '<strong>Both are rhetorical questions, which is why al-Fawzān cites the pair.</strong> '
    'The matn says <em>the most truthful speech is the speech of Allah</em>, and the '
    'Qurʾān states that not as a claim to be proved but as a question nobody will answer: '
    '<em>who is more truthful than Allah?</em> Once that question has been asked, '
    'preferring any man’s word over His has already been answered.')
b += B.sharh(
    p('And the second: <em><strong>that the best guidance is the guidance of Muḥammad '
      'ﷺ</strong></em>. al-Fawzān pauses on the vowelling, because the word carries two '
      'readings:') +
    table([
        row('<span dir="rtl" lang="ar">الهَدْي</span><br>'
            '<span style="font-size:.82rem;font-weight:400">fatḥah on the hāʾ, sukūn on '
            'the dāl</span>',
            '<em><strong>السَّمْتُ وَالطَّرِيقَةُ وَالسِّيرَة</strong> — his bearing, '
            'his way, his conduct</em>'),
        row('<span dir="rtl" lang="ar">الهُدَى</span><br>'
            '<span style="font-size:.82rem;font-weight:400">ḍammah on the hāʾ, fatḥah '
            'on the dāl</span>',
            '<em>and it is also read thus — that is: '
            '<strong>الدَّلَالَةُ وَالإِرْشَاد</strong>, the pointing-out and the '
            'directing</em>'),
    ], fs='.91rem') +
    p('<strong>The two readings are not in competition; they name the two things a '
      'student takes from him ﷺ.</strong> On the first, what is best is <em>how he '
      'lived</em>; on the second, what is best is <em>what he taught</em>. And a single '
      'vowel decides which — the kind of observation this track has met before, in '
      'Lesson 4, where a vowel turned Mūsā into the speaker.'))
b += B.sharh(
    p('<em><strong>%s</strong> — that is: <strong>they put it first and take it, and '
      'they leave whatever opposes it of the speech of the creation, whoever they '
      'may be — leaders, or scholars, or devotees.</strong></em>'
      % ar('وَيُؤْثِرُونَ كَلَامَ اللهِ')) +
    p('<strong>That list of three is doing something.</strong> It names the three kinds '
      'of authority a man might actually be tempted to put above the text — '
      '<em>power, learning, and piety</em> — and rules out all three. The last is the '
      'hardest and so it is placed last: a reputation for worship is the credential '
      'that most readily overrides a text in people’s hearts.') +
    p('<em>And <strong>%s</strong> — that is: his Sunnah, his conduct, his teaching and '
      'his directing — <strong>over the guidance of anyone else</strong> of the '
      'creation, <strong>however great his standing, if his guidance opposes the '
      'guidance of the Messenger of Allah ﷺ</strong>. And that is in acting upon His '
      'saying:</em>' % ar('وَيُقَدِّمُونَ هَدْيَ مُحَمَّدٍ ﷺ')))
b += B.ayah(
    'يَا أَيُّهَا الَّذِينَ آمَنُوا أَطِيعُوا اللَّهَ وَأَطِيعُوا الرَّسُولَ وَأُولِي '
    'الْأَمْرِ مِنْكُمْ فَإِنْ تَنَازَعْتُمْ فِي شَيْءٍ فَرُدُّوهُ إِلَى اللَّهِ '
    'وَالرَّسُولِ إِنْ كُنْتُمْ تُؤْمِنُونَ بِاللَّهِ وَالْيَوْمِ الْآخِرِ',
    '"O you who believe, obey Allah and obey the Messenger and those in authority among '
    'you. Then if you differ in anything, refer it to Allah and the Messenger, if you '
    'believe in Allah and the Last Day."',
    'Sūrat al-Nisāʾ 4:59 · سُورَةُ النِّسَاء')
b += B.prose(
    'And see what the āyah does with the three obediences. <strong>It repeats the verb '
    'for Allah and for the Messenger, and it does not repeat it for those in '
    'authority</strong> — they are joined to the Messenger’s obedience rather than given '
    'one of their own. Then, when there is a dispute, <strong>the referral is to Allah '
    'and the Messenger only.</strong> The āyah establishes the obedience of rulers and '
    'subordinates it in the same breath — which is exactly the clause the matn is '
    'resting on.')

# ------------------------------------------------------------------ the two names
b += B.heading('لِمَاذَا حَمَلُوا الاسْمَيْن', 'Why They Carry Both Names')
b += B.sharh(
    table([
        row(ar('أَهْلُ الكِتَابِ وَالسُّنَّة'),
            '<em>for the sake of <strong>their clinging to the Book of Allah and '
            'preferring His speech to the speech of everyone, and their clinging to the '
            'guidance of the Messenger of Allah and putting it before the guidance of '
            'everyone</strong> — they were given this noble title, '
            '<strong>which conveys that these two belong to them in particular</strong>, '
            'as against those who deviated from the Book and the Sunnah among the sects '
            'of misguidance, such as the Muʿtazilah, the Khawārij and the '
            'Rawāfiḍ.</em>'),
        row(ar('أَهْلُ الجَمَاعَة'),
            '<em><strong>and al-jamāʿah is the opposite of al-furqah</strong> — because '
            '<strong>clinging to the Book and the Sunnah yields gathering and '
            'harmony</strong></em>'),
    ]))
b += B.ayah(
    'وَاعْتَصِمُوا بِحَبْلِ اللَّهِ جَمِيعًا وَلَا تَفَرَّقُوا',
    '"And hold fast, all of you together, to the rope of Allah, and do not become '
    'divided."',
    'Sūrat Āl ʿImrān 3:103 · سُورَةُ آلِ عِمْرَان')
b += box(
    '<p style="margin:0;font-size:.95rem"><em>So <strong>al-jamāʿah here is: those '
    'gathered upon the truth.</strong></em></p>'
    '<p style="margin:.6rem 0 0;font-size:.93rem"><strong>That is the definition the '
    'whole name depends on, and it rules out the obvious misreading.</strong> The '
    'jamāʿah is not «the majority», and it is not «whoever happens to be assembled». '
    'The āyah commands holding to <em>the rope of Allah</em> and forbids division in the '
    'same sentence — so <strong>the gathering is a consequence of holding to the '
    'revelation, not an alternative to it.</strong> Which is why Ibn Masʿūd '
    'رضي الله عنه could say, as Lesson 2 recorded, that the jamāʿah is whatever agrees '
    'with the truth <em>even if you are alone.</em></p>')

# ------------------------------------------------------------------ the three usul
b += B.heading('الأُصُولُ الثَّلَاثَةُ وَالمِيزَان',
               'The Three Foundations, and the Scale')
b += B.sharh(
    p('<em>And of the qualities of Ahl al-Sunnah: <strong>gathering upon taking the Book '
      'and the Sunnah, agreement upon the truth, and cooperation upon righteousness and '
      'taqwā — and this has borne fruit in the existence of ijmāʿ.</strong></em>') +
    p('<em><strong>And the ijmāʿ is the third foundation relied upon in knowledge and in '
      'religion.</strong> The scholars of uṣūl have defined ijmāʿ as: '
      '<strong>the agreement of the scholars of an age upon a matter of religion; and it '
      'is a decisive proof that must be acted upon.</strong> And his words %s — that is: '
      '<strong>after the first two foundations, which are the Book and the '
      'Sunnah.</strong></em>' % ar('وَهُوَ الأَصْلُ الثَّالِث')) +
    p('<em>And of their qualities, that they <strong>%s</strong> — the Book, the Sunnah '
      'and the ijmāʿ — <strong>all that people are upon of sayings and deeds, inward or '
      'outward, of what has a connection to the religion</strong>. So '
      '<strong>they make these three foundations a scale for distinguishing truth from '
      'falsehood, and guidance from misguidance</strong>, in what issues from people of '
      'verbal or practical dealings, whether of belief or of action.</em>'
      % ar('يَزِنُونَ بِهَذِهِ الأُصُولِ الثَّلَاثَة')))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem"><strong>Then the clause that limits '
    'the scale — and it completes the definition of bidʿah above.</strong> al-Fawzān '
    'stresses the matn’s own restriction, <em>%s</em>:</p>'
    '<p style="margin:0;font-size:.94rem"><em>— of the deeds of people, '
    '<strong>such as the prayer, the fast, the Ḥajj and the zakāh</strong>… '
    '<strong>as for worldly matters, the default ruling in them is '
    'permissibility.</strong></em></p>'
    '<p style="margin:.6rem 0 0;font-size:.93rem">So the three foundations are '
    'the scale <strong>for what is offered as religion</strong>, and they are not a '
    'licence to demand a text for every ordinary act. '
    '<strong>Worship is restricted to what is legislated; the world is open except '
    'where a prohibition came.</strong> A student who misses this turns the creed into a '
    'burden it was never meant to be — and it is the same distinction that keeps the '
    'linguistic sense of bidʿah from swallowing the Sharīʿah sense.</p>'
    % ar('مِمَّا لَهُ تَعَلُّقٌ بِالدِّين'))

b += B.heading('الإِجْمَاعُ الَّذِي يَنْضَبِط', 'The Ijmāʿ That Can Be Pinned Down')
b += B.sharh(
    p('<em>Then the Shaykh رحمه الله clarified the reality of the ijmāʿ that is made a '
      'foundation in drawing evidence, and said: <strong>%s</strong> — that is: '
      '<strong>whose occurrence can be affirmed with certainty</strong> — '
      '<strong>it is what the righteous salaf were upon</strong>, '
      '<em>since they were few, gathered in the Ḥijāz, so that recording them and '
      'knowing their view on a question was possible.</em></em>'
      % ar('وَالإِجْمَاعُ الَّذِي يَنْضَبِط')) +
    p('<em>And <strong>%s</strong> — that is: after the salaf:</em>'
      % ar('وَبَعْدَهُمْ كَثُرَ الاخْتِلَافُ وَانْتَشَرَتِ الأُمَّة')) +
    table([
        row('<span dir="rtl" lang="ar">أَوَّلًا</span>',
            '<em><strong>the abundance of disagreement</strong>, such that encompassing '
            'their sayings is not possible</em>'),
        row('<span dir="rtl" lang="ar">ثَانِيًا</span>',
            '<em><strong>the spreading of the Ummah into the regions of the earth after '
            'the conquests</strong>, such that it is not customarily possible for the '
            'case to reach every one of them and for him to come to know of it — and '
            'then <strong>it is not possible to affirm with certainty that they '
            'concurred upon a single saying in it.</strong></em>'),
    ], fs='.92rem') +
    p('<strong>So this is a statement about what can be known, not about what is '
      'binding.</strong> Ijmāʿ remains a decisive proof; the point is that a claim of '
      'ijmāʿ is only as good as the possibility of having checked — and that possibility '
      'shrank as the Ummah grew. Which is why <em>«the scholars have agreed»</em> is a '
      'claim to be examined rather than a formula to be accepted.'))
b += box(
    '<p style="margin:0 0 .45rem;font-size:.95rem"><strong dir="rtl" lang="ar">'
    'تَنْبِيهٌ</strong> — why only three?</p>'
    '<p style="margin:0;font-size:.94rem"><em>The Shaykh رحمه الله restricted himself '
    'to mentioning the three foundations and did not mention the fourth foundation, '
    'which is <strong>القِيَاس</strong> — <strong>because al-qiyās is disputed</strong>, '
    'just as they disputed over other foundations whose reference is the books of '
    'uṣūl.</em></p>'
    '<p style="margin:.6rem 0 0;font-size:.92rem">Which is a characteristic move of this '
    'creed, and worth naming as a method. <strong>A book of ʿaqīdah states what the '
    'Ummah is bound by, so it carries only what is agreed</strong> — the disputed is '
    'left to the discipline that handles dispute. That is why the Wāsiṭiyyah is short '
    'and why nothing in it has needed to be withdrawn.</p>',
    wash='#fff8e6', edge='#d4a017')

b += B.vocab([
    ('آثَارُ الرَّسُولِ ﷺ', 'āthār al-rasūl', 'his traces',
     'His Sunnah — what is narrated of a saying, a deed or an approval; NOT his physical '
     'traces, since pursuing those caused shirk in earlier nations'),
    ('الرَّاشِد', 'al-rāshid', 'the rightly-guided one',
     'One who knew the truth AND acted by it'),
    ('الغَاوِي', 'al-ghāwī', 'the errant one',
     'One who knew the truth and did NOT act by it — the opposite of الرَّاشِد, and the '
     'two differ by obedience, not knowledge'),
    ('النَّوَاجِذ', 'al-nawājidh', 'the back molars',
     'The furthest back of the teeth — «bite upon it with the nawājidh» is a figure for '
     'the intensity of clinging'),
    ('البِدْعَة', 'al-bidʿah', 'an innovation',
     'لُغَةً what has no prior precedent · شَرْعًا what no Sharīʿah evidence indicated — '
     'introduced AND ascribed to the religion'),
    ('الهَدْي', 'al-hady', 'bearing, conduct',
     'السَّمْتُ وَالطَّرِيقَةُ وَالسِّيرَة; and read الهُدَى it is '
     'الدَّلَالَةُ وَالإِرْشَاد, the pointing-out and directing'),
    ('الجَمَاعَة', 'al-jamāʿah', 'the gathering',
     'The opposite of الفُرْقَة — and here specifically '
     'المُجْتَمِعُونَ عَلَى الحَقّ, those gathered upon the truth'),
    ('الإِجْمَاع', 'al-ijmāʿ', 'scholarly consensus',
     'اتِّفَاقُ عُلَمَاءِ العَصْرِ عَلَى أَمْرٍ دِينِيّ — a decisive proof that must be '
     'acted upon; the third foundation'),
    ('يَنْضَبِط', 'yanḍabiṭ', 'can be pinned down',
     'That whose occurrence can be affirmed with certainty — true of the salaf in the '
     'Ḥijāz, not of a scattered Ummah'),
    ('القِيَاس', 'al-qiyās', 'analogical reasoning',
     'The fourth foundation, left out of the matn because it is disputed — a creed '
     'carries only what is agreed'),
])
b += B.mcq('ws-l51', [
    ('What does آثَارُ الرَّسُولِ ﷺ mean here — and what does it NOT mean?',
     ['His physical relics, which are to be honoured',
      'His Sunnah — what is narrated of a saying, deed or approval; NOT his physical '
      'traces like where he sat or slept, since pursuing those caused shirk in earlier '
      'nations',
      'Only his sayings, excluding his deeds',
      'His lineage and household'], 1),
    ('What does «inwardly and outwardly» exclude?',
     ['Following him in matters of worldly custom',
      'The way of the hypocrites, who follow him outwardly and not inwardly',
      'Following the Companions',
      'Acting on a single-chain narration'], 1),
    ('What three grounds does al-Fawzān give for following the forerunners?',
     ['Their numbers, their lineage and their wealth',
      'They witnessed the sending down, they heard its interpretation, and they received '
      'from the Messenger ﷺ without an intermediary',
      'Their consensus, their piety and their jihād',
      'Their proximity to Makkah and Madīnah'], 1),
    ('How does al-Fawzān answer «the way of the salaf is safer, the way of the khalaf is '
     'more learned»?',
     ['By conceding it and adding that safety is more important',
      'By claiming all three words for the salaf — أَسْلَمُ وَأَعْلَمُ وَأَحْكَم; a '
      'safety bought by ignorance would be no safety',
      'By denying that the khalaf had any knowledge at all',
      'By referring the question to the books of uṣūl'], 1),
    ('What is the difference between الرَّاشِد and الغَاوِي?',
     ['One has knowledge, the other does not',
      'Both know the truth — the rāshid acts by it and the ghāwī does not; so they '
      'differ by obedience, not knowledge',
      'One is a Companion, the other a later Muslim',
      'One is a caliph, the other a subject'], 1),
    ('What are the two definitions of البِدْعَة?',
     ['A sin, and a major sin',
      'لُغَةً what has no prior precedent; شَرْعًا what no Sharīʿah evidence indicated — '
      'introduced AND ascribed to the religion',
      'An error in creed, and an error in action',
      'What the Companions rejected, and what later scholars rejected'], 1),
    ('Which āyah does al-Fawzān pair with «who is more truthful than Allah in speech»?',
     ['Āl ʿImrān 3:110', 'al-Nisāʾ 4:122 — «who is more truthful than Allah in word»',
      'al-Tawbah 9:100', 'Yūnus 10:62'], 1),
    ('What do the two readings الهَدْي and الهُدَى give?',
     ['A weak reading and a strong one',
      'الهَدْي = his bearing, way and conduct — HOW he lived; الهُدَى = the pointing-out '
      'and directing — WHAT he taught',
      'A Madinan reading and a Makkan one',
      'The same meaning in two dialects'], 1),
    ('Whose speech does the matn say is left when it opposes the revelation?',
     ['Only that of the innovators',
      'Anyone’s — leaders, or scholars, or devotees; a reputation for worship is no '
      'exception',
      'Only that of the non-Arabs', 'Only that of the later generations'], 1),
    ('What does al-Nisāʾ 4:59 do with the three obediences?',
     ['It makes all three equal and independent',
      'It repeats the verb for Allah and the Messenger but not for those in authority, '
      'and refers disputes to Allah and the Messenger only — establishing the rulers’ '
      'obedience and subordinating it at once',
      'It abrogates obedience to rulers',
      'It restricts obedience to the Caliphs'], 1),
    ('What exactly is الجَمَاعَة, per al-Fawzān here?',
     ['The majority of the Muslims in any age',
      'المُجْتَمِعُونَ عَلَى الحَقّ — those gathered upon the truth; so the gathering is '
      'a consequence of holding to revelation, not an alternative to it',
      'Those assembled behind one imām',
      'The scholars of an age'], 1),
    ('What is the limit on the three foundations as a scale?',
     ['They apply only to creed, not to action',
      'They weigh what has a connection to the RELIGION — worship is restricted to what '
      'is legislated, while in worldly matters the default is permissibility',
      'They apply only to the salaf',
      'They apply only where there is no dispute'], 1),
    ('Which ijmāʿ can be pinned down, and why?',
     ['Any ijmāʿ reported by a trustworthy scholar',
      'That of the righteous salaf — they were few and gathered in the Ḥijāz, so '
      'recording them and knowing their view was possible',
      'The ijmāʿ of the four schools',
      'The ijmāʿ of the scholars of the Ḥaramayn'], 1),
    ('Why does the author mention only three foundations?',
     ['Because the fourth was not yet known',
      'Because the fourth — القِيَاس — is disputed, and a book of creed carries only '
      'what is agreed',
      'Because qiyās is a branch of the Sunnah',
      'Because the Companions rejected qiyās'], 1),
])
b += B.tf('ws-l51-tf', [
    ('اتِّبَاعُ آثَارِهِ ﷺ يَعْنِي تَتَبُّعَ مَوَاضِعِ جُلُوسِهِ وَنَوْمِهِ.',
     'Following his ﷺ traces means pursuing the places where he sat and slept.', False),
    ('أَقْوَالُ الصَّحَابَةِ حُجَّةٌ يَجِبُ اتِّبَاعُهَا إِذَا لَمْ يُوجَدْ نَصٌّ '
     'عَنِ النَّبِيِّ ﷺ.',
     'The sayings of the Companions are a proof that must be followed when no text from '
     'the Prophet ﷺ is found.', True),
    ('كُلُّ مَا لَا مِثَالَ لَهُ سَابِقٌ فَهُوَ بِدْعَةٌ فِي الدِّينِ.',
     'Everything that has no prior precedent is an innovation in the religion.', False),
    ('الجَمَاعَةُ هُمُ المُجْتَمِعُونَ عَلَى الحَقِّ.',
     'The jamāʿah are those gathered upon the truth.', True),
    ('تَرَكَ الشَّيْخُ ذِكْرَ القِيَاسِ لِأَنَّهُ مُخْتَلَفٌ فِيهِ.',
     'The Shaykh left out mentioning qiyās because it is disputed.', True),
])
b += B.memorize(
    'أَسْلَمُ وَأَعْلَمُ وَأَحْكَم',
    'Three words, and they are an answer rather than a slogan. The saying they refute '
    'grants the salaf <em>safety</em> and takes <em>knowledge</em> away from them — which '
    'is how a man honours his predecessors out of the argument. <strong>Ahl al-Sunnah '
    'claim all three: the men who watched the revelation descend and asked the Messenger '
    'ﷺ what it meant were not merely more cautious than those who came after. They knew '
    'more.</strong>')
b += B.aiquiz('The first closing fasl of al-Aqidah al-Wasitiyyah on the qualities of Ahl '
              'al-Sunnah: athar al-rasul as his Sunnah and not his physical relics and '
              'why pursuing those caused shirk, inwardly and outwardly against the '
              'hypocrites, the three grounds for following the forerunners and the answer '
              'aslam wa-alam wa-ahkam to the claim that the way of the khalaf is more '
              'learned, the hadith of the rightly-guided Caliphs with al-Tirmidhis '
              'grading, al-rashid against al-ghawi, the nawajidh, the two definitions of '
              'bidah and the role of ascription to the religion, the two readings al-hady '
              'and al-huda, the three authorities ruled out as leaders scholars and '
              'devotees, what al-Nisa 4:59 does with the three obediences, the jamaah as '
              'those gathered upon the truth, the three usul as a scale restricted to what '
              'has a connection to the religion with permissibility the default in worldly '
              'matters, which ijma can be pinned down and the two reasons a later one '
              'cannot, and why qiyas is left out')
b += B.further()
b += B.nav('was-l50-karamat-al-awliya.html', 'The Karāmāt of the Awliyāʾ',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l51')

io.open(os.path.join(B.AQ, 'was-l51-sifat-ahl-al-sunnah.html'), 'w',
        encoding='utf-8', newline='\n').write(B.shell(
    'صِفَاتُ أَهْلِ السُّنَّةِ وَلِمَ سُمُّوا بِذَلِك',
    'The Qualities of Ahl al-Sunnah, and Why They Are So Named',
    'Lesson 51 of al-ʿAqīdah al-Wāsiṭiyyah: following his ﷺ traces — his Sunnah and not '
    'his relics; the three grounds for following the forerunners and the answer to «the '
    'way of the khalaf is more learned»; al-rāshid against al-ghāwī; the two definitions '
    'of bidʿah; why they carry both names; the three foundations as a scale, and which '
    'ijmāʿ can be pinned down.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الحَادِي وَالخَمْسُون', '6',
           'صِفَاتُ أَهْلِ السُّنَّةِ وَلِمَ سُمُّوا بِذَلِك',
           'The Qualities of Ahl al-Sunnah, and Why They Are So Named', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l51-sifat-ahl-al-sunnah.html')
