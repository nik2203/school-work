def frac_sum(n,start=1,s=0):
    s+=1/start
    if start<n:
        frac_sum(n,start+1,s)
    else:
        print(s)

n=int(input('enter the limit '))
frac_sum(n)
