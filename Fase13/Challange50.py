sum = 0
for i in range(0, 6):
    number = int(input('Write a number: '))
    if (number % 2 == 0):
        sum += number
print('The total is {}'.format(sum))