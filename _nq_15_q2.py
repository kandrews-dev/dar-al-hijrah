# -*- coding: utf-8 -*-
"""Lesson 15 — MCQ bank, second half (mutual support, the spy, Ḥāṭib), then
the vocabulary, the true/false set, the memorisation line and the nav.
"""
from _nq_15_lib import B, p, ar
from _nq_15_q1 import QS

QS = QS + [
    ('Under the book’s own heading on mutual support, which two verses does '
     'the sharḥ set against one another?',
     ['al-Tawbah 9:67 on the hypocrites, and 9:71 on the believing men and '
      'women being <strong>أَوْلِيَاءُ بَعْض</strong>',
      'al-Māʾidah 5:51 and 5:82',
      'al-Mumtaḥanah 60:1 and 60:8',
      'al-Nisāʾ 4:97 and 4:99'], 0),
    ('What does he say the walāyah between believers <em>requires</em>?',
     ['Agreement in every matter of opinion',
      'Financial support alone',
      '<strong>النَّصِيحَةَ وَالتَّوْجِيهَ وَالإِعَانَةَ عَلَى '
      'الخَيْر</strong>, and the absence of envy, deceit, betrayal and '
      'wrongdoing',
      'Nothing beyond refraining from harm'], 2),
    ('If a Muslim deceives or betrays his brother, what does the sharḥ call '
     'it?',
     ['A worldly matter outside the chapter',
      '<strong>نَقْصٌ فِي الإِيمَانِ وَضَعْفٌ فِي هَذِهِ '
      'الوِلَايَة</strong> — and the duty is <strong>الاسْتِدْرَاك</strong>',
      'The nullifier itself',
      'Nothing is said of it here'], 1),
    ('What does he say about nationalities when speaking of the believers?',
     ['They are a lawful basis of preference',
      'They determine who one must support',
      '<strong>الجِنْسِيَّاتُ هَذِهِ لَا قِيمَةَ لَهَا، الجِنْسِيَّةُ '
      'العَامَّةُ هِيَ الإِسْلَام</strong>',
      'He does not discuss them'], 2),
    ('Put the two nationalism passages together. What is the single principle?',
     ['Arabness is a valid bond; other nationalities are not',
      'Nationality is refused as a ground for walāʾ with disbelievers '
      '<em>and</em> as a ground for withholding walāʾ from believers',
      'Nationality matters only in time of war',
      'Nationality is a worldly matter with no bearing either way'], 1),
    ('In his gloss on «<span dir="rtl" lang="ar">المُؤْمِنُ لِلْمُؤْمِنِ '
     'كَالْبِنْيَان</span>», what does he say of the lower part of the '
     'building?',
     ['It is the least important part',
      '<strong>أَمْسَكَ أَسْفَلُهَا أَعْلَاهَا، وَإِنْ سَقَطَ أَسْفَلُهَا '
      'سَقَطَت</strong> — the lower holds the upper, and if the lower falls '
      'the whole falls',
      'It need not be sound if the upper is',
      'The image is not explained'], 1),
    ('Which two things does he include <em>inside</em> his definition of '
     'Islamic brotherhood?',
     ['Unanimity of opinion and avoidance of dispute',
      'Shared lineage and shared land',
      '<strong>الأَخْذُ عَلَى يَدِ السَّفِيهِ وَرَدُّ الظَّالِمِ عَنْ '
      'ظُلْمِه</strong> — restraining the fool and turning the wrongdoer back',
      'Silence about one another’s faults'], 2),
    ('On jihād, what does he say is <strong>not</strong> found in the Book and '
     'the Sunnah?',
     ['That the Muslims are one body',
      'That cooperation is obliged',
      'Any indication that the one whom the enemy has fallen upon is '
      '<strong>alone</strong> responsible for the jihād',
      'Any indication that the distant are excused'], 2),
    ('The sharḥ says the spy’s harm is great. What does it say of Ḥāṭib '
     'specifically?',
     ['That he deserved no punishment at all',
      'That he was a hypocrite whose cover was lifted',
      'That he deserved killing <strong>لَوْلَا أَنَّهُ شَهِدَ بَدْرًا '
      'وَصَدَّقَهُ النَّبِيُّ ﷺ</strong>',
      'That his case is not reported soundly'], 2),
    ('Asked whether a spy is killed as a ḥadd or as a disbeliever, what is '
     'the answer?',
     ['Always as a disbeliever',
      'Always as a ḥadd',
      'The question is declined',
      '<strong>عَلَى حَسَبِ حَالِه</strong> — as a disbeliever if he spies '
      'for the disbelievers, and as the <strong>بُغَاة</strong> are killed if '
      'he spies for rebels'], 3),
    ('«<span dir="rtl" lang="ar">عَلَى حَسَبِ حَالِه</span>» belongs to a '
     'pattern in this book. Which of these is the <em>same</em> move?',
     ['<span dir="rtl" lang="ar">هَذَا أَصْلٌ أَصِيل</span>',
      '<span dir="rtl" lang="ar">فِيهِ التَّفْصِيل</span> on the magician, '
      'and <span dir="rtl" lang="ar">عَلَى حَسَبِ التَّوْلِيَة</span> on 5:51',
      '<span dir="rtl" lang="ar">نَسْأَلُ اللهَ العَافِيَة</span>',
      '<span dir="rtl" lang="ar">هَذَا مِنْ نَوَاقِضِ الإِسْلَام</span>'], 1),
    ('What are the <strong>two</strong> preventers that Ibn Bāz says came '
     'together for Ḥāṭib?',
     ['His kinship to Quraysh and his poverty',
      'His <strong>تَأْوِيل</strong>, and his having been present at Badr '
      'with the ṣaḥīḥ ḥadīth attached to its people',
      'His repentance and his ignorance',
      'His coercion and his youth'], 1),
    ('Does the sharḥ soften the description of the act itself?',
     ['Yes — it calls it a minor sin',
      'Yes — it says it was not really spying',
      'No — it says <strong>التَّجَسُّسَ تَوَلٍّ لِلْمُشْرِكِين، رِدَّةٌ '
      'تُوجِبُ القَتْل</strong>, and holds that beside the man’s being '
      'excused',
      'It gives no description of the act'], 2),
    ('What is the distinction that makes those two statements consistent?',
     ['A distinction between war and peace',
      'A distinction between the Companions and those after them',
      'A distinction between major and minor shirk',
      'The distinction between the ruling on an <strong>act</strong> and the '
      'ruling on a <strong>particular man</strong>'], 3),
    ('Which section of this book is that distinction the subject of?',
     ['<span dir="rtl" lang="ar">نَوَاقِضُ الوُضُوء</span>',
      '<span dir="rtl" lang="ar">بَابُ الجِهَاد</span>',
      '<span dir="rtl" lang="ar">مَوَانِعُ تَكْفِيرِ المُعَيَّن</span> — the '
      'barriers to declaring a particular person a disbeliever',
      '<span dir="rtl" lang="ar">كِتَابُ التَّوْحِيد</span>'], 2),
    ('Al-Rājiḥī and Ibn Bāz differ on one question. What is it?',
     ['Whether Ḥāṭib’s act was tawallī at all',
      'Whether the spy is killed',
      'Whether the two preventers can ever combine again for anyone after '
      'Ḥāṭib',
      'Whether Ḥāṭib was present at Badr'], 2),
    ('What is al-Rājiḥī’s position?',
     ['<strong>مَا يَجْتَمِعَان</strong> — they cannot combine; whoever spies '
      'on the Muslims is killed',
      'They combine for every sincere Muslim',
      'The question belongs to the walī al-amr',
      'He does not address it'], 0),
    ('And what is Ibn Bāz’s answer when asked directly?',
     ['He agrees that they cannot combine',
      '<strong>الأَظْهَر</strong> that a man with such prior service may be '
      'treated as the Prophet ﷺ treated Ḥāṭib — <em>while</em> '
      '<strong>الأَصْلُ أَنَّ الجَاسُوسَ يُقْتَل</strong>',
      'That the spy is never killed',
      'That the case cannot arise again'], 1),
    ('Whose judgement does Ibn Bāz say the exception rests with?',
     ['The man himself, if he is sincere',
      'The scholars of his locality',
      'His family and tribe',
      '<strong>وَلِيُّ الأَمْر</strong> — who may see that his record '
      'intercedes for the acceptance of his excuse'],
     3),
    ('In another sitting Ibn Bāz says «<span dir="rtl" lang="ar">فَغَيْرُ '
     'حَاطِبٍ لَا يُلْحَقُ بِهِ وَلَا يُسَاوِيه</span>». How does the lesson '
     'handle the two answers?',
     ['By quoting only the merciful one',
      'By quoting only the severe one',
      'By declaring one of them unreliable',
      'By giving both, and reading the second as a warning against turning '
      'the first into a rule — <strong>الأَصْل</strong> remains the killing'], 3),
    ('How many imāms does the footnote name as having stated expressly that '
     'Ḥāṭib was a <span dir="rtl" lang="ar">مُتَأَوِّل</span>?',
     ['Two', 'Five', 'Fourteen — from al-Qāḍī Abū Yaʿlā to Ibn ʿUthaymīn',
      'The number is not given'], 2),
    ('What did Ḥāṭib himself say, in the report of Jābir?',
     ['That he had erred out of ignorance of the ruling',
      'That he had been coerced',
      '<strong>لَمْ أَفْعَلْهُ غِشًّا… وَلَا نِفَاقًا؛ قَدْ عَلِمْتُ أَنَّ '
      'اللهَ مُظْهِرٌ رَسُولَهُ وَمُتِمٌّ لَهُ أَمْرَه</strong>',
      'Nothing is reported of his words'], 2),
    ('How is that report graded, and by whom?',
     ['It is weak by consensus',
      '<strong>بِسَنَدٍ صَحِيح</strong> — and <strong>Ibn Kathīr</strong> '
      'graded it <strong>عَلَى شَرْطِ مُسْلِم</strong>',
      'No grading is given',
      'It is graded ḥasan by al-Tirmidhī'], 1),
    ('And the report of Ibn ʿAbbās?',
     ['<strong>بِسَنَدٍ حَسَن</strong> — al-Ḥākim graded it ṣaḥīḥ and '
      '<strong>al-Dhahabī agreed</strong>; Ibn Kathīr: '
      '<strong>إِسْنَادٌ جَيِّد</strong>',
      'It is mursal and therefore set aside',
      'It is a fabrication',
      'Only al-Ṭaḥāwī reports it, without a grading'], 0),
    ('In that report, what reason does Ḥāṭib give for writing?',
     ['That he hoped for wealth from Quraysh',
      'That he doubted the outcome of the campaign',
      'That he was a stranger among the people of Makkah, his family were in '
      'their midst, and he feared for them — and that the letter '
      '<strong>لَا يَضُرُّ اللهَ وَرَسُولَه</strong>',
      'That he was ordered to by another'], 2),
    ('Which sentence of Ḥāṭib’s does al-Bukhārī preserve?',
     ['<span dir="rtl" lang="ar">إِنِّي تَائِبٌ إِلَى الله</span>',
      '<span dir="rtl" lang="ar">مَا أَرَدْتُ إِلَّا المَال</span>',
      '<span dir="rtl" lang="ar">وَاللهِ مَا كَفَرْتُ وَلَا ازْدَدْتُ '
      'لِلْإِسْلَامِ إِلَّا حُبًّا</span>',
      'None is preserved'], 2),
    ('The objection is raised: if an excused interpreter does not sin, why '
     'did Ḥāṭib need a good deed to be pardoned? What is the answer?',
     ['That he was not in fact an interpreter',
      'That the pardon was for his family’s sake',
      'That he <strong>did</strong> sin — by knowingly disobeying the order '
      'to conceal the news — and the <strong>taʾwīl</strong> lay in his '
      'belief that the disclosure would do the believers no harm',
      'That the objection is left unanswered'], 2),
    ('What does that answer establish about a man’s state?',
     ['That interpretation always removes the sin',
      'That a sin always implies disbelief',
      'That a man may be <strong>sinning and interpreting at once</strong> — '
      'the interpretation answering the takfīr while the sin answers for '
      'itself',
      'That the two can never coexist'], 2),
    ('Al-Qārī adds a point about Ḥāṭib’s ijtihād. What is it?',
     ['That it was sound in every respect',
      'That he fell short in concealing the matter and not seeking the '
      'Prophet’s ﷺ permission',
      'That he had no ijtihād at all',
      'That he should have emigrated instead'], 1),
    ('Al-Ṭaḥāwī’s principle explains why Ḥāṭib was not even punished. What is '
     'it?',
     ['That the Companions were exempt from punishment',
      'That spying carried no punishment at that time',
      'That the Prophet ﷺ pardoned all offences before Badr',
      'The Sunnah of <strong>إِقَالَةِ ذَوِي الهَيْئَاتِ '
      'عَثَرَاتِهِم</strong> — overlooking the slips of people of standing — '
      '<strong>إِلَّا فِي حَدٍّ مِنْ حُدُودِ الله</strong>'], 3),
    ('What is the control case that proves the exception in that principle?',
     ['The case of Māʿiz',
      'The case of the man who stole from the treasury',
      '<strong>قُدَامَة</strong> — whose offence contained a ḥadd of Allah, '
      'and <strong>neither ʿUmar nor ʿAlī nor anyone else</strong> lifted it '
      'for his standing',
      'No control case is given'], 2),
    ('So what does standing buy a man, and what does it not?',
     ['It buys him everything short of execution',
      'It buys him nothing at all',
      'It buys the overlooking of a punishment that is <strong>not</strong> a '
      'ḥadd; it does <strong>not</strong> lift a ḥadd of Allah’s',
      'It buys a lighter ḥadd'], 2),
    ('Al-Mumtaḥanah 60:1 was revealed about this very incident. What does its '
     'closing clause say of the one who does it?',
     ['<span dir="rtl" lang="ar">فَقَدْ كَفَرَ وَخَرَجَ مِنَ '
      'الإِسْلَام</span>',
      '<span dir="rtl" lang="ar">فَقَدْ ضَلَّ سَوَاءَ السَّبِيل</span> — he '
      'has strayed from the straight way',
      '<span dir="rtl" lang="ar">فَأُولَئِكَ هُمُ المُنَافِقُون</span>',
      '<span dir="rtl" lang="ar">فَلَا تَوْبَةَ لَه</span>'], 1),
    ('And what is the significance of that wording for this clause?',
     ['It shows the verse is abrogated',
      'It shows the verse concerns only the Companions',
      'It makes no difference to the ruling',
      'It names a straying, <strong>not</strong> an exit from Islām — and the '
      'man it was revealed about died a Muslim'], 3),
]

