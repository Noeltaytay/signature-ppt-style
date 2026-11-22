# Animation Design

The animation pattern is part of the signature style. Keep it consistent even
when the palette changes.

## 1. Principles

- Animation serves comprehension, not decoration.
- Use native PowerPoint effects only.
- One idea per entrance; do not animate every child element.
- Titles and section pages auto-play; evidence and conclusions wait for a click.
- No spin, bounce, fly-in, zoom, continuous loop, flicker, or sound.
- If an effect draws attention to itself, remove it.

## 2. Global settings

- Page transition: **Fade**, 0.45–0.60 s.
- Object entrance: `entrance_fade` or `entrance_wipe`.
- Default trigger: `after-previous`.
- Default duration: 0.30–0.60 s.
- Decelerate: 0.35–0.40 for a soft landing.
- No exit animations unless the story explicitly needs a replacement.

## 3. Per-page pattern

### Cover
1. Title — auto, fade, 0.50 s.
2. Positioning/role — auto, fade, 0.40 s.
3. Visual/image panel — auto, fade, 0.60 s.
4. Identity (name/school) — on click, fade, 0.45 s.
5. Info band — after previous, fade, 0.40 s.

### Contents
1. Heading/route line — auto, fade, 0.45 s.
2. Five rows — sequential `entrance_wipe` down, 0.30 s each.
3. Footer — after previous, fade, 0.35 s.

### Chapter divider
1. Giant chapter number — auto, fade, 0.60 s.
2. Schematic panel — auto, fade, 0.70 s.
3. Title plate — auto, fade, 0.60 s.
4. Tagline — auto, fade, 0.50 s.

No clicks on dividers; they are a 3–5 second transition.

### Capability matrix
1. Title — auto, fade.
2. Rows 1–5 — first row on click, remaining after previous, 0.30–0.35 s.
3. Stats band — on click, fade, 0.40 s.

### Project page
1. Title — auto, fade.
2. Evidence field — on click, fade, 0.55 s.
3. Technical chain — on click, wipe down, 0.60 s.
4. Result — after previous, fade, 0.40 s.

### Research / internship
1. Title — auto.
2. Left/software block — on click, fade.
3. Right/hardware block — after previous, fade.
4. Takeaway band — on click, wipe up.

### Career plan
1. Title — auto.
2. Three stages — first on click, remaining after previous.
3. Action band — on click, wipe up.

### Closing
1. Visual — auto, fade, 0.70 s.
2. Claim — auto, fade, 0.60 s.
3. Identity/thanks — after previous, fade, 0.50 s.

## 4. Naming

`animations.json` slide keys must equal SVG stems. Group IDs must exist in the
SVG.

Divider groups:

```text
chapter-number
chapter-visual
chapter-plate
chapter-line
```

Content pages can use section-specific IDs (`p03-title`, `p05-row-1`, etc.), but
they must stay stable across renames.

## 5. Validation

```bash
python "$PPT_MASTER_DIR/scripts/animation_config.py" validate "<project>"
```

- Every slide key must match an SVG.
- Every referenced group must exist.
- Transitions should be Fade.
- Durations should be in the ranges above.

## 6. Rehearsal

- Divider pages: 3–5 s, no click.
- Content pages: one click for evidence, one for conclusion.
- If the deck feels “click-heavy”, remove a group rather than adding a new
  effect.
- If the deck feels static, add one meaningful reveal, not decoration.
