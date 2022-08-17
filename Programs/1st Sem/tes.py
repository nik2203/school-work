'''n=int(input('Enter seconds since midnight'))
hours=(n//3600)%24
print(hours)
minutes=(n//60)%(60*24)
print(minutes)

celsius=int(input())
faren=(celsius*1.8)+32
print(faren)

from math import sqrt
x1=2
y1=5
x2=6
y2=7
print(sqrt(((x1-x2)**2)+((y1-y2)**2)))


h1=int(input())
m1=int(input())
s1=int(input())
t1=(h1*3600)+(m1*60)+s1
h2=int(input())
m2=int(input())
s2=int(input())
t2=(h2*3600)+(m2*60)+s2
print(t2-t1)
'''
dist=int(input('enter dist'))
print(dist*1000,dist*100000,dist*3280.84,dist*39370.1)
