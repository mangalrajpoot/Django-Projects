#Decorators: It is a function that accept function as a argument
# and return a function
# It takes result of function,modifies the results and return it.
# In Decorators, functions are taken as the argument into another 
# function and then called inside wrapper function.
#We use @function_name to specify a decorator to be applied on another
# function 

def decor(func):
    def inner():
        print("Before implementing!!")
        func()
        print("After Implementing!!")
    return inner

@decor
def func1():
    print("Hello")

# result = decor(func1)    
# result()

func1()

#------------------------------------
def decor2(func):
    def inner():
        val=func()
        return val+12
    return inner

def decor3(func):
    def inner():
        val=func()
        return val+20
    return inner 

@decor2
@decor3
def sum():
    return 12
print(sum())

# result1 = decor2(sum)
# print(result1())
#===============================
# result1 = decor2(decor3(sum))
# print(result1())



