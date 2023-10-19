import random

word_list = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Grape']

word = random.choice(word_list)

print(word)

guess = input('What is your letter?')

if len(guess) == 1:
    print('Good guess.')
else:
    print('Oops! That is not a valid input.')

print(guess)