n=int(input('Enter a range '))
for i in range(1,n+1):
    print('*'*i)
#Right align#
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(' ',end=' ')
    for k in range(i):
        print('*',end=' ')
    print()
