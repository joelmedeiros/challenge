def read(message):
    '''
    :todo Need to catch exceptions for an input with numbers and letters ex U$10
    :param message:
    :return:
    '''
    valid = False
    while not valid:
        number = str(input(message)).replace(',', '.').strip()
        valid = not number.isalpha() and number != ''
        if (not valid):
            print(f'\033[0;31mError "{number}" is an invalid number\033[m')

    return float(number)