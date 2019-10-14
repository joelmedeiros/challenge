from random import randint
from time import sleep
from operator import itemgetter
dice = {}
for i in range(1,5):
    dice[f'player{i}'] = randint(1, 6)
    print(f'The player{i} got {dice[f"player{i}"]} in the dice')
    sleep(0.5)

i = 1
ranking = sorted(dice.items(), key=itemgetter(1), reverse=True)
for player, value in ranking:
    print(f'{i} place: {player} with {value}')
    i += 1