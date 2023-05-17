list1=["python","java","css",55,76,908]
print(list1)
for i in list1:
    print(i)
print(list1[1])
print(list1[1:5])
# using addition operator
a=["sojan","sachin","pottan","vattan"]
b=a+list1
print(b)

c=["kol","lop"]
a.append(c)
print(a)

x=["a","b","c","d",'e',1]
y=[1,2,3,4,5]
x.extend(y)
print(x)


del x[0]
print(x)

y.remove(1)
print(y)

x.clear()
print(x)

#del y
#print(y)
e=list([9,8,76,45])
print(e)

