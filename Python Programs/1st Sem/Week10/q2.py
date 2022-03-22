import functools as fc

#a
l=['hi','as12aas','12asda','sdfw231vx','44ad21','asdt5']
print(list(filter(lambda x: x if x[0].isdigit()==False else None,l)))

#b
l=[12,12313,453,7534,5232,7584,9234,2341]
print(fc.reduce(lambda x,y: x if x>y else y,l))

#c
l=[(2,4),(6,3),(8,2),(10,5),(6,5),(7,2)]
print(list(filter(lambda x: x if x[0]%x[1]==0 else None,l)))