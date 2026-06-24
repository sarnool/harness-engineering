
# PROMPTS.md — Complete Prompt Reference
# Cotton Collegiate Alumni Association Website
# Use these prompts in GitHub Copilot Agent Mode (VS Code)

---

## SECTION 1 — INITIAL PROJECT SETUP

### 1.1 Full Build (Run Once at the Start)
```
Follow the skill in .github/skills/build-and-verify.md completely.
Run all phases from start to finish without stopping for approval.
Build the full site, verify it, fix all issues found, and report
back with a summary when complete.
```

### 1.2 Scan Photos Only
```
Scan all photos in assets/images/ including all subfolders.
For each photo generate a metadata entry with: file path, description,
people, setting, mood, suggested pages, and alt text.
Save the result to knowledge/image-metadata.txt.
Do not build anything yet — just scan and report back.
```

### 1.3 Design the Site Structure Only (No Code)
```
Read every file in knowledge/ and knowledge/image-metadata.txt.
Based on the content and your expertise in alumni association websites,
propose the full site map and navigation structure with your reasoning.
Do not generate any code — wait for my feedback.
```

### 1.4 Build After Structure is Approved
```
The proposed structure is approved. Now build the full site following
.github/skills/build-and-verify.md from Phase 2 onwards.
Skip Phase 1 — photos are already scanned and structure is agreed.
```

---

## SECTION 2 — TICKET MANAGEMENT

### 2.1 Pick Up and Work on Next Ticket
```
Check tickets/todo/ for pending tickets and start work.
Follow the ticket workflow in .github/skills/build-and-verify.md.
Pick the highest priority ticket, implement it, verify it,
self-correct any issues, and report back when done.
```

### 2.2 Work on a Specific Ticket
```
Pick up ticket [CCAA-XXX] from tickets/todo/ and start work.
Follow the ticket workflow in .github/skills/build-and-verify.md.
Implement, verify, self-correct, and report back when done.
```

### 2.3 Check What Tickets Are Waiting
```
List all ticket files currently in tickets/todo/.
For each one show the ticket ID, title, and priority.
Do not start work — just report what is waiting.
```

### 2.4 Check What Is In Progress
```
List all ticket files currently in tickets/in-progress/.
For each one show the ticket ID, title, and how far along it is
based on any notes in the file.
```

### 2.5 Check What Has Been Completed
```
List all ticket files in tickets/done/.
For each one show the ticket ID, title, completion date,
and files that were changed.
```

### 2.6 Work Through All Pending Tickets
```
Check tickets/todo/ and work through all pending tickets one by one.
Start with the highest priority. After completing each ticket,
pick up the next one automatically until tickets/todo/ is empty.
Report a summary when all tickets are done.
```

---

## SECTION 3 — PAGE MANAGEMENT

### 3.1 Build a Single New Page
```
Build a new page for [topic] following .github/skills/page-builder.md.
Read the relevant knowledge files for content.
Read knowledge/image-metadata.txt for photos.
Run all verification checks after building and fix any issues found.
Report back when done.
```

### 3.2 Rebuild an Existing Page from Scratch
```
Rebuild [filename.html] completely from scratch.
Follow .github/skills/page-builder.md.
Use the latest content from the knowledge base and image metadata.
Keep the navigation unchanged.
Run all verification checks after rebuilding and fix any issues.
Report back when done.
```

### 3.3 Update a Page with New Content
```
Update [filename.html] with the latest content from knowledge/[filename].txt.
Do not change the page structure, navigation, header, or footer.
Only update the content sections.
Run verification checks after updating and fix any issues found.
```

### 3.4 Add a New Section to an Existing Page
```
Add a [section description] section to [filename.html].
Place it [after/before] the [existing section name] section.
Source the content from knowledge/[filename].txt.
Choose the most appropriate photo from knowledge/image-metadata.txt.
Add any new CSS to css/styles.css — no inline styles.
Run verification checks after adding and fix any issues found.
```

---

## SECTION 4 — NAVIGATION MANAGEMENT

### 4.1 Review and Update Navigation
```
Re-read the full knowledge base and review the current navigation.
Decide if any changes are needed based on the content that exists.
Propose any changes with reasoning.
Wait for my approval before making any changes.
```

### 4.2 Apply Approved Navigation Changes
```
The proposed navigation changes are approved.
Update the navigation structure following .github/skills/navigation.md.
Apply the updated header block to every HTML file in the project.
Verify navigation consistency across all pages after updating.
Fix any issues found and report back.
```

### 4.3 Add a New Page to the Navigation
```
A new page [filename.html] has been added to the site.
Decide where it belongs in the navigation based on its content
and industry best practice for alumni association websites.
Explain your reasoning, then update the header block on all pages.
Run navigation consistency checks and fix any issues found.
```

---

## SECTION 5 — CONTENT MANAGEMENT

### 5.1 Add New Knowledge and Decide What to Do With It
```
A new knowledge file has been added: knowledge/[filename].txt
Read it and decide:
1. Does it need its own page or does it belong within an existing page?
2. If existing page — which one and which section?
3. If new page — where does it sit in the navigation?
Propose your decision with reasoning. Wait for my approval.
```

