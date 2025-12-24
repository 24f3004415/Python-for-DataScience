num = int(input("Enter a number: "))
copy = num
reverse = 0
while num>0:
    l_digit = num%10
    reverse = (reverse*10)+l_digit
    num = num//10

if copy == reverse:
    print("It's a palindrome")
else:
    print("Not a palindrome")