def myreduce(func, itera):#function which defines or works according to the reduce function
    it = iter(itera)
    val = next(it)
    for element in it:
        val = func(val, element)
    return val

l=[12,31,2,12,312,534,35,4,753,2,233,34,75,3,45]
#a
maxi=lambda x,y: x if x>y else y
print(myreduce(maxi,l))

#b
conc=lambda x,y: str(x)+str(y)
print(myreduce(conc,l))