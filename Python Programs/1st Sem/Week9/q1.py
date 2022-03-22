def counter():
    count=0
    def increment():
        nonlocal count
        count+=5
        return count
    return increment

co=counter()
n=int(input('Enter number of times to increment\n'))
for i in range(n):
    c=co()
    print(c)