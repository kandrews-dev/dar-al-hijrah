# -*- coding: utf-8 -*-
"""Wasitiyyah L27 -- Part 2, section 6 (second half): the Throne above all
created things, and the hadith of the slave-girl -- "Where is Allah?"
Sharh pp.100-101."""
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
    'The ḥadīth of the slave-girl is reported by <strong>مُسْلِم</strong>; the ḥadīth of the '
    'Throne is graded <strong>حَسَن</strong> in the matn, reported by '
    '<strong>أَبُو دَاوُد</strong> and others.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Say what %s refers to in the ḥadīth of the Throne.' % ar('فَوْقَ ذَلِكَ'),
    'State the three things al-Fawzān derives from that ḥadīth.',
    'Give the ruling this lesson establishes about asking %s.' % ar('أَيْنَ اللهُ؟'),
    'Name the two rulings al-Fawzān draws from %s.' % ar('أَعْتِقْهَا فَإِنَّهَا مُؤْمِنَةٌ'),
])

b += B.heading('«وَالعَرْشُ فَوْقَ ذَلِكَ، وَاللهُ فَوْقَ العَرْش»',
               '"And the Throne Is above That, and Allah Is above the Throne"')
b += B.matn(
    'وَقَوْلُهُ ﷺ: «وَالعَرْشُ فَوْقَ ذَلِكَ، وَاللهُ فَوْقَ العَرْشِ، وَهُوَ يَعْلَمُ '
    'مَا أَنْتُمْ عَلَيْهِ» حَدِيثٌ حَسَنٌ رَوَاهُ أَبُو دَاوُدَ وَغَيْرُهُ.')
b += B.hadith(
    'وَالعَرْشُ فَوْقَ ذَلِكَ، وَاللهُ فَوْقَ العَرْشِ، وَهُوَ يَعْلَمُ مَا أَنْتُمْ '
    'عَلَيْهِ',
    '"And the Throne is above that, and Allah is above the Throne — and He knows what state you '
    'are in."',
    'حَدِيثٌ حَسَنٌ — graded ḥasan by the author; reported by Abū Dāwūd and others')
b += B.sharh(
    p('<strong>%s</strong> — al-Fawzān refers back: <em>the explanation of %s came '
      'before</em>, at the āyāt of the istiwāʾ. That was Lesson 16: <em>in the language it is the '
      'couch of the king; and what is intended here, as the totality of the texts indicates, is a '
      'couch having legs, borne by the angels, like a dome over the world, and it is the roof of '
      'the created things.</em>' % (ar('وَالعَرْشُ فَوْقَ ذَلِكَ'), ar('العَرْش'))) +
    p('And <strong>%s</strong> — <em>that is: <strong>above the created things which the '
      'Messenger &#65018; set out for his Companions</strong> in the ḥadīth in which he mentioned '
      'the distance between the heaven and the earth, and what is between each heaven and the '
      'next, and the thickness of each heaven, and the sea which is above the seventh heaven and '
      'what is between its lowest part and its highest, and what is above that sea of '
      '<strong>the eight mighty mountain-goats</strong>; and then above that is the Throne.</em>'
      % ar('فَوْقَ ذَلِكَ')) +
    p('The point of reciting that ladder is not the astronomy. It is that '
      '<strong>«above» in this ḥadīth is the last term of a series</strong> which the Prophet '
      '&#65018; had just laid out, rung by rung, for the people listening. Whatever is said about '
      'the particulars of each rung, <strong>the sentence is plainly locating the Throne at the '
      'top of everything created, and Allah above the Throne.</strong>'))
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>established over it with an istiwāʾ befitting '
      'His majesty</strong></em>. The same formula as Lesson 16, and the same restraint: the '
      'fact affirmed, the manner not described.' % ar('وَاللهُ فَوْقَ العَرْشِ')) +
    p('<strong>%s</strong> — <em>by <strong>His encompassing knowledge, from which nothing is '
      'hidden</strong></em>.' % ar('وَهُوَ يَعْلَمُ مَا أَنْتُمْ عَلَيْهِ')) +
    p('And that final clause is doing something the student should notice, because it is the whole '
      'answer to an objection that has not yet been raised. <strong>Someone might hear «Allah is '
      'above the Throne» and conclude that He is therefore far from us.</strong> The ḥadīth '
      'closes the door in its own last four words: <em>He is above the Throne</em> '
      '<strong>and</strong> <em>He knows what state you are in</em>. The height and the knowledge '
      'arrive in one breath — which is exactly the reconciliation Lesson 17 made for the '
      'maʿiyyah, and §7 will make again.') +
    p('<strong>And the shāhid — three things:</strong>') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.93rem">'
    '<p style="margin:0">— <strong>the affirming of Allah’s highness over His '
    'Throne</strong>; <strong>and that His Throne is above all of the created things</strong>; '
    '<strong>and that Allah’s knowledge encompasses the deeds of the servants</strong>, '
    '<em>nothing of which is hidden from Him</em>.</p></div>')

