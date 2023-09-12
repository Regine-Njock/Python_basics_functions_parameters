
    
# def getParity(a, b):
    
#     # x=a%2==0
#     # return x

#     y=type(b)==int
#     return y
       
    
# print(getParity(-2, 'number'))
def getParity(param1, param2):
    
        # new_param1 = type(param2)== int
        # new_param2 = type(param2)== str
        # new_tuple=(new_param1,new_param2)
    
        # return new_tuple
    if param1%2==0 and param2=='even':
        return True
    elif param1%2!=0 and param2=='odd':
        return True
    elif param2!='even'and param2!='odd':
     return 'Parity indicated is unknown'
    else:
        return False

print(getParity(2,'even'), getParity(1, 'even'))
print(getParity(9, 'even'), getParity(7, 'odd'))
print(getParity (1, 'even'), getParity(4, 'even'))
print(getParity(-2, 'number'))

