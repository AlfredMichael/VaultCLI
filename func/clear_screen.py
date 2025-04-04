import os

def clear_screen():
    """
    Clears the console screen.
    """
    os.system("cls" if os.name == "nt" else "clear")
