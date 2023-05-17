row=5
for i in range(row):
    for j in range(row):
        print(i,j,"   ",end=" ")
    print()
m=row

for i in range(row):
    for j in range(row):
        if i==0 or j==row-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


for i in range(row):
    for j in range(m-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
    for j in range(i):
        print("*",end=" ")