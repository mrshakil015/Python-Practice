# Claculates he Body Mass Index (BMI) form a user's weight and height


height = input("Enter your hight in m: ")
weight = input("Enter your weight in kg: ")

weight = int(weight)
height = float(height)

BMI = weight/(height ** 2)
print("BMI is: "+str(BMI))