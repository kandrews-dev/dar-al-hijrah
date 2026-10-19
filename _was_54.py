# -*- coding: utf-8 -*-
"""Wasitiyyah L54 -- the close of the matn: their way IS the religion of Islam,
the 73 sects, al-firqah al-najiyah, al-ta'ifah al-mansurah, and the author's
closing du'a'. Sharh pp.201-202."""
import io, os, importlib.util

spec = importlib.util.spec_from_file_location('qb', os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '_mutunbuild.py'))
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
B.set_source(os.path.join(B.AQ, 'was-l01-basmalah.html'))
B.FOOT = ('al-ʿAqīdah al-Wāsiṭiyyah of Shaykh al-Islām Ibn Taymiyyah '
          '· sharḥ of Shaykh Ṣāliḥ al-Fawzān · in our own words')
B.READING = [
    'Shaykh <strong>صَالِحٌ الفَوْزَان</strong>, <em>شَرْحُ العَقِيدَةِ الوَاسِطِيَّة</em> '
    '(Riyadh, Presidency of Scholarly Research &amp; Iftāʾ) — the sharḥ this track '
    'follows, and which closes here.',
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
    'State the %s — the greatest distinction — that the author closes the book with.'
    % ar('المَزِيَّةُ العُظْمَى'),
    'Explain the logic by which the saved sect is identified, and why the identification '
    'does not depend on counting the sects.',
    'Give the clause of the ḥadīth that settles WHICH group is meant.',
    'Say what %s means and the two explanations al-Fawzān reports for the name.'
    % ar('الأَبْدَال'),
    'Give the four things the Prophet ﷺ said about %s.'
    % ar('الطَّائِفَةُ المَنْصُورَة'),
    'Say what the author asks for in his closing duʿāʾ, and why he asks for that and '
    'not for more.',
])

# ------------------------------------------------------------------ matn
b += B.heading('خَاتِمَةُ الرِّسَالَة', 'The Conclusion of the Treatise')
b += B.matn(
    'وَطَرِيقَتُهُمْ هِيَ دِينُ الإِسْلَامِ الَّذِي بَعَثَ اللهُ بِهِ مُحَمَّدًا ﷺ. '
    'لَكِنْ لَمَّا أَخْبَرَ النَّبِيُّ ﷺ أَنَّ أُمَّتَهُ سَتَفْتَرِقُ عَلَى ثَلَاثٍ '
    'وَسَبْعِينَ فِرْقَةً، كُلُّهَا فِي النَّارِ إِلَّا وَاحِدَةً وَهِيَ '
    'الجَمَاعَةُ — وَفِي حَدِيثٍ عَنْهُ أَنَّهُ قَالَ: «هُمْ مَنْ كَانَ عَلَى مِثْلِ '
    'مَا أَنَا عَلَيْهِ اليَوْمَ وَأَصْحَابِي» — صَارَ المُتَمَسِّكُونَ '
    'بِالإِسْلَامِ المَحْضِ الخَالِصِ عَنِ الشَّوْبِ هُمْ أَهْلَ السُّنَّةِ '
    'وَالجَمَاعَةِ. وَفِيهِمُ الصِّدِّيقُونَ وَالشُّهَدَاءُ وَالصَّالِحُونَ؛ '
    'وَمِنْهُمْ أَعْلَامُ الهُدَى وَمَصَابِيحُ الدُّجَى، أُولُو المَنَاقِبِ '
    'المَأْثُورَةِ وَالفَضَائِلِ المَذْكُورَةِ. وَفِيهِمُ الأَبْدَالُ، وَفِيهِمْ '
    'أَئِمَّةُ الدِّينِ الَّذِينَ أَجْمَعَ المُسْلِمُونَ عَلَى هِدَايَتِهِمْ؛ '
    'وَهُمُ الطَّائِفَةُ المَنْصُورَةُ الَّذِينَ قَالَ فِيهِمُ النَّبِيُّ ﷺ: «لَا '
    'تَزَالُ طَائِفَةٌ مِنْ أُمَّتِي عَلَى الحَقِّ مَنْصُورَةً، لَا يَضُرُّهُمْ مَنْ '
    'خَالَفَهُمْ وَلَا مَنْ خَذَلَهُمْ، حَتَّى تَقُومَ السَّاعَةُ». '
    'فَنَسْأَلُ اللهَ أَنْ يَجْعَلَنَا مِنْهُمْ، وَأَنْ لَا يُزِيغَ قُلُوبَنَا '
    'بَعْدَ إِذْ هَدَانَا.')

