def del_char(word,character):
    if len(character) == 1:
        result = []
        for letter in word:
            if letter != character:
                result.append(letter)
                
        return ''.join(result)
        
    else:
        return word
s = input()
c = input()
print(del_char(s,c))