# Layout & Spacing

## Start with too much white space

Start generous and remove deliberately. Packing information densely is a conscious trade-off for a data-dense screen (an ops dashboard, a financial table) — never the default. Starting cramped and trying to add air later does not work, because you end up defending the cramped layout you already built.

## One spacing and sizing scale

- Do not nitpick between 120px and 125px. Constrain yourself to a scale and take the next step when a value feels tight: 4, 8, 12, 16, 24, 32, 48, 64.
- Use `rem` for type and layout dimensions so the page respects the user's own font-size setting. Use `em` for space *inside* a component that should track that component's text size.
- Farga's scale is `--px-*`: `--px-0` is 1rem, then `--px-p1` 1.5rem, `--px-p2` 2rem, `--px-p3` 3rem, rising to 48rem. It is a 1.5× progression, not the 4px grid above. **Use it** — a second scale alongside the project's own is worse than either one alone. Note the negative tokens are named out of order: `--px-n3` is 0.25rem, `--px-n1` is 0.5rem, `--px-n2` is 0.75rem.

## Do not fill the screen

Stretching a layout to 1200–1400px because the monitor is wide makes inputs and actions hard to parse. Constrain to what the content needs and centre it with comfortable margins.

In Farga, `.container` caps at 1200px and `.prose` at 65ch. Long-form text wants the `ch` limit even inside a wide container — the container cap alone still leaves ~150 characters per line at the 14px base size.

## Spacing must show what belongs together

Space *around* a group must be strictly larger than space *within* it. Proximity is the whole mechanism by which a layout communicates structure; if the two are equal, the grouping is a guess.

Forms are where it breaks most often. If the gap between a label and its input is close to the gap between one field and the next, the label reads as belonging to the control below it. Farga's field rhythm comes from `form p { margin-bottom: 0.5rem }` plus the label's own line box, so a new field group needs visibly more space than that — a `fieldset`, a grid gap, or a section break.

## Fewer borders

Reach for a background tint, a shadow, or simply more spacing before adding another line. A border is the loudest way to separate two things and the easiest to overuse.

Farga's separator borders (`--border-color-muted`) measure 1.20:1 on white and `--border-color-primary` 2.23:1 — below the 3:1 non-text floor, which is fine for *decorative* separation between content blocks but not where a border is the only thing identifying an empty control. Those keep a strong border: `.btn-outline` uses `--color-primary` at 6.40:1. See `references/accessible-components.md` for which boundaries are in scope.
