# -*- coding: utf-8 -*-
"""Wasitiyyah L13 -- sections 10-12: the Face, the two Hands, the Eyes.
Sharh pp.50-55."""
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
    'Give the two reasons the interpretations of %s as “the Essence” or “the reward” are void.'
    % ar('الوَجْه'),
    'Give al-Fawzān’s three arguments that %s does not mean power or favour.' % ar('اليَد'),
    'Explain why the plural %s does not imply many eyes — from Arabic usage.'
    % ar('بِأَعْيُنِنَا'),
    'Define %s in the language, in its three parts.' % ar('الصَّبْر'),
])

b += B.heading('١٠ · إِثْبَاتُ الوَجْهِ لِلَّهِ سُبْحَانَه', 'Section 10 — The Face')
b += B.matn(
    'وَقَوْلُهُ: ﴿وَيَبْقَىٰ وَجْهُ رَبِّكَ ذُو الْجَلَالِ وَالْإِكْرَامِ﴾، وَقَوْلُهُ: '
    '﴿كُلُّ شَيْءٍ هَالِكٌ إِلَّا وَجْهَهُ﴾.')
b += B.ayah(
    'كُلُّ مَنْ عَلَيْهَا فَانٍ وَيَبْقَىٰ وَجْهُ رَبِّكَ ذُو الْجَلَالِ وَالْإِكْرَامِ',
    '"Everyone upon it is passing away, and there remains the Face of your Lord, Owner of '
    'Majesty and Honour."',
    'Sūrat al-Raḥmān 55:26–27 · سورة الرحمن')
b += B.sharh(
    p('al-Fawzān reads it in context: the āyah comes after %s — Allah informs us that '
      '<em>all the people of the earth will go and die, and none will remain but His noble '
      'Face</em>; for the Lord does not die, rather He is the Living who never dies.'
      % ar('كُلُّ مَنْ عَلَيْهَا فَانٍ')) +
    p('<strong>%s</strong> is greatness and grandeur. <strong>%s</strong> — the One who honours '
      'His prophets and His righteous servants; and it is also said: the One who <em>deserves to '
      'be held above</em> everything that does not befit Him.'
      % (ar('ذُو الجَلَالِ'), ar('وَالإِكْرَام'))))
b += B.ayah(
    'كُلُّ شَيْءٍ هَالِكٌ إِلَّا وَجْهَهُ',
    '"Everything will perish except His Face."',
    'Sūrat al-Qaṣaṣ 28:88 · سورة القصص')
b += B.sharh(
    p('<strong>The shāhid:</strong> both āyāt affirm the Face for Allah, and it is of '
      '<strong>%s</strong> — His attributes of Essence. It is a real face, befitting His majesty, '
      '%s — <em>not</em> as the deniers of the attributes claim, that the Face is not real and '
      'that what is meant is the Essence, or the reward, or a direction.'
      % (ar('صِفَاتِهِ الذَّاتِيَّة'), ar('لَيْسَ كَمِثْلِهِ شَيْءٌ'))) +
    p('And al-Fawzān says those interpretations are void <strong>on more than one ground</strong>. '
      'Two he states:') +
    '<ol style="margin:0 0 .7rem;padding-right:1.3rem;line-height:2.1">'
    '<li><strong>The Face is mentioned alongside the Essence</strong> — and a thing is not '
    'joined to itself. If “Face” simply meant “Essence,” the wording would be '
    'saying nothing twice.</li>'
    '<li><strong>No nation’s language works that way.</strong> <em>It is not known in the '
    'language of any people on earth that “the face of a thing” means its essence, or '
    'its reward.</em> The interpretation is not a reading of Arabic; it is a replacement for '
    'it.</li>'
    '</ol>' +
    p('And he gives the word\'s actual meaning: %s in the language is <strong>the front of '
      'anything</strong> — <em>because it is the first part of it that one faces</em> — and in '
      'each thing it is according to what it is annexed to. A man\'s face, a house\'s face, a '
      'garment\'s face: in every case the front, in the manner suited to that thing.'
      % ar('الوَجْه')))

