input = int(input('Write a number between 0 and 9999: \n'))

print('Unit:', input//1 % 10)
print('Ten:', input//10 %10)
print('Hundred:', input//100 % 10)
print('Thousand:', input//1000 % 10)