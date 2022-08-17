n=int(input('Enter a number '))
ctr=0
if n==1 or n==0:
    print('Invalid input')
for i in range(2,n):
    if n%i==0:
        ctr+=1
        break
    else:
        ctr=0
if ctr>0:
    print('It is not a prime number')
else:
    print('It is a prime number')
