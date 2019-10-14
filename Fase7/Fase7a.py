n1 = int(input('Write a number: '))
n2 = int(input('Write another: '))
sum = n1+n2
sub = n1-n2
mult = n1*n2
div = n1/n2
div2 = n1//n2
pow = n1**n2

print("The sum of {} and {} is {}".format(n1, n2, sum), end= '\n')
print("The sub of {} and {} is {}".format(n1, n2, sub), end= '\n')
print("The multi of {} and {} is {}".format(n1, n2, mult), end= '\n')
print("The division of {} and {} is {}".format(n1, n2, div), end= '\n')
print("The integer division of {} and {} is {}".format(n1, n2, div2), end= '\n')
print("The power of {} and {} is {}".format(n1, n2, pow), end= '\n Done.')