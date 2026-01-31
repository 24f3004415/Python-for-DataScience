word = "mmmmmooooohhhhhiiiiitttta"
freq_map = {}

for i in range(len(word)):
    freq_map[word[i]] = freq_map.get(word[i], 0) + 1

def nonRepeating():
    for key,value in freq_map.items():
        if freq_map[key] == 1:
            return f"{key}: {value}"
    
    return -1

print(nonRepeating())

