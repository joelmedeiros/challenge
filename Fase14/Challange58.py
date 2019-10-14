from random import randint
randomNumber = randint(0,10)
number = None
hunches = 0
hit = False
while hit is False:
    number = int(input('Try to discover the number: '))
    hunches += 1
    hit = number == randomNumber
    print("You're right! You made {} hunches".format(hunches) if hit else "You missed! Try again")
