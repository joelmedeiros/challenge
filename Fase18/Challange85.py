numbers = [[], []]

for i in range(1, 8):
    number = int(input(f'Write the number {i}: '))
    if (number % 2 == 0):
        numbers[0].append(number)
    else:
        numbers[1].append(number)

numbers[0].sort()
print(f'The even values are {numbers[0]}')
numbers[1].sort()
print(f'The odd values are {numbers[1]}')