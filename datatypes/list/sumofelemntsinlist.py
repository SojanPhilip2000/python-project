a=[]
num = int(input("enter the value"))
summ=0

for i in range(0,num):
    value = int(input("enter the values"))
    a.append(value)
    summ=summ+a[i]
print(summ)

print(a[:])

sum=0
for i in a:
    sum=sum+i
    print(sum)