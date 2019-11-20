intValid = False
intNumber = False
while not intValid:
    try:
        intNumber = int(input('Write a integer number: '))
    except KeyboardInterrupt:
        print('\033[0;31mNo number entered. \033[m')
        intValid = True
    except:
        print(f'\033[0;31mPlease, type a valid number. \033[m')
    else:
        intValid = True

floatValid = False
floatNumber = 0
while not floatValid:
    try:
        floatNumber = float(input('Write a float number: '))
    except KeyboardInterrupt:
        print('\033[0;31mNo number entered. \033[m')
        floatValid = True
    except:
        print(f'\033[0;31mPlease, type a valid number. \033[m')
    else:
        floatValid = True

print(f'The integer value entered was {intNumber} and the float value was {floatNumber}')