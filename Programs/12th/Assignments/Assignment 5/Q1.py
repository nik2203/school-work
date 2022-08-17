import pickle

countries=[['Afghanistan','Kabul','34.28N','69.11E'],['Albania','Tirane','41.18N','19.49E'],['Algeria','Algiers','36.42N','03.08E'],['Iceland','Reykjavik','64.10N','21.57W'],['India','New Delhi','28.73N','77.13E'],['Indonesia','Jakarta','06.09S','106.49E']]

fh=open('countries.dat','wb')
for i in countries:
    pickle.dump(', '.join(i)+'\n',fh)
fh.close()

#Question 2
with open('countries.dat','rb') as fh:
    l=[]
    while True:
        try:
            a=pickle.load(fh)
            l.append(a)
        except EOFError:
            break

x=input('enter country for country details ')
for i in l:
    if x in i:
        print(i)