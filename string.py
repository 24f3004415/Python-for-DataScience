name = "Mohit"
age = 19

print('hello your name is',name,'and your age is',age)

print(f'hello your name is {name} and your age is {age}')

input_name = input('Enter your name:')
input_age = int(input('Enter your age: '))

print(f'Your name is {input_name} and your age is {input_age}')

if (input_age>18) :
    print("And you can vote")
else:
    print("And You can't vote")