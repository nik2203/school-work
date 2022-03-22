'''2.Write a function to mimic filter - called myfilter.
Test this with the following calls. Given a list of strings,
remove all strings having first character as digit.'''

def myfilter(it):
    for i in it:
        if i[0].isdigit():
            it.remove(i)
        else:
            pass
    return it

l=['1asdbf','ashdf23','hukdifg','65knkjn','kjdhis','9askd']
print('The list before filtering is',l)
print('The list after filtering is',myfilter(l))