def base():
    x=int(input('Enter the base\n'))
    def nroot():
        n=int(input('Enter which root to find\n'))
        return x**(1/n)
    return nroot

r=base()
res=r()
print(round(res,3))
