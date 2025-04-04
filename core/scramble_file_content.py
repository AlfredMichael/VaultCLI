import random
from colorama import Fore
import random

from colorama import Fore


def scramble_file_content(file_path):
    """
    Scramble the content of the file by overwriting it with random data.
    """
    try:
        with open(file_path, "w") as file:
            scrambled_content = "".join(random.choices("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()", k=100))
            file.write(scrambled_content)
        print(Fore.YELLOW + "⚠️ File content scrambled successfully.")
    except Exception as e:
        print(Fore.RED + f"❌ Failed to scramble file content. Error: {str(e)}")