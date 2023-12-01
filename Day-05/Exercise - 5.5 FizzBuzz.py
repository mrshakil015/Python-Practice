# Fizz buzz is a group word game for children to teach them about division.[1] Players take turns to count incrementally, replacing any number divisible by three with the word "fizz", and any number divisible by five with the word "buzz", and any number divisible by both 3 and 5 with the word "fizzbuzz".
print("FizzBuzz Count start:")
for number in range(1,101):
    if number % 3 ==0:
        if number % 5 ==0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif number % 5 ==0:
        print("Buzz")
    else:
        print(number)
