from pap import Q7 as endel




que=[]
front=rear=-1
state=input('Do you want to start? (y/n)\n')
while state=='y' or state=='Y':
    prog=int(input('Do you want to:\n'
                   '1. Work with program lists\n'
                   '2. Work with a list of words\n'))
    #Q8
    if prog==1:
        subs=input('Do you want to start (y/n)\n')
        while subs=='y' or subs=='Y':
            n=input('Do you want to: \n'
                '1. Add a process \n'
                '2. Execute the process \n'
                '3. Calculate Throughput \n')
            if n=='1':
                np=eval(input('Enter the new process as [\'Process ID\',Burst time] \n'))
                endel.enq(que,front,rear,np)
                front+=1
                rear=len(que)-1
            if n=='2' and len(que)>0:
                endel.deq(que,front,rear)
                print('Process has been executed')
                rear-=1
            elif n=='2' and len(que)==0:
                print('The queue is empty')
            if n=='3' and len(que)>0:
                tim=0
                for i in range(len(que)):
                    tim+=que[i][1]
                throu=tim/len(que)
                print(throu,'seconds is the throughput for the current queue')
            elif n=='3' and len(que)==0:
                print('There is nothing in the queue')
            subs=input('Do you want to continue with the program list? (y/n)\n')
    #Q9
    if prog==2:
        wordsalad=['elephant','cork','ocean','bat']
        front=0
        rear=len(wordsalad)-1
        print('The current queue of words is',wordsalad)
        subs=input('Do you want to start (y/n)\n')
        while subs=='y' or subs=='Y':
            x=input('Do you want to:\n'
                    '1. Add a word to the queue\n'
                    '2. Delete a word from the queue\n')
            if x=='1':
                new=input('Enter word to add to queue\n')
                endel.enq(wordsalad,front,rear,new)
                print('The queue is now',wordsalad)
                rear+=1
            if x=='2':
                endel.deq(wordsalad,front,rear)
                print('The queue is now',wordsalad)
                rear-=1
            subs=input('Do you want to continue with the word queue?(y/n)\n')
    state=input('Do you want to continue? (y/n)\n')

