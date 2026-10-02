# -*- coding: utf-8 -*-
"""Shared page builders for matn-depth mutun units.

Used to build Aqeedah Unit 5 (al-Qawaid al-Arba'); reusable for the Wasitiyyah
and the other mutun. SRC is the page whose header/nav gets spliced, so new
lessons always carry the current nav -- repoint it if building another unit.

Splices the live header/nav out of the existing u5 page so new lessons carry the
current dropdowns. Quiz markup follows the real engine contract in js/main.js:
initMCQ reads data-correct=<index> on .mcq-question; initTrueFalse needs
.tf-text/.tf-ar plus .tf-buttons with two .tf-btn[data-val].
"""
import io, re, os

BASE = os.path.dirname(os.path.abspath(__file__))
AQ = os.path.join(BASE, 'pages', 'aqeedah')
SRC = io.open(os.path.join(AQ, 'u5-qawaid-arba.html'), encoding='utf-8').read()
PRE = SRC[:SRC.index('<main>')]
POST = SRC[SRC.index('</main>'):]

FOOT = (u"al-Qawāʿid al-Arbaʿ of Imam Muḥammad ibn ʿAbd al-Wahhāb · "
        u"sharḥ of Ṣāliḥ ibn ʿAbd al-ʿAzīz Āl al-Shaykh "
        u"and al-Fawzān · in our own words")

READING = [
    u'Shaykh Ṣāliḥ ibn ʿAbd al-ʿAzīz Āl al-Shaykh, '
    u'<em>Sharḥ al-Qawāʿid al-Arbaʿ</em> (Maktabat Dār al-Ḥijāz, '
    u'1st ed. 1433H) — the sharḥ this unit follows.',
    u'Shaykh Ṣāliḥ al-Fawzān, <em>Sharḥ al-Qawāʿid al-Arbaʿ</em>.',
    u'Shaykh Muḥammad ibn Ṣāliḥ al-ʿUthaymīn, '
    u'<em>Sharḥ Kashf al-Shubuhāt</em> — the companion treatise of the same author, '
    u'on answering the arguments of the mushrikīn.',
]


def shell(title_ar, title_en, desc, body):
    pre = re.sub(r'<title>.*?</title>',
                 u'<title>%s — %s | العقيدة | '
                 u'دار الهجرة</title>'
                 % (title_ar, title_en), PRE, flags=re.S)
    pre = re.sub(r'(<meta name="description" content=")(.*?)(">)',
                 lambda m: m.group(1) + desc + m.group(3), pre, count=1, flags=re.S)
    post = re.sub(r'(<footer class="site-footer">.*?<p>)(.*?)(</p>)',
                  lambda m: m.group(1) + FOOT + m.group(3), POST, count=1, flags=re.S)
    # POST already begins with </main>, so do not close it again here
    return pre + u'<main>\n' + body + u'\n' + post


def card(num_label, year, tar, ten, inner, back=u'u5-qawaid-arba.html',
         back_label=u'القَوَاعِدُ الأَرْبَع'):
    return (u'  <div style="max-width:860px;margin:0 auto;padding:var(--space-xl)">\n'
            u'    <a href="%s" style="font-size:.82rem;color:var(--ink-light);text-decoration:none">← %s</a>\n\n'
            u'    <div class="lesson-card" style="margin-top:var(--space-md)">\n'
            u'      <div class="lesson-card-header">\n'
            u'        <span class="lesson-number">%s</span>'
            u'<span class="year-badge" data-year="%s">Year %s</span>\n'
            u'        <div class="lesson-title-wrap">\n'
            u'          <p class="lesson-title-ar">%s</p>\n'
            u'          <p class="lesson-title-en">%s</p>\n'
            u'        </div>\n'
            u'      </div>\n\n'
            u'      <div class="lesson-card-body">\n\n%s\n'
            u'      </div>\n'
            u'    </div>\n'
            u'  </div>') % (back, back_label, num_label, year, year, tar, ten, inner)


