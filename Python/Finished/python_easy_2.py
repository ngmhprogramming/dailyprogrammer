def unknownForce():
    mode = input("What is your unknown in F = MA? ")
    if mode == "F":
        m = int(input("Enter M in Kilograms. "))
        a = int(input("Enter A in m/sec^2. "))
        print("F is " + str(m * a) + " Newtons.")
    elif mode == "M":
        f = int(input("Enter F in Newtons. "))
        a = int(input("Enter A in m/sec^2. "))
        print("M is " + str(f // a) + " Kilograms.")
    elif mode == "A":
        f = int(input("Enter F in Newtons. "))
        m = int(input("Enter M in Kilograms. "))
        print("A is " + str(f // m) + " m/sec^2.")

if __name__ == "__main__":
    unknownForce()
