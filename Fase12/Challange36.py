houseValue = float(input('What is the price of the house? '))
salary = float(input('What is the salary of the buyer? '))
years = int(input('In how many years he/she will pay? '))

months = years*12
houseValuePerMonth = houseValue/months

maxValue = salary * .3

if (houseValuePerMonth > maxValue):
    print('Loan denied, the monthly price is ${:.2f} and is greater than 30% of {:.2f} (${:.2f})'.format(houseValuePerMonth, salary, maxValue))
else:
    print('Loan Approved')