# -*- coding: utf-8 -*-
"""مُرَاجَعَةُ المَتْن -- the end-of-text review for al-Aqidah al-Wasitiyyah.

Not an exam. The traditional check on a matn is that the student recites it
back and the shaykh sees whether the meanings are held, so this walks the
matn's own seven parts in order and asks for them. Each item hides its answer
under a native <details>, which keeps the recall active without a timer or a
score -- and a score is worth nothing to a lone student in any case, since
nobody is collecting it.

Every item links to the lesson it comes from, so a missed one sends the student
to the right page rather than to a mark out of 35.
"""
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

N = [0]


def item(q, ans, href, label):
    """One review item: the prompt, then the answer behind a toggle."""
    N[0] += 1
    return (
        '<details style="border:1px solid var(--ivory-dark);border-radius:var(--radius-md);'
        'background:white;padding:var(--space-md) var(--space-lg);margin:0 0 .7rem">\n'
        '  <summary style="cursor:pointer;font-size:.95rem;color:var(--ink);'
        'line-height:1.8;font-weight:600;list-style:none">'
        '<span style="color:var(--ink-faint);font-weight:400;font-size:.8rem;'
        'margin-left:.4rem">%d</span> %s</summary>\n'
        '  <div style="font-size:.92rem;color:var(--ink-mid);line-height:1.9;'
        'margin-top:.8rem;padding-top:.8rem;border-top:1px solid var(--line)">%s\n'
        '    <p style="margin:.75rem 0 0;font-size:.78rem">'
        '<a href="%s" style="color:var(--teal-deep);font-weight:600">%s →</a></p>\n'
        '  </div>\n</details>\n' % (N[0], q, ans, href, label))


def part(ar, en, pages):
    return (
        '<div style="margin:var(--space-xl) 0 var(--space-md);padding-bottom:.6rem;'
        'border-bottom:2px solid var(--brand)">\n'
        '  <p style="font-family:var(--font-arabic);font-size:1.25rem;direction:rtl;'
        'color:var(--teal-deep);font-weight:700;margin:0 0 2px">%s</p>\n'
        '  <p style="font-size:.86rem;font-weight:600;color:var(--ink-mid);margin:0">%s'
        '<span style="color:var(--ink-faint);font-weight:400"> · %s</span></p>\n'
        '</div>\n' % (ar, en, pages))


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = ''

b += ('<div style="background:var(--brand-wash);border:1px solid var(--brand);'
      'border-radius:var(--radius-lg);padding:var(--space-lg);'
      'margin-bottom:var(--space-lg)">\n'
      '<p style="font-size:.93rem;color:var(--ink-mid);line-height:1.9;margin:0">'
      'Read the question, answer it <strong>from memory and out loud</strong>, and only '
      'then open the answer. An item you cannot answer is not a mark lost — it is a '
      'lesson to go back to, and each one carries its link.</p>\n'
      '<p style="font-size:.88rem;color:var(--ink-light);line-height:1.85;'
      'margin:.7rem 0 0">This is not a test and nothing is recorded. It is the check '
      'a student makes on himself before he says he has read a matn: '
      '<span dir="rtl" lang="ar">هَلْ تَحْفَظُ المَعَانِيَ أَمْ قَرَأْتَ '
      'فَحَسْب؟</span> — <em>do you hold the meanings, or did you merely read?</em></p>\n'
      '</div>\n')

# ------------------------------------------------------------------- Part 1
b += part('الجُزْءُ الأَوَّل · الأَدِلَّةُ مِنَ القُرْآن',
          'Part 1 — The Evidence from the Qurʾān', 'Lessons 7–21')
b += item(
    'Which āyah is the دُسْتُور of this whole subject, and what does each half of it '
    'refute?',
    '<p style="margin:0"><strong>al-Shūrā 42:11</strong> — %s. <strong>The first half '
    'refutes the %s</strong>, who liken Allah to His creation; <strong>the second half '
    'refutes the %s</strong>, who strip Him of His attributes. The āyah affirms and '
    'negates in one breath, which is the method of the entire matn.</p>'
    % (ar('لَيْسَ كَمِثْلِهِ شَيْءٌ وَهُوَ السَّمِيعُ البَصِيرُ'),
       ar('مُمَثِّلَة'), ar('مُعَطِّلَة')),
    'was-l05-mawqif-ilhad.html', 'Lesson 5')
