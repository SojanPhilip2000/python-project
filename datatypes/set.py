a={"sojan","sachin","pottan",1,"vattan"}
print(a)
for i in a:
    print(i)
a.add("apppi")
a.update(["appikkuuss"])
print(a)

a.discard("apppi")
a.remove("appikkuuss")
print(a)
c={9,8,76,}
b={1,2,3,4,5}
# union method
print(a.union(b,c))
print(a|b)
# intersection method
print(a.intersection(b))
print(a&b)
#difference operation
print(a.difference(b))
print(a-b)
#symmetric difference
print(a.symmetric_difference(b))
print(a^b)

