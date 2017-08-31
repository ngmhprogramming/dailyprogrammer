##This works by inserting a new username and password at the start of the file
##This works because the login program searches from the start to end so the
##fake details are picked up instead

from hashlib import sha1

usernames = ""
passwords = ""

with open("python_easy_5_usernames.data", "a+", encoding="utf-8") as file:
    usernames = file.read()

with open("python_easy_5_passwords.data", "a+", encoding="utf-8") as file:
    passwords = file.read()

while True:
    username = input("Username to insert / hack. ")
    password = input("Password to use. ")
    
    with open("python_easy_5_usernames.data", "w", encoding="utf-8") as file:
        file.write(sha1(username.encode("utf-8")).hexdigest() + "\n" + usernames)
    
    with open("python_easy_5_passwords.data", "w", encoding="utf-8") as file:
        file.write(sha1(password.encode("utf-8")).hexdigest() + "\n" + passwords)
    
    print("Done.")
