from cryptography.fernet import Fernet
import dbfile as db

def encrypt_text(plain_text, key):
    cipher = Fernet(key)
    encrypted = cipher.encrypt(plain_text.encode())
    return encrypted

def decrypt_text(encrypted_text, key):
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_text).decode()
    return decrypted

if __name__ == "__main__":
    key = db.read_pass(2)         # Example: [(2, 'TzJczx8gR...==')]
    key1 = key[0][1].encode()     # Convert to bytes
    print("Key:", key1)

    check = db.read_pass(1)       # [(1, 'gAAAAABl...')]
    print("Encrypted password:", check[0][1])

    print("Key (bytes):", key1)
    print("Length of key:", len(key1))
    print("Encrypted password (raw):", check[0][1])
    print("Encrypted password (type):", type(check[0][1]))
    check2 = check[0][1]
    check2 = check2.encode()
    print("Encrypted password (raw):", check[0][1])
    print("Encrypted password (type):", type(check[0][1]))


    check1 = decrypt_text(check[0][1].encode(), key1)  # ✅ Encode before decrypt
    print("Decrypted password:", check1)
