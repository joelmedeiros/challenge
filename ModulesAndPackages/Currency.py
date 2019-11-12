from money import currency

number = float(input('Write the price: $'))

print(f'The half of {number} is {currency.half(number)}')
print(f'The double of {number} is {currency.double(number)}')
print(f'Increasing 10% of {number} we have {currency.increase(number, 10)}')
print(f'Decreasing 13% of {number} we have {currency.decrease(number, 13)}')
