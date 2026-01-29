# Slide Style Guide
## The AI Innovator's Dilemma — Jax Tech 2026

---

## Overview

**Aesthetic:** Dark, minimal, strategic. Think "a16z meets Linear."
**Tone:** Authoritative but accessible. You're sharing hard truths, not selling.
**Philosophy:** Slides are visual anchors, not transcripts. One idea per slide.

---

## Color Palette

### Primary Colors

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| **Background** | Near Black | `#0A0A0F` | All slide backgrounds |
| **Text Primary** | Off White | `#F5F5F7` | Headlines, key text |
| **Text Secondary** | Cool Gray | `#8E8E93` | Captions, labels, de-emphasized |

### Accent Colors

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| **Primary Accent** | Electric Blue | `#0A84FF` | Key callouts, highlights, links |
| **Warning/Tension** | Warm Amber | `#FF9F0A` | Barriers, problems, "temptation" |
| **Success/Opportunity** | Mint Green | `#30D158` | Solutions, startup advantages |

### Usage Rules

- Use **one accent per slide** maximum
- Accent colors are for emphasis only — never backgrounds
- Gray (`#8E8E93`) for anything secondary or supporting
- No gradients on text; subtle gradients on shapes only

---

## Typography

### Font Stack

| Element | Font | Weight | Size |
|---------|------|--------|------|
| **Slide Title** | Inter or SF Pro Display | Bold (700) | 72–96px |
| **Headline** | Inter or SF Pro Display | Semibold (600) | 48–64px |
| **Body Text** | Inter or SF Pro Text | Regular (400) | 28–32px |
| **Labels/Captions** | Inter or SF Pro Text | Medium (500) | 18–24px |
| **Code/Data** | JetBrains Mono or SF Mono | Regular (400) | 24–28px |

### Typography Rules

- **All caps** for slide category labels (e.g., "1 · THE SCOPE PROBLEM")
- **Sentence case** for headlines and body
- **Maximum 2 font weights** per slide
- Line height: 1.3 for headlines, 1.5 for body
- Letter spacing: +0.5% for all caps labels

### Fallback (Web-Safe)

If Inter/SF unavailable: `system-ui, -apple-system, "Segoe UI", sans-serif`

---

## Layout Principles

### Slide Dimensions

- **Aspect Ratio:** 16:9
- **Resolution:** 1920 × 1080px
- **Safe Margin:** 80px on all sides

### Grid System

```
┌─────────────────────────────────────────────────────────────┐
│  80px margin                                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │   CONTENT AREA (1760 × 920px)                       │   │
│  │                                                     │   │
│  │   • 12-column grid, 24px gutters                    │   │
│  │   • Vertical rhythm: 40px baseline                  │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Content Placement

| Slide Type | Layout |
|------------|--------|
| **Title Slide** | Centered, vertical stack |
| **Statement Slide** | Large text, center or left-aligned |
| **Comparison** | Two columns, equal width |
| **Diagram** | Visual centered, caption below |
| **Framework** | Left-aligned list or vertical stack |

### Whitespace

- **Minimum 40% empty space** per slide
- Group related elements; separate unrelated with generous gaps
- When in doubt, remove elements

---

## Visual Elements

### Cards & Containers

```css
/* Card Style */
background: rgba(255, 255, 255, 0.05);
border: 1px solid rgba(255, 255, 255, 0.1);
border-radius: 16px;
padding: 32px;

