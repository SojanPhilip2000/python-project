def valuecheck(function):   #function = sub
    def swap(a,b):          #a=3,b=6
        if a<b:
            a,b=b,a         #a=6,b=3
            
            return function(a,b)
        else:
            return function(a,b)
    return swap

@valuecheck
def subtract(num1,num2):
    return num1-num2
print(subtract(6,3))
print(subtract(3,6))

@valuecheck
def devide(num1,num2):
    return num1//num2
print(devide(6,3))
print(devide(3,6))
