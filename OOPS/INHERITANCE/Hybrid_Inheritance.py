#2 ya 2 se jyada type k inheritance mix ho jaye --> Hybrid Inheritance

class Father:
    def skill(self):
        print("Belt hi belt")

class Mother:
    def skill(self):
        print('De taane')

class Child(Father, Mother):  # Multiple Inheritance
    def skill(self):
        print('Na padhna aur na padhne dena')

class Student(Child):    # Multi-Level Inheritance
    def skill(self):
        print("Hello")