b += B.heading('حَدِيثُ الجَارِيَة · «أَيْنَ اللهُ؟»',
               'The Ḥadīth of the Slave-Girl — "Where Is Allah?"')
b += B.matn(
    'وَقَوْلُهُ ﷺ لِلْجَارِيَةِ: «أَيْنَ اللهُ؟» قَالَتْ: فِي السَّمَاءِ. قَالَ: «مَنْ '
    'أَنَا؟» قَالَتْ: أَنْتَ رَسُولُ اللهِ. قَالَ: «أَعْتِقْهَا فَإِنَّهَا مُؤْمِنَةٌ» '
    'رَوَاهُ مُسْلِمٌ.')
b += B.prose(
    'al-Fawzān gives the story in full, and it is worth having, because the creedal point is '
    'carried by an everyday incident. <em>She was <strong>the slave-girl of Muʿāwiyah ibn '
    'al-Ḥakam</strong>. Her master Muʿāwiyah became angry with her and struck her on the face. '
    '<strong>Then he regretted it</strong>, and informed the Messenger of Allah &#65018;, and '
    'said: shall I not free her? So the Prophet &#65018; said: <strong>«yes — bring her to '
    'me.»</strong> So he brought her to the Messenger of Allah &#65018;.</em>')
b += B.hadith(
    'أَيْنَ اللهُ؟ — قَالَتْ: فِي السَّمَاءِ. قَالَ: مَنْ أَنَا؟ — قَالَتْ: أَنْتَ رَسُولُ '
    'اللهِ. قَالَ: أَعْتِقْهَا فَإِنَّهَا مُؤْمِنَةٌ',
    '"Where is Allah? She said: above the heaven. He said: who am I? She said: you are the '
    'Messenger of Allah. He said: free her, for she is a believer."',
    'رَوَاهُ مُسْلِمٌ')
b += B.sharh(
    p('<strong>%s</strong> — and al-Fawzān draws the ruling straight out of the fact that the '
      'Prophet &#65018; asked it: <em>in it is <strong>a proof for the permissibility of asking '
      'about Allah with %s</strong></em>.' % (ar('أَيْنَ اللهُ؟'), ar('أَيْنَ'))) +
    p('That is a larger point than it looks. The deniers of the ʿuluww hold that <em>where?</em> '
      'is an improper question about Allah — that it presupposes a place and so presupposes a '
      'body. <strong>But the Prophet &#65018; asked it.</strong> He asked it of an uneducated '
      'slave-girl, as the test of whether she was a believer, and he accepted her one-word '
      'answer. <strong>A question the Messenger of Allah &#65018; put to a servant cannot be a '
      'question that misrepresents Allah.</strong>') +
    p('<strong>%s</strong> — <em>that is: Allah سبحانه is above the heaven</em>; and <em>the '
      'explanation of this phrase came before</em> — the previous lesson, where either reading of '
      'the %s yields the height.' % (ar('قَالَتْ: فِي السَّمَاءِ'), ar('فِي'))) +
    p('<strong>%s</strong> — <em>he asked her <strong>about her belief concerning him</strong></em>. '
      '<strong>%s</strong> — <em>so <strong>she affirmed the messengership for him</strong>.</em>'
      % (ar('قَالَ: مَنْ أَنَا؟'), ar('قَالَتْ: أَنْتَ رَسُولُ اللهِ'))) +
    p('Two questions, and between them they are the two testimonies. <strong>He examined her on '
      'the Lord she worshipped and on the Messenger she followed</strong> — and the first of the '
      'two was answered with a statement about where Allah is.'))
