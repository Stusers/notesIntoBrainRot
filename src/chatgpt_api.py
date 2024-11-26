from openai import OpenAI



def get_meme_text_from_chatgpt(notes, openai_api_key, box_count):
    """
    Uses OpenAI's API to generate text for multiple text boxes in a meme.

    :param notes: Notes to process
    :param openai_api_key: OpenAI API key
    :param box_count: Number of text boxes in the meme
    :return: List of generated text for each box
    """
    client = OpenAI(api_key=openai_api_key)

    # Construct the prompt dynamically based on box_count
    prompt = f"""
    You are a funny meme generator. You are sarcastic to the point and dont stress about being funny. your a chill guy.
    Understand the context or topic you provide.
    Evavulate most common jokes said with the provided meme template.
    Add humorously relevant captions to the template.
    Based on the following notes, 
    generate text for {box_count} text boxes for a meme.
    Notes:
    {notes}
    Response format:
    Text 1: [text for box 1]
    Text 2: [text for box 2]
    ...
    """

    # Use the updated API for chat completions
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a creative meme text generator."},
            {"role": "user", "content": prompt},
        ]
    )

    # Extract and parse the response content
    response_text = response.choices[0].message.content
    texts = []
    for line in response_text.split("\n"):
        if line.startswith("Text"):
            _, text = line.split(": ", 1)
            texts.append(text.strip())

    return texts
