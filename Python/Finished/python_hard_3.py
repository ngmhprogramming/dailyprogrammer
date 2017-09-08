def unscramble():
    searches = ["mkeart", "sleewa", "edcudls", "iragoge", "usrlsle", "nalraoci", "nsdeuto", "amrhat", "inknsy", "iferkna"]
    results = []

    with open("python_hard_3_wordlist.txt") as file:
        words = file.read();
        words = words.split("\n")
        for search in searches:
            for word in words:
                if sorted(search) == sorted(word):
                    results.append(word)
                    break

    for search in range(len(searches)):
        print(searches[search] + " unscrambled is " + results[search])

if __name__ == "__main__":
    unscramble()