b += B.sharh(
    p('<strong>%s</strong> — he said this <em>to her master</em>. And al-Fawzān takes two rulings '
      'from it:' % ar('أَعْتِقْهَا فَإِنَّهَا مُؤْمِنَةٌ')) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.9rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line)">'
    '<strong>١</strong> that <strong>whoever bears this testimony is a believer</strong></td></tr>'
    '<tr><td style="padding:.55rem .75rem;border:1px solid var(--line)">'
    '<strong>٢</strong> and that <strong>the freeing (of a slave, as an expiation) has '
    'īmān as a condition for it</strong></td></tr>'
    '</table></div>' +
    p('The second is why the question was asked at all. Muʿāwiyah did not come for a theology '
      'lesson; he came to free a girl he had wronged. <strong>The Prophet &#65018; had to '
      'establish that she was a believer before the freeing would serve</strong> — and the '
      'examination he used was two questions long.') +
    p('<strong>And the shāhid from the ḥadīth: that in it is a proof for Allah\'s highness above '
      'His creation, above His heavens; and that <em>He is pointed to in the direction of height '
      'with a perceptible pointing</em></strong> (%s).'
      % ar('يُشَارُ إِلَيْهِ فِي جِهَةِ العُلُوِّ إِشَارَةً حِسِّيَّةً')) +
    p('Keep that last phrase beside Lesson 21, where the objection from %s was answered by '
      'splitting the word: <em>indwelling in creation</em> is false, <em>above creation</em> is '
      'true. <strong>Here is the true sense, confirmed by a gesture</strong> — and by the one '
      'person in the room who had never studied a book.' % ar('الجِهَة')))
b += B.prose(
    'It is worth stopping on who the witness is. Of the four texts in this section, three are '
    'words of the Prophet &#65018;. The fourth is <strong>the one-word answer of a slave-girl who '
    'was asked a question and said the first true thing</strong> — and the Messenger of Allah '
    '&#65018; pronounced her a believer on the strength of it. <strong>Whatever this doctrine is, '
    'it is not a subtlety reserved for specialists.</strong> That is the author\'s point in '
    'including her at all.')

