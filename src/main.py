import os
import random
import requests
from file_handler import read_text_file
from chatgpt_api import get_meme_text_from_chatgpt
from imgflip_api import generate_meme
from config_handler import load_config

def fetch_meme_templates():

   
    url = "https://api.imgflip.com/get_memes"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data["success"]:
                return data["data"]["memes"]
            else:
                print("Error fetching meme templates:", data.get("error_message", "Unknown error"))
        else:
            print("Failed to connect to Imgflip API. Status code:", response.status_code)
    except Exception as e:
        print(f"An error occurred: {e}")
    return []

if __name__ == "__main__":
    # Load configuration
    config = load_config()

    # Fetch all meme templates
    meme_templates = fetch_meme_templates()
    if not meme_templates:
        print("No meme templates available. Exiting.")
        exit(1)

    # Randomly select a meme template
    selected_template = random.choice(meme_templates)
    template_id = selected_template["id"]
    template_name = selected_template["name"]
    box_count = selected_template.get("box_count", 2)  # Default to 2 if not specified

    print(f"Selected Meme Template: {template_name} (ID: {template_id}, Boxes: {box_count})")

    # Read input notes and include template description
    input_file = "../input/input.txt"
    notes = read_text_file(input_file)
    notes_with_template = f"{notes}\n\nMeme Template: {template_name} (with {box_count} text boxes)"

    # Get meme text from ChatGPT, requesting text for each box
    meme_text = get_meme_text_from_chatgpt(notes_with_template, config["openai_api_key"], box_count)

    if meme_text:
        print("ChatGPT generated:")
        for i, text in enumerate(meme_text, 1):
            print(f"Text {i}: {text}")

        # Generate meme using Imgflip API with the selected template
        meme_url = generate_meme(meme_text, {
            "imgflip_username": config["imgflip_username"],
            "imgflip_password": config["imgflip_password"],
            "meme_template_id": template_id,
        })

        if meme_url:
            print("Meme URL:", meme_url)

            # Save meme to the output folder
            output_file = "../output/meme.jpg"
            try:
                response = requests.get(meme_url)
                if response.status_code == 200:
                    # Ensure the output directory exists
                    os.makedirs(os.path.dirname(output_file), exist_ok=True)
                    with open(output_file, "wb") as f:
                        f.write(response.content)
                    print(f"Meme saved to {output_file}")
            except Exception as e:
                print(f"Error saving meme: {e}")
