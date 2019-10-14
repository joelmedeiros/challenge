distance = float(input('Tell me the distance of your trip: '))
price = distance * .5 if distance <= 200 else distance * .45
print('The total of yor trip will cost ${:.2f}'.format(price))