# ------------------------------------------------------------------ al-maziyyah
b += B.heading('المَزِيَّةُ العُظْمَى · طَرِيقَتُهُمْ هِيَ دِينُ الإِسْلَام',
               'The Greatest Distinction — Their Way IS the Religion of Islam')
b += B.sharh(
    p('<em>The Shaykh رحمه الله continues the clarification of the distinctions of Ahl '
      'al-Sunnah wa-l-Jamāʿah, and he made clear <strong>their greatest '
      'distinction</strong>, which is: that <strong>%s</strong> — that is: '
      '<strong>it is their madhhab and their road to Allah</strong>.</em>'
      % ar('طَرِيقَتَهُمْ دِينُ الإِسْلَام')) +
    p('<strong>Read what that sentence refuses to be.</strong> It does not say that '
      'their way is <em>the best</em> of the ways, or <em>the safest</em>, or <em>the '
      'nearest</em> to Islam. <strong>It says their way is Islam</strong> — the religion '
      'Allah sent Muḥammad ﷺ with, and not a school within it.') +
    p('<em>And that <strong>at the splitting which the Prophet ﷺ informed would occur in '
      'this Ummah, they held firm upon Islam</strong></em> — upon <strong>%s</strong>, '
      '<em>that is: <strong>the pure Islam, unmixed with admixtures</strong>; and for '
      'that reason <strong>they won the title Ahl al-Sunnah wa-l-Jamāʿah</strong>.</em>'
      % ar('مَا كَانَ عَلَيْهِ النَّبِيُّ ﷺ وَأَصْحَابُهُ')))
b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem"><strong>Follow the logic of the '
    '«لَكِنْ», because the whole passage is one argument and the particle is its '
    'hinge:</strong></p>'
    '<p style="margin:0;font-size:.94rem">'
    '<strong>١</strong> &nbsp;Their way is simply the religion of Islam — so in '
    'principle it needs no party name at all.<br>'
    '<strong>٢</strong> &nbsp;<em>But</em> the Prophet ﷺ informed that the Ummah '
    '<em>would</em> split, and that of the sects only one is saved.<br>'
    '<strong>٣</strong> &nbsp;Once a splitting has happened, <strong>the ones still '
    'holding the unmixed thing need a name to be told apart by</strong>.<br>'
    '<strong>٤</strong> &nbsp;<em>So</em> those holding the pure Islam '
    '<strong>came to be</strong> — صَارَ — Ahl al-Sunnah wa-l-Jamāʿah.</p>'
    '<p style="margin:.65rem 0 0;font-size:.93rem"><strong>The verb صَارَ is the point.</strong> '
    'The name is something they <em>became</em>, imposed by the splitting rather than '
    'chosen as a banner. Which is exactly the observation Lesson 2 made from the other '
    'direction: <em>the sects are named after their innovation, their leader or their '
    'deeds, and this group alone is named after the thing everybody claims.</em></p>')

b += B.heading('الفِرْقَةُ النَّاجِيَةُ وَمَا يُعَيِّنُهَا',
               'The Saved Sect, and What Identifies It')
b += B.sharh(
    p('The matn alludes to the ḥadīth of the splitting of the Ummah, '
      '<em>كُلُّهَا فِي النَّارِ إِلَّا وَاحِدَةً</em>, and then — '
      '<strong>and this is the clause that does the work</strong> — '
      'it brings the wording that identifies which one:'))
b += B.hadith(
    'هُمْ مَنْ كَانَ عَلَى مِثْلِ مَا أَنَا عَلَيْهِ اليَوْمَ وَأَصْحَابِي',
    '"They are whoever is upon the like of what I am upon today, and my Companions."',
    'يَذْكُرُهُ المُصَنِّفُ بِقَوْلِهِ: وَفِي حَدِيثٍ عَنْهُ — '
    'وَالمُصَنِّفُ لَمْ يَسُقْ لَهُ تَخْرِيجًا هُنَا')
