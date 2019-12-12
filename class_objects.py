## Classes & Objects
# to create your own data types >> Student.py
# from file import class
from Student import Student
from Student2 import Student2

# create an actual student >> object
# name, major...
student1 = Student("Pista", "Business", 3.1, False)
student2 = Student2("Joli", "Art", 3.5)

print(student1.name)
print(student2.on_honor_roll())

# you can do objects and classes with anything...
# you can model real world objects