b += item(
    'Name the four doors the author closes, and state the relation between the first '
    'two.',
    '<p style="margin:0 0 .5rem">%s · %s · %s · %s.</p>'
    '<p style="margin:0"><strong>Every %s is also a %s, but not the reverse</strong> — '
    'a man who twists the wording has thereby stripped the attribute, while a man may '
    'strip the attribute without touching the wording at all.</p>'
    % (ar('التَّحْرِيف'), ar('التَّعْطِيل'), ar('التَّكْيِيف'), ar('التَّمْثِيل'),
       ar('مُحَرِّف'), ar('مُعَطِّل')),
    'was-l04-manhaj-sifat.html', 'Lesson 4')
b += item(
    'Why does Sūrat al-Ikhlāṣ equal a third of the Qurʾān?',
    '<p style="margin:0">Because <strong>the meanings of the Qurʾān are three</strong> — '
    '%s, %s and %s — <strong>and this sūrah is tawḥīd alone</strong>. It is also named '
    'al-Ikhlāṣ for two reasons: it is purely about Allah\'s attributes, and '
    '<strong>it frees the one who recites it from shirk</strong>.</p>'
    % (ar('تَوْحِيد'), ar('قَصَص'), ar('أَحْكَام')),
    'was-l07-ikhlas.html', 'Lesson 7')
b += item(
    'Why are %s the greatest of the names?' % ar('الحَيُّ القَيُّوم'),
    '<p style="margin:0">Because <strong>%s points to the attributes of the '
    '<em>Essence</em> and %s to the attributes of the <em>Actions</em> — so every '
    'attribute returns to these two.</strong> That is why Āyat al-Kursī, which opens '
    'with them, is the greatest āyah.</p>' % (ar('الحَيّ'), ar('القَيُّوم')),
    'was-l08-ayat-al-kursi.html', 'Lesson 8')
b += item(
    'Give the proof of %s in its two steps.' % ar('التَّمَانُع'),
    '<p style="margin:0"><strong>Two gods means division</strong> — each would take away '
    'what he created. <strong>Division means contention</strong> — each would seek to '
    'overcome the other. <strong>And a loser is no god.</strong> So the premise destroys '
    'itself.</p>',
    'was-l15-nafy-sharik-tamanu.html', 'Lesson 15')
b += item(
    'Give the grounds for refusing to read %s as %s.'
    % (ar('اسْتَوَى'), ar('اسْتَوْلَى')),
    '<p style="margin:0 0 .5rem">The seven āyāt use <strong>one unvarying wording</strong>; '
    'the four Arabic senses of %s <strong>are all senses of height</strong>; the reading '
    'is not reported from any of the salaf; and — the sharpest of them — '
    '<strong>the particle %s</strong>.</p>'
    '<p style="margin:0"><em>«Then He rose over the Throne»</em> places the rising '
    '<strong>after</strong> the creation; but the Throne already stood fifty thousand '
    'years before. <strong>If %s meant «took control», He would have been out of control '
    'of it until then</strong> — which no one says.</p>'
    % (ar('اسْتَوَى'), ar('ثُمَّ'), ar('اسْتَوَى')),
    'was-l16-istiwa-uluww.html', 'Lesson 16')
b += item(
    'What is the one rule that separates the Qurʾān\'s negations from the '
    '%s\'s?' % ar('مُعَطِّلَة'),
    '<p style="margin:0"><strong>What the Qurʾān negates is deficiencies, never '
    'perfections</strong> — and every negation it makes carries an affirmation inside it. '
    'It says He does not sleep, which affirms the perfection of His life; it never says '
    'He does not hear. The %s negate perfections, which is the opposite '
    'operation.</p>' % ar('مُعَطِّلَة'),
    'was-l06-nafy-ithbat.html', 'Lesson 6')
