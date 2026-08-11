# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**دار الهجرة — Dār al-Hijrah** (Salafi Foundational School of Islamic Sciences). A pure static site (HTML/CSS/JS, no build step, no framework, no backend). All files live under `C:\Users\abdul\Downloads\Madrasah-Site\`.

## Dev server

```powershell
cd C:\Users\abdul\Downloads\Madrasah-Site
python -m http.server 8123
# then open http://localhost:8123
```

## Rebuilding the search index

After adding or renaming any HTML page, run:

```powershell
python C:\Users\abdul\Downloads\_searchindex.py
```

This re-scans all HTML files and injects the `MDRS_SEARCH` array into `js/main.js` at the `// %%INDEX%%` marker. Skipping this step leaves the search stale.

## Architecture

```
index.html           ← home page
css/main.css         ← single stylesheet (token system + all themes)
js/main.js           ← shared engine: quiz, flashcards, progress, themes, search, year filter
assets/
  pdfs/              ← hosted source PDFs (kebab-named)
  md/                ← pypdf text extracts (text-based PDFs only; scanned ones = 0 chars)
  calligraphy-bg.svg ← tiled background
pages/
  islam101/
  quran/
  hadeeth/
  seerah/
  fiqh/
  aqeedah/
  arabic/            ← hub for all Arabic tracks; links into pages/grammar/ for naḥw lessons
  grammar/           ← al-Ājurrūmiyyah naḥw lessons (referenced from the Arabic tab)
  resources/
```

Lesson files live two levels deep (`pages/<subject>/<lesson>.html`) and use root-relative asset paths (`../../css/main.css`, `../../js/main.js`).

### CSS theme system

`:root` defines lilac tokens as defaults. Theme overrides are `[data-theme="emerald"]`, `[data-theme="ocean"]`, `[data-theme="red"]`, `[data-theme="sand"]`, `[data-theme="royal"]` on `<html>`. Theme is applied immediately via an inline `<script>` in `<head>` before the stylesheet to prevent flash. Subject tab colors (`--tab-*`) are fixed jewel tones that don't change with theme.

### JS engine (`js/main.js`)

Key globals and functions:
- `STATE` — `{ year, progress, scores }`, persisted to `localStorage` under keys `mdrs_year`, `mdrs_progress`, `mdrs_scores`
- `markLessonComplete(id)` — saves a lesson's completion flag
- `initQuiz(id)` / `initTrueFalse()` / `initMCQ()` — auto-initialize from `data-quiz` / `data-quiz-id` attributes
- `initFlashcards()` — targets `[data-ar]` / `[data-en]` vocab cards
- `initThemeSwitcher()` — injects the pop-out `#theme-dock`
- `initSearch()` — Ctrl/⌘-K or `/` to open the command-palette overlay
- `generateAIQuiz(id)` — wired in HTML but requires a backend API key; currently non-functional as a static file

Exams are **self-contained** per-file (inline `<style>` + `<script>`): 35 marks, 35-min timer, 5 sections, auto-marked, score saved to `STATE.scores`.

### Year filter

Content tagged `data-min-year="N"` and/or `data-max-year="N"` is shown/hidden by `applyYearFilter()` based on `STATE.year` (1–5). The year selector is a `<select class="year-select">` rendered site-wide.

## Lesson conventions

Every lesson file must follow this structure in order:
1. Header nav (8 tabs, correct active tab highlighted)
2. Sidebar: unit lesson list + "on this page" anchor links
3. `<div class="objectives-box">` — 3–5 bullet learning objectives
4. Bilingual sections: Arabic proof/text stacked above English explanation
5. Vocab flashcards (`data-ar` / `data-translit` / `data-en` / `data-root` / `data-definition` / `data-example`)
6. Exercises: T/F (`data-quiz="tf"`) and MCQ (`data-quiz="mcq"`) blocks, each with `data-quiz-id="<id>"`
7. Memorize block
8. AI quiz button: `<button onclick="generateAIQuiz('<id>')">`
9. Prev / continue nav with `markLessonComplete('<id>')`

**Lesson ID format:** `<subject-prefix><unit>-l<lesson>` e.g. `aq4-l2`, `fq2-l1`, `nh-l5`, `is1-l3`, `sr-l1`, `hd-h01`, `qr-fatihah`.

