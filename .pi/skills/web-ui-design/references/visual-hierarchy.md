# Visual Hierarchy & Micro-Design Polish

From *Refactoring UI* (Wathan & Schoger). This is the short delta — for the full treatment of type scale, color, spacing, depth, and copy, read the `refactoring-ui` skill if the workspace has it.

## Hierarchy & layout

- **Start with a feature**: do not begin by designing a generic shell or header/footer frame. Build the core interactive feature first, then assemble the surrounding interface around it.
- **Data presentation**: do not label every piece of data when the context or format already conveys it. A formatted price, a timestamp, and an email address do not need a caption.
- **Spacing is its own discipline**: the scale, container widths and the grouping rule live in `references/layout-and-spacing.md`.

## Button sizing and padding ratios

Padding must not scale proportionally with font size (do not define it in `em` off the font size). If it does, small buttons look bloated and large ones look cramped. The padding-to-font ratio has to *grow* with the button:

| Tier | Font size | Padding | Padding ÷ font (Y / X) | Derived height |
|---|---|---|---|---|
| Extra small | 12px | `6px 8px` | 0.50 / 0.67 | 24px |
| Small | 14px | `8px 10px` | 0.57 / 0.71 | 30px |
| Medium | 16px | `12px 16px` | 0.75 / 1.00 | 40px |
| Large | 20px | `15px 30px` | 0.75 / 1.50 | 50px |

This is the scale Farga already ships, by class:

| Class | Font size | Padding |
|---|---|---|
| `.btn-small` | 12px | `6px 8px` |
| `button` / `.btn` (base) | 14px | `8px 10px` |
| `.btn-large` | 16px | `12px 16px` |
| `.btn-extra` | 20px | `15px 30px` |

Use those classes rather than re-deriving padding. Matching the size tier to a foreign scale is the fastest way to make a Farga UI look off.

Touch targets are separate from visual size: a 24px-tall button still needs a hit area that satisfies `references/mobile-touch-inputs.md`. Grow the *hit area* (padding, or a transparent overlay for icon-only controls), never the visible geometry in a way that breaks the ratios above.

Contrast floors for fills, borders and focus rings are in `references/accessible-components.md`.

## Button hierarchy and consistency

- **One shape per group**: primary, secondary and tertiary buttons sitting together keep the same border radius and height tier. Only fill and border change between tiers — never mix pills, ovals and rounded rectangles in one group. Farga uses `0.5rem` for every button variant.
- **Tiers**:
  - **Primary** — solid fill, high contrast label. One per view.
  - **Secondary** — outlined, same shape and height as primary.
  - **Tertiary** — borderless ghost or plain link.
- **Destructive actions** stay in the secondary tier until a confirmation step, then may become primary red.

## Contrast and stroke width

The normative floor (WCAG 2.2 SC 1.4.11, AA) is **3:1** for the visual information that identifies a UI component or its state. W3C's own low-vision work raises the bar for thin marks, because anti-aliasing renders a 1px line noticeably fainter than the colour you authored:

- **Filled button labels**: 4.5:1 against the fill (SC 1.4.3).
- **Thin strokes and icons, under 3 CSS px**: 4.5:1 against adjacent colours (recommended by W3C's Low Vision task force, not required by 2.2).
- **Thick strokes, 3 CSS px and above**: 3:1 — the normative floor.
- **Focus indicators**: 3:1 against the adjacent background (SC 1.4.11).

## Finishing touches
- **Accent borders**: a subtle colored top or side border reinforces a primary card without overwhelming it.
- **Empty states**: never show a bare layout on a new account or a filtered-to-nothing list. Design a dedicated empty state with an icon, explanatory copy, and an action button.
- **Shadows and elevation**: `references/depth-and-shadow.md` — one overhead light source, a five-tier scale, and the layered-shadow recipe.
