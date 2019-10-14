list = list()

while True:
    list.append(int(input('Write a number: ')))
    if (str(input('Do you want continue? [Y/n]')) in 'nN'):
        break

print(f'You have typed {len(list)} elements.')
list.sort(reverse=True)
print(f'The values sorted by desc are: {list}')
print('The value 5 exists in the list' if 5 in list else 'The value 5 not found in the list')
