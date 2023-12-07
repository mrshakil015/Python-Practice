
#Add
def add(n1, n2):
    return n1 + n2

#Subtraction
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


num1 = float(input("What's your first number?: "))
num2 = float(input("What's another number?: "))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick any operation from the line above: ")
calculation = operations[operation_symbol]
answer = calculation(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
iteration = False
while not iteration:
    repeate = input("Do you want to run any operation? Yes or No: ").lower()
    if repeate == "yes":
        operation_symbol = input("Pick another operation: ")
        num3 = float(input("What's another number?: "))
        calculation = operations[operation_symbol]
        num = answer
        answer = calculation(answer, num3)
        print(answer)
        print(f"{num} {operation_symbol} {num3} = {answer}")
    if repeate == "no":
        iteration = True
