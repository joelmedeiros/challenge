
def count(b,f,r):
    '''
    Make a count and shows in the screen
    :param b: begin the count
    :param f: finish the count
    :param r: counter rate
    :return: counter
    Made by me
    '''
    i = b
    while i <= f:
        print(f'{i}', end='..')
        i += r
    print('Done!')

count(2,10,2)

help(count)