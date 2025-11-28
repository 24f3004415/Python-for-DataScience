# Loopcontrolstatements
# Python  gives us  some  tools  to control how loops  behave  & a  classical  example  of them are 2 statement - break & continue.

# The break keyword:
# It stops the loop immediately.


#Break for multiple of 6
i=1
while i<= 10:
    if(i%6 ==0):
        break
    print(i)
    i+=1
#output:1,2,3,4,5


# The continue keyword:
#It skips the rest of the current iteration and moves to the next one.

#Skip multiples of 3
i=0
while(i<10):
    i+=1
    if(i%3==0):
        continue
    print(i)
#output:1,2,4,5,7,8,10