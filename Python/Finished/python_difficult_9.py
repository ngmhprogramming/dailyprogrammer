def replaceText():
    original = input("Original String: ")
    new = input("New String: ")
    with open("python_difficult_9_text.txt", "r+") as file:
        contents = file.read().replace(original, new)
    with open("python_difficult_9_text.txt", "w+") as file:
        file.write(contents)

if __name__ == "__main__":
    replaceText()
