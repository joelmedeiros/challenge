from datetime import date
year = int(input('Write a year or press 0 to check the actual year: '))
if (year == 0):
    year = date.today().year
print('Leap' if year % 400 == 0 or (year % 4 == 0  and year % 100 != 0) else 'Non-leap')