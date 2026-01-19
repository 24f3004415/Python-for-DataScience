# from pathlib import Path

# name = input("Enter the name of the file")

# data = input('Enter the data')

# p = Path(name)

# if p.exists():
#     print("Sorry this file already exists")

# else:
#     file = open(p, 'w')
#     file.write(data)

# 'a' is used for appending and 'w' is used for overwriting

# easy way to open file and work with them
 
with open('Mohit.py', 'r') as fs:
    print(fs.read())
