
def main():
    print('-' * 30)
    print('Main menu'.center(30))
    print('-' * 30)
    print('1 - List registers')
    print('2 - Register new')
    print('3 - Leave')
    print('-' * 30)

    while True:
        try:
            option = int(input('Option: '))
        except TypeError:
            print('Invalid option')
            continue
        break

    return option