b += item(
    'How are the two objections to the ruʾyah answered — %s, and %s?'
    % (ar('لَنْ تَرَانِي'), ar('لَا تُدْرِكُهُ الأَبْصَار')),
    '<p style="margin:0 0 .5rem"><strong>%s is a statement about this world\'s '
    'capacity</strong>, not about the next; the same Mūsā is granted it in the Hereafter, '
    'and the mountain crumbling shows the matter was one of capacity.</p>'
    '<p style="margin:0"><strong>%s negates <em>encompassing</em>, not seeing</strong> — '
    'and a thing cannot be said to be un-encompassed unless it is first seen. '
    '<strong>So the objection presupposes what it denies.</strong> And note the two '
    'words: %s with the %s is <em>radiant</em>; %s with the %s is <em>looking</em>.</p>'
    % (ar('لَنْ تَرَانِي'), ar('الإِدْرَاك'), ar('نَاضِرَة'), ar('ضَاد'),
       ar('نَاظِرَة'), ar('ظَاء')),
    'was-l21-ruyah.html', 'Lesson 21')

# ------------------------------------------------------------------- Part 2
b += part('الجُزْءُ الثَّانِي · الأَدِلَّةُ مِنَ السُّنَّة',
          'Part 2 — The Evidence from the Sunnah', 'Lessons 22–29')
b += item(
    'Give the five conditions of a %s ḥadīth.' % ar('صَحِيح'),
    '<p style="margin:0"><strong>١</strong> an unbroken chain · <strong>٢</strong> the '
    'uprightness of every narrator · <strong>٣</strong> the precision of every narrator · '
    '<strong>٤</strong> freedom from %s, irregularity · <strong>٥</strong> freedom from '
    '%s, a hidden defect. <em>This is the muṣṭalaḥ arriving exactly where the matn needs '
    'it — the author is about to argue from ḥadīth, so the standard comes '
    'first.</em></p>' % (ar('الشُّذُوذ'), ar('العِلَّة')),
    'was-l22-sunnah-shart.html', 'Lesson 22')
b += item(
    'On what two grounds is %s read in its real sense?' % ar('النُّزُول'),
    '<p style="margin:0"><strong>%s</strong> — the default is the real meaning, and that '
    'nothing has been elided. To read «our Lord descends» as «His command descends» is to '
    'claim a deletion the speaker did not make; and <strong>the one who is most truthful '
    'and most able to express himself said what he meant.</strong></p>'
    % ar('الأَصْلُ الحَقِيقَةُ وَعَدَمُ الحَذْف'),
    'was-l23-nuzul.html', 'Lesson 23')

# ------------------------------------------------------------------- Part 3
b += part('الجُزْءُ الثَّالِث · الوَاجِبَاتُ وَمَكَانَةُ أَهْلِ السُّنَّة',
          'Part 3 — The Obligations, and the Standing of Ahl al-Sunnah',
          'Lessons 30–35')
b += item(
    'Why can the ʿuluww and the maʿiyyah both be affirmed without contradiction?',
    '<p style="margin:0"><strong>%s</strong> — <em>because all of it is true, and the '
    'true does not contradict itself.</em> He is above His Throne in reality and with His '
    'creation in reality, and the second does not mean mixture. al-Mujādilah 58:7 '
    '<strong>opens and seals with knowledge</strong>, so the verse interprets itself.</p>'
    % ar('لِأَنَّ الكُلَّ حَقٌّ، وَالحَقُّ لَا يَتَنَاقَض'),
    'was-l31-wujub-istiwa-maiyyah.html', 'Lesson 31')
b += item(
    'What is the difference between %s and %s?' % (ar('التَّحْرِيف'), ar('الصِّيَانَة')),
    '<p style="margin:0"><strong>Both claim to protect the text; only one of them reads '
    'it.</strong> %s is turning the wording from its meaning after having understood it. '
    '%s is guarding the text by taking it as it came. The muʿaṭṭil believes he is '
    'honouring Allah by denying the attribute — which is why the error is sincere and '
    'still an error.</p>' % (ar('التَّحْرِيف'), ar('الصِّيَانَة')),
    'was-l30-makanah-wasat.html', 'Lesson 30')

# ------------------------------------------------------------------- Part 4
b += part('الجُزْءُ الرَّابِع · اليَوْمُ الآخِر',
          'Part 4 — The Last Day', 'Lessons 36–41')
