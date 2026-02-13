# 3. Private members
#   • Indicated by a double underscore __
#   • Python does name mangling: the variable name becomes _ClassName variable.
#   • Cannot be accessed directly from outside.

class Bank:
    def __init__(self, balance):
        self.__balance = balance # private variable

    # GETTER
    def get_balance(self):
        return f"Current balance of an account is Rs. {self.__balance}"

    # SETTER
    def set_balance(self, new_balance):
        print(f"Old balance of account was Rs. {self.__balance}")
        self.__balance = new_balance
        return f"Update balance is Rs. {self.__balance}."


b = Bank(5000)
#print(b.__balance) # ERROR: attribute not accessible

print(b._Bank__balance) # Allowed (name-mangled form)
print(b.get_balance())
print(b.set_balance(10_000))