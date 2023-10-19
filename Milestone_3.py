import random

word_list = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Grape']

word = random.choice(word_list)

print(word)

def check_guess(guess):
        if guess in word:
            print(f'Good guess! {guess} is in the word.')
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')

def ask_for_input():
       while True:
        guess = input('What is your letter?')
        guess.lower()
        if guess.isalpha() == True and len(guess) == 1:
            print(guess)
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
        check_guess(guess)

ask_for_input()