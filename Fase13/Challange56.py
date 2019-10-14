ageSum = 0
OlderName = None
OlderAge = None
WomenLessThan20 = 0
for i in range(0, 4):
    name = str(input('Write the name: '))
    age = int(input('Write the age: '))
    sex = str(input('Write the sex [M]ale|[F]emale: ')).lower()
    ageSum += age

    if (sex == 'm' and (OlderName is None and OlderAge is None or age > OlderAge)):
        OlderName = name
        OlderAge = age

    if (sex == 'f' and age < 20):
        WomenLessThan20 += 1

    print('~-'*20)


print('The medium age of the group is {:.2f}'.format(ageSum/4))
print('{} is the older and he is {} years old'.format(OlderName, OlderAge))
print('There are {} women less than 20 years old.'.format(WomenLessThan20))
