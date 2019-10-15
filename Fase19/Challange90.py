student = {}

student['name'] = str(input('Name: '))
student['avg'] = float(input('Average: '))
if student['avg'] >= 7:
    student['status'] = 'approved'
elif 5 <= student['avg'] < 7:
    student['status'] = 'recuperation'
else:
    student['status'] = 'disapproved'
print('-=' * 30)
for k, v in student.items():
    print(f'The {k} is {v}')