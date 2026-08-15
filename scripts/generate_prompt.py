def generate_prompt(
    output_type,
    style
):

    prompt = f"""
Create an idol {output_type}.

Style:
{style}

Requirements:

- Preserve idol identity
- High quality
- Professional design
- Fan merchandise aesthetic

"""

    return prompt


if __name__ == "__main__":

    print(
        generate_prompt(
            "photocard",
            "luxury kpop style"
        )
    )
