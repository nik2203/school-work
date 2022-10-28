def counter():#This is a counter function
    count=0#initializing count variable to 0
    def increment():#nested function definition
        nonlocal count#initialoizing count to  a non local variable
        count+=5#count operation 
        return count
    return increment

co=counter()
n=int(input('Enter number of times to increment\n'))
for i in range(n):#calling function using for loop
    c=co()
    print(c)