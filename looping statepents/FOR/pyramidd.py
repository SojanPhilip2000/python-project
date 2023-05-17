n=10
for i in range(n//2+1):
    for j in range(n//2):
        print(end="  ")
    n=n-2

    for j in range(i):
        print("* ",end="  ")
    print()
