# -*- coding: utf-8 -*-
"""Wasitiyyah L30 -- Part 3 opens: the standing of Ahl al-Sunnah among the
sects of the Ummah. The five pairs they stand between, each party named and
traced. Sharh pp.108-112."""
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
    '<em>المِصْبَاحُ المُنِير</em> — the lexicon al-Fawzān cites for the word '
    '<span dir="rtl" lang="ar">الوَسَط</span>.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


def pair(no, bab, left, left_txt, right, right_txt, mid):
    """One of the five 'between two extremes' sections, as a three-row table."""
    return (
        '<div style="overflow-x:auto;margin:0 0 1rem">'
        '<table style="width:100%%;border-collapse:collapse;font-size:.89rem">'
        '<tr><td colspan="2" style="padding:.5rem .75rem;border:1px solid var(--line);'
        'background:var(--ivory);font-weight:700">%s · %s</td></tr>'
        '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap;'
        'vertical-align:top" dir="rtl" lang="ar"><strong>%s</strong></td>'
        '<td style="padding:.55rem .75rem;border:1px solid var(--line)">%s</td></tr>'
        '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap;'
        'vertical-align:top" dir="rtl" lang="ar"><strong>%s</strong></td>'
        '<td style="padding:.55rem .75rem;border:1px solid var(--line)">%s</td></tr>'
        '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap;'
        'vertical-align:top;background:var(--brand-wash)" dir="rtl" lang="ar">'
        '<strong>أَهْلُ السُّنَّة</strong></td>'
        '<td style="padding:.55rem .75rem;border:1px solid var(--line);'
        'background:var(--brand-wash)">%s</td></tr>'
        '</table></div>' % (no, bab, left, left_txt, right, right_txt, mid))


b = B.objectives([
    'Say what %s means here, and the āyah al-Fawzān grounds it in.' % ar('الوَسَط'),
    'Name both extremes in each of the five bābs, and trace each name to its origin.',
    'Give the one-line summary of how Ahl al-Sunnah settle the question of %s.'
    % ar('الوَعْد وَالوَعِيد'),
    'State the definition of %s that al-Fawzān gives.' % ar('الصَّحَابِيّ'),
])

b += B.heading('القِسْمُ الثَّالِث · مَكَانَةُ أَهْلِ السُّنَّةِ بَيْنَ فِرَقِ الأُمَّة',
               'Part Three — The Standing of Ahl al-Sunnah among the Sects of the Ummah')
b += B.prose(
    'al-Fawzān explains why the author turns here, and the reasoning is a piece of pedagogy worth '
    'noting: <em>when the Shaykh رحمه الله had made clear the position of Ahl al-Sunnah toward the '
    'texts of the attributes, <strong>he wanted to make clear their standing among the sects of '
    'the Ummah, so that their worth and their excellence would be known by comparing them with '
    'others</strong> — for <strong>%s</strong>, the opposite is what shows up the goodness of its '
    'opposite, <strong>and %s</strong>, by their contraries things are made clear.</em>'
    % (ar('الضِّدَّ يُظْهِرُ حُسْنَهُ الضِّدُّ'), ar('بِضِدِّهَا تَتَبَيَّنُ الأَشْيَاءُ')))
