class sample:
    def __init__(self):
        self.a1 = 'This is public'
        self.__a2 = 'This is Private'
        self._a3 = 'This is Protected'

    def show(self):   #Getter
        print(self.a1)
        print(self.__a2)
        print(self._a3)

    def change(self):  #Setter
        self.__a2 = "This is not a private attribute anymore"

obj = sample()
obj.change()
obj.show()