from random import randint
tuple = randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10)

print('The generated numbers are: ', end= '')

higher = tuple[0]
smaller = tuple[len(tuple)-1]
for i in range(0, len(tuple)):
    print(tuple[i], end=' ')

print(f'\nThe smaller number is: {max(tuple)}')
print(f'The higher number is: {min(tuple)}')