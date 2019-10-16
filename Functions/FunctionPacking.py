from time import sleep


def higher(*values):
    print('-=' * 30)
    print('Analysing data ...')
    for value in values:
        print(value, end=' ')
        sleep(0.5)
    print(f'There are {len(values)} values')
    print(f'The higher value is {max(values)}')


higher(2, 9, 4, 5, 7, 1)
higher(4, 7, 0)
higher(1, 2)
higher(6)
higher(0)