b += B.heading('١١ · إِثْبَاتُ اليَدَيْنِ لِلَّهِ تَعَالَى', 'Section 11 — The Two Hands')
b += B.matn(
    'وَقَوْلُهُ: ﴿مَا مَنَعَكَ أَنْ تَسْجُدَ لِمَا خَلَقْتُ بِيَدَيَّ﴾، وَقَوْلُهُ: ﴿وَقَالَتِ '
    'الْيَهُودُ يَدُ اللَّهِ مَغْلُولَةٌ غُلَّتْ أَيْدِيهِمْ وَلُعِنُوا بِمَا قَالُوا بَلْ '
    'يَدَاهُ مَبْسُوطَتَانِ يُنْفِقُ كَيْفَ يَشَاءُ﴾.')
b += B.ayah(
    'مَا مَنَعَكَ أَنْ تَسْجُدَ لِمَا خَلَقْتُ بِيَدَيَّ',
    '"What prevented you from prostrating to what I created with My two Hands?"',
    'Sūrat Ṣād 38:75 · سورة ص')
b += B.sharh(
    p('The address is to Iblīs, when he refused to prostrate to Ādam عَلَيْهِ السَّلَامُ: '
      '<em>what thing turned you away and held you back from prostrating?</em> And %s means '
      '<strong>I undertook his creation with My Hands, without any intermediary</strong> — '
      '<em>and in this is an ennobling and honouring of Ādam.</em>'
      % ar('لِمَا خَلَقْتُ بِيَدَيَّ')))
b += B.ayah(
    'وَقَالَتِ الْيَهُودُ يَدُ اللَّهِ مَغْلُولَةٌ غُلَّتْ أَيْدِيهِمْ وَلُعِنُوا بِمَا قَالُوا '
    'بَلْ يَدَاهُ مَبْسُوطَتَانِ يُنْفِقُ كَيْفَ يَشَاءُ',
    '"And the Jews said: Allah\'s hand is tied. Their hands are tied, and they are cursed for '
    'what they said. Rather, His two Hands are outstretched; He gives as He wills."',
    'Sūrat al-Māʾidah 5:64 · سورة المائدة')
b += B.sharh(
    p('al-Fawzān explains what they meant and what they did not: by %s they described Him as '
      '<strong>miserly</strong> — as they also described Him as poor while they were rich — '
      '<em>not that they meant His hand was literally bound.</em> And %s is Allah\'s reply, '
      'meeting them with the very thing they said, matching them for what they fabricated. '
      '<em>And so it came to pass for them</em> — for among them is a great deal of miserliness '
      'and envy.' % (ar('يَدُ اللهِ مَغْلُولَةٌ'), ar('غُلَّتْ أَيْدِيهِمْ'))))
b += B.sharh(
    p('<strong>The shāhid:</strong> the āyāt affirm <em>two real Hands, befitting His majesty and '
      'greatness, not like the hands of the creature</em> — %s. And in this is the refutation of '
      'whoever negated the two real Hands and claimed that what is meant by “hand” is '
      '<strong>power</strong> or <strong>favour</strong>. al-Fawzān calls that '
      '<em>a void interpretation and a distortion of the Noble Qurʾān</em> — and then gives '
      'three arguments. The first is the one to remember:' % ar('لَيْسَ كَمِثْلِهِ شَيْءٌ')) +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0 0 .5rem;font-size:.93rem"><strong>1. It would destroy the honour being '
    'given to Ādam.</strong> If “Hand” meant <em>power</em>, then singling Ādam '
    'out as created by them is pointless — because <strong>every</strong> creature, '
    '<em>including Iblīs himself</em>, was created by His power. What distinction over Iblīs '
    'would Ādam then have?</p>'
    '<p style="margin:0;font-size:.93rem">— and <strong>Iblīs could have answered back: '
    '“and You created me with Your hands too!”</strong> The rebuke in the āyah only '
    'works because the Hands are real and particular.</p></div>' +
    '<ol start="2" style="margin:0 0 .7rem;padding-right:1.3rem;line-height:2.1">'
    '<li>If “hand” meant power, <strong>Allah would have to have two powers</strong> '
    '— and the Muslims are agreed that this is false.</li>'
    '<li>If it meant favour, the meaning would be that <strong>He created Ādam with two '
    'favours</strong> — also false, because Allah’s favours are beyond counting, not '
    'two.</li>'
    '</ol>' +
    p('Three arguments, and none of them appeals to anything but the text and plain reasoning. '
      'That is how this book handles the attributes throughout.'))

