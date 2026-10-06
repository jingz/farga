# Visual and Interaction Design

## Never let colour carry state alone

A red/green pair is unreadable for a large share of users, and the same is true of any single-hue cue. Every state needs a second channel:

- **Text**: "Valid", "Failed", "3 unread" next to the colour.
- **Shape**: a circle for one state and a triangle for a warning; a filled versus outlined badge.
- **Icon**: an alert glyph beside an error, a check beside success.
- **Pattern or underline**: underline links inside body text; a dotted border for a draft.

The normative parts are SC 1.4.1 (never colour alone) and SC 1.4.11 (contrast) — see `references/accessible-components.md`.

Farga: `.badge.success` / `.danger` / `.info` differ only by hue today, whereas `.alert` pairs its hue with a glyph. Give badges a glyph or a label before relying on one for status. The side menu and the tab bar already mark the active item with weight rather than colour ✓.

## Consistency is a requirement, not a preference

WCAG 2.2 Guideline 3.2 (Predictable) and Shneiderman's consistency rule agree: a control that looks and behaves the same everywhere is learned once.

- Persistent navigation and common actions keep the same screen position across views.
- Controls of the same hierarchy (primary / secondary / tertiary) keep identical geometry, radius and states — the shape rule is in `references/visual-hierarchy.md`.
- Inline helper text beats a tooltip for anything a user must know.

## Focus and keyboard

- Every interactive element keeps a visible focus indicator (SC 2.4.7, AA). Removing an outline without replacing it is a defect, not a style choice. SC 2.4.13 (AAA) adds a size and a 3:1 contrast requirement between the focused and unfocused state.
- Tab order follows reading order. `Tab` moves between widgets, arrow keys move *within* one (radio groups, tabs, listboxes, menus), `Enter` and `Space` activate, `Esc` dismisses.
- Farga's global `:where(a, button, summary, input, select, textarea, [tabindex]):focus-visible` ring satisfies SC 2.4.7 everywhere at 6.40:1 on white ✓. Override it per component only with something equally visible.

## Design for every input device

The same interface gets driven by keyboard, mouse, touch, switch control, sip-and-puff and eye tracking. Two consequences: never require precision pointing for a primary task, and never require a gesture a switch user cannot produce. Details in `references/mobile-touch-inputs.md`.

## Time and flashing

- No more than **three flashes in any one second** (SC 2.3.1). This covers loading spinners and transition effects, not just video.
- Avoid time limits. If one is unavoidable: warn before expiry, allow extension or disabling, and preserve the user's work (SC 2.2.1).
- Farga has no time limits and no flashing transitions ✓.
