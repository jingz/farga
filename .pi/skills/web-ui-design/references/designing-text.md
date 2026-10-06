# Designing Text

## Use a scale, not taste

Define the sizes once and never type a number that is not on the scale. A workable set: 12, 14, 16, 18, 20, 24, 30, with 36/48/60/72 above for display. Choosing 13px, 15px and 17px in the same screen is the tell that there is no scale.

Farga ships `--fs-0` through `--fs-11`: 10, 12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72px. Use those tokens. They are **px-based**, so they ignore a user's larger browser font size — that is the project's decision, not a licence to add more px sizes on top.

Two exceptions worth knowing: `--fs-0` (10px) is below the comfortable reading floor and is currently used for tooltips, and the base size is 14px, which is dense for long-form reading. Do not go below 12px for anything a user must read.

## Two weights are enough

- Normal (400, or 500 for a typeface that needs it) for body copy.
- Heavy (600/700) for headings and emphasis.

Nothing lighter. Weights under 400 lose their strokes at UI sizes, and never de-emphasise by switching to a light weight — use a lighter colour or a smaller size instead. Farga follows this already: 400 and 700 only, with `bold` for active navigation and tabs.

Watch the trade-off on muted text: `--text-color-muted` measures **3.98:1** on white. Fine at 18px+ or bold, a failure for 14px body copy. `references/accessible-components.md` has the measured table.

## Font choice, and the fallback nobody checks

Neutral, tall x-height sans-serifs for UI (Helvetica, Arial, Roboto, the system stack); avoid condensed or low-x-height faces for interactive elements; prefer battle-tested pairings for display faces rather than an untested combination.

Farga declares `Arial, sans-serif` for UI and `Palatino, serif` for headings, and loads **no webfont**. Palatino is not installed on Windows or Android, so the editorial serif identity collapses to a generic serif on those platforms — the look you approve on macOS is not what most users see. Either ship the font, or choose a stack whose first family you are willing to lose.

`.ft-fantasy` (Papyrus) and `.ft-cursive` (Brush Script MT) also exist as utilities. They are decoration, not a text treatment.

## Input width is part of the label

Do not stretch every input to 100% of its container. A field sized for what it expects — a birth year that fits four characters, a ZIP, a country code — reads faster and signals what to type before the user starts.

In Farga, `form label input { width: 100% }` and `select` fill their container by default, so size a field with the layout (`.field-row`, a grid column, a narrower wrapper) rather than inline styles. `form.html` in the docs shows the grid approach.
