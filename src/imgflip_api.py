import requests

def generate_meme(top_text, bottom_text, config):
    """
    Generates a meme using the Imgflip API.

    """
    url = "https://api.imgflip.com/caption_image"
    payload = {
        "template_id": config["meme_template_id"],
        "username": config["imgflip_username"],
        "password": config["imgflip_password"],
        "text0": top_text,
        "text1": bottom_text,
    }

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
