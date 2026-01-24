a = 'Abba'
b = 'abab'

if len(a) != len(b):
    print('Not an Anagram')

elif sorted(a) == sorted(b):
    print('its an Anagram')

else:
    print('Not an anagram')

print(sorted(a))