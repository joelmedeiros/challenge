weight = float(input('Tell me your weight: '))
height = float(input('Tell me your height: '))

bmi = weight / (height ** 2)
print ('Your BMI is {:.1f} and you are in the scale of ...'.format(bmi))
if (bmi < 18.5):
    print('Under weight')
elif (bmi >= 18.5 and bmi < 25):
    print('Ideal weight')
elif bmi >= 25 and bmi < 30:
    print('Overweight')
elif bmi >= 30 and bmi < 40:
    print('Obesity')
else:
    print('Morbid obesity')

