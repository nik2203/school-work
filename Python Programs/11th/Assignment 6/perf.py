n=int(input('Enter a range '))
a=2
x=0
while(x**2<=n):
    for i in range(1,n//2):
        if a%i==0:
            x+=i
    if x==a:
        print(a,'is a perfect no.')
    else:
        a+=1
        x=0
