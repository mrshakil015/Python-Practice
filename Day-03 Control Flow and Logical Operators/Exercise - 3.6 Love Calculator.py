#https://app.codingrooms.com/management/assignments/364926/overview

name1 = input("What is your name? ")
name2 = input("What is their name? ")

combined_name = name1 + name2
lower_name = combined_name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

true = t + r + u + e 
 
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score <10 or love_score >90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >=40 or love_score<=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")