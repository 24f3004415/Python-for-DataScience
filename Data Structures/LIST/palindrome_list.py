lst = [2,3,15,15,3]
rev_list = []

for i in range(len(lst)-1, -1, -1):
    rev_list.append(lst[i])

if rev_list == lst:
    print('The list is Pallindromic')
else:
    print('Not a Pallindromic')