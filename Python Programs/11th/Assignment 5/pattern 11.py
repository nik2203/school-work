n=int(input('Enter a range '))
x=n
for i in range(1,n+1):
    for m in range(1):
        print('#'*n,end='')
        n-=1
    for j in range(1,i+1):
        print(j,end='')
    for k in range(i-1,0,-1):
        print(k,end='')
    for l in range(1):
        print('#'*x,end='')
        x-=1
    print()
