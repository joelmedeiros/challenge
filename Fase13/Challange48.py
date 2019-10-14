sum = 0
numbers = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        sum += i
        numbers += 1

print('The sum is {} between {} numbers'.format(sum, numbers))