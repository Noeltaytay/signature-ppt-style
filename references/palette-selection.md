# Palette Selection

The structure is fixed; the palette is chosen from the content. Use this method
instead of defaulting to blue-gray.

## 1. Read the content first

Before choosing colors, identify:

- **Domain**: corporate, academic, product, culture, healthcare, education,
  finance, robotics, nonprofit, etc.
- **Tone**: serious, optimistic, technical, warm, premium, civic.
- **Existing brand**: logo, product UI, campaign, venue, or client guidelines.
- **Imagery**: hero photo, product screenshot, field site, artwork. Sample one
  dominant color from it.
- **Audience**: executives, judges, students, customers, public sector.
- **Delivery**: projected in a bright room, printed, or remote. Projection
  favors high contrast and darker fields.

## 2. Choose five roles

| Role | Question | Typical source |
| --- | --- | --- |
| `primary` | What color owns the topic? | Brand, industry, hero image |
| `secondary` | What quieter relative supports it? | A desaturated/tinted primary |
| `accent` | What one counterpoint draws the eye? | Complementary, warm/cool counterpoint |
| `background` | What field makes text easy to read? | Warm/cool neutral, not pure white |
| `text` / `muted` | What reads on the background? | Near-primary or neutral |

Do not choose five unrelated colors. A palette is a family with one accent.

## 3. Build the role set

Start from one primary, derive the rest:

- `secondary` = primary mixed with 15–30% neutral/white, or a neighboring hue.
- `background` = a very light tint of primary/neutral, or a deep neutral for a
  dark deck.
- `accent` = one hue 90–180° away from primary, or a warm metallic.
- `text` = primary darkened until contrast is ≥ 4.5:1 on background.
- `muted` = text mixed with background 30–45%.
- `divider` = background mixed with text 15–20%.
- `on_primary` = white/cream/near-white tested on primary.

## 4. Contrast gates

Minimum:

- body text / background: 4.5:1
- large title / background: 3:1
- on_primary / primary: 4.5:1
- accent / background: 3:1 for large text/graphics; 4.5:1 for small text
- chart colors: distinguishable by luminance, not hue alone

Use a contrast checker. Do not rely on the eye alone.

## 5. Apply to the fixed structure

Map roles to the structural elements:

| Structural element | Role |
| --- | --- |
| Cover/TOC/divider field | primary / dark_field |
| Content header/footer bands | primary |
| Content page background | background |
| Title/body text | text |
| Secondary text/captions | muted |
| Rules/borders/chevrons/numbers | accent |
| Title plate | background/surface |
| Info band | background/surface |
| Chart series | chart_palette |
| Supporting gradients/schematics | derived tints |

Use `scripts/apply_palette.py` to recolor the templates.

## 6. Recipe examples

### Corporate / consulting
- Primary `#12324A`
- Background `#F6F8FA`
- Accent `#B08D57`
- Character: navy, white, brass

### Academic / humanities
- Primary `#6B2F3A`
- Background `#F6F1E7`
- Accent `#A8763E`
- Character: burgundy, cream, brass

### Product / AI / robotics
- Primary `#0B1220`
- Background `#F5F7FA`
- Accent `#38BDF8`
- Character: charcoal, white, cyan

### Culture / education
- Primary `#2F3A3F`
- Background `#F4EFE6`
- Accent `#B23A2E`
- Character: ink, rice paper, vermilion

### Career / serious editorial
- Primary `#192F59`
- Background `#F7FAFE`
- Accent `#C2A368`
- Character: navy, cream, restrained gold

## 7. Avoid

- A fixed blue-gray palette on every deck.
- Rainbow charts with no hierarchy.
- Two accent hues competing for attention.
- Low-contrast gray-on-gray body text.
- White text on a mid-tone accent without a contrast check.
- Changing the page structure to accommodate a palette.

## 8. Record the choice

Create a `tokens.json` / palette JSON in the project:

```json
{
  "name": "project-palette",
  "source": "brand navy + brass from event identity",
  "colors": {
    "primary": "#12324A",
    "secondary": "#3E5C76",
    "action": "#2F6B8F",
    "background": "#F6F8FA",
    "surface": "#FFFFFF",
    "accent": "#B08D57",
    "text": "#142433",
    "muted": "#5C6B78",
    "divider": "#C9D4DD",
    "on_primary": "#F7FAFC"
  }
}
```

This keeps the color decision traceable when the deck is revised later.
