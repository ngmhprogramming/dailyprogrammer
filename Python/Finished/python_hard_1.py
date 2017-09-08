def guess():
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

if __name__ == "__main__":
    guess()
