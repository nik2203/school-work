import math
#Sphere
r=int(input('Enter radius '))
area=4*math.pi*(r**2)
volume=(4/3)*math.pi*(r**3)
print('The surface area is '+str(area))
print('The volume is '+str(volume))


#Cylinder
rad=int(input('Enter radius '))
h=int(input('Enter height '))
carea=2*math.pi*rad*(h+rad)
cvolume=2*math.pi*(rad**2)*h
print('The total surface area is '+str(carea))
print('The volume is '+str(cvolume))

#Cone
radius=int(input('Enter radius '))
l=int(input('Enter slant length'))
height=int(input('Enter height '))
tsa=math.pi*radius*(l+radius)
covolume=(1/3)*math.pi*(r**3)
print('The surface area is '+str(tsa))
print('The volume is '+str(covolume))
