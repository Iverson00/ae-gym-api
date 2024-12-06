from cryptography.fernet import Fernet
import os


def get_key():
    if os.getenv("KEY") is None:
        key = Fernet.generate_key().decode()  
        os.environ["KEY"] = key


    return os.getenv("KEY")


def encrypt(data):
    key = get_key().encode()
    cipher_suite = Fernet(key)
    message = data.encode()
    return cipher_suite.encrypt(message)


def decrypt(data):
    key = get_key().encode()
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(data).decode()
