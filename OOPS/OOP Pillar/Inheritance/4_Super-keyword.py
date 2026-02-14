class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)   # calling parent constructor
        self.grade = grade


Insaan = Student("Mohit", 10.0)
print(Insaan.name)
print(Insaan.grade)