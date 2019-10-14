moreThan18yo = men = womenLessThan20yo = 0

while True:
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Write a sex [M/F]:')).strip().upper()[0]

    age = int(input('Write the age: '))

    if (age > 18):
        moreThan18yo +=1

    if (sex == 'M'):
        men += 1
    elif (age < 20):
        womenLessThan20yo += 1

    answer = ' '
    while answer not in 'YN':
        answer = str(input('Do you want to continue? [Y/N]')).strip().upper()[0]

    if(answer == 'N'):
        break

print(f'''There\'s {moreThan18yo} people more than 18 y/o
There\'s {men} men
There\'s {womenLessThan20yo} women less than 20 y/o''')