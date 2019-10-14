km = float(input("Tell me how much km: "))
days = int(input("And now, how many days: "))
priceDay = days * 60.00
priceKm = km * .15
print("You have to pay R$ {:.2f} for {} day(s) and {}km".format(priceDay + priceKm, days, km))