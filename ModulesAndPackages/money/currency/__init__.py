def half(number, formatted=False):
    result = number / 2
    if (formatted):
        return format(result)
    return result


def double(number, formatted=False):
    result = number * 2
    if (formatted):
        return format(result)
    return result


def percent(number, percentage):
    return (percentage / 100) * number


def increase(number, increment, formatted=False):
    result = number + percent(number, increment)
    if (formatted):
        return format(result)
    return result


def decrease(number, decrement, formatted=False):
    result = number - percent(number, decrement)
    if (formatted):
        return format(result)
    return result


def format(number, currency='R$'):
    return f'{currency} {number:>.2f}'.replace(".", ",")


def summary(number, increment, decrement, formatted=True):
    print('-' * 30)
    print('Summary'.center(30))
    print('-' * 30)
    print(f'Price analysed: \t{format(number):>1}')
    print(f'Half: \t\t\t\t\t\t{half(number, formatted)}')
    print(f'Double: \t\t\t\t\t{double(number, formatted)}')
    print(f'{increment}% increment: \t\t{increase(number, increment, formatted)}')
    print(f'{decrement}% decrement: \t\t{decrease(number, decrement, formatted)}')
    print('-' * 30)
