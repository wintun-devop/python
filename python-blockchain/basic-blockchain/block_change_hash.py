import hashlib

#Declare a message
message = "Python is great"

#hasing message
h1=hashlib.sha256(message.encode())
h1_digest_message=h1.hexdigest()
print(h1)
print(h1_digest_message)