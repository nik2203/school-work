n=int(input('Enter a range '))
for i in range(n,-1,-1):
    for j in range(n-i,0,-1):
        print(' ',end='')
    print('x'+' '*i*2+'x')
print(' '*n+'x')
for l in range(0,n+1):
    for m in range(0,n-l):
        print(' ',end='')
    print('x'+' '*l*2+'x')
