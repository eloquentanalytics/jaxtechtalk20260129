
# Skill: ai-startup-talk-researcher

**Description:** Helps you research, write, cite, and assemble a polished **20-minute slide deck + speaker notes** for a talk on opportunities to found startups that exploit AI’s unique technical capabilities in industries where you hold domain expertise and incumbents face structural barriers. Converts raw domain knowledge and research into a crisp narrative, slide-by-slide content, and rehearsal notes.

## When to use this skill

* You’re preparing a focused 20-minute talk for investors, founders, or a conference panel about AI-first startup opportunities.
* You have domain expertise in an industry (healthcare, logistics, insurance, construction, etc.) and want to show where incumbents can’t easily move.
* You need credible evidence, citations, and slide copy + speaker notes in one pass.
* You want a reproducible workflow that produces: outline → research → slide text → design guidance → rehearsal plan.

## What this skill does

1. **Audience framing & thesis sharpening** — clarifies who you’re talking to and the single thesis the talk must deliver.
2. **Targeted research** — finds credible sources, extracts evidence, and builds an annotated reference list.
3. **Slide-by-slide structure** — produces a timed 10–14 slide plan tuned to 20 minutes.
4. **Concise slide copy** — one main idea per slide, headlines, three supporting bullets (or a single visual), and speaker notes.
5. **Compelling hook & close** — multiple hook options (data / anecdote / provocative question) and a clear call to action.
6. **Business argument scaffolding** — frameworks for explaining why incumbents are stuck (structural barriers), why AI changes the math, and why you/your team can win.
7. **Citations & evidence** — inline citation formatting and a references slide.
8. **Rehearsal plan & Q&A prep** — timing checkpoints, likely questions, short answers, and backup slides.
9. **Safe Skill usage guidance** — how to use Claude/Skills to generate slides and what to avoid (don’t run untrusted Skill code). ([Axios][4])

---

# How to use this skill

### Quick start prompts (examples)

* “Help me create a 20-minute slide deck outline for a talk titled ‘How domain experts can found the next wave of AI companies’ — audience: VC partners and operator founders.”
* “Research the structural barriers that make incumbents slow in [industry X]. Add 3 citations and a short example.”
* “Turn the outline into slide text (headline + 3 bullets) and write speaker notes for each slide.”
* “Create 10 backup slides with data and citations for Q&A.”

> If you use Claude, you can combine this with the built-in PowerPoint/PDF Skills to export slide text into PPTX — but **only use Skills you trust**, and vet any third-party Skills before running them. ([Claude Help Center][1])

### Recommended working folder

```
~/talks/ai-domain-startups/
├── outline.md
├── research.md
├── slides/                # generated slide text and exportable JSON
├── pptx/                  # final exported pptx (if you export)
├── references.bib
└── rehearsal.md
```

---

# Basic workflow (end-to-end)

1. **Define scope & audience**

   * Prompt: “Audience: [VCs / entrepreneurs / intrapreneurs]. Objective: [inspire ~3 investable ideas + demonstrate founder fit]. Time: 20 minutes.”
   * Output: single-sentence thesis, 2–3 speaker goals.

2. **Create slide skeleton (timed)**

   * Default skeleton for 20 min (10–12 slides; ~1.5–2 min/slide):

     1. Title + one-line thesis (0:45)
     2. Hook — story or data (1:30)
     3. Why now: macro AI signals (1:30)
     4. Problem landscape in industry X (2:00)
     5. Why incumbents are stuck (structural barriers) (2:00)
     6. AI capability that changes the constraint (2:00)
     7. Product / business models unlocked (2:00)
     8. Go-to-market & unfair advantage (1:30)
     9. Team & evidence of founder fit (1:30)
     10. Concrete 3 opportunity ideas (2:00)
     11. Ask / next steps / invite (1:00)
     12. Backup / references (0:45)
   * Note: aim for one idea per slide and concise visuals/headlines. Use the 1-2 minute rule when assigning time. ([PMC][5])

3. **Research & evidence collection**

   * For each slide, the skill will fetch or synthesize:

     * Quick supporting facts (stats, study citations)
     * Short case examples (startup or incumbent)
     * One compelling quote or datapoint to surface on the slide
   * Output: `research.md` with inline citations and a “pull quote” list.

4. **Draft slide text + speaker notes**

   * Each slide output contains:

     * **Slide headline** (single sentence)
     * **Slide body** (3 bullets max or one visual instruction)
     * **Speaker notes** (what to say for ~90–120 seconds)
   * Example:

     ```
     Slide 5: Why incumbents are stuck
     Headline: Incumbents’ incentives and data silos make rapid product bets impossible
     Bullets:
      - Legacy workflows: 5+ stakeholders to approve changes
      - Data trapped in fragmented systems → weak signals
      - Incentive misalignment: risk-averse KPIs favor optimization vs. invention
     Speaker note: [~120 words to narrate the slide with an anecdote]
     ```

