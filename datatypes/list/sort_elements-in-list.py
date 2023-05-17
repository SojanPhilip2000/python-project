"""a=[]
limit=5
for i in range(limit):
    value=int(input("enter the values"))
    a.append(value)
print(a)
for i in range(limit-1):
        if a[i] > a[i+1]:
            temp=a[i+1]
            a[i+1]=a[i]
            a[i]=temp
        else:
            pass
print(a)"""

a=[]
limit=5
for i in range(limit):
    value=int(input("enter the values"))
    a.append(value)
print(a)
for i in range(limit):
    for j in range(i+1,limit-1):
        if a[i] > a[j]:
            temp=a[j]
            a[j]=a[i]
            a[i]=temp
        else:
            continue
print(a)