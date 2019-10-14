from datetime import date
legalAge = 0
notOfLegalAge = 0
actualYear = date.today().year
for i in range(0, 7):
    birthDate = int(input('Write a birth date: '))
    if (actualYear - birthDate < 21):
        notOfLegalAge += 1
    else:
        legalAge += 1

print('{} people are in the legal age and {} are not in the legal age.'.format(legalAge, notOfLegalAge))