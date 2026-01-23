str1 = "hfchfxig475jkgcxteud6576cc#*^$^%$^%"

char = 0
digit = 0
symbols = 0

for i in str1:
    if i.isalpha():
        char += 1

    elif i.isdigit():
        digit += 1

    else:
        symbols += 1

print(char)
print(digit)
print(symbols)