prices = 'Bread Kg', 10.99, \
         'Meat', 24.99, \
         'Pizza', 29.99, \
         'Apple', 6.99

for i in range(0, len(prices)):
    if (i % 2 == 0):
        print(f'{prices[i]:.<30}', end='$US ')
    else:
        print(f'{prices[i]:>5}')