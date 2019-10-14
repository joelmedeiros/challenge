print('=-'*10, 'Arithmetic Progression', '=-'*10)
term = int(input('First term: '))
ratio = int(input('Ratio: '))
last = term + 9 * ratio
for i in range(term, last + ratio, ratio):
    print(i, end= ' -> ')

print('DONE')