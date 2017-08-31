##Hello, coders! An important part of programming is being able to apply your programs, so your challenge for today is to create a calculator application
##that has use in your life. It might be an interest calculator, or it might be something that you can use in the classroom. For example, if you were in physics
##class, you might want to make a F = M * A calc.
##EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A, but also A = F/M, and M = F/A!

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
