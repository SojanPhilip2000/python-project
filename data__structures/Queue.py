queue=[]
size=int(input("enter the limit: "))
c=0
def enqueue():
    global c
    if c>=size:
        print("sorry, queue is full")
    else:
        e=int(input("enter the element: "))
        queue.append(e)
        print(queue)
        c+=1
def dequeue():
    global c
    if c<1:
        print("sorry, nothing left")
    else:
        del queue[0]
        #queue.remove(queue[0])
        c=c-1
        print(queue)
while True:
    opt=int(input("entr the ooptiion \n 1. enqueue \n 2. dequeue"))
    if opt ==1:
            enqueue()
    else:
            dequeue()