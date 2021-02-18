def unit_d(ar,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if str(ar[j])[-1]<str(ar[j+1])[-1]: 
                ar[j],ar[j+1]=ar[j+1],ar[j]
    return ar

ar=eval(input('enter an array of only positive integers '))
n=len(ar)
print(unit_d(ar,n))
