##Your challenge for today is to create a program which is password protected, and wont open unless the correct user and password is given.
##For extra credit, have the user and password in a seperate .txt file.
##for even more extra credit, break into your own program :)

from hashlib import sha1

with open("python_easy_5_usernames.data", "a+", encoding="utf-8") as file:
    pass

with open("python_easy_5_passwords.data", "a+", encoding="utf-8") as file:
    pass

usernames = []
passwords = []

def getData():
    global usernames
    global passwords
    with open("python_easy_5_usernames.data", "r+", encoding="utf-8") as file:
        usernames = file.read()
        usernames = usernames.split("\n")

    with open("python_easy_5_passwords.data", "r+", encoding="utf-8") as file:
        passwords = file.read()
        passwords = passwords.split("\n")

def login(username, password):
    global usernames
    global passwords
    getData()
    if sha1(username.encode("utf-8")).hexdigest() not in usernames:
        return False
    elif passwords[usernames.index(sha1(username.encode("utf-8")).hexdigest())] == sha1(password.encode("utf-8")).hexdigest():
        return True
    else:
        return False

def signup(username, password):
    global usernames
    getData()
    if username in usernames:
        return False
    else:
        with open("python_easy_5_usernames.data", "a+", encoding="utf-8") as file:
            file.write(username + "\n")

        with open("python_easy_5_passwords.data", "a+", encoding="utf-8") as file:
            file.write(sha1(password.encode("utf-8")).hexdigest() + "\n")
        return True

while True:
    action = input("What would you like to do?\n1) Signup\n2) Login\nAction: ")
    username = input("Username: ")
    password = input("Password: ")

    if action == "1":
        result = signup(username, password)
        
        if result:
            print("Signup Successful.")
        else:
            print("Signup Unsuccessful.")
    elif action == "2":
        result = login(username, password)
        
        if result:
            print("Login Successful.")
        else:
            print("Login Unsuccessful.")
