import random

is_difficulty_chosen = False
difficulty = -1
user_won = False
counter = 0

print('*****Hello and welcome to the guessing game!*****')
name = input('What is your name? ')
game_difficulty = input('Enter a value of 1, 2, or 3 to choose a difficulty: ')

while is_difficulty_chosen is False:
    try:
        if int(game_difficulty) == 1:
            difficulty = 100
            is_difficulty_chosen = True
        elif int(game_difficulty) == 2:
            difficulty = 500
            is_difficulty_chosen = True
        elif int(game_difficulty) == 3:
            difficulty = 1000
            is_difficulty_chosen = True
        else:
            game_difficulty = input('Enter a value of 1, 2, or 3 to choose a difficulty: ')
    except ValueError:
        print('You did not enter a number try again')
        game_difficulty = input('Enter a value of 1, 2, or 3 to choose a difficulty: ')

magic_number = random.randint(1, difficulty)
print(magic_number)
while user_won is False:
    user_input = input('Guess the number between 1 and ' + str(difficulty) + ': ')
    try:
        user_input = int(user_input)
    except ValueError:
        print('You did not enter a number try again')
        continue
    if user_input == magic_number:
        counter = counter + 1
        print('\nYou Win ' + name + '! The number was ' + str(magic_number))
        print('Total number of guesses was: ' + str(counter))
        user_won = True
    elif user_input > magic_number:
        print('Too high!')
        counter = counter + 1
    elif user_input < magic_number:
        print('Too Low!')
        counter = counter + 1
