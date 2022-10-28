def seive(n):
    comp_no=[]
    for i in range(2,n+1):
        if i not in comp_no:
            print(i)
            for j in range(i*i,n+1,i):
                comp_no.append(j)

n=int(input('Enter the range to find prime numbers\n'))
seive(n)