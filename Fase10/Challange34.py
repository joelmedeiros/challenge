salary = float(input('Write the employee salary: '))
increase = salary * .1 if salary > 1250.00 else salary * .15
print('The salary increase will be {:.2f} and the new salary will be {:.2f}'.format(increase, salary + increase))
