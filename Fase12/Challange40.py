n1 = float(input('First student\'s note: '))
n2 = float(input('Second student\'s note: '))

media = (n1 + n2)/2

if media < 5:
    print('You\'re disapproved')
elif 7 > media >= 5:
    print('You\'re in recovery')
else:
    print('You\'re approved')

print('Your final note is {:.1f}'.format(media))