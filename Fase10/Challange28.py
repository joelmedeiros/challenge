from random import randint
randomNumber = randint(0,5)
number = int(input('Try to discover the number: '))
print("You're right!" if number == randomNumber else "You missed!")
print('The random number was {}' . format(randomNumber))