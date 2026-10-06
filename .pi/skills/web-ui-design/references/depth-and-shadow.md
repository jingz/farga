# Depth & Shadow

## One overhead light source

Every shadow in the interface should be consistent with a single light above the screen.

- **Raised elements** cast down: a shadow with a positive vertical offset, never a shadow above the element.
- **Recessed wells** — an inset panel, a sunken field — are lit on the bottom inner edge, because light from above catches the lip. That is an *inset* shadow with a negative offset:

```css
/* illuminated bottom lip of a recessed well */
box-shadow: inset 0 -2px 0 hsla(0, 0%, 100%, 0.15);
```

Dropping `inset` here is the common mistake: without it the same declaration paints a light bar *below* the element instead of inside it, which reads as a second, broken highlight.

## Use an elevation scale, not one-off shadows

Define the shadows once as tokens and assign them by layer. A workable five-tier set:

| Tier | Use | Value |
|---|---|---|
| 1 | Buttons, subtle lift | `0 1px 3px hsla(0, 0%, 0%, 0.2)` |
| 2 | Cards, drag targets | `0 4px 6px hsla(0, 0%, 0%, 0.2)` |
| 3 | Dropdowns, menus | `0 5px 15px hsla(0, 0%, 0%, 0.2)` |
| 4 | Flyouts, popovers | `0 10px 24px hsla(0, 0%, 0%, 0.2)` |
| 5 | Modals, dialogs | `0 15px 35px hsla(0, 0%, 0%, 0.2)` |

Farga currently has no scale: `dialog` is `0 8px 24px`, `drawer` `-8px 0 24px`, `popover` `0 4px 16px`, all `rgba(0,0,0,.15)`, plus `0 1px 2px rgba(0,0,0,.35)` on the switch and checkbox knobs. Three dialog-layer surfaces with three different depths is the symptom. Adopt the table as `--shadow-1` … `--shadow-5` and map the components onto it.

Also worth promoting: `learner.css` in the app already uses a *brand-tinted* shadow, `0 0.75rem 2rem rgba(35, 61, 95, 0.1)`. A shadow tinted with the brand hue looks more intentional than flat black and costs nothing. Prefer it for elevated surfaces, keeping black for the tight contact shadow.

## Layer two shadows for realism

A single soft shadow looks synthetic. Stack a tight, darker contact shadow with a wide, faint directional one:

```css
box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15),
            0 3px 6px rgba(0, 0, 0, 0.10);
```

The contact shadow matters most at low elevations and fades out as elements rise: a button sits close to the page, a modal does not.

## Flat depth, and overlapping planes

- In a flat visual language, a **hard-edged shadow** with no blur reads as depth without any fuzz: `box-shadow: 0 3px 0 hsl(...)`. Use one or the other — flat offsets and soft elevations in the same view look like a mistake.
- **Overlap** establishes planes more strongly than any shadow: a card pulled up across a banner edge, an avatar breaking its container's corner. Negative margins or a transform are enough.

## Dark mode

Shadows are nearly invisible on a dark background. Do not rely on elevation alone — indicate raised surfaces with a lighter surface colour instead, and keep any remaining shadow tight.
