from openai import OpenAI


client = OpenAI()


def generate_image(prompt):

    response = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )

    image_url = response.data[0].url

    return image_url


if __name__ == "__main__":

    prompt = """
    Create a luxury K-pop idol photocard design.
    Black and silver theme.
    Premium album style.
    """

    result = generate_image(prompt)

    print(result)
