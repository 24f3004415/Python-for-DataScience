# *args --> works on tuples
def add(*chacha):
    print(type(chacha))
    print(sum(chacha))

add(1,2,3,4,5,6,7,8,9,0,5)

# **Kwargs() --> dictionary ka form
# keywords argument

sample = lambda name,gender : print(name,gender)
sample(name = "Mohit",gender = "Male")

def info(**Modiji):
    for key,value in Modiji.items():
        print(key,value)

info(name = "Rahul", age= 21, gender = "ND")


# LAMBDA FUNCTION
# keyword-->lambda
# SYNTAX--> lambda parameter:expression

