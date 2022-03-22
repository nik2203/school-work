sl=[]
il=[]
fl=[]
cl=[]
ll=[]
tl=[]
dl=[]
bl=[]
sel=[]
l=eval(input('Enter a list of various data types\n'))
for i in l:
    if type(i)==str:
        sl.append(i)
    elif type(i)==int:
        il.append(i)
    elif type(i)==float:
        fl.append(i)
    elif type(i)==complex:
        cl.append(i)
    elif type(i)==list:
        ll.append(i)
    elif type(i)==tuple:
        tl.append(i)
    elif type(i)==dict:
        dl.append(i)
    elif type(i)==bool:
        bl.append(i)
    else:
        sel.append(i)
print('The list of strings is',sl,'the list of integers is',il,'the list of floats is',fl,'the list of complex numbers is',cl,'the list of lists is',ll,\
    'the list of tuples is',tl,'the list of dictionaries is',dl,'the list of booleans is',bl,'and the list of sets is',sel)