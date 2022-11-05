'''Rijndael Symmetric Encryption'''
from time import time
from cryptography.fernet import Fernet


def encryptor(data: str):
    key = Fernet.generate_key()
    f = Fernet(key)
    r = f.encrypt(bytes(data, 'utf-8')).decode()
    return r, key


def decryptor(data: str, key: str):
    f = Fernet(key)
    r = f.decrypt(bytes(data, 'utf-8')).decode()
    if not r:
        raise ValueError('Error decryption failed')
    return r
