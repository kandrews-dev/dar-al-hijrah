# -*- coding: utf-8 -*-
"""Lesson 15 — MCQ bank, first half (the permission, the ijmāʿ, the excuses,
the civilities, the three categories, the household, residence, the state).
"""

QS = [
    ('Under what heading does the sharḥ open the second half of the eighth '
     'nullifier?',
     ['<span dir="rtl" lang="ar">الاسْتِعَانَةُ بِالكُفَّارِ عَلَى '
      'الكُفَّار</span> — seeking the help of disbelievers against '
      'disbelievers',
      '<span dir="rtl" lang="ar">حُكْمُ المُرْتَدّ</span>',
      '<span dir="rtl" lang="ar">نَوَاقِضُ الوُضُوء</span>',
      '<span dir="rtl" lang="ar">بَابُ الجِهَاد</span>'], 0),
    ('In Ibn Bāz’s own words, what is the one thing that is '
     '<strong>not</strong> permitted?',
     ['Seeking any help at all from a disbeliever',
      '<span dir="rtl" lang="ar">أَنْ يَنْصُرَ الكُفَّارَ عَلَى '
      'المُسْلِمِين</span> — giving the disbelievers victory over the Muslims',
      'Trading with a disbelieving state',
      'Living in a disbelieving country for any reason'], 1),
    ('He applies the distinction to a case of his own lifetime. What does he '
     'say about seeking the help of some disbelievers against Ṣaddām?',
     ['That it is the apostasy the scholars mention',
      'That he declines to rule on contemporary cases',
      'That it is of what <strong>protects the Muslims and their lands</strong> '
      'from the criminals and the aggressors',
      'That it is permitted only if no Muslim army exists'], 2),
    ('What is the sentence with which he separates the two cases?',
     ['<span dir="rtl" lang="ar">وَفَرْقٌ بَيْنَ الاثْنَيْن</span> — and '
      'there is a difference between the two',
      '<span dir="rtl" lang="ar">كِلَاهُمَا سَوَاء</span>',
      '<span dir="rtl" lang="ar">هَذَا مَحَلُّ نَظَر</span>',
      '<span dir="rtl" lang="ar">فِيهِ خِلَافٌ قَوِيّ</span>'], 0),
    ('When the fiqh chapter «<span dir="rtl" lang="ar">بَابُ حُكْمِ '
     'المُرْتَدّ</span>» lists aiding the disbelievers, what does Ibn Bāz say '
     'that chapter was actually about?',
     ['Any dealing whatever with a disbelieving state',
      'Residing in a land of disbelief',
      '<span dir="rtl" lang="ar">أَنْ يَنْصُرَ المُسْلِمُ الكَافِرَ عَلَى '
      'إِخْوَانِهِ المُسْلِمِين</span> — a Muslim giving a disbeliever '
      'victory over his Muslim brothers',
      'Accepting money from disbelievers'], 2),
    ('The ijmāʿ he reports is on which act?',
     ['Sitting with disbelievers and eating with them',
      'Residing in their lands without need',
      'Returning their greeting',
      'Backing the disbelievers against the Muslims and aiding them '
      '<strong>بِأَيِّ نَوْعٍ مِنَ المُسَاعَدَة</strong>'], 3),
    ('Which scholar’s transmission of that ijmāʿ does the footnote cite '
     'first, and why?',
     ['<span dir="rtl" lang="ar">ابْنُ حَزْم</span> — because Ibn Bāz says he '
      'is <strong>مِنْ أَعْلَمِ النَّاسِ بِالإِجْمَاعِ وَالخِلَاف</strong>',
      '<span dir="rtl" lang="ar">ابْنُ حَجَر</span> — because of <em>al-Fatḥ</em>',
      '<span dir="rtl" lang="ar">النَّوَوِيّ</span> — because of <em>Sharḥ Muslim</em>',
      '<span dir="rtl" lang="ar">الذَّهَبِيّ</span> — because of his gradings'], 0),
    ('The author of the matn himself is quoted on this clause. Which four '
     'words in his sentence show that this nullifier has its own door?',
     ['<span dir="rtl" lang="ar">وَلَوْ لَمْ يُشْرِك</span> — even if he did '
      'not commit shirk',
      '<span dir="rtl" lang="ar">وَلَوْ كَانَ جَاهِلًا</span>',
      '<span dir="rtl" lang="ar">إِلَّا أَنْ يَتُوب</span>',
      '<span dir="rtl" lang="ar">بَعْدَ إِقَامَةِ الحُجَّة</span>'], 0),
    ('The first excuse the sharḥ refuses is kinship. What is the answer to a '
     'man who says he aided them for the sake of his relatives and children?',
     ['It is accepted if the fear was genuine',
      '<span dir="rtl" lang="ar">لَا يَنْفَعُهُ هَذَا</span> — it does not '
      'benefit him; it is tawallī and apostasy <strong>عِنْدَ جَمِيعِ '
      'أَهْلِ العِلْم</strong>',
      'It is a sin but not tawallī',
      'The matter is referred to the walī al-amr'], 1),
    ('In the footnote from <em>Miṣbāḥ al-Ẓalām</em>, what single act is named '
     'as the line Allah set for the protection of such a man’s blood?',
     ['Pronouncing the shahādah in public',
      'Paying the zakāh',
      '<span dir="rtl" lang="ar">اعْتِزَالُ قِتَالِ المُسْلِمِين</span> — '
      'withdrawing from fighting the Muslims',
      'Emigrating within the year'], 2),
    ('What does Ibn Taymiyyah say the exegetes are <em>agreed</em> upon '
     'regarding the cause of revelation of al-Māʾidah 5:52?',
     ['That it was revealed about the Jews of Madīnah',
      'That it was revealed about the people of the Book generally',
      'That it was revealed about men who allied with the disbelievers '
      '<strong>لِلْخَوْفِ الَّذِي فِي قُلُوبِهِم</strong> — out of the fear '
      'in their hearts, not because they believed the disbelievers were right',
      'That no agreement exists on its cause of revelation'], 2),
    ('What does the compiler say that footnote establishes?',
     ['That fear is an excuse which lifts the ruling',
      '<strong>بَاعِثَ التَّوَلِّي</strong> — the motive of the siding-with, '
      'and that it was not love of their religion',
      'That the verse is not muḥkamah',
      'That the men in question were disbelievers from the outset'], 1),
    ('What does the nationalism passage reduce to, in Ibn Bāz’s own words?',
     ['A political error with no religious dimension',
      'A permissible worldly arrangement',
      'An error only when its leaders are disbelievers',
      '<strong>مُوَالَاةٌ وَمُعَادَاةٌ وَحُبٌّ وَبُغْضٌ عَلَى غَيْرِ '
      'دِينِ الله</strong> — allying and opposing, loving and hating, on '
      'something other than the religion of Allah'], 3),
    ('Ibn Taymiyyah states expressly that '
     '﴿<span dir="rtl" lang="ar">وَمَنْ يَتَوَلَّهُمْ مِنْكُمْ فَإِنَّهُ '
     'مِنْهُمْ</span>﴾ is what?',
     ['<span dir="rtl" lang="ar">آيَةٌ مَنْسُوخَة</span>',
      '<span dir="rtl" lang="ar">آيَةٌ مُحْكَمَة</span> — a verse not open '
      'to being softened',
      '<span dir="rtl" lang="ar">آيَةٌ مُتَشَابِهَة</span>',
      '<span dir="rtl" lang="ar">خَاصَّةٌ بِأَهْلِ المَدِينَة</span>'], 1),
    ('If the Christians showed the believers love and affection first, what '
     'then?',
     ['<span dir="rtl" lang="ar">لَمْ يَجُزْ لِأَهْلِ الإِيمَانِ أَنْ '
      'يُوَادُّوهُمْ وَيُوَالُوهُم</span> — reciprocity is not a ground',
      'Affection becomes permitted by way of repayment',
      'It becomes obligatory to return the affection',
      'The matter is left to each person’s judgement'], 0),
    ('According to the qāʿidah of istiḥlāl as the sharḥ states it, what two '
     'conditions must the matter meet before declaring it lawful is apostasy?',
     ['That the person be a scholar, and that he repeat it',
      'That it be well known, and that he be warned',
      'That it be <strong>مُجْمَعٌ عَلَيْه</strong>, and that there be '
      '<strong>مَا فِيهِ خِلَافٌ وَلَا شُبْهَة</strong> — no disagreement in '
      'it and no doubt',
      'That it be mentioned in the Qurʾān by name'], 2),
    ('Taking disbelievers as intimate companions — <span dir="rtl" lang="ar">'
     'أَصْحَابًا وَأَخْدَانًا</span> — is what, in his words?',
     ['The nullifier itself',
      'Permitted at need',
      '<strong>مِنْ كَبَائِرِ الذُّنُوبِ وَمِنْ وَسَائِلِ الكُفْرِ '
      'بِالله</strong> — of the major sins and of the means to disbelief',
      'A matter of disagreement'], 2),
    ('Asked the ruling on allying with the mushrikīn, what is the first word '
     'of his answer?',
     ['<span dir="rtl" lang="ar">المُوَالَاةُ أَقْسَام</span> — allying is of '
      'several kinds',
      '<span dir="rtl" lang="ar">كُلُّهَا رِدَّة</span>',
      '<span dir="rtl" lang="ar">كُلُّهَا مَعْصِيَة</span>',
      '<span dir="rtl" lang="ar">لَا أَعْلَمُ ذَلِك</span>'], 0),
    ('Sitting with them to eat, drink and laugh is, in his answer, what?',
     ['Apostasy',
      'Permitted without restriction',
      '<strong>مَعْصِيَةٌ بِخِلَافِ التَّوَلِّي</strong> — a sin, expressly '
      'unlike siding-with',
      'Disliked but not sinful'], 2),
    ('He distinguishes three degrees of love. Which is correct?',
     ['All three are disbelief',
      'All three are permitted at need',
      'Love of their religion is a sin; natural love is disbelief',
      'Love of their religion is <strong>كُفْر</strong>; natural love — '
      'because he is a father or relative — is of <strong>muwālāh and not '
      'tawallī</strong>, and is still <strong>not permitted</strong>, being a '
      'means to something greater'], 3),
    ('Returning a disbeliever’s greeting when he greets first, and asking '
     'after his children, is what?',
     ['<span dir="rtl" lang="ar">لَيْسَ هَذَا مِنَ المُوَالَاة</span> — not '
      'even the lesser tier; these are <strong>مُجَامَلَات</strong>',
      'Tawallī',
      'Muwālāh, and therefore a sin',
      'Permitted only with relatives'], 0),
    ('Eating with a disbeliever and accepting his invitation — what precedent '
     'does he cite?',
     ['The treaty of al-Ḥudaybiyah',
      'The Prophet ﷺ accepting the invitation of the Jews and eating of their '
      'food, where a lawful benefit was in view',
      'The hiring of Ibn Urayqiṭ',
      'The ransom of the captives of Badr'], 1),
    ('Reciting ruqyah over a disbeliever: what is his ruling, and on what '
     'verse?',
     ['Forbidden in every case',
      'Permitted only for the people of the Book',
      'Permitted where there is no state of war between us — on al-Mumtaḥanah '
      '60:8',
      'Permitted only if he asks for it himself'], 2),
    ('Who is named alongside Ibn Bāz on that ruqyah fatwā of the Lajnah?',
     ['<span dir="rtl" lang="ar">الغُدَيَّان · الفَوْزَان · بَكْر أَبُو '
      'زَيْد · عَبْدُ العَزِيزِ آلُ الشَّيْخ</span>',
      '<span dir="rtl" lang="ar">الأَلْبَانِيّ · ابْنُ عُثَيْمِين</span>',
      '<span dir="rtl" lang="ar">ابْنُ حَزْم · ابْنُ تَيْمِيَّة</span>',
      'No one; he gave it alone'], 0),
    ('Asked whether a Muslim may be glad at a calamity striking a '
     'disbelieving country, what reason does he give for permitting it?',
     ['Because they are enemies and deserve it',
      'Because it weakens them militarily',
      'Because <strong>قَدْ يَكُونُ مَوْعِظَةً لَهُم، قَدْ يَكُونُ فِيهِ '
      'هِدَايَة</strong> — it may be an admonition for them, it may contain '
      'guidance',
      'He does not permit it at all'], 2),
    ('In the footnote on that question, how does al-Nawawī gloss the '
     'Prophet’s ﷺ laughter in the report of Saʿd ibn Abī Waqqāṣ?',
     ['<span dir="rtl" lang="ar">فَرَحًا بِقَتْلِهِ عَدُوًّا، لَا '
      'لِانْكِشَافِه</span> — out of gladness at his killing an '
      'enemy, not at his being exposed',
      'Out of amusement at what had happened to the man',
      'As a sign of displeasure',
      'The gloss is not given'], 0),
    ('In his division of mankind into three, what is owed to the first — the '
     '<span dir="rtl" lang="ar">مُؤْمِنُونَ خُلَّص</span>?',
     ['Love only, with no further duty',
      '<strong>المَحَبَّةُ وَالوِلَايَةُ وَالنَّصْرَةُ وَالتَّأْيِيدُ '
      'وَالتَّعَاوُنُ مَعَهُمْ فِي كُلِّ خَيْر</strong>',
      'Neutrality unless they are of one’s own land',
      'Support only in matters of religion, not of the world'], 1),
    ('The footnote glosses his words «<span dir="rtl" lang="ar">فِي عَهْدِهِ '
     'ﷺ وَبَعْدَ ذَلِك</span>». What does it say they mean?',
     ['The lifetime of the Companions only',
      '<span dir="rtl" lang="ar">أَيْ: فِي جَمِيعِ الأَزْمِنَة</span> — in '
      'all times',
      'The first three generations',
      'Until the conquest of Makkah'], 1),
    ('What is owed to the <strong>third</strong> category — the Muslim who '
     'has sins and shortcomings?',
     ['He is treated as a disbeliever until he repents',
      'He is loved without qualification',
      'He is disowned until he corrects himself',
      'Walāyah and love <strong>مِنْ جَانِب</strong>, and dislike, direction '
      'and correction <strong>مِنْ جَانِبٍ آخَر</strong> — loved for his '
      'Islām, disliked <strong>عَلَى قَدْرِ مَعَاصِيه</strong>'], 3),
    ('With what words does the entry on that third category end?',
     ['<span dir="rtl" lang="ar">وَاللهُ أَعْلَم</span>',
      '<span dir="rtl" lang="ar">فَيُهْجَرُ حَتَّى يَتُوب</span>',
      '<span dir="rtl" lang="ar">وَلَا يُهْمَل</span> — and he is not to be '
      'abandoned',
      '<span dir="rtl" lang="ar">فَهُوَ مِنْهُم</span>'], 2),
    ('In the passage on the Prophet’s ﷺ household, which two of its members '
     'does he name as obliged to be hated for Allah’s sake?',
     ['<span dir="rtl" lang="ar">أَبُو لَهَبٍ وَأَبُو طَالِب</span>',
      '<span dir="rtl" lang="ar">عَلِيٌّ وَالعَبَّاس</span>',
      '<span dir="rtl" lang="ar">الحَسَنُ وَالحُسَيْن</span>',
      'None of them; lineage protects them'], 0),
    ('How far does he push the criterion of faith over lineage in that '
     'passage?',
     ['Only as far as the Quraysh',
      'He does not extend it beyond Banū Hāshim',
      'As far as the believers of Banū Hāshim being loved as those of Tamīm '
      'and Qaḥṭān are — <strong>حَتَّى العَبْدُ المَمْلُوك</strong> — while a '
      'disbeliever is hated <strong>وَلَوْ كَانَ مِنْ أَوْلَادِ '
      'الأَنْبِيَاء</strong>',
      'Only to those alive in his own time'], 2),
    ('A man came to love ʿAbd al-Muṭṭalib and Abū Ṭālib for their protection '
     'of the Prophet ﷺ. What is the answer?',
     ['Their protection does <strong>not</strong> oblige love of them — ʿAbd '
      'al-Muṭṭalib died upon the religion of Jāhiliyyah, and Abū Ṭālib knew '
      'the truth and did not act on it',
      'Such love is obligatory in gratitude',
      'Such love is permitted but not obligatory',
      'The question is not answered'], 0),
    ('What did Abū Ṭālib say at his death, as the sharḥ reports it?',
     ['He pronounced the shahādah',
      'He asked for more time',
      'He said nothing at all',
      '(<span dir="rtl" lang="ar">هُوَ عَلَى مِلَّةِ عَبْدِ '
      'المُطَّلِب</span>)'], 3),
    ('Put the two halves of the eighth nullifier together: the first cited '
     'Abū Ṭālib’s protection as proof that accepting a disbeliever’s help is '
     'permitted, and this half says that protection does not oblige love of '
     'him. What follows?',
     ['One of the two passages must be a mistake',
      'That a Muslim may lawfully <strong>accept</strong> a disbeliever’s '
      'shelter and still owe him <strong>barāʾah</strong> — what you may do '
      'with a man and what you may give him in your heart are two questions',
      'That accepting help from disbelievers is forbidden after all',
      'That love of a disbeliever is permitted if he has helped you'], 1),
    ('What does Ibn Bāz say «<span dir="rtl" lang="ar">ظَالِمِي '
     'أَنْفُسِهِم</span>» means in al-Nisāʾ 4:97?',
     ['By their hypocrisy',
      '<strong>بِالإِقَامَةِ بَيْنَ المُشْرِكِين</strong> — by their '
      'residence among the mushrikīn',
      'By their refusal to fight',
      'By their disbelief'], 1),
    ('What does the sharḥ say the verse was revealed about?',
     ['The hypocrites of Madīnah',
      'Muslims who remained in Makkah and went out with the enemies of Allah '
      'at Badr — <strong>وَالمَشْهُورُ أَنَّهُمْ كَانُوا '
      'مُكْرَهِين</strong>',
      'The people of the Book who withheld help',
      'Those who fled from the battle'], 1),
    ('What does he say would have been the ruling had they gone out fighting '
     'willingly?',
     ['They would have been sinners only',
      'The matter would be referred to the walī al-amr',
      '<span dir="rtl" lang="ar">كَانُوا مُرْتَدِّين</span>',
      'There is no report on this'], 2),
    ('In the two cases he divides them into, what is said of the one who was '
     '<strong>coerced</strong> and did not consent?',
     ['He has no blame of any kind',
      'He is a disbeliever like the first',
      'He <strong>sinned by residing among them and by not hastening to '
      'hijrah</strong>, and his residence became a <strong>وَسِيلَةٌ '
      'وَذَرِيعَة</strong> to what followed',
      'He must be killed as a bāghī'], 2),
    ('What preventative does this folio name against the whole danger of '
     'residence among them?',
     ['Concealing one’s religion',
      'Avoiding their language',
      '<span dir="rtl" lang="ar">الهِجْرَة</span> — emigration, before the '
      'situation does the choosing',
      'Seeking a fatwā each time'], 2),
    ('Al-Nisāʾ 4:98–99 names an exception. Who is it, and what is held out '
     'to them?',
     ['The scholars; they are given licence to remain',
      'The wealthy; they are told to ransom themselves',
      'Those who remained for trade; they are warned',
      'The <strong>oppressed</strong> who can devise no plan and find no way '
      '— <strong>عَسَى اللهُ أَنْ يَعْفُوَ عَنْهُم</strong>'], 3),
    ('On a Muslim government aiding a disbelieving state, what does Ibn Bāz '
     'permit?',
     ['Nothing whatever, in any circumstance',
      'Any alliance the ruler judges useful, without condition',
      'Aid where there is <strong>مَصْلَحَةٌ لِلْمُسْلِمِين</strong> and the '
      'repelling of a greater enemy and a greater evil — resting on '
      '<strong>نِيَّةٍ صَالِحَةٍ… وَنَظَرٍ فِي المَصَالِح</strong>',
      'Only the payment of ransom'], 2),
    ('How does the footnote fence that permission?',
     ['It does not; it is left open',
      'By requiring the consent of the scholars of the land',
      'By limiting it to one year at a time',
      '<strong>فِي غَيْرِ حَرْبٍ وَلَا مُظَاهَرَةٍ لَهُمْ عَلَى '
      'المُسْلِمِين</strong>, for a general Muslim benefit, '
      '<strong>كَفَكِّ الأَسْرَى</strong>'], 3),
]
