print("Number: ")
for number in range(1, 10): #it execute 1 to 9 except 10
    print(number)

print("Number with step: ")
for number in range(1, 10,2): #it execute after 2 step like-1,3,5...
    print(number)

print("Calcuate all even number from 1 to 100: ")
even_sum = 0
for number in range(2, 101,2):
    even_sum += number
print("Summation of even number from 1 to 100: ", even_sum)

even_sum2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        even_sum2 += number
print("Summation of even number from 1 to 100: ", even_sum2)