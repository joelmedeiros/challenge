people = []
heaviest = []
lighter = []
heaviestWeight = lighterWeight = 0
goon = True
while goon:
    name = str(input('Name: '))
    weight = int(input('Weight: '))
    person = [name, weight]

    if (weight == heaviestWeight):
        heaviest.append(name)

    if (weight > heaviestWeight or heaviestWeight == 0):
        heaviestWeight = weight
        heaviest.clear()
        heaviest.append(name)

    if (weight == lighterWeight):
        lighter.append(name)

    if (weight < lighterWeight or lighterWeight == 0):
        lighterWeight = weight
        lighter.clear()
        lighter.append(name)

    people.append(person[:])
    person.clear()

    goon = str(input('Do you want to continue? [Y/n]')) not in 'nN'

print(f'You have registered {len(people)} people')
print(f'The heaviest weight was {heaviestWeight} kg. Weight of {heaviest}')
print(f'The lighter weight was {lighterWeight} kg. Weight of {lighter}')