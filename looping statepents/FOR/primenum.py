num=10
for i in range(1,num):

    for j in range(2,i):
        if (i%j) ==0:
            break
    else:
            print(i)
#prime check
flag=0
for i in range(2,num//2):
    if num%i==0:
        flag=1
if flag==0:
    print("prime")
else:
    print("not prime")
