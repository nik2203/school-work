n=int(input('Enter a range '))
x=int(input('Enter a number '))
s=1
for i in range(2,n+1):
    s+=x**i
print(s)
