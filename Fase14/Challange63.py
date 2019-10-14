sequence = int(input('How many numbers of Fibonatti sequence do you want to see? '))
first = 0
second = 1
count = 3
print('{} -> {}'.format(first, second), end='')
while count <= sequence:
    third = first + second
    first = second
    second = third
    print(' -> {}'.format(third), end='')
    count += 1
print(' -> DONE')