b += B.matn(
    'بَلْ هُمُ الوَسَطُ فِي فِرَقِ الأُمَّةِ، كَمَا أَنَّ الأُمَّةَ هِيَ الوَسَطُ فِي '
    'الأُمَمِ. فَهُمْ وَسَطٌ فِي بَابِ صِفَاتِ اللهِِ سُبْحَانَهُ وَتَعَالَى بَيْنَ أَهْلِ '
    'التَّعْطِيلِ الجَهْمِيَّةِ وَأَهْلِ التَّمْثِيلِ المُشَبِّهَةِ. وَهُمْ وَسَطٌ فِي '
    'بَابِ أَفْعَالِ اللهِِ بَيْنَ الجَبْرِيَّةِ وَالقَدَرِيَّةِ وَغَيْرِهِمْ. وَفِي بَابِ '
    'وَعِيدِ اللهِِ بَيْنَ المُرْجِئَةِ وَالوَعِيدِيَّةِ مِنَ القَدَرِيَّةِ وَغَيْرِهِمْ. '
    'وَفِي بَابِ أَسْمَاءِ الإِيمَانِ وَالدِّينِ بَيْنَ الحَرُورِيَّةِ وَالمُعْتَزِلَةِ '
    'وَبَيْنَ المُرْجِئَةِ وَالجَهْمِيَّةِ. وَفِي أَصْحَابِ رَسُولِ اللهِ ﷺ بَيْنَ '
    'الرَّافِضَةِ وَالخَوَارِجِ.')
b += B.sharh(
    p('First the word. al-Fawzān quotes <em>al-Miṣbāḥ al-Munīr</em>: <strong>%s</strong>, '
      'vowelled with the fatḥah on the sīn, <em>is <strong>the balanced</strong></em>; '
      '<em>and what is intended by al-wasaṭ here is <strong>%s — the just, the choicest</strong>.</em>'
      % (ar('الوَسَط'), ar('العَدْلُ الخِيَار'))) +
    p('That is the correction of a modern misreading before it starts. <strong>%s does not mean '
      'lukewarm, or halfway, or moderate in the sense of diluted.</strong> It means <em>the best '
      'part</em> — as the centre of a thing is its choicest part. And the author did not coin the '
      'word; it is the Qurʾān\'s own description of this Ummah:' % ar('الوَسَط')))
b += B.ayah(
    'وَكَذَلِكَ جَعَلْنَاكُمْ أُمَّةً وَسَطًا لِتَكُونُوا شُهَدَاءَ عَلَى النَّاسِ',
    '"And thus We made you a middlemost community, that you may be witnesses over mankind."',
    'Sūrat al-Baqarah 2:143 · سُورَةُ البَقَرَة')
b += B.sharh(
    p('<em>So they are a middle <strong>between the sects that ascribe themselves to Islam</strong>, '
      'just as the Islamic Ummah is a middle <strong>between the nations</strong>: for this Ummah '
      'is a middle between <strong>the nations that incline to excess and immoderation</strong> '
      'and <strong>the nations that incline to negligence and laxity</strong>. And Ahl al-Sunnah '
      'wa-l-Jamāʿah, of this Ummah, are a middle between <strong>the innovating sects of the '
      'Ummah, which deviated from the straight path — some of them going to excess and becoming '
      'extreme, and some of them being lax and so deviating.</strong></em>') +
    p('Note the shape of the claim: <strong>the same pattern repeats at two scales.</strong> The '
      'Ummah among the nations, and Ahl al-Sunnah within the Ummah. And note that both kinds of '
      'deviation are named <em>deviation</em> — the lax are not merely weaker versions of the '
      'correct position; they are off the road in the other direction.'))

