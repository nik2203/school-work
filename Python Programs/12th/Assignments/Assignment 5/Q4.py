import csv

#a
year=input('enter year ')

print('The Robert diNero movies from '+year+' are:\n')

l=[]
l1=[]

with open('diNero.csv','r') as fh:
    data=csv.reader(fh)
    for i in data:
        l1.append(i)
    for i in range(len(l1)-1):
        l.append(l1[i][1])
        if l1[i][0]==year:
            print(l1[i][2])
    #b
    mini=min(l[1:])
    maxi=max(l[1:])
    lowest=[]
    highest=[]
    for i in l1:
        if i[1]==mini:
            lowest.append(i)
        if i[1]==maxi and i[1]!='   Score':
            highest.append(i)
    print('His highest rated movie(s) is/are:\n',highest,sep='\n')
    print('His lowest rated movie(s) is/are\n',lowest,sep='\n')
    


with open('diNero.csv','a') as fh:
    rows=[["2015","    60","Joy"],["2015","    26","Heist"],["2015","  61","The Intern"]]
    writer=csv.writer(fh)
    writer.writerows(rows)