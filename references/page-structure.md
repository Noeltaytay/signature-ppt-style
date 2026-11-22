# Page Structure

## 1. Default 15-page architecture

Use for a five-chapter deck with chapter dividers.

| Page | Role | Content |
| ---: | --- | --- |
| 01 | Cover | Identity + one target role |
| 02 | Contents | Five sections + page markers |
| 03 | Divider 01 | Chapter 01 |
| 04 | Content | First chapter evidence |
| 05 | Divider 02 | Chapter 02 |
| 06 | Content | Second chapter evidence |
| 07 | Divider 03 | Chapter 03 |
| 08 | Content | Third chapter evidence A |
| 09 | Content | Third chapter evidence B |
| 10 | Divider 04 | Chapter 04 |
| 11 | Content | Fourth chapter evidence A |
| 12 | Content | Fourth chapter evidence B |
| 13 | Divider 05 | Chapter 05 |
| 14 | Content | Fifth chapter evidence |
| 15 | Closing | One claim + identity |

For a 3–5 minute talk, use 9 pages: cover, chapter 01, chapter 02, chapter 03 A,
chapter 03 B, chapter 04, chapter 05, closing. Omit the contents page and
dividers, or keep one divider as a demonstration.

## 2. Chapter divider rules

- Every chapter gets one divider.
- Divider pages use **schematic** visuals only.
- A divider is not a content page: one chapter number, one title, one tagline,
  one schematic.
- The right panel previews the chapter's thinking:
  - structure outline
  - checklist
  - process chain
  - data/research motif
  - growth steps
- Keep each divider on screen for 3–5 seconds in a six-minute talk.

## 3. TOC

- Five rows for five chapters.
- Each row: number, Chinese title, English subtitle, one-line description,
  page marker.
- Page markers point to the **divider page**:
  - 01 → 03
  - 02 → 05
  - 03 → 07
  - 04 → 10
  - 05 → 13
- No cards, no icon grid.

## 4. Page numbers

- Footer: `04 / 15` (zero-padded current / total).
- Header: current page number only, right-aligned.
- Divider: page number bottom right.
- Closing: `15 / 15`.
- TOC markers: divider page number.

When total pages change, update every footer/header page number.

## 5. Notes

One note per page. For a six-minute deck, target 340–355 seconds.

- Cover 10–15 s
- Contents 5–10 s
- Each divider 3–5 s
- Content pages 25–75 s depending on importance
- Closing 10 s

`notes/total.md` concatenates all page notes with headings matching the SVG
stems.

## 6. Animation keys

`animations.json` slide keys must equal SVG stems.

Divider group IDs:

```text
chapter-number
chapter-visual
chapter-plate
chapter-line
```

Content page group IDs can be section-specific but must be stable across
renames.

## 7. Renumbering checklist

When inserting/removing a page:

1. Back up `svg_output/`, `notes/`, `animations.json`.
2. Rename SVGs and notes in reverse numeric order.
3. Update header/footer page numbers.
4. Update TOC markers if chapter structure changed.
5. Rename/reorder `animations.json` keys.
6. Rebuild `notes/total.md`.
7. Update `design_spec.md` §IX and `spec_lock.md` page rhythm.
8. Re-run quality, animation, and style checks.
9. Rebuild `svg_final`, PPTX, previews, overview, PDF.

Never rename pages without updating all of the above. The user has explicitly
asked for non-destructive, inspect-first revisions.
