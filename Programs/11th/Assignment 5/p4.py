n=int(input('Enter a range '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n*j,end=' ')
    print()
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(' ',end='  ')
    for k in range(1,n-i+2):
        print(n*k,end=' ')
    print()
