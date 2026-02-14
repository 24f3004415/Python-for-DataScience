class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):   # overriding
        print("Dog barks")

class Cat(Animal):
    def sound(self):   # overriding
        print("Cat meows")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
