#! /usr/bin/env python
import main
from functions import verify

if __name__ == "__main__":
    username = input("Username: ")
    password = input("Password: ")
    verified = verify(username, password)
    if verified:
        logged_in = True
        main.main(username)
    else:
        print("Username or password is incorrect")
