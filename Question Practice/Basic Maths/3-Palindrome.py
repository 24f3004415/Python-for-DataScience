
def reverse(x: int) -> int:
    reverse = 0
    int_min = -2**31
    int_max = (2**31)-1
    if x>=0:
        while x>0:
            l_digit = x%10
            reverse = (reverse*10)+l_digit
            x = x//10
        if reverse<int_min or reverse>int_max:
            return 0
        else:
            return reverse
    else:
        x = abs(x)
        while x>0:
            l_digit = x%10
            reverse = (reverse*10)+l_digit
            x = x//10
        reverse = int(reverse)
        if reverse<int_min or reverse>int_max:
            return 0
        else:
            return int(f"-{reverse}")

print(reverse(45))
print(type(reverse(-45)))
