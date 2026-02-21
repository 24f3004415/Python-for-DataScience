def sumsquare(L):
    sum_of_odd = 0
    sum_of_even = 0
    for num in L:
        if num % 2 == 0:
            sum_of_even += (num)**2
        else:
            sum_of_odd += (num)**2
            
    return [sum_of_odd, sum_of_even]
    
L = eval(input())
print(sumsquare(L))