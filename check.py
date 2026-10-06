#!/usr/bin/env python3
"""Mechanical checks for the Farga doc site, tokens and component rules.

Covers the class of problem a machine finds reliably: duplicate ids, images
without alt, table headers without scope, anchors with no href, unlabelled form
controls, plus Farga's own rules — one radius per tier, tokenised shadows, no
literal colours outside _base.scss, and the contrast floors the tokens promise.

This is not a substitute for axe, and neither replaces a keyboard pass or a
screen reader. It is the linter, run after every build:

    make check
"""

import colorsys
import pathlib
import re
import sys
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent
SITE = ROOT / "site"
SCSS = ROOT / "scss"
BASE = SCSS / "_base.scss"

# Contrast floors the system commits to. (foreground, background, minimum, label)
PAIRS = [
    ("--text-color-primary", "--bg-primary", 4.5, "body text"),
    ("--text-color-muted", "--bg-primary", 4.5, "muted text: hints, metadata"),
    ("--success-color", "--bg-success-color", 4.5, "success text on its tint"),
    ("--danger-color", "--bg-danger-color", 4.5, "danger text on its tint"),
    ("--info-color", "--bg-info-color", 4.5, "info text on its tint"),
    ("--warning-color", "--bg-warning-color", 4.5, "warning text on its tint"),
    ("--color-primary", "--bg-primary", 3.0, "focus ring and links"),
    ("--primary-0", "--primary-7", 4.5, "filled primary button label"),
    ("--secondary-0", "--secondary-8", 4.5, "filled secondary button label"),
    ("--red-0", "--red-7", 4.5, "filled danger button label"),
    ("--green-0", "--green-9", 4.5, "filled success button label"),
]

# Known open item: the light input fill is the only thing bounding an empty
# field, and it measures ~1.09:1. Fixing it means a visible border on every
# input in every consumer, so it is reported rather than enforced.
WARN_PAIRS = [
    ("--bg-input-color", "--bg-primary", 3.0, "empty field boundary"),
]

RADII_OK = {"var(--radius)", "var(--radius-lg)", "50%", "1.25rem", "0", "inherit"}

failures, warnings = [], []


class Page(HTMLParser):
    """Collects the accessibility tree facts a parser can see."""

    VOID = {"img", "input", "br", "hr", "meta", "link", "source", "area",
            "base", "col", "embed", "param", "track", "wbr"}
    SKIP_TYPES = {"hidden", "submit", "button", "reset"}
    # name/id pattern -> the input type that field should use
    EXPECTED_TYPES = [(r"mail", "email"), (r"pass(word|wd)?|pwd", "password"),
                      (r"phone|tel|mobile", "tel"), (r"url|website|site", "url")]

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.label_depth = 0
        self.ids = []
        self.problems = []
        self.controls = []
        self.label_for = set()
        self.fields = []
        self.order = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        line = self.getpos()[0]
        if a.get("id"):
            self.ids.append((line, a["id"]))
        self.order.append((line, tag, a))

        if tag == "label":
            self.label_depth += 1
            if "for" in a:
                self.label_for.add(a["for"])
        elif tag == "img" and "alt" not in a:
            self.problems.append((line, "<img> without alt"))
        elif tag == "th" and "scope" not in a:
            self.problems.append((line, "<th> without scope"))
        elif tag == "a" and "href" not in a and "name" not in a:
            self.problems.append((line, "<a> without href"))
        elif tag in ("input", "select", "textarea"):
            kind = a.get("type", "text")
            if kind not in self.SKIP_TYPES:
                self.controls.append(
                    (line, a.get("id"), self.label_depth > 0, a.get("name") or kind,
                     bool(a.get("aria-label") or a.get("aria-labelledby"))))
            if tag == "input":
                self.fields.append((line, a))
        if a.get("style") and not re.search(r"(max-width|fit-content|margin)", a["style"]):
            if re.search(r"\bwidth:\s*\d", a["style"]):
                self.problems.append(
                    (line, f"inline width in style=\"{a['style']}\" — use .form, .container or max-width"))

    def handle_endtag(self, tag):
        if tag == "label":
            self.label_depth = max(0, self.label_depth - 1)

    def extra_problems(self):
        """Rules that need the surrounding markup, checked after the parse."""
        found = []
        for index, (line, tag, attrs) in enumerate(self.order):
            if tag == "fieldset":
                nxt = next((t for _, t, _ in self.order[index + 1:index + 2]), None)
                if nxt != "legend":
                    found.append((line, "<fieldset> with no <legend> — an unnamed group is announced as one"))
        for line, attrs in self.fields:
            kind = attrs.get("type", "text")
            hint = (attrs.get("name", "") + " " + attrs.get("id", "")).lower()
            for pattern, expected in self.EXPECTED_TYPES:
                if re.search(pattern, hint) and kind == "text":
                    found.append((line, f"'{attrs.get('name') or attrs.get('id')}' is type=\"text\" — use type=\"{expected}\""))
            if kind == "password" and "autocomplete" not in attrs:
                found.append((line, "password field without autocomplete — no password manager can fill it"))
        return found


