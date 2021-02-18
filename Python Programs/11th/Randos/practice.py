import math
import random
#Assignment 2
x=2
y=3
z=4
p=1.5
print('1',5&3)
print('2',5^3)
print('3',5|3)
print('4',not 5)
print('5',~5)
print('6',not p)
print('7',5<3>4)
print('8',not(x>y))
print('9',x-y*2>y*2 or not y*p>y)
print('10',1<x<10)
print('11',10<x<20)
print('12',x<10<x*10<100)
print('13',10>x<=9)
print('14',5==x>4)

#1
r=int(input('Enter radius of circle '))
print('The area of the circle is',math.pi*r**2,' and the circumference is',2*math.pi*r)

#2
p=int(input('Enter principal amount '))
r=int(input('Enter interest rate '))
t=int(input('Enter time period in years '))
print('Simple interest is',p*r*t)

#3
s1=int(input('Enter length of side 1 '))
s2=int(input('Enter length of side 2 '))
s3=int(input('Enter length of side 3 '))
sp=(s1+s2+s3)/2
print('The area of the triangle is',(sp*(sp-s1)*(sp-s2)*(sp-s3))**(1/2))

#4
m1=int(input('Enter marks in subject 1 '))
m2=int(input('enter marks in subject 2 '))
m3=int(input('enter marks in subject 3 '))
m4=int(input('enter marks in subject 4 '))
m5=int(input('enter marks in subject 5 '))
m=int(input('enter max marks '))
avg=(m1+m2+m3+m4+m5)/5
print('the average is',avg,' the percentage is',(avg/m)*100)

#5
l=int(input('enter length '))
b=int(input('enter breadth '))
print('The area is',l*b,'the perimeter is',2*(l+b))

#6
sn=input('enter student name ')
sc=input('enter student class ')
srn=input('enter student roll no. ')
ss=input('enter student section ')
print(sn+' is in '+sc+ss+' and their roll no. is '+srn)