BODY = B.vocab([
    ('الاسْتِعَانَة', 'al-istiʿānah', 'seeking help',
     'Seeking another’s help. The heading this half of the clause opens '
     'under — and its first ruling is a permission, not a prohibition.'),
    ('المُظَاهَرَة', 'al-muẓāharah', 'backing against',
     'Backing someone against another. The matn’s own word for the '
     'nullifier, and the ijmāʿ is on it «بِأَيِّ نَوْعٍ مِنَ '
     'المُسَاعَدَة».'),
    ('المُجَامَلَات', 'al-mujāmalāt', 'ordinary civilities',
     'Returning a greeting, asking after a man’s children, answering his '
     'question. Ibn Bāz: «لَيْسَ هَذَا مِنَ المُوَالَاة» — not even the '
     'lesser tier.'),
    ('بِطَانَة', 'biṭānah', 'inner circle',
     'The lining of a garment, hence a man’s confidants. The Qurʾān forbids '
     'taking the disbelievers as this.'),
    ('القَوْمِيَّة', 'al-qawmiyyah', 'nationalism',
     'Loyalty organised around a people rather than the religion. Condemned '
     'here in both directions: «الجِنْسِيَّاتُ هَذِهِ لَا قِيمَةَ لَهَا».'),
    ('التَّجَسُّس', 'al-tajassus', 'spying',
     'Ibn Bāz: «تَوَلٍّ لِلْمُشْرِكِين، رِدَّةٌ تُوجِبُ القَتْل» — and the '
     'ruling on the man «عَلَى حَسَبِ حَالِه».'),
    ('السَّابِقَة', 'al-sābiqah', 'prior record',
     'A man’s standing earned beforehand. One of the two preventers in '
     'Ḥāṭib’s case — and what «قَدْ يَرَى فِيهَا وَلِيُّ الأَمْر».'),
    ('التَّأْوِيل', 'al-taʾwīl', 'interpretation',
     'The other preventer: Ḥāṭib believed his letter would do the believers '
     'no harm. A barrier to takfīr that leaves the sin standing.'),
    ('ذَوُو الهَيْئَات', 'dhawū al-hayʾāt', 'people of standing',
     'Al-Ṭaḥāwī: their slips are overlooked «إِلَّا فِي حَدٍّ مِنْ حُدُودِ '
     'الله» — and Qudāmah’s case is the proof of the exception.'),
])

