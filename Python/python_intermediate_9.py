##Write a program that will take a string ("I LIEK CHOCOLATE MILK"), and allow the user to scan a text file
##for strings that match. after this, allow them to replaces all instances of the string with another
##("I quite enjoy chocolate milk. hrmmm. yes.")
original = input("Original String: ")
new = input("New String: ")
with open("python_intermediate_9_text.data", "r+") as file:
    contents = file.read().replace(original, new)
with open("python_intermediate_9_text.data", "w+") as file:
    file.write(contents)
