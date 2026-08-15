from api.image_generator import generate_image


def select_workflow(request):

    request = request.lower()

    if "wallpaper" in request or "壁纸" in request:
        return "wallpaper"

    if "sticker" in request or "贴纸" in request:
        return "sticker"

    if "photocard" in request or "小卡" in request:
        return "photocard"

    return "unknown"



def build_prompt(workflow, style):

    prompts = {

        "wallpaper":
        """
        Create a premium idol wallpaper.
        High resolution.
        Professional composition.
        """,

        "sticker":
        """
        Create a collectible idol sticker.
        Transparent background.
        Clean outline.
        """,

        "photocard":
        """
        Create a luxury idol photocard.
        Album style design.
        """
    }


    return prompts.get(workflow, "") + f"""
    
Style:
{style}

Requirements:
- Preserve idol identity
- High quality
- Professional fan merchandise design

"""



def run_agent(request, style):

    workflow = select_workflow(request)

    prompt = build_prompt(
        workflow,
        style
    )

    result = generate_image(prompt)

    return result



if __name__ == "__main__":

    output = run_agent(
        "Create a photocard",
        "K-pop luxury black silver style"
    )

    print(output)
