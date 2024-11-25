import json
import os

def load_config(file_path="../config.json"):
    """
    Loads the configuration file and returns a dictionary of settings.
    :param file_path: Relative path to the config file
    :return: Dictionary of configuration data
    """
    try:

        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, file_path)

        with open(full_path, "r") as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {file_path}.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Configuration file at {file_path} is not properly formatted.")
        exit(1)