/* Highlighted Card (accent) */
border: 1px solid rgba(10, 132, 255, 0.4);
box-shadow: 0 0 40px rgba(10, 132, 255, 0.15);
```

### Dividers & Lines

- Use sparingly
- Color: `rgba(255, 255, 255, 0.15)`
- Thickness: 1px
- No decorative lines — only functional separators

### Icons

- Style: Outlined, not filled
- Stroke width: 1.5–2px
- Size: 32–48px
- Source: Lucide, Phosphor, or Heroicons (outline)
- Color: Match text color (primary or secondary)

### Diagrams

- Use simple geometric shapes
- Rounded rectangles (`border-radius: 12px`)
- Arrows: Simple, no fancy heads
- Labels directly on or adjacent to shapes (no legends)

### Images

- Use sparingly (your talk is conceptual)
- Full-bleed or contained in rounded cards
- Subtle dark overlay if text on image: `rgba(0, 0, 0, 0.6)`
- Exception: Stanley trunk photo (Slide 6) — let it be raw

---

## Slide Types & Templates

### 1. Title Slide

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                                                             │
│                                                             │
│              THE AI INNOVATOR'S DILEMMA                     │
│              ─────────────────────────────                  │
│              What Do You Do With a Tool                     │
│                 That Can Do Anything?                       │
│                                                             │
│                                                             │
│              ┌─────────────────────────────┐                │
│              │  "Thesis statement here"    │                │
│              └─────────────────────────────┘                │
│                                                             │
│                     Philip O'Donnell                        │
│                     Jax Tech · Jan 2026                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2. Section Header (Barrier Intro)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   1 · THE SCOPE PROBLEM                    ← Label (caps)   │
│                                                             │
│                                                             │
│                                                             │
│        They never fully cross                               │
│        the threshold.                      ← Headline       │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3. Statement Slide

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                                                             │
│                                                             │
│        95% → 100%                                           │
│        is not 5%.                                           │
│                                                             │
│        It's a different                                     │
│        business entirely.                                   │
│                                                             │
│                                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

Large text, minimal. Let it land.

### 4. Comparison (Two Column)

```
┌─────────────────────────────────────────────────────────────┐
│   Headline Text Here                                        │
│                                                             │
│   ┌────────────────────────┐  ┌────────────────────────┐   │
│   │                        │  │                        │   │
│   │       INCUMBENT        │  │        STARTUP         │   │
│   │                        │  │                        │   │
│   │   • Point one          │  │   • Point one          │   │
│   │   • Point two          │  │   • Point two          │   │
│   │   • Point three        │  │   • Point three        │   │
│   │                        │  │                        │   │
│   └────────────────────────┘  └────────────────────────┘   │
│                      ↑ amber               ↑ mint          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 5. Diagram Slide

```
┌─────────────────────────────────────────────────────────────┐
│   Headline Text Here                                        │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐  │
│   │                                                     │  │
│   │              [DIAGRAM / VISUAL]                     │  │
│   │                                                     │  │
│   │                                                     │  │
│   └─────────────────────────────────────────────────────┘  │
│                                                             │
│              Caption or takeaway line                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Animation & Transitions

### Slide Transitions

- **Type:** Fade or subtle slide (horizontal)
- **Duration:** 300–400ms
- **Easing:** `ease-out` or `cubic-bezier(0.25, 0.1, 0.25, 1)`

### Content Animation

- **Entrance:** Fade up (opacity 0→1, translateY 20px→0)
- **Stagger:** 100ms delay between elements
- **Duration:** 400ms per element

### Rules

- Animate content IN only (no exit animations)
- Maximum 3 animated elements per slide
- No bounces, spins, or attention-seeking effects
- Animation should feel like breathing, not performing

---

## Specific Slide Notes

| Slide | Special Treatment |
|-------|-------------------|
| **Slide 1 (Title)** | Thesis in a subtle card with blue glow |
| **Slide 4 (Story Circle)** | Use amber for failure points, keep diagram simple |
| **Slide 6 (Upside Down)** | Stanley trunk photo is the star — minimal text |
| **Slide 7 (Shortest Path)** | Two cards: amber "temptation" vs faded "true prize" |
| **Slide 10 (Framework)** | Clean vertical list — this is the takeaway |
| **Slide 13 (CTA)** | Lots of space, let the question breathe |

---

## Do's and Don'ts

### Do

- ✓ Use one idea per slide
- ✓ Let slides breathe (40%+ whitespace)
- ✓ Use accent colors sparingly for emphasis
- ✓ Make headlines scannable in 2 seconds
- ✓ Use consistent alignment (prefer left)
- ✓ Test on a projector or large screen

### Don't

- ✗ Bullet point lists longer than 3 items
- ✗ Multiple accent colors on one slide
- ✗ Decorative elements that don't inform
- ✗ Clip art, stock icons, or cheesy graphics
- ✗ Text smaller than 24px
- ✗ Animations that distract from your words

---

## File & Asset Checklist

```
/slides
  ├── index.html          # Main presentation
  ├── styles.css          # Custom styles
  └── /img
      ├── stanley-trunk.jpg   # Slide 6 (DARPA winner)
      └── qr-code.png         # Slide 13/14 (optional)
```

### Image Specs

- Format: JPG for photos, PNG for graphics, SVG for icons
- Max file size: 500KB per image
- Optimize before including

---

## Quick Reference

```
Background:    #0A0A0F
Text:          #F5F5F7
Muted:         #8E8E93
Accent Blue:   #0A84FF
Accent Amber:  #FF9F0A
Accent Green:  #30D158

Font:          Inter / SF Pro
Title:         72–96px Bold
Headline:      48–64px Semibold
Body:          28–32px Regular

Slide:         1920 × 1080 (16:9)
Margins:       80px
```

---

*Style guide created for "The AI Innovator's Dilemma" — Jax Tech, January 2026*
