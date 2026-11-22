# Decision Log

A compact record of the user's feedback and how this skill encodes it. This is
the "why" behind the style guide.

| Feedback | Rule in this skill |
| --- | --- |
| 不要每页都是深蓝背景、规则卡片、科技边框 | Content pages use a light field; no card grids; dark fields reserved for cover/TOC/dividers/closing |
| 结构、装饰设计固定，颜色根据内容匹配 | Fixed geometry + decorative motifs; palette selected from topic/brand/imagery |
| 保持动画设计、页面布局、衔接页、字体和装饰 | Animation pattern, layout, typography, divider system, and decorations are fixed |
| 配色保持现有审美，但不要固定 | Same contrast/restraint/one-accent quality; hues are content-driven |
| 统一蓝灰色系，降低背景明暗反差 | Light content + dark header/footer bands; blue-gray is one example preset |
| 我想要参考 PPT 里的蓝色色调 | Blue-gray `#192F59/#094183/#50638A` kept as `bluegray-example`, not fixed globally |
| 第一版封面和目录设计保留 | Dark technical cover/TOC with orbit rings, giant watermark, gold rules |
| 第二版内容页设计保留 | Light content pages with 72 px navy header and 40 px navy footer |
| 章节衔接页要有参考图那种感觉 | Full-bleed navy, giant number, cream title plate, gold border, handwritten tagline, torn-paper panel |
| 衔接页不要用真实图片，用示意图 | Every chapter divider panel is a schematic; no `<image>` on divider pages |
| 五个章节都要衔接页 | Default 15-page roster includes five dividers |
| 大幅减少装饰元素 | No tech grids, dotted rings, icon walls, decorative English on content pages |
| 提高字号 | Title 44, subtitle 24, body 20–26, caption 16–19 |
| 减少内容碎片化 | ≤ 7 content units per page; open rows/columns/bands instead of cards |
| 金色只做少量强调 | Accent only for rules, borders, numbers, small keywords; gold is one example |
| 不要大量无意义英文小字 | English only as section translation or short labels |
| 不要用网络图片冒充项目成果 | Real photos only; schematics labeled; no fake evidence |
| 不要虚构数据/奖项 | Evidence rules: no invented metrics, awards, dates, or results |
| 先检查已有文件，不覆盖已完成内容 | Inspect/backup/non-destructive workflow |
| 从崩溃中断处继续，分批处理 | Batch/checkpoint workflow; inspect before restart |
| 完成后给可编辑 PPTX/PDF/预览 | Output contract: PPTX + PDF + preview + notes + reports |
| 不要覆盖正在打开的 PPTX | Check `~$*.pptx`; export new timestamped file |

## How to apply a new preference

When the user gives new visual feedback:

1. Add a row here (date/feedback/rule).
2. Update `style-guide.md` if the rule changes.
3. Update the chosen palette JSON in `presets/` if a token changes.
4. Update `SKILL.md` hard rules if the preference is non-negotiable.
5. Re-run `check_style.py` on the template library.

This keeps the skill as a living record of the user's taste, not a static theme.
