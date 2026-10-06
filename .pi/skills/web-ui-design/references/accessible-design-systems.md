# Accessible Design Systems

## Sequence the work people-first

A system that treats accessibility as "screen reader support" starts in the wrong place. Build in this order — each layer is harder to retrofit than the one before:

1. **Contrast and colour independence** — low vision and colour deficiency. Cheapest to fix while nothing depends on the palette.
2. **Type size, spacing, cognitive clarity** — everyone, including dyslexic and neurodivergent users.
3. **Input methods** — touch, keyboard, switch, voice (`references/mobile-touch-inputs.md`, `references/visual-interaction-design.md`).
4. **Assistive tech specifics** — accessible names, live regions, roles.

Farga's own audit ran this order backwards, semantics first, which is why the contrast failures in `references/accessible-components.md` outlived everything else.

## Type tokens and scaling

- Separate **font size** (fixed values) from **scaling** (what happens at 200% text resize and 400% zoom). A token system that encodes only px sizes silently bets against both.
- Name tokens for the role, not for a heading level: `text-body-sm`, `text-display` — not `h3`. Copy that ties body text to `<h3>` becomes unusable the moment the heading level changes. Farga's `--fs-0` … `--fs-11` are scale-named ✓ and the `h1`–`h6` mapping lives in `typography.scss`, which is the right place for it.
- Avoid ultralight brand faces: they lose strokes at UI sizes and on low-density displays. Farga uses 400 and 700 only ✓ (`references/designing-text.md`).

## Components to omit

- **Tooltips as a content channel.** No single tooltip pattern works across screen readers, and hover does not exist on touch. Keep copy inline. If a tooltip stays, it must be supplementary — Farga ships `[data-tooltip]`, so treat it as decoration and never as the only place a value or instruction is stated.
- **Custom `<div>` dropdowns.** Use the native `<select>` to choose from a list; Farga and the app already do ✓. If you genuinely need type-ahead or a multi-select combobox, that is the most defect-prone pattern in the ARIA practice guide: implement it completely, including its keyboard model, and test with a screen reader.
- Contrast for shapes, icons and strokes is in `references/accessible-components.md` — solid shapes and alert icons 3:1, thin outline strokes 4.5:1.

## Annotate at handoff

Write the accessible name, reading order, tap-target size and any live-region behaviour into the design deliverable. Unwritten intent is unshipped intent — those exact values are what gets dropped between design and code.
