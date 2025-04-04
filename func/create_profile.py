import os

from colorama import Fore

from core.encryption import encrypt_master_key, derive_encryption_key
from core.storage import save_to_file
from core.user_input import collect_user_info_profile
from func.clear_screen import clear_screen


def rename_existing_file(filename="vault_data.json"):
    """
    Renames any existing file incrementally.
    """
    if os.path.exists(filename):
        counter = 1
        while True:
            new_filename = f"vault_data_previous_{counter}.json"
            if not os.path.exists(new_filename):
                os.rename(filename, new_filename)
                print(Fore.YELLOW + f"⚠️ Existing file renamed to {new_filename}.")
                break
            counter += 1


def create_profile():
    """
    Create a new user profile and save it to a JSON file.
    """
    # clear_screen()

    # Collect user information
    name, email, master_key = collect_user_info_profile()

    # Derive encryption key from the master key
    encryption_key = derive_encryption_key(master_key)

    # Encrypt the master key
    encrypted_master_key = encrypt_master_key(master_key, encryption_key)

    profile = {
        "name": name,
        "email": email if email else "Not Provided",
        "master_key": encrypted_master_key,
        "passwords": {},  # Empty dictionary for passwords
    }

    # Rename any existing file before saving the new profile
    rename_existing_file("vault_data.json")

    # Save the new profile to vault_data.json
    save_to_file(profile, master_key)
    print(Fore.GREEN + "\n✅ Setup complete! Your information has been securely stored.")
    print(Fore.YELLOW + "⚠️ Keep your master key safe! You'll need it to unlock VaultCLI.\n")
