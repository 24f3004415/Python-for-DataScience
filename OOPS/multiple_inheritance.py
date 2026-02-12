class Bank:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"This is Bank Class: {self.name}")

class Account:
    def __init__(self,account_no):
        self.account_no = account_no

    def show2(self):
        print(f"This is account class {self.account_no}")

class Customer(Bank, Account):
    def __init__(self, name, account_no):
        Bank.__init__(self, name)
        Account.__init__(self,account_no)

    def show3(self):
        print("This is customer class")

obj = Customer("Vijay", 1234567890)
obj.show()
obj.show2()
obj.show3()