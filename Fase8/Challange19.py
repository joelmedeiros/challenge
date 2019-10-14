from random import choice
students = []
students.append(input("Tell me a student's name: "))
students.append(input("Tell me another: "))
students.append(input("Another: "))
students.append(input("the last one: "))
print("The student was chosen {}".format(choice(students)))