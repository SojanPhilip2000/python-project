a=511
b=1
c=61
if a>b:
    if a>c:
        print("a is greater")
    elif b>c:
        print("b is greater")
    else:
        print("c is greater")
elif b>c:
    print("b is greater")
else:print("c is greater")

if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")