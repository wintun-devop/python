import hashlib


def make_hashing(inputData):
    algorithm = "sha256"
    # Choose the hash algorithm
    hash_algorithm = hashlib.new(algorithm)
    # Encode the password as bytes before hashing
    password_bytes = inputData.encode("utf-8")
    # Update the hash object with the password bytes
    hash_algorithm.update(password_bytes)
    # Get the hexadecimal representation of the hash
    hashed_password = hash_algorithm.hexdigest()
    return hashed_password


a = make_hashing("abc123!@#")
print(a)