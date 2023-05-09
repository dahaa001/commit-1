import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    wrong_guess=0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            wrong_guess += 1
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            wrong_guess += 1
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!! It took {wrong_guess + 1} guesses in total. You had in total {wrong_guess} wrong')


guess(10)