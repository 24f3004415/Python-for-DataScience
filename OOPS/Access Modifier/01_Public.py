# Python has 3 access levels:
#     1. Public members
#         • Accessible everywhere, written like normal variables.

class Student:
    def init (self, name):
        self.name = name # public variable

s = Student("Mohit")

print(s.name) # Allowed

