numbers = list()
even = list()
odd = list()
''' 1st way
while True:
    number = int(input('Write a number: '))
    if (number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)

    numbers.append(number)
    if (str(input('Do you want continue ?')) in 'nN'):
        break
'''

while True:
    number = int(input('Write a number: '))
    numbers.append(number)
    if (str(input('Do you want continue ?')) in 'nN'):
        break

for k, v in enumerate(numbers):
    if (v % 2 == 0):
        even.append(v)
    else:
        odd.append(v)
        
print(f'The numbers you have typed are {numbers}')
print(f'The even are {even}')
print(f'The odds are {odd}')