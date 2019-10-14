from datetime import date
birthYear = int(input('Tell me yor birth year: '))

actualYear = date.today().year
age = actualYear - birthYear
print('The athlete is {} y/o'.format(age))
if (age <= 9):
    category = 'Little'
elif age <= 14:
    category = 'Childlike'
elif age <= 19:
    category = 'Junior'
elif age <= 25:
    category = 'Senior'
else:
    category = 'Master'

print(category)