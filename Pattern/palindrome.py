def palindrome(n):
    rev = 0
    copy = n
    while n> 0:
        rev = rev*10 + n%10
        n = n//10
    if copy == rev:
        print("It's a palindrome")
    else:
        print("Not a palindrome")   

palindrome(121)
palindrome(1221)
palindrome(12221)
palindrome(122221)
palindrome(1222221)
palindrome(12222221)