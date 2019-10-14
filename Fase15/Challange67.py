while True:
    number = int(input('What number you want to see the table? '))
    if (number < 0):
        break

    print('-' * 30)
    i = 1
    while True:
        print(f'{number} x {i} = {i*number}')
        if (i == 10):
            break
        i +=1
    print('-' * 30)

print('Bye ...')
