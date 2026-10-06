# Evaluating and Prioritising Accessibility

## The toolchain, in the order it catches things

1. **Accessibility tree inspection** — Chrome/Edge DevTools → Accessibility pane. Shows the role, name and state a screen reader actually receives. This is where "the label is missing" and "the name is the entire sentence" become visible.
2. **Automated audits** — axe DevTools, Lighthouse. They catch the mechanical third: missing alt, contrast, unlabelled form fields, duplicate ids. Run them as a linter, never as proof.
3. **Keyboard-only pass** — Tab the whole page: is the order the reading order, is the ring visible on everything, do `Space`/`Enter` work, can you get out of every widget, and does anything scroll into view under a sticky header?
4. **Real assistive technology** — NVDA and JAWS on Windows, VoiceOver on macOS and iOS, TalkBack on Android. One representative combination beats none.

An automated pass reports false positives and misses context. An overlay on a broken page is a broken page with a badge on it. Neither substitutes for 1–4.

## Give every finding a severity

| Severity | Examples | Handling |
|---|---|---|
| 1 — Blocker | Keyboard trap, missing form label, content unreadable by a screen reader, flashing | Fix before the feature ships |
| 2 — High | Failing contrast on a critical control, missing captions, targets under 24px | Fix in the current cycle |
| 3 — Medium | Skipped heading level, "click here" links, no plain-text summary for a chart | Schedule |
| 4 — Low | Redundant alt text, `tabindex` on a non-interactive element | Bundle with nearby work |

Triage against the real page, not the report: a contrast failure on a badge nobody sees ranks below a heading problem on the main path.

## Team practice

- Designers, developers and QA share the review so the fix lands in the artifact that caused it, rather than being handed down twice.
- Put the criteria in the ticket before work starts. "Submits with keyboard only, error text announced, 44px targets" is testable; "make it accessible" is not.
- Keep one running list of what the system already fails. Known-bad tokens get fixed once; unknown ones get rediscovered on every screen.

## In this repo

The app has a `pytest` suite and the doc site builds from `templates/pages`, but neither runs an accessibility linter. Running axe against the built `site/*.html` would cover the mechanical third in CI, and the contrast table in `references/accessible-components.md` already lists the known failures with their measured ratios — those are Severity 2 by the table above and currently ship.
