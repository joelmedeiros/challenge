n1 = int(input('Write a number: '))
n2 = int(input('Write another number: '))

if (n1 > n2) :
    print ('{} is greater than {}'.format(n1, n2))
elif n2 > n1:
    print ('{} is greater than {}'.format(n2, n1))
else:
    print('Both numbers are equal')