b += item(
    'What kind of thing is the %s, precisely?' % ar('الحِسَاب'),
    '<p style="margin:0">For the believer it is <strong>an acquainting, not an '
    'investigation</strong> — Allah makes him know his sins and then forgives them. '
    'The one <em>argued with</em> in the reckoning is destroyed; the believer is '
    '<strong>shown</strong>, not cross-examined.</p>',
    'was-l38-dawawin-hisab.html', 'Lesson 38')
b += item(
    'What is %s derived from, and what does the derivation teach?' % ar('الشَّفَاعَة'),
    '<p style="margin:0">From <strong>%s, the even number</strong> — the intercessor '
    '<em>makes the one person into a pair</em>, joining himself to him. Hence the two '
    'conditions on every accepted intercession: <strong>%s</strong> — Allah\'s permission '
    'for the intercessor, and His being pleased with the one interceded for.</p>'
    % (ar('الشَّفْع'), ar('الإِذْنُ وَالرِّضَا')),
    'was-l40-shafaat.html', 'Lesson 40')
b += item(
    'State the asymmetry between the Garden and the Fire.',
    '<p style="margin:0"><strong>The Garden is entered by His mercy; the Fire is not '
    'entered until the proof has been established against a man.</strong> Nobody is '
    'punished for what no messenger reached him with — and nobody earns the Garden by '
    'his deeds alone, not even the Prophet ﷺ, as he himself said.</p>',
    'was-l41-ikhraj-bi-la-shafaah.html', 'Lesson 41')

# ------------------------------------------------------------------- Part 5
b += part('الجُزْءُ الخَامِس · الإِيمَانُ بِالقَدَر',
          'Part 5 — Belief in the Decree', 'Lessons 42–44')
b += item(
    'Give the four %s of qadar, and the two degrees they fall into.'
    % ar('مَرَاتِب'),
    '<p style="margin:0 0 .5rem"><strong>%s · %s · %s · %s</strong> — knowledge, '
    'writing, will, and creating.</p>'
    '<p style="margin:0">The <strong>first degree</strong> is the knowledge and the '
    'writing; the <strong>second</strong> is the will and the creating. '
    '<em>Whoever affirms all four has affirmed the decree as Ahl al-Sunnah affirm '
    'it.</em></p>'
    % (ar('العِلْم'), ar('الكِتَابَة'), ar('المَشِيئَة'), ar('الخَلْق')),
    'was-l42-qadar-ilm-kitabah.html', 'Lesson 42')
b += item(
    'al-Anʿām 6:148 reports the mushrikūn arguing from the decree. Every premise they '
    'use is true. Where exactly does the argument fail?',
    '<p style="margin:0">It is true that Allah willed it; true that nothing occurs '
    'against His will. <strong>The fallacy is using the decree, which is hidden, to '
    'answer the Sharīʿah, which is revealed.</strong> The decree is not a proof against a '
    'command, because no man knows it until after he has acted — '
    '<strong>and nobody accepts the argument when he is himself the one wronged.</strong></p>',
    'was-l43-mashiah-khalq.html', 'Lesson 43')
b += item(
    'The matn ascribes «%s» to the Prophet ﷺ. What does al-Fawzān do with that, and why?'
    % ar('مَجُوسُ هَذِهِ الأُمَّة'),
    '<p style="margin:0"><strong>He corrects the matn.</strong> It is not established as '
    'a statement of the Prophet ﷺ, <strong>because the Qadariyyah arose after his '
    'time</strong>. The censure is therefore <strong>%s</strong> — stopping at the '
    'Companions. <em>Worth holding onto as a habit of mind: a sharḥ that corrects its own '
    'matn is doing what a sharḥ is for.</em></p>' % ar('مَوْقُوفٌ عَلَى الصَّحَابَة'),
    'was-l44-afal-al-ibad.html', 'Lesson 44')

# ------------------------------------------------------------------- Part 6
b += part('الجُزْءُ السَّادِس · الإِيمَانُ وَالصَّحَابَة',
          'Part 6 — Īmān, and the Companions', 'Lessons 45–49')
