print('=-'*10, 'Arithmetic Progression', '=-'*10)
term = int(input('First term: '))
ratio = int(input('Ratio: '))
count = 1
max = 10
while count < max:
    print('{}'.format(term, count), end= ' -> ' if count < (max -1) else '')
    term += ratio
    count += 1

    if count == max:
        max += int(input('\nHow many terms do you want to show? '))

print('DONE')

print('{} terms were showed.'.format(max))