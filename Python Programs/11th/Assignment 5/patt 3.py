n=int(input('Enter a range '))
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(j,end=' ')
    print()
for  i in range(n,0,-1):
    for j in range(i):
        print(' ',end=' ')
    for k in range(i,n+1):
        print(k,end=' ')
    print()
