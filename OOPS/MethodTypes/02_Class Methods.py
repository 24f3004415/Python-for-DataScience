# 2. Class Methods
#     • Use @classmethod decorator.
#     • Take cls (class) as first argument.
#     • Used to work with class-level data.


class Laptop:
    storage_type = "SSD"   # Class Attribute

    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    @classmethod
    def change_storage_type(cls, new_type):
        cls.storage_type = new_type


# Yaha:
# cls → Laptop class ko refer karega
# storage_type change ho jayega sab objects ke liye

# Maan lo:
# Laptop.storage_type = "SSD"

# Agar tum class method se change karte ho:
# Laptop.storage_type = "HDD"

# Toh jitne bhi objects hain:
# l1 = Laptop(8, 512)
# l2 = Laptop(16, 1024)

# Dono ka storage_type ho jayega "HDD"
# Kyuki ye class attribute hai.



# 🔴 3️⃣ Difference Crystal Clear
# | Feature             | Instance Method             | Class Method          |
# | ------------------- | --------------------------- | --------------------- |
# | First Parameter     | `self`                      | `cls`                 |
# | Access              | Instance + Class attributes | Only Class attributes |
# | Call kaise hota hai | `obj.method()`              | `Class.method()`      |
