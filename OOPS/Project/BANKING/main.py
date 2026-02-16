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
    def update(cls):
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(cls.data))

    #Generate Random Account Number
    @staticmethod
    def generateAccountNo():
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
            'account No.' : Bank.generateAccountNo(),
            'balance' : 0
        }

        if info['age'] > 18 and len(str(info['pin'])) == 4 and len(str(info['phone No.'])) == 10:
            Bank.data.append(info)
            Bank.update()
            print('Data added in a list.')

        else:
            print("Account cannot be created due to Wrong Credentials !!!")
            

obj = Bank()
obj.createAccount()

