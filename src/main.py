import os
import requests
from file_handler import read_text_file
from chatgpt_api import get_meme_text_from_chatgpt
from imgflip_api import generate_meme
from config_handler import load_config

if __name__ == "__main__":
    # Load configuration
    config = load_config()

    # Read input notes
    input_file = "../input/input.txt"
    notes = read_text_file(input_file)


    meme_text = get_meme_text_from_chatgpt(notes, config["openai_api_key"])

    if "Top Text" in meme_text and "Bottom Text" in meme_text:
        print("ChatGPT generated:")
        print("Top Text:", meme_text["Top Text"])
        print("Bottom Text:", meme_text["Bottom Text"])


        meme_url = generate_meme(meme_text["Top Text"], meme_text["Bottom Text"], config)

        if meme_url:
            print("Meme URL:", meme_url)


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
