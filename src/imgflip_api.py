import requests


def generate_meme(box_texts, config):
    """
    Generates a meme using the Imgflip API with dynamic text boxes.
    :param box_texts: List of text for each box
    :param config: Configuration dictionary with API credentials and dynamic template ID
    :return: URL of the generated meme
    """
    url = "https://api.imgflip.com/caption_image"
    payload = {
        "template_id": config["meme_template_id"],
        "username": config["imgflip_username"],
        "password": config["imgflip_password"],
    }

    # Add text for each box dynamically
    for i, text in enumerate(box_texts):
        payload[f"text{i}"] = text

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        data = response.json()
        if data["success"]:
            return data["data"]["url"]
        else:
            print("Imgflip API error:", data["error_message"])
    else:
        print("Failed to connect to Imgflip API.")
    return None
