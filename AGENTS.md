# Agent Guidelines (Farga)

Farga is a minimalistic CSS design system: SCSS sources, compiled stylesheets, and a
documentation site that doubles as the component bench. These guidelines govern how it is
built, extended and shipped.

---

## 1. Project overview

**What it is.** ~2,600 lines of SCSS across 21 files, compiling to two stylesheets:

| Artifact | Contents | Raw | gzip -9 | brotli -q11 |
|---|---|---|---|---|
| `site/assets/farga.css` | core components — the file consumers take | 37.4 kB | 7.5 kB | 6.3 kB |
| `site/assets/farga.all.css` | core plus the opt-in utility classes | 60.8 kB | 12.9 kB | 10.3 kB |

`farga.css` is minified by the build (`sass --style=compressed`), so it has no separate
minification step; `farga.all.css` is deliberately left readable. Compression is the
server's job — the same source is 5.0× smaller gzipped and 5.9× smaller as brotli, so quote
the brotli column when someone asks what the stylesheet costs over the wire. Regenerate
these numbers with `make size` whenever the CSS changes materially.

The only build tooling is the `sass` binary and a 27-line Jinja2 static site generator
(`main.py`). There is no npm, no bundler, no PostCSS and no framework.

**What ships.** No JavaScript. Every interactive component is a native element: `<details>`
for accordions and menus, `<dialog>` for modals, the popover API for the drawer, a checkbox
for the switch, radio inputs for tabs. Tooltips are the one exception worth knowing about —
their text comes from a CSS `::after` with `attr()`, which is why the skill says never to
make a tooltip the only place information exists. The doc site carries ~40 lines of inline
JS for its theme toggle and active-nav highlight; none of it is part of the stylesheet, and
no consumer needs it.

**Two layers, one intent.** Styling comes from element selectors first — a `<form>`, a
`<table>`, a `<details>` look right with no classes at all — and classes only where a
variant or a composite is genuinely needed (`<button class="btn-danger">`,
`<div class="card">`, `<nav class="sidemenu">`).

**Components.** accordion · alert · avatar · badge · button · card · detail list · dialog ·
drawer · empty state · form controls (input, select, textarea, checkbox, radio, switch,
field row) · layout (container, flex, sidebar, golden, holy grail, grid) · navigation
(basic, side menu, tabs, breadcrumbs, pagination, dropdown) · popover and tooltip ·
table (striped, fixed header, fixed first column) · typography · word card. `utilities.scss`
holds the colour, alignment and text-align helpers and is the only part not in `farga.css`.

**How it is consumed.** As a git submodule by server-rendered applications, which take the
*compiled* CSS and never the SCSS — news-v2 copies `site/assets/farga.css` into
`application/static/css/farga.css`. The compiled output is committed here on purpose, so a
consumer never has to run `sass`.

**Versioning** is the git commit: 100 commits, no tags, no releases, no package manifest.

---

## 2. Project domain

**Who it serves.** Server-rendered applications that want a complete component vocabulary
without a JavaScript build — in practice two kinds of screen:

- **Admin and CRUD** — data tables, filter drawers, pagination, dense forms. This is where
  the design language is at its most utilitarian: 14px base size, compact control heights,
  one accent colour.
- **Content and reading** — editorial pages, articles, definition or word cards. Here the
  serif headings, the `--text-color-muted` metadata and the `.prose` measure do the work.

**Design language.** Muted slate-blue brand (`--primary-*`, 215°/55%) with a teal secondary
(170°/48%), pure-grey neutrals, a serif for headings and a sans for body text, light and
dark themes driven by a `body.dark-mode` class. The palette is deliberately quieter than the
status colours so alerts and errors can shout.

**What it is not, on purpose:**

- Not utility-first. `utilities.scss` is a small opt-in layer; layout comes from a handful
  of composite classes, not a class per property.
- Not a JavaScript component library.
- Not a theming engine. Tokens are CSS custom properties, but there is one palette; rebranding
  means editing `_base.scss`, which is fine and should not be blunted by indirection.
- Not internationalised. No RTL, no logical-property pass, English copy in the docs.
- No licence file yet. If this is meant to be an independent open-source project, that is a
  gap to close rather than assume.

---

## 3. Setup and management

**Prerequisites**

- `sass` installed globally — `npm install -g sass` or `brew install sass/sass/sass`.
- `uv`, which runs the Python tooling. `make build` calls `uv run main.py`; `uv` resolves
  the enclosing project's environment (jinja2 must be importable there), or set one up here
  with `uv venv && uv pip install jinja2`.

**Commands**

| Command | Does |
|---|---|
| `make build` | Compiles both bundles, then renders every doc page into `site/` |
| `make check` | `build`, then the quality gate in section 5. **Run before every commit** |
| `make farga.css` | Compiles the compressed core bundle only |
| `make farga.all.css` | Compiles the uncompressed core + utilities bundle only |
| `make open` | Opens `site/index.html` |
| `make clean` | Removes the compiled CSS |

**Managing the build output.** `site/` is committed, so a change is not finished until the
matching `site/*.html` and `site/assets/*.css` are regenerated — commit sources and build
output together, never one without the other. Never hand-edit anything under `site/` or
`site/assets/`; it is generated. Sourcemaps (`*.map`) are gitignored and not published.

**Managing this repository as a submodule.** This project is vendored by other repositories,
so it has to stand alone:

