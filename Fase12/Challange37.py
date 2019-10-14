number = int(input('Write a number '))
base = int(input('''Chose an option: \n
1 - binary
2 - octal
3 - hexadecimal
'''))

if base == 1:
    print("The number {0} in binary is {0:b}".format(number))
elif base == 2:
    print("The number {0} in octal is {0:o}".format(number))
elif base ==3:
    print("The number {0} in octal is {0:x}".format(number))
else:
    print('Invalid option')