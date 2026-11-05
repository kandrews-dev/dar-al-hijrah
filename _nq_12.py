# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 12 — النَّاقِضُ السَّابِع, part 2: حُكْمُ السَّاحِر.

Printed folios 166-179 (PDF indices 163-176, offset +3). Part 3 takes 179-193.

This is the ruling half, and two things make it worth a lesson of its own.

**First: the ruling is NOT flat, and Ibn Bāz says so himself.** The famous
answer is «الصَّوَابُ فِي السَّاحِر: أَنَّهُ كَافِر، وَأَنَّهُ يُقْتَل»,
with two grounds — his kufr, and his being of the مُفْسِدِين (and he reasons
from the muḥārib: «وَالسَّاحِرُ فَوْقَ ذَلِكَ وَأَشَرُّ مِنْ ذَلِك»). But
then he is pressed on al-Shāfiʿī's view and answers **«فِيهِ التَّفْصِيل: قَدْ
يَكُونُ كُفْرًا فِي ذَاتِه، وَقَدْ يَكُونُ لِمَا يَتَرَتَّبُ عَلَيْهِ مِنَ
الفَسَاد»** — and grants the questioner that the Shāfiʿī distinction is
«الصَّحِيحُ مِنْ حَيْثُ المَعْنَى إِذَا عُرِف»; **the أصل remains kufr unless
it is established by trustworthy means** that his craft involves no worship of
the jinn.

**Second: the ḥadīth everyone quotes for the ḥadd is graded ḍaʿīf here, by
seven named scholars including Ibn Bāz.** «حَدُّ السَّاحِرِ ضَرْبُهُ
بِالسَّيْف» — al-Bukhārī: «هَذَا لَا شَيْء»; al-Tirmidhī: the correct is
mawqūf; al-Dhahabī, Ibn Ḥajar, Ibn Ḥazm, Ibn Rajab; and **Ibn Bāz: «وَالأَحَادِيثُ
المَرْفُوعَةُ فِيهَا ضَعْف، وَالرَّاجِحُ وَقْفُهُ عَلَى جُنْدُبٍ
الخَيْر».** What *does* carry the ruling is the athar of ʿUmar — chain
authenticated, and Ibn Qudāmah: «وَهَذَا اشْتُهِرَ وَلَمْ يُنْكَرْ فَكَانَ
إِجْمَاعًا» — with the precision that **al-Bukhārī narrates the kernel abridged
WITHOUT the command to kill the sorceresses**.

Also here: repentance (refused from the one seized, accepted from the one who
comes of his own accord — al-Shūrā 42:25), the woman magician and the
reconciliation of ʿĀʾishah's selling her slave girl, why the Prophet ﷺ did not
kill Labīd (four answers, none asserted), acting **without** the ruler's
permission («مَحَلُّ اجْتِهَاد», then the qāʿidah), قَلْبُ الأَعْيَان against
al-Rāzī — **where the compiler also rejects one of the arguments made on his
own side** («وَفِي هَذَا الإِلْزَامِ الأَخِيرِ نَظَر») — the Dūmat al-Jandal
athar weakened, the flying magician, and the ʿarrāf material with its textual
criticism of «فَصَدَّقَه».

Rule 8 inventory for this page:
  * «حَدُّ السَّاحِرِ ضَرْبُهُ بِالسَّيْف» — **ḍaʿīf**, seven named gradings.
  * «تَعَلَّمُوا السِّحْرَ وَلَا تَعْمَلُوا بِه» — Ibn Bāz: **بَاطِلٌ لَا
    أَصْلَ لَه**.
  * أَثَرُ عُمَر — «إِسْنَادُهُ صَحِيح», the compiler's own grading, with Ibn
    Ḥazm named.
  * «مَنْ أَتَى عَرَّافًا…» — Ibn Bāz places it in **Ṣaḥīḥ Muslim**; reported
    as he gives it. And his **textual** judgement that «فَصَدَّقَه» in some
    copies of Kitāb al-Tawḥīd is a copyist's addition, «غَيْرُ مَحْفُوظ».
  * «التَّوْبَةُ تَهْدِمُ مَا كَانَ قَبْلَهَا», «لَا تَأْتُوهُم»،
    «لَيْسُوا بِشَيْء», «فَقَدْ كَفَرَ بِمَا أُنْزِلَ عَلَى مُحَمَّد», and
    «إِنْ كَانَ فِي أُمَّتِي مُحَدَّثُونَ فَعُمَر» — quoted here with no
    grading, so the page says so and supplies none.
