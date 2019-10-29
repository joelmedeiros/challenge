def readOnlyInt(message):
    number = str(input(message))
    while number.isdigit() == False:
        print('ERROR! Write a valid integer.')
        number = str(input(message))

    return number


number = readOnlyInt('Write a integer number: ')
print(f'You wrote the integer number {number}')
