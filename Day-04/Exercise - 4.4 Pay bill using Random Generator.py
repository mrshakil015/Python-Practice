# https://app.codingrooms.com/management/assignments/364928/overview
import random
name_string = input("Give me everybody's names, seperated by a comma. ")
names = name_string.split(", ")

#Way-1
num_items = len(names)
random_choice = random.randint(0, num_items-1)
person_who_will_pay = names[random_choice]
print(f"{person_who_will_pay} is going to by the meal today.")

#Way-2
person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} is going to by the meal today.")