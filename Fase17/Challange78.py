list = list()
for n in range(0, 5):
    list.append(int(input(f'Write a number for position {n}: ')))

print(f'You typed the numbers {list}')
max = max(list)
print(f'The greatest number is {max} and the position is ', end='')
for k, v in enumerate(list):
    if (v == max):
        print(f'... {k}', end='')
print('')
min = min(list)
print(f'The lower number is {min} and the position is', end='')
for k, v in enumerate(list):
    if (v == min):
        print(f'... {k}', end='')
