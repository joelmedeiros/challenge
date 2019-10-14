height = float(input("Tell me the wall height: "))
width = float(input("Tell me the wall width: "))
area = height * width
paint = area/2
print("The wall dimension is {:.3f}m2 and you need {} liters to paint it".format(area, paint))