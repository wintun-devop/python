import bcrypt


def make_hashing(input: str):
    # converting password to array of bytes
    bytes = input.encode("utf-8")
    # generating the salt
    salt = bcrypt.gensalt()
    # Hashing the password
    hash = bcrypt.hashpw(bytes, salt)
    return hash


def check_hashing(input: str, hashInput: str):
    # encoding user password
    userBytes = input.encode("utf-8")
    # checking password
    result = bcrypt.checkpw(userBytes, hashInput)
    return result


a = make_hashing("abc123!@#")
print(">>>", a)
b = check_hashing("abc123!@#", a)
print(b)