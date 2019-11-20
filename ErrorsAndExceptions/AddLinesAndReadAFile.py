from utility import file, menu

option = menu.main()
while option != 3:
    if (option == 1):
        file.read()
        option = menu.main()
    elif (option == 2):
        file.add()
        option = menu.main()
print('Bye bye!')