- Commit and push here first; the parent repository then records the new commit as its
  gitlink. Never make the parent's changes depend on an unpushed commit here.
- Keep everything generic. No product names, routes, models or business rules from a
  consumer belong in this repository — if a consumer needs something specific, it belongs
  in that consumer's own stylesheet, driven by the tokens exported here.
- A new generic component or style belongs in this repository first, then gets copied into
  the consumer's compiled `farga.css`.

---

## 4. Project structure

```
.
├── scss/                     # SCSS sources; one component per file
│   ├── _base.scss            # tokens: colours, spacing, type, radius, shadow, themes
│   ├── main.scss             # entry point → site/assets/farga.css (core)
│   ├── all.scss              # entry point → site/assets/farga.all.css (core + utilities)
│   └── *.scss                # components, named after what they style
├── templates/
│   ├── layout/base.html      # doc shell: nav tree, section rhythm, theme script
│   └── pages/*.html          # one demo page per component (source for site/*.html)
├── site/                     # generated doc site + compiled CSS (committed, never edited)
├── main.py                   # renders templates/pages/*.html into site/
├── check.py                  # the quality gate (section 5)
├── Makefile                  # build, check, open, clean
└── .pi/skills/web-ui-design/ # the design and accessibility skill, with its references
```

**Adding a component** means four things, or it is not finished: `scss/<name>.scss`,
registered with `@use` in **both** `main.scss` and `all.scss`, a demo page in
`templates/pages/`, and an entry in the Components group of `templates/layout/base.html`.

**Where things belong**

- Tokens — every colour, radius, shadow, spacing value and theme override — live in
  `_base.scss` and nowhere else. A literal colour outside that file fails the gate.
- Geometry comes from the tokens: `--radius` / `--radius-lg` for corners, `--shadow-1..5` for
  elevation, `--px-*` for space, `--fs-*` for type, `--control-h` for the minimum height of a
  control. Picking a number that is not on a scale is the mistake this gate exists to catch.
- Component-internal padding for buttons and menu rows is its own documented scale, in pixels,
  and is intentionally not the `--px-*` spacing scale.
- Demo markup must be the real thing: a doc page teaches by being copied, so what is shown
  has to be what the system sanctions.

---

## 5. Quality gate

`make check` builds, then runs `check.py`. It exits non-zero on any failure, so it is the
definition of "ready to commit". It is a linter, not a substitute for looking at the page.

**Every built page is checked for**

- duplicate `id`s, `<img>` without `alt`, `<th>` without `scope`, `<a>` without `href`
- form controls with no label: no wrapping `<label>`, no `for=` target, no `aria-label`
- `<fieldset>` without a `<legend>` — an unnamed group is announced as one
- `type="text"` on a field whose name or id says email, password, phone or url
- a password field without `autocomplete`, so no password manager can fill it
- a pixel `width` in an inline `style` attribute

**The token set is checked for**

- 11 contrast pairs in **both** light and dark: body text, muted text, each semantic
  text-on-tint pair, the focus ring, and the label on each filled button variant. Floors are
  4.5:1 for text and 3:1 for the focus indicator.
- two warnings that are reported but do not fail: the empty-field boundary
  (`--bg-input-color`), which needs a border-versus-fill decision rather than a build error.

**The component rules are checked for**

- `border-radius` must be `var(--radius)`, `var(--radius-lg)`, `50%`, `1.25rem`, `0` or
  `inherit` — one radius per tier, so a control never disagrees with the control beside it
- no literal `box-shadow`; elevation comes from `--shadow-*`
- no literal colour outside `_base.scss`

If a rule is wrong, fix `check.py` — do not weaken it silently and do not add a component to
an allow-list to make it pass.

**What the gate cannot see, and a human must:** keyboard traversal, focus order and visible
focus, a real screen reader, the 320px reflow pass (the doc pages should fit with no
horizontal scrolling), animation under `prefers-reduced-motion`, and whether the copy and
the placeholder examples make sense. `references/evaluation-and-prioritization.md` in the
skill covers the manual pass and how to triage what it finds.

---

## 6. Design philosophy

### Native Over JS (YAGNI)
- **CSS First**: Prefer native HTML/CSS features (e.g., `<details>` for accordions, CSS grid/flexbox) over JavaScript. No JS frameworks.
- **No Boilerplate**: Build only what is requested. Avoid speculative abstractions or complex class hierarchies.
- **Minimal Dependencies**: Do not add dependencies for things that can be done with a few lines of SCSS or standard Python libraries.

### Agent-First & Token Efficiency
- **Built for Agents**: Tailored specifically for AI agent consumption and code generation.
- **Token Economy**: Maximize UI building blocks while keeping context consumption low. Every component should be expressive with minimal tokens.
- **Predictable Semantics**: Rely on standard HTML5 tags and concise class names instead of deeply nested wrapper trees. Agents can generate correct UI on the first pass without bloated context prompts.
- **Accessible by default**: Native elements first, focus never removed, contrast enforced
  by the gate. The rules and the reasoning are in `.pi/skills/web-ui-design/`.

---

## 7. Code Adjustments
- Find the shortest, simplest path that solves the problem.
- Reuse existing classes, variables, and components before writing new ones.
- Fix the root cause, not the symptom.
- Check what already consumes a shared rule before changing it: several of the bugs fixed
  in this system were one broad selector (`form div`) reaching into a component.
