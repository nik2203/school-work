def pasc(n):
    for i in range(0,n):
        for j in range(0,i+1): 
            print(bin_co(i, j),' ', end = "") 
        print() 
def bin_co(n, r) : 
    base=1
    if (r>n-r) : 
        r=n-r 
    for i in range(0, r): 
        base*=(n-i) 
        base//=(i+1)      
    return base

x=int(input('enter a number '))
pasc(x)
