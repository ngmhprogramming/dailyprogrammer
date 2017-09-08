def bottleSong():
    bottles = 99

    while bottles > 0:
        if bottles == 1:
            print(str(bottles) + " bottles of beer on the wall, " + str(bottles) + " bottle of beer.", end=" ")
        else:
            print(str(bottles) + " bottles of beer on the wall, " + str(bottles) + " bottles of beer.", end=" ")
        bottles -= 1
        if bottles == 1:
            print("Take one down and pass it around, " + str(bottles) + " bottle of beer on the wall.", end=" ")
        elif bottles == 0:
            print("Take one down and pass it around, no more bottles of beer on the wall.", end=" ")
        else:
            print("Take one down and pass it around, " + str(bottles) + " bottles of beer on the wall.", end=" ")
    print("No more bottles of beer on the wall, no more bottles of beer.", end=" ")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.", end=" ")

if __name__ == "__main__":
    bottleSong()
