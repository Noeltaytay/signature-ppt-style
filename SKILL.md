---
name: signature-ppt-style
description: >
  Personalized PPT structure and decoration system. Use when the user says
  "按我的PPT风格", "和上次一样", "用我的模板", "signature deck", or references
  the previous career-planning deck. The page architecture, spacing, typography,
  cover/TOC/divider/closing compositions, decorative language, and animation
  pattern are fixed; the palette is chosen from the content, industry, brand,
  and imagery. Applies
  to any topic: business review, academic defense, product launch, training,
  portfolio, or competition. Enforces large type, fewer cards, schematic
  chapter dividers, real evidence only, and an inspect-backup-batch workflow.
  Built as an overlay on ppt-master.
metadata:
  version: "0.2.0"
  license: "MIT"
---

# Signature PPT Style

This is the user's **personal PPT structure memory**: a fixed page architecture,
fixed composition rules, fixed typography, a fixed decorative language, and a
fixed animation pattern. The **palette is not fixed**; it is chosen to match the
content while preserving the same design quality.

The goal: a new deck on any topic should feel like it came from the same
designer, while its colors belong to the topic rather than to a single
blue-gray template.

---

## The core split

| Fixed | Variable |
| --- | --- |
| Page architecture (15/9 pages) | Primary/secondary/accent colors |
| 1280×720 canvas; 72 px header; 40 px footer | Light/dark field choice per section |
| Margins, title position, rule position | Chart palette |
| Typography scale and families | Optional brand tints |
| Cover/TOC/divider/closing compositions | Background imagery/schematics |
| Decorative language: orbit field, giant watermark, accent rules, cream plate, torn panel, chevrons, info band | The actual accent hue and field hue |

**Do not change the structure when the palette changes.** Recolor the same
skeleton; do not redesign the page.

---

## When to use

Use when the user:

- says "按我的 PPT 风格", "和上次一样", "用我的模板", "signature deck"
- asks for a deck that should match the previous career-planning deck's
  structure and decoration
- asks for any topic in the same visual language: business, academic, product,
  training, portfolio, competition
- asks to continue, revise, or re-export a deck built with this system

Do not use when the user explicitly asks for a different structure, a client
brand book, or a style exploration. Ask first.

---

## Fixed page architecture

Default **15 pages** for a five-chapter talk:

| Page | Role |
| ---: | --- |
| 01 | Cover |
| 02 | Contents |
| 03 | Divider 01 |
| 04 | Chapter 01 content |
| 05 | Divider 02 |
| 06 | Chapter 02 content |
| 07 | Divider 03 |
| 08 | Chapter 03 content A |
| 09 | Chapter 03 content B |
| 10 | Divider 04 |
| 11 | Chapter 04 content A |
| 12 | Chapter 04 content B |
| 13 | Divider 05 |
| 14 | Chapter 05 content |
| 15 | Closing |

For 3–5 minutes, use a **9-page compact** version: cover, chapter 01, chapter
02, chapter 03 A, chapter 03 B, chapter 04, chapter 05, closing; omit contents
and dividers, or keep one divider.

TOC markers point to the divider page, not the first content page.

---

## Fixed composition rules

### Content page frame

- Canvas 1280×720.
- Header band `0 0 1280 72`; footer band `0 680 1280 40`.
- Margins 64 px.
- Title rule at `x=64 y=112 w=48 h=2`.
- Title baseline `y=168`; subtitle `y=206`.
- Header: name at `x=64`; nav from `x=250`; page number right at `x=1216`.
- Footer: source/boundary at `x=64`; page number right.
- Active nav item: bright + accent underline (`y=64`, width 116).
- No card grid; use open rows, columns, bands, or one large field.
- ≤ 7 content units per page.

### Cover

- Split composition: left identity, right framed image/schematic panel.
- Orbit field, giant single-character watermark, accent rules.
- Title 96 px serif, 2–3 lines; one line may use the accent.
- Bottom light info band with three columns.
- Page number bottom right.
- The cover may be more decorative than content pages.

### TOC

- Full-bleed primary field; orbit rings; giant section-count watermark.
- Left: “目录” 96 px + `CONTENTS` + route line.
- Right: five rows: number, title, English subtitle, one-line description,
  page marker.
