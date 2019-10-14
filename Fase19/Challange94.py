goon = True
people = []
women = []
person = {}
sum = 0
while goon:
    person['name'] = str(input('Name: '))
    person['sex'] = str(input('Sex: [m/f]'))
    if (person['sex'] in 'fF'):
        women.append(person['name'])
    age = int(input('Age: '))
    person['age'] = age
    sum += age
    people.append(person.copy())
    goon = str(input('Do you want to continue? [y/N]')) not in 'nN'

print(f'The group has {len(people)} people')
avg = sum/len(people)
print(f'The average is {avg}')
print(f'The women are: {women}')

print(f'The list of people above the average is:')
for k, person in enumerate(people):
    if (person['age'] > avg):
        for k, v in person.items():
            print(f'{k} = {v}', end='; ')
        print('')

