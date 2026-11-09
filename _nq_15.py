# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 15 — النَّاقِضُ الثَّامِن, part 2.

Printed folios 205-222 (PDF indices 202-219, offset +3) — eighteen folios,
closing the eighth nullifier. Index 220 opens النَّاقِضُ التَّاسِع, which is
how the end of this range is fixed.

The body is assembled from five part files plus the quiz bank, because the
clause has three distinct movements and one file for all of it would be
unreadable:

  A  الاسْتِعَانَةُ بِالكُفَّارِ عَلَى الكُفَّار — the book's own heading, and
     the clause's second half opens on a PERMISSION, with Ibn Bāz applying it
     to a named contemporary case in his own words. Then the ijmāʿ on what the
     nullifier actually is, with its transmitters named — Ibn Ḥazm, and the
     author of the matn himself — and the first excuse refused: kinship.
  B  Fear, and nationality. Al-Māʾidah 5:51-52 against the pan-Arab
     nationalism of his own day, with Ibn Taymiyyah's footnote isolating the
     MOTIVE of tawallī: it was fear, not love of their religion, and the verse
     came down anyway. Then the qāʿidah of istiḥlāl, with its own restraint
     stated three ways.
  C  The tiers restated, and page after page of ordinary civility ruled NOT to
     be the nullifier; the three categories of mankind, whose third is the
     sentence that makes the clause teachable; the household by the same
     criterion, Abū Lahab and Abū Ṭālib included; residence among the
     mushrikīn on al-Nisāʾ 4:97-99, where the preventative named is HIJRAH;
     and the state-level case, permitted and then fenced by its footnote.
  D  وُجُوبُ التَّنَاصُرِ وَالتَّعَاضُدِ بَيْنَ المُؤْمِنِين — the book's
     second printed heading here. Walāʾ read forwards: what a Muslim OWES
     believers, with deceiving and betraying a brother named a نَقْصٌ فِي
     الوِلَايَة inside this very chapter.
  E  The spy, and Ḥāṭib. The longest topic, and the one that forces the
     distinction between the ruling on an act and the ruling on a man.

Two things on these folios are NOT flattened, because flattening either would
misreport the source:

  * Al-Rājiḥī holds the two preventers can never combine again — «مَا
    يَجْتَمِعَان». Ibn Bāz, asked directly, answers «الأَظْهَر» that they can,
    with الأَصْل still being the killing and the judgement belonging to وَلِيّ
    الأَمْر. The compiler's own «قُلْت» sides with Ibn Bāz. All three are on
    the page, named.
  * Ibn Bāz's own two sittings differ: in one a later man may be treated as
    Ḥāṭib was; in another, «فَغَيْرُ حَاطِبٍ لَا يُلْحَقُ بِهِ وَلَا
    يُسَاوِيه». The page gives both and says plainly that they pull in
    different directions.

Rule 8: every report here carries a grading from a named authority — Ibn Bāz
naming «اعْمَلُوا مَا شِئْتُم» الحَدِيثَ الصَّحِيح; «بِسَنَدٍ صَحِيح» with
Ibn Kathīr's «عَلَى شَرْطِ مُسْلِم»; «بِسَنَدٍ حَسَن» with al-Ḥākim,
al-Dhahabī's agreement, al-Ḍiyāʾ and Ibn Kathīr's «إِسْنَادٌ جَيِّد». Where
the sharḥ names a source and gives no grading (al-Bukhārī and Muslim on
«كَالْبِنْيَان»; Muslim on the report of Saʿd; the phrase «مَا فَعَلَ أَبُو
الحُبَاب», for which it names nothing at all) the page says so and supplies
none.
"""
from _nq_15_lib import B
import _nq_15_a, _nq_15_b, _nq_15_c, _nq_15_d, _nq_15_e, _nq_15_q2

body = (_nq_15_a.BODY + _nq_15_b.BODY + _nq_15_c.BODY
        + _nq_15_d.BODY + _nq_15_e.BODY + _nq_15_q2.BODY)

B.write('nq-l15-al-istianah-wa-al-jasus.html',
        'النَّاقِضُ الثَّامِن · الاسْتِعَانَةُ وَالجَاسُوس',
        'The Eighth Nullifier, Part 2 — Seeking Help, and the Spy',
        'The eighth nullifier closed, from the words of Shaykh Ibn Bāz: the '
        'permission this half opens on — seeking the help of disbelievers '
        'against disbelievers, applied to a named contemporary case — against '
        'the ijmāʿ on backing them against the Muslims, with Ibn Ḥazm and the '
        'author of the matn named as its transmitters; the three excuses '
        'refused, kinship and fear and nationality, with Ibn Taymiyyah on the '
        'motive of siding-with; the qāʿidah of istiḥlāl and the restraint '
        'built into it; page after page of ordinary civility ruled not to be '
        'the nullifier at all; the three categories of mankind, and what is '
        'owed to the sinning Muslim by measure; the household judged by faith '
        'and not lineage; residence among the mushrikīn on al-Nisāʾ 4:97–99, '
        'where the remedy named is hijrah; what a Muslim owes his believing '
        'brother, under the book’s own heading on mutual support; and the spy '
        '— with Ḥāṭib ibn Abī Baltaʿah, the two barriers that prevented his '
        'takfīr, the fourteen imāms who called him a mutaʾawwil, and the '
        'places where the scholars quoted here disagree.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ الخَامِسَ عَشَر', '6', body)
print('wrote nq-l15-al-istianah-wa-al-jasus.html')