b += item(
    'Define īmān as Ahl al-Sunnah define it, and distinguish %s from %s.'
    % (ar('الإِيمَانُ المُطْلَق'), ar('مُطْلَقُ الإِيمَان')),
    '<p style="margin:0 0 .5rem"><strong>%s</strong> — statement with the tongue, belief '
    'in the heart, and action with the limbs; it increases with obedience and decreases '
    'with disobedience.</p>'
    '<p style="margin:0">The two phrases differ <strong>only in word order</strong>, and '
    'everything turns on it. <strong>%s</strong> is the <em>complete</em> īmān, which the '
    'sinner loses. <strong>%s</strong> is the <em>bare minimum</em> of it, which he keeps '
    '— which is why he is a believer by his faith, sinful by his major sin, and not '
    'declared a disbeliever.</p>'
    % (ar('قَوْلٌ بِاللِّسَانِ وَاعْتِقَادٌ بِالقَلْبِ وَعَمَلٌ بِالجَوَارِح'),
       ar('الإِيمَانُ المُطْلَق'), ar('مُطْلَقُ الإِيمَان')),
    'was-l45-haqiqat-al-iman.html', 'Lesson 45')
b += item(
    'Who are %s, and what qualification does al-Fawzān attach to allying with them?'
    % ar('أَهْلُ البَيْت'),
    '<p style="margin:0"><strong>%s and %s</strong> — those upon whom the ṣadaqah is '
    'forbidden — <strong>and his wives and daughters</strong>. The qualification: '
    '<em>one who opposes the Sunnah and does not stand upright upon the religion is '
    '<strong>not</strong></em> taken as an ally. <strong>Kinship to the Prophet ﷺ is a '
    'real and honoured right; it is not an immunity</strong> — and that one clause '
    'separates this creed from the Rāfiḍah on one side and the Nawāṣib on the other.</p>'
    % (ar('بَنُو هَاشِم'), ar('بَنُو عَبْدِ المُطَّلِب')),
    'was-l48-ahl-al-bayt-wa-al-azwaj.html', 'Lesson 48')
b += item(
    'In what respect are the wives «Mothers of the Believers» — and in what respect are '
    'they not?',
    '<p style="margin:0">Mothers <strong>in reverence, and in the forbiddance of marrying '
    'them</strong>. <strong>NOT</strong> in the remaining rulings: regarding seclusion and '
    'looking, <strong>their ruling is the ruling of unrelated women</strong>. '
    '<em>Motherhood here is a legal status, not a biological fiction</em> — the Qurʾān '
    'calls them mothers in one āyah and commands the believers to address them from '
    'behind a screen in another.</p>',
    'was-l48-ahl-al-bayt-wa-al-azwaj.html', 'Lesson 48')
b += item(
    'Give the four excuses for the narrations of the Companions\' faults, in order — and '
    'the rule under the second.',
    '<p style="margin:0 0 .5rem"><strong>١</strong> some is <strong>a lie</strong>, and a '
    'lie gets no attention · <strong>٢</strong> some is <strong>distorted</strong>, added '
    'to and altered · <strong>٣</strong> what is authentic, <strong>they are excused in '
    'it</strong>: mujtahids right or mujtahids mistaken · <strong>٤</strong> they were '
    '<strong>never claimed to be sinless</strong> in the first place.</p>'
    '<p style="margin:0">The rule under the second is the transferable one: '
    '<strong>%s</strong> — <em>the excellence of the Companions is KNOWN and their '
    'integrity CERTAIN, so the known and certain is not abandoned for a distorted matter '
    'that is doubted.</em> <strong>A certainty is not surrendered to a doubt.</strong></p>'
    % ar('لَا يُتْرَكُ المَعْلُومُ المُتَيَقَّنُ لِأَمْرٍ مُحَرَّفٍ مَشْكُوكٍ فِيه'),
    'was-l49-ma-shajara-bayna-al-sahabah.html', 'Lesson 49')
b += item(
    'Why does the ḥadīth of the judge settle the question of what passed between the '
    'Companions?',
    '<p style="margin:0"><em>«When the judge exerts himself and is correct he has two '
    'rewards; and when he exerts himself and errs he has one»</em> — '
    '<strong>al-Bukhārī and Muslim</strong>. <strong>On neither branch is there sin.</strong> '
    'So what issued from a Companion is either ijtihād — rewarded, and the error forgiven '
    '— or not ijtihād, and he has of precedence and merit what effaces it. '
    '<strong>There is no third case, and neither leaves anything for a later man to '
    'prosecute.</strong></p>',
    'was-l49-ma-shajara-bayna-al-sahabah.html', 'Lesson 49')

