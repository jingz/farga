---
name: web-ui-design
description: Design, build and evaluate accessible, responsive web UI. Use when setting spacing, typography, colour, button sizing, shadows or imagery, writing inclusive copy, structuring HTML/ARIA, sizing touch and voice targets, or running a WCAG 2.2 audit and triaging the findings.
---

# Web UI Design & Accessibility

Visual hierarchy (*Refactoring UI*) and accessible frontend engineering (WCAG 2.2, WAI-ARIA) are the same job: hierarchy tells a sighted user where to look, semantics tell everyone else what they are looking at. Apply both together.

Read the reference for the topic before writing markup, styling or a test plan.

**Building blocks**

- `references/layout-and-spacing.md` — white space, the spacing scale, container widths, grouping, fewer borders.
- `references/designing-text.md` — type scale, the two-weight rule, font stacks and their fallbacks, input widths.
- `references/coloring.md` — per-hue ramps, assigning colour to meaning, saturation and grey discipline.
- `references/depth-and-shadow.md` — one overhead light source, a five-tier elevation scale, layered and flat shadows.
- `references/working-with-images.md` — alt text by image kind, text baked into images, cropping uploads, small icons.
- `references/visual-hierarchy.md` — button sizing and padding ratios, action weight, emphasis, empty states.

**Accessibility**

- `references/accessible-components.md` — the contrast table (including Farga's measured failures), the 5 rules of ARIA, data tables.
- `references/developing-html-css-aria.md` — semantics, CSS-generated content, user preferences, reflow at 320px.
- `references/visual-interaction-design.md` — state cues beyond colour, consistency, focus and keyboard, time limits, flashing.
- `references/mobile-touch-inputs.md` — touch targets, gesture alternatives, voice labels, focus grouping.
- `references/accessible-content-writing-media.md` — plain language, headings, captions, transcripts, social text.
- `references/accessible-design-systems.md` — what to build first, what to omit, handoff annotations.

**Process**

- `references/evaluation-and-prioritization.md` — accessibility tree, linters, screen readers, severity triage.
- `references/emerging-tech-vr-ar-ai.md` — VR/AR accommodations and AI governance; only if the product ships those.
- `assets/design-tokens.json` — default spacing, type, button and elevation values for projects with no system of their own.

If the project already defines its own tokens (design-system SCSS, CSS custom properties, a theme file), **those win**. Never introduce a second scale beside an existing one.

For the longer *Refactoring UI* treatment, read the `refactoring-ui` skill if it is installed in this workspace (news-v2 keeps it at `.pi/skills/refactoring-ui.md`).

## Core directives

1. **Hierarchy, emphasis and buttons**
   - **Feature first**: design the screen's actual feature or workflow, not a generic canvas or header/footer shell filled in afterwards.
   - **Action weight**: one prominent primary action per view. Secondary actions use muted fills or outlines, tertiary actions are text links, and destructive actions stay low-emphasis until an explicit confirmation step.
   - **De-emphasize rather than over-emphasize**: make the loud thing quieter before making the important thing louder.
   - **Button padding is not proportional**: never scale padding off the font size in `em`. Bigger buttons take proportionally more generous padding (20px font → `15px 30px`), smaller ones disproportionately tighter (12px font → `6px 8px`). Use Farga's tiers — `.btn-small` 12px, base 14px, `.btn-large` 16px, `.btn-extra` 20px — and don't re-derive padding.
   - **One shape per group**: all tiers share a border radius and height tier; only fill and border change.

2. **Layout and spacing**
   - Start with generous white space and condense deliberately; dense is a choice for data-dense screens, not a default.
   - Space *around* a group must exceed the space *within* it, or the grouping reads as a guess. In forms, a label sits closer to its input than to the next field.
   - Constrain containers to the width the content needs; give long-form text a `ch` measure rather than letting it fill a wide container.

3. **Typography**
   - One type scale, no off-scale sizes. Two weights: 400/500 for body, 600/700 for emphasis. Never below 400 in UI text.
   - De-emphasize with a lighter colour or a smaller size, never a lighter weight.
   - Check the fallback, not just the first font in the stack: a stack whose first family is missing lands on a generic fallback and loses the intended voice.

4. **Colour and depth**
   - Build a ramp per hue (light surfaces, mid action, dark text), then assign ramps to meaning and keep that meaning stable everywhere.
   - Contrast: 4.5:1 for text, 3:1 for the visual information identifying a component or its state, 4.5:1 recommended for strokes under 3 CSS px. Several Farga colours fail today — the table in `references/accessible-components.md` names them.
   - Never let colour carry state alone; add a label, icon or border change.
   - Emulate one overhead light source, and assign shadows from a fixed elevation scale rather than writing them per component.

5. **Semantic HTML first, ARIA last**
   - **Native elements win**: `<button>`, `<select>`, `<dialog>`, `<nav>`, `<main>`. Reach for `aria-expanded`, `aria-describedby` and friends only when native semantics fall short.
   - **Never suppress focus**, and never remove a focus outline without replacing it: every interactive element keeps a visible indicator (SC 2.4.7).
   - **Forms**: keep format expectations (e.g. `MM/DD/YYYY`) in a visible label or helper text wired up with `aria-describedby` — never hide required guidance in placeholder text only.
   - **Content in CSS is not content**: a glyph or string from `::before`/`::after` is not dependably announced. Keep the meaning in text and the pseudo-element decorative.
   - **Images**: name the action, not the picture, and never bake copy into a bitmap.

6. **Multi-input and scannable interfaces**
   - **Labels with action intent**: avoid "Click Here" and bare "Submit". Use "Save your work" or "Submit your order" — screen reader and voice-control users hear the label out of context.
   - **Voice commands**: every control needs a concise, unique, predictable visible label matching its accessible name, so iOS Voice Control and Android Voice Access can target it unambiguously.
   - **Touch targets**: 44×44 CSS px (WCAG 2.5.5, AAA); 24×24 CSS px is the AA floor (SC 2.5.8), and undersized targets pass only when a 24px circle centred on each intersects no other target's circle.

7. **Content and media**
   - Front-load the point in sentences and headings; keep paragraphs to 4–5 sentences; headings are structure, never emphasis.
   - Links and buttons name their destination or action — never "click here" or a bare URL.
   - Multimedia needs captions that include meaningful non-speech audio, a transcript for audio-only, and audio description when the visuals carry information the dialogue does not.
   - PascalCase hashtags (`#AccessibleDesign`), one emoji at most, and no copy baked into raster images.

8. **Verify, then triage**
   - Automated checkers catch the mechanical third (alt, contrast, missing labels, duplicate ids). Use them as a linter, never as proof.
   - The accessibility tree, a keyboard-only pass, and one real screen reader catch the rest. An overlay is not a fix.
   - Give every finding a severity — blocker, high, medium, low — and triage against the real page, not the report. Process detail in `references/evaluation-and-prioritization.md`.
