tuple = int(input('Write a number: ')), \
        int(input('Write another number: ')), \
        int(input('Write another one: ')), \
        int(input('Write the last one: '))

print(f'You wrote these numbers {tuple}')
print(f'The 9 value appeared {tuple.count(9)} times')
if (tuple.index(3)):
    print(f'The 3 value appeared {tuple.index(3)+1} position')
else:
    print(f'The 3 value appeared in none position')

print('The odd values are: ', end=' ')
for i in range(0, len(tuple)):
    print(tuple[i] if tuple[i] % 2 == 0 else '', end=' ')
