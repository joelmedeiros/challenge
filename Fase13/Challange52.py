number = int(input('Write a number: '))
divisions = 0
for i in range(1, number+1):
    if (number % i == 0):
        print('\033[33m', end ='')
        divisions += 1
    else:
        print('\033[31m', end ='')

    print(' ' , i, end ='')

print('\n\033[m', end ='')
if (divisions == 2):
    print('The number {} is primary'.format(number))
else:
    print('The number {} is not a primary'.format(number))