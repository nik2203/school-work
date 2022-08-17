#Assignment 5
n=int(input('enter range '))
for i in range(1,n+1):
    print('*'*i)
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(' ',end=' ')
    for k in range(i):
        print('*',end=' ')
    print()

#2
n=int(input('enter range '))
for i in range(n,0,-1):
    for j in range(n-i+1):
        print(i,end='')
    print()

for i in range(n,0,-1):
    for j in range(i):
        print(' ',end=' ')
    for k in range(n-i+1):
        print(i,end=' ')
    print()

#3
n=int(input('enter range '))
for i in range(1,n+1):
    for j in range(n-i+1,n+1):
        print(j,end='')
    print()

for i in range(1,n+1):
    for j in range(n-i+1):
        print(' ',end=' ')
    for k in range(n-i+1,n+1):
        print(k,end=' ')
    print()

#6
n=int(input('enter range '))
for i in range(0,n):
    for j in range(i+1,n+1):
        print(j,end='')
    print()

for i in range(0,n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(i+1,n+1):
        print(k,end=' ')
    print()
