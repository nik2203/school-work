def phone_no(name,b,t):
    if t>=b: 
        mid=b+(t-b)//2
        if (l[mid][0]).lower()==name: 
            return l[mid][1]
        elif (l[mid][0]).lower()>name: 
            return phone_no(name,b,mid-1) 
        else: 
            return phone_no(name,mid+1,t)
    else:
        return 'The person does not have a registered phone number'


l=[('Asha',9823495001),('Dhanush',9712334031),('Mahika',8334656893),('Vikas',8319564967)]
n=input('enter the name of the person ')
print(phone_no(n.lower(),0,len(l)-1))
