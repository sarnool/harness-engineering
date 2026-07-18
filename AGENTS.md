# Website Builder Harness — Orchestration

This file is the mandatory workflow controller. The agent must follow every stage in order. Do not skip stages. Do not write any output files before completing Stages 1–3 and passing the human checkpoint.

---

## Mandatory Build Workflow

```
Stage 1  → Content Analysis        (skills/content-analyst.md)
Stage 2a → Image Intelligence      (skills/image-analyst.md)
Stage 2b → Brand Inference         (skills/brand-inference.md)
Stage 2c → Site Architecture       (skills/site-architect.md)
Stage 2d → Section Architecture    (skills/section-architecture.md)
Stage 2e → Component Selection     (skills/component-library.md)
── HUMAN CHECKPOINT ──
Stage 3a → Project Scaffolding     (skills/html-engineer.md § Scaffolding)
Stage 3b → Partials Generation     (skills/partials-manager.md)
Stage 3c → Shared CSS Generation   (skills/html-engineer.md § CSS)
Stage 3d → Shared JS Generation    (skills/html-engineer.md § JS)
Stage 3e → Page Generation         (skills/html-engineer.md § Pages)
Stage 4  → Validation              (skills/html-engineer.md § Validation)
```

---

## Stage Descriptions

### Stage 1 — Content Analysis
Load `skills/content-analyst.md`. Read all files in `knowledge-files/`. Produce a **Content Brief** covering: entity type, audience, tone signals, content inventory, and priority message.

### Stage 2a — Image Intelligence
Load `skills/image-analyst.md`.
- Always re-scan `knowledge-files/assets/images/` and reconcile with `knowledge-files/assets/images/image-metadata.txt`.
  - **If metadata exists:** parse it, detect new image files missing from metadata, and append entries for new images.
  - **If metadata does not exist:** scan all images and create metadata using the schema in `skills/image-analyst.md`.
- For each newly detected image file:
  - If a sibling `<original_stem>_optimized<original_ext>` exists and that optimized file is in metadata, treat the original as already handled and skip it.
  - Check whether it is already optimized.
  - If not optimized, create one optimized file named `<original_stem>_optimized<original_ext>` in the same folder.
  - Update metadata to reference the optimized filename in `File path` for that new image.
  - Do not add the unoptimized original file to metadata when an optimized sibling exists.
  - Do not bulk-optimize existing images already tracked in metadata.
- Produce an **Image Assignment Map**: a list of which images will be used in which sections and why.

### Stage 2b — Brand Inference
Load `skills/brand-inference.md`. Using the Content Brief and Image Assignment Map, produce a **Design Token Set**: colour palette, typography, spacing scale, border radius, and animation style.

### Stage 2c — Site Architecture
Load `skills/site-architect.md`. Using the Content Brief, decide:
- Whether the site is **simple** (single page) or **complex** (multi-page)
- If multi-page: which pages to create, what content goes on each, and how they link together
- Produce a **Site Map** listing every page with its filename, title, nav label, and content sections

### Stage 2d — Section Architecture
Load `skills/section-architecture.md`. For **each page** in the Site Map, produce a **Section Blueprint**: an ordered list of sections, the content that populates each, and which image (if any) is assigned to each section.

### Stage 2e — Component Selection
Load `skills/component-library.md`. For each section across all pages, select the appropriate named component variant.

---

## Human Checkpoint

Before writing any files, present the following to the user for review:
1. Content Brief (summary)
2. Image Assignment Map
3. Design Token Set
4. Site Map (pages, filenames, nav labels)
5. Section Blueprint per page with component selections

Ask: *"Does this plan look right? Any changes before I build?"*

Only proceed to Stage 3 after explicit user confirmation.

---

### Stage 3a — Project Scaffolding
Load `skills/html-engineer.md § Scaffolding`. Create the full output folder structure before writing any file content.

### Stage 3b — Partials Generation
Load `skills/partials-manager.md`. Generate `partials/header.html` and `partials/footer.html`. These are generated once and referenced by every page. Do not duplicate header or footer content inside individual page files.

### Stage 3c — Shared CSS Generation
Load `skills/html-engineer.md § CSS`. Generate `assets/css/main.css` containing all design tokens, base styles, layout utilities, and component styles. No page file may contain a `<style>` block.

### Stage 3d — Shared JS Generation
Load `skills/html-engineer.md § JS`. Generate `assets/js/main.js` containing all interactive behaviour. No page file may contain a `<script>` block or inline event handlers.

### Stage 3e — Page Generation
Load `skills/html-engineer.md § Pages`. Generate each `.html` page file per the Site Map. Each page links to the shared CSS and JS, and assembles the header and footer partials via the include pattern defined in `skills/partials-manager.md`.

### Stage 4 — Validation
Run the full validation checklist in `skills/html-engineer.md § Validation` across all generated files before delivering output.

---

## Output File Locations

| Purpose | Path |
|---|---|
| Knowledge files | `knowledge-files/` |
| Image assets | `knowledge-files/assets/images/` |
| Image metadata | `knowledge-files/assets/images/image-metadata.txt` |
| Generated pages | `output/` |
| Shared CSS | `output/assets/css/main.css` |
| Shared JS | `output/assets/js/main.js` |
| Partials | `output/partials/header.html` `output/partials/footer.html` |
| Build state | `STATUS.md` |
| Decision log | `DECISIONS.md` |

---

## Source File Locations

| Purpose | Path |
|---|---|
| Knowledge files | `knowledge-files/` |
| Image assets | `knowledge-files/assets/images/` |
| Image metadata | `knowledge-files/assets/images/image-metadata.txt` |
| Build state | `STATUS.md` |
| Decision log | `DECISIONS.md` |

---

## Entry Points

Use prompts from `PROMPTS.md`. Do not begin a build without a valid entry-point prompt.