# ------------------------------------------------------------------- Part 7
b += part('الجُزْءُ السَّابِع · الكَرَامَاتُ وَصِفَاتُ أَهْلِ السُّنَّة',
          'Part 7 — The Karāmāt, and the Qualities of Ahl al-Sunnah',
          'Lessons 50–54')
b += item(
    'Who is a %s — and where is the word defined?' % ar('وَلِيّ'),
    '<p style="margin:0"><strong>%s</strong>, the believer who has taqwā. And the '
    'definition is <strong>given by Allah, not assembled by the scholars</strong>: Yūnus '
    '10:62 names «the awliyāʾ of Allah» and <strong>the very next āyah says who they '
    'are</strong> — <em>those who believed and used to have taqwā.</em> The word itself '
    'is from <strong>%s — love and nearness</strong>, so <strong>wilāyah is earned by '
    'obedience and by nothing else</strong>: not by a lineage, a robe, a chain or a '
    'tomb.</p>' % (ar('المُؤْمِنُ المُتَّقِي'), ar('الوَلَاء')),
    'was-l50-karamat-al-awliya.html', 'Lesson 50')
b += item(
    'Why can a wonder never, by itself, be proof in a man\'s favour?',
    '<p style="margin:0">Because of <strong>%s</strong>. Even granting that something '
    'genuinely happened, <strong>a real event may be granted precisely in order to draw a '
    'man on by degrees until he is seized.</strong> So the question to put to any reported '
    'marvel is not <em>«did it happen?»</em> but <em>«is this man, by the Qurʾān\'s own '
    'definition, a believer with taqwā?»</em> <strong>Ask about the man, not about the '
    'marvel.</strong></p>' % ar('الاسْتِدْرَاج'),
    'was-l50-karamat-al-awliya.html', 'Lesson 50')
b += item(
    'What does «following his ﷺ %s» mean — and what does it deliberately NOT mean?'
    % ar('آثَار'),
    '<p style="margin:0"><strong>His Sunnah</strong> — what is narrated of a saying, a '
    'deed or an approval. <strong>NOT his physical traces</strong>, the places where he '
    'sat and slept: <em>because pursuing that is a cause of falling into shirk, as '
    'happened in the nations before.</em> The Arabic %s carries both senses, and '
    'al-Fawzān affirms the first and warns against the second in the same breath.</p>'
    % ar('أَثَر'),
    'was-l51-sifat-ahl-al-sunnah.html', 'Lesson 51')
b += item(
    'Answer the saying: «the way of the salaf is safer, but the way of the khalaf is more '
    'learned and more judicious.»',
    '<p style="margin:0"><strong>%s</strong> — safer <em>and</em> more learned <em>and</em> '
    'more judicious. The saying concedes safety and takes knowledge away, which is a way '
    'of honouring the salaf out of the argument. <strong>The men who watched the '
    'revelation descend, heard its interpretation, and received from the Messenger ﷺ with '
    'no intermediary were not merely more cautious. They knew more</strong> — and a '
    'safety bought by ignorance would be no safety at all.</p>'
    % ar('أَسْلَمُ وَأَعْلَمُ وَأَحْكَم'),
    'was-l51-sifat-ahl-al-sunnah.html', 'Lesson 51')
b += item(
    'Define %s in both registers — and say what makes a novelty one.' % ar('البِدْعَة'),
    '<p style="margin:0"><strong>%s</strong> what has no prior precedent; <strong>%s</strong> '
    'what no Sharīʿah evidence has indicated. <strong>The two conditions together are the '
    'whole definition: introduced AND ascribed to the religion.</strong> That is why the '
    'Sharīʿah sense is narrower — a new tool or a new way of recording a text has no prior '
    'precedent and is no innovation, because nobody ascribes it to the religion. '
    '<em>The ascription is what makes the novelty a bidʿah.</em></p>'
    % (ar('لُغَةً'), ar('شَرْعًا')),
    'was-l51-sifat-ahl-al-sunnah.html', 'Lesson 51')
