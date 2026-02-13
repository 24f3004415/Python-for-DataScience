from pathlib import Path
import json

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

obj = Bank()

