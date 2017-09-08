from string import whitespace, punctuation

def anagrams():
    print("Story from http://www.classicshorts.com/stories/aos.html.")
    
    with open("python_difficult_5_text.txt", "r+") as file:
        text = file.read().lower()
        for char in punctuation:
            text = text.replace(char, "")
        for char in whitespace:
            if char != " ":
                text = text.replace(char, "")
        text = text.split(" ")

    anagrams = []

    for char in text:
        matches = []
        sort = "".join(sorted(list(char)))
        matches.append(char)
        for check in text[1:]:
            if sort == "".join(sorted(list(check))):
                if check not in matches:
                    text.pop(text.index(check))
                    matches.append(check)
        if len(matches) > 1:
            anagrams.append(matches)
        text.pop(text.index(char))

    for anagram in anagrams:
        anagram.sort()

    final = []
    for anagram in anagrams:
        if anagram not in final:
            final.append(anagram)

    anagrams = final

    compiled = "Anagrams:\n"
    for anagram in anagrams:
        compiled += ", ".join(anagram) + "\n"
    compiled = compiled[:-1]

    print(compiled)

if __name__ == "__main__":
    anagrams()