b += item(
    'What exactly is %s, and which ijmāʿ can be relied on?' % ar('الجَمَاعَة'),
    '<p style="margin:0 0 .5rem"><strong>%s — those gathered upon the truth.</strong> Not '
    '«the majority», and not whoever happens to be assembled: the āyah commands holding to '
    'the rope of Allah and forbids division in one sentence, so <strong>the gathering is a '
    'consequence of holding to revelation, not an alternative to it.</strong></p>'
    '<p style="margin:0">And <strong>%s</strong> is that of the righteous salaf — they '
    'were few and gathered in the Ḥijāz, so their view could be known. After them the '
    'disagreement multiplied and the Ummah spread, so <strong>a claim of ijmāʿ is only as '
    'good as the possibility of having checked.</strong></p>'
    % (ar('المُجْتَمِعُونَ عَلَى الحَقّ'), ar('الإِجْمَاعُ الَّذِي يَنْضَبِط')),
    'was-l51-sifat-ahl-al-sunnah.html', 'Lesson 51')
b += item(
    'Why does the author list only three foundations and leave out %s?' % ar('القِيَاس'),
    '<p style="margin:0"><strong>Because qiyās is disputed, and a book of creed carries '
    'only what is agreed.</strong> The disputed is left to the discipline that handles '
    'dispute, the books of uṣūl. <em>That is why the Wāsiṭiyyah is short, and why nothing '
    'in it has needed to be withdrawn.</em></p>',
    'was-l51-sifat-ahl-al-sunnah.html', 'Lesson 51')
b += item(
    'On what two grounds do Ahl al-Sunnah hold the Ḥajj, the Jumuʿah and the ʿĪds with '
    'the rulers, <em>«righteous or corrupt»</em>?',
    '<p style="margin:0 0 .5rem">First note the author\'s own qualification: '
    '<strong>a corruption that does not take them out of the religion.</strong> The ruling '
    'is about a sinful Muslim ruler and addresses nothing else.</p>'
    '<p style="margin:0"><strong>١</strong> the Muslims\' purpose is <strong>the gathering '
    'of the word and distance from division</strong>; <strong>٢</strong> a corrupt ruler '
    '<strong>is not deposed by his corruption</strong>, and rebellion brings the loss of '
    'rights and the spilling of blood. Ibn Taymiyyah: <em>«hardly a party is known to have '
    'rebelled against a holder of authority but that in its rebellion there was more '
    'corruption than in what it removed.»</em></p>',
    'was-l52-mukammilat-al-aqidah.html', 'Lesson 52')
b += item(
    'Give the three holdings-back that make up %s, and define %s.'
    % (ar('الصَّبْر'), ar('الشُّكْر')),
    '<p style="margin:0 0 .5rem">%s is <strong>%s — holding back</strong>: of '
    '<strong>the soul from anguish</strong>, <strong>the tongue from complaint and '
    'discontent</strong>, and <strong>the limbs from striking the cheeks and tearing the '
    'garments</strong>.</p>'
    '<p style="margin:0">%s is <strong>the servant\'s expending of what Allah favoured him '
    'with in obedience to Him</strong>. <em>Note the symmetry: ṣabr is defined entirely by '
    'restraint and shukr entirely by expenditure</em> — so gratitude is not a warm feeling '
    'about a blessing but <strong>the use the blessing is put to</strong>.</p>'
    % (ar('الصَّبْر'), ar('الحَبْس'), ar('الشُّكْر')),
    'was-l52-mukammilat-al-aqidah.html', 'Lesson 52')
b += item(
    'What two things does «%s» establish about īmān itself?'
    % ar('أَكْمَلُ المُؤْمِنِينَ إِيمَانًا أَحْسَنُهُمْ خُلُقًا'),
    '<p style="margin:0"><strong>That deeds enter into the name of īmān</strong>, and '
    '<strong>that īmān admits of degrees.</strong> «The most complete in īmān» presupposes '
    'degrees of completeness, and what raises a man through them here is '
    '<em>character</em> — a deed of the limbs and the tongue. <strong>So the doctrinal '
    'claim of Part 6 and the ethical claim of Part 7 are one claim</strong>, which is why '
    'a book on the attributes of Allah ends with manners.</p>',
    'was-l53-makarim-al-akhlaq.html', 'Lesson 53')
