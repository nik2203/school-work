from random import shuffle

with open("SRN.txt",'r') as fd:
    f = fd.read()
    f = f.lower()

with open("SRN.txt","w") as fd:
    fd.write(f)

'''
print("he:",f.count('he'),'\n'+
      'h:',f.count('h'),'\n'+
      'ed:',f.count('ed'),'\n'+
      'oo:',f.count('oo'),'\n'+
      'a',f.count('a'),'\n'+
      'as',f.count('as'),'\n')


with open("SRN.txt",'r') as fd:
    f = fd.read()
    for i in ['he','h','ed','oo','a','as']:
        print(f.replace(i, '\033[44m{}\033[0m'.format(i)),end="\n\n")

'''

def gen_key(alphabet_string):
    l = list(alphabet_string)
    shuffle(l)
    return ''.join(l)


plain = f
cipher = ''
decipher = ''
alpha = 'abcdefghjiklmnopqrstuvwxyz'
key = gen_key(alpha)

for i in range(len(plain)):
    if not (plain[i].isalpha()):
        cipher += plain[i]
    else:
        ind = alpha.index(plain[i])
        cipher += key[ind]

for i in cipher:
    if not(i.isalpha()):
        decipher += i
    else:
        ind = key.index(i)
        decipher += alpha[ind]

print(cipher)
print('\n')
print(decipher)