students = []
while True:
    name = str(input('Name: '))
    n1 = float(input('Grade 1: '))
    n2 = float(input('Grade 2: '))
    students.append([name, [n1, n2]])

    if(str(input('Continue? [Y/n]')) in 'nN'):
        break

print(f'{"Num":<5}{"Name":<10}{"Average":>8}')
for number, student in enumerate(students):
    avg = sum(student[1])/2
    print(f'{number:<5}{student[0]:<10}{avg:>8}')

while True:
    index = int(input('Show what student grade? type 999 to stop '))
    if (index == 999):
        break
    if(index > len(students)):
        print('Student not found, try again')
        continue

    print(f'The grades of {students[index][0]} are {students[index][1]}')

print('Bye bye!')