def upper(mat,n):
    for i in range(n): 
        for j in range(n):
            if (i>j):
                print(' ',end=' ')
            else: 
                print(mat[i][j],end=' ') 
        print()
def lower(mat,n):
    for i in range(0,n):
        for j in range(i+1):
            print(mat[i][j],end=' ')
        print()


mat=eval(input('enter a n x n  matrix '))
n=len(mat)
x=int(input('do you want to see:\n'
            '1. the upper half\n'
            '2. the lower half\n'))
if x==1:
    upper(mat,n)
if x==2:
    lower(mat,n)
