def seive(n):#DEFINING FUNCTION SEIVE
    comp_no=[]#INITIALIZING EMPTY LIST
    for i in range(2,n+1):#FOR LOOP 
        if i not in comp_no:#INITIALIZING IF CONDITION TO ADD TO LIST 
            print(i)
            for j in range(i*i,n+1,i):
                comp_no.append(j)#APPEND PRIME NUMBERS

n=int(input('Enter the range to find prime numbers\n'))
seive(n)#CALLING FUNCTION