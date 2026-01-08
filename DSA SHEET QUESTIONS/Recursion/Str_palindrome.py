# https://www.geeksforgeeks.org/problems/palindrome-string0817/1
word = input("Enter to a word to check whether it's a palindrome or not: ")
l_pointer = 0
r_pointer = len(word)-1
is_palindrome = True

while l_pointer<r_pointer:
    if word[l_pointer] != word[r_pointer]:
        is_palindrome = False
        break

    l_pointer += 1
    r_pointer -= 1

if is_palindrome:
    print("yes! It's a palindrome.")
else:
    print("No! It's not a palindrome.")

# Recursion method
def isPalindrome(self, s):
    return self.check(s, 0, len(s) - 1)
    
def check(self, s, l, r):
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return self.check(s, l + 1, r - 1)

