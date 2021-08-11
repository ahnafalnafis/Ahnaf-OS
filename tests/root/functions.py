import json
import os
import dotenv


def read(file):
    """To read both json and Plaintext file"""
    if file.endswith(".json"):
        with open(file) as handler:
            content = json.load(handler)
            handler.close()
    else:
        handler = open(file)
        content = handler.read()
        handler.close()

    return content


def verify(username, password):
    """To verify the username and password"""
    dotenv.load_dotenv("etc/passwd")
    users = read("etc/users").split()
    passwd = os.getenv(username)
    if username in users and password == passwd:
        return True

    else:
        return False
