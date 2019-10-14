sentence = str(input('Write a sentence: ')).replace(' ', '').upper().strip()
newSentence = sentence[::-1]
# for i in range(len(sentence) -1, -1, -1):
#     newSentence += sentence[i]

print('The inverse of {} is {}'.format(sentence, newSentence))
if (newSentence == sentence):
    print('Your sentence is a palindrome')
else:
    print('Your sentence is not a palindrome')