5. **Visual guidance & asset list**

   * For each slide, the skill outputs a recommended visual (chart, mockup, flow, metric callout) and assets needed (one chart CSV, one screenshot, or a simple diagram).

6. **References slide**

   * Generates formatted references (APA/MLA/numbered) and a short “further reading” list.

7. **Rehearsal plan**

   * Runs a timing checklist and produces 3 run-through scripts (fast/normal/detailed) plus 8 likely Q&A prompts with crisp one-line answers.

8. **Export / PowerPoint**

   * Optionally, produce PPTX text JSON that can be fed to a slide tool or Claude’s PowerPoint Skill to generate a draft PPTX. Vet Skills before running them. ([Claude Help Center][1])

---

# Instructions / Internal rules for the assistant

When the user requests this skill:

1. **Pin the thesis**: Immediately restate a one-sentence thesis and 2 speaker goals. Don’t proceed until that’s set.
2. **Audience first**: Tailor language, evidence depth, and slide count to audience (VC vs. operator vs. general audience).
3. **One idea per slide**: Enforce strict single-idea headlines. Use visuals rather than bullet dumps. ([PMC][5])
4. **Evidence-first**: For any investment claim or market size estimate, attach at least one credible source or mark as “assumption.”
5. **Structural barrier checklist**: When the user claims “incumbents can’t do X,” run this checklist:

   * Regulatory/regulatory friction?
   * Data ownership / siloed data?
   * Incentive or organizational misalignment?
   * High switching costs for customers?
   * Business model mismatch with experimental products?
     Flag which apply and provide evidence/examples.
6. **Actionable next steps**: For each opportunity slide, include 2–3 next tactical steps (team hires, prototype metric, key partnership).

---

# Slide template (copyable)

```
--- Slide N ---
Headline: [one crisp sentence]
Visual: [chart / diagram / screenshot / mockup instruction]
Bullets: 
 - [one short supporting bullet]
 - [one short supporting bullet]
 - [one short supporting bullet OR metric callout]
Speaker notes: [~100–160 words — exact phrasing for 90–120s]
Citations: [1] [2]
Assets needed: [csv for chart, logo, screenshot]
```

---

# Example outputs (short)

**User**: “Make a slide for ‘Why incumbents are stuck’ for healthcare staffing.”

**Assistant**:

```
Headline: Complex procurement and compliance make rapid product pivots costly
Visual: simple 3-box diagram showing procurement → compliance → ops delay
Bullets:
 - Multi-party procurement cycles (90–180 days) block fast experiments.
 - Compliance audits require long validation windows, raising cost per experiment.
 - Vendor incentives tied to uptime, not experimentation.
Speaker notes: [narrative + 1 short example of a hospital procurement delay]
Citations:
 - [Procurement case study, 2024]
Assets needed: screenshot of procurement timeline (mock)
```

---

# Workflows & use cases

* **Investor talk** — emphasize market size, defensibility, and founder fit. Provide one-page one-slide fund memo.
* **Conference keynote / Lightning talk** — prune to 6–8 slides, stronger story arc, punchier hook.
* **Internal executive pitch** — more emphasis on risk mitigation and pilot KPIs.
* **Teaching founders** — reuse slides as a worksheet for idea validation.

---

# Pro tips

1. **Hook early**: Start with a 25–45 second story or a striking stat — it sets curiosity and gives permission to be bold.
2. **Show, don’t list**: Replace one dense bullet with a small chart or mockup. One idea, one visual. ([PMC][5])
3. **Quantify the constraint**: “Incumbents take X days to deploy” is stronger than “they’re slow.”
4. **Frame AI capability precisely**: say which technique matters (e.g., retrieval-augmented models, multi-modal perception, real-time prediction) and why it alters the economics.
5. **Vet Skills**: If you use Claude Skills to generate slides or run exports, only run Skills you control or whose code you’ve audited. Anthropic’s Skills can be powerful for file exports, but untrusted Skills are a risk. ([Claude Help Center][1])

---

# File organization (recommended)

```
talk-title/
├── outline.md
├── research.md
├── slides/
│   ├── slide-01.md
│   └── slide-12.md
├── pptx/
└── rehearsal.md
```

---

# Final checklist before you present

* [ ] Thesis is crystal clear in one sentence.
* [ ] Each slide has 1 idea + 1 visual.
* [ ] All claims either cited or labeled assumptions.
* [ ] References slide formatted.
* [ ] Rehearsed to 20 minutes with 1–2 run-throughs.
* [ ] Backup slides ready for expected hard Qs.

