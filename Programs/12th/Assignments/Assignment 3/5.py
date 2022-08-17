from datetime import date

date1=input('enter the current date in (yyyy/mm/dd) format ')
date2=input('enter the date in the same format ')
d1=tuple(date1.split('/'))
d2=tuple(date2.split('/'))
date1=date(int(d1[0]),int(d1[1]),int(d1[2]))
date2=date(int(d2[0]),int(d2[1]),int(d2[2]))
print((date2-date1).days,'days')