b += box(
    '<p style="margin:0 0 .5rem;font-size:.95rem"><strong dir="rtl" lang="ar">'
    'تَنْبِيهٌ</strong> — on the attribution of this clause.</p>'
    '<p style="margin:0;font-size:.93rem">The author introduces it with '
    '<em>«وَفِي حَدِيثٍ عَنْهُ» — and in a ḥadīth from him</em>, and '
    '<strong>al-Fawzān passes over it without stating a grading</strong>. '
    'Per the rule this track adopted in Lesson 22, <strong>this page reports the '
    'wording as the author gives it and supplies no grading of its own.</strong> '
    'Nothing in the section rests on it alone: <strong>the identification it '
    'states is established independently</strong> by the whole of Part 6 — the '
    'obligation toward the Companions — and by the ḥadīth of the victorious group '
    'below, which is in <strong>al-Bukhārī and Muslim</strong>.</p>',
    wash='#fff8e6', edge='#d4a017')
b += B.prose(
    'And notice how the identification works, because it is the most practical sentence '
    'in the closing passage. <strong>It is not «they are the group with the correct '
    'opinions», which every sect would claim.</strong> It is a historical test: '
    '<em>whoever is upon the like of what I am upon <strong>today</strong>, and my '
    'Companions.</em> The standard is a state of affairs that actually existed at a '
    'datable moment, in front of named men — <strong>so the question «which group?» '
    'becomes a question about evidence rather than about self-description.</strong> '
    'Which is why the two preceding Parts had to establish the standing of the '
    'Companions before this clause could mean anything.')
b += B.prose(
    'And it is worth seeing what the identification does <em>not</em> require. '
    '<strong>It does not require that the seventy-three be enumerated.</strong> A great '
    'deal of effort has been spent over the centuries trying to list them, and the matn '
    'spends none: once the saved group is fixed by what it is <em>upon</em>, the count of '
    'the others is of no practical use to a man deciding where to stand.')

# ------------------------------------------------------------------ who is in them
b += B.heading('وَفِيهِمْ · مَنْ تَضُمُّهُ هَذِهِ الطَّائِفَة',
               'And Among Them — Whom This Group Contains')
b += B.sharh(
    p('<em>And there came to be among them:</em>') +
    table([
        row(ar('الصِّدِّيقُون'),
            '<em><strong>those who go to the utmost in truthfulness and in '
            'affirming</strong></em>'),
        row(ar('الشُّهَدَاء'),
            '<em><strong>those slain in the path of Allah</strong></em>'),
        row(ar('الصَّالِحُون'),
            '<em><strong>the people of righteous deeds</strong></em>'),
        row(ar('أَعْلَامُ الهُدَى'),
            '<em>that is: <strong>among Ahl al-Sunnah are the eminent scholars, '
            'characterized by every praiseworthy description in knowledge and in '
            'deed</strong></em>'),
        row(ar('الأَبْدَال'),
            '<em>and they are <strong>the awliyāʾ and the devoted worshippers</strong>. '
            'They were named so — <strong>it is said: because whenever one of them dies, '
            'he is replaced (أُبْدِلَ) by another</strong>; <strong>and in a narration '
            'from Aḥmad, that they are أَصْحَابُ الحَدِيث, the people of '
            'ḥadīth</strong></em>'),
        row(ar('أَئِمَّةُ الدِّين'),
            '<em>that is: <strong>among Ahl al-Sunnah are the scholars who are taken as '
            'a pattern — such as the four imāms and others</strong></em>'),
    ], fs='.9rem'))
b += B.prose(
    '<strong>Three of those names repay a second look.</strong> '
    'الصِّدِّيقُون was defined in Lesson 48, of Abū Bakr and of ʿĀʾishah '
    'رضي الله عنهما — so the word arrives here already weighted. '
    'And <strong>the two explanations of الأَبْدَال are not rivals so much as two '
    'different claims about who carries a religion.</strong> On the first, the awliyāʾ '
    'are <em>replaced</em> — the religion is never left without men upholding it, which '
    'is the same promise the next ḥadīth makes. On the second, reported from '
    '<strong>Imām Aḥmad</strong>, they are <em>the people of ḥadīth</em>: the men who '
    'carry the transmission itself. <strong>Both readings say that the thing which '
    'persists is not an institution but a line of men</strong> — and that is as true of '
    'this matn as of anything, since it reaches us only because such men copied it.')
