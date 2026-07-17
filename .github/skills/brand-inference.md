# Skill: Brand Inference

## Purpose
Map the Content Brief and Image Assignment Map to a concrete Design Token Set. Every visual decision must be traceable to a signal from the content or images — no arbitrary choices.

---

## Step 1 — Colour Temperature

| Signal | Direction |
|---|---|
| Tone: Warm + Entity: Beauty/Wellness/Hospitality | Warm palette — blush, rose, terracotta, cream |
| Tone: Warm + Entity: Food/Lifestyle | Warm palette — amber, sage, warm white |
| Tone: Neutral + Entity: Professional Services | Neutral palette — slate, stone, off-white |
| Tone: Cool + Entity: Tech/Engineering/AI | Cool palette — dark navy, cyan, indigo, charcoal |
| Tone: Formal + Entity: Legal/Finance | Conservative — deep navy or charcoal, white, gold accent |
| Image mood contains "warm" or "welcoming" | Reinforce warm direction |
| Image mood contains "calm" or "restorative" | Soften the palette — avoid high contrast |
| Image mood contains "professional" or "organised" | Increase contrast, reduce saturation |

---

## Step 2 — Typography

| Signal | Font Style |
|---|---|
| Warm + Lifestyle/Beauty | Serif body (Georgia, Playfair) — elegant, personal |
| Tech/Engineering | Sans-serif (system-ui, Inter) — clean, modern |
| Professional Services | Serif headings + sans-serif body — authoritative but readable |
| Casual/Friendly tone | Rounded sans-serif — approachable |
| Technical complexity | Monospace accents — signals precision |

---

## Step 3 — Spacing & Density

| Signal | Spacing |
|---|---|
| Warm, relaxed tone | Generous whitespace — sections breathe |
| Professional, formal tone | Moderate whitespace — structured |
| Technical, data-heavy content | Tighter spacing — information density |

---

## Step 4 — Shape Language

| Signal | Border Radius |
|---|---|
| Warm/Lifestyle | Large radius (16–24px) — soft, friendly |
| Professional Services | Medium radius (8–12px) — approachable but structured |
| Tech/Engineering | Small radius (4–8px) or none — sharp, precise |

---

## Step 5 — Animation Style

| Signal | Animation |
|---|---|
| Warm/Lifestyle | Gentle transitions (200–300ms ease), subtle hover lifts |
| Tech/Engineering | Fade-ins, glows, terminal-style effects |
| Formal/Conservative | Minimal — transitions only, no decorative animation |

---

## Output: Design Token Set

Produce a token set in this format:

```
COLOURS:
  --bg-primary:     [hex]
  --bg-secondary:   [hex]
  --accent:         [hex]
  --accent-dark:    [hex]
  --text-primary:   [hex]
  --text-muted:     [hex]
  --border:         [hex or rgba]
  --white:          [hex]

TYPOGRAPHY:
  --font-body:      [font stack]
  --font-heading:   [font stack]
  --font-mono:      [font stack, if used]

SPACING:
  --space-section:  [px value for section padding]
  --space-card:     [px value for card padding]
  --space-gap:      [px value for grid gaps]

SHAPE:
  --radius-card:    [px]
  --radius-btn:     [px]

ANIMATION:
  --transition:     [e.g. 0.25s ease]
```

Every token must be used in the generated CSS. No hardcoded values in the HTML output.
