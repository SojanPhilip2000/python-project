names=["sojan","sachin","amma","pappa"]
new=[x for x in names if "n" in x]
print(new)
new1=[]
for j in names:
    if "n" in j:
        new1=j
        print(new1)