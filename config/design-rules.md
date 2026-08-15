# Design and QA rules

## Identity

- Preserve facial geometry, skin tone, hairstyle, expression, pose cues, and distinctive accessories.
- Do not beautify by changing ethnicity, face shape, age, or body proportions.
- Prefer one strong edit over a collage when only one reference image is supplied.

## Composition

- Maintain one clear focal point and balanced negative space.
- Protect crop, clock, widget, trim, and cut-line safe zones for the chosen asset.
- Match the palette to the source outfit and lighting unless the user explicitly requests a contrast.

## Text

- Use exact user-provided spelling. Keep generated text short.
- Never invent signatures, endorsements, agency logos, or official marks.
- Add the creator mark from `assets/jessica-fan-made-mark.svg` when confusion with official merchandise is plausible. If the asset cannot be composited, use the exact fallback text `JESSICA • FAN MADE`.

## Creator mark

- Preserve the sparkle-and-capsule construction, proportions, and exact wording of the supplied SVG.
- Place it in a lower corner or bottom safe zone with clear breathing room; never cover a face, hand, garment detail, or cut line.
- Keep its width near 8–14% of the canvas on wallpapers and sticker sheets, or 14–20% on photocards. Keep opacity between 65–85% when compositing over artwork.
- Use a light mark on dark areas and a charcoal mark on light areas. Do not add agency names, trademarks, signatures, or language implying official endorsement.

## Final inspection

Reject or retry outputs with identity drift, extra people, malformed anatomy, unreadable text, missing or misspelled creator attribution, unintended watermark, broken transparency, or incorrect aspect ratio.
