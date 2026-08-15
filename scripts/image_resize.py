from PIL import Image
import argparse


def resize_image(input_path, output_path, width, height):

    img = Image.open(input_path)

    resized = img.resize(
        (width, height),
        Image.LANCZOS
    )

    resized.save(output_path)

    print(
        f"Saved resized image: {output_path}"
    )


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Resize idol images for creative outputs"
    )

    parser.add_argument(
        "--input",
        required=True
    )

    parser.add_argument(
        "--output",
        required=True
    )

    parser.add_argument(
        "--width",
        type=int,
        required=True
    )

    parser.add_argument(
        "--height",
        type=int,
        required=True
    )

    args = parser.parse_args()


    resize_image(
        args.input,
        args.output,
        args.width,
        args.height
    )
