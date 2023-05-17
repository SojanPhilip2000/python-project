num1=int(input("enter the number: "))
if num1<0:
    raise Exception("negative error")
else:
    print(num1+10)