### 5.2 Update Content Across the Whole Site
```
Re-read every file in knowledge/.
Compare the knowledge base content against every HTML page.
Identify any content on the site that is outdated or missing.
List all discrepancies, then update all affected pages.
Run verification checks after updating and fix any issues found.
```

### 5.3 Add New Photos and Update Metadata
```
New photos have been added to assets/images/.
Scan only the new or unrecognised files.
Append their metadata to knowledge/image-metadata.txt
without overwriting existing entries.
Then check if any existing pages should use the new photos
and update them if appropriate.
```

---

## SECTION 6 — VERIFICATION AND FIXES

### 6.1 Run a Full Site Verification
```
Run all verification checks from Phase 3 of .github/skills/build-and-verify.md
across the entire site.
Log all issues found in build-log.txt.
Fix every issue found and re-run the relevant check to confirm the fix.
Report back with a summary of issues found and fixed.
```

### 6.2 Check for Broken Links Only
```
Check every <a href="..."> in every HTML file.
Confirm each target file exists in the project.
List all broken or empty links found.
Fix them all and confirm each fix.
```

### 6.3 Check for Broken Images Only
```
Check every <img src="..."> in every HTML file.
Confirm each image file exists at the exact path referenced.
List all broken image references and missing alt attributes found.
Fix them all and confirm each fix.
```

### 6.4 Check Navigation Consistency Only
```
Compare the <header> and <nav> block across every HTML file.
Confirm they are identical on all pages.
Confirm the active class is set correctly on each page.
List any inconsistencies found, fix them, and confirm each fix.
```

### 6.5 Run Accessibility Check Only
```
Check every HTML file for accessibility issues:
- Missing or empty alt attributes on images
- Missing aria-label on interactive elements
- Incorrect heading hierarchy
- Missing labels on form inputs
- Color contrast issues (WCAG AA minimum)
List all issues found, fix them, and confirm each fix.
```

### 6.6 Fix a Specific Issue
```
Fix the following issue on [filename.html]:
[describe the issue clearly]
After fixing, run the relevant verification check to confirm it is resolved.
Report back with what was changed.
```

### 6.7 Run Verification and Correction Loop Until Clean
```
Run the verification workflow in .github/skills/verify-quality.md.
List every issue found in build-log.txt.
Then run the correction workflow in .github/skills/correct-quality.md.
Repeat the verify-and-correct loop until no issues remain.
Only stop when the site passes the relevant verification checks.
Report back with a summary of issues found and fixed.
```

---

## SECTION 7 — CORRECTIONS AND ADJUSTMENTS

### 7.1 Change the Look and Feel
```
Update the visual design of the site with these changes:
[describe what you want changed — colors, fonts, spacing, layout]
Apply changes to css/styles.css only — no inline styles.
Make sure changes are consistent across all pages.
Run verification checks after applying and fix any issues found.
```

### 7.2 Change Brand Colors
```
Update the site brand colors:
Primary color: [hex value]
Accent color: [hex value]
Update the CSS custom properties in css/styles.css.
Verify color contrast still meets WCAG AA after the change.
Fix any contrast issues found and report back.
```

### 7.3 Something Looks Wrong on a Page
```
Something looks wrong on [filename.html]:
[describe what looks wrong as clearly as possible]
Investigate the HTML and CSS, identify the cause, fix it,
and confirm the fix resolves the issue.
```

### 7.4 Revert a Page to Match the Knowledge Base
```
[filename.html] has drifted from the knowledge base content.
Re-read knowledge/[filename].txt and update the page to match exactly.
Do not change the structure, navigation, or styling — content only.
```

---

## SECTION 8 — REPORTING AND AUDIT

### 8.1 Show the Full Build Log
```
Read build-log.txt and summarise:
- What pages were created and when
- What tickets have been completed
- What issues were found and fixed
- What TODOs are still outstanding
```

### 8.2 What Has Changed Since Last Build
```
Review build-log.txt and list everything that has changed
since the initial build was completed.
Group changes by: pages added, pages updated, tickets completed,
issues fixed, and outstanding items.
```

### 8.3 What Still Needs Human Input
```
Review build-log.txt and list all outstanding TODO items
that could not be resolved automatically and need human input.
For each one explain clearly what is needed.
```

---

## QUICK REFERENCE

| Situation | Prompt to use |
|---|---|
| Starting the project for the first time | 1.1 Full Build |
| Just want to scan photos first | 1.2 Scan Photos Only |
| Want to review structure before building | 1.3 Design Only |
| New ticket to implement | 2.1 or 2.2 |
| Want to clear all pending tickets | 2.6 |
| Adding a new page | 3.1 Build a Single New Page |
| Page content is outdated | 3.2 or 3.3 |
| New knowledge file added | 5.1 |
| New photos added | 5.3 |
| Something looks broken | 6.1 Full Verification |
| Specific thing looks wrong | 7.3 |
| Want to see what has been done | 8.1 or 8.2 |
