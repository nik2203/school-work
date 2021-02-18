def multiple(lim,start=1):
    print(3*start)
    if (start+1)*3<lim:
        multiple(lim,start+1)
    elif (start+1)*3==lim:
        print(lim)
    
n=int(input('enter the limit '))
multiple(n)
        
        
