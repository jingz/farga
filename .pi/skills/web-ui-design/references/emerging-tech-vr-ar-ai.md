# Emerging Tech: VR, AR and AI

Only the third section applies to a normal web application. The first two matter if the product ships an immersive or camera-based experience.

## VR

- **Locomotion**: offer teleportation alongside smooth movement. Continuous motion without a matching physical sensation causes vestibular mismatch and nausea, and it is the accommodation users ask for first.
- **Comfort**: stable high frame rate; let users restrict camera motion or narrow the field of view; provide a one-touch re-orientation.
- **Sight**: scalable HUD, high-contrast mode, a visible reticle, audio description of the space.
- **Hearing**: mono output option, left/right balance, captions that work spatially rather than as a flat overlay.

## AR

- Environments vary by user and by minute, so provide brightness adjustment, a high-contrast backing behind text, and resizable text.
- Let users toggle information layers off. Overlay clutter is a cognitive-load problem before it is an aesthetic one.
- Support eye, head and voice input: holding a device up for long sessions is fatigue, and some users cannot do it at all.

## AI

- **Training data has to include disabled, neurodivergent and non-standard speech.** Recognition that only handles broadcast-standard speech excludes exactly the people voice input was meant to serve.
- **Do not correct people into someone else's words.** Aggressive autocorrect distorts dyslexic and neurodivergent input and destroys intent. Make suggestions refusable and never silently rewrite what someone typed.
- **Generated output needs human review.** Machine alt text, automatic captions and accessibility overlays produce confident false positives and miss context. Treat generated descriptions as drafts, and never let an overlay stand in for accessible code.
- **Applies to this project**: the app generates vocabulary copy and pronunciation audio with a language model (`application/services/llm.py`). Review generated text before it is presented as authoritative, keep the visible text alternative beside generated audio, and let any voice input path tolerate non-standard speech.