## Teaching style rules (load-bearing — apply to all new content)

1. **Arabic script, not transliteration in body text.** Write الكلام (speech) not "al-kalām". Use Arabic + English meaning in parentheses on first use, then Arabic alone. Exceptions: vocab flashcard transliteration line, `<title>` tags/meta descriptions (searchability), historic proper names where transliteration is the common reading.
1a. **FULL ḥarakāt on every Arabic word (load-bearing).** All Arabic in the Arabic sections (and Arabic words everywhere) must be fully vowelled — every fatḥah, ḍammah, kasrah, **sukūn**, shaddah, and tanwīn written — so a new student knows exactly how to pronounce it, **including the sukūn so they know where to stop/pause cleanly**. This includes **Arabic titles and headings**, not just body words. No bare/unvowelled Arabic anywhere in vocab, examples, tables, passages, titles, or headings. Applies to new content AND retroactively to existing pages.
1b. **Explain vocabulary with the Qurʾān first, then hadith, wherever possible.** For each word, prefer a Qurʾānic example — and ALWAYS give the exact sūrah:āyah reference number as the anchor. Hadith may be used where the Qurʾān doesn't fit. VERIFY both before use: the āyah wording + number must be exact, and hadith wording + attribution/authenticity must be checked. No unverified proof-texts (this is the translation-audit standard).
2. **Lessons teach everything on-page.** PDFs and external links go in a "Further reading — optional aids" section at the bottom with a note that they are not required.
3. **Sources: Ahl al-Sunnah only.** Acceptable: Ibn Taymiyyah, Ibn al-Qayyim, Ibn ʿAbd al-Wahhāb, Ibn Bāz, Ibn ʿUthaymīn, al-Albānī, al-Saʿdī, al-Fawzān, al-Mubārakfūrī.
4. **No verbatim copyrighted text.** Explain in own words, with attribution.
5. **Build only in Claude Code.** The chat interface is for visual mockups only — editing the same files from both contexts causes divergence.
6. **Progressive immersion (Books 2 → 3).** Book 1 = full scaffolding (Arabic + transliteration + English). From **Book 2 Unit 1**, DROP transliteration for any word already taught in Book 1; from **Book 3**, drop it for any word taught in Books 1–2. English is minimized and gradually phased out so Book 2 onward is *mainly Arabic* (Arabic-through-Arabic definitions, as in the معجم عربي-عربي). New words still get first-use support; known words are Arabic-only. **Where English/transliteration is kept, hide it under a collapsible native `<details>` "peek" toggle (hidden by default from Book 2)** — the student reads the Arabic first and only glances if stuck, avoiding immediate glossing. Mirrors the tap-to-flip flashcard; no JS needed.
7. **تَعْبِير (Expression) box — bottom of each lesson.** Teaches expressions/idioms/false-friend words by COMPREHENSION, not translation, in four layers: **(a) المعنى** — a simple-Arabic paraphrase; **(b) الصُّورة** — the root + the image/logic behind the words (e.g. «ضَرَبَ في الأرضِ»: the traveller strikes the earth with his steps as he crosses it → travel); **(c) في القرآن** — the verified āyah with its number (rule 1b); **(d) عائلةُ الجَذْر** — the root-family cluster of related expressions (reinforces ṣarf root-thinking). A footer teaches the transferable skill: *if the literal meaning doesn't stand, it's a تعبير — look at the root, the image, the context.* The **English/transliteration sits under a collapsible `<details>` "peek" toggle** (per rule 6), fading book by book (full Bk1 → none Bk3). Same box absorbs single-word false-friends (سَيَّارَة = caravan) — same four moves.

## Multi-page propagation

When adding a new tab or changing the nav, update all ~80 pages in one scripted Python pass (as done historically with `_grambuild.py`, `_demote.py`, etc.). Never hand-edit nav in individual files.

## Progress tracking

`_PROGRESS.md` at the site root is the single source of truth. Update the tab completion percentage and the home page `.completion` bars whenever a tab's lesson count changes.

## PDF text extraction

Text-based PDFs: `pypdf` (pip-installed). Scanned/image PDFs yield 0 chars and require Tesseract OCR + poppler (Tesseract installed via winget; not yet wired in). For scanned sources, write lessons from the matn + attributed tradition without needing the PDF text directly.
