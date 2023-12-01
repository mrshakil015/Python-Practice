print("Welcome to the BMI 2.0 Calculator?")
height = input("Enter your hight in m: ")
weight = input("Enter your weight in kg: ")

weight = int(weight)
height = float(height)

bmi = round(weight/(height ** 2))

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you are normal weight.")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinicaly obese.")