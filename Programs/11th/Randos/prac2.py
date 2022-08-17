#Armstrong numbers
n=input('enter a 3 digit number ')
ctr=0
c=0
while ctr==0:
    for i in range(len(n)):
        c+=int(n[i])**3
    if c==int(n):
        ctr+=1
    else:
        break
if ctr==1:
    print('It is an armstrong number ')
else:
    print('It is not an armstrong number ')

for i in range(1,500):
    n=str(i)
    c=0
    for j in range(len(n)):
       c+=int(n[j])**3
    if c==i:
        print(c,end='\n')
    else:
        continue

#Factorial
n=int(input('enter a number '))
s=1
for i in range(1,n+1):
    s*=i
print(s,'is the factorial of',n)

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


