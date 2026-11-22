# signature-ppt-style

A personal Claude Code skill that packages the user's **PPT structure and
decoration language**, while letting the **palette follow the content**.

- **Fixed**: page architecture, layout geometry, typography, cover/TOC/
  chapter-divider/closing compositions, decorative motifs, and the animation
  pattern.
- **Variable**: primary, background, accent, muted, divider, and chart colors,
  chosen from the topic, industry, brand, and imagery.

This means a business review can be navy/steel, an academic defense can be
burgundy/cream, a product launch can be charcoal/cyan, and a career portfolio
can use the original blue-gray — while all decks share the same design DNA.

## What it fixes

- 15-page / 9-page architecture with chapter dividers
- 1280×720 canvas, 72 px header, 40 px footer, 64 px margins
- Large type: title 44, subtitle 24, body 20–26, caption 16–19
- Cover: split composition, orbit field, giant watermark, info band, framed panel
- TOC: five rows, route line, page markers to dividers
- Divider: giant chapter number, light title plate, accent chevrons, handwritten
  tagline, torn-paper **schematic** panel
- Content pages: open rows/columns/bands, no card grid, ≤ 7 units
- Closing: full-bleed field, one claim, identity, framed panel
- Animation: Fade transitions, title auto → evidence click → result, divider
  four-step fade, no fly/bounce/spin
- Real photos only on cover/content evidence/closing; never on dividers

## What it does not fix

- the actual hues — those come from the content
- the number of chapters or pages beyond the default architecture
- the content itself

## Install

Copy the folder into:

```text
~/.claude/skills/signature-ppt-style/
```

or project scope:

```text
<project>/.claude/skills/signature-ppt-style/
```

On Windows:

```text
C:\Users\<you>\.claude\skills\signature-ppt-style\
```

Restart Claude Code or reload skills after copying.

## Use

> 用 signature-ppt-style 做一份 12 页的企业季度复盘。
> 结构按我的模板；颜色根据企业品牌来定。
> 每个章节都要衔接页，衔接页用示意图，不要放真实照片。

Or:

> 和上次职业规划 PPT 一样，这次做产品发布，颜色用深色科技风。

The skill reuses the structure and decoration, then chooses a palette that fits
the content.

## Palette recipes

| Preset | Topic | Character |
| --- | --- | --- |
| `bluegray-example.json` | Career / serious editorial | Navy, cream, restrained gold |
| `corporate-navy.json` | Corporate / consulting | Navy, white, steel |
| `academic-warm.json` | Academic / humanities | Burgundy, cream, brass |
| `product-dark.json` | Product / AI / robotics | Charcoal, white, cyan |
| `culture-ink.json` | Culture / education | Ink, rice paper, vermilion |

These are starting points, not a fixed palette. Sample the actual brand/imagery
when available.

## Recolor the structural templates

```bash
python scripts/apply_palette.py \
  --palette presets/academic-warm.json \
  --src templates \
  --out ./my-deck/templates
```

The script preserves the geometry and decorative language, and maps the
semantic roles to the chosen palette. Review gradients and contrast afterward.

## Templates

- `templates/cover-dark-editorial.svg`
- `templates/toc-dark-editorial.svg`
- `templates/chapter-divider-schematic.svg`
- `templates/content-frame.svg`
- `templates/closing-dark-editorial.svg`

All are anonymized 1280×720 SVGs with `{{PLACEHOLDERS}}`. The bundled colors
are the approved blue-gray example; recolor with a palette.

## Examples

- `examples/business-review-outline.md`
- `examples/academic-defense-outline.md`
- `examples/product-launch-outline.md`
- `examples/career-portfolio-outline.md`

Each uses the same structure with a different palette direction.

## Dependency

A style/workflow overlay on [`ppt-master`](https://github.com/hugohe3/ppt-master)
(MIT). `ppt-master` handles SVG → native PPTX, images, notes, animations, and
postflight. This package handles structure, decoration, palette selection, and
working preferences.

## Privacy

Templates use placeholders only. Do not publish real names, schools, photos,
client data, or confidential project details.

## License

MIT. See `LICENSE`.

`ppt-master` is a separate project by Hugo He, also MIT; this repository does not
vendor or relicense its source.
