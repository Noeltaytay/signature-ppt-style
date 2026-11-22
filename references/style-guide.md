# Style Guide — Fixed Structure, Content-Driven Palette

This is the user's approved **structure and decoration language**. The geometry
and decorative motifs are fixed; the palette is chosen from the content.

## 1. The split

| Fixed | Variable |
| --- | --- |
| Page architecture | Primary field color |
| Canvas, margins, header/footer heights | Background color |
| Title/rule positions | Accent color |
| Type scale and families | Muted/divider colors |
| Cover/TOC/divider/closing compositions | Chart palette |
| Orbit field, giant watermark, accent rules, cream plate, torn panel, chevrons, info band | The actual hues |

Never redesign the skeleton when the palette changes. Recolor the same geometry.

## 2. Palette roles

Choose five roles from the content:

| Role | Meaning | Rule |
| --- | --- | --- |
| `primary` | Main field/header/footer/divider | The color the topic "owns" |
| `secondary` | Supporting structure | A quieter relative of primary |
| `accent` | Rules, borders, numbers, small keywords | One hue; small area only |
| `background` | Content page field | Light neutral or dark field; not pure white/near-black |
| `text` / `muted` | Primary/secondary text | ≥ 4.5:1 on background |
| `on_primary` | Text on primary | ≥ 4.5:1 |

Supporting tints for gradients and schematics are derived from these roles by
`scripts/apply_palette.py`.

### Example directions

- **Career / serious editorial**: navy `#192F59`, cream `#F7FAFE`, gold
  `#C2A368`.
- **Corporate / consulting**: navy `#12324A`, white `#F6F8FA`, steel/brass
  accent.
- **Academic / humanities**: burgundy `#6B2F3A`, cream `#F6F1E7`, brass
  `#A8763E`.
- **Product / AI / robotics**: charcoal `#0B1220`, white `#F5F7FA`, cyan
  `#38BDF8`.
- **Culture / education**: ink `#2F3A3F`, rice paper `#F4EFE6`, vermilion
  `#B23A2E`.

These are recipes, not a fixed palette. Sample the actual brand/imagery where
available.

## 3. Typography (fixed)

- Display/title: `Georgia, Source Han Serif SC Heavy, SimSun`
- Body: `Microsoft YaHei, Arial`
- Handwritten: `KaiTi, STKaiti, Microsoft YaHei`
- Display 84–96; title 44; subtitle 24; body 20–26; annotation 22;
  caption 16–19; micro 12–14; chapter number 420; stage numeral 56.
- No more than five sizes on one page.
- No all-caps English walls; English is a section translation or short label.

## 4. Content page frame (fixed)

- 1280×720.
- Header `0 0 1280 72`; footer `0 680 1280 40`.
- Margins 64.
- Header: name at `x=64`; nav from `x=250`; page number right at `x=1216`.
- Footer: source/boundary at `x=64`; page number right.
- Title rule at `x=64 y=112 w=48 h=2`; title baseline `y=168`;
  subtitle `y=206`.
- Active nav item: bright + accent underline (`y=64`, width 116).
- No card grid; open rows/columns/bands; ≤ 7 content units.

## 5. Cover (fixed composition)

- Navy/primary gradient field; orbit rings and sparse dots.
- Giant single-character watermark (or a short brand glyph).
- Accent rule + event line.
- Title 96 px serif, 2–3 lines; one line may use the accent.
- Subtitle + target role/positioning.
- Name, affiliation, tagline.
- Bottom light info band (748×64) with three columns.
- Right accent-framed image/schematic panel.
- Page number 12 px.

Colors follow the palette; the geometry and decorations stay.

## 6. TOC (fixed composition)

- Full-bleed primary field; orbit rings; giant section-count watermark.
- Left: “目录” 96 px + `CONTENTS` + route line.
- Right: five rows: number, title, English subtitle, one-line description,
  page marker.
- Active row: accent vertical bar + bright title.
- Page markers point to chapter dividers.

## 7. Chapter divider (fixed composition)

- Full-bleed primary field.
- Giant chapter number 420 px at `x=80 y=540`, low opacity.
- Light title plate at `x=84 y=294 w=604 h=224`; accent offset/border.
- Chinese title 96 px at `x=132 y=420`; English 22–24 px at `x=134 y=470`;
  two accent chevrons.
- Handwritten tagline 34 px at `x=110 y=600`.
- Right: torn-paper panel with a **schematic**.
- **No real photos/screenshots on dividers.**
- `PART 0X` and page number.

The plate uses the palette's `background`/`surface`; border/chevrons use
`accent`. Do not hardcode blue/gold.

## 8. Content page patterns (fixed information patterns)

- Capability matrix: five open rows; requirement/evidence/source.
- Project: one large evidence field + five-step chain + result.
- Research/competition: two columns; completed vs exploring.
- Internship: two rows; software vs hardware.
- Plan: three stages; bottom action band.
- Closing: one claim, identity, thanks.

## 9. Decorative language (fixed)

Keep:

- orbit rings and radial lines on cover/TOC/dividers
- giant watermark
- accent rules and a thin accent border on the light title plate
- cream/light info band on the cover
- torn-paper schematic panel on dividers
- double accent chevrons on the divider plate
- handwritten tagline
- header/footer bands on content pages
- open rows and one large evidence field

Do not add:

- card grids, icon walls, tech grids on content pages
- unrelated birds/flowers/clouds
- decorative English walls
- a second accent hue
- fake project photos or metrics

## 10. Why

The user rejected fixed dark pages, card grids, excessive decoration, small
type, and fragmented content. They approved the structure above but want the
palette to belong to each new topic. So: **structure fixed, color content-led**.
