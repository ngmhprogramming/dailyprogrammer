##create a calculator program that will take an input, following normal calculator input (5*5+4) and give an answer (29). This calculator should use all four
##operators.
##For extra credit, add other operators (6(4+3), 3 ** 3, etc.)

from ast import literal_eval

while True:
    mode = input("Which mode? 1 for scam mode and 2 for legit mode.")
    expression = input("Enter expresesion. ")
    if mode == "1":
        print(literal_eval(expression))
    if mode == "2":
        print(calculate(expression))
