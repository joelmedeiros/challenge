n1 = int(input('Write a number: '))
n2 = int(input('Write another number: '))

option = 0
while option != 5:
    option = int(input('''Choose an option:
    [1] Sum
    [2] Multiply
    [3] Greater
    [4] Change numbers
    [5] Exit
    '''))

    if option == 1:
        print('The sum of {} and {} is {}'.format(n1, n2, n1 + n2))
    if option == 2:
        print('The multiply of {} and {} is {}'.format(n1, n2, n1 * n2))
    if option == 3:
        print('The greater number between {} and {} is {}'.format(n1, n2, n1 if n1 > n2 else n2))
    if option == 4:
        n1 = int(input('Write a number: '))
        n2 = int(input('Write another number: '))
    else:
        print('Invalid option.')