b += B.heading('١٢ · إِثْبَاتُ العَيْنَيْنِ لِلَّهِ تَعَالَى', 'Section 12 — The Eyes')
b += B.matn(
    'وَقَوْلُهُ: ﴿وَاصْبِرْ لِحُكْمِ رَبِّكَ فَإِنَّكَ بِأَعْيُنِنَا﴾، وَقَوْلُهُ: '
    '﴿تَجْرِي بِأَعْيُنِنَا جَزَاءً لِمَنْ كَانَ كُفِرَ﴾، وَقَوْلُهُ: ﴿وَأَلْقَيْتُ عَلَيْكَ '
    'مَحَبَّةً مِنِّي وَلِتُصْنَعَ عَلَىٰ عَيْنِي﴾.')
b += B.ayah(
    'وَاصْبِرْ لِحُكْمِ رَبِّكَ فَإِنَّكَ بِأَعْيُنِنَا',
    '"And be patient for the decree of your Lord — for you are before Our Eyes."',
    'Sūrat al-Ṭūr 52:48 · سورة الطور')
b += B.sharh(
    p('Before the attribute, al-Fawzān defines the command. <strong>%s</strong> in the language '
      'is <em>restraining and withholding</em>. And he divides it into three, which is worth '
      'carrying well beyond this lesson:' % ar('الصَّبْر')) +
    '<ul style="margin:0 0 .7rem;padding-right:1.2rem;line-height:2">'
    '<li>restraining <strong>the soul</strong> from anguish;</li>'
    '<li>restraining <strong>the tongue</strong> from complaining and from discontent;</li>'
    '<li>restraining <strong>the limbs</strong> from striking the cheeks and tearing the '
    'garments.</li>'
    '</ul>' +
    p('So patience is not a feeling one waits to arrive. It is three refusals, and a man can '
      'perform all three while his heart is breaking.') +
    p('<strong>%s</strong> means His decree, both universal and legislated. And <strong>%s</strong> '
      'means <em>in Our sight, seen by Us</em> — which is precisely why the patience is '
      'commanded. The one being wronged is being watched.'
      % (ar('لِحُكْمِ رَبِّكَ'), ar('فَإِنَّكَ بِأَعْيُنِنَا'))))
b += B.ayah(
    'تَجْرِي بِأَعْيُنِنَا جَزَاءً لِمَنْ كَانَ كُفِرَ',
    '"…sailing before Our Eyes — a reward for the one who had been denied."',
    'Sūrat al-Qamar 54:14 · سورة القمر')
b += B.sharh(
    p('Of Nūḥ\'s ship, carried %s — <em>a vessel of broad planks, and nails by which those planks '
      'were bound</em> (the singular of %s being %s). It sailed <strong>in Our sight and view, '
      'and under Our protection</strong>. And %s means: what We did with Nūḥ and his people, of '
      'saving him and drowning them, was <em>a recompense for the one who had been denied</em> — '
      'and that is Nūḥ عَلَيْهِ السَّلَامُ.'
      % (ar('عَلَىٰ ذَاتِ أَلْوَاحٍ وَدُسُرٍ'), ar('دُسُر'), ar('دِسَار'),
         ar('جَزَاءً لِمَنْ كَانَ كُفِرَ'))))
b += B.ayah(
    'وَأَلْقَيْتُ عَلَيْكَ مَحَبَّةً مِنِّي وَلِتُصْنَعَ عَلَىٰ عَيْنِي',
    '"And I cast upon you love from Me, and so that you would be brought up before My Eye."',
    'Sūrat Ṭā Hā 20:39 · سورة طه')
b += B.heading('«بِأَعْيُنِنَا» وَ«عَلَى عَيْنِي»: مَسْأَلَةٌ فِي اللُّغَة',
               'A Question of Arabic Usage')
