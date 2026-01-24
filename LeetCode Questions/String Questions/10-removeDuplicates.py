a = 'abccdeeffgghhiijjk'
s = ''
dic = {}

# for i in a:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1 

# for i in dic:
#     if dic[i] == 1:
#         s += i

# print(dic,s)

for i in a:
    dic[i] = dic.get(i, 0) + 1

print(dic)

