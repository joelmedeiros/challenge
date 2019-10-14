total = moreThan1000 = 0
cheaperProductPrice = cheaperProductName = None

while True:
    name =  str(input('Product name: '))
    value = float(input('Value: R$'))

    total += value
    if (value > 1000):
        moreThan1000 += 1

    if (cheaperProductPrice is None or cheaperProductPrice > value):
        cheaperProductPrice = value
        cheaperProductName = name


    answer = ' '
    while answer not in 'YN':
        answer = str(input('Do you want to continue? [Y/n]')).strip().upper()[0]

    if(answer == 'N'):
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'The total cost is R${total:.2f}')
print(f'There\'s {moreThan1000} products more than R$ 1000')
print(f'The cheaper product is \'{cheaperProductName}\' and its value is R${cheaperProductPrice:.2f}')