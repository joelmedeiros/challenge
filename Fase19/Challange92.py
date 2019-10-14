from datetime import date

data = {}
thisYear =  date.today().year
data['name'] = str(input('Name: '))
birthDate = int(input('Birth date: '))
data['age'] =  thisYear - birthDate
data['CTPS'] = int(input('CTPS: '))

if (data['CTPS'] != 0) :
    data['hiring'] = int(input('Hiring year: '))
    data['salary'] = float(input('Salary: '))
    data['retirement'] = data['age'] + (35 - (thisYear - data['hiring']))

print('~=' * 30)

for k, v in data.items():
    print(f'The {k} has the value {v}')