# read
# write
# append

# read

f=open('example.txt','r')
for i in f:
    print(i)

# to avoid the line space in between the two words strip the line break
f=open('example.txt','r')
for i in f:
    d=i.rstrip('\n')
    print(d)