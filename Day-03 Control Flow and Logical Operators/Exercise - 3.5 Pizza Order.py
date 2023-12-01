# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L- ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

pepperoin = input("Do you want pepperoin? Y or N- ")
if pepperoin == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3
bill_cheese = input("Do you want extra cheese? Y or N- ")
if bill_cheese == "Y":
    bill +=1
    
print(f"Your final bill: {bill}")