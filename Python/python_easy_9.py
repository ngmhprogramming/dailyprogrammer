##write a program that will allow the user to input digits, and arrange them in numerical order.
##for extra credit, have it also arrange strings in alphabetical order
terms = input("Enter terms, separated by a space: ")
terms = " ".join(sorted(terms.split(" ")))
print(terms)
