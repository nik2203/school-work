x=2
y=3
z=4
p=1.5
#1
print(5&3)
#2
print(5^3)
#3
print(5|3)
#4
print(not 5)
#5
print(~5)
#6
print(not p)
#7
print(5<3>4)
#8
print(not(x>y))
#9
print(x-y*2>y*2 or not y*p>y)
#10
print(1<x<10)
#11
print(10<x<20)
#12
print(x<10<x*10<100)
#13
print(10>x<=9)
#14
print(5==x>4)

#15
import math
r=int(input('enter radius of circle '))
print('The area is',int(math.pi*r**2),'and the circumference is',int(2*math.pi*r))

#16
p=int(input('Enter principal amount '))
t=int(input('Enter time period in years '))
r=int(input('Enter interest rate '))
print('The simple interest is',p*r*t,'and the final amount is',p+p*r*t)

#17
s1=int(input('enter side 1 '))
s2=int(input('enter side 2 '))
s3=int(input('enter side 2 '))
sp=(s1+s2+s3)/2
print('The area of the triangle is',int(math.sqrt(sp*(sp-s1)*(sp-s2)*(sp-s3))),'sq units')

#18

