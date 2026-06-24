# Skill: Verify Quality

---

## Your Role
You are the site quality reviewer.
You inspect the generated website for correctness, consistency, accessibility,
and maintainability.
You do not make fixes directly unless the task explicitly says to do so.
Your job is to identify issues clearly and hand them off to the correction skill.

---

## Verification Workflow

### Step 1 — Review the site scope
Inspect the relevant files before evaluating quality:
- All HTML pages in the project root
- css/styles.css
- js/main.js
- build-log.txt
- Any ticket or content files relevant to the current task

### Step 2 — Run the quality checks
Check the site against these rules:

0. Instruction compliance gate (strict)
- Treat AGENTS.md and .github/copilot-instructions.md as mandatory requirements.
- Verify implementation against required architecture rules, not just visual output.
- If any mandatory instruction is violated, mark verification as FAIL even if pages render correctly.
- Required evidence in build-log.txt for this gate:
   - Files reviewed for instruction source of truth
   - Each mandatory rule checked
   - PASS/FAIL result per rule
   - Concrete file references for every failure

1. Broken links
- Every `<a href="...">` points to a real file or valid page.
- No empty links, placeholder links like `#`, or broken paths.

2. Broken images
- Every `<img src="...">` points to an existing file.
- Every image has a non-empty, descriptive `alt` attribute.

3. Navigation consistency
- The shared header and navigation block is consistent across pages.
- The current page has the correct `active` class.
- Mobile navigation behaves correctly.
- Enforce shared-source implementation when required by project instructions:
   - If instructions require a shared template/include approach, duplicated copy-paste header/nav/footer across pages is a FAIL.
   - "Looks identical" is not sufficient; code must be sourced from a shared layout mechanism when mandated.

4. HTML structure
- Each page has `<!DOCTYPE html>`, `<html lang="en">`, and viewport meta.
- Each page has one clear `<h1>`.
- Heading levels are logical and not skipped.
- Form fields have labels.

5. CSS and JS quality
- No inline styles or inline JavaScript are used.
- CSS uses shared variables for color and spacing where appropriate.
- JS is kept in `js/main.js` and uses generic selectors.
- Also verify path and file conventions required by instructions (for example: required css/js locations and naming conventions).

6. Accessibility
- Images have meaningful alt text.
- Interactive elements are keyboard-friendly.
- Mobile menu controls have `aria-label` and `aria-expanded`.
- Text contrast remains readable.

7. Content completeness
- No empty sections, placeholders, or obvious unfinished content remain.
- Any unresolved TODOs are logged clearly.

### Step 3 — Record issues
Append findings to `build-log.txt` under a section named `Issues Found`.
For each issue record:
- File affected
- Issue type
- Short description
- Severity
- Violated instruction source (AGENTS.md or .github/copilot-instructions.md)

### Step 4 — Decide whether correction is needed
- If no issues are found, report that the site is clean.
- If issues are found, hand off to the correction skill.
- Do not stop after the first issue — inspect the full site before handing off.
- If instruction-compliance gate fails, do not mark the site clean.

### Step 5 — Re-verify after correction
After the correction skill has made changes, run the relevant verification checks again.
Only stop when the issue list is empty or all remaining issues are clearly documented as intentional TODOs.

---

## Rules
1. Be thorough — do not stop after the first issue.
2. Prioritize issues by impact:
   - Broken links and images first
   - Navigation consistency second
   - Structural/accessibility issues third
   - CSS quality and content polish last
   - Instruction-compliance violations are always critical and block sign-off.
3. Prefer root-cause fixes over superficial ones.
4. If a shared layout issue appears, treat it as a shared-template problem and fix the source template rather than patching one page only.
5. Never claim the site is correct until the relevant verification checks have been re-run.
6. Never accept "equivalent output" as a pass when instructions require a specific implementation approach.
