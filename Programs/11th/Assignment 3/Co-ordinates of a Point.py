#Co-ordinates of a point
x=float(input('Enter x co-ordinate '))
y=float(input('Enter y co-ordinate '))
if x==0 and y==0 :
    print('The point is on origin')
elif x==0 :
    print('The point is on the y-axis')
elif y==0:
    print('The point is on the x-axis')
elif x>0 and y>0:
    print('The point is in the 1st quadrant')
elif x<0 and y>0:
    print('The point is in the 2nd quadrant')
elif x<0 and y<0:
    print('The point is in the 3rd quadrant')
elif x>0 and y<0:
    print('The point is in the 4th quadrant')
