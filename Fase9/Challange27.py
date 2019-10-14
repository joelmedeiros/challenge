fullname = str(input('Write your full name: \n')).strip()
names = fullname.split()

print('First name: {}'.format(names[0]))
print('Last name: {}'.format(names[len(names) -1]))