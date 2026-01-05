lst=[10,20,30,40,50,50,10,20,50,50,50,50,50]
dict = {}
# method-1
for i in range(len(lst)):
    if lst[i] not in dict:
        dict[lst[i]] = 1
    else:
        dict[lst[i]] += 1

print(dict)

# method-2
method_dict = {}
for i in range(len(lst)):
    method_dict[lst[i]] = method_dict.get(lst[i], 0)+1

print(method_dict)