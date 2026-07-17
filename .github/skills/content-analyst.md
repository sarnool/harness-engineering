# Skill: Content Analyst

## Purpose
Read the knowledge file(s) and extract structured signals before any design or code decisions are made. Output a Content Brief.

---

## Instructions

Read all files in `knowledge-files/` (excluding the `assets/` subfolder — that is handled by `image-analyst.md`).

Answer each of the following questions. Do not proceed to brand inference until all questions are answered.

---

## Questions to Answer

### 1. Entity Type
What is this website for?
- Personal portfolio / individual professional
- Local business / service provider
- Product or SaaS
- Organisation or institution
- Other (describe)

### 2. Audience
Who is the primary visitor?
- What do they want to know immediately?
- What action do you want them to take?

### 3. Tone Signals
Read the language used in the knowledge file. Identify:
- **Formality:** Casual / Semi-formal / Formal
- **Warmth:** Cold / Neutral / Warm
- **Complexity:** Simple / Moderate / Technical

### 4. Content Inventory
List every distinct content category found in the knowledge file. Examples:
- About / Bio summary
- Services or offerings (with prices if present)
- Team members
- Projects or portfolio items
- Testimonials or social proof
- Location and hours
- Contact details
- FAQs
- Packages or bundles
- Loyalty or membership programs
- Research or thought leadership

### 5. Priority Message
What is the single most important thing a visitor should understand within 5 seconds of landing on the page? Write it as one sentence.

### 6. Calls to Action
What are the 1–3 most important actions a visitor should take? (e.g. Book Now, View Projects, Get in Touch)

---

## Output: Content Brief

Produce a structured Content Brief in this format:

```
ENTITY TYPE: [type]
AUDIENCE: [description]
TONE: [Formality] | [Warmth] | [Complexity]
PRIORITY MESSAGE: [one sentence]
PRIMARY CTA: [action]
SECONDARY CTA: [action, if applicable]

CONTENT INVENTORY:
- [Section name]: [brief description of content available]
- [Section name]: [brief description]
...
```

The Content Brief is the input to all Stage 2 skills. Do not modify it once confirmed.
