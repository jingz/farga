# Mobile & Alternative Input Handling

Covered by WCAG 2.2 SC 2.5.5 (target size, AAA) and SC 2.5.8 (target size minimum, AA), among others.

## Touch targets and cards

- **Minimum target bounds**: interactive controls get at least 44×44 CSS px of touch area (WCAG 2.5.5, AAA). 24×24 CSS px is the AA floor (SC 2.5.8) — and an undersized target only passes AA if a 24px-diameter circle centred on it intersects no other target's circle. Space is the substitute for size, not a fixed number: a 16px control therefore needs 4px of clear space on every side (24 − 16 = 8, split across both edges), while a 20px control needs 2px.
- **Keep controls apart**: crowding is its own failure. Adjacent destructive and primary actions, and anything a tremor can send you past, need visibly more than the minimum gap — accidental activation is the complaint that follows.
- **Pad, do not grow**: where a visually small control is required, add padding or a pseudo-element hit area rather than enlarging the visible box.
- **Card patterns**: group related elements into structured container cards with clear interactive boundaries, so a tap has one obvious target.

## Voice and alternative inputs

- **Voice control identifiers**: controls need distinct visible labels that match their accessible names, so users of iOS Voice Control or Android Voice Access can say "Tap [Label]" or "Show names" without ambiguity.
- **Name and state are separate**: iOS distinguishes `accessibilityLabel` (what the control does) from `accessibilityValue` (its current state), and Voice Control matches on the label. The same split applies on the web: the accessible name describes the action, the value or `aria-checked` describes the state. Android matches more loosely and predictively, which is a reason to keep labels unique rather than a reason to be vague.
- **Confirm the action**: a voice or switch activation needs visible feedback, plus haptics on mobile where available, or the user cannot tell whether the command landed.
- **Single-point operation**: provide a single-click or single-tap alternative for anything that depends on dragging, swiping, pinching, or multi-point gestures.
- **Focus order**: keep keyboard and switch traversal logical (Tab order follows reading order) and keep a visible, high-contrast focus ring on every active element. Never remove an outline without replacing it.

## Grouping and focus order

- **One stop per compound control**: a card that has one action should be one stop, not a container plus a link plus an icon. Compound elements are announced as a unit — the platform equivalent is grouping views together into a single accessible container.
- **Do not let a container swallow its children**: if a card is itself tappable and also holds inner actions (save, delete), the inner controls must stay reachable. A container that captures every tap is the mobile version of a keyboard trap.
- **Floating action buttons go last**: a FAB placed early in the DOM interrupts the reading order for screen reader and switch users. Put it at the end of the flow and let CSS position it visually.
