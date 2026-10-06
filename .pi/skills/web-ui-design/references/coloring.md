# Coloring

## Build a ramp per hue

A real interface needs 5–10 shades of each hue, not three. Pick a vibrant mid shade that works as a solid button fill, a very light one for tinted panels and alert fills, and a very dark one for text on light backgrounds, then interpolate the rest. Hold the hue constant and move lightness; let saturation fall slightly as you approach the light end.

Farga ships 16 hues × 10 shades (`--primary-0` … `--primary-9`, per hue). In that scale 0–2 are surfaces, 3–5 borders, 6–7 actions, 8–9 text and dark surfaces. When you need "the red one", use the ramp rather than a one-off hex.

## Assign colours to meaning, once

| Role | Where it goes |
|---|---|
| Primary / brand | Navigation highlights, links, primary buttons |
| Danger (red) | Irreversible actions, errors, failed states |
| Warning (amber) | Caution, things needing attention but not failed |
| Success (green) | Confirmations, positive trends, completed states |
| Accents (teal, pink, violet) | Categories, highlights, chart series |

Two rules that keep this honest: a semantic colour means the same thing everywhere (do not use red for "new"), and a status colour is reserved for status (do not use green as decoration).

## Saturation has to be one decision

Farga's brand hues are muted — `--primary-*` at 55% saturation, `--secondary-*` at 48% — while all twelve system hues (red, pink, grape, violet, indigo, blue, cyan, teal, green, lime, yellow, orange) sit at a flat 80%. The result is that alerts, badges and `.btn-danger`/`.btn-success` are louder than the brand they live in. Either mute the system ramps toward the brand, or accept that status outranks brand on the page — but pick one. Muting is the cheaper fix: reducing saturation 20–40% is the fastest way to make a palette look chosen.

## Do not let two names share one colour

Farga carries `--indigo` (230°), `--violet` (255°), `--blue` (208°), `--cyan` (188°) and `--teal` (162°) alongside `--primary` (215°) and `--secondary` (170°). `--primary-7` is nearly `--blue-7`; `--secondary-8` is nearly `--teal-8`. Two names for one colour guarantees drift and makes a maintainer guess which is canonical. Collapse to the brand hues plus the system states, and delete the rest.

## Greys carry the palette

Pure greys (`hsl(0,0%,x)`) next to a 215° brand read as "nobody chose these". A few percent of the brand hue — or a deliberate warm shift — makes the neutrals look like part of the same system.

## Contrast and colour-alone

Colour never carries state by itself: pair it with a label, an icon, or a border change, and check the pairing rather than assuming it passes. The contrast table, the measured Farga failures, and the state rules live in `references/accessible-components.md`.
