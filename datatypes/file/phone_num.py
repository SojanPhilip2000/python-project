f1=open('phn_num.txt','r')
f2=open('valid_phone_num.txt','w')
for i in f1:
    n=i.rstrip("\n")
    if len(n)==10:
        f2.write(i)
