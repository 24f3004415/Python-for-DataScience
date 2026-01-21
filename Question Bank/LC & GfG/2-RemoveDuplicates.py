# Method ---> 1 (Using dict.fromkeys())
# dict.fromkeys() method creates a dictionary with keys from the list, automatically removing duplicates because dictionary keys are unique. The order is preserved where dictionaries maintain insertion order.

a = [1, 2, 2, 3, 4, 4, 5]

b = list(dict.fromkeys(a))
print(b)

# Method ---> 2 (Using a Loop)
# This is a simple method that involves iterating over the list and appending elements to a new list if they are not already present.

a = [1, 2, 2, 3, 4, 4, 5]

b = []

for x in a:
    if x not in b:
        b.append(x)
print(b)