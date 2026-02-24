from pathlib import Path
import json
import random
import string

class Bank:
    database = r"C:\Users\HP\Downloads\python shery\OOPS\Project\BANKING\data.json"
    data = []

    try:
        if Path(database).exists():
            print('Database Exist!!!')
            with open(database, 'r') as fs:
                data = json.load(fs)

        else:
            print("No such file exists")

    except Exception as err:
        print(f"Error occurred: {err}")

    @classmethod
    def __update(cls):
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(cls.data))

    #Generate Random Account Number
    @staticmethod
    def __generateAccountNo():
        randomNumbers = random.choices(string.digits, k=4)
        randomAlphabets = random.choices(string.ascii_letters, k=4)
        id = randomNumbers + randomAlphabets
        random.shuffle(id)
        return ''.join(id)

    # create user
    def createAccount(self):
        info = {
            'name' : input("Enter your name: "),
            'age' : int(input("Enter your age: ")),
            'email' : input("ENter your email: "),
            'pin' : int(input("Enter your pin: ")),
            'phone No.' : int(input("ENter your phone No.")),
            'account No.' : Bank.__generateAccountNo(),
            'balance' : 0
        }

        if info['age'] > 18 and len(str(info['pin'])) == 4 and len(str(info['phone No.'])) == 10:
            Bank.data.append(info)
            Bank.__update()
            print('Data added in a list.')

        else:
            print("Account cannot be created due to Wrong Credentials !!!")


    # function to deposit money
    def depositMoney(self):
        AccountNumber = input("Enter your Account Number: ")
        PinNumber = int(input("Enter your pin: "))

        user_data = [i for i in Bank.data if i['account No.'] == AccountNumber and i['pin'] == PinNumber]

        if user_data == False:
            print("User does not exist!!!")

        else:
            Money = int(input('Enter the amount you want to deposit: '))
            if Money <= 0:
                print("Invalid Input :( ")

            elif Money > 10_000:
                print('deposit limit exceeded!!!')

            else:
                user_data[0]['balance'] += Money
                Bank.__update()
                print(f"Rs. {Money} has been credited successfully!!")
                print("THANK YOU FOR BANKING WITH US :) ")


    # function to withdraw money
    def withdrawMoney(self):
        AccountNumber = input("Enter your Account Number: ")
        PinNumber = int(input("Enter your pin: "))

        user_data = [i for i in Bank.data if i['account No.'] == AccountNumber and i['pin'] == PinNumber]

        if user_data == False:
            print("User does not exist!!!")

        else:
            Money = int(input('Enter the amount you want to withdraw: '))

            if Money <= 0:
                print("Invalid Input :( ")

            elif Money > 10_000:
                print('withdraw limit exceeded!!!')

            else:
                if user_data[0]['balance'] < Money:
                    print("You don't have sufficient balance in your account")
                else:
                    user_data[0]['balance'] -= Money
                    Bank.__update()
                    print(f"Rs. {Money} has been withdrawn successfully!!")
                    print("THANK YOU FOR BANKING WITH US :) ")


    # function to see customer details
    def details(self):
        AccountNumber = input("Enter your Account Number: ")
        PinNumber = int(input("Enter your pin: "))

        user_data = [i for i in Bank.data if i['account No.'] == AccountNumber and i['pin'] == PinNumber]

        if user_data == False:
            print("User does not exist!!!")

        else:
            print('------------------------------')
            print('Your details are as follows: ')
            for i in user_data[0]:
                print(f"{i} : {user_data[0][i]}")
                
        print('THANK YOU FOR BANKING WITH US!!')
        print("Have a good day!!!")


    # function to delete customer account
    def delete_account(self):
        print('-------------------------------------------')
        AccountNumber = input("Enter your Account Number: ")
        PinNumber = int(input("Enter your pin: "))

        user_data = [i for i in Bank.data if i['account No.'] == AccountNumber and i['pin'] == PinNumber]

        if user_data == False:
            print("User does not exist!!!")

        else:
            print('-------------------------------------------')
            print('Are you sure you want to delete your account?')
            print('Press 1 to continue')
            print('Press 2 to revert back.')
            print('-------------------------------------------')
            user_delete_choice = int(input('Enter your choice: '))

            if user_delete_choice == 1:
                idx = Bank.data.index(user_data[0])
                Bank.data.pop(idx)
                Bank.__update()
                print('-------------------------------------------')
                print('Account deleted Successfully!!')
                print('-------------------------------------------')
                print("Thank you for banking with us...")

            elif user_delete_choice == 2:
                print('-------------------------------------------')
                print("Operation Terminated")

            elif user_delete_choice != 1 and user_delete_choice != 2:
                print('-------------------------------------------')
                print("Invalid Input.")            

    def __update_account(self):

        print('-------------------------------------------')
        AccountNumber = input("Enter your Account Number: ")
        PinNumber = int(input("Enter your pin: "))

        user_data = [i for i in Bank.data if i['account No.'] == AccountNumber and i['pin'] == PinNumber]
        if user_data == False:
            print("User does not exist!!!")

        else:
            print('You cannot change your account number and balance.')
            print('Enter your new details if you want to __update or Enter key otherwise.')

            new_data = {
            'name' : input("Enter your new name: "),
            'age' : int(input("Enter your new age: ")),
            'email' : input("ENter your new email: "),
            'pin' : int(input("Enter your new pin: ")),
            'phone No.' : int(input("ENter your new phone No.")),
        }

        if new_data['name'] == "":
            new_data['name'] = user_data[0]['name']

        if new_data['age'] == "":
            new_data['age'] = user_data[0]['age']

        if new_data['email'] == "":
            new_data['email'] = user_data[0]['email']

        if new_data['pin'] == "":
            new_data['pin'] = user_data[0]['pin']
        else:
            new_data['pin'] = int(new_data['pin'])

        if new_data['phone No.'] == "":
            new_data['phone No.'] = user_data[0]['phone No.']
        else:
            new_data['phone No.'] = int(new_data['phone No.'])


        new_data['account No.'] = user_data[0]['account No.']
        new_data['balance'] = user_data[0]['balance']

        user_data[0].__update(new_data)
        Bank.__update()

obj = Bank()

print("Enter 1 to create account.")
print("Enter 2 to deposit money in your account.")
print("Enter 3 to withdraw money.")
print("Enter 4 to check your account details.")
print("Enter 5 to __update your account details.")
print("Enter 6 to delete your account.")

user_input = int(input("Enter your response to proceed: "))

if user_input == 1:
    obj.createAccount()

if user_input == 2:
    obj.depositMoney()

if user_input == 3:
    obj.withdrawMoney()

if user_input == 4:
    obj.details()

if user_input == 5:
    obj.__update_account()

if user_input == 6:
    obj.delete_account()
