f=open('filedata.txt','r')
l=[]
for i in f:
    data=i.rstrip("\n").split(" ")
    l.extend(data)
print(l)