sum = numbers = i = 0
num = int(input('Write a number [999 to stop]: '))
while num != 999:
    numbers += 1
    sum += num
    num = int(input('Write a number [999 to stop]: '))
    i += 1

print('You wrote down {} numbers and the sum of them is {}.'.format(numbers, sum))