b += B.sharh(
    p('<em>And <strong>%s</strong> — that is: <strong>Ahl al-Sunnah are the group '
      'mentioned in the ḥadīth</strong>:</em>' % ar('وَهُمُ الطَّائِفَةُ المَنْصُورَة')))
b += B.hadith(
    'لَا تَزَالُ طَائِفَةٌ مِنْ أُمَّتِي عَلَى الحَقِّ مَنْصُورَةً، لَا يَضُرُّهُمْ '
    'مَنْ خَالَفَهُمْ وَلَا مَنْ خَذَلَهُمْ، حَتَّى تَقُومَ السَّاعَةُ',
    '"A group of my Ummah will not cease to be upon the truth, given victory. Neither '
    'the one who opposes them nor the one who forsakes them will harm them, until the '
    'Hour comes."',
    'رَوَاهُ البُخَارِيُّ وَمُسْلِمٌ')
b += B.sharh(
    p('Four things are said in that sentence, and each one answers a fear a student of '
      'this creed will actually have:') +
    table([
        row(ar('لَا تَزَالُ طَائِفَة'),
            '<em>that the truth is never left without people upon it</em> — '
            '<strong>so a man standing on it is never the last</strong>'),
        row(ar('عَلَى الحَقِّ مَنْصُورَة'),
            '<em>that they are <strong>upon the truth</strong> and '
            '<strong>given victory</strong></em> — and the order matters: the victory is '
            'predicated of them <em>because</em> they are upon the truth'),
        row(ar('لَا يَضُرُّهُمْ مَنْ خَالَفَهُمْ'),
            '<em>the harm of <strong>open opposition</strong> is ruled out</em>'),
        row(ar('وَلَا مَنْ خَذَلَهُمْ'),
            '<em>and the harm of <strong>being forsaken</strong> — by those who should '
            'have stood with them and did not</em>'),
    ], fs='.91rem') +
    p('<strong>That fourth clause is the kindest thing in the ḥadīth.</strong> '
      'Opposition from an enemy is expected; <em>خِذْلَان</em> — abandonment by one\'s '
      'own — is the harder blow, and it is named separately and separately ruled out. '
      'And the promise runs <strong>%s</strong>, which is to say that there is no era in '
      'which a man can claim the thing has died out and he is excused.'
      % ar('حَتَّى تَقُومَ السَّاعَة')))

# ------------------------------------------------------------------ the dua
b += B.heading('الدُّعَاءُ الَّذِي خَتَمَ بِهِ', 'The Duʿāʾ He Closed With')
b += B.sharh(
    p('<em>Then the Shaykh sealed his blessed treatise <strong>with supplication, and '
      'with the ṣalāh and salām upon the Prophet ﷺ.</strong></em>'))
b += box(
    '<p style="margin:0 0 .6rem;font-size:1.02rem;text-align:center" dir="rtl" '
    'lang="ar"><strong>فَنَسْأَلُ اللهَ أَنْ يَجْعَلَنَا مِنْهُمْ، وَأَنْ لَا '
    'يُزِيغَ قُلُوبَنَا بَعْدَ إِذْ هَدَانَا</strong></p>'
    '<p style="margin:0;font-size:.95rem;text-align:center"><em>"So we ask Allah to make '
    'us of them, and not to turn our hearts aside after He has guided us."</em></p>')
b += B.prose(
    '<strong>Two requests, and it is worth asking why these two and not others.</strong> '
    'The first is <em>admission</em> — «make us of them». After fifty-three lessons of '
    'establishing what this group holds, the author does not claim membership in it; '
    'he asks for it. <strong>And the second is not a request for more knowledge, or for '
    'victory, or for the defeat of the sects he has spent the book answering. It is a '
    'request to be allowed to keep what he already has.</strong>')