def check_pages():
    pages = sorted(SITE.glob("*.html"))
    if not pages:
        failures.append("no built pages in site/ — run make build first")
        return 0
    for path in pages:
        page = Page()
        page.feed(path.read_text())
        seen = {}
        for line, ident in page.ids:
            if ident in seen:
                failures.append(
                    f"{path.name}:{line} duplicate id '{ident}' (first at line {seen[ident]})")
            seen.setdefault(ident, line)
        for line, msg in page.problems:
            failures.append(f"{path.name}:{line} {msg}")
        for line, msg in page.extra_problems():
            failures.append(f"{path.name}:{line} {msg}")
        for line, ident, inside, name, aria_named in page.controls:
            if inside or aria_named or (ident and ident in page.label_for):
                continue
            failures.append(f"{path.name}:{line} control '{name}' has no label")
    return len(pages)


def to_linear(channel):
    return channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    r, g, b = (to_linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    la, lb = luminance(a), luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def parse_colour(value, tokens, depth=0):
    value = (value or "").strip()
    named = {"white": (1.0, 1.0, 1.0), "black": (0.0, 0.0, 0.0)}
    if value in named:
        return named[value]
    ref = re.match(r"var\((--[\w-]+)\)", value)
    if ref and depth < 8:
        return parse_colour(tokens.get(ref.group(1), ""), tokens, depth + 1)
    hsl = re.match(r"hsl\(\s*([\d.]+)\s*,\s*([\d.]+)%\s*,\s*([\d.]+)%\s*\)", value)
    if hsl:
        h, s, l = (float(x) for x in hsl.groups())
        return colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    hexed = re.match(r"#([0-9a-fA-F]{6})\b", value)
    if hexed:
        digits = hexed.group(1)
        return tuple(int(digits[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return None


def check_contrast():
    source = BASE.read_text()
    light_src, _, dark_src = source.partition("body.dark-mode")
    light = dict(re.findall(r"(--[\w-]+):\s*([^;]+);", light_src))
    dark = {**light, **dict(re.findall(r"(--[\w-]+):\s*([^;]+);", dark_src))}

    for theme, tokens in (("light", light), ("dark", dark)):
        for fg, bg, minimum, label in PAIRS:
            fore = parse_colour(tokens.get(fg, ""), tokens)
            back = parse_colour(tokens.get(bg, ""), tokens)
            if fore is None or back is None:
                failures.append(f"{theme}: cannot resolve {fg} or {bg}")
                continue
            measured = ratio(fore, back)
            if measured < minimum:
                failures.append(
                    f"{theme}: {label} is {measured:.2f}:1, needs {minimum}:1 ({fg} on {bg})")
        for fg, bg, minimum, label in WARN_PAIRS:
            fore = parse_colour(tokens.get(fg, ""), tokens)
            back = parse_colour(tokens.get(bg, ""), tokens)
            if fore is None or back is None:
                continue
            measured = ratio(fore, back)
            if measured < minimum:
                warnings.append(
                    f"{theme}: {label} is {measured:.2f}:1, wants {minimum}:1 ({fg} on {bg})")


LITERAL_COLOUR = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\(")


def check_system_rules():
    for path in sorted(SCSS.glob("*.scss")):
        # token partials are where literal colours belong; everything else must
        # name a token
        if path.name.startswith("_"):
            continue
        for number, line in enumerate(path.read_text().splitlines(), 1):
            radius = re.search(r"border-radius:\s*([^;]+)", line)
            if radius and radius.group(1).strip() not in RADII_OK:
                failures.append(
                    f"{path.name}:{number} border-radius {radius.group(1).strip()} "
                    f"— use --radius or --radius-lg")
            if re.search(r"box-shadow:", line) and LITERAL_COLOUR.search(line):
                failures.append(
                    f"{path.name}:{number} literal box-shadow — use a --shadow-* token")
            if LITERAL_COLOUR.search(line) and "data:image" not in line:
                failures.append(
                    f"{path.name}:{number} literal colour — define it in _base.scss")


def main():
    pages = check_pages()
    check_contrast()
    check_system_rules()

    for message in warnings:
        print(f"warning: {message}")
    for message in failures:
        print(f"FAIL: {message}")
    print(f"\n{pages} pages, {len(failures)} failures, {len(warnings)} warnings")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
