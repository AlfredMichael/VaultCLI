from func.create_profile import create_profile
from func.backup_data import backup_data
from func.load_backup import load_backup
from func.save_password import save_password
from func.request_password import request_password
from colorama import init, Fore, Style
from func.clear_screen import clear_screen

# Initialize Colorama for colored terminal output
init(autoreset=True)

# Implement business logic like what happens when a user enters an email that doesnt qualify as an original email or a name that corresponds to your name


def main():
    while True:
        # clear_screen()
        print(Fore.CYAN + "🌟 Welcome to VaultCLI - Your Secure Password Manager 🌟")
        print(Fore.LIGHTGREEN_EX + "\nWhat would you like to do today?")
        print(Fore.YELLOW + "1. 🆕 Create Profile")
        print(Fore.YELLOW + "2. 💾 Save Password")
        print(Fore.YELLOW + "3. 🔍 Request Password")
        print(Fore.YELLOW + "4. 📤 Backup Data")
        print(Fore.YELLOW + "5. ♻️ Load Backup")
        print(Fore.YELLOW + "6. ❌ Exit")
        choice = input(Fore.LIGHTBLUE_EX + "\nChoose an option (1-5): ")

        if choice == "1":
            create_profile()
        elif choice == "2":
            save_password()
        elif choice == "3":
            request_password()
        elif choice == "4":
            backup_data()
        elif choice == "5":
            load_backup()
        elif choice == "6":
            print(Fore.LIGHTMAGENTA_EX + "\n👋 Goodbye! Stay safe! 🔐\n")
            break
        else:
            print(Fore.RED + "\n❌ Invalid choice. Please try again.")




if __name__ == "__main__":
    main()