b += item(
    'How can %s be forbidden «%s» — with a right?'
    % (ar('الاسْتِطَالَة'), ar('بِحَقٍّ أَوْ بِغَيْرِ حَقّ')),
    '<p style="margin:0">Because the overbearing man <strong>with</strong> a right '
    '<strong>has boasted</strong> — %s — and <strong>without</strong> a right '
    '<strong>has transgressed</strong> — %s — <strong>and both were already forbidden by '
    'name in the same sentence.</strong> Having a right changes what you are owed; '
    '<em>it does not license contempt for the person who owes it.</em></p>'
    % (ar('فَقَدِ افْتَخَرَ'), ar('فَقَدْ بَغَى')),
    'was-l53-makarim-al-akhlaq.html', 'Lesson 53')
b += item(
    'How is the saved sect identified — and what does the identification NOT require?',
    '<p style="margin:0 0 .5rem">By <strong>a historical test, not by a claim</strong>: '
    '<em>whoever is upon the like of what I am upon <strong>today</strong>, and my '
    'Companions.</em> The standard is a state of affairs that existed at a datable moment '
    'in front of named men — <strong>so «which group?» becomes a question about evidence '
    'rather than self-description</strong>, which every sect could supply.</p>'
    '<p style="margin:0"><strong>It does not require that the seventy-three be '
    'enumerated.</strong> Once the saved group is fixed by what it is <em>upon</em>, '
    'counting the others is of no use to a man deciding where to stand.</p>',
    'was-l54-khatimah.html', 'Lesson 54')
b += item(
    'The author closes with two requests. What are they — and what is notable about the '
    'second?',
    '<p style="margin:0 0 .5rem"><strong>%s</strong> — <em>that He make us of them, and '
    'that He not turn our hearts aside after He has guided us.</em></p>'
    '<p style="margin:0">After establishing the attributes, the Last Day, the Decree, the '
    'Companions and the manners of the saved group, <strong>he asks neither for more '
    'knowledge nor for victory. He asks to be allowed to keep what he has</strong> — '
    'in the wording of Āl ʿImrān 3:8. <em>Because the hearts that turn aside are hearts '
    'that had been guided</em>, which is the one danger a book like this cannot protect '
    'its reader from.</p>'
    % ar('أَنْ يَجْعَلَنَا مِنْهُمْ، وَأَنْ لَا يُزِيغَ قُلُوبَنَا بَعْدَ إِذْ هَدَانَا'),
    'was-l54-khatimah.html', 'Lesson 54')

b += ('<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
      'border-radius:var(--radius-sm);padding:var(--space-lg);margin:var(--space-xl) 0 0">\n'
      '<p style="font-family:var(--font-arabic);font-size:1.1rem;direction:rtl;'
      'color:var(--teal-deep);font-weight:700;margin:0 0 .5rem;text-align:center">'
      'وَأَنْ لَا يُزِيغَ قُلُوبَنَا بَعْدَ إِذْ هَدَانَا</p>\n'
      '<p style="font-size:.9rem;color:var(--ink-mid);line-height:1.85;margin:0;'
      'text-align:center">The matn ends on a request, not a claim. '
      '<strong>Whatever of these %d you could answer, the author of the book you have '
      'just read did not think knowing it was the same as keeping it.</strong></p>\n'
      '</div>\n' % N[0])

b += B.nav('was-l54-khatimah.html', 'The Conclusion of the Treatise',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-murajaah')

io.open(os.path.join(B.AQ, 'wasitiyyah-murajaah.html'), 'w',
        encoding='utf-8', newline='\n').write(B.shell(
    'مُرَاجَعَةُ المَتْن',
    'What You Should Now Know',
    'The end-of-text review for al-ʿAqīdah al-Wāsiṭiyyah: %d prompts walking the matn’s '
    'seven parts in order, each with its answer under a tap-to-reveal and a link back to '
    'the lesson it comes from. Not an exam — the check a student makes on himself before '
    'he says he has read a matn.' % N[0],
    B.card('الوَاسِطِيَّة · المُرَاجَعَة', '6',
           'مُرَاجَعَةُ المَتْن',
           'What You Should Now Know — a review of the whole text', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote wasitiyyah-murajaah.html with %d items' % N[0])
