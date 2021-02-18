#1
n=int(input('enter no. '))
for i in range(n+1):
    print('*'*i)
for i in range(n,-1,-1):
    print(' '*i,end='')
    print('*'*(n-i))

#2
n=int(input('enter a no. '))
for i in range(n):
    for j in range(-1,i):
        print(n-i,end='')
    print()
for i in range(n):
    for j in range(n,i,-1):
        print(' ',end='')
    for k in range(-1,i):
        print(n-i,end='')
    print()

#3
