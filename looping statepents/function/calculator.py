def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multipilication(a,b):
    return a*b
def division(a,b):
    return a/b
a= int(input("enter the first number:"))
print("choices are A.adiittion , B.subtraction, C.multipilication, D.devision")
choice= input("enter the choice:")
b= int(input("enter the second number:"))
if choice=="A":
    print(addition(a,b))
elif choice=="B":
    print(subtraction(a,b))
elif choice=="C":
    print(multipilication(a,b))
elif choice=="D":
    print(division(a,b))