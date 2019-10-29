def factorial(number, show=False):
    '''
    Calc the number's facorial
    :param number: number to calc
    :param show: (optional) Show the process
    :return:  The factorial value of the number
    '''
    result = 1
    printString = []
    for i in range(number, 0, -1):
        result *= i
        printString.append(i)

    if (show):
        print(' x '.join(str(x) for x in printString), end='')
        print(f' = {result}')
    else:
        return result


#show the process
factorial(5, show=True)
#print only results
print(factorial(5))
#show docs
help(factorial)
