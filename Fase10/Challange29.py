speed = float(input('What is the car speed? '))

if speed > 80:
    fine = (speed-80)*7
    print('You were fined {:.2f}' .format(fine))