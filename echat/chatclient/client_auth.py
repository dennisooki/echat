#create a function that accepts 2 strings username and password, and checks if username is in echat.db
#if username is in echat.db, use dehash_password function to dehash the password and compare it to the password provided by the user

from ..db.db_controller import *
from ..crypters.cryptr import *

def user_login(username, password):
    print("Attempting LogIn")
    every1=fetch_all_usernames()
    print("Registered users: ", every1)
    info=""
    if username in every1:
        stored_pwd=fetch_password_hash(username)
        hashed_input_pwd=hash_password(password)
        
        if hashed_input_pwd==stored_pwd:
            info="Login Successful"
            print(info)
            return True, info
        else:
            info="Username found but Wrong Password"
            print(info)
            return False, info         
    else:
        info="Username not found"
        print(info)
        return False, info
    
#create a function to register a new user
def user_register(username, password):
    print("Attempting Registration")
    every1=fetch_all_usernames()
    print(every1)
    info=""
    if username in every1:
        info="Username already exists"
        print(info)
        return False, info
    else:
        hashed_input_pwd=hash_password(password)
        insert_user(username, hashed_input_pwd)
        info="Registration Successful"
        print(info)
        return True, info


    