def objectives(items):
    lis = u'\n'.join(u'            <li>%s</li>' % i for i in items)
    return (u'        <div class="objectives-box">\n'
            u'          <p class="objectives-title">Objectives — '
            u'أَهْدَافُ الدَّرْس</p>\n'
            u'          <ul class="objectives-list">\n%s\n          </ul>\n'
            u'        </div>\n') % lis


def heading(ar, en):
    return (u'\n        <div class="section-heading">\n'
            u'          <span class="sh-ar">%s</span>\n'
            u'          <span class="sh-en">%s</span>\n'
            u'        </div>\n') % (ar, en)


def matn(text, note=None):
    extra = (u'\n          <p style="font-size:.78rem;color:var(--ink-light);'
             u'margin-top:var(--space-sm);font-style:italic">%s</p>' % note) if note else u''
    return (u'\n        <div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
            u'border-radius:var(--radius-sm);padding:var(--space-lg);margin:var(--space-lg) 0">\n'
            u'          <p style="font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;'
            u'color:var(--ink-light);margin:0 0 var(--space-sm)">'
            u'مِنَ المَتْن · '
            u'the author’s own words</p>\n'
            u'          <p dir="rtl" lang="ar" style="font-size:1.2rem;line-height:2.5;'
            u'text-align:right;margin:0;color:var(--ink)">%s</p>%s\n'
            u'        </div>\n') % (text, extra)


def prose(html):
    return (u'        <p style="font-size:.92rem;color:var(--ink-mid);line-height:1.85;'
            u'margin-bottom:var(--space-md)">\n          %s\n        </p>\n') % html


def sharh(html):
    return (u'\n        <div style="border:1px solid var(--line);border-radius:var(--radius-sm);'
            u'padding:var(--space-lg);margin:var(--space-md) 0 var(--space-lg)">\n'
            u'          <p style="font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;'
            u'color:var(--ink-light);margin:0 0 var(--space-sm)">'
            u'الشَّرْح · the explanation</p>\n'
            u'          <div style="font-size:.92rem;color:var(--ink-mid);line-height:1.85">%s</div>\n'
            u'        </div>\n') % html


def ayah(ar, en, src):
    return (u'        <div class="ayah-block">\n'
            u'          <p class="ayah-arabic">%s</p>\n'
            u'          <p class="ayah-translation">%s</p>\n'
            u'          <p class="ayah-source">%s</p>\n'
            u'        </div>\n') % (ar, en, src)


def hadith(ar, en, src):
    return (u'        <div class="hadith-block">\n'
            u'          <p class="hadith-arabic">%s</p>\n'
            u'          <p class="hadith-translation">%s</p>\n'
            u'          <p class="hadith-source">%s</p>\n'
            u'        </div>\n') % (ar, en, src)


def vocab(cards):
    out = []
    for ar, tr, en, df in cards:
        out.append(u'          <div class="vocab-card" data-ar="%s" data-translit="%s" '
                   u'data-en="%s" data-definition="%s">\n'
                   u'            <span class="vocab-ar">%s</span>'
                   u'<span class="vocab-transliteration">%s</span>'
                   u'<span class="vocab-en">%s</span>\n'
                   u'          </div>' % (ar, tr, en, df, ar, tr, en))
    return (heading(u'المُفْرَدَات',
                    u'Key Vocabulary — tap to flip')
            + u'        <div class="vocab-grid">\n' + u'\n'.join(out) + u'\n        </div>\n')


def mcq(qid, qs):
    """qs = [(question, [options...], correct_index), ...]"""
    blocks = []
    for q, opts, ci in qs:
        o = u'\n'.join(u'                  <div class="mcq-option">%s</div>' % t for t in opts)
        blocks.append(u'              <div class="mcq-question" data-correct="%d">\n'
                      u'                <p class="mcq-q-text">%s</p>\n'
                      u'                <div class="mcq-options">\n%s\n'
                      u'                </div>\n'
                      u'              </div>' % (ci, q, o))
    return (u'\n        <div class="exercise-block" style="margin-top:var(--space-xl)">\n'
            u'          <div class="exercise-header">\n'
            u'            <span class="exercise-type">Check Your Understanding · MCQ</span>\n'
            u'            <span class="exercise-title-ar">'
            u'أَسْئِلَة</span>\n'
            u'          </div>\n'
            u'          <div class="exercise-body">\n'
            u'            <div data-quiz="mcq" data-quiz-id="%s">\n%s\n'
            u'            </div>\n          </div>\n        </div>\n') % (qid, u'\n'.join(blocks))


