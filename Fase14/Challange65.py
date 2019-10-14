average = count = sum = max = min = 0
wannaContinue = 'Y'
while wannaContinue == 'Y':
    num = int(input('Write a number: '))
    if (count == 0 or max < num):
        max = num

    if (count == 0 or min > num):
        min = num

    count += 1
    sum += num
    wannaContinue = str(input('Do you want to continue? [Y/N]')).upper()
average = sum/count
print('You wrote down {} numbers, the average is {}, the greater number is {} and smallest is {}'.format(count, average, max, min))
