from random import shuffle
students = []
students.append(input("Tell me a student's name: "))
students.append(input("Tell me another: "))
students.append(input("Another: "))
students.append(input("the last one: "))

shuffle(students)
print("The order is: \n", students)