b += B.sharh(
    p('A student reading these three āyāt side by side will notice something: one says %s '
      '(plural), another says %s (singular). Does the Qurʾān affirm many eyes? One eye?'
      % (ar('بِأَعْيُنِنَا'), ar('عَلَىٰ عَيْنِي'))) +
    p('al-Fawzān settles it from Arabic usage, and begins by ruling out the wrong answer: '
      '<strong>what is meant is not the affirming of a single eye, for that would be an evident '
      'defect — Allah is far above it.</strong>') +
    p('Then the rule: <strong>the Arabs make an annexed noun singular, dual or plural according '
      'to the state of what it is annexed to.</strong>') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.88rem;margin:0 0 .7rem">'
    '<tr style="background:var(--brand-wash)">'
    '<th style="padding:.5rem .6rem;text-align:left;border:1px solid var(--line)">Annexed to…</th>'
    '<th style="padding:.5rem .6rem;text-align:left;border:1px solid var(--line)">The noun becomes</th>'
    '<th style="padding:.5rem .6rem;text-align:left;border:1px solid var(--line)">Example</th></tr>'
    '<tr><td style="padding:.5rem .6rem;border:1px solid var(--line)">a singular</td>'
    '<td style="padding:.5rem .6rem;border:1px solid var(--line)">singular</td>'
    '<td style="padding:.5rem .6rem;border:1px solid var(--line)">'
    '<span dir="rtl" lang="ar">عَلَىٰ عَيْنِي</span></td></tr>'
    '<tr><td style="padding:.5rem .6rem;border:1px solid var(--line)">a plural (stated or as a '
    'pronoun)</td>'
    '<td style="padding:.5rem .6rem;border:1px solid var(--line)">better made plural, to match '
    'the wording</td>'
    '<td style="padding:.5rem .6rem;border:1px solid var(--line)">'
    '<span dir="rtl" lang="ar">فَإِنَّكَ بِأَعْيُنِنَا</span></td></tr>'
    '<tr><td style="padding:.5rem .6rem;border:1px solid var(--line)">a <strong>dual</strong></td>'
    '<td style="padding:.5rem .6rem;border:1px solid var(--line)">most eloquently made '
    '<strong>plural</strong></td>'
    '<td style="padding:.5rem .6rem;border:1px solid var(--line)">'
    '<span dir="rtl" lang="ar">فَقَدْ صَغَتْ قُلُوبُكُمَا</span> — and there are only '
    '<strong>two</strong> hearts</td></tr>'
    '</table></div>' +
    p('That third row is the proof, and it is decisive. Allah says to two people <em>“your '
      '<strong>hearts</strong> have inclined”</em> — plural — when between two people there are '
      'exactly two hearts. Nobody reading it imagines a crowd of hearts. The plural is the '
      'eloquent form when annexed to a dual, and that is all it is.') +
    p('So, al-Fawzān concludes: <strong>the hearer is not confused by a speaker saying “We see '
      'you with Our eyes” or “We seize you with Our hands” — and not one human being on the face '
      'of the earth understands from it many eyes on a single face.</strong>') +
    p('Which is the method of this whole book applied to a grammar question: the text is left '
      'standing, the Arabic is read as Arabic, and the imagined difficulty turns out to have been '
      'imported rather than found.'))

