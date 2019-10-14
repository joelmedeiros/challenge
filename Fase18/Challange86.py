matrix = []
for x in range(0, 3):
    matrix.append([])
    for y in range(0, 3):
        matrix[x].append(int(input(f'Write a value for [{x}, {y}]: ')))

for m in matrix:
    for n in m:
        print(f'[{n:^5}]', end='')
    print()