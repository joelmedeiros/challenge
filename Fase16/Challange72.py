numbers = 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'

n = int(input('Write a number: '))
while n not in range(0,21):
    n = int(input('Try again. Write a number: '))

print(f'You wrote {numbers[n]}')