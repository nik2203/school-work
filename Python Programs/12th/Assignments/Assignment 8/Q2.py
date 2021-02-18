from func import listops

ar=[1,53,23,0,12,5,8,29,30,73]

x=int(input('what number do you want to find '))

sea=int(input('do you want to carry out a:/n'
          '1. linear search/n'
          '2. binary search/n'))
if sea==1:
    ar_search(ar,x)
if sea==2:
    l=int(input('what is the lower limit of the array '))
    u=int(input('what is the upper limit of the array '))
    bin_sear(l,u,ar,x)

