price = float(input('Product price: '))
paymentMethod = int(input('''What is the payment method? 
1 - In cash (10% discount)
2 - To the sigh on the card (5% discount)
3 - In installment 2x
4 - In installment more than 3x with 20% interest bearing card \n'''))

if (paymentMethod == 1):
    print('You\'ll pay {:.2f} for the product'.format(price - (price * 0.1)))
elif (paymentMethod == 2):
    print('You\'ll pay {:.2f} for the product'.format(price - (price * 0.05)))
elif (paymentMethod == 3):
    print('You\'ll pay {:.2f} for the product'.format(price))
else:
    print('You\'ll pay {:.2f} for the product'.format(price + (price * 0.2)))