BODY += B.mcq('nq-l15-mcq', QS)

BODY += B.tf('nq-l15-tf', [
    ('الاسْتِعَانَةُ بِالكُفَّارِ عَلَى الكُفَّارِ رِدَّةٌ عَنِ '
     'الإِسْلَامِ عِنْدَ ابْنِ بَاز.',
     'Seeking the help of disbelievers against disbelievers is apostasy for '
     'Ibn Bāz.', False),
    ('مُظَاهَرَةُ الكُفَّارِ عَلَى المُسْلِمِينَ رِدَّةٌ بِالإِجْمَاع.',
     'Backing the disbelievers against the Muslims is apostasy by ijmāʿ.',
     True),
    ('الخَوْفُ وَمُرَاعَاةُ الأَرْحَامِ عُذْرَانِ يَرْفَعَانِ هَذَا '
     'النَّاقِض.',
     'Fear and the care of relatives are two excuses that lift this '
     'nullifier.', False),
    ('رَدُّ السَّلَامِ عَلَى الكَافِرِ إِذَا سَلَّمَ لَيْسَ مِنَ '
     'المُوَالَاة.',
     'Returning a disbeliever’s greeting when he greets first is not of '
     'muwālāh.', True),
    ('المُسْلِمُ العَاصِي يُحَبُّ لِإِسْلَامِهِ وَيُبْغَضُ عَلَى قَدْرِ '
     'مَعَاصِيه.',
     'A sinning Muslim is loved for his Islām and disliked in the measure of '
     'his sins.', True),
    ('أَبُو طَالِبٍ مِنْ أَهْلِ البَيْتِ فَتَجِبُ مَحَبَّتُهُ لِحِمَايَتِهِ '
     'النَّبِيَّ ﷺ.',
     'Abū Ṭālib is of the household, so love of him is obliged for his '
     'protection of the Prophet ﷺ.', False),
    ('مَنَعَ التَّأْوِيلُ وَالسَّابِقَةُ تَكْفِيرَ حَاطِبٍ مَعَ أَنَّ '
     'الفِعْلَ نَفْسَهُ رِدَّةٌ تُوجِبُ القَتْل.',
     'Interpretation and prior record prevented Ḥāṭib’s takfīr, although the '
     'act itself is apostasy warranting execution.', True),
])

