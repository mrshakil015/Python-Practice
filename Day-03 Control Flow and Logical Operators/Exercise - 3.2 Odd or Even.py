print("Welcome to the Odd & Even Number checker!")
number = int(input("Which number do you want to check? "))


result = number % 2
if result == 0:
    print("This is an even number.")
else:
    print("This is and odd number.")