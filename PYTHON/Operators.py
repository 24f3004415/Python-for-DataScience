# Operators are used to perform operations on variables and values.

# Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# Division in Python
# Python has two division operators:

# / - Division (returns a float)
# // - Floor division (returns an integer)

# Assignment Operators
# Assignment operators are used to assign values to variables

# Comparison Operators
# Comparison operators are used to compare two values

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Logical Operators
# Logical operators are used to combine conditional statements:

x = 5
y = 3

print(x < y and x < 10)
print(x < y or x < 10)
print(not(x < y and x < 10))

# Identity Operators
# Identity operators are used to compare the memory location of two objects:

x = 5
y = 3

print(x is y)
print(x is not y)

# Membership Operators
# Membership operators are used to check if a value is present in a sequence:

x = 5
y = 3

print(x in y)
print(x not in y)

# Bitwise Operators
# Bitwise operators are used to perform operations on the binary representation of numbers:

x = 5
y = 3

print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x << y)
print(x >> y)

# Precedence
# Precedence is the order in which operators are evaluated:


# The precedence order is described in the table below, starting with the highest precedence at the top:
# ()	Parentheses	
# **	Exponentiation	
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	Multiplication, division, floor division, and modulus	
# +  -	Addition and subtraction	
# <<  >>	Bitwise left and right shifts	
# &	Bitwise AND	
# ^	Bitwise XOR	
# |	Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
# not	Logical NOT	
# and	AND	
# or	OR
