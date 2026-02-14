class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def make_sound(animal):
    animal.speak()


d = Dog()
c = Cat()

make_sound(d)
make_sound(c)
