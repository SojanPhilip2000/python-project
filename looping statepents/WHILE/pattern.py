num = 5
i=1
while i<=num:
    j=1
    while j<=i:
        print("*", end=" ")
        j=j+1
    print()
    i=i+1

for i in range(num):
    for j in range(i):
        print(end="*")