#!/usr/bin/env python3
"""Build a portable image-edit prompt without calling any external API."""

from __future__ import annotations

import argparse
from pathlib import Path


ASSETS = {
    "wallpaper": {"composition": "portrait editorial composition with clear clock and widget safe zones", "output": "1290x2796 PNG"},
    "sticker": {"composition": "centered die-cut sticker, bold clean outline, transparent background", "output": "3000x3000 transparent PNG when supported"},
    "sticker-sheet": {"composition": "exact 16:25 portrait collectible sticker sheet with realistic people and 4-8 separately cut simplified objects, varied scale, natural spacing, and a full balanced layout", "output": "1600x2500 opaque PNG or JPG, or another exact 16:25 size"},
    "photocard": {"composition": "premium 2.5:3.5 collectible card layout with print-safe margins", "output": "750x1050 PNG minimum"},
}

CREATOR_MARK = "JESSICA • FAN MADE"


def generate_prompt(output_type: str, style: str, text: str = "", notes: str = "") -> str:
    """Return a complete prompt for a host-provided image editing tool."""
    asset = ASSETS[output_type]
    copy = text.strip() or "no text"
    extra = notes.strip() or "none"
    treatment = "" if output_type != "sticker-sheet" else """
Analyze the source scene first. Use only people and recognizable objects actually present.
Keep people photorealistic and identity-faithful. Simplify objects into clean editorial
illustrations with broad color blocks and reduced texture. Give every extracted element
an independent warm-white die-cut border and soft paper shadow. Arrange them on an opaque
matte-paper background whose hue and warmth are derived from the source photo. Do not use
transparency, a checkerboard, or a reconstructed full-scene background.
"""
    return f"""Edit the supplied reference image into an unofficial fan-made {output_type}.

Preserve the subject's recognizable identity: facial geometry, skin tone, hairstyle,
expression, pose cues, and distinctive accessories. Use the reference image as the
identity source; do not replace the person.
{treatment}

Art direction: {style.strip()}
Composition: {asset['composition']}
Exact text: {copy}
Additional requirements: {extra}
Output target: {asset['output']}
Creator attribution: reserve a quiet bottom safe-zone position for the exact mark
"{CREATOR_MARK}". Prefer compositing assets/jessica-fan-made-mark.svg after generation
when a local graphics tool is available so the lettering remains exact.

Quality constraints: polished lighting, coherent anatomy, crisp edges, balanced spacing.
Avoid face reshaping, extra people, extra fingers or limbs, illegible text, brand logos,
third-party watermarks, fake signatures, and anything that implies official endorsement.
""".strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build an Idol Creative Studio prompt (no API call or API key required).")
    parser.add_argument("--type", choices=sorted(ASSETS), required=True)
    parser.add_argument("--style", required=True)
    parser.add_argument("--text", default="")
    parser.add_argument("--notes", default="")
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    prompt = generate_prompt(args.type, args.style, args.text, args.notes)
    if args.output:
        args.output.write_text(prompt + "\n", encoding="utf-8")
        print(f"Saved prompt: {args.output}")
    else:
        print(prompt)


if __name__ == "__main__":
    main()
