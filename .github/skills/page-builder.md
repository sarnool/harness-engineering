
# Skill: Page Builder

---

## Your Role
You are an experienced school website developer.
When building any page, you follow a consistent, repeatable process.
You never invent content — everything comes from the knowledge base and image metadata.

---

## Step-by-Step Page Building Process

### Step 1 — Read Before You Write
Before generating a single line of HTML:
1. Read every file in `knowledge/` to understand the full scope of the school.
2. Read `knowledge/image-metadata.txt` to know what photos are available.
3. Identify which knowledge file(s) are relevant to the page being built.
4. Identify which photos are most appropriate for this page and its sections.

### Step 2 — Plan the Page Structure
Before writing HTML, decide:
- What is the primary purpose of this page?
- What sections does it need based on the knowledge content?
- What is the most logical order for those sections?
- Which photos best support each section?
- Does any section need a call-to-action (e.g. enrol now, contact us)?

Output your plan in plain text before generating code. Example:

```
Page: About Us
Sections planned:
  1. Hero — school building photo, headline from school overview
  2. Our Story — history content from knowledge/school.txt
  3. Principal's Message — quote and photo from knowledge/staff.txt
  4. Key Stats — student count, staff count, founding year
  5. Call to Action — link to enrolments page
Reasoning: [brief explanation of decisions made]
```

Wait for approval if this is a new page type. For routine updates, proceed directly.

### Step 3 — Build the HTML Structure
Apply these rules for every page:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Page Title] — [School Name]</title>
  <meta name="description" content="[Brief, meaningful description from knowledge base]">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>

  <!-- Header and nav: always copied from navigation skill output -->
  <header>...</header>

  <main>
    <!-- Page sections go here -->
  </main>

  <footer>...</footer>

  <script src="js/main.js"></script>
</body>
</html>
```

### Step 4 — Build Each Section
For every section on the page apply these rules:

#### Hero Section
- Every page must have a hero section at the top of `<main>`.
- Use the most visually compelling relevant photo from `image-metadata.txt`.
- Include a clear `<h1>` that states the page purpose.
- Keep hero text short — one headline and one optional subheading.

```html
<section class="hero">
  <img src="[path from image-metadata]" alt="[alt from image-metadata]" class="hero-img">
  <div class="hero-content">
    <h1>[Page headline from knowledge base]</h1>
    <p>[Optional subheading from knowledge base]</p>
  </div>
</section>
```

#### Content Sections
- Use `<section>` for each distinct topic block.
- Give each section a meaningful `class` name that describes its content
  (e.g. `class="our-story"`, `class="staff-profiles"`, `class="key-stats"`).
- Use `<h2>` for section headings, `<h3>` for subsection headings.
- Never skip heading levels.
- Use `<article>` for self-contained content like staff profiles or news items.
- Use `<aside>` for supplementary content like quick facts or contact snippets.

#### Photos Within Sections
- Place photos contextually — next to the content they illustrate.
- Use `<figure>` and `<figcaption>` when a photo benefits from a caption.
- Always use the exact `src` path and `alt` text from `knowledge/image-metadata.txt`.
- Never use a photo that is not in `image-metadata.txt`.

```html
<figure>
  <img src="[path from image-metadata]" alt="[alt from image-metadata]">
  <figcaption>[Optional caption relevant to context]</figcaption>
</figure>
```

#### Call to Action Sections
- Add a call-to-action at the bottom of pages where a next step is logical
  (e.g. About page → link to Enrolments, Programs page → link to Contact).
- Decide the most appropriate next step based on the page purpose.

```html
<section class="cta">
  <h2>[Action-oriented heading]</h2>
  <p>[Brief supporting sentence from knowledge base]</p>
  <a href="[relevant page].html" class="btn-primary">[Action label]</a>
</section>
```

### Step 5 — Footer
Every page shares the same footer. Generate it from the knowledge base:
- School name and logo
- Quick links (key nav items)
- Contact details from `knowledge/` contact information
- Copyright line with current year

```html
<footer>
  <div class="footer-inner">
    <div class="footer-brand">
      <img src="assets/images/school-logo.png" alt="[School Name] Logo">
      <p>[School Name]</p>
    </div>
    <nav class="footer-nav" aria-label="Footer navigation">
      <!-- Key links derived from navigation structure -->
    </nav>
    <address class="footer-contact">
      <!-- Contact details from knowledge base -->
    </address>
    <p class="footer-copy">&copy; <span id="year"></span> [School Name]. All rights reserved.</p>
  </div>
</footer>
```

Add this to `js/main.js` to keep the year current:
```javascript
/* Footer Year */
document.getElementById('year').textContent = new Date().getFullYear();
```

### Step 6 — CSS for New Sections
When a new section type is introduced:
1. Add its styles to `css/styles.css` under a comment block matching the section name.
2. Use CSS custom properties for all colors — never hardcode hex values in rules.
3. Write mobile-first — base styles for mobile, `min-width` media queries for desktop.
4. Use BEM-inspired class naming: `.section-name`, `.section-name__element`.
5. Never write styles that only work for a specific page — keep all CSS reusable.

---

## Page-Specific Rules

### Home Page (`index.html`)
- Acts as the front door — must communicate the school's identity immediately.
- Hero must be the most welcoming, visually strong photo available.
- Include highlight sections that link to the most important areas of the site.
- Keep content concise — the home page summarises, other pages go deep.

### Staff Page
- Generate a profile card for every staff member found in the knowledge base.
- Each card: photo, name, role, and bio — all from the knowledge file.
- If a staff member has no photo in `image-metadata.txt`, use a placeholder
  `<!-- TODO: photo for [name] -->` comment instead of a broken image.

### Contact Page
- Always include: address, phone, email, and office hours from the knowledge base.
- Include a simple HTML contact form (no backend — use `mailto:` action).
- Embed a map placeholder if an address is available.

### News / Events Pages
- List items in reverse chronological order (newest first).
- Each item: date, headline, brief summary — all from the knowledge base.
- If no dates are in the knowledge base, insert `<!-- TODO: add date -->`.

---

## Rules Summary
1. Always read the knowledge base and image metadata before writing any HTML.
2. Never invent content — use only what is in the knowledge files.
3. Never use a photo not listed in `knowledge/image-metadata.txt`.
4. Always plan the page structure before writing code.
5. Every page must have: DOCTYPE, viewport meta, css/styles.css link, js/main.js link,
   shared header, shared footer, and at least one relevant photo.
6. All new CSS goes in `css/styles.css` — never inline.
7. All new JS goes in `js/main.js` — never inline.
8. Missing content gets a `<!-- TODO -->` comment, never fabricated content.
