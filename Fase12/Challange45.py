from random import randint
player = int(input('''1- Rock
2 - Paper
3 - Scissors\n'''))

print('Player: ')
if (player == 1):
    print('Rock')
elif (player == 2):
    print('Paper')
else:
    print('Scissors')

computer = randint(1,3)
print('Computer: ')
if (computer == 1):
    print('Rock')
elif (computer == 2):
    print('Paper')
else:
    print('Scissors')

if (computer == 1 and player == 1) or (computer == 2 and player == 2) or (computer == 3 and player == 3):
    print('Try again')
elif(computer == 1 and player == 2) or (computer == 2 and player == 3) or (computer == 3 and player == 1):
    print('You win!')
else:
    print('You lose!')



