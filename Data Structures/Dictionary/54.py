d1 = {"a":10,"b":20,"c":30}
d2 = {"d":40,"a":50,"c":60}

for i in d2:
    if i not in d1:
        d1[i] = d2[i]
    else:
        d1[i] += d2[i]

print(d1)