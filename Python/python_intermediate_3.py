##Welcome to cipher day!
##Create a program that can take a piece of text and encrypt it with an alphabetical substitution cipher. This can ignore white space, numbers, and symbols.
##for extra credit, make it encrypt whitespace, numbers, and symbols!
##for extra extra credit, decode someone elses cipher!

from random import randint

def encrypt(text, key):
    if key == "":
        for char in range(16):
            key += chr(randint(0, 127))
        print("Your key is " + key)
    if len(text) != len(key):
        oldKey = key
        key = ""
        for char in range(len(text)):
            key += oldKey[char % len(oldKey)]
    encrypted = ""
    for char in range(len(text)):
        newASCII = ord(text[char]) + ord(key[char])
        multiple = newASCII // 127
        newASCII -= multiple * 127
        encrypted += chr(newASCII)
    print("The encrypted text is:\n" + encrypted)

def decrypt(text, key):
    if key == "":
        for char in range(16):
            key += chr(randint(0, 127))
        print("Your key is " + key)
    if len(text) != len(key):
        oldKey = key
        key = ""
        for char in range(len(text)):
            key += oldKey[char % len(oldKey)]
    decrypted = ""
    for char in range(len(text)):
        newASCII = ord(text[char]) - ord(key[char])
        if newASCII < 0:
            newASCII = 127 + newASCII
        decrypted += chr(newASCII)
    print("The decrypted text is:\n" + decrypted)

def caesarDecrypt(text, key):
    decrypted = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if key == "":
        for tried in range(len(alphabet) - 1):
            print("Trying with the key " + str(tried) + ".")
            key = tried + 1
            for char in text:
                if char in alphabet:
                    newIndex = alphabet.index(char) - key
                    if newIndex < 0:
                        newIndex = len(alphabet) + newIndex
                    decrypted += alphabet[newIndex]
                elif char in alphabet.upper():
                    newIndex = alphabet.upper().index(char) - key
                    if newIndex < 0:
                        newIndex = len(alphabet) + newIndex
                    decrypted += alphabet.upper()[newIndex]
                else:
                    decrypted += char
            print("The decrypted text is:\n" + decrypted)
            decrypted = ""
    else:
        key = int(key)
        for char in text:
            if char in alphabet:
                newIndex = alphabet.index(char) - key
                if newIndex < 0:
                    newIndex = len(alphabet) + newIndex
                decrypted += alphabet[newIndex]
            elif char in alphabet.upper():
                newIndex = alphabet.upper().index(char) - key
                if newIndex < 0:
                    newIndex = len(alphabet) + newIndex
                decrypted += alphabet.upper()[newIndex]
            else:
                decrypted += char
        print("The decrypted text is:\n" + decrypted)

print("Some samples.")
print("Encrypting with Text = ILoveReddit, Key = dailyprogrammer")
encrypt("ILoveReddit", "dailyprogrammer")
print("Decrypting with Text = ..Yc_CXTL\V, Key = dailyprogrammer")
decrypt("..Yc_CXTL\V", "dailyprogrammer")

print("Protip: It may not work on multi-line inputs, so if it doesn't work you should remove the line break and replace it with a random character as a substitution.")
while True:
    action = input("What do you want to do?\n1) Encrypt\n2) Decrypt\n3) Decrypt Caesar")
    text = input("Enter your text. ")
    key = input("Enter your key. Leave blank for a random key. Or Brute Force for Caesar decrypt.")
    if action == "1":
        encrypt(text, key)
    elif action == "2":
        decrypt(text, key)
    elif action == "3":
        caesarDecrypt(text, key)
