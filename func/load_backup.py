import json
import shutil
import os
from core.storage import save_to_file, load_from_file
from core.user_input import collect_user_info_save_password, collect_backup_file
from colorama import Fore
from func.clear_screen import clear_screen


def validate_key(key, file_path):
    """
    Validate the key by attempting to load and decrypt the file.
    """
    try:
        # Attempt to load the file with the provided key
        profile = load_from_file(key, file_path)
        if profile:
            return True, None
        else:
            return False, "Failed to decrypt the file with the provided key. Please check your key."
    except Exception as e:
        return False, f"An error occurred while validating the key: {str(e)}"


def load_backup():
    """
    Load data from a user-specified backup file into the main profile file.
    """
    clear_screen()
    file_path, key = collect_backup_file()

    # Validate the key
    is_valid, error_message = validate_key(key, file_path)
    if not is_valid:
        print(Fore.RED + f"❌ {error_message}")
        return

    # Check if the backup file exists
    if os.path.exists(file_path):
        try:
            # Copy the backup file data directly to the main profile file
            destination_file = "vault_data.json"
            shutil.copyfile(file_path, destination_file)
            print(Fore.GREEN + "✅ Backup data has been successfully loaded into your main profile!")
        except Exception as e:
            print(Fore.RED + f"❌ Failed to load the backup file. Error: {str(e)}")
    else:
        print(Fore.RED + f"❌ No file found at the specified path: {file_path}. Please check the path and try again.")