"""
import io, os, importlib.util

spec = importlib.util.spec_from_file_location('nq', os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '_nqbuild.py'))
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


def box(inner, wash='var(--brand-wash)', edge='var(--brand)'):
    return ('<div style="background:%s;border-right:4px solid %s;'
            'border-radius:var(--radius-sm);padding:var(--space-md);'
            'margin:0 0 .8rem">%s</div>' % (wash, edge, inner))


def row(k, v):
    return ('<tr><td style="padding:.62rem .8rem;border:1px solid var(--line);'
            'white-space:nowrap;vertical-align:top"><strong>%s</strong></td>'
            '<td style="padding:.62rem .8rem;border:1px solid var(--line)">%s</td></tr>'
            % (k, v))


def row3(a, b_, c):
    return ('<tr><td style="padding:.62rem .8rem;border:1px solid var(--line);'
            'vertical-align:top">%s</td>'
            '<td style="padding:.62rem .8rem;border:1px solid var(--line);'
            'vertical-align:top">%s</td>'
            '<td style="padding:.62rem .8rem;border:1px solid var(--line);'
            'vertical-align:top">%s</td></tr>' % (a, b_, c))


def thead3(a, b_, c):
    cell = ('<th style="padding:.5rem .8rem;border:1px solid var(--line);'
            'text-align:left;font-size:.76rem;letter-spacing:.05em;'
            'text-transform:uppercase;color:var(--ink-light)">%s</th>')
    return '<tr>' + (cell % a) + (cell % b_) + (cell % c) + '</tr>'


def table(rows, fs='.91rem'):
    return ('<div style="overflow-x:auto"><table style="width:100%%;'
            'border-collapse:collapse;font-size:%s;margin:0 0 .75rem">%s</table></div>'
            % (fs, ''.join(rows)))


def qa(q, a):
    return ('<div style="margin:0 0 .6rem;padding-right:.8rem;'
            'border-right:2px solid var(--line)">'
            '<p style="margin:0 0 .25rem;font-size:.88rem;color:var(--ink-light)">'
            '<strong>Q —</strong> <em>%s</em></p>'
            '<p style="margin:0;font-size:.93rem"><strong>Ibn Bāz —</strong> %s</p>'
            '</div>' % (q, a))


b = B.objectives([
    'Give the <strong>two grounds</strong> on which Ibn Bāz holds the magician '
    'is killed, and the comparison he reasons from.',
    'State the %s he grants on al-Shāfiʿī’s view — and what remains the %s.'
    % (ar('تَفْصِيل'), ar('أَصْل')),
    'Say whether the magician is killed <strong>as a ḥadd or as a '
    'disbeliever</strong>, and what follows for washing, shrouding, the prayer '
    'and burial.',
    'State when the magician’s repentance is <strong>refused</strong> and when '
    'it is <strong>accepted</strong> — and the one fact the whole answer turns '
    'on.',
    'Give the grading of %s and name at least three of the scholars who gave '
    'it.' % ('«' + ar('حَدُّ السَّاحِرِ ضَرْبُهُ بِالسَّيْف') + '»'),
    'Say what <em>does</em> carry the ruling, how its chain is graded, and the '
    'one precision about al-Bukhārī’s wording.',
    'State the rule on <strong>acting without the ruler’s permission</strong>, '
    'and what Ibn Bāz nevertheless said of Jundub.',
    'Refute %s — and give the argument the compiler <strong>rejects</strong> on '
    'his own side.' % ar('قَلْبُ الأَعْيَان'),
])

b += B.provenance(166, 179)

b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><strong>Part 1 established '
        'what siḥr is. These folios rule on the man.</strong> And two things '
        'here are not what the clause’s reputation suggests.</p>'
        '<p style="margin:0;font-size:.93rem"><strong>One:</strong> Ibn Bāz '
        'states the ruling at its strongest and then, pressed, says '
        '<em>«فِيهِ التَّفْصِيل»</em> — there is a distinction in it — and '
        'grants that al-Shāfiʿī’s position is <em>«الصَّحِيحُ مِنْ حَيْثُ '
        'المَعْنَى إِذَا عُرِف»</em>.<br>'
        '<strong>Two:</strong> <em>the one ḥadīth everybody quotes for the ḥadd '
        'of the magician is graded weak on these very folios — by seven named '
        'scholars, Ibn Bāz among them.</em> What actually carries the ruling is '
        'something else, and the page shows which.</p>',
        wash='var(--accent-wash)', edge='var(--accent)'))

# ---------------------------------------------------------------- the ruling
b += B.heading('قَتْلُ السَّاحِر', 'The Ruling, and Its Two Grounds')
b += B.sharh(
    box('<p style="margin:0;font-size:.95rem"><em>«<strong>The correct position '
        'regarding the magician is that he is a disbeliever, and that he is '
        'killed</strong> — because he does not practise magic except by way of '
        '<strong>worship of the devils</strong>, worship of the jinn and drawing '
        'near to them by what they love; and when he has drawn near to them by '
        'what they love, they teach him things by which he bewitches people and '
        'terrifies people and bewitches their eyes. '
        '<strong>So for this his killing became obligatory, for two '
        'reasons:</strong></em></p>'))
b += B.sharh(table([
    row('الأَوَّل',
        '<em>«<strong>his disbelief, and his misguidance, and his apostasy '
        '— if he was a Muslim</strong>»</em>'),
    row('الثَّانِي',
        '<em>«because he is <strong>of the people of corruption</strong>, of '
        'those who spread corruption in the earth; and whoever is of the people '
        'of corruption, it is obligatory to <strong>relieve the people of his '
        'evil</strong>»</em>'),
]) + p('And the second ground he argues by comparison, from the verse on '
       'killing a soul — <em>«except for a soul, or for corruption in the '
       'earth»</em>:') +
    box('<p style="margin:0;font-size:.93rem"><em>«And for this the killing of '
        '<strong>the highway robbers</strong> became obligatory when the '
        'interest requires their killing — and Allah gave a choice in that, so '
        'if the one in authority sees that killing them is more beneficial than '
        'crucifying them and amputating, he kills them, <strong>to protect the '
        'people from their evil</strong>. <strong>And the magician is above that '
        'and worse than that</strong> — because he practises worship of other '
        'than Allah; he practises shirk… so for this the majority of the people '
        'of knowledge held that he is killed.»</em></p>'))
b += B.ayah(
    'مَن قَتَلَ نَفْسًا بِغَيْرِ نَفْسٍ أَوْ فَسَادٍ فِي الْأَرْضِ',
    '…whoever kills a soul, other than for a soul or for corruption in the '
    'earth…',
    'سُورَةُ المَائِدَة · 5:32')
b += B.prose(
    '<em>Keep the structure of the two grounds, because they do different '
    'work.</em> The first is about <strong>what he has become</strong> — an '
    'apostate. The second is about <strong>what he does to others</strong> — '
    'and it is a public-order ground, reasoned from the muḥārib, and therefore '
    '<em>belongs to the one in authority by its very form</em>. '
    '<strong>Neither ground is available to a private person; the second one '
    'explicitly names the ruler making a judgement of interest.</strong>')

# ---------------------------------------------------------------- the tafsil
b += B.heading('فِيهِ التَّفْصِيل', 'Then He Is Pressed, and Distinguishes')
b += B.prose(
    'Having stated it that strongly, he states al-Shāfiʿī’s position himself — '
    '<em>and does not dismiss it.</em>')
b += B.sharh(
    box('<p style="margin:0;font-size:.93rem"><em>«As for his disbelief and his '
        'misguidance — what is known with the people of knowledge is that he is '
        'a disbeliever, for the noble verse. <strong>But al-Shāfiʿī — may Allah '
        'have mercy on him — and a group said: his magic is examined.</strong> '
        'So if his magic is of what is practised with <strong>potions and '
        'fumigation, without drawing near to the jinn and without worship of the '
        'jinn</strong> — then this one is <strong>disciplined, or killed</strong>, '
        'upon the disagreement in that. But if his magic is of what is practised '
        'with <strong>worship of the jinn and drawing near to them</strong> — '
        'then this one is a <strong>disbeliever</strong>; '
        '<strong>and this meaning ought not to be a place of '
        'disagreement</strong>.»</em></p>'))
b += B.sharh(
    qa('On al-Shāfiʿī’s view it emerges that <strong>magic is not disbelief in '
       'itself</strong>, but by what attaches to the deed?',
       '<em>«<strong>According to the deed of the one doing it.</strong>»</em>') +
    qa('And that is the correct position, Shaykh?',
       '<em>«<strong>And this is the correct position from the standpoint of '
       'the meaning — if it is known, if this is established.</strong> '
       'Otherwise, <strong>the default is that he is a disbeliever; this is the '
       'default</strong>… so the default concerning him is that he is killed and '
       'that he is a disbeliever — <strong>unless it is known by established '
       'means, by the route of the trustworthy, that he is not of those who '
       'practise worship of the jinn</strong>.»</em>') +
    qa('So magic is not disbelief in itself, but for what follows from it?',
       '<em>«<strong>فِيهِ التَّفْصِيل</strong> — there is a distinction in it: '
       '<strong>it may be disbelief in itself, and it may be [disbelief] for '
       'what follows from it of corruption.</strong> So if his magic is by '
       'drawing near to the devils and the jinn and worshipping them and '
       'slaughtering for them and vowing to them — <strong>it becomes greater '
       'disbelief</strong>, and for this Allah named it disbelief… '
       'But if he described it and it became clear that it is something that '
       '<strong>harms people yet is not a drawing near to other than '
       'Allah</strong>, and there is in it no disbelief in Allah nor any claim '
       'that necessitates disbelief — <strong>such as his holding that they '
       'dispose of the universe apart from Allah, or that they change things by '
       'their knowledge — that is the greater disbelief, from the standpoint of '
       'their shirk in the lordship.</strong>»</em>'))
b += B.sharh(table([
    thead3('his craft', 'the ruling', 'the burden'),
    row3('Worship of the jinn — slaughter, vows, drawing near',
         '<strong>كُفْرٌ أَكْبَر</strong>, and «this meaning ought not to be a '
         'place of disagreement»',
         '—'),
    row3('Potions, fumigation, harm — <strong>no</strong> worship of the jinn, '
         'no claim that they dispose of the universe',
         '<strong>Disciplined, or killed</strong> upon the disagreement — '
         '<strong>not</strong> declared a disbeliever',
         '<strong>On whoever claims it.</strong> «The default is that he is a '
         'disbeliever… unless it is known <em>by established means, by the route '
         'of the trustworthy</em>»'),
    row3('Holding that they dispose of the universe, or change things by their '
         'own knowledge',
         '<strong>الكُفْرُ الأَكْبَر</strong> — and he names the reason: '
         '<em>shirk in the RUBŪBIYYAH</em>',
         '—'),
]) + p('<strong>So the clause has a distinction in it and the burden of proof '
       'sits on the exception.</strong> <em>That is a different thing from a flat '
       'rule, and a different thing again from a loose one. Ibn Bāz holds the '
       'default where the verse put it, and will move off it — but only on '
       'establishment «by the route of the trustworthy», which is not a thing a '
       'bystander can supply.</em>'))

# ---------------------------------------------------------------- kufran
b += B.heading('يُقْتَلُ كُفْرًا', 'Killed As a Disbeliever, Not As a Ḥadd')
b += B.sharh(
    qa('Is the magician killed <strong>as a ḥadd</strong>, or '
       '<strong>as a disbeliever</strong>?',
       '<em>«<strong>He is killed as a disbeliever</strong> — because he does '
       'not practise it except by shirk and worship of the jinn.»</em>') +
    qa('And the ruling on praying over the magician, and burying him in the '
       'graveyards of the Muslims, after he is killed?',
       '<em>«If he is killed, <strong>he is not prayed over, and not buried in '
       'the graveyards of the Muslims</strong>; he is buried in the graveyards '
       'of the disbelievers, <strong>and he is not washed and not '
       'shrouded</strong>.»</em>') +
    p('<em>That answer is where the abstraction stops being abstract.</em> '
      '<strong>The classification is not rhetorical</strong> — it governs the '
      'washing, the shroud, the janāzah and the ground. <em>Which is also why '
      'the distinction above matters so much: a man disciplined for a harmful '
      'craft is buried as a Muslim, and a man killed for shirk is not.</em>'))

# ---------------------------------------------------------------- repentance
b += B.heading('تَوْبَةُ السَّاحِر', 'His Repentance — and the One Fact It Turns On')
b += B.prose(
    '<strong>This is the most carefully balanced answer on the folios</strong>, '
    'and it separates two things that are constantly run together: '
    '<em>whether the worldly sentence is lifted</em>, and <em>whether Allah '
    'accepts him</em>.')
b += B.sharh(
    box('<p style="margin:0 0 .55rem;font-size:.94rem"><em>«And it has been '
        'established from ʿUmar رَضِيَ اللهُ عَنْه that he wrote to his '
        'governors — I mean his commanders — with the <strong>killing of the '
        'magicians</strong>, to prevent their corruption in the earth and their '
        'harming of the Muslims and their bringing of harm upon the people. '
        '<strong>So whenever they are known, it is obligatory upon the guardians '
        'of the Muslims’ affairs to kill them — even if they say: we have '
        'repented</strong>; because they are not believed.»</em></p>'
        '<p style="margin:0;font-size:.95rem"><em>«<strong>But if they are '
        'truthful in the repentance, that benefits them with Allah</strong> — '
        'for the generality of His saying…»</em></p>'))
b += B.ayah(
    'وَهُوَ الَّذِي يَقْبَلُ التَّوْبَةَ عَنْ عِبَادِهِ وَيَعْفُو عَنِ '
    'السَّيِّئَاتِ وَيَعْلَمُ مَا تَفْعَلُونَ',
    'And it is He who accepts repentance from His servants and pardons misdeeds, '
    'and He knows what you do.',
    'سُورَةُ الشُّورَى · 42:25')
b += B.sharh(
    p('With it he cites the Prophet’s ﷺ words <em>«%s»</em> — repentance '
      'demolishes what came before it. <strong>The sharḥ gives no grading for '
      'that wording at this place, so none is supplied here.</strong>'
      % ar('التَّوْبَةُ تَهْدِمُ مَا كَانَ قَبْلَهَا')) +
    box('<p style="margin:0;font-size:.94rem"><em>«As for one who '
        '<strong>comes to the guardians of affairs without having been '
        'seized</strong>, informing of his repentance, and that he had done '
        'such-and-such in time past and has repented to Allah, and good has '
        'appeared from him — <strong>this one’s repentance is accepted</strong>; '
        'because he came <strong>by choice</strong>, seeking good, announcing '
        'his repentance, <strong>without anyone having seized him or anyone '
        'having brought a claim against him</strong>.»</em></p>'
        '<p style="margin:.5rem 0 0;font-size:.93rem"><em>«And the point is that '
        'if he comes in a form in which there is <strong>no stratagem and no '
        'deceit</strong>, then the like of this one’s repentance is accepted; '
        'because he came repentant, regretful — like others of the disbelievers '
        'who have an evil past, and then Allah favours them with repentance '
        '<strong>without coercion and without a claim against them from '
        'anyone</strong>.»</em></p>'))
b += B.sharh(table([
    thead3('', 'he was SEIZED', 'he CAME of his own accord'),
    row3('<strong>the worldly sentence</strong>',
         'Carried out — «<em>even if they say: we have repented; because they '
         'are not believed</em>»',
         '<strong>Lifted</strong> — «<em>this one’s repentance is '
         'accepted</em>»'),
    row3('<strong>with Allah</strong>',
         '<strong>Accepted if he is truthful</strong> — «<em>that benefits them '
         'with Allah</em>», on al-Shūrā 42:25',
         'Accepted'),
    row3('<strong>the reason</strong>',
         'Credibility: a claim of repentance under arrest is «<em>a '
         'stratagem</em>»',
         '«<em>He came <strong>by choice</strong>… without anyone having seized '
         'him</em>»'),
]) + p('<strong>Read the second row.</strong> <em>Even the man who is executed '
       'is not pronounced upon before Allah.</em> The refusal is a judgement '
       'about <strong>credibility in a court</strong>, not about Allah’s mercy — '
       'and Ibn Bāz says so in the same breath as the refusal. '
       '<em>And the magicians of Pharaoh, from part 1, are the Qurʾān’s own case '
       'of the door in the second row standing open.</em>'))
b += B.sharh(
    qa('And the killing of a <strong>woman</strong> magician?',
       '<em>«<strong>This is the correct position; her ruling is the ruling of '
       'the man</strong> — and for this Ḥafṣah killed the slave girl who had '
       'bewitched her.»</em>') +
    p('<strong>And the compiler handles the obvious objection rather than '
      'ignoring it.</strong> ʿĀʾishah رَضِيَ اللهُ عَنْهَا, in a report of '
      'ʿAbd al-Razzāq, <em>sold</em> the slave girl who had bewitched her rather '
      'than killing her. His answer: <em>it is borne on the slave girl not '
      'having worked the magic herself, but having asked a magician to work it '
      'for her — «for had she been the one who bewitched her herself, she would '
      'not have sold her to a bedouin; rather she would have killed her», since '
      'a slave girl’s knowledge of magic is a defect for which a sale is '
      'returned, and she might have bewitched the bedouin who bought her or '
      'another.</em>'))

# ---------------------------------------------------------------- the hadith
b += B.heading('حَدُّ السَّاحِرِ ضَرْبُهُ بِالسَّيْف',
               'The One Ḥadīth Everybody Quotes — and Its Grading')
b += B.prose(
    '<strong>This is the most instructive page in the clause, and it is a '
    'footnote.</strong> <em>The report is quoted everywhere, by everyone, as the '
    'ḥadd of the magician. The compiler takes it apart, and the names he quotes '
    'are not obscure ones.</em>')
b += B.hadith(
    'حَدُّ السَّاحِرِ ضَرْبُهُ بِالسَّيْف',
    '“The ḥadd of the magician is a stroke of the sword.”',
    'ضَعِيفٌ مَرْفُوعًا · the correct is that it is the word of Jundub '
    'رَضِيَ اللهُ عَنْه — see the gradings below')
b += B.sharh(table([
    row('the chain',
        'All of them from <strong>Ismāʿīl ibn Muslim al-Makkī</strong> from '
        'al-Ḥasan al-Baṣrī from Jundub al-Khayr from the Prophet ﷺ — narrated by '
        'al-Tirmidhī, Ibn Abī ʿĀṣim, al-Ṭabarānī, al-Dāraquṭnī, Ibn ʿAdī, '
        'al-Bayhaqī and others'),
    row('the defect',
        '<em>«a weak ḥadīth: <strong>Ismāʿīl ibn Muslim was inconsistent in '
        'it</strong>, and in him is weakness — so once he narrated it '
        '<strong>connected</strong>, and once he narrated it from al-Ḥasan '
        'al-Baṣrī <strong>mursal</strong>»</em>. The one corroborator, '
        '<strong>Khālid al-ʿAbdī</strong>, is «<em>very weak, not to be argued '
        'with</em>»'),
    row('البُخَارِيّ',
        'asked about it by al-Tirmidhī, he said: <em>«<strong>هَذَا لَا '
        'شَيْء</strong>»</em> — “this is nothing” — <em>«and Ismāʿīl is very '
        'weak»</em>'),
    row('التِّرْمِذِيّ',
        '<em>«<strong>and the correct is: from al-Ḥasan, from Jundub, '
        'mawqūf</strong>»</em> — and <strong>Ibn Rajab</strong> affirmed that in '
        '<em>Jāmiʿ al-ʿUlūm wa-l-Ḥikam</em>'),
    row('الذَّهَبِيّ',
        'in <em>al-Kabāʾir</em>: <em>«<strong>the correct is that it is from the '
        'statement of Jundub</strong>»</em>'),
    row('ابْنُ حَجَر',
        'in <em>al-Fatḥ</em>: <em>«<strong>in its chain is weakness</strong>»</em>'),
    row('ابْنُ حَزْم',
        'weakened it in <em>al-Muḥallā</em>; and <strong>Ibn al-Mundhir</strong> '
        'in <em>al-Iqnāʿ</em>: <em>«in its chain there is a criticism»</em>'),
    row('ابْنُ بَاز',
        '<em>«<strong>and the marfūʿ aḥādīth — in them is weakness; and the '
        'preponderant view is its being mawqūf upon Jundub al-Khayr</strong>»</em>'),
]))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><strong>Seven named '
        'scholars, and the Shaykh of this very sharḥ among them.</strong> '
        '<em>So the single most-quoted proof for the magician’s death penalty is '
        'not, as a prophetic ḥadīth, something this book will rest the ruling '
        'on.</em></p>'
        '<p style="margin:0;font-size:.93rem"><strong>And yet the ruling '
        'stands</strong> — which is the lesson. <em>The ruling does not fall '
        'because one proof for it falls.</em> It rests on the verse, on the '
        'reasoning about corruption, and on what follows.</p>',
        wash='var(--accent-wash)', edge='var(--accent)'))
b += B.heading('أَثَرُ عُمَر', 'What Does Carry It')
b += B.sharh(table([
    row('the athar',
        'From <strong>Bajālah</strong>: <em>«ʿUmar ibn al-Khaṭṭāb wrote: '
        '<strong>kill every magician and sorceress</strong>» — he said: '
        '<strong>so we killed three sorceresses</strong>»</em>. Narrated by Abū '
        'Dāwūd, Aḥmad, ʿAbd al-Razzāq, al-Bayhaqī, and Ibn Ḥazm in '
        '<em>al-Muḥallā</em>'),
    row('its grading',
        '<em>«<strong>وَإِسْنَادُهُ صَحِيح</strong>»</em> — the compiler’s own '
        'grading — <em>«and <strong>Ibn Ḥazm</strong> authenticated it»</em>'),
    row('and the ijmāʿ',
        '<strong>Ibn Qudāmah</strong> in <em>al-Mughnī</em>: '
        '<em>«<strong>and this became well known and was not objected to, so it '
        'was a consensus</strong>»</em>. Likewise <strong>Sulaymān ibn '
        'ʿAbdillāh</strong> in <em>al-Taysīr</em>: «<em>and the people acted on '
        'it in his caliphate without objection, so it was a '
        'consensus</em>»; and <strong>al-Qannawjī</strong> in '
        '<em>al-Rawḍah al-Nadiyyah</em>: «<em>the Rightly-Guided Caliphs acted '
        'upon the killing of the magicians, and that became widespread and no '
        'one objected to it</em>»'),
    row('<strong>the precision</strong>',
        '<em>«and <strong>al-Bukhārī narrated in his Ṣaḥīḥ the kernel of the '
        'report abridged, WITHOUT the command to kill the sorceresses</strong>»</em>. '
        '<em>Which is exactly the kind of sentence that separates a careful book '
        'from a loose one — the Ṣaḥīḥ is cited for what it contains and not for '
        'what one would like it to contain.</em>'),
    row('and Jundub',
        'Ibn Bāz: <em>«it is established of <strong>Jundub al-Khayr '
        'al-Azdī</strong>, one of the Companions of the Prophet ﷺ, that he '
        'killed some of the magicians»</em> — he came upon one performing before '
        '<strong>al-Walīd</strong>, playing with his own head and restoring it, '
        '<em>«so he came at him from a direction he did not know and killed him, '
        'and said: <strong>restore your head, if you are truthful</strong>»</em>'),
]))
b += B.prose(
    '<em>So the structure of the proof is worth naming.</em> '
    '<strong>A weak marfūʿ report; a ṣaḥīḥ athar of ʿUmar; a reported consensus '
    'built on that athar’s having gone unopposed; and a Companion’s deed.</strong> '
    '<em>The ruling is as strong as that stack — and no stronger than it, which '
    'is why the stack is shown rather than summarised.</em>')
b += B.sharh(
    p('<strong>And the compiler faces the obvious question squarely:</strong> '
      '<em>if the ḥadd of the magician is death, why did the Prophet ﷺ not kill '
      'Labīd, who bewitched him?</em> He gives <strong>four</strong> answers, '
      'and asserts none of them:') +
    table([
        row('قِيل',
            'Labīd may not have worked the magic himself — <em>another made it '
            'for him</em>, so he was not the magician'),
        row('قِيل',
            'He may have left killing him <em>for the treaty that was between '
            'him and the Jews</em>'),
        row('قِيل',
            'Labīd was <em>a hypocrite outwardly professing Islām</em>, so '
            'killing him was left <strong>«lest people say that Muḥammad kills '
            'his companions»</strong>'),
        row('قِيل',
            'It may have been <em>before it was established that the ḥadd of '
            'the magician is death</em>; and <em>«he left him for fear of the '
            'Jews’ mischief, for they were people of force until Allah '
            'destroyed them»</em>'),
    ]) +
    p('<em>Four «قِيل»s and no verdict.</em> <strong>That is the honest shape of '
      'an answer to a question the texts do not settle</strong>, and it is worth '
      'noticing in a book that is perfectly willing to be decisive elsewhere.'))

# ---------------------------------------------------------------- without permission
b += B.heading('بِغَيْرِ إِذْنِ وَلِيِّ الأَمْر', 'Acting Without Permission')
b += B.prose(
    'And then the question Jundub’s deed raises, put to him by his student '
    'Shaykh ʿUmar al-ʿĪd: <em>whoever does what Jundub did when he sees a '
    'magician — is it said that it is permitted, or that the matter is referred '
    'to the one in authority?</em>')
b += B.sharh(
    box('<p style="margin:0;font-size:.93rem"><em>«In any case '
        '<strong>this is a place of ijtihād</strong>. If he fears that the one '
        'in authority will not permit him, and he wants to nullify his plot and '
        'to aid the truth — then this is like what Jundub did, fine. But if he '
        'hopes that the one in authority will agree and will assist him in this '
        'matter, then there is no harm. <strong>The matter differs according to '
        'the strength of the man in his faith and his vigour and his '
        'boldness</strong>; so if he seeks permission so as not to harm himself, '
        'there is no harm; and if he goes forward and does not mind, as Jundub '
        'went forward, there is no harm — because it is '
        '<strong>of the chapter of aiding the truth</strong>.</em></p>'
        '<p style="margin:.6rem 0 0;font-size:.95rem"><em>«<strong>But the rule '
        'in this is: that these matters are not undertaken except by the '
        'permission of the guardians of affairs</strong> — so that no corruption '
        'occurs, and so that he does not harm himself.»</em></p>'))
b += B.sharh(
    qa('And if he is killed [for it]?',
       '<em>«<strong>Even if he is killed — the matter is easy.</strong>»</em>') +
    p('<strong>Read the whole answer and not the half of it.</strong> <em>He '
      'allows the case and then states the rule against it in the same '
      'paragraph — «لَكِنَّ القَاعِدَةَ فِي هَذَا: أَنَّ هَذِهِ الأُمُورَ لَا '
      'يُقْدَمُ عَلَيْهَا إِلَّا بِإِذْنِ وُلَاةِ الأُمُور» — with two reasons: '
      '<strong>lest corruption occur, and lest he harm himself</strong>.</em>') +
    p('<em>And notice what the permitted case actually is in his description:</em> '
      'a man <strong>in the presence of the ruler</strong>, where the ruler '
      '<em>knows</em> the man is a corrupter, who <strong>puts himself '
      'forward to make the falsehood clear to the people</strong> and does not '
      'mind <em>if he is imprisoned or beaten</em>. '
      '<strong>The thing being praised is a man accepting cost to expose a '
      'fraud — not a man taking a sentence into his own hands in '
      'secret.</strong>'))

# ---------------------------------------------------------------- qalb al-ayan
b += B.heading('قَلْبُ الأَعْيَان', 'Can a Magician Turn a Man Into a Donkey?')
b += B.sharh(
    p('Ibn Bāz, replying to <strong>al-Rāzī</strong>’s claim that the magician '
      'can turn a man into a donkey:') +
    box('<p style="margin:0;font-size:.94rem"><em>«Then his saying — “that by it '
        'he attains to <strong>changing the physical essences</strong>” — '
        '<strong>is also an error</strong>. Rather what is attained by it is '
        '<strong>the seeming, and the hurt, and the harm</strong>; and as for '
        'the essences, <strong>the magicians do not attain to that</strong>… '
        'As for changing the essences — <strong>no. All of this is false, and '
        'great ignorance.</strong>»</em></p>') +
    p('His proof is the two verses from part 1 — <em>«they bewitched the '
      '<strong>eyes</strong> of the people»</em> and <em>«it was '
      '<strong>made to seem</strong> to him»</em> — plus <em>«and they could not '
      'harm anyone by it except by Allah’s permission»</em>. '
      '<strong>Seeming, and harm. Not creation.</strong>'))
b += B.sharh(
    p('The compiler then stacks the arguments, and the best of them is '
      '<strong>Ibn Jarīr’s</strong>, which is a reductio about truth itself:') +
    box('<p style="margin:0;font-size:.93rem"><em>«They said: <strong>had it been '
        'within the magicians’ power to originate bodies and to overturn the '
        'realities of essences from the forms they are in, there would be no '
        'distinction between falsehood and truth</strong>, and it would be '
        'possible that <strong>all perceptible things</strong> were of what the '
        'magicians bewitched and whose essences they overturned.»</em></p>') +
    p('<em>And he adds ʿĀʾishah’s report of the Prophet ﷺ having been bewitched '
      '— «it was made to SEEM to him that he was doing a thing when he was not '
      'doing it» — as «the clearest indication of the falsity of the claim of '
      'those who claim that the magician originates the essences of things».</em>'))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><strong>And here is the '
        'thing worth most on this page: the compiler rejects one of the '
        'arguments made on his own side.</strong></p>'
        '<p style="margin:0 0 .5rem;font-size:.93rem">Two writers he quotes '
        'argue: <em>if that were possible, the magicians would be the richest of '
        'people and the kings of the world — and no court file in all the ages '
        'records a claim against a magician for turning a brother into a '
        'donkey.</em></p>'
        '<p style="margin:0;font-size:.94rem">His comment: '
        '<em>«<strong>وَفِي هَذَا الإِلْزَامِ الأَخِيرِ نَظَر</strong>» — '
        'and in this last binding argument there is something to be examined — '
        '<strong>because we all say that the magician can, by Allah’s '
        'permission, bewitch the eyes of the gold-sellers by giving them blank '
        'papers which they see as thousands</strong>; and with that they were '
        'not the richest of people.»</em> And his explanation of why: '
        '<em>«because Allah — blessed and exalted — <strong>nullifies most of '
        'their magic</strong> by which they harm people. Then too, '
        '<strong>magic is limited</strong>: the magician cannot bewitch all '
        'people, nor everyone he wishes to bewitch, nor is he able to perform '
        'magic at every time.»</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)'))
b += B.prose(
    '<strong>That is a scholar refusing a bad argument for a conclusion he '
    'holds</strong>, and it is worth more as a model than the conclusion is. '
    '<em>He then gives the argument he does accept, and it is a tawḥīd '
    'argument:</em> overturning essences into other essences is '
    '<strong>a kind of creating</strong>; the magician works only through the '
    'jinn; <em>«and the jinn are not able to create, and whoever says they are '
    'able to create has disbelieved in Allah»</em> — so if the jinn cannot '
    'create, <strong>their helpers among the magicians of mankind cannot '
    'either.</strong>')
b += B.sharh(
    p('And the athar of <strong>Dūmat al-Jandal</strong> — the woman who claimed '
      'she commanded wheat to sprout and ripen and grind in an instant, which '
      'Ibn Kathīr called <em>«a strange report and an astonishing account»</em> '
      'and which some used to prove that essences can be overturned — is '
      'answered three ways:') +
    table([
        row('١', 'The woman is <strong>unknown</strong> — «and how is reliance '
            'placed on a woman with whom the devils had toyed, and who claimed '
            'that her faith had departed from her?»'),
        row('٢', 'Even granting her truthfulness, it is borne on her '
            '<strong>having been bewitched with the magic of seeming</strong> — '
            'she supposed she had sown and nothing was sown'),
        row('٣', '<strong>The report is not sound</strong>, for the weakness of '
            'its chain. <strong>Ibn Bāz:</strong> <em>«in its chain is '
            '<strong>ʿAbd al-Raḥmān ibn Abī al-Zinād</strong>, and in him is '
            'criticism, and this is <strong>of his oddities and his '
            'singularities</strong>… so it is not relied upon and not turned '
            'to… the upshot is that this is of the strange reports: it is either '
            '<strong>a concealed defect, or of ʿAbd al-Raḥmān’s errors, or of '
            'this old woman’s lying</strong>»</em>'),
    ]) +
    p('<em>And Ibn Bāz adds a substantive objection too:</em> the report '
      '<strong>contains nothing of what the magicians actually teach</strong> — '
      '«<em>they teach them shirk with Allah and worship of the jinn besides '
      'Allah</em>» — «<em>and there is mentioned here nothing but mere sowing '
      'and reaping and grinding, and this is nothing</em>».'))
b += B.sharh(
    qa('Does the magician <strong>fly in the air</strong>, in reality?',
       '<em>«It is said that <strong>the jinn carry him</strong> — not of '
       'himself; like how they used to <strong>eavesdrop</strong>, some of them '
       'mounting above others until they reached the lowest heaven and received '
       'what was said there… <strong>So Allah gave them things of strength, and '
       'gave them things of swift movement, for a far-reaching wisdom</strong> — '
       'like what He gave the angels: the angel descends from the heaven and '
       'ascends in an instant.»</em>') +
    p('<em>And asked whether it is established that they carry a person:</em> '
      '<strong>«هَذَا يُقَالُ — يَقُولُهُ الَّذِينَ يَتَعَاطَوْنَ '
      'أَخْبَارَهُم»</strong> — <em>“this is said; those who deal in reports of '
      'them say it”</em> — and he attributes the mention to Shaykh al-Islām '
      'and others. <strong>Note the register: he reports who says it and does '
      'not adopt it.</strong>'))
b += B.ayah(
    'وَأَنَّا كُنَّا نَقْعُدُ مِنْهَا مَقَاعِدَ لِلسَّمْعِ فَمَن يَسْتَمِعِ '
    'الْآنَ يَجِدْ لَهُ شِهَابًا رَّصَدًا',
    'And we used to sit in stations therein to listen, but whoever listens now '
    'will find a burning flame lying in wait for him.',
    'سُورَةُ الجِنّ · 72:9')

# ---------------------------------------------------------------- the arraf
b += B.heading('سُؤَالُ العَرَّافِ وَتَصْدِيقُه', 'Asking Them, and Believing Them')
b += B.prose(
    'The last block on these folios is about the <strong>client</strong>, not '
    'the magician — and it is the part most people will actually need.')
b += B.sharh(
    box('<p style="margin:0;font-size:.93rem"><em>«So the upshot is: '
        '<strong>these people teach the people what harms them and does not '
        'benefit them</strong>, so that they may consume people’s wealth '
        'wrongfully and live among people by falsehood, in consuming their '
        'wealth and lying to them. <strong>So whoever believes them, of those '
        'who ask them, in the claim of knowledge of the unseen — has disbelieved '
        'as they have.</strong> And as for <strong>mere asking</strong> — it is '
        'not permitted, because it is <strong>a means to believing '
        'them</strong>.»</em></p>'))
b += B.hadith(
    'مَنْ أَتَى عَرَّافًا فَسَأَلَهُ عَنْ شَيْءٍ لَمْ تُقْبَلْ لَهُ صَلَاةُ '
    'أَرْبَعِينَ يَوْمًا',
    '“Whoever comes to a fortune-teller and asks him about something — no '
    'prayer of his is accepted for forty days.”',
    'يَنْسِبُهُ الشَّيْخُ إِلَى صَحِيحِ مُسْلِم، عَنْ بَعْضِ أَزْوَاجِ '
    'النَّبِيِّ ﷺ · reported as the sharḥ places it')
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.94rem"><strong>And now a piece of '
        'textual criticism aimed at a printed book of this very school.</strong> '
        'Some copies of <em>Kitāb al-Tawḥīd</em> carry the ḥadīth with the extra '
        'words <strong>«%s»</strong> — “and believes him”.</p>'
        '<p style="margin:0;font-size:.94rem">Ibn Bāz: '
        '<em>«and as for what is in some copies of Kitāb al-Tawḥīd, '
        '“<strong>fa-ṣaddaqahu</strong>” — <strong>this is not '
        'preserved</strong>; the narration is only “<em>and asks him about '
        'something</em>”, thus did <strong>Muslim</strong> narrate it»</em>; and '
        'elsewhere: <em>«by this it is known that what occurred in some copies '
        'of al-Tawḥīd, “fa-ṣaddaqahu”, is <strong>a mistake — it is not in '
        'Muslim</strong>, rather <strong>a mistake from some of the copyists who '
        'added “fa-ṣaddaqahu”</strong>.»</em></p>'
        % ar('فَصَدَّقَه')) +
    p('<strong>And the correction is not a softening — it sharpens the '
      'ruling.</strong> <em>Because if the forty-day threat is on '
      '<strong>asking alone</strong>, then asking alone carries it; and '
      '«<em>when the believing comes, the threat becomes severer — and that is '
      'disbelief</em>».</em>'))
b += B.sharh(table([
    thead3('what he did', 'the ruling', 'the proof'),
    row3('<strong>Asked</strong> only, without believing',
         '<strong>Not</strong> disbelief — but forbidden, and under the threat: '
         '<em>no prayer accepted for forty days</em>',
         'the ḥadīth, on the preserved wording. <em>And the footnote reasons: '
         '«for had he disbelieved, none of his deeds would be accepted on any of '
         'his days»</em>'),
    row3('<strong>Believed</strong> him in the claim of knowledge of the unseen',
         '<strong>كُفْر</strong> — and asked «greater disbelief?» he answered '
         '<em>«نَعَم، هَذَا الظَّاهِر»</em>, and of «lesser disbelief» said '
         '<em>«لَيْسَ بِظَاهِر»</em>',
         '«<em>for the unseen — none knows it but Allah</em>». And the ḥadīth '
         '«<em>فَقَدْ كَفَرَ بِمَا أُنْزِلَ عَلَى مُحَمَّد</em>» — '
         '<strong>given here without a grading, so none is supplied</strong>'),
    row3('Believed him <strong>in one particular report</strong> — e.g. about '
         'treating a sick relative — <strong>without</strong> believing a claim '
         'of knowing the unseen',
         '«<em><strong>هَذِهِ مَسْأَلَةٌ جُزْئِيَّة</strong> — a partial '
         'matter; what is threatened with disbelief does not follow from '
         'it</em>»',
         '«<em>rather he believed him that this occurred — not that he knows the '
         'unseen</em>». <strong>But</strong>: «<em>as for believing him in '
         'knowledge of the unseen — <strong>even by reason of one specific '
         'case</strong> — the ḥadīth includes him</em>»'),
]))
b += B.prose(
    '<em>That third row is the real-world case and he does not flatten it.</em> '
    '<strong>What is believed matters, not merely whom.</strong> A man who takes '
    'a factual statement as having happened is in one place; a man who takes the '
    'teller to <em>know the unseen</em> — even about one matter — is in another. '
    '<em>And the second does not become safe by being small.</em>')
b += B.sharh(
    p('He also explains <strong>why asking alone carries so heavy a '
      'threat</strong>, and the reason is social rather than personal: '
      '<em>«because it is a means to believing, and a means to '
      '<strong>making his affair appear and spreading his reputation until '
      'people seek him out</strong>»</em> — and in the <em>Fatāwā</em>: '
      '<em>«because coming to them and asking them <strong>raises their '
      'standing</strong>, and causes their affair to become widespread in the '
      'lands, and people’s believing of them»</em>.') +
    p('He quotes the Prophet ﷺ on the kāhins — <em>«%s»</em> and '
      '<em>«%s»</em> — <strong>both given here without attribution or grading, '
      'so none is supplied.</strong>'
      % (ar('لَا تَأْتُوهُم'), ar('لَيْسُوا بِشَيْء'))))
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.93rem"><strong>And a footnote '
        'guards the sentence «none knows the unseen but Allah» from being '
        'over-read.</strong> It does not contradict that some of the awliyāʾ may '
        'have something disclosed to them — <em>«not because they are described '
        'with knowledge of the unseen or part of it, but they are '
        '<strong>inspired</strong> at some time; and then this inspiration is '
        '<strong>a preponderant supposition, not knowledge</strong>»</em>.</p>'
        '<p style="margin:0;font-size:.93rem">Ibn Bāz, asked about '
        '<strong>المُكَاشَفَات</strong>: <em>«what appears is that they divide '
        'into two kinds — <strong>a sound kind and a corrupt kind</strong>: a '
        'kind belonging to the false Ṣūfīs, and a kind belonging to the people '
        'of good and faith», like what came that they are inspired — '
        '«<strong>إِنْ كَانَ فِي أُمَّتِي مُحَدَّثُونَ فَعُمَر</strong>» — '
        '«as in the story of <strong>Sāriyah of the mountain</strong>… and it is '
        'called <strong>فِرَاسَة</strong> and called <strong>كَرَامَة</strong>»; '
        'whereas the others «<em>have no insight — rather the devils convey to '
        'them slight hidden things, and they inform people of them, claiming '
        'they are unseen matters disclosed to them</em>».</em></p>'
        '<p style="margin:.5rem 0 0;font-size:.91rem;color:var(--ink-light)">'
        '<em>That wording of the Prophet ﷺ is quoted here loosely, with «مِثْلُ '
        'مَا جَاءَ» and no grading, so the page supplies none.</em></p>'))

# ---------------------------------------------------------------- batil hadith
b += B.heading('تَعَلَّمُوا السِّحْرَ وَلَا تَعْمَلُوا بِه', 'A Fabrication, Named')
b += B.sharh(
    qa('What is the soundness of a ḥadīth I heard from the Prophet ﷺ: '
       '<strong>«learn magic but do not act upon it»</strong>?',
       '<em>«<strong>هَذَا الحَدِيثُ بَاطِلٌ لَا أَصْلَ لَه</strong> — this '
       'ḥadīth is false; it has no basis. And it is not permitted to learn '
       'magic, nor to act upon it; and that is an abomination — rather '
       '<strong>disbelief and misguidance</strong>… <strong>because learning '
       'magic, all of it, is disbelief</strong>; and for this He informed of the '
       'two angels that they do not teach people magic until they say to the '
       'learner: «إِنَّمَا نَحْنُ فِتْنَةٌ فَلَا تَكْفُر» — so it is known that '
       'it is disbelief and misguidance.»</em>') +
    p('<strong>Two fabrications named on one clause</strong> — this, and the '
      'weak marfūʿ of the ḥadd. <em>And the second rule-8 lesson of these '
      'folios: a report’s being universally repeated is no part of its '
      'grading.</em>'))
b += B.prose(
    '<strong>Part 3 takes printed folios ١٧٩–١٩٣</strong> and closes the longest '
    'clause in the book: <em>whether the Prophet ﷺ was bewitched and how that '
    'sits with «وَاللهُ يَعْصِمُكَ مِنَ النَّاس», النُّشْرَة and what is '
    'permitted in treating magic, telling the bewitched from the insane, and '
    'Hārūt and Mārūt.</em>')

b += B.vocab([
    ('المُفْسِدُونَ فِي الأَرْض', 'al-mufsidūn fī al-arḍ',
     'those who spread corruption in the earth',
     'The SECOND ground for the magician’s killing, reasoned from the highway '
     'robber — «وَالسَّاحِرُ فَوْقَ ذَلِكَ وَأَشَرُّ مِنْ ذَلِك». A '
     'public-order ground, and it names the one in authority by its own form.'),
    ('فِيهِ التَّفْصِيل', 'fīhi al-tafṣīl', 'there is a distinction in it',
     'Ibn Bāz, pressed on al-Shāfiʿī’s view: magic «may be disbelief in itself, '
     'and may be for what follows from it of corruption».'),
    ('الأَصْل', 'al-aṣl', 'the default',
     'What remains when the distinction is granted: «الأَصْلُ أَنَّهُ كَافِر… '
     'إِلَّا إِذَا عُرِفَ بِطُرُقٍ ثَابِتَةٍ بِطَرِيقِ الثِّقَات». The burden '
     'sits on the exception.'),
    ('يُقْتَلُ كُفْرًا', 'yuqtalu kufran', 'he is killed as a disbeliever',
     'Not as a ḥadd. And the classification is not rhetorical: not washed, not '
     'shrouded, not prayed over, buried in the graves of the disbelievers.'),
    ('مَوْقُوف', 'mawqūf',
     'stopping at a Companion, not reaching the Prophet ﷺ',
     'What «حَدُّ السَّاحِرِ ضَرْبُهُ بِالسَّيْف» really is — Ibn Bāz: '
     '«وَالرَّاجِحُ وَقْفُهُ عَلَى جُنْدُبٍ الخَيْر»; al-Bukhārī of the marfūʿ '
     'chain: «هَذَا لَا شَيْء».'),
    ('أَثَرُ عُمَر', 'athar ʿUmar', 'the report of ʿUmar',
     'What does carry the ruling — «اقْتُلُوا كُلَّ سَاحِرٍ وَسَاحِرَة», chain '
     'graded ṣaḥīḥ; Ibn Qudāmah: «اشْتُهِرَ وَلَمْ يُنْكَرْ فَكَانَ '
     'إِجْمَاعًا». And al-Bukhārī has the kernel WITHOUT the command.'),
    ('قَلْبُ الأَعْيَان', 'qalb al-aʿyān', 'overturning physical essences',
     'What the magician CANNOT do — «كُلُّ هَذَا بَاطِلٌ وَجَهْلٌ كَبِير». It '
     'is a kind of creating, and the jinn cannot create; so neither can their '
     'helpers.'),
    ('الإِلْزَام', 'al-ilzām', 'a binding argument',
     'The compiler on one offered for HIS own conclusion: «وَفِي هَذَا '
     'الإِلْزَامِ الأَخِيرِ نَظَر» — a bad argument for a true conclusion is '
     'still a bad argument.'),
    ('غَيْرُ مَحْفُوظ', 'ghayr maḥfūẓ', 'not preserved',
     'Ibn Bāz’s verdict on «فَصَدَّقَه» in some copies of Kitāb al-Tawḥīd — a '
     'copyist’s addition; Muslim has only «فَسَأَلَهُ عَنْ شَيْء». The '
     'correction SHARPENS the ruling.'),
])

b += B.mcq('nq-l12-mcq', [
    ('What are the two grounds on which Ibn Bāz holds the magician is killed?',
     ['His harm and his lying',
      'His disbelief, misguidance and apostasy if he was a Muslim; and his being '
      'of those who spread corruption in the earth, so that people be relieved '
      'of his evil',
      'His shirk and his theft of wealth',
      'The consensus and the ḥadīth of Jundub'], 1),
    ('From what does he reason the second ground?',
     ['The ḥadīth of the seven mūbiqāt',
      'From the highway robbers — where the one in authority may choose killing '
      'when it is more beneficial, to protect people; «and the magician is above '
      'that and worse than that»',
      'From the ruling on the apostate',
      'From the athar of Ḥafṣah'], 1),
    ('What is notable about the FORM of that second ground?',
     ['It is weaker than the first',
      'It is a public-order ground that names the one in authority making a '
      'judgement of interest — so it is not available to a private person',
      'It applies only in the Ḥaram',
      'It is disputed among the four imāms'], 1),
    ('What did al-Shāfiʿī and a group hold?',
     ['That the magician is never killed',
      'That his magic is EXAMINED: if it is potions and fumigation without '
      'drawing near to the jinn, he is disciplined or killed upon the '
      'disagreement; if it involves worship of the jinn, he is a disbeliever',
      'That he is always a disbeliever',
      'That the matter belongs to the scholars of his land'], 1),
    ('What did Ibn Bāz answer when the questioner said that was the correct '
     'position?',
     ['That it is an error',
      '«And this is the correct position from the standpoint of the meaning — IF '
      'IT IS KNOWN, if this is established» — otherwise the default is that he '
      'is a disbeliever',
      'That the matter is one of ijtihād with no answer',
      'That al-Shāfiʿī did not say it'], 1),
    ('On what condition will he move off the default?',
     ['On the magician’s own claim',
      'If it is known «by established means, BY THE ROUTE OF THE TRUSTWORTHY» '
      'that he is not of those who practise worship of the jinn',
      'On the testimony of two witnesses of any kind',
      'If he has repented'], 1),
    ('Asked directly whether magic is disbelief in itself, he answered:',
     ['«It is in itself»',
      '«فِيهِ التَّفْصِيل» — it may be disbelief in itself, and it may be for '
      'what follows from it of corruption',
      '«It is never in itself»',
      '«The question may not be asked»'], 1),
    ('Which claim does he name as the greater disbelief «from the standpoint of '
     'shirk in the lordship»?',
     ['Claiming to heal',
      'Holding that they dispose of the universe apart from Allah, or that they '
      'change things by their own knowledge',
      'Claiming to know the future',
      'Taking payment for magic'], 1),
    ('Is the magician killed as a ḥadd or as a disbeliever?',
     ['As a ḥadd',
      'As a disbeliever — «because he does not practise it except by shirk and '
      'worship of the jinn»',
      'As a muḥārib only',
      'The sharḥ does not say'], 1),
    ('What follows from that for his body?',
     ['He is washed and prayed over as a Muslim',
      'He is not washed, not shrouded, not prayed over, and buried in the '
      'graveyards of the disbelievers',
      'He is buried without a shroud but prayed over',
      'The matter is left to his family'], 1),
    ('Why does the distinction about his craft matter so much in practice?',
     ['It affects only the wording of the sentence',
      'Because a man disciplined for a harmful craft is buried as a Muslim, and '
      'a man killed for shirk is not',
      'Because it determines who carries out the sentence',
      'Because it affects the inheritance only'], 1),
    ('ʿUmar wrote to his governors with what?',
     ['The imprisonment of magicians',
      'The killing of the magicians — «kill every magician and sorceress»; '
      'Bajālah: «so we killed three sorceresses»',
      'Their exile from the Arabian peninsula',
      'Their being asked to repent three times'], 1),
    ('How is that athar graded, and by whom?',
     ['Weak, by Ibn Ḥazm',
      'Its chain is ṣaḥīḥ — the compiler’s grading — and Ibn Ḥazm authenticated '
      'it',
      'Ḥasan, by al-Bayhaqī',
      'No grading is given'], 1),
    ('What did Ibn Qudāmah say about it?',
     ['That it is the view of ʿUmar alone',
      '«And this became well known and was not objected to, so it was a '
      'consensus»',
      'That it was abrogated',
      'That it applies to men only'], 1),
    ('What precision does the compiler add about al-Bukhārī?',
     ['That he narrates it with a fuller wording',
      'That he narrates the kernel of the report ABRIDGED — without the command '
      'to kill the sorceresses',
      'That he rejects the report',
      'That he narrates it from Jundub'], 1),
    ('«حَدُّ السَّاحِرِ ضَرْبُهُ بِالسَّيْف» — what is its grading here?',
     ['Ṣaḥīḥ',
      'Weak as a marfūʿ report; the correct is that it is MAWQŪF, the word of '
      'Jundub',
      'Ḥasan by corroboration',
      'No grading is given'], 1),
    ('What did al-Bukhārī say of it when al-Tirmidhī asked him?',
     ['«It is ḥasan»',
      '«هَذَا لَا شَيْء» — this is nothing — and «Ismāʿīl is very weak»',
      '«Its chain is sound»',
      '«I do not know it»'], 1),
    ('And Ibn Bāz himself?',
     ['That it is authentic',
      '«And the marfūʿ aḥādīth — in them is weakness; and the preponderant view '
      'is its being mawqūf upon Jundub al-Khayr»',
      'That he had not examined it',
      'That it is a fabrication'], 1),
    ('What is the defect in the chain?',
     ['A break between al-Ḥasan and Jundub only',
      'Ismāʿīl ibn Muslim al-Makkī was INCONSISTENT in it — once connected, once '
      'mursal — and in him is weakness; his one corroborator, Khālid al-ʿAbdī, '
      'is very weak',
      'The unknown identity of Jundub',
      'Nothing; the chain is sound'], 1),
    ('So what does the ruling actually rest on, as the page shows it?',
     ['The weak marfūʿ report',
      'A stack: the verse; the reasoning about corruption; the ṣaḥīḥ athar of '
      'ʿUmar; a reported consensus built on that athar having gone unopposed; '
      'and a Companion’s deed',
      'Consensus alone',
      'The view of the majority alone'], 1),
    ('Why did the Prophet ﷺ not kill Labīd, who bewitched him? The compiler '
     'gives:',
     ['One decisive answer',
      'Four answers introduced with «قِيل», asserting none — including that '
      'Labīd may not have worked it himself, the treaty with the Jews, that he '
      'was a hypocrite outwardly professing Islām «lest people say Muḥammad '
      'kills his companions», and that it may have been before the ḥadd was '
      'established',
      'No answer at all',
      'Two answers, both certain'], 1),
    ('When the magician who has been SEIZED says he has repented?',
     ['The sentence is lifted',
      'It is carried out — «even if they say: we have repented; because they are '
      'not believed»',
      'He is imprisoned instead',
      'He is asked to repent three times'], 1),
    ('And what does Ibn Bāz say in the same breath about that man before Allah?',
     ['That his repentance is void',
      '«But if they are truthful in the repentance, THAT BENEFITS THEM WITH '
      'ALLAH» — on al-Shūrā 42:25',
      'That nothing can be said',
      'That he is in the Fire'], 1),
    ('And the magician who comes forward of his own accord, before being seized?',
     ['He is still killed',
      'His repentance is accepted — «because he came BY CHOICE, seeking good, '
      'announcing his repentance, without anyone having seized him or brought a '
      'claim against him»',
      'He is imprisoned',
      'He must leave the land'], 1),
    ('So what does the whole answer turn on?',
     ['The gravity of his magic',
      'Whether he came of his own accord or was seized — a judgement about '
      'CREDIBILITY in a court, not about Allah’s mercy',
      'How long he practised',
      'Whether he harmed anyone'], 1),
    ('The woman magician?',
     ['She is imprisoned, not killed',
      '«Her ruling is the ruling of the man» — and for this Ḥafṣah killed the '
      'slave girl who bewitched her',
      'She is exiled',
      'The matter is disputed with no answer'], 1),
    ('How does the compiler reconcile ʿĀʾishah having SOLD the slave girl who '
     'bewitched her?',
     ['By rejecting the report',
      'That the slave girl had not worked the magic herself but asked a magician '
      'to work it for her — «for had she bewitched her herself she would not '
      'have sold her to a bedouin; rather she would have killed her»',
      'That ʿĀʾishah was unaware',
      'That the ruling differs for slaves'], 1),
    ('On acting against a magician WITHOUT the ruler’s permission, Ibn Bāz '
     'said:',
     ['It is forbidden absolutely',
      'It is a place of ijtihād — and then stated the rule in the same '
      'paragraph: «these matters are not undertaken except by the permission of '
      'the guardians of affairs», lest corruption occur and lest he harm himself',
      'It is obligatory on whoever is able',
      'It is permitted only for scholars'], 1),
    ('What is the case he actually praises, in his own description?',
     ['A man killing a magician in secret',
      'A man in the ruler’s presence, where the ruler knows the man is a '
      'corrupter, who puts himself forward to make the falsehood clear to people '
      'and does not mind being imprisoned or beaten',
      'A man gathering a group to act',
      'A man writing to the ruler'], 1),
    ('Can a magician turn a man into a donkey?',
     ['Yes, by Allah’s permission',
      'No — «all of this is false, and great ignorance»; what is attained is the '
      'SEEMING, and the hurt, and the harm, not the essences',
      'Only with the aid of the greater jinn',
      'The question is unanswerable'], 1),
    ('What is Ibn Jarīr’s argument against it?',
     ['That no text reports it',
      'That had it been in their power to originate bodies and overturn the '
      'realities of essences, there would be NO DISTINCTION between falsehood '
      'and truth, and all perceptible things might be what magicians had '
      'overturned',
      'That the jinn are forbidden to do it',
      'That it would contradict the Prophet’s ﷺ miracle'], 1),
    ('Which argument does the compiler REJECT, although it supports his own '
     'conclusion?',
     ['Ibn Jarīr’s reductio',
      'The claim that otherwise magicians would be the richest of people — «and '
      'in this last binding argument there is something to be examined», since a '
      'magician can bewitch gold-sellers’ eyes with blank paper and they are '
      'still not the richest',
      'The report of ʿĀʾishah',
      'The verse «وَلَا يُفْلِحُ السَّاحِرُ حَيْثُ أَتَى»'], 1),
    ('Why does he say they are not, then?',
     ['Because they are forbidden to use it for wealth',
      'Because Allah nullifies most of their magic by which they harm people; '
      'and because magic is LIMITED — not all people, not everyone he wishes, '
      'not at every time',
      'Because the jinn take the wealth',
      'Because they are few'], 1),
    ('Which argument against قَلْبِ الأَعْيَان does he accept?',
     ['The argument from court records',
      'A tawḥīd argument: overturning essences is a kind of CREATING; the '
      'magician works only through the jinn; the jinn cannot create — «and '
      'whoever says they are able to create has disbelieved in Allah» — so '
      'neither can their helpers',
      'The argument from wealth',
      'The argument from experience'], 1),
    ('The athar of Dūmat al-Jandal is answered three ways. Which is Ibn Bāz’s '
     'own chain criticism?',
     ['That Bajālah is unknown',
      'That in its chain is ʿAbd al-Raḥmān ibn Abī al-Zinād, in whom is '
      'criticism, «and this is of his oddities and his singularities»',
      'That al-Ḥākim rejected it',
      'That Ibn Kathīr declared it fabricated'], 1),
    ('And what substantive objection does he add to it?',
     ['That the woman was a Jew',
      'That the report contains nothing of what the magicians actually teach — '
      '«they teach them shirk with Allah and worship of the jinn» — «and there '
      'is mentioned here nothing but mere sowing and reaping and grinding»',
      'That wheat does not grow in Dūmah',
      'That ʿĀʾishah denied it'], 1),
    ('Does the magician fly in the air?',
     ['Yes, by his own power',
      '«It is said that the jinn carry him — not of himself»; and asked whether '
      'it is established, he answered «this is said; those who deal in reports '
      'of them say it» — reporting who says it without adopting it',
      'No, never',
      'Only the greatest of them'], 1),
    ('Mere ASKING a fortune-teller, without believing him:',
     ['Is disbelief',
      'Is forbidden and under the threat — no prayer accepted for forty days — '
      'but not disbelief; «for had he disbelieved, none of his deeds would be '
      'accepted on any of his days»',
      'Is permitted if necessary',
      'Is a minor sin with no threat'], 1),
    ('And BELIEVING him in the claim of knowledge of the unseen?',
     ['Lesser disbelief',
      'Disbelief — and asked whether greater, he said «yes, this is what '
      'appears»; and of «lesser disbelief» he said «that is not what appears»',
      'Fisq',
      'It depends on the matter'], 1),
    ('What did Ibn Bāz judge about «فَصَدَّقَه» in some copies of Kitāb '
     'al-Tawḥīd?',
     ['That it is the preserved wording',
      'That it is NOT PRESERVED — not in Muslim, «rather a mistake from some of '
      'the copyists who added it»; Muslim has only «and asks him about something»',
      'That both wordings are in Muslim',
      'That the whole ḥadīth is weak'], 1),
    ('Why does that correction SHARPEN the ruling rather than soften it?',
     ['It does not; it softens it',
      'Because the forty-day threat then falls on ASKING alone — «and when the '
      'believing comes, the threat becomes severer, and that is disbelief»',
      'Because it makes the ḥadīth weaker',
      'Because it removes the threat entirely'], 1),
    ('A man believes a fortune-teller about one particular matter — his sick '
     'relative — without believing he knows the unseen. Ibn Bāz:',
     ['He has disbelieved',
      '«This is a partial matter; what is threatened with disbelief does not '
      'follow from it» — he believed that this occurred, not that the man knows '
      'the unseen. BUT believing him in knowledge of the unseen, «even by reason '
      'of one specific case», the ḥadīth includes him',
      'He is a fāsiq',
      'The matter requires research'], 1),
    ('Why is mere asking under so heavy a threat?',
     ['Because it wastes money',
      'Because it is a means to believing, and «raises their standing» and '
      'causes their affair to spread in the lands until people seek them out',
      'Because it is a form of worship',
      'Because the jinn attend the asker'], 1),
    ('How does the footnote guard «none knows the unseen but Allah» from being '
     'over-read?',
     ['By restricting it to the Prophets',
      'That some of the awliyāʾ may be INSPIRED at a time — not described with '
      'knowledge of the unseen — and that such inspiration is «a preponderant '
      'supposition, not knowledge»; Ibn Bāz divides المُكَاشَفَات into a sound '
      'kind and a corrupt kind',
      'By denying that it ever happens',
      'By restricting it to the Companions'], 1),
    ('«تَعَلَّمُوا السِّحْرَ وَلَا تَعْمَلُوا بِه» — Ibn Bāz’s verdict?',
     ['Ḥasan',
      '«This ḥadīth is FALSE; it has no basis» — and learning magic, all of it, '
      'is disbelief',
      'Ṣaḥīḥ but misunderstood',
      'Weak but acted upon'], 1),
    ('What is the rule-8 lesson of these folios?',
     ['That weak reports may be used for virtues',
      'That a report’s being universally repeated is no part of its grading — '
      'two of the most-quoted reports in this clause are weak and fabricated '
      'respectively',
      'That gradings are a matter of ijtihād',
      'That only al-Bukhārī and Muslim may be cited'], 1),
])

b += B.tf('nq-l12-tf', [
    ('قَالَ ابْنُ بَازٍ إِنَّ السِّحْرَ كُفْرٌ فِي ذَاتِهِ بِلَا '
     'تَفْصِيل.',
     'Ibn Bāz said magic is disbelief in itself with no distinction.', False),
    ('الأَصْلُ فِي السَّاحِرِ أَنَّهُ كَافِرٌ حَتَّى يُعْرَفَ خِلَافُ ذَلِكَ '
     'بِطَرِيقِ الثِّقَات.',
     'The default concerning the magician is that he is a disbeliever until the '
     'contrary is known by the route of the trustworthy.', True),
    ('السَّاحِرُ يُقْتَلُ حَدًّا لَا كُفْرًا.',
     'The magician is killed as a ḥadd, not as a disbeliever.', False),
    ('حَدِيثُ «حَدُّ السَّاحِرِ ضَرْبُهُ بِالسَّيْفِ» صَحِيحٌ مَرْفُوعًا.',
     'The ḥadīth «the ḥadd of the magician is a stroke of the sword» is '
     'authentic as a marfūʿ report.', False),
    ('إِسْنَادُ أَثَرِ عُمَرَ فِي قَتْلِ السَّحَرَةِ صَحِيح.',
     'The chain of ʿUmar’s report on killing the magicians is authentic.', True),
    ('مَنْ تَابَ مِنَ السِّحْرِ قَبْلَ أَنْ يُقْبَضَ عَلَيْهِ تُقْبَلُ '
     'تَوْبَتُه.',
     'Whoever repents of magic before being seized — his repentance is accepted.',
     True),
    ('مُجَرَّدُ سُؤَالِ العَرَّافِ كُفْرٌ أَكْبَر.',
     'Merely asking a fortune-teller is greater disbelief.', False),
])

b += B.memorize(
    'وَفِي هَذَا الإِلْزَامِ الأَخِيرِ نَظَر',
    'The compiler — <strong>about an argument offered in support of a '
    'conclusion he himself holds.</strong> <em>Two writers argued that if '
    'magicians could overturn essences they would be the richest men alive; he '
    'agrees with their conclusion and takes their argument apart anyway, then '
    'supplies a better one from tawḥīd.</em> <strong>A bad argument for a true '
    'conclusion is still a bad argument</strong>, and these folios show the same '
    'discipline twice more — on %s, which is quoted everywhere and graded weak '
    'here by seven named scholars, and on %s, which Ibn Bāz calls '
    '«بَاطِلٌ لَا أَصْلَ لَه». <em>And the ruling still stands, resting on what '
    'actually carries it.</em>'
    % ('«' + ar('حَدُّ السَّاحِرِ ضَرْبُهُ بِالسَّيْف') + '»',
       '«' + ar('تَعَلَّمُوا السِّحْر') + '»'))

b += B.nav('nq-l11-haqiqat-al-sihr.html',
           'النَّاقِضُ السَّابِع · part 1',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l12')

B.write('nq-l12-hukm-al-sahir.html',
        'النَّاقِضُ السَّابِع · حُكْمُ السَّاحِر',
        'The Seventh Nullifier, Part 2 — The Ruling on the Magician',
        'The ruling half of the seventh nullifier, from the words of Shaykh Ibn '
        'Bāz: the two grounds for the magician’s killing, reasoned from the '
        'highway robber; the tafṣīl he grants on al-Shāfiʿī’s view and the '
        'default that remains, moved off only on establishment «by the route of '
        'the trustworthy»; that he is killed as a disbeliever and not as a ḥadd, '
        'with what follows for washing, shrouding, prayer and burial; when his '
        'repentance is refused and when accepted, and that even the executed man '
        'is not pronounced upon before Allah; the grading of «the ḥadd of the '
        'magician is a stroke of the sword» as weak by seven named scholars '
        'including Ibn Bāz, and what carries the ruling instead; acting without '
        'the ruler’s permission; the refutation of al-Rāzī on overturning '
        'essences, including an argument the compiler rejects on his own side; '
        'and the rulings on asking and believing a fortune-teller.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ الثَّانِي عَشَر', '6', b)
print('wrote nq-l12-hukm-al-sahir.html')
