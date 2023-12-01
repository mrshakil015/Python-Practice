# Round Function
a = 8
b = 3

print("Without Round: "+str(a / b))
print("Round Number: "+str(round(a / b)))
#Round the number to the given percision in decimal digits
print("Round Number: "+str(round(a / b, 2))) 
print("Round Number: "+str(round(2.6666666,2)))

#Flow division
print("Without Round: "+str(a // b))

score = 1
height = 1.6
isWinning = False

#Print the info without f-string
print("Your score is: "+str(score)+", Your height is: "+str(height)+", Your are winning is: "+str(isWinning))

#Print the info using f-string
print(f"Your score is: {score}, Your height is: {height}, Your are winning is: {isWinning}")