- Active row: accent vertical bar + bright title.

### Chapter divider

- Full-bleed primary field.
- Giant chapter number 420 px at `x=80 y=540`, low opacity.
- Light title plate at `x=84 y=294 w=604 h=224`, accent offset and border.
- Chinese title 96 px at `x=132 y=420`; English 22–24 px at `x=134 y=470`;
  two accent chevrons.
- Handwritten tagline 34 px at `x=110 y=600`.
- Right: torn-paper panel with a **schematic** inside.
- **No real photos/screenshots on dividers.**
- `PART 0X` top right; page number bottom right.

### Closing

- Full-bleed primary field.
- One claim, name/role, thanks; no new evidence.
- Right image/schematic panel, same framing language as the cover.

### Typography (fixed)

- Display/title: `Georgia, Source Han Serif SC Heavy, SimSun`
- Body: `Microsoft YaHei, Arial`
- Handwritten: `KaiTi, STKaiti, Microsoft YaHei`
- Display 84–96; title 44; subtitle 24; body 20–26; caption 16–19;
  micro 12–14; chapter number 420; stage numeral 56.

### Animation design (fixed)

Animation is functional, not decorative. Use native PowerPoint effects only:

- All page transitions: Fade, 0.45–0.60 s.
- No spin, bounce, fly-in, zoom, continuous loops, or sound effects.
- Titles and dividers auto-play; evidence appears on click; results follow.
- Chapter divider: giant number → schematic → title plate → tagline, all fades.
- Content pages: title auto → evidence on click → chain/rows → result.
- TOC: heading auto → rows sequentially wipe down → footer.
- Keep group IDs in `animations.json` aligned with SVG group IDs.
- Motion should disappear into the talk; if it calls attention to itself, remove it.

See [`references/animation-design.md`](references/animation-design.md).

---

## Content-driven palette

Colors are chosen from the **content**, not from a fixed brand palette.

### Selection method

1. Identify the deck's domain and tone: corporate, academic, product, culture,
   healthcare, education, finance, robotics, etc.
2. Pick one **primary field** color: the color the topic "owns".
3. Pick one **content background**: a light neutral or a dark field that gives
   the primary room to breathe.
4. Pick one **accent**: a warm/cool counterpoint used only for rules, numbers,
   and small keywords.
5. Derive one **muted** text color and one **divider** color.
6. Check contrast for text/background and on-primary pairs.
7. Keep the same five roles across every page. Do not introduce a new color per
   page.

### Palette recipes

| Topic | Primary | Background | Accent | Character |
| --- | --- | --- | --- | --- |
| Career / serious editorial | `#192F59` | `#F7FAFE` | `#C2A368` | Navy, cream, restrained gold |
| Corporate / consulting | `#12324A` | `#F6F8FA` | `#2F6B8F` | Navy, white, steel |
| Academic / humanities | `#6B2F3A` | `#F6F1E7` | `#A8763E` | Burgundy, cream, brass |
| Product / AI / robotics | `#0B1220` | `#F5F7FA` | `#38BDF8` | Charcoal, white, cyan |
| Culture / education | `#2F3A3F` | `#F4EFE6` | `#B23A2E` | Ink, rice paper, vermilion |
| Healthcare / life science | `#0F4C5C` | `#F5FAF9` | `#E07A5F` | Deep teal, white, coral |

These are starting points. Sample the actual deck imagery/brand when available;
do not force a recipe that fights the content.

### Applying a palette

Use `scripts/apply_palette.py` to recolor the structural templates:

```bash
python scripts/apply_palette.py \
  --palette presets/academic-warm.json \
  --src templates \
  --out ./my-deck/templates
```

The script maps the structural roles (primary, secondary, action, background,
accent, muted, divider, on-primary) and generates supporting tints for
gradients. Review the result; adjust tokens if a gradient or plate loses
contrast.

See [`references/palette-selection.md`](references/palette-selection.md).

---

## Decorative language (fixed)

Keep these devices, but recolor them with the palette:

