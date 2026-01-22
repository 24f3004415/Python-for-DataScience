# BY USING LIST COMPREHENSION
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [x for x in a if x % 2 == 0]
odd = [x for x in a if x % 2 != 0]

print(even)
print(odd)


# BY USING HIGHER ORDER FUNCTION

eve = list(filter(lambda x: x % 2 == 0, a))
oddd = list(filter(lambda x: x % 2 != 0, a))

print(eve)
print(oddd)