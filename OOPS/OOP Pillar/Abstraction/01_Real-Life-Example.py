from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Child Class 1
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Processing credit card payment of ₹{amount}")
        print("Payment Successful via Credit Card")


# Child Class 2
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Processing UPI payment of ₹{amount}")
        print("Payment Successful via UPI")


# Child Class 3
class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Processing PayPal payment of ₹{amount}")
        print("Payment Successful via PayPal")


# Using abstraction
def process_payment(payment_method, amount):
    payment_method.pay(amount)


# Driver Code
cc = CreditCardPayment()
upi = UPIPayment()
ppp = PayPalPayment()
process_payment(cc, 5000)
print("-----")
process_payment(upi, 2500)
print("-----")
process_payment(ppp, 50)
