def shift_un(ar,n):
    j=0
    for i in range(n) : 
        if ar[i]<0: 
            t=ar[i] 
            ar[i]=ar[j] 
            ar[j]=t
            j+=1
    return ar 

def shift_so(ar,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if ar[j]>ar[j+1]: 
                ar[j],ar[j+1]=ar[j+1],ar[j]
    return ar




ar=eval(input('enter an array containing both negative and positive elements '))
n=len(ar)
x=int(input('do you want it to b:\n'
            '1. sorted\n'
            '2. unsorted\n'))
if x==1:
    print(shift_so(ar,n))
if x==2:
    print(shift_un(ar,n))