b += B.vocab([
    ('الوَجْه', 'al-wajh', 'the Face',
     'In the language: the front of a thing, the first part one faces'),
    ('ذُو الجَلَال', 'dhū al-jalāl', 'Owner of Majesty', 'Greatness and grandeur'),
    ('الإِكْرَام', 'al-ikrām', 'Honour',
     'He honours His prophets and righteous — and deserves to be held above all unfitting'),
    ('مَغْلُولَة', 'maghlūlah', 'tied, bound',
     'What the Jews said of His hand — meaning miserly, not literally bound'),
    ('صِفَاتٌ ذَاتِيَّة', 'ṣifāt dhātiyyah', 'attributes of Essence',
     'Such as the Face — distinct from the attributes of action'),
    ('دِسَار', 'disār', 'a nail',
     'Plural دُسُر — the nails binding the planks of Nūḥ’s ship'),
    ('الصَّبْر', 'al-ṣabr', 'patience',
     'Restraining the soul, the tongue, and the limbs — three refusals'),
])
b += B.mcq('ws-l13', [
    ('Why is it void to say %s means “the Essence”?' % ar('الوَجْه'),
     ['Because the scholars forbade it',
      'Because the Face is mentioned alongside the Essence — a thing is not joined to itself — '
      'and because no nation’s language makes “the face of a thing” mean its essence',
      'Because the word appears only once', 'Because it is a Madīnan āyah'], 1),
    ('What does %s mean in the language?' % ar('الوَجْه'),
     ['Honour and rank', 'The front of a thing — the first part of it one faces',
      'A direction of prayer', 'The reward of a deed'], 1),
    ('al-Fawzān’s first argument against "hand = power" is —',
     ['That the word is singular in some āyāt',
      'That it would destroy the honour given to Ādam, since every creature including Iblīs was '
      'created by His power — and Iblīs could have answered that he too was made by His hands',
      'That the Arabs never used the word that way',
      'That the Jews said it first'], 1),
    ('If "hand" meant power, what would follow that the Muslims agree is false?',
     ['That Allah has no power at all', 'That Allah would have two powers',
      'That power is created', 'That Ādam had power'], 1),
    ('Why does %s not imply many eyes?' % ar('بِأَعْيُنِنَا'),
     ['Because it is figurative',
      'Because the Arabs make an annexed noun plural to match a plural or dual — as in “your '
      'hearts have inclined,” said of two people with two hearts',
      'Because the plural here means singular',
      'Because the āyah is about the angels'], 1),
    ('What are the three parts of %s in the language?' % ar('الصَّبْر'),
     ['Prayer, fasting and charity',
      'Restraining the soul from anguish, the tongue from complaint, and the limbs from striking '
      'the cheeks and tearing the garments',
      'Knowledge, action and teaching', 'Hope, fear and love'], 1),
    ('What does %s indicate about Ādam?' % ar('لِمَا خَلَقْتُ بِيَدَيَّ'),
     ['That he was created last',
      'That Allah undertook his creation with His Hands without intermediary — an ennobling of '
      'Ādam',
      'That he was created from clay', 'That he was taught the names'], 1),
])
b += B.tf('ws-l13-tf', [
    ('الوَجْهُ مِنْ صِفَاتِ اللهِ الذَّاتِيَّةِ.',
     'The Face is among Allah’s attributes of Essence.', True),
    ('المُرَادُ بِاليَدِ القُدْرَةُ أَوِ النِّعْمَةُ.',
     'What is meant by "hand" is power or favour.', False),
    ('﴿فَقَدْ صَغَتْ قُلُوبُكُمَا﴾ وَإِنَّمَا هُمَا قَلْبَانِ.',
     '"Your hearts have inclined" is said though there are only two hearts.', True),
    ('اليَهُودُ أَرَادُوا أَنَّ يَدَ اللهِ مُوثَقَةٌ حَقِيقَةً.',
     'The Jews meant that Allah’s hand was literally bound.', False),
])
b += B.memorize(
    'كُلُّ مَنْ عَلَيْهَا فَانٍ ۝ وَيَبْقَىٰ وَجْهُ رَبِّكَ ذُو الْجَلَالِ وَالْإِكْرَامِ',
    'Two āyahs that put every attachment in its place. Everyone on the earth is passing — and '
    'the only thing that remains is the One whose Face this is. Recite it when the world feels '
    'permanent.')
b += B.aiquiz('The Face, the two Hands and the Eyes in al-Aqidah al-Wasitiyyah: why interpreting '
              'the Face as the Essence or the reward is void, al-Fawzans three arguments that '
              'hand does not mean power or favour including the Iblis objection, and the Arabic '
              'usage that explains biaayunina alongside ala ayni')
b += B.further()
b += B.nav('was-l12-rahmah-ghadab-maji.html', 'Mercy, Anger, and His Coming',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l13')

io.open(os.path.join(B.AQ, 'was-l13-wajh-yadayn-aynayn.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'الوَجْهُ وَاليَدَانِ وَالعَيْنَان', 'The Face, the Two Hands, and the Eyes',
    'Lesson 13 of al-ʿAqīdah al-Wāsiṭiyyah: why reading the Face as the '
    'Essence or the reward is void, al-Fawzān’s three arguments that “hand” '
    'does not mean power or favour — including that Iblīs could have answered back — '
    'and the Arabic usage that explains bi-aʿyuninā beside ʿalā ʿaynī.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الثَّالِثَ عَشَر', '3',
           'الوَجْهُ وَاليَدَانِ وَالعَيْنَان', 'The Face, the Two Hands, and the Eyes', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l13-wajh-yadayn-aynayn.html')
