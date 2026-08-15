"""Compatibility helpers for v1 users.

The project no longer calls a developer-owned image API. Use the prompt returned here
with the image-generation/editing tool available in the user's Codex or ChatGPT host.
"""

from scripts.generate_prompt import generate_prompt


def generate_image_prompt(prompt: str) -> str:
    """Return the prompt unchanged; no network or credential access occurs."""
    return prompt.strip()


def example_prompt() -> str:
    return generate_prompt("photocard", "luxury black and silver album editorial")
