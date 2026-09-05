<div align="center">
  <img width="180px" src="./site/assets/olives.png" />
</div>

# Farga
**CSS Design System**

Farga is a CSS design system that provides a collection of reusable components and patterns to help build consistent, responsive websites and applications.

## Overview

This project combines SCSS preprocessing with static site generation to create a flexible and maintainable design system. The system includes various UI components like buttons, cards, badges, accordions, and more.

## Getting Started

### Prerequisites

You'll need to install the following tools before building the project:

- **SASS**: A CSS preprocessor that adds features like variables, nesting, and mixins
- **Python UV**: A fast Python package installer and resolver

### Installation Steps

1. **Install SASS globally**
   ```bash
   npm install -g sass
   ```

2. **Install UV Python package manager**
   ```bash
   # Follow installation guide at: https://docs.astral.sh/uv/#installation
   ```

3. **Set up the Python environment and install dependencies**
   ```bash
   # Create a virtual environment
   uv venv
   
   # Install the template engine for static site generation
   uv pip install jinja2
   ```

### Building the Project

Once everything is installed, you can build the project:

```bash
make build
```

This command will process the SCSS files and generate the static site.

## Avatar

Use `.avatar` for initials or an image. Add `.small` or `.large` when needed:

```html
<span class="avatar" role="img" aria-label="Jane Doe">JD</span>
<span class="avatar large"><img src="/avatar.jpg" alt="Jane Doe" /></span>
```

## Grid Layouts

Use `.grid-auto` for a responsive auto-fit grid, or `.grid-2`, `.grid-3`, and `.grid-4` for fixed column layouts that collapse on small screens:

```html
<div class="grid-auto">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>
```

## Detail List

Use `.detail-list` for admin record detail views and any key/value display:

```html
<dl class="detail-list">
  <dt>Email</dt>
  <dd>user@example.com</dd>

  <dt>Active</dt>
  <dd>Yes</dd>
</dl>
```

## Project Structure

- **`scss/`**: Contains all the source SCSS files for the design system
  - `_base.scss`: Base styles and global variables
  - `button.scss`: Button component styles
  - `card.scss`: Card component styles
  - `badge.scss`: Badge component styles
  - `accordion.scss`: Accordion component styles
  - `detail.scss`: Detail list component styles for record detail views
  - `all.scss`: Main file that imports all other SCSS files
- **`templates/`**: Jinja2 templates for static site generation
- **`site/`**: Output directory where the built website files are placed
- **`main.py`**: Python script for static site generation
- **`Makefile`**: Build automation commands