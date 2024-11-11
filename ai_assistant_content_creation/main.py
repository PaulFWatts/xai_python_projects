from openai import OpenAI


def create_style_assistant(writing_example):
    XAI_API_KEY = "YOUR_XAI_API_KEY_GOES_HERE"
    client = OpenAI(
        api_key=XAI_API_KEY,
        base_url="https://api.x.ai/v1",
    )
    system_message = f"""Analyze this writing example and mimic its style, tone, and voice in your responses: {writing_example} Maintain this same writing style in all your responses."""

    return client, system_message


def generate_response(client, system_message, prompt):
    completion = client.chat.completions.create(
        model="grok-beta",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ],
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    my_writing_style = """YOUR WRITING EXAMPLES GO HERE"""

    # Create the assistant
    client, system_message = create_style_assistant(my_writing_style)

    # Generate a response
    prompt = """Write a post about this news:......"""
    response = generate_response(client, system_message, prompt)
    print(response)
