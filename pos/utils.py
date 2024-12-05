from cryptography.fernet import Fernet
import os

def get_key():
    key = os.getenv("ENCRYPTION_KEY")
    if not key:
        raise ValueError("ENCRYPTION_KEY environment variable is missing.")
    return key.encode()

def encrypt(data):
    key = get_key()
    cipher_suite = Fernet(key)
    message = data.encode()
    return cipher_suite.encrypt(message)

def decrypt(data):
    key = get_key()
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(data).decode()
