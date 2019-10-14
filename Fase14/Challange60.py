'''from math import factorial

number = int(input('Write a number: '))

print('The factorial of {} is {}'.format(number, factorial(number)))
'''


number = int(input('Write a number: '))
result = number
n = number

showVar = '{} '.format(number)
for i in range(1, n):
    result *= (n-1)
    showVar += 'x {} '.format(n-1)
    n -= 1

'''
while n > 1:
    result *= (n-1)
    showVar += 'x {} '.format(n-1)
    n -= 1
'''
print('The factorial of {}is {}'.format(showVar, result))

