#Perfect No.
n=int(input('enter a number '))
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
    else:
        continue
if s==n:
    print(n,'is a perfect no. ')
else:
    print(n,'is not a perfect no. ')
n=int(input('enter range '))
for i in range(6,n+1):
    s=0
    for j in range(1,i+1):
        if i%j==0:
            s+=j
        else:
            continue
    if s==i:
        print(i,'is a perfect number')
    else:
        continue
