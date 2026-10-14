# -*- coding: utf-8 -*-
"""Wasitiyyah L23 -- Part 2, section 1: the divine descent to the lowest heaven.
The grammar, the six attributes the single hadith establishes, and al-Fawzan's
two-part refutation of reading it as the descent of His mercy or His command.
Sharh p.93."""
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
    'The ḥadīth itself is <strong>مُتَّفَقٌ عَلَيْه</strong> — agreed upon by '
    '<strong>البُخَارِيّ</strong> and <strong>مُسْلِم</strong>, which is the highest grading a '
    'ḥadīth carries.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Name the six attributes this one ḥadīth establishes.',
    'Explain the construction in %s and where you have met it before.'
    % ar('سَمَاءِ الدُّنْيَا'),
    'Give both of al-Fawzān’s grounds for rejecting “the descent of His mercy or His command”.',
    'Say why %s proves %s as well as %s.'
    % (ar('النُّزُول'), ar('العُلُوّ'), ar('صِفَاتِ الأَفْعَال')),
])

b += B.heading('١ · ثُبُوتُ النُّزُولِ الإِلَهِيِّ إِلَى سَمَاءِ الدُّنْيَا',
               'Section 1 — The Divine Descent to the Lowest Heaven')
b += B.prose(
    'The author opens Part 2 with the ḥadīth that has drawn more reinterpretation than any other '
    'text of the attributes — and he opens with it deliberately. It is '
    '<strong>مُتَّفَقٌ عَلَيْه</strong>, agreed upon by al-Bukhārī and Muslim, so the condition '
    'he set in the previous lesson is met at the highest level before the argument even begins.')
b += B.matn(
    'فَمِنْ ذَلِكَ مِثْلُ قَوْلِهِ ﷺ: «يَنْزِلُ رَبُّنَا إِلَى سَمَاءِ الدُّنْيَا كُلَّ '
    'لَيْلَةٍ حِينَ يَبْقَى ثُلُثُ اللَّيْلِ الآخِرُ، فَيَقُولُ: مَنْ يَدْعُونِي '
    'فَأَسْتَجِيبَ لَهُ؟ مَنْ يَسْأَلُنِي فَأُعْطِيَهُ؟ مَنْ يَسْتَغْفِرُنِي فَأَغْفِرَ '
    'لَهُ؟» مُتَّفَقٌ عَلَيْهِ.')
b += B.hadith(
    'يَنْزِلُ رَبُّنَا إِلَى سَمَاءِ الدُّنْيَا كُلَّ لَيْلَةٍ حِينَ يَبْقَى ثُلُثُ اللَّيْلِ '
    'الآخِرُ، فَيَقُولُ: مَنْ يَدْعُونِي فَأَسْتَجِيبَ لَهُ؟ مَنْ يَسْأَلُنِي فَأُعْطِيَهُ؟ '
    'مَنْ يَسْتَغْفِرُنِي فَأَغْفِرَ لَهُ؟',
    '"Our Lord descends to the lowest heaven every night, when the last third of the night '
    'remains, and says: who is calling upon Me, that I may answer him? Who is asking of Me, that '
    'I may give him? Who is seeking My forgiveness, that I may forgive him?"',
    'مُتَّفَقٌ عَلَيْهِ — al-Bukhārī and Muslim')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>a descent befitting His majesty</strong>. '
      'We believe in it, <strong>and we do not liken it to the descent of the created '
      'thing</strong>, because He سبحانه is</em> %s — «there is nothing like Him» '
      '(al-Shūrā 42:11).' % (ar('يَنْزِلُ رَبُّنَا'), ar('لَيْسَ كَمِثْلِهِ شَيْءٌ'))) +
    p('That is the whole method of Lesson 6 compressed into one sentence, and note its order: '
      '<strong>affirm, then refuse the likeness</strong> — not refuse the likeness by cancelling '
      'the affirmation. The āyah of al-Shūrā is doing the same work here that it did over all of '
      'Part 1.') +
    p('<strong>%s</strong> — <em>that is: <strong>%s</strong></em> — '
      '<em>of the kind where <strong>the thing described is annexed to its own '
      'description</strong></em> (%s).'
      % (ar('إِلَى سَمَاءِ الدُّنْيَا'), ar('السَّمَاءُ الدُّنْيَا'),
         ar('إِضَافَةُ المَوْصُوفِ إِلَى صِفَتِه'))) +
    p('You met this construction two lessons ago in %s — «the Spirit of Holiness», meaning '
      '<em>the purified Spirit</em>. Here it means not «the heaven <em>of</em> the world» but '
      '<strong>the lowest heaven</strong>. Reading the grammar correctly settles which heaven is '
      'meant.' % ar('رُوحُ القُدُسِ')))