b += B.prose(
    'And the wording of the second is taken from the Qurʾān. '
    '<em>«وَأَنْ لَا يُزِيغَ قُلُوبَنَا بَعْدَ إِذْ هَدَانَا»</em> is the duʿāʾ of '
    'those of understanding in Āl ʿImrān, and the whole burden of this treatise sits '
    'inside it: <strong>a man does not hold his creed by having once understood '
    'it.</strong> Guidance is held by being held onto, and the hearts that turn aside '
    'are hearts that had been guided — which is precisely the kind of thing a book that '
    'has catalogued seventy-two ways of going wrong ought to end by admitting.')
b += B.ayah(
    'رَبَّنَا لَا تُزِغْ قُلُوبَنَا بَعْدَ إِذْ هَدَيْتَنَا وَهَبْ لَنَا مِنْ '
    'لَدُنْكَ رَحْمَةً إِنَّكَ أَنْتَ الْوَهَّابُ',
    '"Our Lord, do not turn our hearts aside after You have guided us, and grant us '
    'mercy from Yourself. Indeed You are the Bestower."',
    'Sūrat Āl ʿImrān 3:8 · سُورَةُ آلِ عِمْرَان')
b += box(
    '<p style="margin:0 0 .5rem;font-size:.97rem"><strong>وَالحَمْدُ لِلَّهِ رَبِّ '
    'العَالَمِينَ، وَصَلَّى اللهُ وَسَلَّمَ عَلَى نَبِيِّنَا مُحَمَّدٍ، وَعَلَى '
    'آلِهِ وَصَحْبِهِ وَسَلَّمَ.</strong></p>'
    '<p style="margin:0;font-size:.93rem">With that, <strong>al-ʿAqīdah '
    'al-Wāsiṭiyyah is complete</strong> — fifty-four lessons, the full matn in Ibn '
    'Taymiyyah’s own order, with Shaykh Ṣāliḥ al-Fawzān’s sharḥ taken page by page from '
    'its opening to its last line. <strong>Nothing of the matn has been passed '
    'over.</strong></p>')

