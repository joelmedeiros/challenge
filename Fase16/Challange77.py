words = 'learn', 'warning', 'danger', 'leader', 'tech', 'team'

for i in range(0, len(words)):
    print(f'In the word {words[i].upper()} has these', end=' ')
    for letter in words[i]:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
    print('vowels')