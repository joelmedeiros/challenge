from time import sleep


def factorial(start, end, rate):
    if (rate == 0):
        rate = 1

    print('-=' * 30)
    print(f'Counting from {start} to {end} every {rate}')
    rule = start > end
    while True:
        if rule and rate > 0:
            print(start, end=' ')
            start = start - (rate)
        else:
            print(start, end=' ')
            start = start + (rate)

        if rule and start < end or rule == False and start > end:
            print('DONE!')
            break
        sleep(0.5)
    print('-=' * 30)


factorial(1, 10, 1)
factorial(10, 0, 2)
factorial(90, 40, 10)
factorial(20, 10, -1)
factorial(5, -5, 0)

print('It\'s your turn to customize the factorial.')
factorial(
    int(input('Start from: ')),
    int(input('To: ')),
    int(input('Rate: '))
)
