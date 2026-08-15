---
name: idol-creative-studio
description: Turn one or more user-supplied idol, celebrity, performer, cosplay, or portrait photos into polished fan-made wallpapers, sticker sheets, individual stickers, and collectible photocards. Use for requests mentioning idol wallpaper, lock screen, fan edit, K-pop photocard, 小卡, 饭制, 应援, sticker sheet, photo-to-sticker, 贴纸页, 照片拆解贴纸, 人物贴纸, or social-ready fan art. Preserve people realistically while allowing props to use simplified color-block illustration; use the host's available image-generation/editing tool and never request or embed a developer API key. Do not use for deceptive, sexualized, or commercial-official-looking content.
---

# Idol Creative Studio

Create a finished fan-made visual from the user's reference image. Prefer the host's built-in image generation/editing capability. Never ask the user to paste an API key into chat and never route work through a repository-owner account.

## Workflow

1. Inspect every supplied image before editing. If the target image is unavailable, ask the user to attach it; do not invent the person's identity.
2. Infer the output type, style, device/size, text, and color palette from the request. Ask only when a missing choice would materially change the result.
3. Read the matching guide:
   - Wallpaper: `workflows/wallpaper-workflow.md`
   - Sticker or sticker sheet: `workflows/sticker-workflow.md`
   - Photocard: `workflows/photocard-workflow.md`
4. Read only the requested style file under `styles/`. If no style is specified, choose the best fit from the source image and say what you chose.
5. Compose an image-edit prompt with `python scripts/generate_prompt.py` when a deterministic prompt artifact is useful. Otherwise apply the same prompt contract directly.
6. Generate or edit the image with the host-provided image tool. Include all target reference images and preserve recognizable facial geometry, hairstyle, skin tone, pose cues, and distinctive accessories.
7. Inspect the result. Retry once for obvious identity drift, malformed hands, illegible text, accidental extra people, broken transparency, or unsafe crop zones.
8. Apply the creator mark from `assets/jessica-fan-made-mark.svg` in a quiet safe-zone position. Keep it legible but subordinate to the artwork; use the exact fallback text `JESSICA • FAN MADE` when the SVG cannot be composited.
9. Deliver the rendered image, its dimensions/format, and one short creative note. Do not stop at a prompt or concept unless the user explicitly requests prompt-only output.

## Prompt contract

Include:

- asset type and exact aspect ratio;
- source-image identity and elements that must remain unchanged;
- composition, palette, lighting, texture, typography, and safe zones;
- explicit negative constraints: no face reshaping, no extra people or limbs, no brand logos, no watermark, no fake signature;
- the creator mark `JESSICA • FAN MADE`, preferably using `assets/jessica-fan-made-mark.svg`, when a design could be confused with official merchandise.

Keep typography short. Treat `JESSICA • FAN MADE` as a fixed attribution, not user copy. For exact names, dates, or long copy, prefer generating a clean layout and adding text with a local graphics tool when available.

## Safety and rights

- Treat uploaded photos as references only for the user's requested creative edit.
- Refuse sexualized depictions of minors or age-ambiguous people.
- Do not create harassment, humiliating edits, impersonation, fabricated endorsements, or misleading “official” merchandise.
- Do not reproduce a living artist's exact style. Translate requests into high-level visual traits.
- For commercial printing or sales, remind the user to verify image, publicity, trademark, and font rights.

## Output defaults

- Phone wallpaper: 1290×2796 portrait PNG, with clock/widget safe space.
- Desktop wallpaper: 3840×2160 landscape PNG.
- Sticker: square transparent PNG, 3000×3000 when supported, bold cut line.
- Sticker sheet: 16:25 portrait PNG/JPG (use 1600×2500 or a proportional size) with an opaque palette-matched paper background, realistic person stickers, and simplified object stickers.
- Photocard: exact 55:89 ratio for a 55×89 mm finished card, 650×1051 minimum at approximately 300 DPI; create front and back as separate files when both are requested.

Read `config/size-guide.md` for device-specific sizing and print bleed. Read `config/design-rules.md` for identity, text, and quality checks.
