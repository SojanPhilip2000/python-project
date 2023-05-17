#stack  last in first out
#size
#push #pop #display

stack=[]
c=0
size=int(input("enter the size: "))

def push():
    global c
    if c>=size:
        print("stack is full")
    else:
        e=int(input("enter the element: "))
        stack.append(e)
        print(stack)
        c+=1
def pop():
    global c
    if c < 1:
        print("stack is empty")
    else:
        stack.pop()
        print(stack)
        c-=1
while True:
    opt=int(input("entr the ooptiion \n 1. push \n 2. pop"))
    if opt ==1:
            push()
    else:
            pop()


