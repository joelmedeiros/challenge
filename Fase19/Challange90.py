student = {}

student['name'] = str(input('Name: '))
student['avg'] = float(input('Average: '))

print(f'The name is {student["name"]}')
print(f'The average is {student["avg"]}')
print(f'The student is approved' if student["avg"] >= 7 else 'The student is disapproved')