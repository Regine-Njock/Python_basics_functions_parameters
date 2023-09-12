
def isOdd(number):
    a = number%2 !=0  ###this will return true or false
    return a
    #return number%2 !=0  ###another way of doing it
    
def isEven(number):
    b = number%2 ==0  ### this will return true or false
    return b
print(isOdd(1), isEven(1))
print(isOdd(657842), isEven(657842))
print(isOdd(0), isEven(0))

