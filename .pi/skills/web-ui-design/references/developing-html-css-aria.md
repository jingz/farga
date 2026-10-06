# Developing Accessible HTML, CSS and ARIA

## Semantics before containers

Prefer `<main>`, `<nav>`, `<article>`, `<header>`, `<footer>`, `<button>`, `<dialog>` over `<div>` and `<span>`. Semantic elements arrive with a role, keyboard behaviour and focus handling already wired; a `div` arrives with nothing and every one of those has to be rebuilt and tested.

Farga's drawer, dialog and accordion are built on `<dialog>`, `<details>` and the popover API ✓ — that is the pattern to copy for any new interactive component. The 5 rules of ARIA are in `references/accessible-components.md`; this file covers the mechanics around them.

## Essential content does not live in CSS

`::before` and `::after` with `content: "…"` are not a reliable accessibility surface: assistive tech support for generated content is inconsistent, and a pseudo-element cannot carry `aria-hidden` or a label. Decorative glyphs from CSS are fine when the same meaning exists in text.

Two Farga cases to watch:

- `.alert` marks severity with a CSS glyph (`✓`, `!`, `×`). Keep the severity in the heading or body text too.
- `[data-tooltip]` renders its only text from `attr(data-tooltip)` in a pseudo-element, so the tip's content is not dependably announced. Never let a tooltip be the only place a value or instruction exists (`references/accessible-design-systems.md`).

## Respect user preferences

- `@media (prefers-reduced-motion: reduce)` — remove non-essential transitions and animation. Farga handles this globally ✓.
- `@media (prefers-color-scheme: dark)` — Farga's dark theme is a `body.dark-mode` class toggled by JavaScript, not a media query, so the OS setting only reaches it through the page's own detection (the docs read it on first visit). Prefer the media query as the default and the class as an explicit override.
- Never disable zoom in the viewport meta tag (`user-scalable=no`, `maximum-scale=1`): blocking zoom fails SC 1.4.4.

## Reflow and zoom

Content must work at 320 CSS px width — what SC 1.4.10 Reflow tests, using 400% zoom on a 1280px viewport — with no two-dimensional scrolling and nothing clipped. SC 1.4.4 separately requires text to survive 200% resize; px type does respond to browser zoom, but it ignores a user's font-size preference (`references/designing-text.md`).

Farga's grids collapse below 720px ✓, but check the fixed `25ch` sidebars, the drawer width, and any single-row tab bar at 320px before shipping.

## Dynamic ARIA, used sparingly

- `aria-expanded` on a disclosure control only when the native element does not already convey state — `<details>` does, a custom disclosure does not.
- `aria-labelledby` to point a dialog, region or form at the heading that names it: cheaper and more robust than repeating the words in `aria-label`.
- Anything more ambitious (combobox, tree, grid, tabs that switch panels) means implementing the full WAI-ARIA Authoring Practices pattern including its keyboard model, and testing it with a real screen reader. Farga's radio tabs deliberately use a native radio group instead ✓.
