a={1:"goya",2:"oppa",3:"pooopi"}
b={"name":"sojan","age":7,"job":"pooopi"}
print(a)
print(b)
print(a[1])
print(b["job"])
c={"even":[2,4,6,8,10],"odd":[1,3,5,7,9]}
print(c["even"])
print(c.keys())
print(c.values())
print(c.items())
for i in b:
    print(i)
for i in b.values():
    print(i)
key=[]
value=[]
for i in b:
    key.append(i)
    value.append(b[i])
print(key)
print(value)
for i in b:
    key.append(i)
print(key)