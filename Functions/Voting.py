def vote(birthYear):
    from datetime import date
    age = date.today().year - birthYear
    ageString = f'With {age} years old'
    if (16 <= age < 18 or age >= 65):
        return (f'{ageString} the vote is optional')
    elif (age < 16):
        return (f'{ageString} can not vote')
    else:
        return (f'{ageString} the vote is compulsory')

print(vote(int(input('What is your year of birth? '))))