BODY += B.memorize(
    'وَهَذَا يُفِيدُ أَنَّ أَهْلَ السَّوَابِقِ وَالخَيْرِ العَظِيمِ إِذَا '
    'زَلُّوا وَتَأَوَّلُوا فَيَنْبَغِي أَنْ تُغْتَفَرَ لَهُمْ زَلَّاتُهُمْ '
    'نَظَرًا لِسَوَابِقِهِمْ العَظِيمَة؛ لِأَنَّ الإِنْسَانَ وَإِنْ بَلَغَ '
    'مَا بَلَغَ مِنَ العِلْمِ وَالفَضْلِ قَدْ يَزِلُّ وَقَدْ يَغْلَط',
    'Ibn Bāz, on the folios of the harshest clause in the book. '
    '<strong>This sentence stands inside the chapter on the spy, not somewhere '
    'safer.</strong> <em>A Companion did the thing the nullifier names, and '
    'was neither killed nor declared a disbeliever — because he had '
    'interpreted, and because of what he had done before. And the lesson Ibn '
    'Bāz draws is not about Ḥāṭib. It is about the people of prior service '
    'generally: that their slips should be overlooked.</em> '
    '<strong>And then the reason, which is the whole of it: «لِأَنَّ '
    'الإِنْسَانَ وَإِنْ بَلَغَ مَا بَلَغَ مِنَ العِلْمِ وَالفَضْلِ قَدْ '
    'يَزِلُّ وَقَدْ يَغْلَط» — because a man, however far he has come in '
    'knowledge and merit, may slip and may err.</strong> '
    '<em>Keep beside it the limit that keeps it honest: </em>'
    '<strong>الأَصْلُ أَنَّ الجَاسُوسَ يُقْتَل</strong><em>, and the '
    'overlooking is something «قَدْ يَرَى فِيهَا وَلِيُّ الأَمْر» — it '
    'belongs to the one who carries the case, never to the one hoping to '
    'escape it.</em>')

BODY += B.nav('nq-l14-al-muwalah-wa-al-tawalli.html',
              'النَّاقِضُ الثَّامِن · part 1',
              'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l15')
