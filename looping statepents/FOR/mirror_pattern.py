n=6
for i in range(n):
    for j in range(1,n):
        print(end="  ")
    n=n-1

    for j in range(i):
        print("*",end=" ")
    print()