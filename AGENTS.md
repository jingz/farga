# Agent Guidelines (Farga)

Farga is a minimalistic CSS design system. When working on this project, adhere to the following philosophy:

## 1. Native Over JS (YAGNI)
- **CSS First**: Prefer native HTML/CSS features (e.g., `<details>` for accordions, CSS grid/flexbox) over JavaScript. No JS frameworks.
- **No Boilerplate**: Build only what is requested. Avoid speculative abstractions or complex class hierarchies. 
- **Minimal Dependencies**: Do not add dependencies for things that can be done with a few lines of SCSS or standard Python libraries.

## 2. Agent-First & Token Efficiency
- **Built for Agents**: Tailored specifically for AI agent consumption and code generation.
- **Token Economy**: Maximize UI building blocks while keeping context consumption low. Every component should be expressive with minimal tokens.
- **Predictable Semantics**: Rely on standard HTML5 tags and concise class names instead of deeply nested wrapper trees. Agents can generate correct UI on the first pass without bloated context prompts.

## 3. Structure & Tooling
```
.
├── scss/                  # SCSS source files
│   ├── _base.scss         # Global variables & theme definitions
│   ├── main.scss          # Primary entry point (compiles to farga.css)
│   ├── all.scss           # Uncompressed/full bundle entry point
│   └── *.scss             # Modular component styles (e.g., button, card)
├── templates/             # Jinja2 doc site templates
│   ├── layout/base.html   # Base page layout
│   └── pages/*.html       # Component demo pages (source for site/*.html)
├── site/                  # Built static doc site (committed / served)
│   └── assets/            # Compiled CSS, images, icons
├── main.py                # Static site generator (renders templates to site/)
└── Makefile               # Build automation (`make build`, `make open`)
```
- **Prerequisites**:
  - `sass` must be installed globally (e.g., `npm install -g sass` or `brew install sass/sass/sass`).
  - `uv` is used to run Python tooling.
- **Commands**:
  - `make build`: Compiles all SCSS bundles and renders HTML templates.
  - `make farga.css`: Compiles compressed `site/assets/farga.css`.
  - `make farga.all.css`: Compiles uncompressed `site/assets/farga.all.css`.
  - `uv run main.py`: Generates static doc pages from `templates/pages/` into `site/`.
  - `make open`: Opens `site/index.html` in the browser.
  - `make clean`: Removes compiled CSS artifacts.
- **SCSS**: Modular component styles belong in `scss/` (e.g., `button.scss`). Global variables belong in `_base.scss`.
- **Templates**: Standard Jinja2 templates live in `templates/`. Keep them simple and static.

## 4. Code Adjustments
- Find the shortest, simplest path that solves the problem. 
- Reuse existing classes, variables, and components before writing new ones.
- Fix the root cause, not the symptom.
