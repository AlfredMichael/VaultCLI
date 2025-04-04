from core.storage import save_to_file, load_from_file
from core.user_input import collect_user_info_save_password
from colorama import Fore
from func.clear_screen import clear_screen


def save_password():
    """
    Save a password as a key-value pair (platform-password) in the user's profile.
    """
    clear_screen()
    platform, password, securekey = collect_user_info_save_password()

    # Load existing profile data
    profile = load_from_file(securekey)

    # Update the passwords dictionary
    profile["passwords"][platform] = password
    save_to_file(profile, securekey)
    print(Fore.GREEN + f"✅ Password for {platform} saved successfully!")