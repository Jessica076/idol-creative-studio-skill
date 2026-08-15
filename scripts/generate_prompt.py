#!/usr/bin/env python3
"""Build a portable image-edit prompt without calling any external API."""

from __future__ import annotations

import argparse
from pathlib import Path


ASSETS = {
    "wallpaper": {"composition": "portrait editorial composition with clear clock and widget safe zones", "output": "1290x2796 PNG"},
    "sticker": {"composition": "centered die-cut sticker, bold clean outline, transparent background", "output": "3000x3000 transparent PNG when supported"},
    "photocard": {"composition": "premium 2.5:3.5 collectible card layout with print-safe margins", "output": "750x1050 PNG minimum"},
}


def generate_prompt(output_type: str, style: str, text: str = "", notes: str = "") -> str:
    """Return a complete prompt for a host-provided image editing tool."""
    asset = ASSETS[output_type]
    copy = text.strip() or "no text"
    extra = notes.strip() or "none"
    return f"""Edit the supplied reference image into an unofficial fan-made {output_type}.

Preserve the subject's recognizable identity: facial geometry, skin tone, hairstyle,
expression, pose cues, and distinctive accessories. Use the reference image as the
identity source; do not replace the person.

Art direction: {style.strip()}
Composition: {asset['composition']}
Exact text: {copy}
Additional requirements: {extra}
Output target: {asset['output']}

Quality constraints: polished lighting, coherent anatomy, crisp edges, balanced spacing.
Avoid face reshaping, extra people, extra fingers or limbs, illegible text, brand logos,
watermarks, fake signatures, and anything that implies official endorsement.
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
