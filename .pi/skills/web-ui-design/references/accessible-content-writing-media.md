# Accessible Content: Writing and Multimedia

## Writing that survives being read aloud

- **Front-load**: subject and point in the first few words of a sentence and of a heading. Both skimming and screen-reader users consume the beginning first.
- **Chunk**: 4–5 sentences is the ceiling for a paragraph. A wall of text is a navigation problem, not just a style preference.
- **Plain words**: cut jargon and filler. Say what happens ("Your card was declined"), not a description of a state ("Payment processing exception").
- **Links say where they go**: "read the pricing page", never "click here" or a bare URL (SC 2.4.4). Also check out of context — a screen reader lists links with no surrounding sentence.
- **Headings are structure, not emphasis**: use `h1`–`h6` in order and never a heading because it looks the right size. Users navigate by heading list, so a skipped level or a decorative heading pollutes the outline. Bold text is for emphasis.

## Images

Alt text, decorative versus functional images, text baked into bitmaps, and cropping uploads: `references/working-with-images.md`. Do not restate those rules here.

## Multimedia

- **Captions**: synchronized and accurate, including meaningful non-speech audio — laughter, a door, a name called off-screen (SC 1.2.2).
- **Transcript**: required for audio-only content; note who is speaking and any relevant visual action.
- **Audio description**: narrate what a sighted user sees — scene changes, gestures, on-screen text — when it is not already in the dialogue.
- In this project, generated pronunciation audio always sits beside the visible word or sentence, so its text alternative already exists. Keep that pairing: never put audio on a page without the words it speaks.

## Social and shareable text

- **Hashtags**: capitalise each word (`#AccessibleDesign`) so screen readers and text-to-speech parse words instead of one mangled token.
- **Emoji**: each has a spoken name, so a row of them becomes a paragraph of noise. Use one, at the end.
- Alt text on social images follows the same rules as anywhere else — for a screen reader user it is the only text they get, and some platforms truncate it hard.
