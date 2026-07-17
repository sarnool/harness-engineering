# Skill: Partials Manager

## Purpose
Generate `header.html` and `footer.html` as shared partial files. These files are written once and referenced by every page. No page file may contain its own header or footer markup.

---

## Core Rule

**Single source of truth.** If the nav changes, only `header.html` changes. If the contact details change, only `footer.html` changes. No page file is touched for global layout updates.

---

## § header.html

### What Goes in the Header
- Site logo or name (linked to `index.html`)
- Primary navigation links (from the Site Map navigation order)
- Primary CTA button (the site's main action — e.g. "Book Now", "Get in Touch")
- Mobile hamburger toggle button (controlled by `main.js`)

### Active State Convention
The header partial cannot know which page it is on at build time (static HTML). Use this pattern:

Each nav link gets a `data-page` attribute matching the page filename:
```html
<a href="services.html" data-page="services">Services</a>
```

In `main.js`, the active state is set dynamically:
```js
// ── Active Nav Link ──
function initActiveNav() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('[data-page]').forEach(link => {
    if (link.dataset.page === currentPage.replace('.html', '')) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
  });
}
```

This means `aria-current="page"` and the `.active` class are applied at runtime — not hardcoded in the partial.

### Header Structure
```html
<header class="site-header" role="banner">
  <div class="container">
    <a href="index.html" class="site-logo" aria-label="[Site Name] — Home">
      [Site Name or Logo]
    </a>

    <nav class="site-nav" aria-label="Primary navigation">
      <ul class="nav-links" role="list">
        <li><a href="index.html" data-page="index">Home</a></li>
        <!-- one <li> per page in Site Map nav order -->
      </ul>
    </nav>

    <a href="[primary CTA url]" class="btn btn--primary nav-cta">
      [CTA Label]
    </a>

    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav"
            aria-label="Open navigation menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
```

### Header Rules
- The `<header>` element uses `role="banner"` for accessibility
- Logo always links to `index.html`
- Nav links use relative paths — correct for all pages at the same folder depth
- CTA button links to the most important conversion page
- Mobile nav toggle is a `<button>` — never an `<a>` or `<div>`
- No inline styles — all styling via `main.css` classes

---

## § footer.html

### What Goes in the Footer
- Site logo or name (linked to `index.html`)
- Short tagline or description (1–2 sentences from the knowledge file)
- Footer navigation (all pages — more complete than the header nav)
- Contact details (phone, email, address if applicable)
- Social media links (if present in the knowledge file)
- Copyright line with current year

### Footer Structure
```html
<footer class="site-footer site-footer--full" role="contentinfo">
  <div class="container">
    <div class="footer-grid">

      <div class="footer-brand">
        <a href="index.html" class="site-logo">[Site Name]</a>
        <p>[Short tagline or description from knowledge file]</p>
      </div>

      <nav class="footer-nav" aria-label="Footer navigation">
        <h3 class="footer-nav__heading">Pages</h3>
        <ul role="list">
          <!-- one <li> per page in Site Map -->
        </ul>
      </nav>

      <div class="footer-contact">
        <h3 class="footer-contact__heading">Contact</h3>
        <!-- contact details from knowledge file -->
      </div>

    </div>

    <div class="footer-bottom">
      <p class="footer-copyright">
        &copy; <span data-year></span> [Site Name]. All rights reserved.
      </p>
      <!-- social links if available -->
    </div>
  </div>
</footer>
```

The current year in the copyright line is set dynamically in `main.js`:
```js
// ── Footer Year ──
function initFooterYear() {
  document.querySelectorAll('[data-year]').forEach(el => {
    el.textContent = new Date().getFullYear();
  });
}
```

### Footer Rules
- The `<footer>` element uses `role="contentinfo"` for accessibility
- All contact details sourced verbatim from the knowledge file — nothing invented
- Social links open in a new tab with `target="_blank" rel="noopener noreferrer"`
- No inline styles — all styling via `main.css` classes
- Footer nav includes all pages, not just the primary nav items

---

## § Partial Include Convention

Partials are referenced in generated page templates using comment markers:

```html
<!-- include: partials/header.html -->
```
```html
<!-- include: partials/footer.html -->
```

These markers are source placeholders only and must be compiled before preview/runtime delivery.

Compile step:

```bash
python scripts/compile_includes.py
```

The agent must output `partials/header.html` and `partials/footer.html` as complete source files and ensure runtime pages in `output/*.html` contain rendered header/footer markup after compilation.

---

## § When to Regenerate Partials

Regenerate both partials when:
- A new page is added to the Site Map (nav links change)
- A page is removed or renamed
- Contact details in the knowledge file change
- The site logo or name changes
- Social media links are added or removed

Do **not** regenerate partials when:
- Page content changes (only the page file changes)
- CSS or JS changes
- Images are reassigned

---

## § Validation Checklist

- [ ] `partials/header.html` exists and contains a complete `<header>` element
- [ ] `partials/footer.html` exists and contains a complete `<footer>` element
- [ ] `scripts/compile_includes.py` exists
- [ ] Every page in the Site Map has a nav link in `header.html`
- [ ] Every page in the Site Map has a footer nav link in `footer.html`
- [ ] Include compilation has been run successfully
- [ ] Every runtime page in `output/*.html` contains `<header class="site-header">`
- [ ] Every runtime page in `output/*.html` contains `<footer class="site-footer">`
- [ ] No unresolved include markers remain in runtime pages
- [ ] `data-page` attributes match page filenames (without `.html`)
- [ ] `data-year` attribute present in footer copyright line
- [ ] No inline styles in either partial file
- [ ] All contact details match the knowledge file verbatim
