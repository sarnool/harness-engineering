# Skill: Image Analyst

## Purpose
Read image assets and metadata to produce an Image Assignment Map that tells the HTML engineer exactly which image goes in which section and how to present it.

---

## Step 1 — Metadata Check

Check for the existence of `knowledge-files/assets/images/image-metadata.txt`.

### If metadata EXISTS:
Read the file. For each image entry, extract:
- `File path` — the exact relative path to use in `<img src="...">`
- `Description` — what the image shows
- `Mood` — the emotional tone of the image
- `People` — whether people are present (affects placement — images with people are warmer, better for hero/team; images without people are better for service/feature sections)
- `Suggested pages` — the pages/sections the image is recommended for
- `Alt text` — use verbatim in the `alt` attribute

### If metadata DOES NOT EXIST:
1. Scan all files in `knowledge-files/assets/images/`
2. For each image file found, infer the following from the filename and the Content Brief:
   - **Description:** What does the filename suggest this image shows?
   - **People:** Unknown — flag as `Unverified`
   - **Setting:** Infer from filename
   - **Mood:** Infer from setting and brand context
   - **Suggested pages:** Infer from content inventory in the Content Brief
   - **Alt text:** Generate a descriptive alt text from the inferred description
3. Write a new `image-metadata.txt` to `knowledge-files/assets/images/` using the schema below
4. Notify the user: *"No image metadata found. I've scanned the images folder and created a metadata file at `knowledge-files/assets/images/image-metadata.txt`. Please review and correct any entries marked `Unverified` before the next build."*

---

## Metadata File Schema

Every entry in `image-metadata.txt` must follow this exact format:

```
## Image [N] – [Short Title]
File path: knowledge-files/assets/images/[filename]
Description: [One sentence describing what the image shows.]
People: [None | Number and description of people visible]
Setting: [Where the image is set]
Mood: [Comma-separated mood words]
Suggested pages: [Comma-separated list of page/section names]
Alt text: [Screen-reader-ready description]
```

---

## Step 2 — Image Assignment Rules

Apply these rules to decide where each image is placed:

### Placement Priority Rules
| Signal | Placement |
|---|---|
| Mood contains "welcoming", "warm", "polished" | Hero section — background or split layout |
| People present, mood is "skilled" or "attentive" | Services section or Packages section |
| People present, mood is "calm" or "caring" | Packages section or Testimonials |
| No people, mood is "organised" or "professional" | Feature highlights or Services grid |
| Mood contains "relaxing" or "restorative" | Packages, Spa/Wellness sections |
| Suggested pages explicitly lists a section | Honour that suggestion unless a conflict exists |

### Conflict Resolution
- If two images are both suggested for the same section, prefer the one with people (warmer, more engaging).
- If no image is suitable for a section, leave it imageless — do not force a poor fit.
- Never use the same image twice on the same page.

### Format Rules
- Use the exact `File path` value from metadata as the `src` attribute.
- Always include the `alt` text from metadata verbatim.
- Never hotlink external images — only use files from `knowledge-files/assets/images/`.

---

## Step 3 — Produce the Image Assignment Map

Output a table in this format:

```
| Section       | Image File                  | Rationale                          |
|---------------|-----------------------------|------------------------------------|
| Hero          | salon_interior_hero.jpg     | Warm, welcoming mood; no people    |
| Services      | hair_colouring.avif         | Shows skilled service in action    |
| Packages      | nail_treatment.avif         | Calm, caring mood; people present  |
| ...           | ...                         | ...                                |
```

Unassigned images should be listed at the bottom with a note explaining why they were not used.
