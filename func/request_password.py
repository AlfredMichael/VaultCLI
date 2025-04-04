import os
import os
import time
import signal
from colorama import Fore
from core.monitor_file_access import monitor_file_access
from core.scramble_file_content import scramble_file_content
from core.storage import load_from_file
from core.user_input import collect_platform
from func.clear_screen import clear_screen

# Global variable to track the temporary file path
temp_file_path = None


def signal_handler(sig, frame):
    """Handle termination signals (e.g., Ctrl+C) to delete or scramble the temporary file."""
    global temp_file_path
    if temp_file_path and os.path.exists(temp_file_path):
        try:
            os.remove(temp_file_path)
            print(Fore.GREEN + f"\n✅ Temporary file deleted: {temp_file_path}")
        except Exception:
            print(Fore.RED + "\n❌ Unable to delete the file. Scrambling content instead.")
            scramble_file_content(temp_file_path)
    print(Fore.YELLOW + "\n🔒 Program terminated safely.")
    exit(0)


# Register signal handlers for interruptions and terminations
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


def request_password():
    """
    Retrieve a password for a specific platform from the user's profile and handle temporary storage.
    """
    global temp_file_path

    platform, securekey = collect_platform()

    profile = load_from_file(securekey, "vault_data.json")
    if platform in profile["passwords"]:
        password = profile["passwords"][platform]

        # Generate a temporary file to store the password
        temp_file_path = os.path.join(os.path.expanduser("~/Desktop"), f"{platform}_password.txt")
        try:
            with open(temp_file_path, "w") as temp_file:
                temp_file.write(f"Password for {platform}: {password}")
            print(Fore.GREEN + f"✅ Temporary file created: {temp_file_path}")

            # Monitor file access
            monitor_file_access(temp_file_path)

            # Wait for 60 seconds and attempt to delete the file
            time.sleep(60)
            if os.path.exists(temp_file_path):
                try:
                    os.remove(temp_file_path)
                    print(Fore.GREEN + f"✅ Temporary file deleted: {temp_file_path}")
                except Exception:
                    print(Fore.RED + "❌ Unable to delete the file. Scrambling content instead.")
                    scramble_file_content(temp_file_path)
        except Exception as e:
            print(Fore.RED + f"❌ Failed to create temporary file. Error: {str(e)}")
    else:
        print(Fore.RED + f"❌ No password found for {platform}. Available platforms are:")
        for platform_name in profile["passwords"].keys():
            print(Fore.YELLOW + f"- {platform_name}")