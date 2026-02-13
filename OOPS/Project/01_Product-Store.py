class Product:
    count = 0

    def __init__(self, name, price):
        self.Name = name
        self.Price = price
        Product.count += 1

    # Instance Method
    def get_info(self):
        print(f"The Price of the {self.Name} is ₹ {self.Price}.")

    @classmethod
    def get_count(cls):
        print(f"The totoal count of the product is {cls.count}")

    @staticmethod
    def calculate_discount(price, discount_percent):
        return f"After Discount ₹ {(price - (price * discount_percent / 100))}"


p1 = Product("Laptop", 1_00_000)
p2 = Product("Mobile", 15_000)

p1.get_info()
print(Product.calculate_discount(p1.Price, 10))


    
