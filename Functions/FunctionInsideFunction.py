def write(message):
    def dashed(len):
        print('-' * len)


    message = (' ' * 5) + message + (' ' * 5)
    dashed(len(message))
    print(message)
    dashed(len(message))


write('First message')
write('lorem ipsum dolor sit amet consectetur adipiscing elit')
write('Short msg')