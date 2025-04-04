import base64
import os

from colorama import Fore
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def derive_encryption_key(master_key, salt=b"vault_salt"):
    """
    Derives an encryption key from the master key using PBKDF2.
    """
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(master_key.encode()))


def encrypt_master_key(master_key, encryption_key):
    """
    Encrypts the master key using a derived encryption key.
    """
    fernet = Fernet(encryption_key)
    return fernet.encrypt(master_key.encode()).decode()


def decrypt_master_key(encrypted_master_key):
    """
    Decrypts the master key using the encryption key retrieved from the environment variable.
    """
    # Retrieve the encryption key from the environment variable
    encryption_key = os.environ.get("VAULTCLI_ENCRYPTION_KEY")

    if encryption_key is None:
        raise Exception(Fore.RED + "❌ Encryption key not found in environment variable.")

    # Use the retrieved encryption key for decryption
    fernet = Fernet(encryption_key)
    return fernet.decrypt(encrypted_master_key.encode()).decode()


def generate_key():
    return Fernet.generate_key()


def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())


def decrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.decrypt(data).decode()