b += B.vocab([
    ('المَزِيَّةُ العُظْمَى', 'al-maziyyah al-ʿuẓmā', 'the greatest distinction',
     'That their way IS the religion of Islam — not the best way within it'),
    ('الشَّوْب', 'al-shawb', 'admixture',
     'الإِسْلَامُ المَحْضُ الخَالِصُ عَنِ الشَّوْب — the pure Islam, unmixed'),
    ('صَارَ', 'ṣāra', 'came to be',
     'The verb of the passage: the name Ahl al-Sunnah was imposed by the splitting, not '
     'chosen as a banner'),
    ('الفِرْقَةُ النَّاجِيَة', 'al-firqah al-nājiyah', 'the saved sect',
     'Identified not by its claims but by a historical test: whoever is upon the like of '
     'what he ﷺ and his Companions were upon'),
    ('الصِّدِّيقُون', 'al-ṣiddīqūn', 'the utterly truthful',
     'Those who go to the utmost in truthfulness and in affirming — the word used of '
     'Abū Bakr in Lesson 48'),
    ('الأَبْدَال', 'al-abdāl', 'the substitutes',
     'The awliyāʾ and devoted worshippers; named so because whenever one dies he is '
     'replaced — and in a narration from Aḥmad, they are أَصْحَابُ الحَدِيث'),
    ('مَصَابِيحُ الدُّجَى', 'maṣābīḥ al-dujā', 'the lamps of the darkness',
     'The author’s own phrase for the scholars among them, paired with '
     'أَعْلَامُ الهُدَى'),
    ('الطَّائِفَةُ المَنْصُورَة', 'al-ṭāʾifah al-manṣūrah', 'the group given victory',
     'Upon the truth and given victory — harmed neither by who opposes them nor by who '
     'forsakes them, until the Hour'),
    ('خَذَلَهُم', 'khadhalahum', 'forsook them',
     'Abandonment by those who should have stood with them — named and ruled out '
     'separately from open opposition'),
    ('لَا يُزِيغ', 'lā yuzīgh', 'may He not turn aside',
     'From أَزَاغَ, to turn away — the author’s closing request, taken from the duʿāʾ of '
     'Āl ʿImrān 3:8'),
])
b += B.mcq('ws-l54', [
    ('What does the author give as their greatest distinction?',
     ['That they are the majority of the Ummah',
      'That their way IS the religion of Islam which Allah sent Muḥammad ﷺ with — not '
      'the best way within it',
      'That they possess the soundest chains of narration',
      'That the scholars have agreed upon their guidance'], 1),
    ('What does the particle لَكِنْ do in the closing passage?',
     ['It introduces an exception to the rulings of the creed',
      'It hinges the argument: their way needs no party name in principle, BUT the '
      'foretold splitting made a name necessary to be told apart by',
      'It contrasts the Companions with later generations',
      'It restricts the promise to a single era'], 1),
    ('What is the significance of the verb صَارَ?',
     ['That the group came into existence after the Companions',
      'That the name was something they BECAME — imposed by the splitting rather than '
      'chosen as a banner',
      'That their way changed over time',
      'That the sects became seventy-three in number'], 1),
    ('How is the saved sect identified?',
     ['By holding the correct opinions, which it alone claims',
      'By a historical test — whoever is upon the like of what he ﷺ was upon THAT DAY, '
      'and his Companions; so the question becomes one of evidence, not '
      'self-description',
      'By the agreement of the four imāms',
      'By being the most numerous of the sects'], 1),
    ('What does that identification NOT require?',
     ['That the Companions be honoured',
      'That the seventy-three sects be enumerated — once the saved group is fixed by '
      'what it is upon, counting the others is of no practical use',
      'That the ḥadīth be authentic',
      'That the Qurʾān be preferred to the Sunnah'], 1),
    ('How does this page treat the clause «هُمْ مَنْ كَانَ عَلَى مِثْلِ مَا أَنَا '
     'عَلَيْهِ اليَوْمَ»?',
     ['It grades it ṣaḥīḥ on its own authority',
      'It reports the wording as the author gives it and supplies no grading, since the '
      'author says only «and in a ḥadīth from him» and al-Fawzān states none',
      'It omits it as unreliable',
      'It attributes the grading to al-Albānī'], 1),
    ('Who are الأَبْدَال, and what are the two explanations of the name?',
     ['The four imāms; named for replacing one another in leadership',
      'The awliyāʾ and devoted worshippers — named because whenever one dies he is '
      'replaced by another; and in a narration from Aḥmad, they are the people of ḥadīth',
      'The Companions who outlived the Prophet ﷺ',
      'Those who exchanged this world for the next'], 1),
    ('What do both explanations of الأَبْدَال have in common?',
     ['Both make them a fixed number in every age',
      'Both say that what persists is not an institution but a line of men — the '
      'religion is never left without those upholding or transmitting it',
      'Both restrict them to the Ḥijāz',
      'Both identify them with the four imāms'], 1),
    ('What four things does the ḥadīth say about the victorious group?',
     ['That they are few, poor, patient and rewarded',
      'That a group never ceases to exist; that they are upon the truth and given '
      'victory; that opposition does not harm them; and that being forsaken does not '
      'harm them either — until the Hour',
      'That they are in the Ḥaramayn, are scholars, are obeyed and are victorious',
      'That they fight, migrate, teach and are martyred'], 1),
    ('Why is the clause «وَلَا مَنْ خَذَلَهُمْ» significant?',
     ['Because it refers to the hypocrites of Madīnah',
      'Because abandonment by one’s own is a harder blow than an enemy’s opposition — so '
      'it is named and ruled out separately',
      'Because it abrogates the duty of mutual support',
      'Because it limits the promise to times of war'], 1),
    ('What does the author ask for in his closing duʿāʾ?',
     ['Victory over the sects he has answered',
      'To be made OF them, and that his heart not be turned aside after being guided — '
      'admission, and the keeping of what he already has',
      'Knowledge of what he has not yet learnt',
      'Forgiveness for errors in the treatise'], 1),
    ('Where is the wording of the second request from?',
     ['The ḥadīth of the victorious group',
      'The duʿāʾ of those of understanding in Āl ʿImrān 3:8 — «Our Lord, do not turn our '
      'hearts aside after You have guided us»',
      'Sūrat al-Fātiḥah', 'The khuṭbah at Ghadīr Khumm'], 1),
    ('What does that closing request concede about creed?',
     ['That it may be differed over',
      'That a man does not hold his creed by having once understood it — the hearts that '
      'turn aside are hearts that HAD been guided',
      'That knowledge of it is not obligatory',
      'That it cannot be fully known in this world'], 1),
])
b += B.tf('ws-l54-tf', [
    ('طَرِيقَةُ أَهْلِ السُّنَّةِ مَذْهَبٌ مِنْ مَذَاهِبِ الإِسْلَامِ لَا الإِسْلَامُ '
     'نَفْسُهُ.',
     'The way of Ahl al-Sunnah is one school within Islam rather than Islam itself.',
     False),
    ('تَعْيِينُ الفِرْقَةِ النَّاجِيَةِ مَوْقُوفٌ عَلَى عَدِّ الثَّلَاثِ '
     'وَالسَّبْعِينَ.',
     'Identifying the saved sect depends on enumerating the seventy-three.', False),
    ('الأَبْدَالُ قِيلَ إِنَّهُمْ أَصْحَابُ الحَدِيثِ فِي رِوَايَةٍ عَنْ أَحْمَدَ.',
     'It is said, in a narration from Aḥmad, that the abdāl are the people of ḥadīth.',
     True),
    ('حَدِيثُ الطَّائِفَةِ المَنْصُورَةِ رَوَاهُ البُخَارِيُّ وَمُسْلِمٌ.',
     'The ḥadīth of the victorious group is narrated by al-Bukhārī and Muslim.', True),
    ('خَتَمَ المُؤَلِّفُ رِسَالَتَهُ بِسُؤَالِ النَّصْرِ عَلَى المُخَالِفِينَ.',
     'The author sealed his treatise by asking for victory over his opponents.', False),
])
b += B.memorize(
    'وَأَنْ لَا يُزِيغَ قُلُوبَنَا بَعْدَ إِذْ هَدَانَا',
    'The last words of the matn, and the right ones to end on. After a treatise that has '
    'established the attributes of Allah, the Last Day, the Decree, the Companions and '
    'the manners of the saved group, <strong>the author asks neither for more knowledge '
    'nor for victory. He asks to be allowed to keep what he has.</strong> '
    '<em>Because the hearts that turn aside are hearts that had been guided</em> — which '
    'is the one danger a book like this cannot protect its reader from.')