b += B.heading('أَوَّلًا · فِي بَابِ صِفَاتِ اللهِ', 'First — In the Chapter of Allah’s Attributes')
b += B.sharh(
    pair('١', 'بَابُ صِفَاتِ اللهِ',
         'الجَهْمِيَّة', 'the <em>muʿaṭṭilah</em>, named after <strong>الجَهْمُ بْنُ '
         'صَفْوَانَ التِّرْمِذِيّ</strong>. <em>They went to excess and were immoderate '
         '<strong>in declaring Allah free</strong> (tanzīh) until they '
         '<strong>negated His names and His attributes</strong>, in wariness of likening Him '
         '— so they claimed. And by that they were called muʿaṭṭilah, '
         '<strong>because they stripped Allah of His names and attributes.</strong></em>',
         'المُشَبِّهَة', 'the people of <em>tamthīl</em>. <em>They went to excess and were '
         'immoderate <strong>in affirming the attributes</strong> until they '
         '<strong>likened Allah to His creation and compared His attributes to '
         'theirs</strong> — تَعَالَى اللهُ عَمَّا يَقُولُونَ.</em>',
         '<em>They took the middle between the two extremes: <strong>they affirmed Allah’s '
         'attributes in the manner befitting His majesty, without likening and without '
         'comparison.</strong> So <strong>they did not go to excess in tanzīh, and they did '
         'not go to excess in affirmation</strong> — rather:</em><br>'
         '<span dir="rtl" lang="ar" style="display:inline-block;margin-top:.45rem;'
         'font-weight:700">نَزَّهُوا اللهَ بِلَا تَعْطِيلٍ، وَأَثْبَتُوا لَهُ الأَسْمَاءَ '
         'وَالصِّفَاتِ بِلَا تَمْثِيلٍ</span>') +
    p('That closing pair of clauses is the whole of Parts 1 and 2 in eleven words. '
      '<strong>Both extremes agreed on one false premise</strong> — that affirming an attribute '
      '<em>means</em> likening — and then split over what to do about it. The Jahmiyyah dropped '
      'the attribute to escape the likeness; the Mushabbihah accepted the likeness in order to '
      'keep the attribute. <strong>Ahl al-Sunnah denied the premise</strong>, which is what '
      'al-Shūrā 42:11 does in its two halves, as Lesson 5 showed.'))

b += B.heading('ثَانِيًا · فِي بَابِ أَفْعَالِ اللهِ', 'Second — In the Chapter of Allah’s Actions')
b += B.sharh(
    pair('٢', 'بَابُ أَفْعَالِ اللهِ',
         'الجَبْرِيَّة', 'named after <strong>الجَبْر</strong>, compulsion, '
         '<em>because they say <strong>the servant is compelled in his action</strong>. They went '
         'to excess in affirming Allah’s actions <strong>until they negated the actions of '
         'the servants</strong>, and claimed that they do nothing at all, but that Allah is the '
         'doer and the servant is compelled — so his movements and his actions are all '
         '<strong>involuntary, like the movements of a man with a tremor</strong>, and ascribing '
         'the action to the servant is <strong>figurative</strong>.</em>',
         'القَدَرِيَّة', 'named after <strong>القَدَر</strong>. <em>They went to excess in '
         'affirming the actions of the servants, and said: <strong>the servant creates his own '
         'action, without Allah’s will or volition</strong>; so the actions of the servants '
         '<strong>do not fall under Allah’s will and volition</strong> — Allah neither '
         'decreed them nor willed them, <strong>and they did them independently.</strong></em>',
         '<em>They took the middle, and said: <strong>the servant has choice, and volition, and '
         'an action that issues from him — but he does nothing without Allah’s will, '
         'His volition and His decree.</strong></em>') +
    p('And al-Fawzān grounds each half of that in an āyah. For the <em>deed</em>:'))
b += B.ayah(
    'وَاللَّهُ خَلَقَكُمْ وَمَا تَعْمَلُونَ',
    '"And Allah created you and what you do."',
    'Sūrat al-Ṣāffāt 37:96 · سُورَةُ الصَّافَّات')
b += B.sharh(
    p('<em>So He <strong>affirmed for the servants a deed which is of Allah\'s creating and His '
      'decreeing</strong>.</em> Read it carefully: the āyah does not say Allah created you '
      '<em>instead of</em> your deeds, nor that you do them outside His creating. '
      '<strong>It names both in one breath</strong> — which is exactly the position that neither '
      'extreme can state.') +
    p('And for the <em>volition</em>:'))
b += B.ayah(
    'وَمَا تَشَاءُونَ إِلَّا أَنْ يَشَاءَ اللَّهُ رَبُّ الْعَالَمِينَ',
    '"And you do not will, except that Allah — Lord of the worlds — wills."',
    'Sūrat al-Takwīr 81:29 · سُورَةُ التَّكْوِير')
