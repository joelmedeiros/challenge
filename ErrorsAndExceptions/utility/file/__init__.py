def read():
    try:
        f = open('example.txt', 'r+')
        print('-' * 30)
        print('Records'.center(30))
        print('-' * 30)
        for line in f:
            print(line)
        f.close()
    except:
        print('There are no lines to read')


def add():
    name = str(input('Name: '))
    while True:
        try:
            age = int(input('Age: '))
        except KeyboardInterrupt:
            print('The user did not want to finish the registration.')
            break
        except:
            print('Invalid number, please try again')
        else:
            break

    f = open('example.txt', 'a')
    f.write(f'{name:<20}{age}\n')
    f.close()
    print(f'The {name} was added successfully')
