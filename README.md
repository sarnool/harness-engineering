# 🌐 Website Builder Harness

> A structured AI engineering harness that turns a plain text knowledge file into a fully built, multi-page website — using GitHub Copilot Agent Mode and nothing else.

---

## What Is This?

This is a website building **harness** — a set of instruction files that teach GitHub Copilot *how to think* before it writes a single line of code.

Most people use AI to generate websites by typing something like *"build me a homepage"* and hoping for the best. The output is usually generic, inconsistent, and hard to maintain.

This harness takes a different approach. Before Copilot touches any code, it will:

1. **Read and understand** your content and decide what kind of website to build.
2. **Analyse your images** and decide where each one belongs.
3. **Infer a visual identity** (colors, fonts) from your content's tone.
4. **Decide the site structure** (single page or multi-page).
5. **Plan every section** of every page.
6. **Present the full plan to you** for review before writing code.

The result? A properly structured, professional website with **separated HTML, CSS, and JavaScript**, shared header/footer templates, and full accessibility compliance.

---

## Why Does This Matter?

The difference between asking an AI to *"build a website"* and using a harness is the same as the difference between asking a contractor to *"build a house"* versus handing them a full architectural brief, material specs, and a site plan.

*   **Without a harness:** The AI makes hundreds of silent assumptions about design, structure, and quality—and you have no control over them.
*   **With this harness:** Every decision is explicit, traceable, and reviewable before a single file is written.

This is what **harness engineering** looks like in practice.

---

## What It Produces

Given a simple text file describing your business and a folder of images, the harness autonomously generates a clean, modular website structure:


```

output/
├── index.html
├── services.html
├── about.html
├── contact.html
├── partials/
│   ├── header.html        ← defined once, shared by every page
│   └── footer.html        ← defined once, shared by every page
└── assets/
├── css/
│   └── main.css       ← colors, fonts, and layouts
├── js/
│   └── main.js        ← mobile menus and interactivity
└── images/

```

Every output file follows strict web standards:
*   **No messy inline styling** — all design rules live neatly in `main.css`.
*   **No duplicate markup** — the header and footer are written once and shared.
*   **No "AI hallucinations"** — the text is strictly sourced from your knowledge file.

---

## How the Harness Works

The harness is made up of **8 "skills"** that Copilot loads at each stage of the build. Think of them as specialist team members handing off tasks to one another.


```

Stage 1   content-analyst.md       Reads your text. Extracts tone, audience, and key messages.

Stage 2a  image-analyst.md         Re-scans images, reconciles metadata, optimizes only new files, then assigns images.

Stage 2b  brand-inference.md       Translates your content tone into colors, fonts, and spacing.

Stage 2c  site-architect.md        Determines page layout and creates a site map.

Stage 2d  section-architecture.md  Blueprints every section of every page.

Stage 2e  component-library.md     Picks clean design patterns for each section.

```
      ── ⏸️ YOU REVIEW & EDIT THE PLAN HERE ──

```

Stage 3b  partials-manager.md      Generates shared global layouts (header & footer).

Stage 3+  html-engineer.md         Builds the pages, CSS, JS, and validates the final code.

```

---

## Folder Structure


```

website-builder-harness/
│
├── AGENTS.md                      ← Workflow controller (the conductor)
├── PROMPTS.md                     ← Ready-to-use prompt templates
├── STATUS.md                      ← Track build state across sessions
├── DECISIONS.md                   ← Log of every design decision made
│
├── .github/
│   └── skills/                    ← The 8 skill files loaded by Copilot
│   └── tools/                     ← Local helper scripts (for example image optimization)
│
├── knowledge-files/               ← 📥 DROP YOUR CONTENT HERE
│   ├── my-business.txt
│   └── assets/
│       └── images/
│
└── output/                        ← 📤 GENERATED WEBSITE LANDS HERE

```

---

## 🚀 Quick Start

### Prerequisites
*   **VS Code** with the **GitHub Copilot** extension installed.
*   **GitHub Copilot Agent Mode** enabled in your chat settings.
*   **Python 3.10+** for helper scripts.

Optional for local image optimization helper:
```bash
pip install pillow pillow-avif-plugin
```

---

### Step 1 — Get the Code
*   **Option A (For Developers):** Clone the repository:
    ```bash
    git clone https://github.com/sarnool/harness-engineering.git
    cd harness-engineering
    ```
*   **Option B (For Beginners):** Click the green **Code** button at the top of this GitHub page, select **Download ZIP**, and extract it on your computer. Open the extracted folder in VS Code.

