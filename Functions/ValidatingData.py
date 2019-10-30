def readOnlyInt(message):
    number = str(input(message))
    while number.isdigit() == False:
        print('\033[0;31mERROR! Write a valid integer.\033[m')
        number = str(input(message))
    return number


number = readOnlyInt('Write a integer number: ')
print(f'You wrote the integer number {number}')
