# single level inheritance
# multilevel
# Multiple level inheritance -- 2 parent class and 1 child class


class Animal:
    def __init__(self, name,age,):
        self.name = name
        self.age = age
        self.canWalk = True
        self.__gender = "Male"


    def Show(self):
        print(f"Name of the dog is {self.name} and it's age is {self.age}")

    def Sleep(self):
        print(f"Do cats Sleep? --> {self.canWalk}")

    def gender(self):
        print(f"Do cats Sleep? --> {self.__gender}")



class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def Show2(self):
        print("This is cat class!! Inherited Animal class")
        print(f"{self.name} and {self.age} and breed is {self.breed}")
        print("Hence Proved")



obj = Cat("Shera", 4, "bagadbilla")
obj.Show2()
obj.Show()
obj.gender()
obj.Sleep()