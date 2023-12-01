#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

#User input
age = input("What is your current age?")

#Calculation
age = int(age)

years_remaining = 90 - age
days = (years_remaining * 365)
weeks = (years_remaining * 52)
months = (years_remaining * 12)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")