b += B.aiquiz('The conclusion of al-Aqidah al-Wasitiyyah: the greatest distinction that '
              'their way IS the religion of Islam rather than a school within it, the '
              'hinge of the particle lakin and the force of the verb sara, the saved sect '
              'identified by a historical test rather than by its claims and why that does '
              'not require enumerating the seventy-three, al-siddiqun and al-shuhada and '
              'al-salihun and alam al-huda, the two explanations of al-abdal including the '
              'narration from Ahmad that they are ashab al-hadith, the four clauses of the '
              'hadith of the victorious group in al-Bukhari and Muslim with the separate '
              'ruling out of khidhlan, and the closing dua for admission and for the heart '
              'not to be turned aside, taken from Al Imran 3:8')
b += B.further()
b += B.nav('was-l53-makarim-al-akhlaq.html', 'Noble Character and Beautiful Deeds',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l54')

io.open(os.path.join(B.AQ, 'was-l54-khatimah.html'), 'w',
        encoding='utf-8', newline='\n').write(B.shell(
    'خَاتِمَةُ الرِّسَالَة',
    'The Conclusion of the Treatise',
    'Lesson 54, closing al-ʿAqīdah al-Wāsiṭiyyah: their way IS the religion of Islam; '
    'how the saved sect is identified by a historical test rather than by its own '
    'claims; who the group contains, and the two explanations of al-abdāl; the four '
    'clauses of the ḥadīth of the victorious group; and the author’s closing duʿāʾ — for '
    'admission, and for a heart that is not turned aside after guidance.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الرَّابِعُ وَالخَمْسُون', '6',
           'خَاتِمَةُ الرِّسَالَة',
           'The Conclusion of the Treatise', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l54-khatimah.html')
