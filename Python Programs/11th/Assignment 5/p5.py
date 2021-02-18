x=int(input('Enter a range '))
for i in range(x,0,-1):
    print('*'*i)
for i in range(1,x+1):
    for j in range(i):
        print(' ',end='')
    for k in range(x-i+1):
        print('*',end='')
    print()
