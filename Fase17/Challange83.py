expression = str(input('Write an expression: '))
# if (expression.count('(') != expression.count(')')):
#     print('Your expression is not ok')
#     exit()

brackets = list()
for letter in expression:
    if letter == '(':
        brackets.append('(')
    elif letter == ')':
        if(len(brackets) > 0):
            brackets.pop()
        else:
            brackets.append(')')
            break

print('Your expression is not ok' if len(brackets) > 0 else 'Your expression is ok')