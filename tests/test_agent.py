from core.agent import select_workflow, build_prompt


def test_wallpaper():

    result = select_workflow(
        "Create a wallpaper"
    )

    assert result == "wallpaper"



def test_sticker():

    result = select_workflow(
        "Create a sticker"
    )

    assert result == "sticker"



def test_photocard():

    result = select_workflow(
        "Create a photocard"
    )

    assert result == "photocard"



def test_prompt():

    prompt = build_prompt(
        "photocard",
        "luxury style"
    )

    assert "photocard" in prompt
