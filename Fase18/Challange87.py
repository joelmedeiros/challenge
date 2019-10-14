matrix = []
evenSum = thirdColumnSum = 0
for x in range(0, 3):
    matrix.append([])
    for y in range(0, 3):
        number = int(input(f'Write a value for [{x}, {y}]: '))
        matrix[x].append(number)
        if (number % 2 == 0):
            evenSum += number
        if (y == 2):
            thirdColumnSum += number
print("~=" * 30)
for m in matrix:
    for n in m:
        print(f'[{n: ^5}]', end='')
    print('')
print("~=" * 30)

print(f'The sum of even numbers is {evenSum}')
print(f'The sum of the third column values is {thirdColumnSum}')
print(f'The greatest value in the second line is {max(matrix[1])}')