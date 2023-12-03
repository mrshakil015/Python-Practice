import random
import hangman_words


choosen_word= random.choice(hangman_words.word_list)
print("Welcome to the hangman game!!!")
print(f'Choosen word is: {choosen_word}')
letter_list=[]
blank_list=[]
temp = 0

stages = ['''
          +---+
          |   |
          0   |
         /|\  |
         / \  |
              |
================              
          ''','''
          +---+
          |   |
          0   |
         /|\  |
         /    |
              |
================              
          ''','''
          +---+
          |   |
          0   |
         /|\  |
              |
              |
================              
          ''','''
          +---+
          |   |
          0   |
         /|   |
              |
              |
================              
          '''
          ,'''
          +---+
          |   |
          0   |
          |   |
              |
              |
================              
          ''','''
          +---+
          |   |
          0   |
              |
              |
              |
================              
          ''','''
          +---+
          |   |
              |
              |
              |
              |
================              
          ''']
# print("tyep is; ", type(stages))
for letter in choosen_word:
    letter_list += letter
    blank_list += '_'
    
iteration = len(set(letter_list))
end_of_game = False
wrong_guess =len(stages)-1 

while not end_of_game:

    guess_letter = input("Guess a letter: ").lower()
    if guess_letter in blank_list:
        print("You already guessed letter: ", guess_letter)
    for position in range(0, len(letter_list)):
        letter = choosen_word[position]
        if letter == guess_letter:
            blank_list[position]= letter
    print("Gussed Letter is: ",blank_list)
    
    # print("Wrong Guess!")
    if guess_letter not in choosen_word:
        print(stages[wrong_guess])
        wrong_guess-=1
        if wrong_guess < 0:
            print("You Loss!!")
            print("Word is: ", choosen_word)
            end_of_game = True
    if "_" not in blank_list:
        end_of_game = True
        print("You won!")

    