def tf(qid, qs):
    """qs = [(arabic_statement, english_statement, is_true), ...]"""
    blocks = []
    for ar, en, ans in qs:
        blocks.append(u'              <div class="tf-question" data-answer="%s">\n'
                      u'                <div class="tf-text">\n'
                      u'                  <span class="tf-ar">%s</span>\n'
                      u'                  %s\n'
                      u'                </div>\n'
                      u'                <div class="tf-buttons">\n'
                      u'                  <button class="tf-btn" data-val="true">True ✓</button>\n'
                      u'                  <button class="tf-btn" data-val="false">False ✗</button>\n'
                      u'                </div>\n'
                      u'              </div>' % (u'true' if ans else u'false', ar, en))
    return (u'\n        <div class="exercise-block" style="margin-top:var(--space-lg)">\n'
            u'          <div class="exercise-header">\n'
            u'            <span class="exercise-type">True or False</span>\n'
            u'            <span class="exercise-title-ar">'
            u'صَحٌ أَمْ خَطَأٌ</span>\n'
            u'          </div>\n'
            u'          <div class="exercise-body">\n'
            u'            <div data-quiz="tf" data-quiz-id="%s">\n%s\n'
            u'            </div>\n          </div>\n        </div>\n') % (qid, u'\n'.join(blocks))


def memorize(ar, en):
    return (u'\n        <div class="memorize-block">\n'
            u'          <p class="memorize-label">Memorize &amp; Reflect — '
            u'احْفَظْ وَتَدَبَّرْ</p>\n'
            u'          <p class="memorize-ar">%s</p>\n'
            u'          <p class="memorize-en">%s</p>\n'
            u'        </div>\n') % (ar, en)


def aiquiz(topic):
    return (u'\n        <div style="text-align:center;margin-top:var(--space-lg)">\n'
            u'          <button class="btn-gold" onclick="generateAIQuiz(\'%s\')">'
            u'✨ Generate an extra quiz on this lesson</button>\n'
            u'        </div>\n') % topic


def further(items=None):
    items = items or READING
    lis = u'\n'.join(u'            <li>%s</li>' % i for i in items)
    return (u'\n        <details style="margin-top:var(--space-xl);border:1px solid var(--line);'
            u'border-radius:var(--radius-sm);padding:var(--space-md)">\n'
            u'          <summary style="cursor:pointer;font-size:.88rem;color:var(--ink-mid)">'
            u'Further reading — optional aids · '
            u'<span dir="rtl" lang="ar">لِلاسْتِزَادَة</span>'
            u'</summary>\n'
            u'          <p style="font-size:.84rem;color:var(--ink-light);line-height:1.8;'
            u'margin-top:var(--space-sm)">\n'
            u'            This lesson teaches everything you need on the page. These are optional '
            u'aids — nothing below is required.\n          </p>\n'
            u'          <ul style="font-size:.86rem;color:var(--ink-mid);line-height:1.9;'
            u'padding-right:1.1rem">\n%s\n          </ul>\n'
            u'        </details>\n') % lis


def nav(prev_href, prev_label, next_href, next_label, lesson_id):
    return (u'\n        <div style="display:flex;justify-content:space-between;align-items:center;'
            u'gap:var(--space-md);margin-top:var(--space-xl);flex-wrap:wrap">\n'
            u'          <a href="%s" class="btn-secondary">← %s</a>\n'
            u'          <a href="%s" class="btn-primary" onclick="markLessonComplete(\'%s\')">'
            u'%s →</a>\n'
            u'        </div>\n') % (prev_href, prev_label, next_href, lesson_id, next_label)
