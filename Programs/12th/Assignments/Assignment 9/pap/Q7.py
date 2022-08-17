def enq(arr,front,rear,x):
    if front==None or front==-1:
        arr[0:]=[x]
        front=rear=0
    else:
        arr.append(x)
        rear+=1
    return

def deq(arr,front,rear):
    if front==-1 or front==None:
        print('queue is empty')
    if front==rear:
        print(arr.pop(front))
        front=rear=None
    else:
        print(arr.pop(front))
    return
