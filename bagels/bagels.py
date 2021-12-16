"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(f'''
    Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com

    I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
    Try to guess what it is. 
    Here are some clues:
    When I say:         That means:
    Pico                One digit is correct but in the wrong position.
    Fermi               One digit is correct and in the right position.
    Bagels              No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.
    ''')
    while True:
        secret_num = get_secret_num(NUM_DIGITS)
        print('I have thought up a number.')
        print(f'You have {MAX_GUESSES} guesses to get it.')

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{num_guesses}: ')
                guess = input('> ')
            
            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(f'The answer was {secret_num}.')
            
        print('Do you want to play again? (yes or no)')
        if input('> ').lower().startswith('n'):
            break
    
    print('Thanks for playing!')



def get_clues(guess, secret_num):
    '''Returns a string with Pico, Fermi, Bagels clues for a guess and secret_num pair.'''
    if guess == secret_num:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        # Check if there's a matching digit in a correct place
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        # Check if there's a matching digit but not in correct place
        elif guess[i] in secret_num:
            clues.append('Pico')
    
    # No matching digits found at all
    if len(clues) == 0:
        return 'Bagels'
    
    else:
        # sort clues so their order doesn't reveal order or digits
        clues.sort()
        return ' '.join(clues)

def get_secret_num(digits):
    '''Returns a string made up of NUM_DIGITS unique random digits.'''
    numbers = list('0123456789')
    random.shuffle(numbers)

    secret_num = ''
    for i in range(digits):
        secret_num += str(numbers[i])
    return secret_num


if __name__ == '__main__':
    main()