sentence = str(input('Write a sentence: \n')).strip().lower()
firstPosition = sentence.index('a') + 1
lastPosition = sentence.rindex('a') + 1

print('{} occurrences found of letter "A"'.format(sentence.count('a')))
print('The letter "A" was firstly found in the position {}'.format(firstPosition))
print('The last position that letter "A" was found is in {}'.format(lastPosition))