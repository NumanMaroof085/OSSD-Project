from cryptography.fernet import Fernet
import hashlib as hl
import dbfile as db

def encrypt(text):
    return hl.sha256(text.encode()).hexdigest()


def encrypt_text(plain_text, key):
    cipher = Fernet(key)
    encrypted = cipher.encrypt(plain_text.encode())
    return encrypted

def decrypt_text(encrypted_text, key):
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_text).decode()
    return decrypted

