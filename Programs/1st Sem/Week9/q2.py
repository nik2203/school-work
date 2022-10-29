def base():#defining function base
    x=int(input('Enter the base\n'))#base initialization
    def nroot():
        n=int(input('Enter which root to find\n'))#input is of type int and declaring the root
        return x**(1/n)#operation statement
    return nroot

r=base()
res=r()
print(round(res,3))#function calling
