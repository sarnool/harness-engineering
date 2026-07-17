# Skill: Section Architecture

## Purpose
Decide which sections to build, in what order, and what content and image populates each one. Output a Section Blueprint.

---

## Step 1 — Section Selection Rules

Map each item in the Content Inventory to a section type. Use these rules:

| Content Available | Section to Include |
|---|---|
| Business name + tagline + primary CTA | Hero |
| About / bio summary | About |
| Services or offerings list | Services |
| Pricing or packages | Packages / Pricing |
| Team members | Team |
| Projects or portfolio items | Portfolio |
| Location + hours | Info / Visit |
| FAQs | FAQ |
| Contact details | Contact / Footer |
| Loyalty or membership | Loyalty / CTA Strip |
| Testimonials or social proof | Testimonials |
| Research or thought leadership | Research / Writing |
| Certifications or credentials | Credentials / Stack |

### Mandatory Sections
Every page must include:
- **Hero** — always first
- **Contact or Footer** — always last

### Section Count Limit
Maximum 8 sections per page (excluding nav and footer). If more content exists, consolidate or defer to subpages.

---

## Step 2 — Section Ordering Rules

Follow this priority order. Move sections up if they contain the primary CTA:

1. Hero
2. Social proof strip or marquee (if available — builds immediate trust)
3. Core value proposition section (Services, Portfolio, or About — whichever is most important)
4. Supporting sections (Team, Packages, Research)
5. Logistics sections (Hours, Location, FAQ)
6. Conversion section (Loyalty, CTA strip)
7. Footer / Contact

---

## Step 3 — Image Assignment

For each section in the blueprint, check the Image Assignment Map from `image-analyst.md`.
- If an image is assigned to this section: note the file path and placement style (background, split-layout, inline card, or full-width).
- If no image is assigned: mark as `[no image]`.

### Image Placement Styles
| Style | When to Use |
|---|---|
| `background` | Hero sections — image fills the section background with overlay |
| `split-layout` | About or feature sections — image on one side, text on the other |
| `inline-card` | Services or team grids — image inside a card component |
| `full-width` | Transition sections — image spans full width between content blocks |

---

## Output: Section Blueprint

Produce a blueprint in this format:

```
SECTION BLUEPRINT
─────────────────────────────────────────────
1. NAV
   Content: Logo, nav links, primary CTA button
   Image: [none]

2. HERO
   Content: [headline], [subheadline], [CTA buttons], [stat strip if available]
   Image: [filename] | Placement: background | Alt: [alt text]

3. [SECTION NAME]
   Content: [what goes here]
   Image: [filename or none] | Placement: [style]

...

N. FOOTER
   Content: [logo, links, contact details, social]
   Image: [none]
─────────────────────────────────────────────
```

This blueprint is the contract between Stage 2 and Stage 3. The HTML engineer must not deviate from it without user approval.
