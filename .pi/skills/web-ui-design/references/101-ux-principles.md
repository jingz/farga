# 101 UX Principles (Will Grant)

Will Grant's *101 UX Principles* (2018) is a list of conventions: cheap checks that catch
predictable mistakes. This file indexes the ones that affect interface work, with the
principle number so it can be looked up, and names the rule or file that implements it.

Nothing here overrides `references/accessible-components.md`: where the two disagree,
accessibility wins. Three principles need reconciling with guidance elsewhere in this
skill and are marked ⚖.

## Conventions beat invention

- **#2 Be strategic about these principles.** They are defaults, not laws. Knowing why a
  convention exists is what makes breaking it deliberate.
- **#16 Don't invent new, arbitrary controls.** A control the user has never met costs them
  learning time; `accessible-design-systems.md` says the same about custom dropdowns.
- **#98 Jakob's Law.** Users spend nearly all their time in other products, so yours is the
  one they know least. Match the platform's mechanics, and differentiate in the content.
- **#99 Decide whether an interaction is obvious, easy or possible.** Obvious: on screen.
  Easy: one click away. Possible: inside a settings panel. Not everything can be obvious, and
  treating it that way is what makes an interface noisy.
- **#3 / #4 Simple first, complexity on request.** Ship the focused version, then add depth
  for the users whose workflow actually demands it.

## Controls

- **#13 Make interactive elements obvious.** If it can be clicked, it should look clickable.
- **#14 Size buttons sensibly, group them by function.** The size tiers are in
  `visual-hierarchy.md`; the row is `.actions`.
- **#15 The whole button is the target, with a pointer cursor.** Make the label and its
  padding both clickable, and give clear pressed feedback.
- **#17 Search is a text field with a button labelled "Search".** Never an icon that expands
  into one, and never two steps.
- **#18 Sliders are for non-quantifiable values** — volume, brightness. Numbers get a number field.
- **#19 Numeric entry fields for precise integers.** Let the browser validate them.
- **#20 ⚖ A few fixed options is not a dropdown.** Two or three choices worth showing at once
  belong as radios or a segmented control; a list that is long, unknown, or expected to grow is
  a native `<select>`. `accessible-design-systems.md` prefers the native control, and this is
  where the two meet: choose by how many options there will *ever* be, not how many there are
  today.
- **#54 Pick the right control, and let the platform supply it.** `type="email"`, `"tel"`,
  `"url"`, `"number"`, `"search"`, `type="date"`, `inputmode`: `check.py` already fails the
  build on a text field whose name says email, password, phone or url.

## Destructive actions

- **#21 ⚖ Prefer undo to a confirmation roadblock.** Reconciled with this skill's "destructive
  actions stay low-emphasis until an explicit confirmation step": a *reversible* action gets an
  undo and a grace period, no dialog at all; an *irreversible* one gets a confirmation that
  names what will happen. A client-side form reset is neither, which is why the form docs keep
  Reset out of the actions row entirely.

## Navigation and content structure

- **#23 Infinite scroll is for feeds only** — open-ended streams of similar items.
- **#24 Bounded content paginates.** If it has a beginning, a middle and an end, or position
  matters, give it pages. `nav.pagination` exists for that.
- **#26 Empty states teach the next step.** Illustration, plain explanation, one action —
  `empty_state.scss`, never a bare table.
- **#29 Don't bury primary navigation in a hamburger.** Desktop navigation stays visible.
- **#31 Split long menus into sections, and pair icons with text.** A bare icon is a guess at
  someone else's vocabulary.
- **#95 The best match goes first** on a results page, with usable sorting and filtering.
- **#97 ⚖ Modals are for blocking decisions only.** Not for filtering, not for notifications.
  Farga's drawer is a non-modal popover for exactly this reason.

## Mobile is the baseline

- **#22 / #100 Mobile is not a feature.** About two thirds of global web traffic is mobile
  (StatCounter, 2025), so "does it work on mobile" is answered by the layout, not by a plan.
- **#73 Finger-sized targets.** The numbers, and the spacing test that substitutes for size on
  a small control, are in `references/mobile-touch-inputs.md`.

## Words, data and trust

- **#66 Labels, not placeholder text.** A placeholder disappears as soon as typing starts and
  is not a reliable name — the build fails on a control with no label.
- **#90 "Sign in" and "Sign out", not "Log in".** Plain words over system words.
- **#91 Joining and returning are different flows.** "Create account" and "Sign in" are not one
  form with two buttons; make them separate entry points.
- **#96 Pick good defaults.** A sensible default saves every user the same decision — and it
  must still be what most users want, or it is a trap.
- **#101 Don't join the dark side.** Manipulative friction, fake urgency, opt-out ladders and
  hidden costs are defects, not trade-offs.

## Universal Design's seven principles

Accessibility's broader sibling, and its older relative: the Center for Universal Design at
NC State published these in 1997 (Connell, Jones, Mace, Mueller, Mullick, Ostroff, Sanford,
Steinfeld, Story and Vanderheiden). WCAG is the testable subset of this list; the rest is
design intent worth checking a screen against:

1. Equitable use
2. Flexibility in use
3. Simple and intuitive use
4. Perceptible information
5. Tolerance for error
6. Low physical effort
7. Size and space for approach and use

## In Farga today

Already satisfied: whole-box targets with a pointer cursor (#15, partly), native input types
(#54, enforced by `check.py`), an empty-state component (#26), pagination for bounded lists
(#24), a non-modal drawer instead of a modal filter panel (#97), range limited to brightness
(#18), sensible switch defaults (#96), "Sign in" wording in the composed examples (#90).

Gaps worth knowing: **no `:active` pressed state exists anywhere in the SCSS** — 12 rules set
`cursor: pointer`, none provide the feedback #15 also asks for. There is **no toast or
snackbar component**, so undo (#21) can only be expressed as a confirmation dialog today. And
the doc sidebar, once the layout stacks at 320px, puts a full viewport of navigation in front
of the content (measured at 1.03 viewport heights), which is #29's warning applied to our own
shell.
