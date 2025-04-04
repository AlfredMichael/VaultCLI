import os
from datetime import datetime

from colorama import Fore


def monitor_file_access(file_path, log_file="access_log.txt"):
    """
    Monitors the file access and logs the information in a log file.
    """
    try:
        # Get file access time and log it
        access_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        username = os.getlogin()  # Get current system user
        with open(log_file, "a") as log:
            log.write(f"User '{username}' accessed '{file_path}' at {access_time}\n")
        print(Fore.GREEN + "✅ File access logged successfully.")
    except Exception as e:
        print(Fore.RED + f"❌ Failed to log file access. Error: {str(e)}")