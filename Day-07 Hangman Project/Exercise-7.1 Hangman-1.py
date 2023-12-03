import random
word_list = ["ardvark", "baboon", "camel"]

choosen_word= random.choice(word_list)
print(choosen_word)
guess_letter = input("Guess a letter: ").lower()
for letter in choosen_word:
    if letter == guess_letter:
        print("Right")
    else:
        print("Wrong")
    