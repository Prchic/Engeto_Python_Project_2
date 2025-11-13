"""
Projekt 2: Bulls & Cows

author: Martin Prchal
email: prchalmartin2@gmail.com
"""


import random

# Konstanty
LENGTH = 4  # délka tajného čísla


# Úvodní text
def hello():
    print('Hi there!')
    print('-' * 60)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print('-' * 60)
    print('Enter a number:')
    print('-' * 60)


# Generování tajného čísla
def generate_secret():
    digits = list('0123456789')
    first = random.choice(digits[1:])
    digits.remove(first)

    secret = [first]
    while len(secret) < LENGTH:
        d = random.choice(digits)
        secret.append(d)
        digits.remove(d)

    return ''.join(secret)


# Kontrola vstupu hráče
def is_valid_guess(guess):
    if len(guess) != LENGTH:
        return False, 'Please enter exactly 4 digits.'
    if not guess.isdigit():
        return False, 'Your guess must contain digits only.'
    if guess[0] == '0':
        return False, 'The number must not start with zero.'
    if len(set(guess)) != len(guess):
        return False, 'All digits must be unique (no duplicates).'
    return True, ''


# Vyhodnocení pokusu
def evaluate(secret, guess):
    bulls = 0
    cows = 0

    i = 0
    while i < LENGTH:
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
        i += 1

    return bulls, cows


# Malá pomůcka pro jednotné/množné číslo
def plural(n, word):
    if n == 1:
        return f'{n} {word}'
    else:
        return f'{n} {word}s'


# Hlavní program
def main():
    hello()
    secret = generate_secret()
    attempts = 0

    while True:
        guess = input('>>> ').strip()

        ok, msg = is_valid_guess(guess)
        if not ok:
            print(msg)
            continue

        attempts += 1
        bulls, cows = evaluate(secret, guess)

        if bulls == LENGTH:
            print("Correct, you've guessed the right number")
            if attempts == 1:
                print('in 1 guess!')
            else:
                print(f'in {attempts} guesses!')
            print('-' * 60)
            print("That's amazing!")
            print('Game over. Thanks for playing.')
            break
        else:
            print(f'{plural(bulls, "bull")}, {plural(cows, "cow")}')


if __name__ == '__main__':
    main()