---

### Step 2 — Add Your Content (The "Knowledge File")
Create a plain text file (e.g., `my-business.txt`) in the `knowledge-files/` folder. Write or paste anything about your business, product, or self. Include:
*   What you do and who you serve.
*   Your services, offerings, or pricing.
*   Contact details and physical location.

*(Stuck? Check out the files in `example-shop-site` to see how it's done.)*

---

### Step 3 — Add Your Images
Drop your JPGs or PNGs into `knowledge-files/assets/images/`. 

*Don't worry about cataloging them.* The harness scans and reconciles this folder during Stage 2a. If metadata exists, it detects newly added files, optimizes only those new files when needed, and updates metadata to use the optimized filename.

Optimization behavior for newly added images:
*   The original and optimized files can stay in the same folder.
*   New optimized files are written as `<original_stem>_optimized<original_ext>`.
*   Metadata keeps one canonical entry (prefer optimized file path when generated).
*   Already tracked images are not bulk re-optimized.

---

### Step 4 — Open Copilot Agent Mode
1. Open the **Copilot Chat** panel in VS Code (`Ctrl + Alt + I` or `Cmd + Shift + I` on Mac).
2. Switch the dropdown at the top of the chat panel from *Chat* to **Agent**.

---

### Step 5 — Run the Build Prompt

Copy **one** of these prompts and paste it into the Copilot Agent chat:

#### 🔹 Option A: Guided Build (Recommended)
This prompt pauses at Stage 2 to let you review and adjust the website design before any code is generated.

```text
Build a website from the knowledge file at knowledge-files/[your-filename].txt.
Follow the full workflow in AGENTS.md.
Start with Stage 1 (content analysis), Stage 2a (image intelligence), and Stage 2c (site architecture) before making any design decisions.
Present the Content Brief, Image Assignment Map, Site Map, Design Token Set, and Section Blueprints for my review before writing any files.

```

#### 🔹 Option B: Fully Autonomous Build

This prompt tells the harness to make its own design decisions and build the entire website in one shot.

```text
Build a website from the knowledge file at knowledge-files/[your-filename].txt.
Follow the full workflow in AGENTS.md.
Use your best judgement at the human checkpoint and proceed automatically.
Scaffold the output folder, generate partials, CSS, JS, and all pages per the Site Map.

```

---

### Step 6 — Review and Approve (If using Option A)

Copilot will present a clear blueprint of your site:

* The chosen color palette and fonts.
* Which images it selected for the header, features, and about sections.
* How many pages it will build.

Type **"Looks great, proceed!"** or ask for changes (e.g., *"Change the primary color to forest green"*).

---

### Step 7 — View Your Live Website!

Once Copilot finishes building, it needs to stitch your header and footer into your final pages.

1. Open your terminal in VS Code (`Ctrl + ~`).
2. Run this script to compile the final pages:
```bash
python scripts/compile_includes.py

```


3. Start a local temporary web server to view it:
```bash
python -m http.server 8000

```


4. Open your browser and navigate to: **`http://localhost:8000/output/index.html`**

---

## 🛠️ Modifying Your Website Later

Once your site is built, you can easily ask Copilot to make adjustments. Copy and paste these handy prompts right into your chat:

| Goal | Prompt to Use |
| --- | --- |
| **Add a new page** | `Add a new [page name] page to the site following our harness design rules.` |
| **Add a section** | `Add a [testimonial/pricing/etc] section to output/[page-name].html.` |
| **Sync new images** | `Re-scan knowledge-files/assets/images and reconcile with image-metadata.txt. Detect only newly added image files, optimize only if needed, and update metadata paths without reprocessing tracked files.` |
| **Change colors** | `Update the Design Token Set in output/assets/css/main.css to use a [cool blue / dark mode / warm earth] theme.` |
| **Update text** | `I have updated the knowledge file. Update the website's content to reflect the changes.` |

---

## Design Principles Behind This Harness

* **Separation of Concerns:** HTML structure, CSS styling, and JS interactivity are strictly separated. No messy inline styling.
* **Decisions Before Code:** The harness forces a complete, human-approved plan *before* writing code.
* **Single Source of Truth:** Colors, fonts, and spacing are controlled by CSS variables at the top of `main.css`. Change them once, and the entire site updates.
* **Zero Hallucination:** The AI is tightly bound to *your* input text. It will not make up fake business services or addresses.

---

*Built with GitHub Copilot Agent Mode • No complex frameworks • No build tools required to run.*
