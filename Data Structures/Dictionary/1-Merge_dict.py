d1 = {'a':10,'b':20,'c':30}
d2 = {'d':40,'e':50}

for i in d1:
    if i not in d2:
        d2[i] = d1[i]

print(d2)

for i in d2:
    if i not in d1:
        d1[i] = d2[i]

print(d1)

