from PIL import Image, ImageFilter


def create_sticker(input_path, output_path):

    img = Image.open(input_path)

    img = img.convert("RGBA")

    outline = img.filter(
        ImageFilter.FIND_EDGES
    )

    img.save(output_path)

    print(
        "Sticker template created"
    )


if __name__ == "__main__":

    create_sticker(
        "input.png",
        "sticker.png"
    )
