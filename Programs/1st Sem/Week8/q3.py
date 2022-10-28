#tower of hanoi
def toh(n,from1,to,aux):
    if n==1:
        print('Move ring 1 from',from1,'peg to',to,'peg')
        return
    toh(n-1,from1,aux,to)
    print('Move ring',n,'from',from1,'peg to',to,'peg')
    toh(n-1,aux,to,from1)

n=int(input('Enter number of rings\n'))
toh(n,'Left','Right','Middle')

#b
def powe(n,b1):
    if n==1:
        return b1
    else:
        return powe(n-1,b1*b)
b=int(input('Enter the base\n'))
n=int(input('Enter the power to which it is to be raised\n'))
print(powe(n,b))