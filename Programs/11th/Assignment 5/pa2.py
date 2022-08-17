n=int(input('Enter a range '))
for i in range(n,0,-1):
    for j in range(n-i+1,0,-1):
        print(i,end=' ')
    print()
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(' ',end=' ')
    for k in range(n,i-1,-1):
        print(i,end=' ')
    print()
