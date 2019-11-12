from money import currency

number = float(input('Write the price: $'))

print(f'The half of {currency.format(number)} is {currency.format(currency.half(number), "US$")}')
print(f'The double of {currency.format(number)} is {currency.format(currency.double(number), "US$")}')
print(f'Increasing 10% of {currency.format(number)} we have {currency.format(currency.increase(number, 10), "US$")}')
print(f'Decreasing 13% of {currency.format(number)} we have {currency.format(currency.decrease(number, 13), "US$")}')
