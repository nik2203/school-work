def sum_sq(n,start=1,s=0):
    s+=start**2
    if start<n:
        sum_sq(n,start+1,s)
    else:
        print(s)


n=int(input('enter the limit '))
sum_sq(n)
