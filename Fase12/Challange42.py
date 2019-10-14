r1 = float(input('Write the 1st straight: '))
r2 = float(input('Write the 2nd straight: '))
r3 = float(input('Write the 3th straight: '))

if (r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1):
    print('You can form a triangle', end=' ')
    equalSides = 0
    if (r1 == r2):
        equalSides += 1
    if (r1 == r3):
        equalSides += 1
    if (r2 == r3):
        equalSides += 1

    if (r1 == r2 == r3):
        print('Equilateral')
    elif (r1 != r2 != r3 != r1):
        print('Scalene')
    else:
        print('Isosceles')

else:
    print('You can not form a triangle')
