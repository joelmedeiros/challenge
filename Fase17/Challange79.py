goon = True
numbers = list()
while goon:
    number = int(input('Write a number: '))
    if(numbers.count(number) != 0):
        print('Value already exists!')
    else:
        numbers.append(number)

    goon = str(input('Do you want to continue? [Y/n]')) in 'Yy'

numbers.sort()
print(f'You typed the values {numbers}')