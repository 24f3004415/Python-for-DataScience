class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute (Encapsulation)

    # Getter method to safely access data
    def get_balance(self):
        return f"Current Balance: Rs. {self.__balance}"

    # Setter method to safely modify data with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: Rs. {amount}")
        else:
            print("Invalid deposit amount!")

# Usage
account = BankAccount(1000)

# 1. Accessing via public methods (Correct Way)
print(account.get_balance())
account.deposit(500)

# 2. Trying to access directly (Will cause an error)
# print(account.__balance)  # AttributeError
