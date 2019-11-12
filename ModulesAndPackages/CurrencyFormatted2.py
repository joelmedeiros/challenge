from money import currency

number = float(input('Write the price: $'))

print(f'The half of {number} is {currency.half(number, True)}')
print(f'The double of {number} is {currency.double(number, True)}')
print(f'Increasing 10% of {number} we have {currency.increase(number, 10, True)}')
print(f'Decreasing 13% of {number} we have {currency.decrease(number, 13, True)}')
