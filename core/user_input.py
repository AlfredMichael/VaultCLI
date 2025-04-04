from pathlib import Path
import os
import re
from colorama import init, Fore, Style


# -------------------------- VALIDATION STARTS ------------------------------------------


def validate_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email)


def validate_name(name):
    """Validate that the name is at least 3 characters and contains only alphabets."""
    if len(name) < 3:
        return False, "Name must be at least 3 characters long."
    if not name.isalpha():
        return False, "Name must contain only alphabets."
    return True, None


def validate_master_key(master_key):
    """Validate that the master key is at least 6 characters long."""
    if len(master_key) < 6:
        return False, "Your selected master key isn't secure enough. It must be at least 6 characters long."
    return True, None


def validate_platform(platform):
    """Validate that the platform name is at least 3 characters long."""
    if len(platform) < 3:
        return False, "Platform name must be at least 3 characters long."
    return True, None


def validate_password(password):
    """Validate that the password is at least 3 characters long."""
    if len(password) < 3:
        return False, "Password must be at least 3 characters long."
    return True, None


def validate_file_path(file_path):
    """Validate that the file path is in a valid format and exists."""
    try:
        # Check if the file path is valid
        path = Path(file_path)
        if not path.is_file():  # Check if the path points to a valid file
            return False, "The file path is invalid or the file does not exist."
        return True, None
    except Exception:
        return False, "The file path format is invalid."


# -------------------------- VALIDATION ENDS ------------------------------------------


def collect_user_info_profile():
    """Collect user profile details in a clean way."""
    print(Fore.CYAN + "🚀 Creating a New Profile")

    # Validate name
    while True:
        name = input(Fore.YELLOW + "Enter your name: ").strip()
        is_valid, error_message = validate_name(name)
        if is_valid:
            break
        else:
            print(Fore.RED + f"❌ {error_message}")

    # Validate email
    email = input(Fore.YELLOW + "Enter your email (optional): ").strip()
    while email and not validate_email(email):
        print(Fore.RED + "❌ Invalid email address. Please try again.")
        email = input(Fore.YELLOW + "Enter your email (optional): ").strip()
    if not email:
        print("You skipped entering your email.")

    # Validate master key
    while True:
        master_key = input(Fore.YELLOW + "Set up a master key (keep it safe!): ").strip()
        is_valid, error_message = validate_master_key(master_key)
        if is_valid:
            break
        else:
            print(Fore.RED + f"❌ {error_message}")

    return name, email, master_key


def collect_user_info_save_password():
    """Collect user details in a clean way."""
    while True:
        key = input(Fore.YELLOW + f"🔑 Please enter your secure key: ").strip()
        if key:
            break
        else:
            print(Fore.RED + "❌ Secure key cannot be empty. Please enter your key.")

    print(Fore.CYAN + "🔒 Save a Password")

    # Validate platform
    while True:
        platform = input(Fore.YELLOW + "Platform (e.g., Gmail, Facebook): ").strip()
        is_valid, error_message = validate_platform(platform)
        if is_valid:
            break
        else:
            print(Fore.RED + f"❌ {error_message}")

    # Validate password
    while True:
        password = input(Fore.YELLOW + f"Password for {platform}: ").strip()
        is_valid, error_message = validate_password(password)
        if is_valid:
            break
        else:
            print(Fore.RED + f"❌ {error_message}")

    return platform, password, key


def collect_backup_file():
    """Collect backup file path in a clean way."""
    print(Fore.CYAN + "♻️ Load Backup Data")

    # Validate key
    while True:
        key = input(Fore.YELLOW + f"🔑 Please enter your key: ").strip()
        if key:
            break
        else:
            print(Fore.RED + "❌ Secure key cannot be empty. Please enter your key.")

    # Validate file path
    while True:
        file_path = input(Fore.YELLOW + "Enter the full path to the backup file (e.g., /path/to/backup.json): ").strip()
        is_valid, error_message = validate_file_path(file_path)
        if is_valid:
            break
        else:
            print(Fore.RED + f"❌ {error_message}")

    return file_path, key

def collect_platform():
    """Collect platform and secure key in a clean and validated way."""
    print(Fore.CYAN + "🔑 Please enter your key: ")

    # Validate secure key
    while True:
        securekey = input(Fore.YELLOW + "Enter your secure key: ").strip()
        if securekey:
            break
        else:
            print(Fore.RED + "❌ Secure key cannot be empty. Please enter your key.")

    print(Fore.CYAN + "🔑 Retrieve a Password")

    # Validate platform
    while True:
        platform = input(Fore.YELLOW + "Platform to retrieve password for: ").strip()
        if platform:
            break
        else:
            print(Fore.RED + "❌ Platform cannot be empty. Please enter the platform name.")

    return platform, securekey

