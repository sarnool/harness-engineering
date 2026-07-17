# Skill: Component Library

## Purpose
A catalogue of named, reusable section components. The HTML engineer selects from this library — it does not invent new patterns. Each component has a name, when to use it, image support notes, and key structural rules.

---

## Hero Variants

### `hero-fullscreen`
**Use when:** Strong hero image available with background placement.
**Image:** CSS `background-image` with dark overlay (`rgba(0,0,0,0.45)`). Text overlaid.
**Structure:** Full viewport height. Centred content. H1 + subheading + 2 CTA buttons. Optional stat strip at bottom.

### `hero-split`
**Use when:** No hero image, or image is better shown beside text.
**Image:** Right column `<img>` with `object-fit: cover`, fixed height.
**Structure:** Two-column grid. Text left, image right. H1 + subheading + CTAs.

### `hero-minimal`
**Use when:** Personal portfolio or text-heavy brand with no strong image.
**Image:** None, or small avatar/logo.
**Structure:** Centred text. Large H1. Subtle background gradient only.

---

## Navigation Variants

### `nav-sticky`
Sticky top nav with logo left, links centre/right, CTA button far right. Collapses to hamburger on mobile.

### `nav-simple`
Non-sticky. Logo left, links right. No CTA button. For simpler sites.

---

## Content Section Variants

### `section-grid-cards`
**Use when:** Multiple items of equal weight (services, features, team members).
**Image:** Optional inline card image at top of each card (`object-fit: cover`, fixed height).
**Structure:** Responsive CSS grid. `auto-fit, minmax(220px, 1fr)`. Card = icon/image + heading + body + optional CTA.

### `section-split-feature`
**Use when:** One key feature or about section with a strong image.
**Image:** Split layout — image one side, text other. Alternates on mobile to stack.
**Structure:** Two-column grid. Image column 45%, text column 55%.

### `section-full-width-image`
**Use when:** Transition between sections. Creates visual breathing room.
**Image:** Full-width, fixed height (400px desktop, 250px mobile). `object-fit: cover`. No text overlay.
**Structure:** Single `<figure>` element with `<figcaption>` if caption needed.

### `section-list-detail`
**Use when:** Pricing tables, hours, FAQs, or any structured data.
**Image:** None typically. Focus is on information clarity.
**Structure:** Two-column layout — labels left, values right. Or accordion for FAQs.

### `section-highlight-strip`
**Use when:** Stats, key numbers, or loyalty/membership callout.
**Image:** None. Background colour contrast instead.
**Structure:** Horizontal flex row of 3–5 stat blocks. Each: large number + label.

### `section-marquee`
**Use when:** Long list of tags, services, or keywords to communicate breadth.
**Image:** None.
**Structure:** Infinite scroll animation. Two copies of content for seamless loop.

### `section-cta-banner`
**Use when:** Conversion moment — loyalty signup, booking prompt, contact push.
**Image:** Optional background image with overlay, or solid accent colour.
**Structure:** Centred heading + body + 1–2 buttons.

---

## Team Variants

### `team-grid`
Cards in a responsive grid. Each card: avatar/photo + name + role + short bio.
**Image:** Inline card image if team photos available. Emoji or initial avatar if not.

### `team-list`
Horizontal list of names and roles. Minimal. No photos.

---

## Footer Variants

### `footer-full`
Multi-column. Logo + description left. Link columns centre. Contact details right. Copyright bar at bottom.

### `footer-minimal`
Single row. Logo left. Links centre. Copyright right.

---

## CSS Class Conventions

Every component maps to a CSS class in `main.css`. The HTML engineer uses these class names — never writes inline styles.

| Component | Root CSS Class |
|---|---|
| `hero-fullscreen` | `.hero.hero--fullscreen` |
| `hero-split` | `.hero.hero--split` |
| `hero-minimal` | `.hero.hero--minimal` |
| `nav-sticky` | `.site-nav.site-nav--sticky` |
| `section-grid-cards` | `.section-cards` |
| `section-split-feature` | `.section-split` |
| `section-full-width-image` | `.section-image-break` |
| `section-list-detail` | `.section-list` |
| `section-highlight-strip` | `.section-stats` |
| `section-marquee` | `.section-marquee` |
| `section-cta-banner` | `.section-cta` |
| `team-grid` | `.team-grid` |
| `team-list` | `.team-list` |
| `footer-full` | `.site-footer.site-footer--full` |
| `footer-minimal` | `.site-footer.site-footer--minimal` |

All component styles are defined in `main.css`. No component styles belong in page files.

---

## Selection Guide

The Section Blueprint specifies which section type is needed. Match it to a component here:

| Blueprint Section | Component to Use |
|---|---|
| Hero (image available) | `hero-fullscreen` or `hero-split` |
| Hero (no image) | `hero-minimal` |
| Services / Features | `section-grid-cards` |
| About / Feature highlight | `section-split-feature` |
| Team | `team-grid` |
| Packages / Pricing | `section-grid-cards` or `section-list-detail` |
| FAQ | `section-list-detail` (accordion) |
| Hours / Location | `section-list-detail` |
| Loyalty / CTA | `section-cta-banner` |
| Stats / Numbers | `section-highlight-strip` |
| Keyword/tag list | `section-marquee` |
| Image transition | `section-full-width-image` |
| Footer | `footer-full` or `footer-minimal` |