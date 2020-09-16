import random

print('Hello Cookbook')
name = input('What is your name? ')
print('Hello ' + name)
fav_num = input('What is your favorite number ' + name + '? ')

try:
    print(name + ' your number doubled is: ' + str(int(fav_num) * 2))
except ValueError:
    print('You did not enter a number ' + name + '! a random number chosen.')
    print(name + ' your number doubled is: ' + str(random.randint(1, 100)))
