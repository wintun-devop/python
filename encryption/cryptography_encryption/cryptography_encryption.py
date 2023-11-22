from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return encrypted_message


def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode("utf-8")
    return decrypted_message


# generate key
key = generate_key()
print("key", key)

m = "I love you baby!You are my crazy!"

# encrypt data
encrypt_data = encrypt_message(m, key)
print("encrypt", encrypt_data)

# decrypt data
decrypt_data = decrypt_message(encrypt_data, key)
print("OriginData", decrypt_data)