import shutil
from colorama import Fore
from core.storage import load_from_file
from func.clear_screen import clear_screen


def backup_data():
    """
    Create a backup of the current profile data immediately.
    """
    clear_screen()
    print(Fore.CYAN + "📦 Backing Up Data")

    source_file = "vault_data.json"
    backup_file = "vault_data_backup.json"

    try:
        # Copy the file directly without decoding
        shutil.copyfile(source_file, backup_file)
        print(Fore.GREEN + f"✅ Data backed up successfully to {backup_file}!")
    except FileNotFoundError:
        print(Fore.RED + f"❌ Source file not found: {source_file}")
    except Exception as e:
        print(Fore.RED + f"❌ An error occurred while backing up data: {str(e)}")
