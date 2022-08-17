def push(arr,top,x):
    arr.append(x)
    top+=1
    return top


def pop(arr,top):
    if top==-1 or top==None:
        print('the array is empty')
    else:
        x=arr.pop()
        top-=1
        if top==-1:
            top=None
        return x,top
    return
