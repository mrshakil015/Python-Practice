first = input("Enter first numbr: ")
operator = input("Enter operator (+,-,*,/,%) : ")
second = input("Enter your second number: ")

first = int(first)
second = int(second)
if operator == "+":
    print("Summation: ", first+second)
elif operator == "-":
    print("Subtraction: ", first-second)
elif operator == "*":
    print("Multiplication: ", first*second)
elif operator == "/":
    print("Divide: ", first/second)
elif operator == "%":
    print("Modulas: ", first%second)
else:
    print("Invalid calculation")
