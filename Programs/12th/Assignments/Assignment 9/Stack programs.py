from pap import Q1 as pap


#undo and redo functions for Q6
def undo(top,arr,text): #takes in top value, undo stack and text stack
    pap.push(re_st,top,text)
    text=pap.pop(arr,top)[0]
    return text
def redo(top,arr,text):
    pap.push(un_st,top,text)
    text=pap.pop(arr,top)[0]
    prev=text
    return text



state=input('Do you want to start (y/n)\n')
while state=='y' or state=='Y':
    prog=int(input('What do you want to do:\n'
                   '1. Perform stack operations\n'
                   '2. Reverse a string\n'
                   '3. Convert a decimal number to its binary\n'
                   '4. Convert and evaluate an infix to postfix\n'
                   '5. Try a simple text editor with undo and redo functionality?\n'))
    #Q2
    if prog==1:
        subp=int(input('What do you want to do:\n' #subp- sub program
                       '1. Try popping on an empty stack\n'
                       '2. Push 2 elements into a stack\n'
                       '3. Pop an element from a stack\n'))
        if subp==1:
            arr=eval(input('Enter an array\n'))
            pap.pop(arr,-1)
        if subp==2:
            arr=eval(input('Enter an array\n'))
            top=len(arr)-1
            for i in range(2):
                el=input('Enter element to push\n')
                pap.push(arr,top,el)
                top+=1
            print(arr)
        if subp==3:
            arr=eval(input('Enter an array\n'))
            top=len(arr)-1
            pap.pop(arr,top)
            top-=1
            print(arr)
    #Q3
    if prog==2:
        x=input('Enter a string\n')
        arr=[0 for i in x]
        u=len(arr)
        top=-1
        for i in x:
            pap.push(arr,top,i)
            top+=1
        for i in x:
            j=pap.pop(arr,top)
            print(j[0],end='')
            top-=1
    #Q4
    if prog==3:
        x=int(input('Enter a number\n'))
        arr=[]
        top=-1
        while x>0:
            pap.push(arr,top,x%2)
            x//=2
            top+=1
        while top>-1:
            print(pap.pop(arr,top)[0],end='')
            top-=1
    #Q5
    if prog==4:
        op=['**','*','/','//','%','+','-']
        prior={'**':1,'*':2,'/':2,'//':2,'%':2,'+':3,'-':3}

        x=list(input('enter an expression \n'))
        arr=[]
        out=[]
        ress=[]
        top=-1
        rt=-1
        for i in x: #Conversion
            if i.isalnum(): #checks to see if element is variable/number
                out.append(i)
            elif i=='(':
                pap.push(arr,top,i)
                top+=1
            elif i in op:
                while len(arr)>0 and arr[top]!='(' and prior[arr[top]]<prior[i]:
                    out.append(pap.pop(arr,top)[0])
                    top-=1
                pap.push(arr,top,i) #appends all operators in stack to output before pushing in new operator
                top+=1
            elif i==')':
                while len(arr)>0 and arr[top]!='(': #appends all operators to output
                    out.append(pap.pop(arr,top)[0])
                    top-=1
                pap.pop(arr,top) #pops out bracket
                top-=1
        while len(arr)>0: #appends remaining elements to the output
            out.append(pap.pop(arr,top)[0])
            top-=1
        print(''.join(out),end='')
        for i in out: #Evaluation
            if i not in op: #checks if element isvariable/number
                pap.push(ress,rt,i) #pushes element into result stack
                rt+=1
            else: #if operator is encountered
                val1=pap.pop(ress,rt)[0] 
                rt-=1
                val2=pap.pop(ress,rt)[0]
                rt-=1 #takes out two of previously pushed elements to calculate their result
                if val1.isdigit() and val2.isdigit(): #if both elements are digits, calculates result
                    val3=eval(val1+i+val2)
                    pap.push(ress,rt,str(val3))
                    rt+=1
                else: #if one or neither of elements are digits, calculates result
                    val3=val1+i+val2
                    pap.push(ress,rt,val3)
                    rt+=1
        print('\n'+''.join(ress[::-1]),end='')
    #Q6
    if prog==5:
        un_st=[] #undo stack
        re_st=[] #redo stack
        utop=-1
        rtop=-1
        text=['Type Here']
        prev=text
        print('The text is currently',text)

        subs=input('Do you want to start (y/n)\n')
        while subs=='y' or subs=='Y':
            x=int(input('Do you want to:\n'
                    '1. Edit\n'
                    '2. Undo/Redo\n'
                    '3. Exit\n'))
            if x==1:
                text=eval(input('Enter your edit as a list\n'))
                pap.push(un_st,utop,prev)
                utop+=1
                prev=text
                print('The text is currently',text)
            if x==2:
                x1=int(input('Do you want to:\n'
                             '1. Undo\n'
                             '2. Redo\n'))
                if x1==1 and len(un_st)>0:
                    print('The text is now',undo(utop,un_st,text))
                    rtop+=1
                    utop-=1
                elif x1==1 and len(un_st)==0:
                    print('There is nothing to undo')
                if x1==2 and len(re_st)>0:
                    print('The text is now',redo(rtop, re_st,text))
                    rtop-=1
                    utop+=1
                elif x1==2 and len(re_st)==0:
                    print('There is nothing to redo')
                if x1==3:
                    break
    state=input('\nDo you want to continue (y/n)\n')
