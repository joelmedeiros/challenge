n1 = int(input('Write 1st number: '))
n2 = int(input('Write 2nd number: '))
n3 = int(input('Write 3th number: '))
higher = None
middle = None
lowest = None
if (n1 > n2):
    if (n1 > n3):
        higher = n1
        lowest = n2 if (n3 > n2 ) else n3
    else:
        lowest = n2
        higher = n3
else:
    if (n2 > n3):
        higher = n2
        lowest = n1 if (n3 > n1) else n3
    else:
        higher = n3
        lowest = n1


print('The higher is {} and the lowest is {}'.format(higher, lowest))