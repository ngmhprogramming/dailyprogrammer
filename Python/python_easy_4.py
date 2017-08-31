##You're challenge for today is to create a random password generator!
##For extra credit, allow the user to specify the amount of passwords to generate.
##For even more extra credit, allow the user to specify the length of the strings he wants to generate!

from random import randint

number = input("Number of passwords? ")
length = input("Length of passwords? ")
mode = input("Mode? 1 for all ASCII or 2 for character set. ")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()_+-={}[]|\:;<>?,./\'\""

for i in range(int(number)):
    password = ""
    for j in range(int(length)):
        if mode == "1":
            password += chr(randint(0, 127))
        elif mode == "2":
            password += characters[randint(0, len(characters) - 1)]
    print(password)
