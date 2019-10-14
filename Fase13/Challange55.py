lower = 0
greater = 0

for i  in range(0, 5):
    weight = float(input('Write the weight: '))

    if (i == 0):
        lower = weight
        greater = weight
        continue

    if (weight < lower):
        lower = weight

    if (weight > greater):
        greater = weight

print('The greater weight is {:.1f} and the lower is {:.1f}.'.format(greater, lower))
