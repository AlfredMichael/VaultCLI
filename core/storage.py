import json

from colorama import Fore
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
import os

from core.encryption import derive_encryption_key, decrypt_master_key


def save_to_file(data, master_key, filename="vault_data.json"):
    """
    Encrypts and saves the data to a file using the master key.
    """
    encryption_key = derive_encryption_key(master_key)  # Derive encryption key from master key
    cipher = Fernet(encryption_key)

    # Serialize and encrypt the data
    serialized_data = json.dumps(data).encode()
    encrypted_data = cipher.encrypt(serialized_data)

    # Save encrypted data to file
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print(Fore.GREEN + f"✅ Data saved securely to {filename}")


def load_from_file(master_key, filename="vault_data.json"):
    """
    Decrypts and loads the data from a file using the master key to derive the encryption key.
    """
    try:
        # Derive encryption key from the provided master key
        encryption_key = derive_encryption_key(master_key)

        # Initialize the cipher with the derived encryption key
        cipher = Fernet(encryption_key)

        # Read the encrypted data from the file
        with open(filename, "rb") as file:
            encrypted_data = file.read()

        # Decrypt the file content using the cipher
        decrypted_data = cipher.decrypt(encrypted_data).decode()

        # Deserialize the JSON data into Python dictionary
        return json.loads(decrypted_data)
    except Exception as e:
        # Handle decryption errors gracefully
        print(Fore.RED + "❌ Decryption failed! Incorrect master key or corrupted file.")
        exit()  # Close the app safely after failure