- orbit rings and radial lines on cover/TOC/dividers
- giant single-character or chapter-number watermark
- accent rules and a thin accent border on the light title plate
- cream/light info band on the cover
- torn-paper schematic panel on dividers
- double accent chevrons on the divider plate
- handwritten tagline on dividers
- header/footer bands on content pages
- open rows and one large evidence field, not cards

Do not add unrelated birds, flowers, clouds, icon walls, tech grids on content
pages, or decorative English walls.

---

## Photo and evidence rules

- Real photos only on cover, content evidence pages, and closing.
- Chapter dividers: schematics only.
- Label a schematic as a schematic.
- Do not use network/generated images as fake project evidence.
- No invented metrics, awards, dates, or results.
- Distinguish 负责 / 参与 / 协作 / 正在探索.
- If a photo is missing, use a labeled schematic or text evidence.

---

## Working preferences

1. Inspect existing files before changing; report status first.
2. Do not recreate or overwrite completed work.
3. Back up before structural changes; keep earlier exports.
4. Batch changes; save between batches.
5. Do not overwrite an open PPTX (`~$*.pptx`).
6. Use Chinese for Chinese projects.
7. Deliver PPTX + PDF + preview/overview + notes + report paths.
8. Finish with quality checks; disclose warnings honestly.

See [`references/workflow-preferences.md`](references/workflow-preferences.md).

---

## Quality gates

```bash
python scripts/check_style.py "<project>" --palette presets/<chosen>.json
python "$PPT_MASTER_DIR/scripts/svg_quality_checker.py" "<project>" \
  --canonical-authoring --stage final --json
python "$PPT_MASTER_DIR/scripts/animation_config.py" validate "<project>"
python "$PPT_MASTER_DIR/scripts/finalize_svg.py" "<project>"
python "$PPT_MASTER_DIR/scripts/svg_to_pptx.py" "<project>"
```

Pass criteria:

- 0 blocking SVG errors
- viewBox `0 0 1280 720`
- no banned tags
- images resolve; no `<image>` on chapter dividers
- chosen palette roles are consistent; off-palette colors are warnings
- page count = notes count = animation slide keys
- PPTX postflight passed

Full checklist: [`references/checklist.md`](references/checklist.md).

---

## Templates and presets

- [`templates/cover-dark-editorial.svg`](templates/cover-dark-editorial.svg)
- [`templates/toc-dark-editorial.svg`](templates/toc-dark-editorial.svg)
- [`templates/chapter-divider-schematic.svg`](templates/chapter-divider-schematic.svg)
- [`templates/content-frame.svg`](templates/content-frame.svg)
- [`templates/closing-dark-editorial.svg`](templates/closing-dark-editorial.svg)
- [`presets/bluegray-example.json`](presets/bluegray-example.json)
- [`presets/corporate-navy.json`](presets/corporate-navy.json)
- [`presets/academic-warm.json`](presets/academic-warm.json)
- [`presets/product-dark.json`](presets/product-dark.json)
- [`presets/culture-ink.json`](presets/culture-ink.json)

Templates are structural examples in the approved blue-gray palette. Recolor
them with the chosen palette; do not redesign the geometry.

---

## References

- [`references/style-guide.md`](references/style-guide.md) — fixed structure +
  decorative rules
- [`references/animation-design.md`](references/animation-design.md) — fixed
  transition and object-motion pattern
- [`references/palette-selection.md`](references/palette-selection.md) — how to
  choose colors from content
- [`references/page-structure.md`](references/page-structure.md) — 15/9 pages,
  dividers, renumbering
- [`references/workflow-preferences.md`](references/workflow-preferences.md) —
  inspect/backup/batch/report
- [`references/decision-log.md`](references/decision-log.md) — feedback → rule
- [`references/checklist.md`](references/checklist.md) — final QA
- [`examples/`](examples/) — same structure, different topics and palettes

---

## Example request

> 用 signature-ppt-style 做一份 12 页的企业季度复盘。
> 结构、封面、目录、章节页和内容页骨架都按我的模板；颜色根据企业品牌来定。
> 每个章节都要衔接页，衔接页用示意图，不要放真实照片。
> 内容页大字号、少卡片、留白。最后给我可编辑 PPTX、PDF 和预览。

The structure stays; the palette comes from the content.
