import random

word_list = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Grape']

class Hangman:

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word = self.word.lower()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(list(set(self.word)))
        self.list_of_guesses = []

    def check_guess(self, guess):
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for index, letter in enumerate(self.word): 
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')
        self.list_of_guesses.append(guess)

    def ask_for_input(self):
        while True:
            guess = input('What is your letter?')
            if guess.isalpha() != True and len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                break

def play_game(word_list):
    game = Hangman(word_list)
    while True:
        if game.num_letters > 0 and game.num_lives != 0:
            game.ask_for_input()
            print(game.word_guessed)
            continue
        elif game.num_lives == 0 and game.num_letters > 0:
            print('You lost!')
            break
        elif game.num_lives > 0 and game.num_letters == 0:
            print ('Congratulations. You won the game!')
            break

play_game(word_list)
