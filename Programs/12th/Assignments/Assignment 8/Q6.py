def capit(ar):
    res=[]
    for i in ar:
        res.append(i.capitalize())
    return res

ar=eval(input('enter an array of words '))
print(capit(ar))
