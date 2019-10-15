goon = True
people = []
women = []
person = {}
sum = 0
while goon:
    person['name'] = str(input('Name: '))
    while True:
        person['sex'] = str(input('Sex: [M/F]')).upper()[0]
        if (person['sex'] not in 'FM'):
            print('Wrong value, type only [M]ale or [F]emale.')
            continue
        if (person['sex'] in 'F'):
            women.append(person['name'])
        break
    age = int(input('Age: '))
    person['age'] = age
    sum += age
    people.append(person.copy())
    while True:
        cont = str(input('Do you want to continue? [Y/N]').upper()[0])
        if (cont not in 'NY'):
            print('Wrong value, type only [Y]es or [N]o.')
            continue

        goon = cont != 'N'
        break

print(f'The group has {len(people)} people')
avg = sum/len(people)
print(f'The average is {avg}')
print(f'The women are: ', end='')
for k, woman in enumerate(women):
    print(woman, end=' ')
print()
print(f'The list of people above the average is:')
for k, person in enumerate(people):
    if (person['age'] > avg):
        for k, v in person.items():
            print(f'{k} = {v}', end='; ')
        print('')
print('Done.')
