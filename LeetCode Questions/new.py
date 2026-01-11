import sys

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# print(type(lst))
# print(type(tup))

print(sys.getsizeof(l))
print(sys.getsizeof(lst))
print(sys.getsizeof(tup))
print(sys.getsizeof(s))