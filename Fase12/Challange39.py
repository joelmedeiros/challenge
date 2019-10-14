from datetime import date
birthYear = int(input('Write your birth year: '))
age = date.today().year - birthYear

if age == 18:
    print('You have to go to military enlistment')
elif age < 18:
    yearsLeft = 18 - age
    print('In {} year(s) you will have to go military enlistment'.format(yearsLeft))
else:
    yearsPast = age - 18
    print('Your time to go to military enlistment is over. You have passed {} year(s)'.format(yearsPast))