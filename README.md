<div align="center">
  <img width="180px" src="./site/assets/olives.png" alt="" />
</div>

# Farga

**A CSS design system for server-rendered applications.** Semantic HTML looks right with no
classes at all — a `<form>`, a `<table>`, a `<details>`, a `<dialog>` — and 17 components cover
the rest. No JavaScript ships, and a consumer never runs `sass`.

- **Docs and component bench** — https://jingz.github.io/farga/site/index.html
- **Repository** — https://github.com/jingz/farga

| Artifact | Contents | Raw | gzip -9 | brotli -q11 |
|---|---|---|---|---|
| `site/assets/farga.css` | core components — the file most consumers take | 35.8 kB | 7.2 kB | 6.2 kB |
| `site/assets/farga.all.css` | core plus the utility classes and the rest of the palette | 62.1 kB | 13.2 kB | 10.6 kB |

`farga.css` is minified by the build; `farga.all.css` is left readable. Both are committed, so
consumption is a copy, not a build.

## Use it

Copy the compiled stylesheet into your application's static files and link it:

```bash
cp site/assets/farga.css /path/to/app/static/css/farga.css
```

```html
<link rel="stylesheet" href="/static/css/farga.css">
```

Inside that stylesheet is a layer of CSS custom properties — colours, spacing, type, radius,
elevation, control height, form widths — and every component reads from it. Override a token
in your own stylesheet to adjust the system; there is one palette, not a theming engine:

```css
:root { --primary-7: hsl(215, 55%, 41%); --radius: 0.75rem; }
```

Dark mode is a class on `<body>`: add `dark-mode` and the token block swaps. The doc site reads
`prefers-color-scheme` for a first visit and stores the choice after that.

## Components

accordion · alert · avatar · badge · button · card · detail list · dialog · drawer · empty
state · form controls (input, select, textarea, checkbox, radio, switch, field row) · layout
(container, flex, sidebar, golden, holy grail, grid) · navigation (basic, side menu, tabs,
breadcrumbs, pagination, dropdown) · popover and tooltip · table (striped, fixed header, fixed
first column) · typography · word card.

Each has a page with markup you can copy: [accordion](https://jingz.github.io/farga/site/accordion.html),
[alert](https://jingz.github.io/farga/site/alert.html),
[form controls](https://jingz.github.io/farga/site/form.html),
[form layouts](https://jingz.github.io/farga/site/form_with_layout.html),
[table](https://jingz.github.io/farga/site/table.html) — the rest are in the sidebar of the docs.

### Avatar

Initials or an image, in three sizes:

```html
<span class="avatar" role="img" aria-label="Jane Doe">JD</span>
<span class="avatar large"><img src="/avatar.jpg" alt="Jane Doe"></span>
```

### Empty state

For a list, search or inbox with nothing in it. It names what would appear there and offers the
action that creates it — a blank surface tells the user nothing:

```html
<div class="empty-state">
  <h3>No saved words yet</h3>
  <p>Words you save while reading will show up here, newest first.</p>
  <a class="btn btn-small" href="/today">Browse today's words</a>
</div>
```

### Grid layouts

`.grid-auto` fits as many columns as the container allows; `.grid-2`, `.grid-3` and `.grid-4`
are fixed and collapse to one column below 720px:

```html
<div class="grid-auto">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>
```

### Detail list

Key/value pairs for record detail views:

```html
<dl class="detail-list">
  <dt>Email</dt>
  <dd>user@example.com</dd>

  <dt>Active</dt>
  <dd>Yes</dd>
</dl>
```

### Form column widths

A form is as wide as its content needs. Three widths ship: `.form-narrow` (24rem) for a
two-field form, `.form` (36rem) for a standard one, `.form-wide` (48rem) for a row of controls.

```html
<form class="form-narrow">
  <p>
    <label for="email">Email</label>
    <input id="email" type="email" autocomplete="email" required>
  </p>
  <footer class="actions">
    <a href="/reset">Forgot your password?</a>
    <button type="submit">Sign in</button>
  </footer>
</form>
```

## Development

**Prerequisites**

- `sass` — `npm install -g sass` or `brew install sass/sass/sass`
- `uv`, which runs the Python tooling. `make build` calls `uv run main.py`, so Jinja2 has to be
  importable in the environment `uv` resolves (or set one up here with
  `uv venv && uv pip install jinja2`).

**Commands**

| Command | Does |
|---|---|
| `make build` | Compiles both bundles, then renders every doc page into `site/` |
| `make check` | Builds, then runs the quality gate (see below) |
| `make size` | Prints raw, gzip and brotli sizes for both bundles |
| `make open` | Opens `site/index.html` |
| `make farga.css` / `make farga.all.css` | Compiles one bundle only |
| `make clean` | Removes the compiled CSS |

`site/` is committed: a change is not finished until the matching `site/*.html` and
`site/assets/*.css` are regenerated, so commit sources and build output together.

## Quality gate

`make check` exits non-zero on any failure, which makes it the definition of ready to commit. It
checks every built page for duplicate ids, images without `alt`, table headers without `scope`,
anchors without `href`, controls without a label, fieldsets without a legend, wrong input types
and missing `autocomplete`; the token set for 11 contrast pairs in **both** light and dark; and
the component rules — one radius per tier, elevation only from `--shadow-*`, and no literal
colour outside the token partials.

It is a linter, not a substitute for looking at the page. Keyboard traversal, a screen reader,
the 320px reflow pass and whether the copy makes sense are still manual.

## Project structure

```
.
├── scss/                  # one file per component, named after what it styles
│   ├── _base.scss         # tokens: colour, spacing, type, radius, shadow, themes
│   ├── _palette.scss      # the eight hues only the utilities use — all.css, not core
│   ├── reset.scss         # reset, the global focus ring, reduced motion
│   ├── main.scss          # → site/assets/farga.css (core)
│   └── all.scss           # → site/assets/farga.all.css (core + utilities + palette)
├── templates/
│   ├── layout/base.html   # doc shell
│   └── pages/*.html       # one demo page per component
├── site/                  # generated docs + compiled CSS (committed, never edited by hand)
├── main.py                # renders templates/pages/*.html into site/
├── check.py              # the quality gate
├── Makefile              # build, check, size, open, clean
└── AGENTS.md             # contributor and agent guidelines — read this before changing SCSS
```

**Adding a component** means four things: `scss/<name>.scss`, `@use` in **both** entry points, a
demo page under `templates/pages/`, and an entry in the Components group of
`templates/layout/base.html`. `AGENTS.md` has the rest — where tokens may live, why the button
padding scale is in pixels, and what the gate cannot see.

## License

No licence file yet. Until one is added, the default applies: all rights reserved, so ask before
reusing this in your own project.
