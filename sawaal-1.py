p=10000
r=15
t=3
si = (p*r*t)/100
print(si)
ci= (p*(1+r/100)**t)-p
print(ci)


a='12'
b=2
print(a*b)
print(23-45+20)

print('loss calculation:-')

cost_price = input('4. Enter the cost price: ')
selling_price = input('Enter the selling price: ')  
print("Your loss is: ", float(cost_price) - float(selling_price))

print('5. Profit percentage calculation:-')

cost_price = input('Enter the cost price: ')
profit = input('Enter the profit: ')

print("Your profit percentage is: ", (float(profit) / float(cost_price)) * 100)

print('6. Discount Calculation:-')

marked_price = input('Enter the marked price: ')
selling_price = input('Enter the selling price: ')
print("Your discount is: ", float(marked_price) - float(selling_price))

print('7. percentage increased calculation:-')
original_value = input('Enter the original value: ')
new_value = input('Enter the new value: ')
print("Percentage increase is: ", ((float(new_value) - float(original_value)) / float(original_value)) * 100)

#THE END
