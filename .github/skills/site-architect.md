# Skill: Site Architect

## Purpose
Decide whether the site is simple (single page) or complex (multi-page). If multi-page, define the Site Map — every page, its filename, nav label, and which content sections it contains. This decision is made before any section blueprinting or code generation.

---

## Step 1 — Complexity Assessment

Read the Content Brief from `content-analyst.md`. Count the number of distinct content categories in the Content Inventory.

Apply these rules:

| Condition | Decision |
|---|---|
| 3 or fewer content categories | Single page — all content on `index.html` |
| 4–6 content categories, all closely related | Single page with clear section anchors |
| 4+ content categories where any category has enough depth to stand alone | Multi-page site |
| Any category contains a list of 5+ sub-items (e.g. services, projects, team) | That category gets its own page |
| Entity type is a portfolio or professional profile | Multi-page by default |
| Entity type is a local business with services + booking + team + location | Multi-page by default |
| User has explicitly requested single or multi-page | Honour that request regardless of content volume |

---

## Step 2 — Page Definition (Multi-Page Only)

For each page, define:

- **Filename** — lowercase, hyphenated, `.html` extension (e.g. `services.html`)
- **Page title** — used in `<title>` and `<h1>`
- **Nav label** — short label for the navigation link (max 2 words)
- **Content sections** — which items from the Content Inventory belong on this page
- **Primary CTA** — the main action on this page

### Standard Page Set (adapt as needed)

| Page | Filename | Typical Content |
|---|---|---|
| Home | `index.html` | Hero, highlights, key services summary, team teaser, CTA |
| Services / Work | `services.html` | Full services list with pricing, categories, detail |
| About | `about.html` | Bio/story, team, values, credentials |
| Portfolio / Projects | `portfolio.html` | Project cards, case studies, outcomes |
| Contact / Visit | `contact.html` | Contact form, hours, location, map, transport |
| Blog / Research | `blog.html` | Articles, thought leadership, research summaries |
| Packages | `packages.html` | Bundles, pricing tiers, membership |

Only include pages that have sufficient content to justify them. Do not create empty or thin pages.

---

## Step 3 — Navigation Structure

Define the primary navigation:
- Order pages by visitor priority (most important first)
- Maximum 6 nav items (including Home)
- If more than 6 pages exist, group secondary pages under a dropdown or omit from primary nav
- Every page must be reachable from the nav or from a link on another page — no orphan pages

---

## Step 4 — Cross-Page Linking

Identify where pages should link to each other:
- Home hero CTA → most important action page
- Home service summary cards → Services page
- Home team teaser → About page
- Services page → Contact/Booking page
- Footer → all pages

Document these links in the Site Map so the HTML engineer can wire them correctly.

---

## Step 5 — Image Distribution

Review the Image Assignment Map from `image-analyst.md`. For multi-page sites, distribute images across pages:
- Each page should have at least one image if available
- The strongest hero image goes on `index.html`
- Service/process images go on the Services page
- People images go on the About or Team page
- Do not use the same image on more than one page

Update the Image Assignment Map to reflect which image goes on which page and section.

---

## Output: Site Map

Produce the Site Map in this format:

```
SITE MAP
─────────────────────────────────────────────
Type: [Single Page | Multi-Page]
Total pages: [N]

Pages:
─────────────────────────────────────────────
1. HOME
   Filename: index.html
   Title: [Page title]
   Nav label: Home
   Sections: [list from Content Inventory]
   Primary CTA: [action]
   Images: [filename → section]
   Links to: [other pages]

2. [PAGE NAME]
   Filename: [filename].html
   Title: [Page title]
   Nav label: [label]
   Sections: [list]
   Primary CTA: [action]
   Images: [filename → section]
   Links to: [other pages]

...
─────────────────────────────────────────────
Navigation order: Home | [Page] | [Page] | ... | Contact
─────────────────────────────────────────────
```

The Site Map is the contract for all subsequent stages. No page may be added or removed after the human checkpoint without explicit user approval.
