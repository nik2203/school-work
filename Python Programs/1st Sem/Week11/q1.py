#Programs on functional programming
'''
1.Write a function mymap which takes a callback and an iterable, creates a list,
applies the callback to each element of the iterable and puts the result into list and returns the list.
mymap should mimic map. Test this with the following calls.

a)Create a list of square of odd numbers from 1 to n.

b)Given a list of words, return a list of words with ing appended to it.

c)Given a list of words, return a list of tuples having the word and its length.
'''
def mymap(f,it):
    l=[]
    for i in it:
        l.append(f(i))
    return l
#a
def sq_odd(n):
    return n**2

#c
def worlen(n):
    return (n,len(n))

ran=int(input('Enter range for squares\n'))
l=list(mymap(sq_odd, range(1,ran,2)))
print(l)

#b
worl=eval(input('Enter a list of words\n'))
l=list(mymap(lambda st: st+'ing',worl))
print(l)

worl=eval(input('Enter a list of words\n'))
l=list(mymap(worlen,worl))
print(l)