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

def cipher():
    print("Some samples.")
    print("Encrypting with Text = ILoveReddit, Key = dailyprogrammer")
    encrypt("ILoveReddit", "dailyprogrammer")
    print("Decrypting with Text = ..Yc_CXTL\V, Key = dailyprogrammer")
    decrypt("..Yc_CXTL\V", "dailyprogrammer")

    print("Protip: It may not work on multi-line inputs, so if it doesn't work you should remove the line break and replace it with a random character as a substitution.")
    while True:
        action = input("What do you want to do?\n1) Encrypt\n2) Decrypt ")
        text = input("Enter your text. ")
        key = input("Enter your key. Leave blank for a random key. ")
        if action == "1":
            encrypt(text, key)
        elif action == "2":
            decrypt(text, key)

if __name__ == "__main__":
    cipher()
