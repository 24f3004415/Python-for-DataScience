# A static method is a method defined inside a class that does not operate on instance or class data. It is used for utility functions related to the class and is defined using the @staticmethod decorator.

class Laptop:
    storage_type = "SSD"

    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    @staticmethod
    def company_policy():
        print("All laptops come with 1 year warranty.")


Laptop.company_policy()



# Yaha:

#   Ye kisi object ka data use nahi kar raha

#   Ye class attribute bhi use nahi kar raha

#   Bas logically Laptop se related info hai

# Isliye static method.