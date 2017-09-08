def details():
    name = input("What is your name? ")
    age = input("What is your age? ")
    username = input("What is your Reddit username? ")
    with open("python_get_details_details.txt", "a+", encoding="utf-8") as file:
        file.write(name + " " + age + " " + username + "\n")
    print("Your name is " + name + ", you are " + age + " years old, and your username is " + username + "!")

if __name__ == "__main__":
    details()