b += B.sharh(
    p('Two points of vowelling, and they are not pedantry — each one carries a ruling:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>الآخِرُ</strong> — بِالرَّفْعِ</td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">a description of '
    '<span dir="rtl" lang="ar">ثُلُثُ</span>, not of <span dir="rtl" lang="ar">اللَّيْلِ</span> '
    '— “the <strong>last</strong> third”. <em>And in this is a '
    '<strong>specifying of the time of the divine descent</strong>.</em></td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>فَأَسْتَجِيبَ</strong> — بِالنَّصْبِ</td>'
    '<td style="padding:.55rem .75rem;border:1px solid var(--line)">manṣūb as '
    '<strong>the answer to the question</strong> (<span dir="rtl" lang="ar">جَوَابُ '
    'الاسْتِفْهَامِ</span>) — “that I may answer him”. Likewise '
    '<span dir="rtl" lang="ar">فَأُعْطِيَهُ</span> and '
    '<span dir="rtl" lang="ar">فَأَغْفِرَ لَهُ</span>.</td></tr>'
    '</table></div>' +
    p('The second one matters for how the ḥadīth is heard. The naṣb makes each clause '
      '<em>consequent on the asking</em>: not «I answer» as a bare statement, but '
      '<strong>«so that I may answer him»</strong>. <strong>The descent is described as being '
      '<em>for</em> the one who calls.</strong> That is why this ḥadīth lives in the chapter of '
      'duʿāʾ as much as in the chapter of attributes.'))

b += B.heading('سِتُّ صِفَاتٍ فِي حَدِيثٍ وَاحِد', 'Six Attributes in One Ḥadīth')
b += B.sharh(
    p('al-Fawzān does not stop at the descent. He counts what else the ḥadīth establishes, and '
      'the total is striking for a text of three lines:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.5rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>النُّزُول</strong></td>'
    '<td style="padding:.5rem .75rem;border:1px solid var(--line)">the descent — '
    '<strong>of the attributes of the Actions</strong></td></tr>'
    '<tr><td style="padding:.5rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>العُلُوّ</strong></td>'
    '<td style="padding:.5rem .75rem;border:1px solid var(--line)">the highness — '
    '<em>for <strong>the descending is from a height</strong></em></td></tr>'
    '<tr><td style="padding:.5rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>الكَلَام</strong></td>'
    '<td style="padding:.5rem .75rem;border:1px solid var(--line)">the speech — since there '
    'comes in it <span dir="rtl" lang="ar">فَيَقُولُ</span></td></tr>'
    '<tr><td style="padding:.5rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>الإِجَابَة</strong></td>'
    '<td style="padding:.5rem .75rem;border:1px solid var(--line)">the answering</td></tr>'
    '<tr><td style="padding:.5rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>الإِعْطَاء</strong></td>'
    '<td style="padding:.5rem .75rem;border:1px solid var(--line)">the giving</td></tr>'
    '<tr><td style="padding:.5rem .75rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>المَغْفِرَة</strong></td>'
    '<td style="padding:.5rem .75rem;border:1px solid var(--line)">the forgiving — '
    '<em>and these last three are also <strong>attributes of Actions</strong></em></td></tr>'
    '</table></div>' +
    p('And the second row is the one to keep. <strong>%s — for the descending is from a '
      'height.</strong> This is the same move as Lesson 20, where the <em>inzāl</em> of the '
      'Qurʾān proved the ʿuluww. <strong>Every text that says He comes down says, by saying it, '
      'that He is above.</strong> So the one who reinterprets this ḥadīth to escape affirming the '
      'descent has not escaped the ʿuluww; he has only moved the problem.'
      % ar('فَإِنَّ النُّزُولَ يَكُونُ مِنَ العُلُوِّ')))

b += B.heading('الرَّدُّ عَلَى مَنْ أَوَّلَ الحَدِيث', 'The Refutation of Those Who Reinterpret It')
b += B.prose(
    'The taʾwīl is well known: <em>what descends is not Allah, but <strong>His mercy</strong>, or '
    '<strong>His command</strong>, or an angel sent by Him.</em> al-Fawzān answers it on two '
    'grounds — one from the principles of language, and one from the ḥadīth\'s own words.')
b += B.sharh(
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.93rem">'
    '<p style="margin:0 0 .7rem"><strong>الأَوَّل · </strong><em>Because '
    '<strong>the default is the real meaning, and that nothing has been '
    'omitted</strong></em> (<span dir="rtl" lang="ar">الأَصْلُ الحَقِيقَةُ وَعَدَمُ '
    'الحَذْفِ</span>). To read “our Lord descends” as “our Lord’s '
    '<em>mercy</em> descends” is to insert a word that is not in the text. The one who '
    'inserts it owes a reason, and there is none here.</p>'
    '<p style="margin:0"><strong>الثَّانِي · </strong><em>And because he &#65018; said: '
    '<strong>«who is calling upon Me, that I may answer him?»</strong> — so '
    '<strong>is it conceivable that His mercy, or His command, should say this '
    'statement?!</strong></em></p></div>' +
    p('The second ground needs no technical training at all, which is why al-Fawzān puts it last '
      'and in the form of a question. <strong>Mercy does not speak.</strong> A command does not '
      'say «who is asking of Me, that I may give him». The sentence has a speaker who says '
      '<em>Me</em> and <em>I</em> four times over, and offers to answer, to give and to forgive — '
      'and none of those is something an abstraction or a messenger does on its own account.') +
    p('So the taʾwīl does not merely soften the ḥadīth; <strong>it has to cut the ḥadīth in '
      'half.</strong> It takes the first clause figuratively and then has nowhere to put the '
      'second, because whatever descended is immediately quoted speaking as the Lord. '
      '<strong>A reading that cannot survive the next line of its own proof-text is not a '
      'reading.</strong>') +
    p('And this is the discipline the author laid down in Lesson 4, meeting its first test in '
      'Part 2: <em>taḥrīf</em> was defined there as turning a text from its apparent meaning '
      'without a warrant from the Lawgiver. <strong>Here is what that looks like in '
      'practice.</strong>'))

b += B.vocab([
    ('النُّزُول', 'al-nuzūl', 'the descent',
     'Befitting His majesty — of the attributes of the Actions'),
    ('سَمَاءُ الدُّنْيَا', 'samāʾ al-dunyā', 'the lowest heaven',
     'Annexing the described to its description — as in رُوحُ القُدُسِ'),
    ('جَوَابُ الاسْتِفْهَام', 'jawāb al-istifhām', 'the answer to a question',
     'Why فَأَسْتَجِيبَ is manṣūb: “THAT I may answer him”'),
    ('الأَصْلُ الحَقِيقَة', 'al-aṣl al-ḥaqīqah',
     'the default is the real meaning',
     'With وَعَدَمُ الحَذْفِ — and that nothing has been omitted'),
    ('مُتَّفَقٌ عَلَيْه', 'muttafaq ʿalayh', 'agreed upon',
     'Reported by both al-Bukhārī and Muslim — the highest grading'),
    ('صِفَاتُ الأَفْعَال', 'ṣifāt al-afʿāl', 'attributes of the Actions',
     'Occurring by His will: the descent, the speech, the giving, the forgiving'),
])
b += B.mcq('ws-l23', [
    ('What grading does this ḥadīth carry?',
     ['Ḥasan, reported by Abū Dāwūd',
      'مُتَّفَقٌ عَلَيْه — agreed upon by al-Bukhārī and Muslim',
      'Ṣaḥīḥ by al-Albānī alone', 'Reported by Aḥmad without a grading'], 1),
    ('What construction is %s, and what does it mean?' % ar('سَمَاءِ الدُّنْيَا'),
     ['A possessive annexation: the heaven belonging to this world',
      'Annexing the described to its description — meaning <em>the lowest heaven</em>',
      'An appositive: the heaven, that is, the world',
      'A badal for the Throne'], 1),
    ('Why is %s in the nominative?' % ar('الآخِرُ'),
     ['Because it is the subject of the sentence',
      'Because it describes %s, not %s — "the LAST third", which specifies the time of the descent'
      % (ar('ثُلُثُ'), ar('اللَّيْلِ')),
      'Because it follows a preposition', 'Because it is a ḥāl'], 1),
    ('Which attribute does al-Fawzān say the descent itself proves, besides the descent?',
     ['The mercy', 'The ʿuluww — for the descending is from a height',
      'The maʿiyyah', 'The istiwāʾ'], 1),
    ('What is the first ground for rejecting "His mercy descends"?',
     ['That mercy is created and cannot descend',
      'That the default is the real meaning and that nothing has been omitted — the reinterpreter '
      'is inserting a word the text does not have',
      'That no scholar ever said it',
      'That the ḥadīth is weak in that wording'], 1),
    ('What is the second ground, from the ḥadīth’s own words?',
     ['That it says "every night", and mercy descends always',
      'That the one who descends immediately says "who is calling upon Me, that I may answer him" '
      '— and mercy or a command does not say that',
      'That it names the lowest heaven specifically',
      'That it was narrated by Abū Hurayrah'], 1),
    ('How many attributes does al-Fawzān count in this single ḥadīth?',
     ['Three', 'Six — descent, highness, speech, answering, giving and forgiving',
      'Two', 'Four'], 1),
])
b += B.tf('ws-l23-tf', [
    ('النُّزُولُ مِنْ صِفَاتِ الأَفْعَالِ.',
     'The descent is of the attributes of the Actions.', True),
    ('نُشَبِّهُ نُزُولَ اللهِ بِنُزُولِ المَخْلُوقِ.',
     'We liken Allah’s descent to the descent of the created thing.', False),
    ('الأَصْلُ فِي الكَلَامِ الحَقِيقَةُ وَعَدَمُ الحَذْفِ.',
     'The default in speech is the real meaning, and that nothing has been omitted.', True),
    ('فِي الحَدِيثِ إِثْبَاتُ الكَلَامِ لِلَّهِ تَعَالَى.',
     'The ḥadīth contains an affirmation of speech for Allah.', True),
])
b += B.memorize(
    'مَنْ يَدْعُونِي فَأَسْتَجِيبَ لَهُ؟ مَنْ يَسْأَلُنِي فَأُعْطِيَهُ؟ مَنْ يَسْتَغْفِرُنِي '
    'فَأَغْفِرَ لَهُ؟',
    'Three offers, every night, in the hour when almost nobody is awake to take them. Learn it as '
    'a creed and use it as an invitation — and notice that the clause which refutes the '
    'reinterpreters is the same clause that is calling you.')
b += B.aiquiz('The divine descent in al-Aqidah al-Wasitiyyah: the hadith muttafaq alayh, samaa '
              'al-dunya as annexing the described to its description, the rafa of al-akhir '
              'specifying the time and the nasb of fa-astajiba as the answer to a question, the '
              'six attributes the single hadith establishes, and al-Fawzan two grounds against '
              'reading it as the descent of His mercy or His command')
b += B.further()
b += B.nav('was-l22-sunnah-shart.html', 'The Sunnah and the Condition for a Ḥadīth',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l23')

io.open(os.path.join(B.AQ, 'was-l23-nuzul.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'ثُبُوتُ النُّزُولِ الإِلَهِيّ',
    'The Divine Descent to the Lowest Heaven',
    'Lesson 23 of al-ʿAqīdah al-Wāsiṭiyyah: the '
    'ḥadīth of the descent, the two points of vowelling that carry rulings, the six '
    'attributes this one ḥadīth establishes, and the two grounds on which “His '
    'mercy descends” cannot survive the ḥadīth’s own next line.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الثَّالِثُ وَالعِشْرُون', '3',
           'ثُبُوتُ النُّزُولِ الإِلَهِيّ',
           'The Divine Descent to the Lowest Heaven', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l23-nuzul.html')
