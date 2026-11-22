# Working Preferences

The user cares as much about **how** the deck is made as about the final visual.
Follow these defaults unless the user says otherwise.

## 1. Inspect before changing

Before edits:

- list existing files
- check SVG count, notes, animations, exports, images
- validate XML/ZIP/PDF instead of assuming corruption
- report what is complete, stale, or missing

Do not recreate the project from scratch when a previous session was interrupted.

## 2. Do not overwrite completed work

- Back up `svg_output/`, `notes/`, `animations.json` before structural changes.
- Keep earlier exports; add a new timestamped file instead of deleting history.
- If a PPTX is open (`~$*.pptx` exists), export to a new filename or ask the user
  to close it. Never write through an open file.
- Do not delete backups or prior versions without explicit permission.

## 3. Batch and checkpoint

- Work in small batches: page group → quality check → next group.
- Save intermediate files.
- Avoid one-shot rewrites of the whole deck when a targeted edit will do.
- After a crash, inspect the actual files before continuing.

## 4. Report, then act

The user prefers a short status report before a large change:

- what exists
- what is complete
- what is stale
- what you will change
- what remains

Then execute. Do not silently restart or silently overwrite.

## 5. Adapt to new feedback immediately

The user iterates visually and may change direction mid-task. Treat the latest
instruction as authoritative:

- do not keep an old design because it was previously approved
- do not restore a version the user rejected
- if a request conflicts with an earlier rule, ask one short clarifying question
  or state the trade-off, then proceed

## 6. Truth and evidence

- Use only the user's real facts, photos, dates, awards, and metrics.
- Label schematics as schematics.
- Do not use network or generated images as fake project evidence.
- Distinguish 负责 / 参与 / 协作 / 正在探索.
- Do not fill missing numbers with plausible guesses.

## 7. Language and tone

- Use Chinese for Chinese projects.
- Keep slide text concise and projection-friendly.
- Avoid internal filenames, placeholder notes, and draft comments in final
  slides.
- Speak plainly in status reports; state failures and warnings honestly.

## 8. Output

Deliver:

- editable PPTX
- static PDF
- preview PNGs / overview
- speaker notes
- quality report / postflight report
- exact paths

Report the latest files, not just "done".

## 9. Quality

- 0 blocking SVG errors.
- Animation config valid.
- Page count = notes count.
- Images embedded or resolvable.
- Visual review at 1280×720 and 1920×1080.
- Disclose non-blocking warnings rather than hiding them.

## 10. When requirements conflict

Examples:

- "use my photos" vs "don't put real photos on chapter pages" → photos on
  content pages, schematics on dividers.
- "make it richer" vs "fewer decorations" → richer content through structure,
  not ornament.
- "keep the first version" vs "use the new palette" → keep the composition,
  apply the new palette.

State the resolution in one line, then execute.

## 11. When to ask

Ask only when the choice materially changes the deliverable:

- a new repository/visibility for publishing
- a different brand palette when the skill's palette does not fit
- whether a page should be deleted or moved
- whether personal data/photos may be published

Do not ask about details that can be inferred from the style guide.
