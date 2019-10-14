
sex = str(input('Write a sext [m/f]: ')).lower().strip()
while sex not in 'fm':
    sex = str(input('{} is not a valid sex. Write a sext [m/f]: '.format(sex))).lower().strip()