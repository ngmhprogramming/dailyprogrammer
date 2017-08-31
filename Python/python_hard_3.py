##Welcome to cipher day!
##For this challenge, you need to write a program that will take the scrambled words from this post, and compare them against THIS WORD LIST to
##unscramble them. For bonus points, sort the words by length when you are finished. Post your programs and/or subroutines!
##Here are your words to de-scramble:
##mkeart
##sleewa
##edcudls
##iragoge
##usrlsle
##nalraoci
##nsdeuto
##amrhat
##inknsy
##iferkna

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
