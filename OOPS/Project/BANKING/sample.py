database = [
    {
        "name": "Mohit",
        "age": 19,
        "email": "mohit@gmail.com",
        "pin": 2006,
        "phone No.": 9304495153,
        "account No.": "4d8rI60l",
        "balance": 0
    },
    {
        "name": "Mohit",
        "age": 19,
        "email": "mohit@gmail.com",
        "pin": 2007,
        "phone No.": 9304495153,
        "account No.": "5d8rI60l",
        "balance": 0
    },
    {
        "name": "Mohit",
        "age": 19,
        "email": "mohit@gmail.com",
        "pin": 2006,
        "phone No.": 9304495153,
        "account No.": "4d8rI60l",
        "balance": 0
    }
]

accountno = input('Enetr your account no ')
pin = int(input("Enetr your pin "))

user_data = [i for i in database if i['account No.'] == accountno and i['pin'] == pin]
print("Your Credintials are:")
print(user_data)

if user_data == False:
    print("No such User exist!!")

else:
    balance = int(input('Enter the amount you want to deposit: '))
    user_data[0]['balance'] += balance
    print(user_data)
