##create a program that will ask the users name, age, and reddit username. have it tell them the information
##back, in the format:
##your name is (blank), you are (blank) years old, and your username is (blank)
##for extra credit, have the program log this information in a file to be accessed later.

name = input("What is your name? ")
age = input("What is your age? ")
username = input("What is your Reddit username? ")
with open("python_easy_1_details.data", "a+", encoding="utf-8") as file:
    file.write(name + " " + age + " " + username + "\n")
print("Your name is " + name + ", you are " + age + " years old, and your username is " + username + "!")
