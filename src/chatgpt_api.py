from openai import OpenAI


def get_meme_text_from_chatgpt(notes, openai_api_key):

    # Instantiate the OpenAI client
    client = OpenAI(api_key=openai_api_key)

    # Construct the prompt
    prompt = f"""
    Based on the following notes, generate a 'Top Text' and 'Bottom Text' for a meme.
    Notes:
    {notes}
    Response format:
    Top Text: [your top text]
    Bottom Text: [your bottom text]
    """

    # Send the request to OpenAI API
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a creative meme text generator."},
            {"role": "user", "content": prompt},
        ]
    )

    # Extract the response content
    response_text = response.choices[0].message.content

    # Parse the response to get top and bottom text
    result = {}
    for line in response_text.split("\n"):
        if ": " in line:
            key, value = line.split(": ", 1)
            result[key.strip()] = value.strip()
    return result