b += B.vocab([
    ('العَرْش', 'al-ʿarsh', 'the Throne',
     'Above all the created things — and Allah above it, with an istiwāʾ '
     'befitting His majesty'),
    ('فَوْقَ ذَلِك', 'fawqa dhālik', 'above that',
     'The last term of the ladder of creation the Prophet ط had just set out'),
    ('العِلْمُ المُحِيط', 'al-ʿilm al-muḥīṭ', 'the encompassing knowledge',
     'Named in the same breath as the height — nothing is hidden from Him'),
    ('الجَارِيَة', 'al-jāriyah', 'the slave-girl',
     'The slave-girl of Muʿāwiyah ibn al-Ḥakam'),
    ('أَيْنَ اللهُ؟', 'ayna Allāh', 'where is Allah?',
     'A question the Prophet ط himself asked — so it is permitted'),
    ('العِتْق', 'al-ʿitq', 'the freeing of a slave',
     'Īmān is a condition for it — which is why he ط examined her'),
    ('إِشَارَةٌ حِسِّيَّة', 'ishārah ḥissiyyah', 'a perceptible pointing',
     'He is pointed to in the direction of height'),
])
b += B.mcq('ws-l27', [
    ('What does %s refer to in the ḥadīth of the Throne?' % ar('فَوْقَ ذَلِكَ'),
     ['Above the seventh heaven only',
      'Above the created things the Prophet ﷺ had just enumerated for his Companions — the '
      'heavens, the sea above the seventh, and the eight mighty mountain-goats',
      'Above the angels only', 'Above the Preserved Tablet'], 1),
    ('What does the ḥadīth’s closing clause %s forestall?'
     % ar('وَهُوَ يَعْلَمُ مَا أَنْتُمْ عَلَيْهِ'),
     ['The claim that Allah does not speak',
      'The conclusion that because He is above the Throne He must be far — the height and the '
      'encompassing knowledge arrive together',
      'The claim that the Throne is created',
      'The claim that the ḥadīth is weak'], 1),
    ('What ruling does al-Fawzān derive from the Prophet’s ﷺ asking %s?'
     % ar('أَيْنَ اللهُ؟'),
     ['That the question is improper and was asked only to test her',
      'That it is permissible to ask about Allah with %s' % ar('أَيْنَ'),
      'That only a prophet may ask it', 'That the answer must be given in Arabic'], 1),
    ('Why did the Prophet ﷺ examine the slave-girl at all?',
     ['To teach the Companions a lesson in creed',
      'Because īmān is a condition for the freeing to serve as an expiation',
      'Because her master doubted her', 'Because she had asked to be freed'], 1),
    ('What were the two questions, taken together?',
     ['Her lineage and her religion',
      'The two testimonies — about the Lord she worshipped, and about the Messenger she followed',
      'Her belief in the Last Day and in the decree',
      'Her prayer and her fasting'], 1),
    ('What does al-Fawzān say about the direction of height in this ḥadīth?',
     ['That it may not be spoken of at all',
      'That He is pointed to in the direction of height with a perceptible pointing',
      'That the pointing is purely figurative',
      'That the heaven here means the Throne'], 1),
    ('How does this ḥadīth bear on the objection from %s in Lesson 21?' % ar('الجِهَة'),
     ['It shows the word may never be used of Allah',
      'It confirms the true sense of the word — that He is above His creation — and confirms it '
      'by a gesture, from someone who had never studied',
      'It shows Allah is in a place like created things',
      'It has no bearing on that objection'], 1),
])
b += B.tf('ws-l27-tf', [
    ('العَرْشُ فَوْقَ المَخْلُوقَاتِ كُلِّهَا.',
     'The Throne is above all of the created things.', True),
    ('لَا يَجُوزُ السُّؤَالُ عَنِ اللهِ بِـ«أَيْنَ».',
     'It is not permissible to ask about Allah with "where".', False),
    ('العِتْقُ يُشْتَرَطُ لَهُ الإِيمَانُ.',
     'Īmān is a condition for the freeing of a slave.', True),
    ('أَقَرَّ النَّبِيُّ ﷺ الجَارِيَةَ عَلَى قَوْلِهَا «فِي السَّمَاءِ».',
     'The Prophet ﷺ approved the slave-girl’s answer "above the heaven".', True),
])
b += B.memorize(
    'وَاللهُ فَوْقَ العَرْشِ، وَهُوَ يَعْلَمُ مَا أَنْتُمْ عَلَيْهِ',
    'Learn the two clauses together and you will never need to choose between them. He is above '
    'the Throne — and He knows the state you are in right now. Neither half cancels the other, '
    'and the ḥadīth put them in one sentence so that nobody would try.')
b += B.aiquiz('The Throne above all creation and the hadith of the slave-girl in al-Aqidah '
              'al-Wasitiyyah: what fawqa dhalika refers to, how the closing clause about His '
              'encompassing knowledge forestalls the conclusion that height means distance, the '
              'permissibility of asking ayna Allah since the Prophet asked it, why iman is a '
              'condition for the freeing, and the perceptible pointing in the direction of height')
b += B.further()
b += B.nav('was-l26-uluww-sunnah.html', 'The Highness in the Sunnah — the Ruqyah of the Sick',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l27')

io.open(os.path.join(B.AQ, 'was-l27-arsh-jariyah.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'العَرْشُ فَوْقَ المَخْلُوقَاتِ · وَحَدِيثُ الجَارِيَة',
    'The Throne above Creation, and the Ḥadīth of the Slave-Girl',
    'Lesson 27 of al-ʿAqīdah al-Wāsiṭiyyah: the Throne as the last '
    'rung of the created order, why the ḥadīth joins His height to His encompassing '
    'knowledge in one sentence, and the slave-girl whose one-word answer to “where is '
    'Allah?” the Prophet ط accepted as proof of faith.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ السَّابِعُ وَالعِشْرُون', '3',
           'العَرْشُ فَوْقَ المَخْلُوقَاتِ · وَحَدِيثُ الجَارِيَة',
           'The Throne above Creation, and the Ḥadīth of the Slave-Girl', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l27-arsh-jariyah.html')
