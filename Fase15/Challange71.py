value = int(input('Set the withdraw value R$'))
while True:
    if value >= 50:
        notes50 = value // 50
        value = value % 50
        print(f'A total of {notes50} notes of $50')
    elif value >= 20:
        notes20 = value // 20
        value = value % 20
        print(f'A total of {notes20} notes of $20')
    elif value >= 10:
        notes10 = value // 10
        value = value % 10
        print(f'A total of {notes10} notes of $10')
    elif value >= 1:
        notes1 = value
        value = 0
        print(f'A total of {notes1} notes of $1')
    else:
        break
