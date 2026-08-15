"""Local routing helpers. This module never calls an image API."""

from scripts.generate_prompt import generate_prompt


WORKFLOW_TERMS = {
    "wallpaper": ("wallpaper", "壁纸", "锁屏", "lock screen", "desktop background"),
    "sticker": ("sticker", "贴纸", "emoji", "表情包", "die-cut"),
    "photocard": ("photocard", "photo card", "小卡", "收藏卡", "collectible card"),
}


def select_workflow(request: str) -> str:
    normalized = request.casefold()
    for workflow, terms in WORKFLOW_TERMS.items():
        if any(term in normalized for term in terms):
            return workflow
    return "unknown"


def build_prompt(workflow: str, style: str, text: str = "", notes: str = "") -> str:
    if workflow not in WORKFLOW_TERMS:
        raise ValueError(f"Unsupported workflow: {workflow}")
    return generate_prompt(workflow, style, text, notes)


def run_agent(request: str, style: str, text: str = "", notes: str = "") -> str:
    """Return a prompt for the user's host image tool; perform no network request."""
    workflow = select_workflow(request)
    if workflow == "unknown":
        raise ValueError("Request must specify wallpaper, sticker, or photocard")
    return build_prompt(workflow, style, text, notes)
