def sort():
    terms = input("Enter terms, separated by a space: ")
    terms = " ".join(sorted(terms.split(" ")))
    print(terms)

if __name__ == "__main__":
    sort()
