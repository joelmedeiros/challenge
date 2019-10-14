price = float(input("Tell me the product price: "))
priceWithDiscount = price*0.05
print("The product with discount of 5% is R${:.2f}".format(price - priceWithDiscount))