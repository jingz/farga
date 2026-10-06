# Working With Images

## Classify the image before writing the markup

| Kind | Example | Treatment |
|---|---|---|
| Decorative | Background texture, a logo beside the same word in text | `alt=""` so assistive tech skips it |
| Functional | A print or search icon button | Name the **action**, not the picture: `alt="Print"`, never `alt="Printer"`; `aria-label` for an icon-only button, plus `title` when the glyph is ambiguous |
| Complex | Infographic, diagram, chart | A plain-language summary or an accessible table next to it — the `alt` alone cannot carry it |

Never leave `alt` off entirely, and never use `aria-hidden="true"` on an image that carries meaning (it is redundant next to `alt=""` and harmful instead of it).

Farga's own docs demonstrate the first row: the sidebar logo and the GitHub mark both use `alt=""` because the adjacent text already names them.

## Never bake text into an image

Copy inside a bitmap cannot be selected, translated, zoomed, restyled, or read by a screen reader, and it goes stale the moment the words change. Render real text over a background image instead, using the project's font stack.

## Lock user uploads into a container

User-supplied media arrives at every aspect ratio there is. Do not let it into the layout at its intrinsic size — it will break the grid and reflow everything around it. Give it a fixed-ratio container and crop:

```css
.thumb { aspect-ratio: 4 / 3; overflow: hidden; }
.thumb img { width: 100%; height: 100%; object-fit: cover; object-position: center; }
```

Farga has no image component, but `.avatar` already does exactly this: a fixed 2rem/1.5rem/2.5rem square with `object-fit: cover` on the image inside. Copy that pattern for any new thumbnail, hero or card image.

## Icons are drawn, not scaled

Rendering a detailed bitmap logo at 16px does not produce a small logo, it produces a blur. Redraw simplified iconography for small sizes (favicon, app icon, avatar fallback) instead of downscaling the full-resolution artwork.

For UI icons, match the weight to the type around them and size them relative to the adjacent text line, not the touch target — the tap area comes from the button's padding, per `references/mobile-touch-inputs.md`.
