# Website Builder Harness — Prompt Catalog

Copy and paste these prompts to start a build. Replace values in `[brackets]`.

---

## Build Prompts

### Full Site Build
```
Build a website from the knowledge file at knowledge-files/[filename].
Follow the full workflow in AGENTS.md.
Start with Stage 1 (content analysis), Stage 2a (image intelligence), and Stage 2c (site architecture) before making any design decisions.
Present the Content Brief, Image Assignment Map, Site Map, Design Token Set, and Section Blueprints for my review before writing any files.
```

### Build Without Human Checkpoint
```
Build a website from the knowledge file at knowledge-files/[filename].
Follow the full workflow in AGENTS.md.
Use your best judgement at the human checkpoint and proceed automatically.
Scaffold the output folder, generate partials, CSS, JS, and all pages per the Site Map.
```

---

## Image Prompts

### Generate Missing Metadata
```
No image-metadata.txt exists in knowledge-files/assets/images/.
Scan all image files in that folder and generate the metadata file using the schema in skills/image-analyst.md.
List all images found and flag any entries that need human review.
```

### Sync New Images Into Metadata
```
Re-scan knowledge-files/assets/images/ and reconcile with knowledge-files/assets/images/image-metadata.txt.
Detect only newly added image files that are not already represented in metadata.
For each new file, follow skills/image-analyst.md Step 1 reconciliation rules:
- If not optimized, create <original_stem>_optimized<original_ext> using .github/tools/optimize_images.py.
- Update metadata to reference the optimized filename in File path.
- If an optimized sibling already exists and is in metadata, skip re-processing the original.
Do not reprocess or re-optimize previously tracked files.
Return a summary of added, skipped, and updated metadata entries.
```

### Review Image Assignments
```
Show me the Image Assignment Map for the current build.
Explain why each image was assigned to its section.
```

### Reassign an Image
```
Move [image filename] from [current section] to [target section].
Update the Section Blueprint and regenerate only the affected sections.
```

---

## Edit Prompts

### Add a Page
```
Add a new [page name] page to the site.
Use the content from knowledge-files/[filename] under the heading [heading name].
Follow skills/site-architect.md to update the Site Map.
Update partials/header.html to include the new nav link.
Generate the new [page-name].html using the standard page template from skills/html-engineer.md § Pages.
```

### Add a Section
```
Add a [section type] section to output/[page-name].html.
Use the content from knowledge-files/[filename] under the heading [heading name].
Select the appropriate component from skills/component-library.md.
Insert it between the [section A] and [section B] sections.
Add any new CSS classes needed to output/assets/css/main.css.
```

### Restyle the Site
```
Update the Design Token Set in output/assets/css/main.css.
New brand direction: [describe — e.g. "darker, more professional, navy and gold"].
Update the :root token values only. Do not change any HTML, layout, or content.
```

### Update Content
```
The knowledge file has been updated at knowledge-files/[filename].
Re-run Stage 1 (content analysis) only.
Identify what has changed and update only the affected sections across all pages in output/.
Do not regenerate CSS, JS, or partials unless the change requires it.
```

### Regenerate Partials
```
Regenerate output/partials/header.html and output/partials/footer.html
using the rules in skills/partials-manager.md.
The Site Map has changed: [describe change].
Do not modify any page HTML files or CSS.
```

---

## Diagnostic Prompts

### Explain Design Decisions
```
Explain every design decision made for this site build.
Reference the Content Brief, Site Map, Image Assignment Map, and Design Token Set.
```

### Run Validation
```
Run the full validation checklist from skills/html-engineer.md § Validation
across all files in output/.
List every failure and fix them before responding.
```

### Audit Images
```
Audit all image references across all HTML files in output/.
Verify each src matches image-metadata.txt exactly.
Verify each alt text matches the metadata verbatim.
Report any mismatches and fix them.
```

### Audit Partials
```
Verify that partials/header.html and partials/footer.html are correctly
referenced in every page in output/.
Check that no page contains duplicate header or footer markup.
Report any issues.
```