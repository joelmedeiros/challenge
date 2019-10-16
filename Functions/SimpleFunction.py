print('-' * 30)
print('Area calculator')
print('-' * 30)

width = float(input('WIDTH (m): '))
length = float(input('LENGTH (m): '))

def AreaCalc(w, l):
    return w * l

area = AreaCalc(width, length)

print(f'The area of {width}x{length} is {area}m')