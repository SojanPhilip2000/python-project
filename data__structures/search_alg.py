l=[65,545,654,624,32,1,495,4,6,979,31,64,111,544,4,46,45,]
def linear_search(num):
    for i in l:
        if i==num:
            print("found")
            break
        else:
            continue
linear_search(64)