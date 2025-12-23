l = [10,2,7,6,1,2,4,3,5,6,8]

for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

print(l)