b += B.sharh(
    p('<em>So He <strong>affirmed for the servants a volition which comes after the volition of '
      'Allah تعالى</strong>. And more clarification of this is to come إِنْ شَاءَ اللهُ in the '
      'discussion of al-qadar.</em>') +
    p('That is the precise formulation, and the word to hold is <strong>%s — after</strong>. '
      'The servant\'s will is not denied (against the Jabriyyah) and not independent (against the '
      'Qadariyyah). <strong>It is real, and it is downstream.</strong>' % ar('بَعْدَ')))

b += B.heading('ثَالِثًا · فِي بَابِ وَعِيدِ اللهِ', 'Third — In the Chapter of Allah’s Threat')
b += B.sharh(
    p('<strong>%s</strong> is <em>frightening and threatening</em>; and what is intended here is '
      '<em>the texts in which there is <strong>a threatening of the disobedient with punishment '
      'and exemplary chastisement</strong></em>.' % ar('الوَعِيد')) +
    pair('٣', 'بَابُ وَعِيدِ اللهِ',
         'المُرْجِئَة', 'from <strong>الإِرْجَاء</strong>, <em>postponement</em> — '
         '<em>they were named so because they <strong>postponed the deeds out of the definition '
         'of īmān</strong>, claiming that the one who commits a major sin is not '
         'sinful. And they said: <strong>no sin harms alongside faith, just as no obedience '
         'benefits alongside disbelief.</strong> So with them, the committer of a major sin is '
         '<strong>complete in faith and not exposed to the threat</strong> — they were lax '
         'in the ruling on the disobedient and went to excess in laxity, until they claimed that '
         '<strong>acts of disobedience do not decrease faith</strong>.</em>',
         'الوَعِيدِيَّة', '<em>those who held <strong>the carrying out of the threat</strong> '
         'upon the disobedient, and were severe in that — until they said: '
         '<strong>the committer of a major sin, if he dies without repenting, abides forever in '
         'the Fire</strong>, and they ruled that <strong>he leaves faith in this world</strong>.</em>',
         '<em>They took the middle between the two sides and said: <strong>the committer of a '
         'major sin is sinful, exposed to the threat, deficient in faith, and is ruled to be a '
         'fāsiq</strong> — not as the Murjiʾah say, that he is complete in faith '
         'and not exposed — <strong>but he does not leave faith, and does not abide forever '
         'in the Fire if he enters it.</strong> He is <strong>under the will of Allah</strong>: '
         'if He wills He pardons him, and if He wills He punishes him <em>to the measure of his '
         'sin</em>, then he comes out of the Fire and enters the Garden — not as the '
         'Waʿīdiyyah say.</em>') +
    p('And then al-Fawzān states it in a single line that is the best thing in this section, and '
      'which generalises far past this question:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.97rem;text-align:center" dir="rtl" lang="ar">'
    '<strong>فَالمُرْجِئَةُ أَخَذُوا بِنُصُوصِ الوَعْدِ، وَالوَعِيدِيَّةُ أَخَذُوا '
    'بِنُصُوصِ الوَعِيدِ، وَأَهْلُ السُّنَّةِ وَالجَمَاعَةِ جَمَعُوا بَيْنَهُمَا</strong></p>'
    '<p style="margin:.55rem 0 0;font-size:.92rem;text-align:center"><em>— the '
    'Murjiʾah took the texts of the <strong>promise</strong>; the '
    'Waʿīdiyyah took the texts of the <strong>threat</strong>; and Ahl al-Sunnah '
    'wa-l-Jamāʿah <strong>gathered the two together</strong>.</em></p></div>' +
    p('Which is the same diagnosis as the first bāb, in a different subject. '
      '<strong>Each sect is right about the half of the revelation it is holding.</strong> The '
      'error is not in what they affirmed but in what they had to discard to keep it — and '
      '<em>al-wasaṭ</em> turns out to mean <strong>the position that needs to discard '
      'nothing.</strong>'))

b += B.heading('رَابِعًا · فِي بَابِ أَسْمَاءِ الإِيمَانِ وَالدِّين',
               'Fourth — In the Chapter of the Names of Faith and Religion')
b += B.sharh(
    p('Here the author names four parties, two on each side, and al-Fawzān traces both names on '
      'the severe side to the incidents that produced them:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.89rem;margin:0 0 .9rem">'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>الحَرُورِيَّة</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">'
    '<em>they are <strong>the Khawārij</strong>, named in relation to '
    '<strong>Ḥarūrā</strong>, a village in ʿIrāq '
    '<strong>in which they gathered when they went out against ʿAlī</strong> '
    'رضي الله عنه.</em></td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>المُعْتَزِلَة</strong></td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">'
    '<em>the followers of <strong>وَاصِلُ بْنُ عَطَاءٍ</strong>, '
    '<strong>who withdrew from the gathering of al-Ḥasan al-Baṣrī</strong>, and '
    'his followers went off with him, because of a disagreement that occurred between the two of '
    'them <strong>over the ruling on the Muslim who commits a major sin</strong>. So al-Ḥasan '
    'رحمه الله said of this Wāṣil: '
    '<strong>«he has withdrawn from us»</strong> — so they were called '
    '<em>Muʿtazilah</em>, the withdrawers.</em></td></tr>'
    '</table></div>' +
    p('<em>So the madhhab of the Khawārij and the Muʿtazilah regarding the ruling on the Muslim '
      'who commits a major sin is <strong>a severe madhhab</strong>: they ruled that '
      '<strong>he leaves Islam</strong>. Then the Muʿtazilah said: <strong>he is neither a Muslim '
      'nor a disbeliever, but at %s — the station between the two stations</strong>; and the '
      'Khawārij said: <strong>he is a disbeliever</strong>. '
      '<strong>And they agreed that if he dies in that state he abides forever in the '
      'Fire.</strong></em>' % ar('المَنْزِلَةِ بَيْنَ المَنْزِلَتَيْن')) +
    p('<em>And <strong>the Murjiʾah and the Jahmiyyah stood opposite them</strong> and were lax in '
      'the ruling on him, going to excess in laxity: they said <strong>no act of disobedience '
      'harms alongside faith</strong> — <strong>because faith with them is the assent of the '
      'heart alone</strong>, or along with the utterance of the tongue (with a disagreement among '
      'them), <strong>and the deeds do not enter into it</strong>; so it does not increase by '
      'obedience nor decrease by disobedience.</em>') +
    p('That clause is the root of the whole dispute, and it is worth isolating: '
      '<strong>the question is whether deeds are part of what the word <em>īmān</em> names.</strong> '
      'Say no, and no sin can touch your faith. Say yes but make every deed essential, and one '
      'sin destroys it. <strong>Ahl al-Sunnah say the deeds are part of it and that it has '
      'degrees</strong> — which is why Lesson 28\'s small observation, that <em>afḍal al-īmān</em> '
      'implies faith admits of degrees, was load-bearing after all.') +
    p('<em>And Ahl al-Sunnah wa-l-Jamāʿah took the middle between the two groups, and said: '
      '<strong>the disobedient one does not leave faith by the mere act of disobedience</strong>, '
      'and he is under the will — if Allah wills He pardons him, and if He wills He punishes him '
      'in the Fire, <strong>but he does not abide in it forever</strong>, as the Khawārij and the '
      'Muʿtazilah say. <strong>And the acts of disobedience decrease faith</strong>, and their '
      'doer deserves to enter the Fire unless Allah pardons him; and the committer of a major sin '
      'is <strong>a fāsiq, deficient in faith</strong> — not as the Murjiʾah say, that he is '
      'complete in faith. وَاللهُ تَعَالَى أَعْلَم.</em>'))

b += B.heading('خَامِسًا · فِي أَصْحَابِ رَسُولِ اللهِ ﷺ',
               'Fifth — Regarding the Companions of the Messenger of Allah ﷺ')
b += B.sharh(
    p('And first the definition, which the student should learn exactly as given: '
      '<strong>%s</strong> — <em>the Companion is <strong>whoever met the Prophet &#65018; as a '
      'believer in him, and died upon that</strong>.</em>'
      % ar('الصَّحَابِيُّ: هُوَ مَنْ لَقِيَ النَّبِيَّ ﷺ مُؤْمِنًا بِهِ وَمَاتَ عَلَى ذَلِكَ')) +
    p('Three conditions in one line: <strong>the meeting · the faith at the meeting · and dying '
      'upon it.</strong>') +
    pair('٥', 'أَصْحَابُ رَسُولِ اللهِ ﷺ',
         'الرَّافِضَة', '<em>a name taken from <strong>الرَّفْض</strong>, which is '
         '<strong>abandoning</strong>. They were named so because they said to '
         '<strong>زَيْدِ بْنِ عَلِيِّ بْنِ الحُسَيْنِ</strong>: '
         '<strong>disown the two Shaykhs, Abū Bakr and ʿUmar</strong> — and he '
         'refused, and said: <strong>«مَعَاذَ اللهِ»</strong>, Allah forbid. '
         '<strong>So they abandoned him</strong>, and were called the Rafīḍah.</em><br>'
         '<em>Their madhhab: they <strong>went to excess regarding ʿAlī</strong> '
         'رضي الله عنه and Ahl al-Bayt and '
         'preferred them over everyone else, and <strong>set up enmity toward the rest of the '
         'Companions</strong> — especially the three caliphs Abū Bakr, ʿUmar and '
         'ʿUthmān رضي الله عنهم '
         '— and reviled them and cursed them, and <strong>may even have declared them '
         'disbelievers</strong>, or some of them.</em>',
         'الخَوَارِج', '<em>And the Khawārij stood opposite them: '
         '<strong>they declared ʿAlī</strong> '
         'رضي الله عنه '
         '<strong>a disbeliever, and with him many of the Companions</strong>, '
         '<strong>and fought them and held their blood and their wealth lawful.</strong></em>',
         '<em><strong>Ahl al-Sunnah wa-l-Jamāʿah opposed all of them</strong>: '
         'so they <strong>took all of the Companions as allies</strong>, '
         '<strong>and did not go to excess regarding any one of them</strong>, '
         'and <strong>acknowledged the excellence of all of the Companions, and that they are the '
         'best of this Ummah after its Prophet</strong> ط. And more clarification of this is '
         'to come.</em>') +
    p('Notice how exactly the two errors mirror each other, and that both are expressed as '
      '<em>loyalty</em>. One party loved ʿAlī so much that it cursed his companions; the other '
      'opposed ʿAlī so far that it killed them. <strong>And the middle position is not a lukewarm '
      'affection for everyone — it is loyalty to all of them with excess toward none</strong>, '
      'which is harder than either extreme and is the only one that leaves the generation intact.'))

b += B.heading('خُلَاصَةُ البَاب', 'The Pattern of the Five')
b += B.prose(
    'Set the five side by side and one shape repeats. In every bāb, '
    '<strong>two parties each seize one set of texts and must discard the other</strong> — the '
    'attributes against the likeness, Allah\'s acts against the servant\'s, the promise against '
    'the threat, the assent against the deeds, ʿAlī against the Companions. And in every bāb '
    '<strong>Ahl al-Sunnah hold both sets.</strong> That is what the word <em>wasaṭ</em> has meant '
    'the whole time: not a cautious middle between two bold positions, but '
    '<strong>the only position with nothing left over.</strong>')

b += B.vocab([
    ('الوَسَط', 'al-wasaṭ', 'the middlemost, the choicest',
     'Al-Miṣbāḥ: the balanced — and here, العَدْلُ الخِيَار: the just, the '
     'choicest'),
    ('التَّعْطِيل', 'al-taʿṭīl', 'stripping',
     'The Jahmiyyah — excess in tanzīh until the names and attributes were negated'),
    ('الجَبْرِيَّة', 'al-jabriyyah', 'the compulsionists',
     'The servant’s acts involuntary, like the movements of a man with a tremor'),
    ('القَدَرِيَّة', 'al-qadariyyah', 'the free-willers',
     'The servant creates his own act, outside Allah’s will'),
    ('الإِرْجَاء', 'al-irjāʾ', 'postponement',
     'The Murjiʾah postponed the DEEDS out of the definition of īmān'),
    ('الوَعِيدِيَّة', 'al-waʿīdiyyah', 'the threat-enforcers',
     'The major sinner abides forever in the Fire and leaves faith here'),
    ('المَنْزِلَةُ بَيْنَ المَنْزِلَتَيْن', 'al-manzilah bayna al-manzilatayn',
     'the station between the two stations',
     'The Muʿtazilah: neither Muslim nor disbeliever'),
    ('الحَرُورِيَّة', 'al-ḥarūriyyah', 'the Khawārij',
     'After Ḥarūrā, the ʿIrāqi village where they gathered'),
    ('الرَّافِضَة', 'al-rāfiḍah', 'the abandoners',
     'From الرَّفْض — they abandoned Zayd when he refused to disown Abū Bakr and '
     'ʿUmar'),
    ('الصَّحَابِيّ', 'al-ṣaḥābī', 'the Companion',
     'Whoever met the Prophet ط believing in him, and died upon that'),
])
b += B.mcq('ws-l30', [
    ('What does %s mean here, per al-Fawzān?' % ar('الوَسَط'),
     ['Lukewarm, halfway between two positions',
      'The balanced — and specifically %s, the just and the choicest' % ar('العَدْلُ الخِيَار'),
      'The majority', 'The latest of the generations'], 1),
    ('What false premise did the Jahmiyyah and the Mushabbihah share?',
     ['That the Qurʾān is created',
      'That affirming an attribute means likening Allah to creation — they only differed over '
      'what to do about it',
      'That the attributes are unknowable',
      'That reason precedes revelation'], 1),
    ('What did the Jabriyyah say about ascribing an action to the servant?',
     ['That it is real but incomplete',
      'That it is figurative — his movements being involuntary, like those of a man with a tremor',
      'That it is forbidden to speak of', 'That it applies only to the disobedient'], 1),
    ('What does %s establish, in al-Fawzān’s reading?'
     % ar('وَمَا تَشَاءُونَ إِلَّا أَنْ يَشَاءَ اللَّهُ'),
     ['That the servant has no volition at all',
      'That the servant has a real volition which comes <em>after</em> Allah’s volition',
      'That volition belongs to Allah alone and is ascribed to man figuratively',
      'That the servant wills independently'], 1),
    ('How does al-Fawzān summarise the dispute over the promise and the threat?',
     ['Both parties erred in reading the texts',
      'The Murjiʾah took the texts of the promise, the Waʿīdiyyah took the texts of the threat, '
      'and Ahl al-Sunnah gathered the two together',
      'The texts of the threat abrogate those of the promise',
      'The question is left to Allah without a position'], 1),
    ('Why were the Muʿtazilah so called?',
     ['Because they withdrew from the army of ʿAlī',
      'Because Wāṣil ibn ʿAṭāʾ withdrew from al-Ḥasan al-Baṣrī’s gathering over the ruling '
      'on the major sinner, and al-Ḥasan said: he has withdrawn from us',
      'Because they isolated themselves from the people in worship',
      'Because they withdrew the deeds from faith'], 1),
    ('What is the root of the dispute in the chapter of the names of faith?',
     ['Whether Allah punishes the believer at all',
      'Whether the deeds are part of what the word <em>īmān</em> names',
      'Whether repentance is accepted after death',
      'Whether the Fire has an end'], 1),
    ('What is al-Fawzān’s definition of a Companion?',
     ['Anyone who lived in the Prophet’s ﷺ lifetime',
      'Whoever met the Prophet ﷺ as a believer in him, and died upon that',
      'Anyone who narrated a ḥadīth from him ﷺ',
      'Those who made hijrah with him ﷺ'], 1),
    ('What was the position of Ahl al-Sunnah toward the Companions?',
     ['They preferred Ahl al-Bayt and withheld judgement on the rest',
      'They took all of them as allies, went to excess regarding none, and held them the best of '
      'this Ummah after its Prophet ﷺ',
      'They declared the disputes among them to be sins',
      'They refrained from speaking of them at all'], 1),
])
b += B.tf('ws-l30-tf', [
    ('المُرْجِئَةُ أَخَّرُوا الأَعْمَالَ عَنْ مُسَمَّى الإِيمَانِ.',
     'The Murjiʾah postponed the deeds out of the definition of īmān.', True),
    ('أَهْلُ السُّنَّةِ غَلَوْا فِي التَّنْزِيهِ كَالجَهْمِيَّةِ.',
     'Ahl al-Sunnah went to excess in tanzīh as the Jahmiyyah did.', False),
    ('مُرْتَكِبُ الكَبِيرَةِ عِنْدَ أَهْلِ السُّنَّةِ فَاسِقٌ نَاقِصُ الإِيمَانِ.',
     'For Ahl al-Sunnah the committer of a major sin is a fāsiq, deficient in faith.', True),
    ('الخَوَارِجُ كَفَّرُوا عَلِيًّا رَضِيَ اللهُ عَنْهُ.',
     'The Khawārij declared ʿAlī رضي الله عنه a disbeliever.', True),
])
b += B.memorize(
    'فَالمُرْجِئَةُ أَخَذُوا بِنُصُوصِ الوَعْدِ، وَالوَعِيدِيَّةُ أَخَذُوا بِنُصُوصِ '
    'الوَعِيدِ، وَأَهْلُ السُّنَّةِ وَالجَمَاعَةِ جَمَعُوا بَيْنَهُمَا',
    'Memorize it as a diagnostic tool, not only as a fact about two old sects. Nearly every '
    'deviation you will meet is a half of the revelation held tightly and the other half let go. '
    'When you hear a position that has to explain away a text, ask which half is being dropped.')
b += B.aiquiz('The standing of Ahl al-Sunnah among the sects of the Ummah in al-Aqidah '
              'al-Wasitiyyah: al-wasat as al-adl al-khiyar grounded in al-Baqarah 2:143, and the '
              'five pairs -- the Jahmiyyah and the Mushabbihah on the attributes, the Jabriyyah '
              'and the Qadariyyah on the actions with al-Saffat 37:96 and al-Takwir 81:29, the '
              'Murjiah and the Waidiyyah on the threat, the Haruriyyah and Mutazilah against the '
              'Murjiah and Jahmiyyah on the names of faith, and the Rafidah and Khawarij on the '
              'Companions')
b += B.further()
b += B.nav('was-l29-ruyah-mawqif.html', 'The Seeing, and the Position of Ahl al-Sunnah',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l30')

io.open(os.path.join(B.AQ, 'was-l30-makanah-wasat.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'مَكَانَةُ أَهْلِ السُّنَّةِ بَيْنَ فِرَقِ الأُمَّة',
    'The Standing of Ahl al-Sunnah among the Sects of the Ummah',
    'Lesson 30 of al-ʿAqīdah al-Wāsiṭiyyah, opening Part 3: '
    'al-wasaṭ as the just and the choicest, and the five chāpters in which Ahl '
    'al-Sunnah stand between two extremes — each party named, traced to its origin, and its '
    'position stated in its own terms.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الثَّلَاثُون', '3',
           'مَكَانَةُ أَهْلِ السُّنَّةِ بَيْنَ فِرَقِ الأُمَّة',
           'The Standing of Ahl al-Sunnah among the Sects of the Ummah', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l30-makanah-wasat.html')
