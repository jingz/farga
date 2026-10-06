# Accessible Component Guidelines (WCAG 2.2 AA)

Target WCAG 2.2 level AA: contrast 4.5:1 for body text and 3:1 for large text and UI components (SC 1.4.3, 1.4.11). This file holds the measured contrast table, the 5 rules of ARIA and the table rules. State cues beyond colour, focus requirements and keyboard models are in `references/visual-interaction-design.md`; implementation mechanics (CSS-generated content, user preferences, reflow) are in `references/developing-html-css-aria.md`.

## Contrast by what you are painting

The 3:1 floor in SC 1.4.11 covers the visual information that identifies a control or its state. Thin marks need more, because anti-aliasing renders a 1px line fainter than the colour you authored — W3C's Low Vision task force recommends 4.5:1 for strokes under 3 CSS px:

| Painted thing | Required | Source |
|---|---|---|
| Filled button label on its fill | 4.5:1 | SC 1.4.3 |
| Body text | 4.5:1 | SC 1.4.3 |
| Large text (18px+ bold / 24px+) | 3:1 | SC 1.4.3 |
| Border or icon stroke under 3 CSS px | 4.5:1 | W3C low-vision guidance (recommendation, not required by 2.2) |
| Border or icon stroke 3 CSS px and above | 3:1 | SC 1.4.11 |
| Focus indicator | 3:1 against adjacent colours | SC 1.4.11 |
| Component fill that is the only boundary (empty text input, switch track) | 3:1 | SC 1.4.11 |

A control whose *content* identifies it — a labelled button, a filled input — does not need its boundary to meet 3:1; an empty text field has no content to identify it, so its fill or border does the work and is in scope.

Do not assume a palette passes. Measured in Farga: `--green-0` on `--green-7` is 2.40:1, `--red-4` on white 2.99:1, `--green-7` on white 2.53:1, the grey `--bg-input-color` fill against white 1.09:1. Each fails the row it belongs to above.

## ARIA and semantics

The 5 rules of ARIA (W3C WAI-ARIA):

1. **Prefer native**: if a native HTML element or attribute already has the semantics and behavior you need, use it. `<button>`, not `<div role="button">`; `<select>`, not a hand-built dropdown.
2. **Do not override native semantics** unless you really have to.
3. **Keyboard support is mandatory** for any interactive ARIA control: Tab, Space, Enter, Escape, and arrow keys as the pattern requires.
4. **Never put `aria-hidden="true"` or `role="presentation"` on a focusable element.**
5. **Every interactive element must expose an accessible name** — via visible text, `aria-label`, or `aria-labelledby`.

## Data tables

- Give every table clear `<th>` headers with `scope="col"` or `scope="row"`.
- Use alternating row colors or border shading so low-vision users can track a row across columns.
- For complex tabular data, offer an alternative summary or plain-language description alongside it.

## Images and media

Images have their own reference: `references/working-with-images.md` covers alt text per image kind, text-in-image, cropping user uploads, and small-size icons.
