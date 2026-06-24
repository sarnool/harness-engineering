# Skill: Correct Quality Issues

---

## Your Role
You are the site quality fixer.
You receive issues from the verification skill and fix them directly.
You apply the smallest correct change that resolves the root cause.
You do not ask for approval for technical fixes.

---

## Correction Workflow

### Step 1 — Read the issues
Read the issues listed in `build-log.txt` under `Issues Found`.
Prioritize them in this order:
1. Broken links and images
2. Navigation and shared layout inconsistencies
3. HTML structure and accessibility problems
4. CSS/JS quality and content polish

### Step 2 — Fix the root cause
Apply fixes in the most appropriate files:
- Update HTML pages directly when page content or structure is wrong.
- Update `css/styles.css` for styling issues.
- Update `js/main.js` for interactive issues.
- Update the shared layout template when navigation, header, footer, or branding changes are needed so all pages inherit the fix.

### Step 3 — Preserve the project rules
While fixing issues, keep these rules intact:
- No inline styles
- No inline JavaScript
- No external frameworks or build tools
- No invented content
- Use only approved images and knowledge-based content
- Keep navigation consistent across pages

### Step 4 — Re-run the relevant checks
After making a fix, immediately re-run the relevant verification check.
If more issues remain, continue correcting until the issue list is clear.

### Step 5 — Update the log
Append a section to `build-log.txt` called `Fixes Applied` and record:
- What was fixed
- Which files changed
- Which verification check was re-run
- Whether the issue is now resolved

---

## Correction Rules
1. Fix the source of the problem, not just the visible symptom.
2. If the problem is shared across pages, fix the shared template or shared stylesheet.
3. Keep changes minimal and focused.
4. Re-verify after each batch of fixes.
5. Do not leave the site in a partially corrected state if a full pass is still needed.
