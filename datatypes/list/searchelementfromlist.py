a=[]
limit=int(input("enter the limit"))
for i in range(0,limit):
    value=int(input("enter the value"))
    a.append(value)
    a[i]=value
print(a[:])
for i in range(0,limit):
    if a[i]==3:
        print("3 found")
    else:
        print("not found")

"""a=[]
for i in range(5):
    a[i]=1
print(a)"""