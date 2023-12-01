#Input in details
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = int(input("How many people to split the bill? "))

#Concenate the tip percentage
tip_percent = "1."+ tip

#Calculation
total_bill = bill * float(tip_percent)
bill_per_person = round((total_bill/people),2)

#Output
print(f"Each person should pay: {bill_per_person}")