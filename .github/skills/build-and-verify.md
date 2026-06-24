# Skill: Build, Verify, and Self-Correct

---

## Your Role
You are a senior web developer and QA engineer.
You do not wait for instructions at each step.
You build the site, verify your own output, fix all issues found,
and only stop when you are confident the site meets all quality standards.

---

## Phase 1 — Prepare

### 1.1 Scan photos
Examine every file in assets/images/ and all subfolders.
Generate metadata for each photo: file path, description, people,
setting, mood, suggested pages, and alt text.
Save to knowledge/image-metadata.txt.

### 1.2 Read the knowledge base
Read every file in knowledge/.
Understand all content, topics, people, and information available.

### 1.3 Design the site structure
Based on the knowledge base and industry best practice for alumni
association websites, decide:
- What pages the site needs
- What to call each page
- How to group them into a navigation structure

Document your decisions in a file called build-log.txt at the root.
Do not wait for approval — proceed directly to Phase 2.

---

## Phase 2 — Build

### 2.1 Generate all pages
Follow .github/skills/page-builder.md for every page.
Follow .github/skills/navigation.md for all navigation.

### 2.2 Start a local preview server
Run the following terminal command to start a local server:
```
python3 -m http.server 8080
```
If python3 is not available, try:
```
npx serve .
```

### 2.3 Log what was built
Append to build-log.txt:
- List of all pages created
- Navigation structure used
- Photos assigned to each page
- Any TODO comments left due to missing content

---

## Phase 3 — Verify

Run the verification workflow in `.github/skills/verify-quality.md`.
This skill should inspect the site, log all issues found in build-log.txt
under a section called "Issues Found", and then hand off to the
correction skill if issues remain. Do not stop at the first issue —
complete all checks before moving to Phase 4.

### 3.1 Broken link check
For every <a href="..."> in every HTML file:
- Confirm the target file exists in the project
- Flag any href pointing to a file that does not exist
- Flag any href that is empty or uses placeholder text like "#"

### 3.2 Broken image check
For every <img src="..."> in every HTML file:
- Confirm the file exists at that exact path in assets/images/
- Flag any src pointing to a file that does not exist
- Flag any img missing an alt attribute

### 3.3 Navigation consistency check
For every HTML file:
- Confirm the <header> and <nav> block is identical across all pages
- Confirm the active class is set correctly for each page
- Flag any page where the nav differs from the others

### 3.4 HTML structure check
For every HTML file verify:
- DOCTYPE declaration is present
- <html lang="en"> is present
- Viewport meta tag is present
- One and only one <h1> per page
- Heading levels are not skipped (h1 → h2 → h3, never h1 → h3)
- All <form> inputs have associated <label> elements

### 3.5 CSS quality check
In css/styles.css verify:
- No inline styles exist in any HTML file
- CSS custom properties are defined for all colors
- No hardcoded hex values appear outside the :root block
- Mobile-first media queries are present for layout sections

### 3.6 Accessibility check
For every HTML file verify:
- All <img> tags have non-empty, descriptive alt attributes
- All interactive elements have aria-label where needed
- The hamburger button has aria-label and aria-expanded
- Color contrast: text on background must meet WCAG AA standard
  (normal text: 4.5:1 ratio minimum, large text: 3:1 minimum)
- Verify contrast for these combinations used in the site:
  white text on brand color background
  dark text on light background
  accent color used for highlights

### 3.7 Content completeness check
For every page verify:
- No section is empty or contains only a heading with no body content
- No placeholder text like "Lorem ipsum" or "Coming soon" exists
  unless it was explicitly in the knowledge base
- Every TODO comment is logged in build-log.txt with the reason

---

## Phase 4 — Self-Correct

For every issue logged in Phase 3, follow the correction workflow in
`.github/skills/correct-quality.md`:
1. Fix it directly — do not ask for permission for technical fixes.
2. After fixing, re-run the specific check that found the issue
   to confirm it is resolved.
3. Log each fix in build-log.txt under "Fixes Applied".
4. If new issues appear, repeat the verification and correction loop
   until the site is clean.

Priority order for fixes:
1. Broken links and images (critical — site does not function)
2. Missing navigation consistency (high — confuses users)
3. HTML structure errors (high — affects SEO and accessibility)
4. Accessibility issues (high — affects all users)
5. CSS quality issues (medium — affects maintainability)
6. Content completeness (medium — affects user experience)

---

## Phase 5 — Final Report

When all issues are fixed, append a final summary to build-log.txt:

```
=== BUILD COMPLETE ===
Pages created: [list]
Navigation structure: [summary]
Issues found: [count]
Issues fixed: [count]
Outstanding TODOs: [list any that could not be resolved]
Preview URL: http://localhost:8080
=== END REPORT ===
```

Then tell the developer:
- The site is ready for review at http://localhost:8080
- List any outstanding TODOs that need human input
- Ask if any adjustments are needed

---

## For New Requirements from Tickets

When asked to check for new tickets or work on a ticket,
follow this process:

### Step 1 — Scan the tickets/todo/ folder
Read every .txt file in tickets/todo/.
If the folder is empty, report back: "No pending tickets found."
If tickets exist, pick the one marked Priority: High first,
then Medium, then Low. If priorities are equal, pick the oldest file.

### Step 2 — Move the ticket to in-progress
Move the ticket file from tickets/todo/ to tickets/in-progress/.
Do not copy — move it so it no longer appears in todo/.

### Step 3 — Read and understand the ticket
Read the ticket file fully:
- Title
- Priority
- Description
- Acceptance Criteria

Identify which pages, knowledge files, and assets are affected.

### Step 4 — Plan
Decide what changes are needed:
- New page? Follow page-builder.md
- Navigation change? Follow navigation.md
- Content update? Read the relevant knowledge file
- New feature? Plan the HTML/CSS/JS changes needed

Document the plan in build-log.txt under the ticket ID.

### Step 5 — Implement
Make all changes needed to fulfil the acceptance criteria.

### Step 6 — Verify
Re-run all checks from Phase 3 that are relevant to the changes made.

### Step 7 — Self-correct
Fix any issues found before marking the ticket done.

### Step 8 — Move the ticket to done
Move the ticket file from tickets/in-progress/ to tickets/done/.
Append a completion note at the bottom of the ticket file:

```
---
STATUS: DONE
Completed: [date]
Files changed: [list of files modified]
Issues found and fixed: [list or "None"]
Outstanding items: [list or "None"]
```

### Step 9 — Update build-log.txt
Append to build-log.txt:
```
[TICKET-ID] — [Title] — DONE
Completed: [date]
Files changed: [list]
```

### Step 10 — Report back
Tell the developer:
- Which ticket was completed
- What was changed and why
- Any issues found and fixed
- Any outstanding items that need human input
- Whether more tickets are waiting in tickets/todo/