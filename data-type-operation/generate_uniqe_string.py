import random
import string

def generate_unique_string() -> str:
    length = 30
    chars = string.ascii_letters + string.digits
    result = ''.join(random.choice(chars) for _ in range(length))
    return result

unique_string = generate_unique_string()
print(unique_string)
