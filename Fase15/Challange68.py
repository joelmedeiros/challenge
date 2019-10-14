from random import randint
win = 0
while True:
    rand = randint(0, 10)
    number = int(input(f'Write a value: '))
    evenOrOdd = ' '
    while evenOrOdd not in 'EeOo':
        evenOrOdd = str(input('You want even or odd? [P/O] ')).lower().strip()[0]
    calc = (rand+number)% 2 == 0
    print(f'I choose ... {rand}')
    if ((evenOrOdd == 'e' and calc is True) or (evenOrOdd == 'o' and calc is False)):
        print('Congrats you win!')
        win += 1
    else:
        print(f'You lose ... ')
        break

print(f'You won {win} times.')