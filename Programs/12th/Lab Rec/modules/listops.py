#Q18

def ar_trav(ar):
    if len(ar)==0:
        print('list is empty')
    else:
        for i in range(len(ar)):
            print(ar[i])
    return

def ar_search(ar,x):
    if len(ar)==0:
        print('the element cannot be in the list as it is empty')
    else:
        ind=[]
        for i in range(len(ar)):
            if ar[i]==x:
                ind.append(i+1)
        if len(ind)==0:
            print('the element is not in the list')
        else:
            print('The element was found at positions:',ind)
    return

    
#function to determine whether a list contains only unique values or not
#allows one to determine which list updating function to use.
def is_un(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
        else:
            continue
    if l==l1:
        print('the list has only unique elements')
    else:
        print('the list has duplicate elements')


def l_up_nonun(ar,x,r,u):
    if len(ar)==0:
        print('The array is empty')
        return
    else:
        i=0
        flag=0
        while i<=u:
            if ar[i]==x:
                ar[i]=r
                flag=1
            i+=1
        print('successfully replaced')
    if not flag:
        print('not found')
    return
            
def l_up_un(ar,x,r,u):
    if len(ar)==0:
        print('the list is empty')
    else:
        for i in range(len(ar)):
            if ar[i]==x:
                ar[i]=r
            else:
                continue
        print('replaced')
    return
        

def ins_un(ar,x,u):
    if u==len(ar)-1:
        print('the array is full')
    if len(ar)==0:
        ar[0]=x
    else:
        ar[u+1]=x
        u=u+1
    return


def ins_so(ar,x,u):
    if u==len(ar)-1:
        print('the array is full')
    elif len(ar)==0:
        ar[0]=x
    else:
        i=u
        while (x<=ar[i] and i>=0):
            ar[i+1]=ar[i]
            i-=1
        ar[i+1]=x
        u+=1
    return

def del_arr(ar,x,u):
    if len(ar)==0:
        print('the array is empty')
    pos=-1
    i=0
    while pos==-1 and i<=u:
        if ar[i]==x:
            pos=i
        else:
            i+=1
    if pos==-1:
        print('element not present')
        return
    else:
        pos=pos+1
        for i in range(pos,u+1):
            ar[i]=ar[i+1]
        u-=1
    return

def bin_sear(l,u,ar,x):
    while l<u:
        mid=(l+u)//2
        if ar[mid]==x:
            print('Element found at index number',mid)
            return
        elif ar[mid]>x:
            u=mid-1
        elif ar[mid]<x:
            l=mid+1
    print('element not found')
    return

def mer_un(ar1,ar2,u1,u2):
    ptr1=0
    ptr2=0
    ptr3=0
    ar3=[]
    while (ptr1<u1):
        ar3[ptr3:]=[ar1[ptr1]]
        ptr1+=1
        ptr3+=1
    while (ptr2<u2):
        ar3[ptr3:]=[ar2[ptr2]]
        ptr2+=1
        ptr3+=1
    u3=ptr3-1
    print(ar3)
    return u3

def mer_sor(ar1,ar2,u1,u2):
    ptr1=0
    ptr2=0
    ptr3=0
    ar3=[]
    while(ptr1<u1 and ptr2<u2):
        if ar1[ptr1]<ar2[ptr2]:
            ar3[ptr3:]=[ar1[ptr1]]
            ptr1+=1
            ptr3+=1
        else:
            ar3[ptr3:]=[ar2[ptr2]]
            ptr2+=1
            ptr3+=1
    while(ptr1<u1):
        ar3[ptr3:]=[ar1[ptr1]]
        ptr3+=1
        ptr1+=1
    while(ptr2<u2):
        ar3[ptr3:]=[ar2[ptr2]]
        ptr3+=1
        ptr2+=1
    print(ar3)
    return
    