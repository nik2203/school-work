import json
x=input('enter a string ')
d={}
for i in range(len(x)):
    if x[i] not in d:
        d[x[i]]=1
    else:
        d[x[i]]+=1
print(json.dumps(d,indent=1))
