def title(message, color = 0):
    length = len(message) + 4
    colors = (
        '\033[m',           #none
        '\033[0;30;41m',    #red
        '\033[0;30;42m',    #green
        '\033[0;30;43m',    #yellow
        '\033[0;30;44m',    #purple
        '\033[0;30;45m',    #pink
        '\033[7;30m',       #white
    )
    print(colors[color], end='')
    print('~' * length)
    print(f'  {message}')
    print('~' * length)
    print(colors[0], end='')


def myHelp(functionName):
    title(f'Accessing manual of {functionName}', 6)
    help(functionName)


while True:
    title('Help system', 1)
    functionName = str(input('Write the library or function name >'))
    if (functionName.upper() == 'DONE'):
        break
    myHelp(functionName)

title('Bye!', 2)