#!/usr/bin/python3
""" Exercise Fifteen Password Validation """
import getpass as g

def main():
    """ Validate user input against stored credentials """
    user_creds = {
        'bob':'struggle_bus',
        'tom':'strongpassword',
        'barnes':'sad_lad123',
        }
    username = g.getpass(prompt="Username: ")
    password = g.getpass(prompt="Password: ")
    if username in user_creds.keys():
        if password == user_creds[username]:
            print("Login Successful")
        else:
            print("Username of password incorrect")
    else:
        print("Username or password incorrect")

if __name__ == "__main__":
    main()
