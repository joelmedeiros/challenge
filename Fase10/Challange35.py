r1 = float(input('Write the 1st straight: '))
r2 = float(input('Write the 2nd straight: '))
r3 = float(input('Write the 3th straight: '))
sides = 0
if (r1 + r2 > r3):
    sides += 1
if (r1 + r3 > r2):
    sides += 1
if (r2 + r3 > r1):
    sides += 1
print('You can' if sides > 2 else 'You can not', 'form a triangle')

