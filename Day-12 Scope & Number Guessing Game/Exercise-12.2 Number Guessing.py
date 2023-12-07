import random
from number_guess_art import logo, won, lose

print(logo)
random_num = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' of 'hard': ").lower()

if level == 'easy':
    remaining = 10
    repeat = False
    while not repeat:
        if remaining == 0:
            print("You not guess the number!")
            print(lose)
            repeat = True
        else:
            print(f"You have {remaining} attempts to guess the number.")
            guess = int(input("Make a guess: "))
            if guess > random_num:
                print("Too high.")
            elif guess < random_num:
                print("Too low.")
            elif guess == random_num:
                print(f"You got it! The anser was {random_num}")
                print(won)
                repeat = True
        remaining -=1
elif level == 'hard':
    remaining = 5
    repeat = False
    while not repeat:
        if remaining == 0:
            print("You not guess the number!")
            print(lose)
            repeat = True
        else:
            print(f"You have {remaining} attempts to guess the number.")
            guess = int(input("Make a guess: "))
            if guess > random_num:
                print("Too high.")
            elif guess < random_num:
                print("Too low.")
            elif guess == random_num:
                print(f"You got it! The anser was {random_num}")
                print(won)
        remaining -=1