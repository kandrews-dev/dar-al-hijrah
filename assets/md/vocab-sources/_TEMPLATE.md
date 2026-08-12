# Vocabulary source drop-point

Put the **digitized vocabulary lists** from the scanned textbooks here — one file per book,
made the same way as `Ajrumiyyah-Master.md` (Claude desktop app reading the scanned PDF pages).

The build only needs the **مفردات (vocabulary) lists per unit** — not the whole book.
Give each word in this format (fully vowelled Arabic + English; add plural for nouns, root if easy):

```
## Book 1 — Unit 3 — الأسرة (The Family)
- أَبٌ (ج آبَاء) — father — root: أ ب و
- أُمٌّ (ج أُمَّهَات) — mother — root: أ م م
- اِبْنٌ (ج أَبْنَاء) — son — root: ب ن و
- ابْنُ العَمِّ — cousin (paternal uncle's son)
...
```

Verbs: give māḍī + muḍāriʿ + meaning →  `ذَهَبَ / يَذْهَبُ — to go`
Expressions: give the phrase + meaning →  `أَهْلًا وَسَهْلًا — welcome`

## Files to produce (suggested names)
- `bayna-yadayk-1-vocab.md`   ← Book 1 (for the children)
- `bayna-yadayk-2-vocab.md`   ← Book 2 (for you)
- `bayna-yadayk-3-vocab.md`   ← Book 3 (for you)
- `imsiu-vocab.md`            ← the IMSIU معجم / vocabulary (name the exact series inside)

Once any of these land here, tell me — I extract every word, **de-duplicate** across the two
series and across book levels (and against what's already taught), split children(Bk1)/you(Bk2-3),
and build each unit to ~90% of its real vocabulary, verified and pushed live.

Source PDFs (scanned images, need OCR/transcription) live at:
`C:\Users\abdul\OneDrive\Documents\Arabic Pdf's\`  — Bayna Yadayk 1–4 + IMSIU L3/L4.
Read /mnt/c/Users/abdul/OneDrive/Documents/Arabic\ Pdf\'s/al-arabibiyyah-bayna-yadaik-1.pdf and extract all vocabulary per unit in this format:

## Book 1 — Unit N — [unit title in Arabic]
- fully-vowelled Arabic — English meaning — (plural for nouns) — (root if clear)

Use pdfplumber or PyPDF2. Don't skip any units. Save output to assets/md/vocab-sources/bayna-yadayk-1-vocab.md
Skip the desktop chat handoff. You can read the PDF yourself.

Read C:\Users\abdul\OneDrive\Documents\Arabic Pdf's\al-arabibiyyah-bayna-yadaik-1.pdf directly using pdfplumber (pip install pdfplumber if needed).

Extract all vocabulary per unit in the format specified in _TEMPLATE.md. Save output to assets\md\vocab-sources\bayna-yadayk-1-vocab.md.

If pdfplumber can't extract text (it's a scanned image), use pytesseract for OCR with Arabic language pack (tesseract with -l ara).