#function to hash a password that accepts a string
import hashlib

def hash_password(password):
    #hash the password using sha256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

