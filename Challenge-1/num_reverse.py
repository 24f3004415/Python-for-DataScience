# % is use to extract last digit 
# // (floor division) is use to remove last digit

# i = 1
# while i<=5:
#     print("Hello World!!!")
#     i+=1

# j = 10
# while j>=1:
#     print(j)
#     j -= 1



# is_not_zero = True
# while is_not_zero:
#     i = int(input("enter a number: "))

#     if i == 0:
#         print("While loop break...BYE!!!")
#         is_not_zero = False


# HomeWork
# you have to input untill you found a numberwhich is divisble by both 3&5.

is_divisble_by_3_and_5 = True

while is_divisble_by_3_and_5:
    i = int(input("enter a number: "))

    if i %3 == 0 and i%5== 0:
        print("While loop break...BYE!!!")
        is_divisble_by_3_and_5 = False
