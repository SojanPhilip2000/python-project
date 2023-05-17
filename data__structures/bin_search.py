l=[5,19,6,12,45,1,3,99,8,35,9,65,78,7,15,123,4,44,]
l.sort()
e=2
print(l)

low=0
upper=len(l)

while low<upper:
    middle=(len(l)//2)
    if e==l[middle]:
            print("found")
            break
    elif e>l[middle]:

            l=l[middle:upper]
    else:

            l=l[low:middle]


