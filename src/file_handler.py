import os

def read_text_file(file_path="../input/input.txt"):
    """
    Reads the content of a text file and returns it as a string.
    :param file_path: Relative path to the text file
    :return: Content of the file as a string
    """
    try:
        # Resolve the absolute path to the input file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, file_path)

        with open(full_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        exit(1)
    except Exception as e:
        print(f"Error reading the file: {e}")
        exit(1)
