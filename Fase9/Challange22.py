input = str(input("Write your full name:")).strip()

print('Full name in uppercase ', input.upper())
print('Full name in lowercase ', input.lower())
print('Length of chars without space ', len(input.replace(" ", "")))
print('Length of chars of first name ', len(input.split()[0]))