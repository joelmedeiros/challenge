sum = count = 0
while True:
    number = int(input('Write a number: '))
    if (number == 999):
        break
    sum += number
    count += 1

print(f'You wrote down {count} numbers and the sum between them is {sum}')