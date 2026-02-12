# 1. Instance Methods
# • Take self as the first argument.
# • Can access both instance attributes and class attributes.

class laptop:
    storage_type = "SSD"

    def __init__(self, Ram, Storage):
        self.Ram = Ram
        self.Storage = Storage

    def get_info(self):     #Instance Methdos
        print(f"The Laptop has {self.Ram} GB of RAM, {self.Storage} GB of {self.storage_type}")

laptop1 = laptop(16,512)
laptop1.get_info()