##we all know the classic "guessing game" with higher or lower prompts. lets do a role reversal; you create a program that will guess numbers between
##1-100, and respond appropriately based on whether users say that the number is too high or too low. Try to make a program that can guess your number
##based on user input and great code!

limit = int(input("Maximum possible number? Guesses will be from 1 to this number. "))
guessed = False
low = 1
high = limit
tries = 0
while not guessed:
    tries += 1
    guess = ((low + high) // 2) + 1
    response = input("Is " + str(guess) + " your number? Reply Y for yes, H if your number is higher, and L if your number is lower. ")
    if response == "Y":
        print("That took " + str(tries) + " tries!")
        guessed = True
    elif response == "H":
        low = guess
    elif response == "L":
        high = guess - 2
