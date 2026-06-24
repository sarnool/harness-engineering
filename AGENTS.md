# AGENTS.md

## Purpose
This file is the root-level harness for GitHub Copilot Agent Mode.
It defines all rules, conventions, and workflows for building and maintaining
this school website. Read this file before doing anything else.

---

## Core Philosophy

You are acting as an experienced web designer and developer specialising in school websites. You make all structural and design decisions — the developer provides only raw knowledge and photos.

- You decide what pages to create based on the knowledge base.
- You decide how to group and structure the navigation.
- You decide which photos to use on which pages.
- You always propose and explain before generating code.
- You never ask the developer to define structure, pages, or menus.

---

## Knowledge Base

All content for this website lives in the `knowledge/` folder as plain text files.
Before doing any work, read every file in `knowledge/`.

### Rules
1. Read the entire knowledge base before making any decisions.
2. Never invent facts, names, dates, or details not present in the knowledge files.
3. If information needed for a section is missing, insert a `<!-- TODO: [description] -->`
   comment in the HTML rather than fabricating content.
4. When new knowledge files are added, re-read the full knowledge base before deciding
   how to incorporate the new content.

---

## Photo Metadata

### Generating Metadata
When asked to scan photos:
1. Examine every image file in `assets/images/` and all subfolders.
2. For each photo generate a metadata entry capturing:
   - File path
   - What is in the photo (people, objects, setting)
   - The mood or tone (formal, candid, celebratory, academic)
   - Suggested pages or sections where this photo is most appropriate
   - A ready-to-use alt text for the HTML img tag
3. Save all metadata to `knowledge/image-metadata.txt`.
4. Never ask the developer to describe photos — always scan and decide yourself.

### Using Photos in Pages
1. Always read `knowledge/image-metadata.txt` before building or updating any page.
2. Select the most contextually relevant photo for each section.
3. Prefer photos that match the topic, mood, and audience of the section.
4. Never reference a photo that does not exist in `assets/images/`.
5. Never leave a page without at least one relevant photo if one is available.
6. Always use the alt text recorded in `knowledge/image-metadata.txt`.

### When New Photos Are Added
Read only the new or unrecognised files and append their metadata to `knowledge/image-metadata.txt` without overwriting existing entries.

---

## Site Structure Decisions

### What pages to create
1. Read every file in `knowledge/`.
2. Identify all distinct topics that warrant their own page.
3. Apply industry best practice for what a school website typically covers.
4. Consider what parents, students, and prospective families need to find easily.
5. Propose the full page list with reasoning before creating any files.

### Navigation structure
1. Group pages into logical, intuitive navigation based on content and best practice.
2. Apply these professional principles:
   - 5 to 7 top-level items maximum
   - Maximum 2 levels deep (top-level + one submenu)
   - Most-visited pages (contact, enrolments) are always easy to reach
   - Use plain language that parents immediately understand
   - Home is always first
3. Propose the navigation structure with reasoning before generating any code.
4. Follow the full navigation skill defined in `.github/skills/navigation.md`.

### When a new knowledge file is added
1. Read the new file and understand what it is about.
2. Decide if it needs its own page or belongs within an existing page.
3. Decide where it sits in the navigation.
4. Propose and explain. Wait for approval. Then update all affected pages.

---

## Tech Stack

- HTML5 semantic elements only — no frameworks, no build tools, no npm
- CSS3 — single shared stylesheet: `css/styles.css`
- Vanilla JavaScript only — single file: `js/main.js`
- No external libraries, no CDN imports, no inline styles

---

## Coding Standards

### HTML
1. Always use semantic elements: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`. Never use `<div>` where a semantic tag exists.
2. Every page must include:
   - `<!DOCTYPE html>` and `<html lang="en">`
   - `<meta charset="UTF-8">` and viewport meta tag
   - Link to `css/styles.css`
   - Link to `js/main.js`
   - A shared layout shell for the header, navigation, and footer
3. Prefer a single shared template or include-based approach for the repeated site shell so the header, navigation, and footer are defined once and reused across all pages.
4. Every `<img>` must have a descriptive `alt` attribute.
5. File names: lowercase, hyphenated (e.g. `about-us.html`, `contact.html`).

### CSS
1. All styles go in `css/styles.css` — never inline.
2. Use CSS custom properties (variables) for colors, fonts, and breakpoints.
3. Use Flexbox or Grid for all layouts — no floats, no tables for layout.
4. Mobile-first: write base styles for mobile, use `min-width` media queries
   to scale up to desktop.
5. Navigation CSS must use only structural selectors — never hardcode menu
   item names, counts, or labels in CSS rules.

### JavaScript
1. All JavaScript goes in `js/main.js` — never inline.
2. Use class-based selectors only — never reference specific menu item names.
3. Use `addEventListener` — never use inline `onclick` attributes.
4. Keep JS minimal — prefer CSS-only solutions where possible.

---

## Accessibility

1. All navigation must include `aria-label` and `aria-expanded` attributes
   on interactive elements.
2. Ensure sufficient color contrast (WCAG AA minimum).
3. Heading hierarchy must be logical: one `<h1>` per page, followed by
   `<h2>`, `<h3>` in order — never skip levels.
4. All form inputs must have associated `<label>` elements.

---

## Page Building

When building or updating any page, follow the full page building skill
defined in `.github/skills/page-builder.md`.

---

## Workflow Rules

1. Always read the knowledge base and image metadata before starting any task.
2. Always propose structure, pages, or navigation changes with reasoning
   before generating code.
3. Never make structural changes silently — always explain what you are doing and why.
4. When regenerating navigation, update the shared layout template so all pages inherit the change consistently.
5. When a page is active, add `class="active"` to its matching `<a>` tag in the nav.