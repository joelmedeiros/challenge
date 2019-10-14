from random import randint
from time import sleep

print('-' * 54)
print('                         Games')
print('-' * 54)
games = int(input('How many games do you want? '))

print('=-'*10, 'Raffle games', '=-'*10)

for number in range(0, games):
    game = []
    count = 0
    while count < 6:
        randNumber = randint(1, 60)
        if (randNumber in game):
            continue
        game.append(randNumber)
        count += 1

    game.sort()
    print(f'Game {number+1}: {game}')
    game.clear()
    sleep(1)

print('=-'*10, '< Good luck! >', '=-'*10)