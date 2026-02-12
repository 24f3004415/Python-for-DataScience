# 1. Instance Methods
# • Take self as the first argument.
# • Can access both instance attributes and class attributes.


class Laptop:
    storage_type = "SSD"   # ---> Storage_type is Class Attribute.

    def __init__(self, Ram, Storage):    #---> Self.Ram & Self.Storage are Instance Attributes
        self.Ram = Ram
        self.Storage = Storage

    def get_info(self):     # ---> get_info is Instance Method because it is taking self as 1st argument.
        print(f"The Laptop has {self.Ram} GB of RAM, {self.Storage} GB of {self.storage_type}")


laptop1 = Laptop(16,512)
laptop1.get_info()