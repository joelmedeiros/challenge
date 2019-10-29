def test():
    global globalvar
    globalvar = 1
    functionVar = 10
    print(f'Inside a function globalvar is {globalvar}')
    print(f'Inside a function functionVar is {functionVar}')

globalvar = 2

print(f'In the main globalvar is {globalvar}')
test()
# print(f'In the main functionvar is {functionVar}')  NameError: name 'functionVar' is not defined

print(f'After test function globalvar is {globalvar}')
