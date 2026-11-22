# Templates

All templates are 1280×720 SVGs with `{{PLACEHOLDERS}}`. Replace every
placeholder before exporting; do not ship `{{...}}` in a final deck.

The bundled colors are the approved **blue-gray example**. The geometry and
decorations are the fixed part; recolor with a content-driven palette:

```bash
python scripts/apply_palette.py \
  --palette presets/academic-warm.json \
  --src templates \
  --out ./my-deck/templates
```

| File | Use |
| --- | --- |
| `cover-dark-editorial.svg` | Cover: orbit field, identity, info band, image panel |
| `toc-dark-editorial.svg` | Contents: five sections + page markers |
| `chapter-divider-schematic.svg` | Divider: giant number, light plate, schematic panel |
| `content-frame.svg` | Content page with header/footer bands |
| `closing-dark-editorial.svg` | Closing: one claim + identity |

## Placeholder map

### Cover
- `{{EVENT}}` — competition/event line
- `{{TITLE_LINE_1}}`, `{{TITLE_LINE_2}}`, `{{TITLE_LINE_3}}` — title lines
- `{{SUBTITLE}}` — supporting line
- `{{ROLE}}` — target role
- `{{NAME}}`, `{{AFFILIATION}}`, `{{TAGLINE}}`
- `{{INFO_1_LABEL}}`, `{{INFO_1_VALUE}}`, and 2/3
- `{{PANEL_LABEL}}`, `{{PANEL_CAPTION}}`
- `{{PAGE_NO}}`, `{{TOTAL_PAGES}}`

### TOC
- `{{ROUTE_LINE_1}}`, `{{ROUTE_LINE_2}}`
- `{{SECTION_01}}`…`{{SECTION_05}}`
- `{{SECTION_01_EN}}`…`{{SECTION_05_EN}}`
- `{{SECTION_01_DESC}}`…`{{SECTION_05_DESC}}`
- `{{PAGE_01}}`…`{{PAGE_05}}` — point to divider pages
- `{{AUDIENCE_OR_YEAR}}`, `{{EVENT}}`, `{{PAGE_NO}}`, `{{TOTAL_PAGES}}`

### Chapter divider
- `{{CHAPTER_LABEL}}` — 第一章/第二章
- `{{CHAPTER_TITLE}}` — 职业认知/岗位匹配/…
- `{{CHAPTER_EN}}` — CAREER AWARENESS/ROLE FIT/…
- `{{TAGLINE}}` — one short line
- `{{PART_NO}}`, `{{PAGE_NO}}`, `{{TOTAL_PAGES}}`, `{{EVENT}}`

The five-row schematic in the template is a placeholder pattern. Replace it with
a chapter-specific schematic; do not insert a real photo/screenshot.

### Content frame
- `{{CANDIDATE_NAME}}`, `{{NAV_01}}`…`{{NAV_05}}`
- `{{TITLE}}`, `{{SUBTITLE}}`, `{{BODY_PLACEHOLDER}}`
- `{{SOURCE_OR_BOUNDARY}}`, `{{PAGE_NO}}`, `{{TOTAL_PAGES}}`

### Closing
- `{{CLOSING_LINE_1}}`, `{{CLOSING_LINE_2}}`, `{{CLOSING_SUBTITLE}}`
- `{{NAME}}`, `{{ROLE}}`, `{{THANKS}}`
- `{{EVENT}}`, `{{PAGE_NO}}`, `{{TOTAL_PAGES}}`

## Use

1. Copy the template into a project's `svg_output/`.
2. Replace placeholders with real content.
3. Replace the dashed image placeholder with a real image or a labeled
   schematic.
4. Run `scripts/check_style.py` and the `ppt-master` quality gate.
5. Export PPTX and PDF.

If a placeholder is longer than the original text, reduce the font size or
reflow; do not let text leave the canvas or the plate.
