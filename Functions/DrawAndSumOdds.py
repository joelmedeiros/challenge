from random import randint
from time import sleep


def randomNumbers(numbers):
    print('Raffling 5 values:')
    for i in range(0, 5):
        value = randint(1, 10)
        print(value, end=' ', flush=True)
        numbers.append(value)
        sleep(.5)


def sumOnlyOdd(numbers):
    sum = 0
    for n in numbers:
        if (n % 2 == 0):
            sum += n
    print(sum)


numbers = []
randomNumbers(numbers)
print('Done!')
print(f'Adding the odd values from {numbers}, we have ', end='')
sumOnlyOdd(numbers)
