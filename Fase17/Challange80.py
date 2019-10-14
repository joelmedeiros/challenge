numbers = list()
for n in range(0, 5):
    number = int(input(f'Write a number: '))

    if (len(numbers) == 0 or number > numbers[-1]):
        print(f'Will be inserted in the end of the list')
        numbers.append(number)
        continue

    i = 0
    while True:
        if (number <= numbers[i]):
            print(f'Will be inserted in the position {i}')
            numbers.insert(i, number)
            break

        # if (len(numbers) == i + 1):
        #     print(f'Will be inserted in the end of the list')
        #     numbers.append(number)
        #     break
        i += 1

print(f'The values typed were {numbers}')

# 5 2 3 9 1
# 2 3 1 8 5