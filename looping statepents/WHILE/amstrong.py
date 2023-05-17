num=153
sum=0
#for i in num:
    #sum=sum+(i**(len(num))
#print(sum)
temp=num
count=num
i=0
while(count>0):
    i=i+1
    count=count//10
print(i)
while temp>0:
    digit=temp%10
    sum=sum+digit**i
    temp=temp//10
print(sum)
if num==sum:
    print("amstrong")
else:
    print("not")


